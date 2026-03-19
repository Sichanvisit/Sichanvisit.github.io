---
title: "LangGraph 2 Self Corrective"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-2 LangGraph_2_Self_Corrective"
source_path: "13_LLM_GenAI/Code_Snippets/4-2 LangGraph_2_Self_Corrective.md"
excerpt: "Self-Corrective 검색 (루프): Corrective-RAG (CRAG) 단순화버전"
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
| Code Blocks | 19 |
| Execution Cells | 6 |
| Libraries | `os`, `getpass`, `typing`, `langchain_openai`, `langgraph`, `IPython` |
| Source Note | `4-2 LangGraph_2_Self_Corrective` |

## What I Worked On

- LangGraph 실습 2: Self-Corrective 검색 (루프)
- 핵심: 왜 루프가 필요한가?
- 0. 환경 설정
- 패키지 설치
- API 키 설정

## Implementation Flow

1. LangGraph 실습 2: Self-Corrective 검색 (루프)
2. 핵심: 왜 루프가 필요한가?
3. 0. 환경 설정
4. 패키지 설치
5. API 키 설정
6. 1. 시나리오: Self-Corrective RAG 시뮬레이션

## Code Highlights

### 2. 코드 구현

```python
# ============================================
# [3] Router 정의: 루프 여부 결정
# ============================================

def should_continue(state: SearchState) -> Literal["rewrite_query", "generate"]:
    """
    평가 결과에 따라 루프 여부 결정
    - 관련 있음 OR 최대 시도 횟수 도달 → generate로 이동
    - 관련 없음 AND 시도 가능 → rewrite_query로 이동 (루프!)
    """
    MAX_ATTEMPTS = 5

    print(f"\n[Router] 판단 중...")
    print(f"   is_relevant={state['is_relevant']}, attempts={state['attempts']}")

    if state["is_relevant"]:
        print("   → generate로 이동 (평가 통과)")
        return "generate"

    if state["attempts"] >= MAX_ATTEMPTS:
        print(f"   → generate로 이동 (최대 시도 {MAX_ATTEMPTS}회 도달)")
        return "generate"

    print("   → rewrite_query로 이동 (재시도)")
    return "rewrite_query"  # 👈 루프!
```

### 2. 코드 구현

```python
# ============================================
# [4] 그래프 조립
# ============================================

workflow = StateGraph(SearchState)

# 노드 등록
workflow.add_node("search", search)
workflow.add_node("evaluate", evaluate)
workflow.add_node("rewrite_query", rewrite_query)
workflow.add_node("generate", generate)

# 엣지 연결
workflow.add_edge(START, "search")
workflow.add_edge("search", "evaluate")

# !!! 핵심: 조건부 엣지로 루프 구현 !!!
workflow.add_conditional_edges(
    source="evaluate",
    path=should_continue,
    path_map={
        "rewrite_query": "rewrite_query",   # 루프 경로
        "generate": "generate"              # 탈출 경로
    }
)

# rewrite_query → search 로 되돌아감 (루프 완성!)
workflow.add_edge("rewrite_query", "search")
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/4-2 LangGraph_2_Self_Corrective.md`
- Source formats: `ipynb`, `md`
- Companion files: `4-2 LangGraph_2_Self_Corrective.ipynb`, `4-2 LangGraph_2_Self_Corrective.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> Self-Corrective 검색 (루프): Corrective-RAG (CRAG) 단순화버전
> - LangGraph의 핵심 기능인 **루프(Loop)**를 구현한다 - "결과가 안 좋으면 다시 시도"하는 Self-Corrective 패턴을 이해한다 - 무한 루프 방지를 위한 종료 조건 설계를 학습한다
