---
title: "LangGraph 맛보기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 LangGraph_맛보기"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 LangGraph_맛보기.md"
excerpt: "LangGraph는 LLM 애플리케이션에 \"순환(Loop)\"과 \"제어(Control)\" 기능을 부여하는 라이브러리입니다. 기존 LangChain: A → B → C (일방통행, 되돌아가기 어려움). LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내..."
research_summary: "LangGraph는 LLM 애플리케이션에 \"순환(Loop)\"과 \"제어(Control)\" 기능을 부여하는 라이브러리입니다. 기존 LangChain: A → B → C (일방통행, 되돌아가기 어려움). LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내용(messages)을 계속 업데이트합니다. add_messages: 새로운 대화가 오면 기존 리스트를 덮어쓰지 않고 추가(append)하라는 설정입니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, typing_extensions입니다."
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

LangGraph는 LLM 애플리케이션에 "순환(Loop)"과 "제어(Control)" 기능을 부여하는 라이브러리입니다. 기존 LangChain: A → B → C (일방통행, 되돌아가기 어려움). LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내용(messages)을 계속 업데이트합니다. add_messages: 새로운 대화가 오면 기존 리스트를 덮어쓰지 않고 추가(append)하라는 설정입니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, typing_extensions입니다.

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

### LangGraph > LangGraph란 무엇인가요?

LangGraph는 LLM 애플리케이션에 "순환(Loop)"과 "제어(Control)" 기능을 부여하는 라이브러리입니다. 기존 LangChain: A → B → C (일방통행, 되돌아가기 어려움)

### LangGraph > 상태(State)와 도구(Tool) 정의

LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내용(messages)을 계속 업데이트합니다. add_messages: 새로운 대화가 오면 기존 리스트를 덮어쓰지 않고 추가(append)하라는 설정입니다.

### LangGraph > 노드(Node)와 그래프(Graph) 구성

이제 작업자(Node)를 배치하고 작업 순서(Edge)를 연결합니다. Chatbot Node: LLM이 생각하고 답변하는 곳 - Tools Node: LLM이 도구 사용을 요청하면 실제로 실행하는 곳 - Conditional Edge (분기): LLM의 응답을 보고 "도구 쓸래?" 아니면 "답변 하고 끝낼래?"를 결정 - Loop (순환): 도구를 썼으면 반드시 다시 챗봇에게 돌아가서...

### LangGraph > 실전 테스트

이제 만든 챗봇을 테스트해 봅니다. Case 1: 도구가 필요 없는 일상 대화 - Case 2: 도구가 필요한 계산 요청 (순환 발생)

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

1. LangGraph > LangGraph란 무엇인가요?: LangGraph는 LLM 애플리케이션에 "순환(Loop)"과 "제어(Control)" 기능을 부여하는 라이브러리입니다. 기존 LangChain: A → B → C (일방통행, 되돌아가기 어려움)
2. LangGraph > 상태(State)와 도구(Tool) 정의: LangGraph의 핵심은 State(상태)입니다. 이 상태 객체가 노드들 사이를 흘러다니며 대화 내용(messages)을 계속 업데이트합니다. add_messages: 새로운 대화가 오면 기존 리스트를 덮어쓰지 않고 추가(append...
3. LangGraph > 노드(Node)와 그래프(Graph) 구성: 이제 작업자(Node)를 배치하고 작업 순서(Edge)를 연결합니다. Chatbot Node: LLM이 생각하고 답변하는 곳 - Tools Node: LLM이 도구 사용을 요청하면 실제로 실행하는 곳 - Conditional Edge...
4. LangGraph > 실전 테스트: 이제 만든 챗봇을 테스트해 봅니다. Case 1: 도구가 필요 없는 일상 대화 - Case 2: 도구가 필요한 계산 요청 (순환 발생)

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

### 실전 테스트

`실전 테스트`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 graph.stream()을 통해 각 단계(Node)가 실행될 때마다 결과를 봅니다., 챗봇이 응답한 경우, 도구가 실행된 경우 흐름이 주석과 함께 드러납니다.

```python
from langchain_core.messages import HumanMessage

def run_chat(question):
    print(f"\n 질문: {question}")
    print("-" * 40)

    # graph.stream()을 통해 각 단계(Node)가 실행될 때마다 결과를 봅니다.
    for event in graph.stream({"messages": [HumanMessage(content=question)]}):
        for key, value in event.items():
            print(f" [현재 위치: {key}]")

            # 챗봇이 응답한 경우
            if key == "chatbot":
                msg = value['messages'][-1]
                if msg.tool_calls:
                    print(f"   도구 호출 감지! (이름: {msg.tool_calls[0]['name']}, 값: {msg.tool_calls[0]['args']})")
                else:
                    print(f"   최종 답변: {msg.content}")

            # 도구가 실행된 경우
            elif key == "tools":
                msg = value['messages'][-1]
                print(f"   도구 실행 결과: {msg.content}")
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
