---
title: "LangChain활용"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)LangChain활용"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)LangChain활용.md"
excerpt: "LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소(프롬프트 템플릿, 체인, 메모리, 툴 호출 등)를 결합하여 하나의 완성된 애플리케이션 형태로 구성할 수 있는 단계별 워크플로우 프레임워크입니다. 또한 OpenAI, Hugging Face 등 주요 LLM 플랫폼과 손쉽게 연동할..."
research_summary: "LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소(프롬프트 템플릿, 체인, 메모리, 툴 호출 등)를 결합하여 하나의 완성된 애플리케이션 형태로 구성할 수 있는 단계별 워크플로우 프레임워크입니다. 또한 OpenAI, Hugging Face 등 주요 LLM 플랫폼과 손쉽게 연동할 수 있어 확장성이 뛰어납니다. LangChain은 입력된 프롬프트를 탬플릿화 시키고 불러온 LLM 모델과 연결하여 단계별 워크플로우를 하나의 프로세스로 합쳐 줍니다. 단계별 워크플로우. `ipynb/md` 원본과 10개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 getpass, langchain_openai, os, langchain_core입니다."
research_artifacts: "ipynb/md · 코드 10개 · 실행 6개"
code_block_count: 10
execution_block_count: 6
research_focus:
  - "LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소(프롬프트 템플릿, 체인, 메모리..."
  - "LangChain을 활용한 RAG 실습"
  - "필요 라이브러리 설치"
research_stack:
  - "getpass"
  - "langchain_openai"
  - "os"
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

LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소(프롬프트 템플릿, 체인, 메모리, 툴 호출 등)를 결합하여 하나의 완성된 애플리케이션 형태로 구성할 수 있는 단계별 워크플로우 프레임워크입니다. 또한 OpenAI, Hugging Face 등 주요 LLM 플랫폼과 손쉽게 연동할 수 있어 확장성이 뛰어납니다. LangChain은 입력된 프롬프트를 탬플릿화 시키고 불러온 LLM 모델과 연결하여 단계별 워크플로우를 하나의 프로세스로 합쳐 줍니다. 단계별 워크플로우. `ipynb/md` 원본과 10개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 getpass, langchain_openai, os, langchain_core입니다.

**빠르게 볼 수 있는 포인트**: LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소..., LangChain을 활용한 RAG 실습, 필요 라이브러리 설치.

**남겨둔 자료**: `ipynb/md` 원본과 10개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 getpass, langchain_openai, os, langchain_core입니다.

**주요 스택**: `getpass`, `langchain_openai`, `os`, `langchain_core`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 10 |
| Execution Cells | 6 |
| Libraries | `getpass`, `langchain_openai`, `os`, `langchain_core` |
| Source Note | `3-5 (실습)LangChain활용` |

## What This Note Covers

### LangChain을 활용한 RAG 실습

LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소(프롬프트 템플릿, 체인, 메모리, 툴 호출 등)를 결합하여 하나의 완성된 애플리케이션 형태로 구성할 수 있는 단계별 워크플로우 프레임워크입니다. 또한 OpenAI, Hugging Face 등 주요 LLM 플랫폼과 손쉽게 연동할 수 있어 확장성이 뛰어납니다.

### LangChain을 활용한 RAG 실습 > LangChain 프롬프트 엔지니어링

LangChain은 입력된 프롬프트를 탬플릿화 시키고 불러온 LLM 모델과 연결하여 단계별 워크플로우를 하나의 프로세스로 합쳐 줍니다. 단계별 워크플로우

### LangChain 프롬프트 엔지니어링 > 프롬프트 템플릿 생성

langchain_core.prompts 모듈은 PromptTemplate 객체를 제공하여 사용자가 입력한 프롬프트에 적절한 템플릿을 덮어 씌워 모델에 입력할수 있게 도와줍니다. 이때 PromptTemplate에 입력되는 문자열 안에 {변수이름}형식으로 수정 가능한 변수를 할당할 수 있습니다.

### LangChain 프롬프트 엔지니어링 > LLM - Prompt 체인 만들기 (LCEL 방식)

LangChain에서는 기존의 LLMChain.run() 방식 대신, LangChain Expression Language(LCEL)을 사용해 프롬프트 → LLM → 출력 파싱 과정을 하나의 체인으로 간단히 구성할 수 있습니다. summary_prompt / llm / StrOutputParser() 형태로 체인을 만들고, .invoke()에 사용자 입력을 넣으면 최종 생성 텍스트가 반...

## Why This Matters

### RAG 검색 파이프라인

- 왜 필요한가: LLM이 외부 지식을 안정적으로 참조하게 하려면, 생성 전에 관련 문서를 정확히 찾아오는 검색 단계가 먼저 필요합니다.
- 왜 이 방식을 쓰는가: 이 방식은 모델 파라미터만 믿지 않고 최신 문서나 도메인 지식을 붙일 수 있어서 실제 서비스형 QA에 적합합니다.
- 원리: 문서를 청크로 나누고 임베딩한 뒤, 질문과 가까운 벡터를 검색해 프롬프트에 함께 넣는 구조로 동작합니다.

### 프롬프트 체인 구성

- 왜 필요한가: LLM 호출을 재현 가능하게 만들려면 입력 조합, 프롬프트 템플릿, 후처리 순서를 구조화할 필요가 있습니다.
- 왜 이 방식을 쓰는가: 체인 구조는 실험 중 프롬프트와 입력 변형을 비교하기 쉽고, 이후 RAG나 에이전트 단계로 확장하기도 좋습니다.
- 원리: 질문과 컨텍스트를 정해진 템플릿에 넣고, 모델 호출 결과를 다음 단계 입력으로 넘기며 처리 흐름을 구성합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. LangChain을 활용한 RAG 실습: LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소(프롬프트 템플릿, 체인, 메모리, 툴 호출 등)를 결합하여 하나의 완성된 애플리케이션 형태로 구성할 수 있는 단계별 워크플로우 프레임워크입니다. 또한 OpenAI, Hugging Face...
2. LangChain을 활용한 RAG 실습 > LangChain 프롬프트 엔지니어링: LangChain은 입력된 프롬프트를 탬플릿화 시키고 불러온 LLM 모델과 연결하여 단계별 워크플로우를 하나의 프로세스로 합쳐 줍니다. 단계별 워크플로우
3. LangChain 프롬프트 엔지니어링 > 프롬프트 템플릿 생성: langchain_core.prompts 모듈은 PromptTemplate 객체를 제공하여 사용자가 입력한 프롬프트에 적절한 템플릿을 덮어 씌워 모델에 입력할수 있게 도와줍니다. 이때 PromptTemplate에 입력되는 문자열 안에...
4. LangChain 프롬프트 엔지니어링 > LLM - Prompt 체인 만들기 (LCEL 방식): LangChain에서는 기존의 LLMChain.run() 방식 대신, LangChain Expression Language(LCEL)을 사용해 프롬프트 → LLM → 출력 파싱 과정을 하나의 체인으로 간...

## Code Highlights

### LLM - Prompt 체인 만들기 (LCEL 방식)

`LLM - Prompt 체인 만들기 (LCEL 방식)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Using LangChain Expression Language (LCEL) to cre..., 사용자 프롬프트, 사용자 프롬프트를 체인에 입력 흐름이 주석과 함께 드러납니다.

```python
from langchain_core.output_parsers import StrOutputParser

# Using LangChain Expression Language (LCEL) to create the chain
summary_chain = summary_prompt | llm | StrOutputParser()

# 사용자 프롬프트
text_to_summarize = """
[데일리안 = 조인영 기자] 우리나라 앱 개발자가 앱 마켓사업자에게서 경험하는 주요 불공정 사례는 심사 지연과 등록 거부이며, 앱 내 결제(인앱결제)의 가장 큰 문제점은 ‘과도한 수수료’라고 인식하고 있는 것으로 나타났다.

방송통신위원회와 한국인터넷진흥원은 11일 '전기통신사업법' 제22조의9(앱 마켓사업자의 의무 및 실태조사)에 따른 ‘2024년도 앱 마켓 실태조사 결과’를 발표했다.

2023년도 국내 ‘앱 마켓’ 규모는 거래액 기준으로 8조1952억원으로 2022년 8조 7598억원 대비 6.4% 감소했다

각 사업자별로 보면, 애플 앱스토어(10.1%)와 삼성전자 갤럭시스토어(6.3%)는 전년 대비 매출이 증가했으며, 구글 플레이(△10.1%)와 원스토어(△21.6%)는 감소했다.

4개 앱 마켓사업자의 거래액 대비 수수료 비중은 약 14~26% 수준이며, 앱 등록 매출의 경우 애플 앱스토어는 약 9.4% 증가했고 구글 플레이는 약 12.9% 감소했다.

또한 국내 앱 마켓에 등록된 전체 앱 수는 전년 대비 0.1% 증가한 531만8182개(각 앱 마켓별 중복 포함), 앱 개발자 수는 전년 대비 0.65% 적은 163만6655명(각 앱 마켓별 중복 포함)으로 나타났다.

분야별 앱 등록 비중은 사진‧도구(26.1%), 라이프스타일(15.6%), 미디어‧출판(14.5%) 관련 앱이 전체의 56.2%를 차지했다.

국내 앱 개발자가 이용하는 앱 마켓은 구글 플레이(96.4%), 애플 앱스토어(71.3%) 순(중복포함)이며, 매출액 비중도 구글 플레이가 67.5%로 가장 높았다. 그 를 애플 앱스토어(28.2%), 원스토어(2.9%), 갤럭시스토어(1.5%)가 따랐다.

앱 개발자가 느끼는 주요 불공정 사례로는 앱 심사지연 경험(애플 앱스토어 6.8%, 구글 플레이 26.2%)이 가장 높았으며, 앱 등록 거부 경험(애플 20%, 구글 3%)과 앱 삭제 경험(구글 8.2%, 애플 3.2%)이 그 뒤를 이었다.

앱 내 결제의 가장 큰 문제점은 ‘과도한 수수료’라고 답한 앱 개발자가 0.4%로 가장 높게 나타났으며, 다음으로 ‘환불 등 수익 정산의 불명확함’(11.6%), ‘결제 수단 선택 제한’(8.9%) 순으로 조사됐다.

앱 개발자가 느낀 앱 최초 등록 과정상의 어려움으로는 ‘심사 기준이 확하지 않음’(구글 플레이 29.8%, 애플 앱스토어 29.6%), ‘질의에 대한 드백 지연’(각각 26.1%, 25.3%) 등이 꼽혔다.
# ... trimmed ...
```

### 롤 토큰 Chat 템플릿

`롤 토큰 Chat 템플릿`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ChatPromptTemplate 생성: 시스템/사용자 메시지 정의, LCEL( LangChain Expression Language )을 이용한 체인 구성, 프롬프트 → LLM → 문자열 파서 로 이어지는 파이프라인 구성 흐름이 주석과 함께 드러납니다.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ChatPromptTemplate 생성: 시스템/사용자 메시지 정의
chat_template = ChatPromptTemplate([
    ("system", "당신은 질문의 상황에 적절한 인공지능 모델을 찾아주는 AI 전문가입니다"),
    ("user", "다음 상황에 맞는 모델을 찾아줘 \n{input}")
])

# LCEL( LangChain Expression Language )을 이용한 체인 구성
# 프롬프트 → LLM → 문자열 파서 로 이어지는 파이프라인 구성
chat_chain = chat_template | llm | StrOutputParser()

# 체인을 실행할 때는 딕셔너리 형태로 변수(input)을 전달
response = chat_chain.invoke({"input": "우리는 CCTV에 범죄 상황을 인지하기 위한 기능을 넣으려고 한다"})
print("[응답]\n", response)
```

### 메모리 활용

`메모리 활용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기본 체인: 프롬프트 → LLM, 세션별로 메모리(대화 기록)를 관리할 저장소, RunnableWithMessageHistory로 "메모리 있는 체인" 만들기 흐름이 주석과 함께 드러납니다.

```python
# 3) 기본 체인: 프롬프트 → LLM
base_chain = prompt | llm

# 4) 세션별로 메모리(대화 기록)를 관리할 저장소
store = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 5) RunnableWithMessageHistory로 "메모리 있는 체인" 만들기
llm_chain_with_history = RunnableWithMessageHistory(
    base_chain,
    get_session_history,
    input_messages_key="user_input",  # 입력에서 어떤 key를 user 메시지로 쓸지
    history_messages_key="history",   # 프롬프트의 MessagesPlaceholder 이름
)
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 (실습)LangChain활용.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 (실습)LangChain활용.ipynb`, `3-5 (실습)LangChain활용.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소(프롬프트 템플릿, 체인, 메모리, 툴 호출 등)를 결합하여 하나의 완성된 애플리케이션 형태로 구성할 수 있는 단계별 워크플로우 프레임워크입니다.
> 또한 OpenAI, Hugging Face 등 주요 LLM 플랫폼과 손쉽게 연동할 수 있어 확장성이 뛰어납니다.
