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

## Why This Matters

### 에이전트 상태 흐름

- 왜 필요한가: 단일 호출만으로 해결되지 않는 작업은 추론, 도구 호출, 중간 상태 관리가 이어지는 흐름 제어가 필요합니다.
- 왜 이 방식을 쓰는가: 상태 그래프 기반 접근은 단계별 분기와 재시도를 명시적으로 관리할 수 있어 에이전트 실험을 설명하기 좋습니다.
- 원리: 현재 상태를 노드 간에 전달하면서, 조건에 따라 다음 노드나 도구 호출을 결정하는 방식으로 실행 흐름이 이어집니다.

### 프롬프트 체인 구성

- 왜 필요한가: LLM 호출을 재현 가능하게 만들려면 입력 조합, 프롬프트 템플릿, 후처리 순서를 구조화할 필요가 있습니다.
- 왜 이 방식을 쓰는가: 체인 구조는 실험 중 프롬프트와 입력 변형을 비교하기 쉽고, 이후 RAG나 에이전트 단계로 확장하기도 좋습니다.
- 원리: 질문과 컨텍스트를 정해진 템플릿에 넣고, 모델 호출 결과를 다음 단계 입력으로 넘기며 처리 흐름을 구성합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

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

### 실행: 2단계 - 승인 후 이어서 실행

`실행: 2단계 - 승인 후 이어서 실행`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 사용자 승인 시뮬레이션, 실제 앱에서는 UI를 통해 승인/거절 받음, ⭐ 핵심: None을 전달하면 중단점 이후부터 이어서 실행 흐름이 주석과 함께 드러납니다.

```python
# 사용자 승인 시뮬레이션
print("\n" + "=" * 60)
print("사용자 확인")
print("=" * 60)

# 실제 앱에서는 UI를 통해 승인/거절 받음
user_decision = "승인"  # or "거절"

if user_decision == "승인":
    print("-- 사용자가 발송을 승인했습니다.")
    print("\n 이어서 실행합니다...\n")

    # ⭐ 핵심: None을 전달하면 중단점 이후부터 이어서 실행
    final_result = app.invoke(None, config)

    print("\n" + "=" * 60)
    print("-- 최종 결과")
    print("=" * 60)
    print(f"상태: {final_result['status']}")
    print(f"발송 여부: {final_result['is_sent']}")
else:
    print("❌ 사용자가 발송을 거절했습니다.")
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
