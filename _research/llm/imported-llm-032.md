---
title: "LangGraph 2 Self Corrective"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-2 LangGraph_2_Self_Corrective"
source_path: "13_LLM_GenAI/Code_Snippets/4-2 LangGraph_2_Self_Corrective.md"
excerpt: "Self-Corrective 검색 (루프): Corrective-RAG (CRAG) 단순화버전"
research_summary: "Self-Corrective 검색 (루프): Corrective-RAG (CRAG) 단순화버전. LangChain (Chain): 직선 흐름만 가능. `ipynb/md` 원본과 19개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 6개"
code_block_count: 19
execution_block_count: 6
research_focus:
  - "Self-Corrective 검색 (루프)"
  - "LangGraph 실습 2"
  - "LangChain (Chain)"
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

Self-Corrective 검색 (루프): Corrective-RAG (CRAG) 단순화버전. LangChain (Chain): 직선 흐름만 가능. `ipynb/md` 원본과 19개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다.

**빠르게 볼 수 있는 포인트**: Self-Corrective 검색 (루프), LangGraph 실습 2, LangChain (Chain).

**남겨둔 자료**: `ipynb/md` 원본과 19개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다.

**주요 스택**: `os`, `getpass`, `typing`, `langchain_openai`, `langgraph`

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

## What This Note Covers

### LangGraph 실습 2: Self-Corrective 검색 (루프)

Self-Corrective 검색 (루프): Corrective-RAG (CRAG) 단순화버전

### 핵심: 왜 루프가 필요한가?

LangChain (Chain): 직선 흐름만 가능

### 시나리오: Self-Corrective RAG 시뮬레이션

search: 검색 수행 (시뮬레이션: 3번째에 좋은 결과) - evaluate: 결과 품질 평가 - 평가 통과 시 → generate로 이동 - 평가 실패 시 → search로 되돌아감 (루프!)

### 문제 1: 다중 평가 기준

현재는 "관련성"만 평가합니다. "정확성" 평가도 추가해서, 관련성과 정확성 모두 통과해야 generate로 가도록 수정해보기

## Why This Matters

### RAG 검색 파이프라인

- 왜 필요한가: LLM이 외부 지식을 안정적으로 참조하게 하려면, 생성 전에 관련 문서를 정확히 찾아오는 검색 단계가 먼저 필요합니다.
- 왜 이 방식을 쓰는가: 이 방식은 모델 파라미터만 믿지 않고 최신 문서나 도메인 지식을 붙일 수 있어서 실제 서비스형 QA에 적합합니다.
- 원리: 문서를 청크로 나누고 임베딩한 뒤, 질문과 가까운 벡터를 검색해 프롬프트에 함께 넣는 구조로 동작합니다.

### 에이전트 상태 흐름

- 왜 필요한가: 단일 호출만으로 해결되지 않는 작업은 추론, 도구 호출, 중간 상태 관리가 이어지는 흐름 제어가 필요합니다.
- 왜 이 방식을 쓰는가: 상태 그래프 기반 접근은 단계별 분기와 재시도를 명시적으로 관리할 수 있어 에이전트 실험을 설명하기 좋습니다.
- 원리: 현재 상태를 노드 간에 전달하면서, 조건에 따라 다음 노드나 도구 호출을 결정하는 방식으로 실행 흐름이 이어집니다.

### 프롬프트 체인 구성

- 왜 필요한가: LLM 호출을 재현 가능하게 만들려면 입력 조합, 프롬프트 템플릿, 후처리 순서를 구조화할 필요가 있습니다.
- 왜 이 방식을 쓰는가: 체인 구조는 실험 중 프롬프트와 입력 변형을 비교하기 쉽고, 이후 RAG나 에이전트 단계로 확장하기도 좋습니다.
- 원리: 질문과 컨텍스트를 정해진 템플릿에 넣고, 모델 호출 결과를 다음 단계 입력으로 넘기며 처리 흐름을 구성합니다.

## Implementation Flow

1. LangGraph 실습 2: Self-Corrective 검색 (루프): Self-Corrective 검색 (루프): Corrective-RAG (CRAG) 단순화버전
2. 핵심: 왜 루프가 필요한가?: LangChain (Chain): 직선 흐름만 가능
3. 시나리오: Self-Corrective RAG 시뮬레이션: search: 검색 수행 (시뮬레이션: 3번째에 좋은 결과) - evaluate: 결과 품질 평가 - 평가 통과 시 → generate로 이동 - 평가 실패 시 → search로 되돌아감 (루프!)
4. 문제 1: 다중 평가 기준: 현재는 "관련성"만 평가합니다. "정확성" 평가도 추가해서, 관련성과 정확성 모두 통과해야 generate로 가도록 수정해보기

## Code Highlights

### 코드 구현

`코드 구현`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ============================================, [4] 그래프 조립 흐름이 주석과 함께 드러납니다.

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

### 실행 테스트

`실행 테스트`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 실행! 흐름이 주석과 함께 드러납니다.

```python
# 실행!
print("=" * 60)
print("Self-Corrective RAG 실행")
print("=" * 60)

result = app.invoke({
    "query": "LangGraph란 무엇인가요?",
    "current_query": "LangGraph란 무엇인가요?",
    "search_result": "",
    "is_relevant": False,
    "attempts": 0,
    "final_answer": ""
})

print("\n" + "=" * 60)
print("----최종 결과")
print("=" * 60)
print(f"총 검색 시도: {result['attempts']}회")
print(f"\n최종 답변:\n{result['final_answer']}")
```

### 스트리밍으로 루프 과정 추적

`스트리밍으로 루프 과정 추적`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 각 스텝별 State 변화 추적 흐름이 주석과 함께 드러납니다.

```python
# 각 스텝별 State 변화 추적
print("=" * 60)
print("스트리밍 모드: 각 노드 실행 추적")
print("=" * 60)

step_count = 0
for step in app.stream({
    "query": "LangGraph의 핵심 구성요소는?",
    "current_query": "LangGraph의 핵심 구성요소는?",
    "search_result": "",
    "is_relevant": False,
    "attempts": 0,
    "final_answer": ""
}):
    step_count += 1
    for node_name, node_output in step.items():
        print(f"\n{'─' * 40}")
        print(f"Step {step_count}: 노드 '{node_name}' 완료")
        if "attempts" in node_output:
            print(f"  attempts: {node_output['attempts']}")
        if "is_relevant" in node_output:
            print(f"  is_relevant: {node_output['is_relevant']}")
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
