---
title: "Obsidian RAG"
date: 2026-02-28
priority: 3
excerpt: "Obsidian 노트를 Summary+Raw 2계층 RAG와 하이브리드 검색으로 연결해, 질문-근거-답변 흐름을 만든 개인 지식 검색 프로젝트"
header:
  teaser: /assets/images/portfolio/obsidian-rag-thumb.svg
github_url: "https://github.com/Sichanvisit/Obsidian_RAG"
project_dir: "C:/Users/bhs33/Desktop/project/Obsidian_RAG"
tech_stack:
  - Python
  - FastAPI
  - Streamlit
  - ChromaDB
  - RAG
  - BM25
---
## 1. 프로젝트 한 줄 정의
Obsidian 지식 저장소의 검색 누락과 근거 약화를 줄인 로컬 RAG 시스템

## 2. 배경 및 문제 정의

## 배경
이 시스템은 Obsidian 기반 개인 지식 저장소를 질의응답으로 조회하려고 만들었다.
수집 파이프라인은 `jobs.yaml` 기준 11개 Job으로 운영됐다.
현재 벡터 저장소는 raw 컬렉션 8개와 `chroma.sqlite3` 파일 10개로 구성됐다.
저장된 청크 수는 raw 23,147개, summary 1,123개, 총 24,270개였다.

## 문제
단일 검색기로는 질의 유형 편차를 처리하지 못했다.
키워드 질의에서는 타 프로젝트 문서가 상위에 섞였다.
의미 질의에서는 핵심 문서가 누락됐다.
검색 품질이 낮아도 생성 단계가 진행되어 근거가 약한 장문 응답이 출력됐다.

| 문제 | 구체적 상황 |
|------|------------|
| 프로젝트 문맥 혼입 | 프로젝트 힌트가 약한 질문에서 타 프로젝트 문서가 상위에 섞였다 |
| 근거 추적 약화 | 답변에 인용 태그가 빠진 경우 근거 역추적이 끊겼다 |
| 생성 안정성 저하 | 스트리밍 중 반복 구간이 길어지면서 응답 길이가 과도하게 늘어났다 |

## 3. 기술적 접근

### 3-1. 다중 질의 검색으로 회수율 보정

**문제:**
짧은 질의 하나로는 검색 의도가 충분히 드러나지 않았다.

**접근:**
질의 재작성, 분해, 키워드 질의를 생성한 뒤 다중 질의를 검색에 사용했다.
검색 단계에서는 상위 3개 질의만 실행했다.

**선택 이유:**
재작성 질의와 원 질의를 같이 유지하면 누락을 줄였다.
질의 수를 제한하면 지연 상한을 통제했다.

**구현:**
아래 로직으로 다중 질의를 만들고, 실제 검색은 3개 질의로 제한했다.

```python
# backend/src/graph/agentic_flow.py
multi_queries = list(dict.fromkeys([q.strip() for q in multi_queries if q.strip()]))[:5]
state.current_query = multi_queries[0] if multi_queries else rewritten_query or base_query
state.multi_queries = multi_queries

for i, query in enumerate(queries[:3]):
    docs = self.engine.search(query_for_search, k=5)
```

중복 제거는 `source_path`, 파일명, 스니펫 지문 3중 기준으로 처리했다.

```python
source_key = str(doc.source_path).replace("\\", "/").lower()
source_name_key = Path(source_key).name
if source_key in seen_sources or source_name_key in seen_source_names:
    continue
snippet_fp = self._snippet_fingerprint(getattr(doc, "page_content", ""))
if snippet_fp and snippet_fp in seen_snippets:
    continue
```

**결과:**
질의당 5개, 최대 3개 질의를 검색하는 구조로 후보 상한을 15개로 고정했다.
중복 소스가 컨텍스트에서 제거됐다.

---

### 3-2. 벡터+BM25 병합과 점수 보정

**문제:**
벡터 단독 검색은 키워드 질의에서 흔들렸고, 키워드 단독 검색은 의미 질의에서 누락이 발생했다.

**접근:**
임베딩 검색과 BM25 검색을 동시에 수행하고 RRF로 통합했다.
파일명/본문 키워드 부스트를 추가했다.

**선택 이유:**
질의 유형이 섞인 환경에서는 단일 검색기가 안정적으로 동작하지 않았다.
문서명 힌트가 강한 질문이 반복되어 파일명 부스트가 필요했다.

**구현:**
각 검색기에서 `max(k*5, 20)` 후보를 수집하고 `k=60` RRF로 결합했다.

```python
emb = self.summary_db.query(
    query_embeddings=[q_emb],
    n_results=max(k * 5, 20),
)
bm25_top = self.bm25.get_top_k(bm25_query, k=max(k * 5, 20))
fused_results = self._reciprocal_rank_fusion(embedding_results, bm25_results, k=60)
```

결합 점수에 파일명 매칭 `+0.3`, 본문 매칭 `+0.1`을 더해 프로젝트 문맥을 강화했다.

```python
keyword_boost = 0.0
for kw in query_keywords:
    if kw in filename_lower:
        keyword_boost += 0.3
    elif kw in doc_lower:
        keyword_boost += 0.1
score = base_score + keyword_boost
```

**결과:**
후보 최소치를 20으로 고정해 질의별 편차를 줄였다.
의미 유사도와 어휘 일치가 동시에 반영됐다.

---

### 3-3. 검색 품질 게이트와 재작성 상한

**문제:**
저품질 검색 결과가 그대로 생성 단계로 넘어갔다.

**접근:**
검색 점수로 `PASSED/MARGINAL/FAILED`를 나눴다.
`FAILED` 또는 `MARGINAL` 상황에서만 재작성 루프를 돌렸다.
재작성 횟수 상한을 고정했다.

**선택 이유:**
무조건 재시도하면 지연만 늘었다.
무제한 루프는 응답 안정성을 무너뜨렸다.

**구현:**

```python
if avg_score >= SCORE_THRESHOLD:
    state.retrieval_grade = "PASSED"
elif avg_score >= SCORE_THRESHOLD * ScoreWeights.GRADE_MID_MULTIPLIER:
    state.retrieval_grade = "MARGINAL"
else:
    state.retrieval_grade = "FAILED"

if state.step_counts["rewrite"] >= MAX_RETRIES:
    state.logs.append("Rewrite stopped: max retries reached")
    return state
```

**결과:**
저품질 검색의 직행 생성이 차단됐다.
재작성 루프가 최대 2회로 제한됐다.

---

### 3-4. 생성 반복 절단과 Self-RAG 점수화

**문제:**
스트리밍 생성 중 반복 루프가 누적됐다.

**접근:**
반복 탐지 후 누적 기준을 넘기면 응답을 절단했다.
생성 종료 후 Self-RAG 점수를 계산해 메트릭으로 남겼다.

**선택 이유:**
즉시 중단은 응답 손실이 컸다.
임계치 절단은 내용 손실을 줄이면서 루프를 멈췄다.

**구현:**

```python
if len(answer) > 1000:
    is_dup, reason = check_duplicate(answer, seen_sentences)
    if is_dup:
        duplicate_hits += 1
        if duplicate_hits >= 20 and len(answer) >= 2400:
            answer += "\n\n[Repetition omitted]"
            break
```

Self-RAG 점수는 overlap, grounding, completeness, structure 가중합으로 계산했다.

```python
relevance_score = (
    overlap * 0.4 +
    grounding_score * 0.3 +
    completeness * 0.2 +
    structure_score * 0.1
)
```

**결과:**
반복 구간 절단 경계가 명시됐다.
`tokens_per_second`, `self_rag_score`가 파이프라인 메트릭에 기록됐다.

---

### 3-5. 요약 통합 + 원문 분리 저장 구조

**문제:**
요약 회수율과 원문 근거 추적을 동시에 확보해야 했다.

**접근:**
summary는 단일 통합 컬렉션으로 저장했다.
raw는 프로젝트별 컬렉션으로 분리했다.

**선택 이유:**
질의 초기에 전역 요약 검색이 필요했다.
최종 근거 단계에서는 프로젝트 원문 분리가 필요했다.

**구현:**

```python
# backend/src/pipeline/ingestor.py
if layer == "summary":
    return "summary/integrated_knowledge"
elif layer == "raw":
    base = job.collection_raw if job.collection_raw else job.name
    return f"raw/{base}".strip("/")
```

**결과:**
요약 회수와 원문 근거 추적이 분리된 상태로 동시에 동작했다.

## 4. 시스템 구조

```text
[입력: query, project_name, history]
  → 단계 1: 질의 재작성/분해로 다중 질의 생성
  → 단계 2: summary 임베딩 검색 + BM25 검색 병렬 수행
  → 단계 3: RRF 결합 + 파일명/본문 키워드 보정
  → 단계 4: 링크 기반 raw 확장 + 프로젝트 힌트 필터링
  → 단계 5: 검색 품질 등급화 후 필요 시 재작성 재검색
  → 단계 6: NDJSON 스트리밍 생성 + 반복 절단
  → 단계 7: Self-RAG 검증 점수 기록
[출력: 답변 텍스트, 인용 태그, 단계 로그, 속도/품질 메트릭]
```

이 순서를 유지한 이유는 검색 실패를 생성 이후에 처리하면 비용이 더 커졌기 때문이다.
그래서 생성 전 단계에서 품질 게이트를 통과시켰다.
요약 검색을 먼저 둔 이유는 초기 후보 회수 속도를 확보하기 위해서였다.
원문 확장을 뒤에 둔 이유는 근거 밀도를 올리기 위해서였다.

## 5. 결과 및 성능

### 정성적 개선

| 항목 | 개선 전 | 개선 후 |
|------|---------|---------|
| 검색 입력 | 단일 질의 1개로 검색했다 | 재작성/분해를 포함한 다중 질의를 사용했다 |
| 검색 결합 | 단일 검색기의 편향이 노출됐다 | 임베딩+BM25+RRF로 편향을 분산했다 |
| 품질 제어 | 저품질 검색도 생성으로 직행했다 | 등급 판정 뒤 재작성 루프로 우회했다 |
| 생성 안정성 | 반복 구간이 누적돼 응답이 길어졌다 | 반복 임계치에서 절단해 루프를 중단했다 |
| 근거 표기 | 인용 누락 시 추적이 끊겼다 | 인용 태그 미존재 시 출처 태그를 보강했다 |

### 운영 지표 현황

| 지표 | 상태 |
|------|------|
| 평균 응답 시간 | 미측정 |
| 평균 tokens/second | 미측정 |
| 평균 Self-RAG 점수 | 미측정 |
| 수집 구조 | `tokens_per_second`, `self_rag_score` 필드 구현 완료 |

### 정량 평가 계획

평가셋 120문항을 프로젝트별로 균등 분할한다.
검색 평가는 `Recall@5`, `MRR@10`, 프로젝트 일치율을 사용한다.
생성 평가는 인용 커버리지, groundedness, 반복률을 사용한다.
1차 릴리스 기준은 `Recall@5 ≥ 0.75`, groundedness `≥ 0.80`, 인용 커버리지 `≥ 0.90`으로 둔다.
실행 결과는 NDJSON 로그를 배치 집계해 주간 리포트로 고정한다.

## 6. 주요 설계 판단

| 문제 상황 | 선택지 | 선택 | 이유 |
|-----------|--------|------|------|
| 질의 유형 편차 | 벡터 단독 / BM25 단독 / 혼합 | 혼합 + RRF | 키워드 질의와 의미 질의를 동시에 처리했다 |
| 저장소 구성 | summary/raw 통합 / summary 통합+raw 분리 | summary 통합 + raw 분리 | 전역 회수와 프로젝트 근거 추적을 같이 확보했다 |
| 저품질 검색 처리 | 즉시 생성 / 재작성 후 재검색 | 재작성 후 재검색 | 실패 검색의 직행 생성을 차단했다 |
| 반복 응답 처리 | 즉시 중단 / 무시 / 임계치 절단 | 임계치 절단 | 응답 유실을 줄이면서 루프를 멈췄다 |
| 모델 실행 경로 | 단일 모델 / 로컬-원격 분기 | 로컬-원격 분기 | 환경별 비용과 지연 조건을 분리했다 |

## 7. 현재 한계 및 개선 방향

- 품질 대시보드 API 불일치: 프론트는 `/api/quality/*`를 호출하지만 백엔드 라우트는 `/health`, `/api/chat/stop`, `/api/chat/stream`만 구현됐다. → 품질 메트릭 저장소와 `quality` 라우터를 백엔드에 추가한다.
- 테스트 공백: `backend/tests`는 3개 파일 중 2개가 빈 파일이고, `test_api.py`는 주석 2줄만 존재한다. → 스트리밍 포맷, 검색 등급 분기, 재작성 상한을 통합 테스트로 추가한다.
- 환경 의존 경로 하드코딩: raw 탐색 fallback 경로가 사용자 로컬 절대경로에 고정됐다. → 환경변수 기반 경로 해석기로 통합한다.
- 인코딩 일관성 저하: 일부 파일 주석이 깨져 있고 “한글 주석 복구” 흔적이 남아 있다. → UTF-8 일괄 변환과 인코딩 검증 CI를 추가한다.

## 8. 회고

### 가장 어려웠던 기술적 판단
가장 오래 걸린 판단은 검색 결합 방식이었다.
처음에는 벡터 검색 단독으로 충분하다고 봤다.
운영 질의를 붙여보니 키워드형 질문에서 프로젝트 문맥이 흔들렸다.
BM25를 붙이고 RRF로 결합한 뒤 파일명 가중치를 추가했다.
그 뒤에야 키워드형 질문과 의미형 질문의 편차가 줄었다.

### 처음 가정과 달랐던 부분
처음 가정은 검색 품질이 낮아도 생성 단계가 보정해준다는 것이었다.
실제 파이프라인에서는 저품질 컨텍스트가 들어가면 장문 오답이 먼저 늘었다.
그래서 생성 이전에 품질 게이트를 넣고 재작성 루프를 분리했다.
또한 반복 출력은 프롬프트 수정만으로 해결되지 않았다.
결국 생성 중복 감지와 절단 조건을 코드 레벨에서 강제했다.

### 다시 만든다면 바꿀 부분
다시 만들면 평가 체계를 먼저 고정한다.
현재 구조는 기능 구현이 지표 설계보다 앞서서 개선 폭을 실측으로 즉시 제시하지 못했다.
다음 버전은 질의셋, 정답 근거셋, 로그 집계 스키마를 먼저 만든다.
그 위에서 검색 실험을 돌리면 판단 속도와 회귀 검증 속도가 같이 올라간다.
품질 대시보드도 백엔드 API와 동시에 설계해 단절을 없앤다.

## 9. 코드

📦 [GitHub Repository](https://github.com/Sichanvisit/Obsidian_RAG)

코드 상세, 기술 스택, 설치/실행, API 문서는 저장소 README에서 확인한다.
