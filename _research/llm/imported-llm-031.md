---
title: "LangGraph 1 조건분기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-1 LangGraph_1_조건분기"
source_path: "13_LLM_GenAI/Code_Snippets/4-1 LangGraph_1_조건분기.md"
excerpt: "LangGraph의 핵심 3요소(State, Node, Edge)를 이해한다 - 조건부 엣지(Conditional Edge)로 분기 로직을 구현한다 - 그래프를 시각화하고 실행 흐름을 추적한다"
research_summary: "LangGraph의 핵심 3요소(State, Node, Edge)를 이해한다 - 조건부 엣지(Conditional Edge)로 분기 로직을 구현한다 - 그래프를 시각화하고 실행 흐름을 추적한다. / 요소 / 비유 / 역할 / /------/------/------/ / State / 공유 문서 (Google Docs) / 모든 노드가 읽고 쓰는 기억 저장소 / / Node / 일꾼 / 실제 작업 수행 (LLM 호출, 도구 사용 등) / / Edge / 길 / 노드 간 이동 경로 (일반 / 조건부) /. `ipynb/md` 원본과 12개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다."
research_artifacts: "ipynb/md · 코드 12개 · 실행 7개"
code_block_count: 12
execution_block_count: 7
research_focus:
  - "LangGraph의 핵심 3요소(State, Node, Edge)를 이해한다 - 조건부 엣지(Condi..."
  - "LangGraph 실습 1"
  - "환경 설정"
research_stack:
  - "os"
  - "getpass"
  - "typing"
  - "langchain_openai"
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

LangGraph의 핵심 3요소(State, Node, Edge)를 이해한다 - 조건부 엣지(Conditional Edge)로 분기 로직을 구현한다 - 그래프를 시각화하고 실행 흐름을 추적한다. / 요소 / 비유 / 역할 / /------/------/------/ / State / 공유 문서 (Google Docs) / 모든 노드가 읽고 쓰는 기억 저장소 / / Node / 일꾼 / 실제 작업 수행 (LLM 호출, 도구 사용 등) / / Edge / 길 / 노드 간 이동 경로 (일반 / 조건부) /. `ipynb/md` 원본과 12개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다.

**빠르게 볼 수 있는 포인트**: LangGraph의 핵심 3요소(State, Node, Edge)를 이..., LangGraph 실습 1, 환경 설정.

**남겨둔 자료**: `ipynb/md` 원본과 12개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다.

**주요 스택**: `os`, `getpass`, `typing`, `langchain_openai`, `langgraph`

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

## What This Note Covers

### LangGraph 실습 1: 조건 분기 (Conditional Branching)

LangGraph의 핵심 3요소(State, Node, Edge)를 이해한다 - 조건부 엣지(Conditional Edge)로 분기 로직을 구현한다 - 그래프를 시각화하고 실행 흐름을 추적한다

### LangGraph 3대 요소

/ 요소 / 비유 / 역할 / /------/------/------/ / State / 공유 문서 (Google Docs) / 모든 노드가 읽고 쓰는 기억 저장소 / / Node / 일꾼 / 실제 작업 수행 (LLM 호출, 도구 사용 등) / / Edge / 길 / 노드 간 이동 경로 (일반 / 조건부) /

### 문제 1: 분기 추가하기

현재는 good/bad 두 가지 분기만 있습니다. "애매한 날씨"(예: 흐림) 일 때 "read_book" 노드로 가도록 수정해보세요.

### 문제 2: State 확장하기

State에 "temperature" (기온) 필드를 추가하고, 기온이 30도 이상이면 날씨가 좋아도 "code_at_home"으로 가도록 수정해보세요.

## Implementation Flow

1. LangGraph 실습 1: 조건 분기 (Conditional Branching): LangGraph의 핵심 3요소(State, Node, Edge)를 이해한다 - 조건부 엣지(Conditional Edge)로 분기 로직을 구현한다 - 그래프를 시각화하고 실행 흐름을 추적한다
2. LangGraph 3대 요소: / 요소 / 비유 / 역할 / /------/------/------/ / State / 공유 문서 (Google Docs) / 모든 노드가 읽고 쓰는 기억 저장소 / / Node / 일꾼 / 실제 작업 수행 (LLM 호출, 도구 사용 등) / / Edge / 길 /...
3. 문제 1: 분기 추가하기: 현재는 good/bad 두 가지 분기만 있습니다. "애매한 날씨"(예: 흐림) 일 때 "read_book" 노드로 가도록 수정해보세요.
4. 문제 2: State 확장하기: State에 "temperature" (기온) 필드를 추가하고, 기온이 30도 이상이면 날씨가 좋아도 "code_at_home"으로 가도록 수정해보세요.

## Code Highlights

### 코드 구현

`코드 구현`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ============================================, [2] Node 정의: 실제 작업을 수행하는 함수들 흐름이 주석과 함께 드러납니다.

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

### 실행 테스트

`실행 테스트`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 테스트 1: 좋은 날씨 흐름이 주석과 함께 드러납니다.

```python
# 테스트 1: 좋은 날씨
print("=" * 50)
print("테스트 1: 화창한 날씨")
print("=" * 50)

result1 = app.invoke({
    "weather": "맑고 화창함, 기온 22도",
    "decision": "",
    "activity": ""
})

print(f"\n최종 결과: {result1['activity']}")
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
