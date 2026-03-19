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
