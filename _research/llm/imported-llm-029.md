---
title: "LangGraph 맛보기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 LangGraph_맛보기"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 LangGraph_맛보기.md"
excerpt: "LangGraph는 LLM 애플리케이션에 **\"순환(Loop)\"**과 \"제어(Control)\" 기능을 부여하는 라이브러리입니다."
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
| Code Blocks | 7 |
| Execution Cells | 6 |
| Libraries | `os`, `getpass`, `typing`, `typing_extensions`, `langgraph`, `langchain_openai`, `langchain_core` |
| Source Note | `3-5 LangGraph_맛보기` |

## What I Worked On

- LangGraph
- LangGraph란 무엇인가요?
- 1. 라이브러리 설치
- 2. OpenAI API Key 설정
- 상태(State)와 도구(Tool) 정의

## Implementation Flow

1. LangGraph
2. LangGraph란 무엇인가요?
3. 1. 라이브러리 설치
4. 2. OpenAI API Key 설정
5. 상태(State)와 도구(Tool) 정의
6. 1. 그래프의 상태(State) 정의

## Code Highlights

### 상태(State)와 도구(Tool) 정의

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
