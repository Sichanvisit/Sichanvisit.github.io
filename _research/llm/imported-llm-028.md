---
title: "AI Agent 맛보기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 AI_Agent_맛보기"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 AI_Agent_맛보기.md"
excerpt: "단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, **에이전트(Agent)**는 스스로 계획을 세우고 **도구(Tool)**를 사용하여 실제 행동을 합니다."
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
| Code Blocks | 6 |
| Execution Cells | 4 |
| Libraries | `os`, `getpass`, `langchain_openai`, `langchain_community`, `langgraph`, `langchain_core` |
| Source Note | `3-5 AI_Agent_맛보기` |

## What I Worked On

- AI Agent: 실시간 웹 검색 에이전트 (ReAct:Reasoning + Acting)
- AI 에이전트(AI Agent)란?
- ReAct 에이전트란?
- 1. 라이브러리 설치
- 2. OpenAI API Key 설정

## Implementation Flow

1. AI Agent: 실시간 웹 검색 에이전트 (ReAct:Reasoning + Acting)
2. AI 에이전트(AI Agent)란?
3. ReAct 에이전트란?
4. 1. 라이브러리 설치
5. 2. OpenAI API Key 설정
6. 검색 도구 및 에이전트 생성

## Code Highlights

### 검색 도구 및 에이전트 생성

```python
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent

# 1. LLM 정의
llm = ChatOpenAI(model="gpt-4o-mini")

# 2. 도구(Tool) 정의 - 실제 웹 검색 도구 사용
# DuckDuckGoSearchRun은 API Key 없이 무료로 검색 가능한 도구입니다.: https://start.duckduckgo.com/
search_tool = DuckDuckGoSearchRun()
tools = [search_tool]

# 3. 미리 만들어진 ReAct 에이전트 생성
# LangGraph create_react_agent가 내부적으로 노드, 엣지, 분기 로직을 모두 자동으로 설정해줍니다.
agent_executor = create_react_agent(llm, tools)

print("---검색 에이전트 생성 완료!")
```

### 에이전트 테스트 (실시간 검색)

```python
from langchain_core.messages import HumanMessage

def run_agent(question):
    print(f"\n 질문: {question}")
    print("-" * 50)

    # 에이전트 실행 (스트리밍으로 과정 확인)
    inputs = {"messages": [HumanMessage(content=question)]}

    for chunk in agent_executor.stream(inputs, stream_mode="values"):
        # 메시지의 마지막 내용만 출력
        message = chunk["messages"][-1]

        # 도구가 실행되거나 답변이 생성될 때 출력
        if message.type == "ai":
            # 도구 호출이 포함된 경우
            if message.tool_calls:
                print(f"================[생각] 검색이 필요해! -> '{message.tool_calls[0]['args']}' 검색 시도...")
            # 최종 답변인 경우
            else:
                print(f"================[답변] {message.content}")
        elif message.type == "tool":
            print(f"================[결과] 검색 완료 (내용 일부: {message.content[:100]}...)")
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 AI_Agent_맛보기.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 AI_Agent_맛보기.ipynb`, `3-5 AI_Agent_맛보기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `start.duckduckgo.com`

## Note Preview

> 단순한 LLM(ChatGPT 등)은 묻는 말에 대답만 할 수 있지만, **에이전트(Agent)**는 스스로 계획을 세우고 **도구(Tool)**를 사용하여 실제 행동을 합니다.
> - 에이전트의 핵심 작동 원리: 에이전트는 ReAct (Reasoning + Acting) 방식을 주로 사용합니다.
