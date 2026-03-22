---
title: "LangGraph 1 조건분기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-1 LangGraph_1_조건분기"
source_path: "13_LLM_GenAI/Code_Snippets/4-1 LangGraph_1_조건분기.md"
excerpt: "LangGraph 1 조건분기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 1: 조건... 순서로 핵심 장면을 먼저 훑고, 환경 설정, 코드 구현, 실행 테스트 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipy..."
research_summary: "LangGraph 1 조건분기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 1: 조건... 순서로 핵심 장면을 먼저 훑고, 환경 설정, 코드 구현, 실행 테스트 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 12개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다."
research_artifacts: "ipynb/md · 코드 12개 · 실행 7개"
code_block_count: 12
execution_block_count: 7
research_focus:
  - "LangGraph 실습 1: 조건 분기 (Conditional Branching)"
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

LangGraph 1 조건분기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 1: 조건... 순서로 핵심 장면을 먼저 훑고, 환경 설정, 코드 구현, 실행 테스트 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 12개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다.

**빠르게 볼 수 있는 포인트**: LangGraph 실습 1: 조건 분기 (Conditional Bran....

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

- 읽을 포인트: 세부 흐름: 환경 설정, 코드 구현, 실행 테스트

#### 환경 설정

LangGraph 실습 1: 조건 분기 (Conditional Branching) > 환경 설정 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

#### 코드 구현

LangGraph 실습 1: 조건 분기 (Conditional Branching) > 코드 구현 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

#### 실행 테스트

LangGraph 실습 1: 조건 분기 (Conditional Branching) > 실행 테스트 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

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

1. LangGraph 실습 1: 조건 분기 (Conditional Branching): 환경 설정, 코드 구현

## Code Highlights

### 환경 설정

`환경 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 패키지 설치 흐름이 주석과 함께 드러납니다.

```python
# 패키지 설치
!pip install -q langchain-openai langgraph
```

### 코드 구현

`코드 구현`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ============================================, [4] 그래프 조립 흐름이 주석과 함께 드러납니다.

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

### 스트리밍으로 실행 과정 추적

`스트리밍으로 실행 과정 추적`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 stream()으로 각 노드 실행 후 상태 변화 확인 흐름이 주석과 함께 드러납니다.

```python
# stream()으로 각 노드 실행 후 상태 변화 확인
print("=" * 50)
print("스트리밍 실행: 각 단계별 State 변화 추적")
print("=" * 50)

for step in app.stream({"weather": "소나기가 내림", "decision": "", "activity": ""}):
    print(f"\n----현재 State:")
    for key, value in step.items():
        print(f"   노드 '{key}' 실행 완료 → {value}")
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
> 현재는 good/bad 두 가지 분기만 있습니다. **"애매한 날씨"(예: 흐림)** 일 때 "read_book" 노드로 가도록 수정해보세요.
