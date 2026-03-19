---
title: "LangGraph 1 조건분기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-1 LangGraph_1_조건분기"
source_path: "13_LLM_GenAI/Code_Snippets/4-1 LangGraph_1_조건분기.md"
excerpt: "- LangGraph의 핵심 3요소(State, Node, Edge)를 이해한다 - 조건부 엣지(Conditional Edge)로 분기 로직을 구현한다 - 그래프를 시각화하고 실행 흐름을 추적한다"
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
| Code Blocks | 12 |
| Execution Cells | 7 |
| Libraries | `os`, `getpass`, `typing`, `langchain_openai`, `langgraph`, `IPython` |
| Source Note | `4-1 LangGraph_1_조건분기` |

## What I Worked On

- LangGraph 실습 1: 조건 분기 (Conditional Branching)
- 0. 환경 설정
- 패키지 설치
- API 키 설정
- 1. 핵심 개념 복습

## Implementation Flow

1. LangGraph 실습 1: 조건 분기 (Conditional Branching)
2. 0. 환경 설정
3. 패키지 설치
4. API 키 설정
5. 1. 핵심 개념 복습
6. LangGraph 3대 요소

## Code Highlights

### 3. 코드 구현

```python
# ============================================
# [2] Node 정의: 실제 작업을 수행하는 함수들
# ============================================

def check_weather(state: WeatherState) -> dict:
    """날씨를 보고 좋음/나쁨을 판단하는 노드"""
    print("[check_weather] 날씨 확인 중...")

    weather = state["weather"]

    # LLM에게 판단 요청
    response = llm.invoke(
        f"날씨가 '{weather}'입니다. "
        "야외 활동하기 좋으면 'good', 안 좋으면 'bad'라고만 답해주세요."
    )

    decision = response.content.strip().lower()
    print(f"   → LLM 판단: {decision}")

    # State 업데이트 (변경된 부분만 반환)
    return {"decision": decision}


def go_for_walk(state: WeatherState) -> dict:
    """산책 추천 노드"""
    print("[go_for_walk] 산책을 추천합니다!")
    return {"activity": "산책하기~~"}

# ... trimmed ...
```

### 3. 코드 구현

```python
# ============================================
# [4] 그래프 조립
# ============================================

# 그래프 생성 (State 타입 지정)
workflow = StateGraph(WeatherState)

# 노드 등록
workflow.add_node("check_weather", check_weather)
workflow.add_node("go_for_walk", go_for_walk)
workflow.add_node("code_at_home", code_at_home)

# 엣지 연결
workflow.add_edge(START, "check_weather")  # 시작 → check_weather

# 조건부 엣지: check_weather 이후 router 함수로 분기
workflow.add_conditional_edges(
    source="check_weather",      # 출발 노드
    path=weather_router,          # 분기 결정 함수
    path_map={                    # 반환값 → 도착 노드 매핑
        "go_for_walk": "go_for_walk",
        "code_at_home": "code_at_home",
    }
)

# 종료 엣지
workflow.add_edge("go_for_walk", END)
workflow.add_edge("code_at_home", END)
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/4-1 LangGraph_1_조건분기.md`
- Source formats: `ipynb`, `md`
- Companion files: `4-1 LangGraph_1_조건분기.ipynb`, `4-1 LangGraph_1_조건분기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - LangGraph의 핵심 3요소(State, Node, Edge)를 이해한다 - 조건부 엣지(Conditional Edge)로 분기 로직을 구현한다 - 그래프를 시각화하고 실행 흐름을 추적한다
> ---
