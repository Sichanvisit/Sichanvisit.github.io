---
title: "멀티 벡터 검색"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)멀티_벡터_검색"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)멀티_벡터_검색.md"
excerpt: "**LangChain 1.0+ / GPT-4o-mini / 네이버 뉴스 데이터셋**"
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
| Code Blocks | 19 |
| Execution Cells | 16 |
| Libraries | `langchain`, `os`, `uuid`, `getpass`, `datasets`, `langchain_openai`, `langchain_core`, `langchain_chroma` |
| Source Note | `3-5 (실습)멀티_벡터_검색` |

## What I Worked On

- 멀티 벡터 검색 (Multi-Vector Retrieval) 실습
- 💡 멀티 벡터 검색이란?
- 환경 설정
- LangChain 1.0+ 및 필요 라이브러리 설치
- 버전 확인

## Implementation Flow

1. 멀티 벡터 검색 (Multi-Vector Retrieval) 실습
2. 💡 멀티 벡터 검색이란?
3. 환경 설정
4. LangChain 1.0+ 및 필요 라이브러리 설치
5. 버전 확인
6. LangChain 1.0+ imports

## Code Highlights

### 멀티 벡터 시스템 초기화

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
