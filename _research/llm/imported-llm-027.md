---
title: "한국어 FAQ 챗봇 LangSmith"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)한국어_FAQ_챗봇_LangSmith"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)한국어_FAQ_챗봇_LangSmith.md"
excerpt: "LangChain의 핵심 컴포넌트 이해 및 활용 2"
research_summary: "LangChain의 핵심 컴포넌트 이해 및 활용 2. RAG(Retrieval Augmented Generation) 시스템 구축 3. LangSmith를 통한 모니터링 및 디버깅: 로그인후에 API 키 생성 - https://smith.langchain.com/ 4. 실전 FAQ 챗봇 개발. IT 회사 FAQ 챗봇: 직원들의 자주 묻는 질문에 자동으로 답변하는 시스템. `ipynb/md` 원본과 17개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_openai, langchain_core입니다."
research_artifacts: "ipynb/md · 코드 17개 · 실행 15개"
code_block_count: 17
execution_block_count: 15
research_focus:
  - "LangChain & LangSmith 실습"
  - "LangChain의 핵심 컴포넌트 이해 및 활용 2. RAG(Retrieval Augmented Gen..."
  - "학습 목표"
research_stack:
  - "os"
  - "getpass"
  - "langchain_openai"
  - "langchain_core"
  - "langchain_community"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

LangChain의 핵심 컴포넌트 이해 및 활용 2. RAG(Retrieval Augmented Generation) 시스템 구축 3. LangSmith를 통한 모니터링 및 디버깅: 로그인후에 API 키 생성 - https://smith.langchain.com/ 4. 실전 FAQ 챗봇 개발. IT 회사 FAQ 챗봇: 직원들의 자주 묻는 질문에 자동으로 답변하는 시스템. `ipynb/md` 원본과 17개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_openai, langchain_core입니다.

**빠르게 볼 수 있는 포인트**: LangChain & LangSmith 실습, LangChain의 핵심 컴포넌트 이해 및 활용 2. RAG(Retri..., 학습 목표.

**남겨둔 자료**: `ipynb/md` 원본과 17개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_openai, langchain_core입니다.

**주요 스택**: `os`, `getpass`, `langchain_openai`, `langchain_core`, `langchain_community`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 17 |
| Execution Cells | 15 |
| Libraries | `os`, `getpass`, `langchain_openai`, `langchain_core`, `langchain_community`, `operator`, `gradio` |
| Source Note | `3-5 (실습)한국어_FAQ_챗봇_LangSmith` |

## What This Note Covers

### 학습 목표

LangChain의 핵심 컴포넌트 이해 및 활용 2. RAG(Retrieval Augmented Generation) 시스템 구축 3. LangSmith를 통한 모니터링 및 디버깅: 로그인후에 API 키 생성 - https://smith.langchain.com/ 4. 실전 FAQ 챗봇 개발

### 시나리오

IT 회사 FAQ 챗봇: 직원들의 자주 묻는 질문에 자동으로 답변하는 시스템

### Step 2: FAQ 데이터 준비

실제 회사에서 사용할 법한 HR FAQ 데이터를 준비합니다.

### Step 3: 기본 LangChain 챗봇 (RAG 없이)

먼저 간단한 LLM 기반 챗봇을 만들어봅니다.

## Implementation Flow

1. 학습 목표: LangChain의 핵심 컴포넌트 이해 및 활용 2. RAG(Retrieval Augmented Generation) 시스템 구축 3. LangSmith를 통한 모니터링 및 디버깅: 로그인후에 API 키 생성 - https://smith.langchain.com/ 4. 실전 FAQ 챗봇 개발
2. 시나리오: IT 회사 FAQ 챗봇: 직원들의 자주 묻는 질문에 자동으로 답변하는 시스템
3. Step 2: FAQ 데이터 준비: 실제 회사에서 사용할 법한 HR FAQ 데이터를 준비합니다.
4. Step 3: 기본 LangChain 챗봇 (RAG 없이): 먼저 간단한 LLM 기반 챗봇을 만들어봅니다.

## Code Highlights

### Step 6: 대화 기록 기능 추가 (Memory)

`Step 6: 대화 기록 기능 추가 (Memory)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 LLM & retriever 준비, HR FAQ RAG 프롬프트 (대화 기록 + 컨텍스트 + 질문), base_rag_chain: question + chat_history → context... 흐름이 주석과 함께 드러납니다.

```python
from operator import itemgetter

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_openai import ChatOpenAI

# 1) LLM & retriever 준비
llm = ChatOpenAI(model="gpt-4o-mini")  # 예시, 이미 있으시면 이건 생략
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 2) HR FAQ RAG 프롬프트 (대화 기록 + 컨텍스트 + 질문)
rag_template = """당신은 회사의 HR 챗봇입니다.
아래 제공된 FAQ 정보를 바탕으로 직원의 질문에 정확하고 친절하게 답변해주세요.

FAQ 정보:
{context}

질문: {question}

답변 가이드:
1. FAQ에 정확한 답변이 있으면 그대로 전달하세요
2. FAQ에 없는 내용이면 "정확한 정보는 인사팀(내선 1234)으로 문의해주세요"라고 안내하세요
3. 친절하고 전문적인 톤을 유지하세요

답변:"""

# ... trimmed ...
```

### Step 8: 실전 배포를 위한 추가 기능

`Step 8: 실전 배포를 위한 추가 기능`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 질문 문자열 하나만 넣기, 참고 문서에서 FAQ 질문 타이틀 뽑기 흐름이 주석과 함께 드러납니다.

```python
import gradio as gr

def chatbot_interface(message, history):
    """Gradio 챗봇 인터페이스"""
    # 질문 문자열 하나만 넣기
    result = qa_chain.invoke(message)

    answer = result["answer"]

    # 참고 문서에서 FAQ 질문 타이틀 뽑기
    sources = [
        doc.metadata.get("question", "N/A")
        for doc in result.get("source_documents", [])
    ]

    if sources:
        answer += "\n\n📚 참고한 FAQ:\n" + "\n".join(
            [f"- {s}" for s in sources[:2]]
        )

    return answer

demo = gr.ChatInterface(
    fn=chatbot_interface,
    title="🏢 HR FAQ 챗봇",
    description="회사 HR 관련 질문을 해보세요!",
    examples=[
        "연차는 어떻게 신청하나요?",
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 (실습)한국어_FAQ_챗봇_LangSmith.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 (실습)한국어_FAQ_챗봇_LangSmith.ipynb`, `3-5 (실습)한국어_FAQ_챗봇_LangSmith.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `smith.langchain.com`, `localhost`, `www.gradio.app`, `python.langchain.com`, `docs.smith.langchain.com`

## Note Preview

> 1. LangChain의 핵심 컴포넌트 이해 및 활용 2. RAG(Retrieval Augmented Generation) 시스템 구축 3. LangSmith를 통한 모니터링 및 디버깅: 로그인후에 API 키 생성 - https://smith.langchain.com/ 4. 실전 FAQ 챗봇 개발
> IT 회사 FAQ 챗봇: 직원들의 자주 묻는 질문에 자동으로 답변하는 시스템
