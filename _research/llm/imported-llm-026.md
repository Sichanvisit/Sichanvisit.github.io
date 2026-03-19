---
title: "하이브리드검색 리랭킹"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)하이브리드검색_리랭킹"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)하이브리드검색_리랭킹.md"
excerpt: "키워드 검색(Keyword Search)과 의미 기반 검색(Semantic Search)의 장점을 결합하여 검색 정확도를 높이는 기법"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

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

## What I Worked On

- 하이브리드 검색과 리랭킹
- 하이브리드 검색
- 키워드 검색(Sparse Retriever):
- 의미 검색(Dense Retriever):
- Prompt the user for the OpenAI API key securely

## Implementation Flow

1. 하이브리드 검색과 리랭킹
2. 하이브리드 검색
3. 키워드 검색(Sparse Retriever):
4. 의미 검색(Dense Retriever):
5. Prompt the user for the OpenAI API key securely
6. 1. 샘플 데이터

## Code Highlights

### 의미 검색(Dense Retriever):

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

### Re-ranking 단계 (Cross-Encoder):

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
