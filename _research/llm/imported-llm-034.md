---
title: "LangGraph 4 사람승인"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-4 LangGraph_4_사람승인"
source_path: "13_LLM_GenAI/Code_Snippets/4-4 LangGraph_4_사람승인.md"
excerpt: "LangGraph 4 사람승인에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 4: Hum... 순서로 핵심 장면을 먼저 훑고, 환경 설정, 코드 구현, Human-in-the-Loop 구현 3단계 같은 코드로 실제 구현을 이..."
research_summary: "LangGraph 4 사람승인에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 4: Hum... 순서로 핵심 장면을 먼저 훑고, 환경 설정, 코드 구현, Human-in-the-Loop 구현 3단계 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 19개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 12개"
code_block_count: 19
execution_block_count: 12
research_focus:
  - "LangGraph 실습 4: Human-in-the-Loop (HITL)"
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

LangGraph 4 사람승인에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 LangGraph 실습 4: Hum... 순서로 핵심 장면을 먼저 훑고, 환경 설정, 코드 구현, Human-in-the-Loop 구현 3단계 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 19개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다.

**빠르게 볼 수 있는 포인트**: LangGraph 실습 4: Human-in-the-Loop (HITL).

**남겨둔 자료**: `ipynb/md` 원본과 19개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다.

**주요 스택**: `os`, `getpass`, `typing`, `langchain_openai`, `langgraph`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 19 |
| Execution Cells | 12 |
| Libraries | `os`, `getpass`, `typing`, `langchain_openai`, `langgraph`, `IPython` |
| Source Note | `4-4 LangGraph_4_사람승인` |

## What This Note Covers

### LangGraph 실습 4: Human-in-the-Loop (HITL)

Checkpoint를 사용해 그래프 상태를 저장/복원한다 - interrupt_before로 특정 노드 전에 실행을 멈춘다 - 사용자 승인 후 이어서 실행하는 패턴을 구현한다

- 읽을 포인트: 세부 흐름: 코드 구현, 상태 수정 후 재실행, 핵심 > Human-in-the-Loop 구현 3단계

#### 코드 구현

LangGraph 실습 4: Human-in-the-Loop (HITL) > 코드 구현 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

#### 상태 수정 후 재실행

LangGraph 실습 4: Human-in-the-Loop (HITL) > 상태 수정 후 재실행 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

#### 핵심 > Human-in-the-Loop 구현 3단계

핵심 > Human-in-the-Loop 구현 3단계 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

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

1. LangGraph 실습 4: Human-in-the-Loop (HITL): 코드 구현, 상태 수정 후 재실행

## Code Highlights

### 환경 설정

`환경 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 패키지 설치 흐름이 주석과 함께 드러납니다.

```python
# 패키지 설치
!pip install -q langchain-openai langgraph
```

### 코드 구현

`코드 구현`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ============================================, [2] Node 정의 흐름이 주석과 함께 드러납니다.

```python
# ============================================
# [2] Node 정의
# ============================================

def draft_email(state: EmailState) -> dict:
    """이메일 초안 작성 노드"""
    print("\n  [draft_email] 이메일 초안 작성 중...")

    prompt = f"""
    다음 요청에 맞는 비즈니스 이메일을 작성해주세요.
    요청: {state['request']}
    수신자: {state['recipient']}

    다음 형식으로 작성해주세요:
    제목: [이메일 제목]
    ---
    [이메일 본문]
    """

    response = llm.invoke(prompt)
    content = response.content

    # 제목과 본문 분리
    lines = content.split("\n")
    subject = ""
    body_lines = []
    is_body = False

# ... trimmed ...
```

### Human-in-the-Loop 구현 3단계

`Human-in-the-Loop 구현 3단계`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Checkpointer 생성, 컴파일 시 interrupt_before 지정, 중단점 이후 재개 흐름이 주석과 함께 드러납니다.

```python
# 1. Checkpointer 생성
checkpointer = MemorySaver()  # 또는 SqliteSaver, PostgresSaver 등

# 2. 컴파일 시 interrupt_before 지정
app = workflow.compile(
    checkpointer=checkpointer,
    interrupt_before=["sensitive_node"]
)

# 3. 중단점 이후 재개
app.invoke(None, config)  # None 전달로 이어서 실행
```

### 프로덕션 Checkpointer

`프로덕션 Checkpointer`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 SQLite (파일 저장), PostgreSQL (서버 저장) 흐름이 주석과 함께 드러납니다.

```python
# SQLite (파일 저장)
from langgraph.checkpoint.sqlite import SqliteSaver
checkpointer = SqliteSaver.from_conn_string("checkpoints.db")

# PostgreSQL (서버 저장)
from langgraph.checkpoint.postgres import PostgresSaver
checkpointer = PostgresSaver.from_conn_string("postgresql://...")
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/4-4 LangGraph_4_사람승인.md`
- Source formats: `ipynb`, `md`
- Companion files: `4-4 LangGraph_4_사람승인.ipynb`, `4-4 LangGraph_4_사람승인.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - **Checkpoint**를 사용해 그래프 상태를 저장/복원한다 - **interrupt_before**로 특정 노드 전에 실행을 멈춘다 - 사용자 승인 후 이어서 실행하는 패턴을 구현한다
> AI 에이전트가 **민감한 작업**을 수행하기 전에 **사람의 승인**이 필요한 경우:
