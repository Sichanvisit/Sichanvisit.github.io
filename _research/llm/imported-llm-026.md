---
title: "하이브리드검색 리랭킹"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)하이브리드검색_리랭킹"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)하이브리드검색_리랭킹.md"
excerpt: "키워드 검색(Keyword Search)과 의미 기반 검색(Semantic Search)의 장점을 결합하여 검색 정확도를 높이는 기법"
research_summary: "키워드 검색(Keyword Search)과 의미 기반 검색(Semantic Search)의 장점을 결합하여 검색 정확도를 높이는 기법. BM25 알고리즘이 대표적: 단어의 빈도와 역문서 빈도를 기반으로 작동하며, 정확한 단어 매칭에 강합니다. `ipynb/md` 원본과 10개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 getpass, os, langchain_community, langchain_openai입니다."
research_artifacts: "ipynb/md · 코드 10개 · 실행 7개"
code_block_count: 10
execution_block_count: 7
research_focus:
  - "하이브리드 검색과 리랭킹"
  - "키워드 검색(Keyword Search)과 의미 기반 검색(Semantic Search)의 장점을 결합..."
  - "하이브리드 검색"
research_stack:
  - "getpass"
  - "os"
  - "langchain_community"
  - "langchain_openai"
  - "langchain_core"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

키워드 검색(Keyword Search)과 의미 기반 검색(Semantic Search)의 장점을 결합하여 검색 정확도를 높이는 기법. BM25 알고리즘이 대표적: 단어의 빈도와 역문서 빈도를 기반으로 작동하며, 정확한 단어 매칭에 강합니다. `ipynb/md` 원본과 10개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 getpass, os, langchain_community, langchain_openai입니다.

**빠르게 볼 수 있는 포인트**: 하이브리드 검색과 리랭킹, 키워드 검색(Keyword Search)과 의미 기반 검색(Semant..., 하이브리드 검색.

**남겨둔 자료**: `ipynb/md` 원본과 10개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 getpass, os, langchain_community, langchain_openai입니다.

**주요 스택**: `getpass`, `os`, `langchain_community`, `langchain_openai`, `langchain_core`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 10 |
| Execution Cells | 7 |
| Libraries | `getpass`, `os`, `langchain_community`, `langchain_openai`, `langchain_core`, `langchain_huggingface` |
| Source Note | `3-5 (실습)하이브리드검색_리랭킹` |

## What This Note Covers

### 하이브리드 검색

키워드 검색(Keyword Search)과 의미 기반 검색(Semantic Search)의 장점을 결합하여 검색 정확도를 높이는 기법

### 키워드 검색(Sparse Retriever)

BM25 알고리즘이 대표적: 단어의 빈도와 역문서 빈도를 기반으로 작동하며, 정확한 단어 매칭에 강합니다.

### 의미 검색(Dense Retriever)

임베딩(Embedding) 벡터 유사도(Cosine Similarity 등)를 기반: 단어가 달라도 문맥적 의미가 유사한 문서를 찾는 데 강합니다.

### 리랭킹(Re-ranking): "속도 vs 정확도"의 타협점

Retrieval 단계 (Bi-Encoder)

## Why This Matters

### RAG 검색 파이프라인

- 왜 필요한가: LLM이 외부 지식을 안정적으로 참조하게 하려면, 생성 전에 관련 문서를 정확히 찾아오는 검색 단계가 먼저 필요합니다.
- 왜 이 방식을 쓰는가: 이 방식은 모델 파라미터만 믿지 않고 최신 문서나 도메인 지식을 붙일 수 있어서 실제 서비스형 QA에 적합합니다.
- 원리: 문서를 청크로 나누고 임베딩한 뒤, 질문과 가까운 벡터를 검색해 프롬프트에 함께 넣는 구조로 동작합니다.

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 프롬프트 체인 구성

- 왜 필요한가: LLM 호출을 재현 가능하게 만들려면 입력 조합, 프롬프트 템플릿, 후처리 순서를 구조화할 필요가 있습니다.
- 왜 이 방식을 쓰는가: 체인 구조는 실험 중 프롬프트와 입력 변형을 비교하기 쉽고, 이후 RAG나 에이전트 단계로 확장하기도 좋습니다.
- 원리: 질문과 컨텍스트를 정해진 템플릿에 넣고, 모델 호출 결과를 다음 단계 입력으로 넘기며 처리 흐름을 구성합니다.

## Implementation Flow

1. 하이브리드 검색: 키워드 검색(Keyword Search)과 의미 기반 검색(Semantic Search)의 장점을 결합하여 검색 정확도를 높이는 기법
2. 키워드 검색(Sparse Retriever): BM25 알고리즘이 대표적: 단어의 빈도와 역문서 빈도를 기반으로 작동하며, 정확한 단어 매칭에 강합니다.
3. 의미 검색(Dense Retriever): 임베딩(Embedding) 벡터 유사도(Cosine Similarity 등)를 기반: 단어가 달라도 문맥적 의미가 유사한 문서를 찾는 데 강합니다.
4. 리랭킹(Re-ranking): "속도 vs 정확도"의 타협점: Retrieval 단계 (Bi-Encoder)

## Code Highlights

### 의미 검색(Dense Retriever)

`의미 검색(Dense Retriever)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 샘플 데이터, BM25 retriever, Vector retriever 흐름이 주석과 함께 드러납니다.

```python
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda

# 1. 샘플 데이터
docs_list = [
    "아이폰 15의 배터리 수명은 20시간입니다.",
    "갤럭시 S24는 AI 기능이 탑재되어 있습니다.",
    "사과는 맛있는 과일입니다.",
    "배터리 절약 모드를 켜면 사용 시간이 늘어납니다."
]

# 2. BM25 retriever
bm25 = BM25Retriever.from_texts(docs_list)
bm25.k = 2

# 3. Vector retriever
embedding = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(docs_list, embedding)
vec = vectorstore.as_retriever(search_kwargs={"k": 2})


# 4. 하이브리드 검색 함수
def hybrid_search(query):
    bm25_docs = bm25.invoke(query)
    vec_docs = vec.invoke(query)
# ... trimmed ...
```

### Re-ranking 단계 (Cross-Encoder)

`Re-ranking 단계 (Cross-Encoder)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 문서 준비, BM25 Retriever, Vector Retriever 흐름이 주석과 함께 드러납니다.

```python
from langchain_community.retrievers import BM25Retriever
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda

# ------------------------------
# 1. 문서 준비
# ------------------------------
texts = [
    "강남역에서 가까운 스테이크 맛집 추천 리스트입니다. 분위기 좋은 고기 레스토랑이 많습니다.",
    "서울 강남역에서 파스타가 맛있는 이탈리안 레스토랑 리스트입니다. 크림, 토마토 파스타가 유명합니다.",   # 🎯 정답
    "강남역 맛집 전체 가이드입니다. 파스타부터 고기, 한식까지 다양한 식당을 포함합니다.",
    "서울 홍대 파스타 맛집 추천입니다. 강남역과는 거리가 꽤 있습니다.",
    "부산 남천동 파스타 맛집 리스트입니다. 부산 지역 이탈리안 맛집 모음입니다.",
    "서울 강남역 카페 추천 리스트입니다. 디저트와 커피로 유명한 곳이 많습니다."
]

# ------------------------------
# 2. BM25 Retriever
# ------------------------------
bm25 = BM25Retriever.from_texts(texts)
bm25.k = 3

# ------------------------------
# 3. Vector Retriever
# ------------------------------
# ... trimmed ...
```

### Re-ranking 단계 (Cross-Encoder)

`Re-ranking 단계 (Cross-Encoder)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 테스트: RAG vs 하이브리드 vs 리랭크 비교, (1) RAG 기본: 벡터 검색만 사용, (2) 하이브리드 검색: BM25 + 벡터 흐름이 주석과 함께 드러납니다.

```python
# ------------------------------
# 7. 테스트: RAG vs 하이브리드 vs 리랭크 비교
# ------------------------------
query = "서울 강남역 파스타 맛집 추천"

# (1) RAG 기본: 벡터 검색만 사용
vec_docs = vec.invoke(query)

# (2) 하이브리드 검색: BM25 + 벡터
hybrid_docs = hybrid_retriever.invoke(query)

# (3) 하이브리드 + CrossEncoder 리랭크 (최종 답변에 쓸 문서 1개 선택)
reranked_docs = rerank_with_cross_encoder(query, hybrid_docs, top_n=1)

print("=== 1. 벡터 검색만 사용 (RAG 기본) ===")
for i, d in enumerate(vec_docs, 1):
    print(f"{i}. {d.page_content}")

print("\n=== 2. 하이브리드 검색 (BM25 + 벡터) ===")
for i, d in enumerate(hybrid_docs, 1):
    print(f"{i}. {d.page_content}")

print("\n=== 3. 하이브리드 + CrossEncoder 리랭크 (최종 선택 문서) ===")
for d in reranked_docs:
    print("답변에 사용할 문서:", d.page_content)
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 (실습)하이브리드검색_리랭킹.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 (실습)하이브리드검색_리랭킹.ipynb`, `3-5 (실습)하이브리드검색_리랭킹.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 키워드 검색(Keyword Search)과 의미 기반 검색(Semantic Search)의 장점을 결합하여 검색 정확도를 높이는 기법
> RAG(Retrieval-Augmented Generation) 시스템 구축 시, 단순히 벡터 검색만 사용할 경우 고유명사나 정확한 용어 매칭이 어려울 수 있는데, 하이브리드 서치는 이를 보완(BM25 → 키워드 기반 정확한 검색, Vector Search → 의미 기반 검색)
