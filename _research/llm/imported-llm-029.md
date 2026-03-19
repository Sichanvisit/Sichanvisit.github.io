---
title: "LangGraph 맛보기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 LangGraph_맛보기"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 LangGraph_맛보기.md"
excerpt: "LangGraph는 LLM 애플리케이션에 \"순환(Loop)\"과 \"제어(Control)\" 기능을 부여하는 라이브러리입니다"
research_summary: "LangGraph는 LLM 애플리케이션에 \"순환(Loop)\"과 \"제어(Control)\" 기능을 부여하는 라이브러리입니다. LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내용(messages)을 계속 업데이트합니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, typing_extensions입니다."
research_artifacts: "ipynb/md · 코드 7개 · 실행 6개"
code_block_count: 7
execution_block_count: 6
research_focus:
  - "LangGraph"
  - "LangGraph는 LLM 애플리케이션에 \"순환(Loop)\"과 \"제어(Control)\" 기능을 부여하는..."
  - "LangGraph란 무엇인가요?"
research_stack:
  - "os"
  - "getpass"
  - "typing"
  - "typing_extensions"
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

LangGraph는 LLM 애플리케이션에 "순환(Loop)"과 "제어(Control)" 기능을 부여하는 라이브러리입니다. LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내용(messages)을 계속 업데이트합니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, typing_extensions입니다.

**빠르게 볼 수 있는 포인트**: LangGraph, LangGraph는 LLM 애플리케이션에 "순환(Loop)"과 "제어(..., LangGraph란 무엇인가요?.

**남겨둔 자료**: `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, typing_extensions입니다.

**주요 스택**: `os`, `getpass`, `typing`, `typing_extensions`, `langgraph`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 7 |
| Execution Cells | 6 |
| Libraries | `os`, `getpass`, `typing`, `typing_extensions`, `langgraph`, `langchain_openai`, `langchain_core` |
| Source Note | `3-5 LangGraph_맛보기` |

## What This Note Covers

### LangGraph란 무엇인가요?

LangGraph는 LLM 애플리케이션에 "순환(Loop)"과 "제어(Control)" 기능을 부여하는 라이브러리입니다.

### 상태(State)와 도구(Tool) 정의

LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내용(messages)을 계속 업데이트합니다.

### 노드(Node)와 그래프(Graph) 구성

이제 작업자(Node)를 배치하고 작업 순서(Edge)를 연결합니다.

### 실전 테스트

이제 만든 챗봇을 테스트해 봅니다.

## Implementation Flow

1. LangGraph란 무엇인가요?: LangGraph는 LLM 애플리케이션에 "순환(Loop)"과 "제어(Control)" 기능을 부여하는 라이브러리입니다.
2. 상태(State)와 도구(Tool) 정의: LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내용(messages)을 계속 업데이트합니다.
3. 노드(Node)와 그래프(Graph) 구성: 이제 작업자(Node)를 배치하고 작업 순서(Edge)를 연결합니다.
4. 실전 테스트: 이제 만든 챗봇을 테스트해 봅니다.

## Code Highlights

### 상태(State)와 도구(Tool) 정의

`상태(State)와 도구(Tool) 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 그래프의 상태(State) 정의, 메시지 리스트에 새로운 메시지를 계속 추가(append)하는 방식입니다., 사용할 도구(Tool) 정의 흐름이 주석과 함께 드러납니다.

```python
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

# 1. 그래프의 상태(State) 정의
# 메시지 리스트에 새로운 메시지를 계속 추가(append)하는 방식입니다.
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 2. 사용할 도구(Tool) 정의
# LLM은 수학 계산에 약하므로, 곱셈을 해주는 도구를 쥐어줍니다.
@tool
def multiply(a: int, b: int) -> int:
    """두 정수의 곱셈 결과를 반환합니다. 계산이 필요할 때 사용하세요."""
    return a * b

# 3. LLM과 도구 연결 (Bind)
# gpt-4o-mini 모델이 이 도구의 존재를 알게 됩니다.
llm = ChatOpenAI(model="gpt-4o-mini")
tools = [multiply]
llm_with_tools = llm.bind_tools(tools)

print("상태 정의 및 도구 연결 완료!")
```

### 노드(Node)와 그래프(Graph) 구성

`노드(Node)와 그래프(Graph) 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 챗봇 노드 함수 정의, 현재까지의 대화 기록(state["messages"])을 보고 다음 말을 생성합니다., 그래프 빌더 생성 흐름이 주석과 함께 드러납니다.

```python
from langgraph.prebuilt import ToolNode, tools_condition

# 1. 챗봇 노드 함수 정의
def chatbot(state: State):
    # 현재까지의 대화 기록(state["messages"])을 보고 다음 말을 생성합니다.
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

# 2. 그래프 빌더 생성
graph_builder = StateGraph(State)

# 3. 노드 추가 (작업자 배치)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools)) # LangGraph가 제공하는 도구 실행 전용 노드

# 4. 엣지 연결 (작업 순서 연결)
# [시작] -> [챗봇]
graph_builder.set_entry_point("chatbot")

# [챗봇] -> (조건부 분기) -> [도구] 또는 [종료]
# tools_condition: LLM이 도구를 찾으면 'tools'로, 아니면 '__end__'로 보냅니다.
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

# [도구] -> [챗봇] (★핵심: 도구 사용 후 다시 챗봇으로 돌아옵니다 = 순환)
graph_builder.add_edge("tools", "chatbot")

# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 LangGraph_맛보기.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 LangGraph_맛보기.ipynb`, `3-5 LangGraph_맛보기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> LangGraph는 LLM 애플리케이션에 **"순환(Loop)"**과 "제어(Control)" 기능을 부여하는 라이브러리입니다.
> - 기존 LangChain: A → B → C (일방통행, 되돌아가기 어려움)
