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

1. 학습 목표: LangChain의 핵심 컴포넌트 이해 및 활용 2. RAG(Retrieval Augmented Generation) 시스템 구축 3. LangSmith를 통한 모니터링 및 디버깅: 로그인후에 API 키 생성 - https://smith.langchain.com/ 4. 실전 FAQ 챗봇 개발
2. 시나리오: IT 회사 FAQ 챗봇: 직원들의 자주 묻는 질문에 자동으로 답변하는 시스템
3. Step 2: FAQ 데이터 준비: 실제 회사에서 사용할 법한 HR FAQ 데이터를 준비합니다.
4. Step 3: 기본 LangChain 챗봇 (RAG 없이): 먼저 간단한 LLM 기반 챗봇을 만들어봅니다.

## Code Highlights

### Step 2: FAQ 데이터 준비

`Step 2: FAQ 데이터 준비`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 FAQ 데이터 (실제로는 파일이나 DB에서 가져옴) 흐름이 주석과 함께 드러납니다.

```python
# FAQ 데이터 (실제로는 파일이나 DB에서 가져옴)
faq_data = [
    {
        "질문": "연차는 어떻게 신청하나요?",
        "답변": "연차 신청은 사내 그룹웨어의 '전자결재' 메뉴에서 '휴가신청서'를 작성하면 됩니다. 최소 3일 전에 신청해야 하며, 팀장의 승인이 필요합니다. 긴급한 경우 전화로 먼저 알리고 사후 처리도 가능합니다."
    },
    {
        "질문": "월급날은 언제인가요?",
        "답변": "급여는 매월 25일에 지급됩니다. 25일이 주말이나 공휴일인 경우, 그 전 영업일에 지급됩니다. 급여명세서는 급여일 오전에 이메일로 발송됩니다."
    },
    {
        "질문": "재택근무 신청 방법을 알려주세요",
        "답변": "재택근무는 주 2회까지 가능합니다. 전날 오후 6시까지 팀장에게 슬랙으로 신청하면 됩니다. 재택근무 중에도 오전 10시-오후 5시는 업무 가능 상태여야 하며, 화상회의 참석이 가능해야 합니다."
    },
    {
        "질문": "건강검진은 언제 받나요?",
        "답변": "연간 건강검진은 입사 기념월에 받을 수 있습니다. 회사가 지정한 병원 리스트 중에서 선택 가능하며, 비용은 회사에서 전액 지원합니다. 인사팀으로 연락하시면 예약을 도와드립니다."
    },
    {
        "질문": "야근 수당은 어떻게 되나요?",
        "답변": "평일 오후 7시 이후 근무에 대해서는 야근 수당이 지급됩니다. 그룹웨어에서 야근 신청을 하고 팀장 승인을 받아야 합니다. 야근 수당은 시간당 기본급의 1.5배로 계산되며, 다음 달 급여에 포함됩니다."
    },
    {
        "질문": "경조사 휴가 기준은?",
        "답변": "경조사 휴가는 다음과 같이 제공됩니다. 본인 결혼: 5일, 자녀 결혼: 1일, 부모/배우자 부모 사망: 5일, 조부모/형제자매 사망: 3일. 경조사 발생 시 인사팀에 경조사 증빙서류를 제출해주세요."
    },
    {
        "질문": "점심시간은 몇 시부터 몇 시까지인가요?",
# ... trimmed ...
```

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
