---
title: "AI Agent 맛보기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 AI_Agent_맛보기"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 AI_Agent_맛보기.md"
excerpt: "단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, 에이전트(Agent)는 스스로 계획을 세우고 도구(Tool)를 사용하여 실제 행동을 합니다"
research_summary: "단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, 에이전트(Agent)는 스스로 계획을 세우고 도구(Tool)를 사용하여 실제 행동을 합니다. ReAct (Reasoning + Acting)는 AI가 스스로 \"생각(Reasoning)\"하고, 필요한 \"행동(Acting, 도구 사용)\"을 결정하는 패턴입니다. `ipynb/md` 원본과 6개 코드 블록, 4개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_openai, langchain_community입니다."
research_artifacts: "ipynb/md · 코드 6개 · 실행 4개"
code_block_count: 6
execution_block_count: 4
research_focus:
  - "AI Agent"
  - "단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, 에이전트(Agent)는 스스로 계..."
  - "AI 에이전트(AI Agent)란?"
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

단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, 에이전트(Agent)는 스스로 계획을 세우고 도구(Tool)를 사용하여 실제 행동을 합니다. ReAct (Reasoning + Acting)는 AI가 스스로 "생각(Reasoning)"하고, 필요한 "행동(Acting, 도구 사용)"을 결정하는 패턴입니다. `ipynb/md` 원본과 6개 코드 블록, 4개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_openai, langchain_community입니다.

**빠르게 볼 수 있는 포인트**: AI Agent, 단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만,..., AI 에이전트(AI Agent)란?.

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

### AI 에이전트(AI Agent)란?

단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, 에이전트(Agent)는 스스로 계획을 세우고 도구(Tool)를 사용하여 실제 행동을 합니다.

### ReAct 에이전트란?

ReAct (Reasoning + Acting)는 AI가 스스로 "생각(Reasoning)"하고, 필요한 "행동(Acting, 도구 사용)"을 결정하는 패턴입니다.

### 검색 도구 및 에이전트 생성

여기서 중요한 점은 그래프를 구성하는 코드가 사라지고, create_react_agent 함수 하나로 대체된다는 점입니다.

### 에이전트 테스트 (실시간 검색)

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

1. AI 에이전트(AI Agent)란?: 단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, 에이전트(Agent)는 스스로 계획을 세우고 도구(Tool)를 사용하여 실제 행동을 합니다.
2. ReAct 에이전트란?: ReAct (Reasoning + Acting)는 AI가 스스로 "생각(Reasoning)"하고, 필요한 "행동(Acting, 도구 사용)"을 결정하는 패턴입니다.
3. 검색 도구 및 에이전트 생성: 여기서 중요한 점은 그래프를 구성하는 코드가 사라지고, create_react_agent 함수 하나로 대체된다는 점입니다.
4. 에이전트 테스트 (실시간 검색): LLM은 최신 정보를 모릅니다(예: 오늘 날씨, 최근 뉴스 등). 하지만 이 에이전트는 검색 도구를 사용해 답변해냅니다.

## Code Highlights

### ReAct 에이전트란?

`ReAct 에이전트란?`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 OpenAI API Key 설정 흐름이 주석과 함께 드러납니다.

```python
import os
import getpass

# 2. OpenAI API Key 설정
if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key 입력: ")
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

`에이전트 테스트 (실시간 검색)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 에이전트 실행 (스트리밍으로 과정 확인), 메시지의 마지막 내용만 출력, 도구가 실행되거나 답변이 생성될 때 출력 흐름이 주석과 함께 드러납니다.

```python
from langchain_core.messages import HumanMessage

def run_agent(question):
    print(f"\n 질문: {question}")
    print("-" * 50)

    # 에이전트 실행 (스트리밍으로 과정 확인)
    inputs = {"messages": [HumanMessage(content=question)]}

    for chunk in agent_executor.stream(inputs, stream_mode="values"):
        # 메시지의 마지막 내용만 출력
        message = chunk["messages"][-1]

        # 도구가 실행되거나 답변이 생성될 때 출력
        if message.type == "ai":
            # 도구 호출이 포함된 경우
            if message.tool_calls:
                print(f"================[생각] 검색이 필요해! -> '{message.tool_calls[0]['args']}' 검색 시도...")
            # 최종 답변인 경우
            else:
                print(f"================[답변] {message.content}")
        elif message.type == "tool":
            print(f"================[결과] 검색 완료 (내용 일부: {message.content[:100]}...)")
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
