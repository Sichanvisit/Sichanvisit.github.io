---
title: "멀티 벡터 검색"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)멀티_벡터_검색"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)멀티_벡터_검색.md"
excerpt: "LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋"
research_summary: "LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 19개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 langchain, os, uuid, getpass입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 16개"
code_block_count: 19
execution_block_count: 16
research_focus:
  - "LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋"
  - "멀티 벡터 검색 (Multi-Vector Retrieval) 실습"
  - "💡 멀티 벡터 검색이란?"
research_stack:
  - "langchain"
  - "os"
  - "uuid"
  - "getpass"
  - "datasets"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 19개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 langchain, os, uuid, getpass입니다.

**빠르게 볼 수 있는 포인트**: LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋, 멀티 벡터 검색 (Multi-Vector Retrieval) 실습, 💡 멀티 벡터 검색이란?.

**남겨둔 자료**: `ipynb/md` 원본과 19개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 langchain, os, uuid, getpass입니다.

**주요 스택**: `langchain`, `os`, `uuid`, `getpass`, `datasets`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 19 |
| Execution Cells | 16 |
| Libraries | `langchain`, `os`, `uuid`, `getpass`, `datasets`, `langchain_openai`, `langchain_core`, `langchain_chroma` |
| Source Note | `3-5 (실습)멀티_벡터_검색` |

## What This Note Covers

### 멀티 벡터 검색 (Multi-Vector Retrieval) 실습

LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋

### Key Step

LangChain 1.0+ 및 필요 라이브러리 설치

### Key Step

실습 - 요약으로 검색 → 원본 반환

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

1. 멀티 벡터 검색 (Multi-Vector Retrieval) 실습: LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋
2. Key Step: LangChain 1.0+ 및 필요 라이브러리 설치
3. Key Step: 실습 - 요약으로 검색 → 원본 반환

## Code Highlights

### 멀티 벡터 시스템 초기화

`멀티 벡터 시스템 초기화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 parent 문서 저장 (docstore 역할), 예: docstore = { "A": Document(...), "B": Document..., MultiVectorRetriever 기능 구현 흐름이 주석과 함께 드러납니다.

```python
from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda

# -------------------------------------------------------
# 1) parent 문서 저장 (docstore 역할)
# -------------------------------------------------------
# 예: docstore = { "A": Document(...), "B": Document(...) }
parent_store = docstore

# -------------------------------------------------------
# 2) MultiVectorRetriever 기능 구현
#    - child 벡터 저장소 = vectorstore
#    - parent 문서 = parent_store
#    - id_key = "doc_id"
# -------------------------------------------------------
def multivector_retrieve(query):
    # 1. child 문서 검색
    child_docs = vectorstore.similarity_search(query, k=5)

    # 2. child -> parent id 매핑
    parent_ids = {doc.metadata["doc_id"] for doc in child_docs}

    # 3. parent 문서 반환
    parent_docs = [parent_store[id] for id in parent_ids in id in parent_store]

    return parent_docs

# LCEL Runnable 형태의 retriever 만들기 (MultiVectorRetriever 대체)
# ... trimmed ...
```

### 문서 인덱싱 (요약 → 원본 매핑)

`문서 인덱싱 (요약 → 원본 매핑)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 고유 ID 생성, 원본 문서 (DocStore 저장용), 요약 문서 (VectorStore 검색용) 흐름이 주석과 함께 드러납니다.

```python
import uuid
from langchain_core.documents import Document

doc_ids = []
summary_docs = []
full_docs = []

for idx, item in enumerate(data):
    # 고유 ID 생성
    doc_id = str(uuid.uuid4())
    doc_ids.append(doc_id)

    # -------------------------
    # 1) 원본 문서 (DocStore 저장용)
    # -------------------------
    full_doc = Document(
        page_content=item['document'],
        metadata={
            "doc_id": doc_id,
            "title": item.get('title', f'뉴스_{idx}'),
            "type": "full_document"
        }
    )
    full_docs.append(full_doc)

    # -------------------------
    # 2) 요약 문서 (VectorStore 검색용)
    # -------------------------
# ... trimmed ...
```

### RAG 시스템 구축

`RAG 시스템 구축`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 문서 검색, 컨텍스트 생성, 답변 생성 흐름이 주석과 함께 드러납니다.

```python
def ask_question(question, k=3):
    print("질문: {question}")
    print("="*80)

    # 문서 검색
    docs = retriever.invoke({"query": question, "k":k})
    print(f"검색 완료")

    if not docs:
        print("관련 문서를 찾지 못했습니다")
        return None

    for i, doc in enumerate(docs, 1):
        print(f"  {i}. {doc.metadata.get('title', 'N/A')[:60]}")

    # 컨텍스트 생성
    context = "\n".join([
        f"[기사 {i+1}] {doc.metadata.get('title', '')}\n{doc.page_content}"
        for i, doc in enumerate(docs)
    ])

    # 답변 생성
    print(f"\n GPT-4o-mini 답변 생성중")
    answer = rag_chain.invoke({"context": context, "question": question})


    print("\n" + "="*80)
    print(" 답변:")
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 (실습)멀티_벡터_검색.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 (실습)멀티_벡터_검색.ipynb`, `3-5 (실습)멀티_벡터_검색.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> **LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋**
> ---
