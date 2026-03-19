---
title: "LangGraph 4 사람승인"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-4 LangGraph_4_사람승인"
source_path: "13_LLM_GenAI/Code_Snippets/4-4 LangGraph_4_사람승인.md"
excerpt: "Checkpoint를 사용해 그래프 상태를 저장/복원한다 - interrupt_before로 특정 노드 전에 실행을 멈춘다 - 사용자 승인 후 이어서 실행하는 패턴을 구현한다"
research_summary: "Checkpoint를 사용해 그래프 상태를 저장/복원한다 - interrupt_before로 특정 노드 전에 실행을 멈춘다 - 사용자 승인 후 이어서 실행하는 패턴을 구현한다. AI 에이전트가 민감한 작업을 수행하기 전에 사람의 승인이 필요한 경우. `ipynb/md` 원본과 19개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 12개"
code_block_count: 19
execution_block_count: 12
research_focus:
  - "Checkpoint를 사용해 그래프 상태를 저장/복원한다 - interrupt_before로 특정 노드..."
  - "LangGraph 실습 4"
  - "AI 에이전트가 민감한 작업을 수행하기 전에 사람의 승인이 필요한 경우"
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

Checkpoint를 사용해 그래프 상태를 저장/복원한다 - interrupt_before로 특정 노드 전에 실행을 멈춘다 - 사용자 승인 후 이어서 실행하는 패턴을 구현한다. AI 에이전트가 민감한 작업을 수행하기 전에 사람의 승인이 필요한 경우. `ipynb/md` 원본과 19개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, getpass, typing, langchain_openai입니다.

**빠르게 볼 수 있는 포인트**: Checkpoint를 사용해 그래프 상태를 저장/복원한다 - inter..., LangGraph 실습 4, AI 에이전트가 민감한 작업을 수행하기 전에 사람의 승인이 필요한 경우.

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

### 핵심 개념: 왜 Human-in-the-Loop가 필요한가?

AI 에이전트가 민감한 작업을 수행하기 전에 사람의 승인이 필요한 경우

### 시나리오: 이메일 발송 에이전트

사용자 요청을 받아 이메일 초안을 작성하고, 발송 전에 사용자 확인을 받는 에이전트입니다.

### 주요 메서드

/ 메서드 / 설명 / /--------/------/ / app.invoke(None, config) / 중단점 이후 이어서 실행 / / app.get_state(config) / 현재 상태 조회 / / app.update_state(config, values) / 상태 수정 / / app.get_state_history(config) / 상태 히스토리 조회 /

## Implementation Flow

1. LangGraph 실습 4: Human-in-the-Loop (HITL): Checkpoint를 사용해 그래프 상태를 저장/복원한다 - interrupt_before로 특정 노드 전에 실행을 멈춘다 - 사용자 승인 후 이어서 실행하는 패턴을 구현한다
2. 핵심 개념: 왜 Human-in-the-Loop가 필요한가?: AI 에이전트가 민감한 작업을 수행하기 전에 사람의 승인이 필요한 경우
3. 시나리오: 이메일 발송 에이전트: 사용자 요청을 받아 이메일 초안을 작성하고, 발송 전에 사용자 확인을 받는 에이전트입니다.
4. 주요 메서드: / 메서드 / 설명 / /--------/------/ / app.invoke(None, config) / 중단점 이후 이어서 실행 / / app.get_state(config) / 현재 상태 조회 / / app.update_state(config, values) / 상태 수정 / /...

## Code Highlights

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

### 실행: 1단계 - 중단점까지 실행

`실행: 1단계 - 중단점까지 실행`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 스레드 ID: 대화 세션 식별자, 초기 입력, 실행 (send_email 전에 자동으로 멈춤) 흐름이 주석과 함께 드러납니다.

```python
# 스레드 ID: 대화 세션 식별자
thread_id = "email-session-001"
config = {"configurable": {"thread_id": thread_id}}

# 초기 입력
initial_input = {
    "request": "프로젝트 진행 상황 보고 및 다음 주 미팅 요청",
    "recipient": "김팀장님",
    "subject": "",
    "body": "",
    "review_notes": "",
    "is_sent": False,
    "status": "시작"
}

print("=" * 60)
print("--1단계: 이메일 작성 및 검토 (send_email 전에 멈춤)")
print("=" * 60)

# 실행 (send_email 전에 자동으로 멈춤)
result = app.invoke(initial_input, config)

print("\n" + "=" * 60)
print("⏸️ 중단됨! 현재 상태:")
print("=" * 60)
print(f"상태: {result['status']}")
print(f"제목: {result['subject']}")
print(f"검토 노트: {result['review_notes']}")
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
> ---
