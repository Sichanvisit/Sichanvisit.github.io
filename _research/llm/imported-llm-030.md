---
title: "RAG 맛보기"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 RAG_맛보기"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 RAG_맛보기.md"
excerpt: "**RAG(Retrieval-Augmented Generation)**는 대규모 언어 모델(LLM)이 **외부의 지식(데이터)**을 참고하여 더 정확하고 풍부한 답변을 생성하도록 만드는 기술입니다."
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
| Code Blocks | 7 |
| Execution Cells | 3 |
| Libraries | `os`, `langchain_openai`, `langchain_core`, `getpass` |
| Source Note | `3-5 RAG_맛보기` |

## What I Worked On

- RAG (검색 증강 생성)
- **왜 RAG가 필요한가요?**
- **RAG의 작동 원리 (3단계)**
- Prompt the user for the OpenAI API key securely
- 1. 모델 준비

## Implementation Flow

1. RAG (검색 증강 생성)
2. **왜 RAG가 필요한가요?**
3. **RAG의 작동 원리 (3단계)**
4. Prompt the user for the OpenAI API key securely
5. 1. 모델 준비
6. 2. 우리 가게만의 지식 (Context) - 아직 DB 없이 변수로 직접 정의

## Code Highlights

### **RAG의 작동 원리 (3단계)**

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

### **RAG의 작동 원리 (3단계)**

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
