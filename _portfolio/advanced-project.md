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

## 1. 프로젝트 한 줄 정의
제품 사진 한 장으로 판매용 광고 이미지를 자동 기획·생성·수정한 시스템

## 2. 배경 및 문제 정의

## 배경
프로젝트 기획 문서 19개를 기준으로 서비스 목표를 먼저 고정했다.  
목표는 소상공인용 광고 제작 시간을 줄이고, 결과물을 바로 수정 가능한 워크플로우로 만드는 일이었다.  
상세페이지는 구매 심리 흐름 5단계를 기준으로 11~17장 구성을 목표로 잡았다.

## 문제
단일 생성 버튼 구조는 결과가 어긋날 때 전체를 다시 돌려야 했다.  
텍스트 카피와 이미지 생성이 분리돼서 단계 간 톤 불일치가 반복됐다.  
기획 문서에는 11~17장 생성 요구가 있었지만 초기 구현은 단일 장수 흐름에 가까웠다.

| 문제 | 구체적 상황 |
|------|------------|
| 재작업 비용 과다 | 배경만 바꾸고 싶어도 전체 파이프라인을 다시 실행했다. |
| 기획-생성 단절 | 카피셋 문서의 5단계 메시지 흐름이 이미지 레이아웃에 일관되게 반영되지 않았다. |
| 장수 전략 미정렬 | 서비스 기획 문서는 11~17장 전략을 요구했지만 코드 기본값은 1~5장 중심으로 동작했다. |
| 성능 검증 공백 | 단계 시간 기록 구조는 있었지만 실측 로그와 평가셋이 없었다. |

## 3. 기술적 접근

### 3-1. 기획 프레임을 AIDA 기반 5단계로 고정

**문제:**
카피와 이미지를 따로 만들면 설득 흐름이 끊겼다.

**접근:**
기획 문서의 5단계 카피셋(Hook, Problem, Solution, Trust, Closing)을 페이지 역할 기준으로 고정했다.

**선택 이유:**
문서에서 상세페이지 설득 구조를 AIDA로 명시했고, 이 구조가 장수 확장(11~17장) 기준이 됐다.

**구현:**
`get_page_role`과 페이지별 prompt 생성 로직으로 역할을 강제하고, 각 페이지에 `design_intent`를 저장했다.

```python
def get_page_role(page_number: int, total_pages: int) -> str:
    if page_number == 1:
        return "cover"
    elif page_number == total_pages:
        return "cta"
    elif page_number <= (total_pages // 2) + 1:
        return "feature"
    else:
        return "review"
```

**결과:**
기획 문서의 메시지 순서가 코드 레벨 페이지 역할로 연결됐다.

### 3-2. 초기화/생성 분리로 재생성 비용 절감

**문제:**
초기화와 생성이 붙어 있어 실패 시 복구 비용이 컸다.

**접근:**
`init_project`와 `execute_project`를 분리하고 manifest 중심 상태관리를 적용했다.

**선택 이유:**
멘토 피드백 문서의 핵심 요구가 부분 재생성과 편집 루프였다.

**구현:**
`StateManager`가 프로젝트 상태를 저장하고, 재생성 API가 특정 프로젝트를 다시 실행한다.

```python
manifest = director.init_project(...)
...
manifest = director.execute_project(user_id="guest", project_id=project_id)
```

**결과:**
초기화 실패와 생성 실패를 분리해 복구 경로를 단순화했다.

### 3-3. 5단계 생성 파이프라인과 단계별 타이밍 기록

**문제:**
병목 단계가 명확하지 않아 최적화 우선순위를 잡기 어려웠다.

**접근:**
컷아웃→배경생성→업스케일→후처리→텍스트 오버레이를 고정하고 단계 시간을 기록했다.

**선택 이유:**
로드맵 문서가 MVP 이후 고도화를 단계별로 진행하도록 제시했고, 측정 가능한 구조가 필요했다.

**구현:**
`PerformanceTimer`로 step 단위 시간을 `execution_time` 딕셔너리에 저장했다.

```python
with PerformanceTimer(logger, "step_2_flux_inference", page.execution_time):
    generated_image = flux_engine.generate(...)
page.execution_time['step_2_generation'] = round(duration_page, 2)
```

**결과:**
페이지별 단계 시간과 실패 이력이 manifest에 축적됐다.

### 3-4. LLM 이중화로 기획 단계 중단 방지

**문제:**
단일 LLM 실패 시 전체 흐름이 중단됐다.

**접근:**
OpenAI 1순위, Gemini 2순위 failover를 적용했다.

**선택 이유:**
기획 단계가 막히면 후속 이미지 엔진이 전부 대기 상태가 됐다.

**구현:**
Primary 예외 발생 시 Secondary를 즉시 호출했다.

```python
if self.primary:
    try:
        return self.primary.generate(system_prompt, user_prompt, max_tokens)
    except Exception:
        logger.warning("즉시 Gemini 1.5 Flash로 긴급 이관")
if self.secondary:
    return self.secondary.generate(system_prompt, user_prompt, max_tokens)
```

**결과:**
기획 단계 장애가 전체 파이프라인 중단으로 이어지지 않았다.

### 3-5. 편집기 중심의 부분 수정 경로 확보

**문제:**
문서에서 요구한 "배경만 수정", "문구만 수정" 흐름이 코드에서 분리되지 않았다.

**접근:**
레이어 편집 API와 페이지 재생성 API를 분리해 후편집 경로를 고정했다.

**선택 이유:**
멘토 피드백 문서의 핵심은 비파괴 편집과 반복 수정 속도였다.

**구현:**
`/editor/.../layers/...` 패치 API와 `/projects/{id}/pages/{n}/regenerate`를 사용한다.

**결과:**
전체 재생성 없이 페이지 단위 수정 경로가 열렸다.

## 4. 시스템 구조

```text
[입력: 제품 이미지 1장 + 요청 JSON]
  → 단계 1: 프로젝트 초기화 (manifest, 폴더, 기하정보)
  → 단계 2: 콘텐츠 기획 (5단계 역할 기반 카피/프롬프트)
  → 단계 3: 이미지 생성 파이프라인
      3-1 Cutout
      3-2 Background Generation
      3-3 Upscale
      3-4 Color Correction
      3-5 Text/Shape Overlay
  → 단계 4: 결과 저장 (assets/renders/output, manifest)
  → 단계 5: 편집/재생성 API로 반복 수정
[출력: 광고 이미지 세트 + 상태 이력]
```

이 순서는 문서에서 제시한 MVP 전략과 동일하게 잡았다.  
먼저 "생성 가능"을 확보하고, 그다음 편집 루프를 붙이는 방식으로 구현했다.  
그래서 기획-생성-수정이 한 데이터(`manifest.json`)를 공유한다.

## 5. 결과 및 성능

### 5-1. 정성적 개선

| 항목 | 개선 전 | 개선 후 |
|------|---------|---------|
| 상세페이지 흐름 | 단일 이미지 중심 사고였다 | 5단계 카피셋 기반 흐름으로 고정했다 |
| 재생성 범위 | 전체 파이프라인 재실행이 기본이었다 | 프로젝트/페이지 단위 재생성으로 분리했다 |
| 후편집 | 텍스트/레이어 수정 경로가 약했다 | 레이어 패치 API와 재렌더 경로를 확보했다 |
| 기획 안정성 | 단일 LLM 실패에 취약했다 | OpenAI→Gemini failover를 적용했다 |

### 5-2. 운영 지표

| 지표 | 코드상 수집 방식 | 현재 값 |
|------|------------------|---------|
| 단계별 처리시간 | `execution_time` 딕셔너리 저장 | 미측정 |
| 상태 전이 | `PENDING/PROCESSING/COMPLETED/FAILED` | 미측정 |
| 실행 이력 | `execution_history` 누적 | 미측정 |
| 11~17장 생성 성공률 | 별도 집계 코드 없음 | 미측정 |

워크스페이스에 실측 로그와 산출 manifest 샘플이 없어 운영 수치는 비어 있었다.

### 5-3. 정량 평가 계획

1. 11~17장 상세페이지 평가셋 120건을 만든다.  
카테고리 6종 × 톤 5종 × 장수 4구간(11/13/15/17)으로 구성한다.
2. 단계 실패율을 측정한다.  
`FAILED page / total page`를 지표로 사용하고 목표는 2% 이하로 둔다.
3. 재생성 지연을 측정한다.  
페이지 단위 재생성 p50 5초 이하, p95 12초 이하를 목표로 둔다.
4. 카피-이미지 일치율을 측정한다.  
페이지 역할(cover/feature/cta)과 생성 결과의 일치율 목표를 90% 이상으로 둔다.

## 6. 주요 설계 판단

| 문제 상황 | 선택지 | 선택 | 이유 |
|-----------|--------|------|------|
| 설득 흐름 부재 | 자유 생성 / 5단계 구조 | 5단계 카피셋 고정 | 기획 문서의 AIDA 흐름을 코드에 매핑했다 |
| 재작업 비용 과다 | 전체 재생성 / 부분 재생성 | 프로젝트·페이지 단위 재생성 | 수정 요청이 반복되는 운영 패턴에 맞췄다 |
| 기획 단계 장애 | 단일 LLM / 이중화 | OpenAI→Gemini failover | 기획 중단이 전체 중단으로 이어지는 문제를 막았다 |
| 향후 확장 우선순위 불명확 | 기능 동시 개발 / MVP 후 확장 | MVP 우선 + 기능 5종 순차 확장 | 로드맵 문서의 우선순위 전략을 그대로 적용했다 |

## 7. 현재 한계

- 11~17장 운영 검증 미완료: 장수 확장 전략은 문서화됐지만 자동 평가 루프가 없다 → 장수별 실패율 리포트 배치를 추가한다.
- 테스트 부재: `tests/` 폴더가 없어 회귀 검증 자동화가 없다 → 파이프라인 통합 테스트와 API 계약 테스트를 추가한다.
- 의존성 명세 공백: `requirements/requirements.txt`가 비어 있다 → 실사용 import 기준으로 의존성 잠금 파일을 생성한다.
- 확장 기능 미구현: Brand Kit, Context Mockup, Style Reference, Magic Eraser, Smart Resize가 문서 단계에 머물러 있다 → 난이도/효과 기준으로 순차 구현한다.
- 실측 지표 공백: 단계 시간은 저장하지만 집계 대시보드가 없다 → manifest 집계 스크립트와 주간 리포트를 추가한다.

## 8. 회고

### 가장 어려웠던 기술적 판단
가장 오래 고민한 지점은 "생성 품질"과 "수정 속도"의 우선순위였다.  
처음에는 한 번에 완성도를 올리는 쪽으로 설계를 밀었다.  
실사용 시나리오를 정리하니 수정 요청이 더 자주 발생했다.  
그래서 전체 완성도보다 부분 재생성 구조를 먼저 고정했다.

### 처음 가정과 달랐던 부분
처음에는 단일 장수 생성이 핵심이라고 가정했다.  
기획 문서를 정리하면서 핵심은 11~17장 스토리 구조라는 점이 드러났다.  
그래서 페이지 역할과 카피셋 기준을 코드 구조에 맞춰 다시 배치했다.  
이후 포트폴리오 문서도 "무엇을 만들었는지"보다 "왜 그런 구조를 택했는지" 중심으로 재작성했다.

### 다시 만든다면 바꿀 부분
다시 만든다면 관측 계층부터 만든다.  
현재 구조는 기록은 남기지만 집계가 없어 의사결정 속도가 느리다.  
다음 버전에서는 장수별 실패율과 재생성 시간을 먼저 대시보드화한다.  
그 다음 Brand Kit와 Style Reference를 붙여 사용자 반복 입력을 줄인다.

## 9. 코드

📦 [GitHub Repository](https://github.com/Sichanvisit/AI5_advanced)

코드 상세, 기술 스택, 설치법, API 문서는 GitHub README에서 확인하면 된다.
