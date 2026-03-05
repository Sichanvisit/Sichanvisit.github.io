---
title: "LangChain 기반 고성능 RAG 시스템 엔지니어링 총괄 가이드"
date: 2026-01-15
study_tab: "LLM"
tags:
  - LLM
  - RAG
  - LangChain
  - Retrieval
  - VectorDB
  - LCEL
excerpt: "데이터 파이프라인 관점에서 LangChain RAG를 설계·최적화하는 실무 가이드를 정리합니다."
header:
  teaser: /assets/images/profile.png
---

LangChain은 단순 툴킷이 아니라, 비정형 데이터를 가공해 LLM 추론에 연결하는 **데이터 파이프라인 프레임워크**입니다.  
RAG 품질은 결국 각 단계(분할, 인덱싱, 검색, 재정렬, 생성)를 얼마나 정교하게 설계하느냐에서 결정됩니다.

## 1. 데이터 전처리 및 인덱싱: 정보 손실 없는 구조화

LLM이 잘 읽고, 검색기가 잘 찾는 지식 조각(Chunk)을 만드는 단계입니다.

### RecursiveCharacterTextSplitter
- 구두점(`\n\n`, `\n`, 공백 등) 기반 계층 분할
- `chunk_overlap`으로 경계 문맥 보존
- 빠르고 안정적이지만, 의미 단위 분할에는 한계

### SemanticChunker
- 임베딩 기반 의미 변화 지점(Breakpoint) 탐지
- 문단의 의미 일관성 유지에 유리
- 법률/기술문서처럼 문맥 의존성이 강한 도메인에서 효과적

### ParentDocumentRetriever
- 검색은 작은 Child chunk로 정밀하게 수행
- 반환은 큰 Parent 문서로 문맥을 확장
- 정밀도와 풍부한 컨텍스트를 동시에 확보

### SelfQueryRetriever
- 질문을 `검색 쿼리 + 메타데이터 필터`로 분해
- 예: 작성자, 연도, 제품군, 버전 등의 조건 검색
- 단순 유사도 검색 대비 정확도 향상

## 2. 의미론적 저장: 벡터 공간 설계

텍스트를 임베딩으로 변환하고, 빠르게 검색 가능한 인덱스를 구성합니다.

### 임베딩 모델 선택
- OpenAIEmbeddings: 품질·편의성 강점
- HuggingFaceEmbeddings: 로컬/온프레미스 유연성
- 핵심 원칙: **문서 언어·질문 언어·도메인 용어의 일관성**

### VectorStore 선택
- FAISS: 로컬, 빠른 실험, 고성능
- Chroma: 로컬 개발/프로토타이핑 용이
- Pinecone: 클라우드 확장성과 운영 편의성

대규모 검색에서는 HNSW류 ANN 인덱싱이 성능 핵심입니다.

## 3. 지능형 검색: 검색 품질이 답변 품질

단일 쿼리 유사도 검색만으로는 누락과 노이즈가 자주 발생합니다.

### MultiQueryRetriever (Query Expansion)
- 질문을 3~5개 변형 질의로 확장
- 모호한 질문의 recall 향상

### EnsembleRetriever (Hybrid Search)
- BM25(키워드) + Vector(의미) 결과 결합
- 고유명사/숫자/약어 + 의미 유사도를 동시에 반영

### Re-ranking (Cross-Encoder)
- 1차 검색 상위 문서를 재평가해 순위 재정렬
- 실제로 정답률 상승 폭이 큰 구간

### HyDE
- 질문에 대한 가상 답변을 먼저 생성
- 해당 가상 답변으로 검색해 의미 간극 축소

## 4. 생성 제어: LCEL 기반 파이프라인 설계

검색 결과를 안전하고 일관된 출력으로 만드는 단계입니다.

### LCEL (LangChain Expression Language)
- `Prompt | Model | Parser` 형태로 체인 선언
- 단계별 재사용과 가독성 향상

### RunnableParallel
- 검색, 메타데이터 조회, 포맷팅 병렬 처리
- 지연 시간 단축

### RunnableBranch
- 의도 분기(일반 대화 vs 지식 질의)
- 불필요한 검색 호출 최소화

### ContextualCompressionRetriever
- 검색 문서에서 질문 관련 문장만 추출
- 토큰 비용 절감 + 노이즈 감소

### Output Parser
- JSON/Pydantic 구조화 출력
- 후속 시스템(API, UI, 워크플로우) 연동 안정화

## 5. 문제-해결 맵

| 단계 | 대표 문제 | 권장 해결책 |
|---|---|---|
| 데이터 처리 | 문맥 단절, 파편화 | `SemanticChunker`, `ParentDocumentRetriever` |
| 인덱싱 | 필터 부재, 탐색 범위 과다 | `SelfQueryRetriever`, 메타데이터 태깅 |
| 1차 검색 | 누락, 키워드 미스 | `MultiQueryRetriever`, Hybrid(Ensemble) |
| 2차 검색 | 순위 부정확, 노이즈 | Re-ranking, `ContextualCompressionRetriever` |
| 생성 최적화 | 토큰 과다, 답변 장황 | Compression, 출력 스키마 고정 |
| 워크플로우 | 지연, 분기 처리 미흡 | LCEL + Parallel/Branch 설계 |

## 6. 엔지니어링 실전 전략

### 검색 누락이 잦다면
- MultiQuery로 질의 다양화
- BM25 + Vector Hybrid 결합

### 답변 노이즈가 많다면
- Re-ranker 도입
- Contextual Compression으로 핵심 문장만 주입

### 할루시네이션이 우려된다면
- 프롬프트에 근거 기반 답변 강제
- 문서 출처(`source`, `url`, `chunk_id`)를 답변에 함께 반환

### 대화형 맥락이 필요하다면
- 메모리(세션 히스토리) 계층 추가
- 장기 대화는 외부 저장소 기반 히스토리 관리

## 결론

LangChain RAG의 본질은  
**비정형 데이터 변환 → 검색 최적화 → 근거 기반 생성 제어**를 하나의 파이프라인으로 설계하는 일입니다.

클래스를 많이 쓰는 것이 중요한 게 아니라,
문제 지점마다 맞는 조합을 설계하고 측정하는 것이 성능을 결정합니다.

한 줄 요약: **RAG의 승부는 모델 크기보다 파이프라인 품질에서 갈립니다.**
