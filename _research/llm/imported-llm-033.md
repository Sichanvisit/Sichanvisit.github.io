---
title: "LangGraph 3 ReAct에이전트"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-3 LangGraph_3_ReAct에이전트"
source_path: "13_LLM_GenAI/Code_Snippets/4-3 LangGraph_3_ReAct에이전트.md"
excerpt: "- LLM이 **스스로 도구를 선택**하는 ReAct 패턴을 이해한다 - create_react_agent로 빠르게 에이전트를 만든다 - 내부 동작을 StateGraph로 직접 구현해본다"
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
| Code Blocks | 17 |
| Execution Cells | 11 |
| Libraries | `os`, `getpass`, `langchain_core`, `typing`, `random`, `langchain_openai`, `langgraph`, `IPython` |
| Source Note | `4-3 LangGraph_3_ReAct에이전트` |

## What I Worked On

- LangGraph 실습 3: Tool 에이전트 (ReAct 패턴)
- 핵심 개념: ReAct 패턴
- 0. 환경 설정
- 패키지 설치
- API 키 설정

## Implementation Flow

1. LangGraph 실습 3: Tool 에이전트 (ReAct 패턴)
2. 핵심 개념: ReAct 패턴
3. 0. 환경 설정
4. 패키지 설치
5. API 키 설정
6. 1. 도구(Tool) 정의

## Code Highlights

### 1. 도구(Tool) 정의

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

### 3. 방법 2: StateGraph로 직접 구현 (상세 버전)

```python
# ============================================
# [2] Node 정의
# ============================================

def call_llm(state: AgentState) -> dict:
    """LLM을 호출하여 다음 행동 결정"""
    print("\n  [call_llm] LLM 호출 중...")

    messages = state["messages"]
    response = llm_with_tools.invoke(messages)

    if response.tool_calls:
        print(f"   → 도구 호출 결정: {[tc['name'] for tc in response.tool_calls]}")
    else:
        print("   → 최종 답변 생성")

    return {"messages": [response]}


def call_tools(state: AgentState) -> dict:
    """도구 실행"""
    print("\n  [call_tools] 도구 실행 중...")

    # 마지막 AI 메시지에서 tool_calls 추출
    last_message = state["messages"][-1]
    tool_calls = last_message.tool_calls

    # 도구 이름 → 도구 함수 매핑
# ... trimmed ...
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
> ---
