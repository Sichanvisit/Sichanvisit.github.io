---
title: "AI Agent 맛보기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 AI_Agent_맛보기"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 AI_Agent_맛보기.md"
excerpt: "AI Agent 맛보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 AI Agent: 실시간 웹 검색... 순서로 핵심 장면을 먼저 훑고, ReAct 에이전트란?, 검색 도구 및 에이전트 생성, 에이전트 테스트 (실시간 검색) 같은 코드로 실제..."
research_summary: "AI Agent 맛보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 AI Agent: 실시간 웹 검색... 순서로 핵심 장면을 먼저 훑고, ReAct 에이전트란?, 검색 도구 및 에이전트 생성, 에이전트 테스트 (실시간 검색) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 6개 코드 블록, 4개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_openai, langchain_community입니다."
research_artifacts: "ipynb/md · 코드 6개 · 실행 4개"
code_block_count: 6
execution_block_count: 4
research_focus:
  - "AI Agent: 실시간 웹 검색 에이전트 (ReAct:Reasoning + Acting)"
research_stack:
  - "os"
  - "getpass"
  - "langchain_openai"
  - "langchain_community"
  - "langgraph"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

AI Agent 맛보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 AI Agent: 실시간 웹 검색... 순서로 핵심 장면을 먼저 훑고, ReAct 에이전트란?, 검색 도구 및 에이전트 생성, 에이전트 테스트 (실시간 검색) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 6개 코드 블록, 4개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_openai, langchain_community입니다.

**빠르게 볼 수 있는 포인트**: AI Agent: 실시간 웹 검색 에이전트 (ReAct:Reasonin....

**남겨둔 자료**: `ipynb/md` 원본과 6개 코드 블록, 4개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_openai, langchain_community입니다.

**주요 스택**: `os`, `getpass`, `langchain_openai`, `langchain_community`, `langgraph`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 6 |
| Execution Cells | 4 |
| Libraries | `os`, `getpass`, `langchain_openai`, `langchain_community`, `langgraph`, `langchain_core` |
| Source Note | `3-5 AI_Agent_맛보기` |

## What This Note Covers

### AI Agent: 실시간 웹 검색 에이전트 (ReAct:Reasoning + Acting)

AI 에이전트(AI Agent)란?, ReAct 에이전트란?, 에이전트 테스트 (실시간 검색) 같은 코드를 직접 따라가며 AI Agent: 실시간 웹 검색 에이전트 (ReAct:Reasoning + Acting) 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: AI 에이전트(AI Agent)란?, ReAct 에이전트란?, 에이전트 테스트 (실시간 검색)

#### AI 에이전트(AI Agent)란?

단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, 에이전트(Agent)는 스스로 계획을 세우고 도구(Tool)를 사용하여 실제 행동을 합니다. 에이전트의 핵심 작동 원리: 에이전트는 ReAct (Reasoning + Acting) 방식을 주로 사용합니다.

#### ReAct 에이전트란?

ReAct (Reasoning + Acting)는 AI가 스스로 "생각(Reasoning)"하고, 필요한 "행동(Acting, 도구 사용)"을 결정하는 패턴입니다. LangGraph 맛보기 실습: 노드와 조건부 엣지를 우리가 직접 연결했습니다. (수동)

#### 에이전트 테스트 (실시간 검색)

LLM은 최신 정보를 모릅니다(예: 오늘 날씨, 최근 뉴스 등). 하지만 이 에이전트는 검색 도구를 사용해 답변해냅니다.

## Why This Matters

### 에이전트 상태 흐름

- 왜 필요한가: 단일 호출만으로 해결되지 않는 작업은 추론, 도구 호출, 중간 상태 관리가 이어지는 흐름 제어가 필요합니다.
- 왜 이 방식을 쓰는가: 상태 그래프 기반 접근은 단계별 분기와 재시도를 명시적으로 관리할 수 있어 에이전트 실험을 설명하기 좋습니다.
- 원리: 현재 상태를 노드 간에 전달하면서, 조건에 따라 다음 노드나 도구 호출을 결정하는 방식으로 실행 흐름이 이어집니다.

### 프롬프트 체인 구성

- 왜 필요한가: LLM 호출을 재현 가능하게 만들려면 입력 조합, 프롬프트 템플릿, 후처리 순서를 구조화할 필요가 있습니다.
- 왜 이 방식을 쓰는가: 체인 구조는 실험 중 프롬프트와 입력 변형을 비교하기 쉽고, 이후 RAG나 에이전트 단계로 확장하기도 좋습니다.
- 원리: 질문과 컨텍스트를 정해진 템플릿에 넣고, 모델 호출 결과를 다음 단계 입력으로 넘기며 처리 흐름을 구성합니다.

## Implementation Flow

1. AI Agent: 실시간 웹 검색 에이전트 (ReAct:Reasoning + Acting): AI 에이전트(AI Agent)란?, ReAct 에이전트란?

## Code Highlights

### ReAct 에이전트란?

`ReAct 에이전트란?`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 라이브러리 설치 흐름이 주석과 함께 드러납니다.

```python
# 1. 라이브러리 설치
!pip install -qU langgraph langchain-openai langchain-community duckduckgo-search ddgs
```

### 검색 도구 및 에이전트 생성

`검색 도구 및 에이전트 생성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 LLM 정의, 도구(Tool) 정의 - 실제 웹 검색 도구 사용, DuckDuckGoSearchRun은 API Key 없이 무료로 검색 가능한 도구입니다.... 흐름이 주석과 함께 드러납니다.

```python
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

# 1. LLM 정의
llm = ChatOpenAI(model="gpt-4o-mini")

# 2. 도구(Tool) 정의 - 실제 웹 검색 도구 사용
# DuckDuckGoSearchRun은 API Key 없이 무료로 검색 가능한 도구입니다.: https://start.duckduckgo.com/
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

# 3. 미리 만들어진 ReAct 에이전트 생성
# LangGraph create_react_agent가 내부적으로 노드, 엣지, 분기 로직을 모두 자동으로 설정해줍니다.
agent_executor = create_react_agent(llm, tools)

print("---검색 에이전트 생성 완료!")
```

### 에이전트 테스트 (실시간 검색)

`에이전트 테스트 (실시간 검색)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 테스트 1 실행, 최신 정보가 필요한 질문 (LLM 학습 데이터에 없는 내용) 흐름이 주석과 함께 드러납니다.

```python
# --- 테스트 1 실행 ---
# 1. 최신 정보가 필요한 질문 (LLM 학습 데이터에 없는 내용)
run_agent("2025년 11월 현재 주요 뉴스는 뭐야?")
```

### 에이전트 테스트 (실시간 검색)

`에이전트 테스트 (실시간 검색)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 테스트 2 실행, 일반 상식 질문 (검색 없이 대답 가능한지 확인) 흐름이 주석과 함께 드러납니다.

```python
# --- 테스트 2 실행 ---
# 2. 일반 상식 질문 (검색 없이 대답 가능한지 확인)
run_agent("사과는 영어로 뭐야?")
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 AI_Agent_맛보기.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 AI_Agent_맛보기.ipynb`, `3-5 AI_Agent_맛보기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `start.duckduckgo.com`

## Note Preview

> 단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, **에이전트(Agent)**는 스스로 계획을 세우고 **도구(Tool)**를 사용하여 실제 행동을 합니다.
> - 에이전트의 핵심 작동 원리: 에이전트는 ReAct (Reasoning + Acting) 방식을 주로 사용합니다.
