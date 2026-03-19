---
title: "LangChain활용"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)LangChain활용"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)LangChain활용.md"
excerpt: "LangChain은 LLM에 입력되는 프롬프트에 다양한 엔지니어링 요소(프롬프트 템플릿, 체인, 메모리, 툴 호출 등)를 결합하여 하나의 완성된 애플리케이션 형태로 구성할 수 있는 단계별 워크플로우 프레임워크입니다."
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
| Execution Cells | 6 |
| Libraries | `getpass`, `langchain_openai`, `os`, `langchain_core` |
| Source Note | `3-5 (실습)LangChain활용` |

## What I Worked On

- LangChain을 활용한 RAG 실습
- 필요 라이브러리 설치
- LangChain 프롬프트 엔지니어링
- OpenAI API key
- API키 설정

## Implementation Flow

1. LangChain을 활용한 RAG 실습
2. 필요 라이브러리 설치
3. LangChain 프롬프트 엔지니어링
4. OpenAI API key
5. API키 설정
6. 모델 로드

## Code Highlights

### LLM - Prompt 체인 만들기 (LCEL 방식)

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

### 메모리 활용

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
