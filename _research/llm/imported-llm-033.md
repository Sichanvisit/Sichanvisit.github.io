---
title: "LangGraph 3 ReAct에이전트"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-3 LangGraph_3_ReAct에이전트"
source_path: "13_LLM_GenAI/Code_Snippets/4-3 LangGraph_3_ReAct에이전트.md"
excerpt: "LangGraph 3 ReAct에이전트에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 3: Too... 순서로 핵심 장면을 먼저 훑고, 도구(Tool) 정의, 방법 1: create_react_ag..., 방법 2: Stat..."
research_summary: "LangGraph 3 ReAct에이전트에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 3: Too... 순서로 핵심 장면을 먼저 훑고, 도구(Tool) 정의, 방법 1: create_react_ag..., 방법 2: StateGraph로 직접... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 17개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_core, typing입니다."
research_artifacts: "ipynb/md · 코드 17개 · 실행 11개"
code_block_count: 17
execution_block_count: 11
research_focus:
  - "LangGraph 실습 3: Tool 에이전트 (ReAct 패턴)"
research_stack:
  - "os"
  - "getpass"
  - "langchain_core"
  - "typing"
  - "random"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

LangGraph 3 ReAct에이전트에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 3: Too... 순서로 핵심 장면을 먼저 훑고, 도구(Tool) 정의, 방법 1: create_react_ag..., 방법 2: StateGraph로 직접... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 17개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_core, typing입니다.

**빠르게 볼 수 있는 포인트**: LangGraph 실습 3: Tool 에이전트 (ReAct 패턴).

**남겨둔 자료**: `ipynb/md` 원본과 17개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, langchain_core, typing입니다.

**주요 스택**: `os`, `getpass`, `langchain_core`, `typing`, `random`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 17 |
| Execution Cells | 11 |
| Libraries | `os`, `getpass`, `langchain_core`, `typing`, `random`, `langchain_openai`, `langgraph`, `IPython` |
| Source Note | `4-3 LangGraph_3_ReAct에이전트` |

## What This Note Covers

### LangGraph 실습 3: Tool 에이전트 (ReAct 패턴)

LLM이 스스로 도구를 선택하는 ReAct 패턴을 이해한다 - create_react_agent로 빠르게 에이전트를 만든다 - 내부 동작을 StateGraph로 직접 구현해본다

- 읽을 포인트: 세부 흐름: 도구(Tool) 정의, 방법 1: create_react_agent (간편 버전), 방법 2: StateGraph로 직접 구현 (상세 버전)

#### 도구(Tool) 정의

LLM이 사용할 수 있는 도구들을 정의합니다. @tool 데코레이터를 사용하면 함수가 LLM이 호출 가능한 도구로 변환됩니다.

#### 방법 1: create_react_agent (간편 버전)

LangGraph가 제공하는 create_react_agent를 사용하면 단 몇 줄로 ReAct 에이전트를 만들 수 있습니다.

#### 방법 2: StateGraph로 직접 구현 (상세 버전)

create_react_agent의 내부 동작을 이해하기 위해 StateGraph로 직접 ReAct 패턴을 구현해봅니다. !-- #region id="ehPFqxtf1nfF"

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

1. LangGraph 실습 3: Tool 에이전트 (ReAct 패턴): 도구(Tool) 정의, 방법 1: create_react_agent (간편 버전)

## Code Highlights

### 도구(Tool) 정의

`도구(Tool) 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 시뮬레이션용 가짜 데이터, 안전한 eval (숫자와 연산자만 허용) 흐름이 주석과 함께 드러납니다.

```python
from langchain_core.tools import tool
from typing import Annotated
import random


@tool
def get_weather(city: Annotated[str, "도시 이름 (예: 서울, 부산)"]) -> str:
    """특정 도시의 현재 날씨를 조회합니다."""
    # 시뮬레이션용 가짜 데이터
    weather_data = {
        "서울": {"temp": 22, "condition": "맑음", "humidity": 45},
        "부산": {"temp": 25, "condition": "흐림", "humidity": 65},
        "제주": {"temp": 27, "condition": "비", "humidity": 80},
    }

    if city in weather_data:
        data = weather_data[city]
        return f"{city} 날씨: {data['temp']}°C, {data['condition']}, 습도 {data['humidity']}%"
    else:
        return f"{city}의 날씨 정보를 찾을 수 없습니다."


@tool
def calculator(
    expression: Annotated[str, "계산할 수식 (예: 23 * 17)"]
) -> str:
    """수학 계산을 수행합니다. 사칙연산과 거듭제곱을 지원합니다."""
    try:
# ... trimmed ...
```

### 방법 1: create_react_agent (간편 버전)

`방법 1: create_react_agent (간편 버전)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 LLM 설정, ReAct 에이전트 생성 (단 1줄!) 흐름이 주석과 함께 드러납니다.

```python
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# LLM 설정
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ReAct 에이전트 생성 (단 1줄!)
react_agent = create_react_agent(llm, tools)

print("ReAct 에이전트 생성 완료!")
```

### 방법 2: StateGraph로 직접 구현 (상세 버전)

`방법 2: StateGraph로 직접 구현 (상세 버전)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ============================================, [4] 그래프 조립 흐름이 주석과 함께 드러납니다.

```python
# ============================================
# [4] 그래프 조립
# ============================================

workflow = StateGraph(AgentState)

# 노드 등록
workflow.add_node("call_llm", call_llm)
workflow.add_node("call_tools", call_tools)

# 엣지 연결
workflow.add_edge(START, "call_llm")

# 조건부 엣지: LLM 응답에 따라 분기
workflow.add_conditional_edges(
    source="call_llm",
    path=should_continue,
    path_map={
        "call_tools": "call_tools",
        "__end__": END
    }
)

# 도구 실행 후 → 다시 LLM (루프!)
workflow.add_edge("call_tools", "call_llm")

# 컴파일
custom_agent = workflow.compile()
# ... trimmed ...
```

### ReAct 패턴 흐름

`ReAct 패턴 흐름`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```text
       ┌──────────────────────────┐
       │                          │
       ▼                          │ (도구 결과 전달)
  [call_llm] ──(tool_calls)──> [call_tools]
       │
       │ (no tool_calls)
       ▼
      END
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/4-3 LangGraph_3_ReAct에이전트.md`
- Source formats: `ipynb`, `md`
- Companion files: `4-3 LangGraph_3_ReAct에이전트.ipynb`, `4-3 LangGraph_3_ReAct에이전트.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - LLM이 **스스로 도구를 선택**하는 ReAct 패턴을 이해한다 - create_react_agent로 빠르게 에이전트를 만든다 - 내부 동작을 StateGraph로 직접 구현해본다
> **ReAct = Reasoning + Acting**
