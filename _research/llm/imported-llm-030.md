---
title: "RAG 맛보기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 RAG_맛보기"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 RAG_맛보기.md"
excerpt: "RAG 맛보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 RAG (검색 증강 생성) 순서로 핵심 장면을 먼저 훑고, RAG의 작동 원리 (3단계) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 7개 코드 블록,..."
research_summary: "RAG 맛보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 RAG (검색 증강 생성) 순서로 핵심 장면을 먼저 훑고, RAG의 작동 원리 (3단계) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 7개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_openai, langchain_core, getpass입니다."
research_artifacts: "ipynb/md · 코드 7개 · 실행 3개"
code_block_count: 7
execution_block_count: 3
research_focus:
  - "RAG (검색 증강 생성)"
research_stack:
  - "os"
  - "langchain_openai"
  - "langchain_core"
  - "getpass"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

RAG 맛보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 RAG (검색 증강 생성) 순서로 핵심 장면을 먼저 훑고, RAG의 작동 원리 (3단계) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 7개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_openai, langchain_core, getpass입니다.

**빠르게 볼 수 있는 포인트**: RAG (검색 증강 생성).

**남겨둔 자료**: `ipynb/md` 원본과 7개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_openai, langchain_core, getpass입니다.

**주요 스택**: `os`, `langchain_openai`, `langchain_core`, `getpass`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 7 |
| Execution Cells | 3 |
| Libraries | `os`, `langchain_openai`, `langchain_core`, `getpass` |
| Source Note | `3-5 RAG_맛보기` |

## What This Note Covers

### RAG (검색 증강 생성)

RAG(Retrieval-Augmented Generation)는 대규모 언어 모델(LLM)이 외부의 지식(데이터)을 참고하여 더 정확하고 풍부한 답변을 생성하도록 만드는 기술입니다. 쉽게 비유하자면, "시험을 볼 때 교과서를 펼쳐 놓고 답을 찾는 오픈 북 테스트(Open-book Test)"와 같습니다.

- 읽을 포인트: 세부 흐름: 왜 RAG가 필요한가요?, RAG의 작동 원리 (3단계)

#### 왜 RAG가 필요한가요?

LLM(ChatGPT 등)은 다음과 같은 한계: 1. 최신 정보 부재: 학습 시점 이후의 정보는 알지 못합니다. 2. 환각 현상 (Hallucination): 모르는 내용도 사실인 것처럼 거짓말을 할 수 있습니다. 3. 사내/비공개 데이터 접근 불가: 기업 내부 문서나 개인적인 자...

#### RAG의 작동 원리 (3단계)

검색 (Retrieval): 사용자의 질문과 관련된 문서를 벡터 DB(Vector DB) 등에서 찾아옵니다. 2. 증강 (Augmented): 찾아온 정보를 프롬프트에 끼워 넣어(Context) 질문을 보강합니다. 3. 생성 (Generation): LLM은 보강된 정보를 바탕으로...

## Why This Matters

### RAG 검색 파이프라인

- 왜 필요한가: LLM이 외부 지식을 안정적으로 참조하게 하려면, 생성 전에 관련 문서를 정확히 찾아오는 검색 단계가 먼저 필요합니다.
- 왜 이 방식을 쓰는가: 이 방식은 모델 파라미터만 믿지 않고 최신 문서나 도메인 지식을 붙일 수 있어서 실제 서비스형 QA에 적합합니다.
- 원리: 문서를 청크로 나누고 임베딩한 뒤, 질문과 가까운 벡터를 검색해 프롬프트에 함께 넣는 구조로 동작합니다.

### 프롬프트 체인 구성

- 왜 필요한가: LLM 호출을 재현 가능하게 만들려면 입력 조합, 프롬프트 템플릿, 후처리 순서를 구조화할 필요가 있습니다.
- 왜 이 방식을 쓰는가: 체인 구조는 실험 중 프롬프트와 입력 변형을 비교하기 쉽고, 이후 RAG나 에이전트 단계로 확장하기도 좋습니다.
- 원리: 질문과 컨텍스트를 정해진 템플릿에 넣고, 모델 호출 결과를 다음 단계 입력으로 넘기며 처리 흐름을 구성합니다.

## Implementation Flow

1. RAG (검색 증강 생성): 왜 RAG가 필요한가요?, RAG의 작동 원리 (3단계)

## Code Highlights

### RAG의 작동 원리 (3단계)

`RAG의 작동 원리 (3단계)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 준비, 우리 가게만의 지식 (Context) - 아직 DB 없이 변수로 직접 정의 흐름이 주석과 함께 드러납니다.

```python
# 1. 모델 준비
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 2. 우리 가게만의 지식 (Context) - 아직 DB 없이 변수로 직접 정의
context = """
[맛있는 김밥집 메뉴판]
1. 원조 김밥: 3,000원 - 40년 전통의 맛
2. 치즈 폭탄 김밥: 4,500원 - 모짜렐라 치즈가 듬뿍
3. 불닭 김밥: 5,000원 - 아주 매움, 맵찔이 금지
* 영업 시간: 오전 10시 ~ 오후 8시 (매주 월요일 휴무)
"""
```

### RAG의 작동 원리 (3단계)

`RAG의 작동 원리 (3단계)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 프롬프트 템플릿 만들기, RAG의 핵심: {context} 자리에 검색된 문서를 넣는 것! 흐름이 주석과 함께 드러납니다.

```python
# 3. 프롬프트 템플릿 만들기
# RAG의 핵심: {context} 자리에 검색된 문서를 넣는 것!
template = """
당신은 친절한 김밥집 점원입니다.
아래 [참고 정보]를 바탕으로 손님의 [질문]에 답변해주세요.
정보에 없는 내용은 "잘 모르겠습니다"라고 답하세요.

[참고 정보]
{context}

[질문]: {question}
"""

prompt = PromptTemplate.from_template(template)
```

### RAG의 작동 원리 (3단계)

`RAG의 작동 원리 (3단계)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 LangChain의 파이프라인: LangChain Expression Language(L..., 프롬프트 -> LLM -> 문자열 변환 흐름이 주석과 함께 드러납니다.

```python
# 4. LangChain의 파이프라인: LangChain Expression Language(LCEL)
# 프롬프트 -> LLM -> 문자열 변환
chain = prompt | llm | StrOutputParser()
```

### RAG의 작동 원리 (3단계)

`RAG의 작동 원리 (3단계)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 실행 및 결과 확인 흐름이 주석과 함께 드러납니다.

```python
# 5. 실행 및 결과 확인
question = "불닭 김밥 얼마인가요? 그리고 지금 저녁 9시인데 가도 되나요?"

response = chain.invoke({"context": context, "question": question})

print("=== AI 답변 ===")
print(response)
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 RAG_맛보기.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 RAG_맛보기.ipynb`, `3-5 RAG_맛보기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `ai.google.dev`, `platform.openai.com`

## Note Preview

> **RAG(Retrieval-Augmented Generation)**는 대규모 언어 모델(LLM)이 **외부의 지식(데이터)**을 참고하여 더 정확하고 풍부한 답변을 생성하도록 만드는 기술입니다.
> 쉽게 비유하자면, **"시험을 볼 때 교과서를 펼쳐 놓고 답을 찾는 오픈 북 테스트(Open-book Test)"**와 같습니다.
