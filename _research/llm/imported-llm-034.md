---
title: "LangGraph 4 사람승인"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "4-4 LangGraph_4_사람승인"
source_path: "13_LLM_GenAI/Code_Snippets/4-4 LangGraph_4_사람승인.md"
excerpt: "- **Checkpoint**를 사용해 그래프 상태를 저장/복원한다 - **interrupt_before**로 특정 노드 전에 실행을 멈춘다 - 사용자 승인 후 이어서 실행하는 패턴을 구현한다"
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
| Execution Cells | 12 |
| Libraries | `os`, `getpass`, `typing`, `langchain_openai`, `langgraph`, `IPython` |
| Source Note | `4-4 LangGraph_4_사람승인` |

## What I Worked On

- LangGraph 실습 4: Human-in-the-Loop (HITL)
- 핵심 개념: 왜 Human-in-the-Loop가 필요한가?
- 0. 환경 설정
- 패키지 설치
- API 키 설정

## Implementation Flow

1. LangGraph 실습 4: Human-in-the-Loop (HITL)
2. 핵심 개념: 왜 Human-in-the-Loop가 필요한가?
3. 0. 환경 설정
4. 패키지 설치
5. API 키 설정
6. 1. 시나리오: 이메일 발송 에이전트

## Code Highlights

### 2. 코드 구현

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

### 3. 실행: 1단계 - 중단점까지 실행

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
