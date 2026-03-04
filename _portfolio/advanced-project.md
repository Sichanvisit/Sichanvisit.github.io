---
title: "Advanced Project"
date: 2026-02-28
priority: 1
excerpt: "제품 이미지와 텍스트 입력으로 광고 크리에이티브를 자동 생성하는 End-to-End AI 파이프라인"
header:
  teaser: /assets/images/profile.png
github_url: "https://github.com/codeitTeam5/SMB_GenMarketingContents"
project_dir: "C:/Users/bhs33/Desktop/project/Advanced_Project"
tech_stack:
  - Python
  - Computer Vision
  - LLM
  - Prompt Engineering
---
# 포트폴리오 작성 문서 (GitBlog 초안)

## 1. 프로젝트 한 줄 정의
상품 광고 제작의 수작업 병목을 줄인 자동 이미지 생성 스튜디오

## 2. 배경 및 문제 정의

## 배경
이 프로젝트는 업로드 이미지 1장을 받아 5단계 파이프라인으로 결과 이미지를 만든다.  
코드 기준으로 백엔드 핵심 모듈은 `core` 56개 파일, API/프론트/워커는 `app` 32개 파일로 분리됐다.  
API 라우트는 31개이며, 산출물 저장 구조는 `assets/renders/output` 3개 폴더로 고정됐다.

## 문제
기존 흐름은 생성 단계와 편집 단계를 분리하지 못해서 재생성 비용이 반복됐다.  
GPU 메모리 관리가 단계별로 일관되지 않아서 OOM이 직접 발생했다.  
레이어 좌표 기준이 혼재돼서 편집기 좌표와 생성기 좌표가 어긋났다.

| 문제 | 구체적 상황 |
|------|------------|
| 생성 단계 결합 | `/projects/init` 호출 한 번에 초기화와 생성이 함께 실행돼 실패 원인 분리가 어려웠다. |
| 메모리 병목 | 커밋 히스토리에 `OOM 터지는거 방지` 수정이 남아 있고, 코드에 VRAM 언로드 로직이 반복 추가됐다. |
| 좌표 불일치 | ratio 좌표와 px 좌표를 함께 받는 분기가 많아 레이어 위치 보정 코드가 누적됐다. |
| 관측 지표 부족 | `execution_time` 기록 필드는 존재하지만 워크스페이스에 실측 로그 파일이 없어서 운영 수치가 비어 있었다. |

## 3. 기술적 접근

### 3-1. 오케스트레이션 분리 (초기화/생성 분리)

**문제:**
초기화와 생성이 강결합돼 디버깅 단위가 불명확했다.

**접근:**
`Director.init_project`와 `Director.execute_project`를 분리했다.

**선택 이유:**
프로젝트 상태를 `manifest.json`에 저장하고 재시작 지점을 명시해야 재생성이 가능했다.

**구현:**
`StateManager`가 프로젝트 폴더와 manifest를 관리하고, `execute_project`가 상태를 읽어 후속 단계를 수행한다.

```python
state_mgr = StateManager(user_id, project_id)
state_mgr.init_project_structure()
...
state_mgr.save_manifest(manifest)
...
manifest = state_mgr.load_manifest()
result = self.generator.run_production_pipeline(manifest, state_mgr)
```

**결과:**
생성 실패 후 `/projects/{id}/generate` 또는 페이지 재생성 API로 재시작 경로가 분리됐다.

### 3-2. 5단계 파이프라인 고정과 단계별 시간 기록

**문제:**
단계별 실패 지점이 로그에서 분리되지 않아 병목 위치가 불명확했다.

**접근:**
컷아웃→배경생성→업스케일→후처리→텍스트 오버레이 5단계를 고정했다.

**선택 이유:**
각 단계를 독립 함수로 유지해야 우회 실행, 재생성, 단계 스킵이 가능했다.

**구현:**
각 단계 시작/종료를 `execution_history`에 남기고, `PerformanceTimer`로 초 단위 시간을 `execution_time`에 저장한다.

```python
with PerformanceTimer(logger, "step_2_flux_inference", page.execution_time):
    generated_image = flux_engine.generate(...)
...
page.execution_time['step_2_generation'] = round(duration_page, 2)
manifest.execution_history.append(
    f"[{get_kst_timestamp()}] 페이지 {page.page_number} 생성 완료 ({duration_page:.2f}초)"
)
```

**결과:**
파이프라인 단계별 처리시간, 실패 페이지, 중단 위치가 manifest 단위로 추적됐다.

### 3-3. VRAM 상주 전략과 경량 모델 언로드

**문제:**
무거운 모델 재로딩이 반복돼 지연과 OOM이 동시에 발생했다.

**접근:**
`VRAMHandler`를 싱글톤으로 두고 heavy/light 모델을 분리 관리했다.

**선택 이유:**
Flux·업스케일러처럼 로딩 비용이 큰 모델은 상주시켜야 처리 지연을 줄일 수 있었다.

**구현:**
`keep_heavy=True` 기본 전략으로 경량 엔진만 언로드하고 heavy 엔진 집합을 유지한다.

```python
if keep_heavy:
    keys_to_remove = [k for k in self._loaded_models.keys() if k not in self._current_heavy_models]
    for k in keys_to_remove:
        ...
        del self._loaded_models[k]
```

**결과:**
모델 교체 횟수가 줄었고, OOM 대응 로직이 `VRAMHandler`로 집중됐다.

### 3-4. LLM 이중화로 기획 단계 단절 방지

**문제:**
단일 LLM 의존 구조에서 API 실패 시 기획 단계가 중단됐다.

**접근:**
OpenAI 1순위, Gemini 2순위 failover 엔진을 구성했다.

**선택 이유:**
기획 단계 중단은 전체 파이프라인 중단으로 이어져 대체 경로가 필수였다.

**구현:**
`FailoverLLMEngine.generate`에서 OpenAI 예외 시 Gemini를 즉시 호출한다.

```python
if self.primary:
    try:
        return self.primary.generate(system_prompt, user_prompt, max_tokens)
    except Exception:
        logger.warning("즉시 Gemini로 긴급 이관")

if self.secondary:
    return self.secondary.generate(system_prompt, user_prompt, max_tokens)
```

**결과:**
기획 단계가 단일 공급자 장애에 묶이지 않았다.

### 3-5. 레이어 계산을 생성기에서 분리

**문제:**
생성 단계와 레이어 배치 로직이 섞여 좌표 버그 수정 범위가 넓어졌다.

**접근:**
`LayoutManager`를 별도 엔진으로 분리하고 z-index 규칙을 고정했다.

**선택 이유:**
편집기 렌더링과 생성기 좌표 해석을 동일 규칙으로 맞춰야 재렌더 품질이 유지됐다.

**구현:**
`bg=0, product=20, text=30, overlay shape=40` 우선순위를 부여하고 최종 정렬한다.

**결과:**
레이어 겹침 오류가 배치 로직 내부에서 정리됐고, editor 재렌더 경로가 단순화됐다.

## 4. 시스템 구조

```text
[입력: 업로드 이미지 + UserRequest JSON]
  → 단계 1: Downscale/입력 최적화
  → 단계 2: Director.init_project (폴더/manifest/기하정보)
  → 단계 3: CreativeDirector 또는 ContentPipeline (페이지 기획)
  → 단계 4: DetailPageGenerator 5단계 실행
      4-1 Cutout
      4-2 Background Generation(Flux)
      4-3 Upscale
      4-4 Color Correction
      4-5 Text/Shape Overlay
  → 단계 5: manifest 저장 + 편집 API로 후속 수정
[출력: assets/renders/output + manifest.json]
```

이 순서는 입력 안정화 후 기획을 확정하고, 그 다음 무거운 생성 단계를 수행하도록 설계됐다.  
무거운 생성을 먼저 실행하면 프롬프트 변경이나 레이어 수정이 발생할 때 재실행 비용이 커졌다.  
그래서 기획 데이터(`design_intent`)를 먼저 고정하고 이미지 합성을 뒤에 두는 순서를 유지했다.

## 5. 결과 및 성능

### 5-1. 정성적 개선

| 항목 | 개선 전 | 개선 후 |
|------|---------|---------|
| 파이프라인 제어 | 초기화와 생성이 한 호출로 붙어 있었다 | 초기화(`init_project`)와 실행(`execute_project`)이 분리됐다 |
| 실패 복구 | 전체 재시작이 필요했다 | 프로젝트/페이지 단위 재생성 엔드포인트로 복구했다 |
| 좌표 일관성 | px/ratio 혼용 보정이 여러 위치에 흩어졌다 | `LayoutManager`에서 레이어 좌표를 먼저 확정했다 |
| 모델 장애 대응 | 단일 LLM 실패 시 기획이 중단됐다 | OpenAI 실패 시 Gemini로 즉시 이관했다 |

### 5-2. 운영 지표

| 지표 | 코드상 수집 방식 | 현재 값 |
|------|------------------|---------|
| 단계별 처리시간(초) | `page.execution_time`에 step 키 저장 | 미측정 |
| 페이지 상태 전이 | `PENDING/PROCESSING/COMPLETED/FAILED` 저장 | 미측정 |
| 실행 이력 | `manifest.execution_history` 문자열 로그 | 미측정 |
| API 처리량/성공률 | 별도 집계 코드 없음 | 미측정 |

실측 로그 파일(`logcheck/server.log`)과 실행 산출 manifest가 현재 워크스페이스에 없어서 수치 결과는 비어 있었다.

### 5-3. 정량 평가 계획

1. 평가셋 200건을 만든다.  
상품 카테고리 10종 × 톤 5종 × 레이아웃 4종으로 균등 샘플링한다.
2. 실패율 지표를 기록한다.  
`FAILED 페이지 수 / 전체 페이지 수`를 지표로 삼고 목표를 3% 이하로 둔다.
3. 단계 지연 지표를 기록한다.  
`step_2_flux_inference` p50/p95를 측정하고 목표를 p50 8초 이하, p95 20초 이하로 둔다.
4. 편집 재렌더 정확도를 기록한다.  
편집 후 레이어 박스 IoU를 측정하고 목표를 0.95 이상으로 둔다.

## 6. 주요 설계 판단

| 문제 상황 | 선택지 | 선택 | 이유 |
|-----------|--------|------|------|
| 생성 실패 후 복구가 어려웠다 | 전체 재생성 / 프로젝트 단위 재시작 | 프로젝트·페이지 단위 재시작 | manifest 저장 구조를 이미 사용하고 있었기 때문이다 |
| GPU 메모리 재로딩 비용이 컸다 | 매 요청 전체 언로드 / heavy 상주 | heavy 상주 + light 언로드 | 모델 로딩 시간을 줄이고 OOM 대응 지점을 한곳에 모았다 |
| 기획 LLM 장애가 발생했다 | 단일 공급자 / 이중화 | OpenAI→Gemini failover | 기획 단계 중단을 막아 전체 파이프라인 중단을 줄였다 |
| 레이어 충돌이 반복됐다 | 생성기 내부 즉흥 배치 / 전용 레이아웃 매니저 | LayoutManager 분리 | 좌표 규칙과 z-index 규칙을 한곳에서 유지했다 |

## 7. 현재 한계

- 운영 실측 부재: 단계 시간은 코드에 저장되지만 로그 수집 파이프라인이 없어 대시보드가 비었다 → `execution_time` 수집기를 추가하고 배치 리포트를 자동 생성한다.
- 테스트 부재: `tests/` 디렉토리가 없어 회귀 검증 자동화가 없다 → 파이프라인 최소 통합 테스트와 API 스키마 테스트를 추가한다.
- 의존성 명세 누락: `requirements/requirements.txt` 길이가 0이라 재현성이 떨어졌다 → 실제 import 기준으로 잠금 파일을 생성한다.
- 설정 파일 공백: `config/logging_config.yaml` 길이가 0이라 설정 기반 로깅 전환이 막혔다 → 코드 기반 로깅과 yaml 설정을 단일 소스로 통합한다.
- 프리셋 파일 신뢰도 저하: 프리셋 JSON 로드가 예외를 허용하는 구조라 오류가 런타임에 드러났다 → CI에서 JSON 검증 단계를 추가한다.

## 8. 회고

### 가장 어려웠던 기술적 판단
가장 오래 걸린 판단은 GPU 메모리 전략이었다.  
초기 구조는 단계마다 모델을 바꾸는 방식이라 로딩 지연과 OOM이 동시에 발생했다.  
그래서 heavy 모델 상주와 light 모델 정리로 정책을 분리했다.  
이후 언로드 정책을 `VRAMHandler`로 모으면서 파이프라인 코드의 메모리 분기가 줄었다.

### 처음 가정과 달랐던 부분
처음에는 생성과 편집을 한 경로에서 처리해도 충분하다고 가정했다.  
실제 운용에서는 페이지 단위 재생성과 레이어 수정 요청이 반복됐다.  
이 패턴 때문에 초기화와 실행을 분리하고 editor 전용 API를 확장했다.  
결과적으로 생성 실패 복구와 후편집 경로가 서로 간섭하지 않게 정리됐다.

### 다시 만든다면 바꿀 부분
다시 만든다면 측정 계층을 먼저 만든다.  
현재 코드는 시간과 상태를 기록하지만 집계와 시각화가 빠져 있다.  
그래서 성능 회귀를 커밋 단위로 비교하지 못했다.  
다음 버전에서는 manifest 기반 배치 리포트를 우선 구현하고, 그 다음 모델·레이아웃 개선을 진행한다.

## 9. 코드

📦 [GitHub Repository](https://github.com/Sichanvisit/AI5_advanced)

코드 상세, 기술 스택, 설치법, API 문서는 GitHub README에서 확인하면 된다.
