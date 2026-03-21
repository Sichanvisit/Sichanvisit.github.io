---
title: "여행 가이드 봇 만들기 혼자실습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Practice"
source_title: "3-5 (실습)여행_가이드_봇_만들기_혼자실습"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)여행_가이드_봇_만들기_혼자실습.md"
excerpt: "여행 가이드 봇 만들기 - 혼자 실습, RAG 실습 준비, 초기 설정 중심으로 구현 과정을 정리한 여행 가이드 봇 만들기 혼자실습 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과..."
research_summary: "여행 가이드 봇 만들기 - 혼자 실습, RAG 실습 준비, 초기 설정 중심으로 구현 과정을 정리한 여행 가이드 봇 만들기 혼자실습 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 10개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_community, langchain_text_splitters, langchain_openai입니다."
research_artifacts: "ipynb/md · 코드 10개 · 실행 7개"
code_block_count: 10
execution_block_count: 7
research_focus:
  - "여행 가이드 봇 만들기 - 혼자 실습"
  - "RAG 실습 준비"
  - "초기 설정"
research_stack:
  - "os"
  - "langchain_community"
  - "langchain_text_splitters"
  - "langchain_openai"
  - "langchain_chroma"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - practice
---

여행 가이드 봇 만들기 - 혼자 실습, RAG 실습 준비, 초기 설정 중심으로 구현 과정을 정리한 여행 가이드 봇 만들기 혼자실습 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 10개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_community, langchain_text_splitters, langchain_openai입니다.

**빠르게 볼 수 있는 포인트**: 여행 가이드 봇 만들기 - 혼자 실습, RAG 실습 준비, 초기 설정.

**남겨둔 자료**: `ipynb/md` 원본과 10개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_community, langchain_text_splitters, langchain_openai입니다.

**주요 스택**: `os`, `langchain_community`, `langchain_text_splitters`, `langchain_openai`, `langchain_chroma`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 10 |
| Execution Cells | 7 |
| Libraries | `os`, `langchain_community`, `langchain_text_splitters`, `langchain_openai`, `langchain_chroma`, `langchain_core`, `getpass` |
| Source Note | `3-5 (실습)여행_가이드_봇_만들기_혼자실습` |

## What This Note Covers

- 여행 가이드 봇 만들기 - 혼자 실습
- RAG 실습 준비
- 초기 설정
- OpenAI API key
- API키 설정

## Why This Matters

### RAG 검색 파이프라인

- 왜 필요한가: LLM이 외부 지식을 안정적으로 참조하게 하려면, 생성 전에 관련 문서를 정확히 찾아오는 검색 단계가 먼저 필요합니다.
- 왜 이 방식을 쓰는가: 이 방식은 모델 파라미터만 믿지 않고 최신 문서나 도메인 지식을 붙일 수 있어서 실제 서비스형 QA에 적합합니다.
- 원리: 문서를 청크로 나누고 임베딩한 뒤, 질문과 가까운 벡터를 검색해 프롬프트에 함께 넣는 구조로 동작합니다.

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 프롬프트 체인 구성

- 왜 필요한가: LLM 호출을 재현 가능하게 만들려면 입력 조합, 프롬프트 템플릿, 후처리 순서를 구조화할 필요가 있습니다.
- 왜 이 방식을 쓰는가: 체인 구조는 실험 중 프롬프트와 입력 변형을 비교하기 쉽고, 이후 RAG나 에이전트 단계로 확장하기도 좋습니다.
- 원리: 질문과 컨텍스트를 정해진 템플릿에 넣고, 모델 호출 결과를 다음 단계 입력으로 넘기며 처리 흐름을 구성합니다.

## Implementation Flow

1. Key Step: 여행 가이드 봇 만들기 - 혼자 실습
2. Key Step: 실습용 데이터 (제주도 맛집 가이드)
3. Key Step: 문서를 불러오고(Load) 자르기(Split)

## Code Highlights

### RAG 실습 준비

`RAG 실습 준비`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 실습용 데이터 (제주도 맛집 가이드), 파일 생성 흐름이 주석과 함께 드러납니다.

```python
# 실습용 데이터 (제주도 맛집 가이드)
jeju_content = """
[제주도 맛집 & 여행 가이드]
1. 흑돼지 거리: 제주시 건입동에 위치. 저녁 7시 이후에는 웨이팅이 1시간 이상 발생할 수 있음.
   추천 메뉴는 흑돼지 오겹살(200g 2만원). 멜젓에 찍어 먹는 것이 특징.

2. 우도 땅콩 아이스크림: 우도 검멀레 해변 앞이 원조. 가격은 5,000원.
   고소한 땅콩 가루가 듬뿍 뿌려져 있음. 배 시간 때문에 오후 4시 이전에 가는 것을 추천.

3. 성산일출봉: 입장료 5,000원. 왕복 소요 시간 50분.
   매월 첫째 주 월요일은 휴관. 새벽 일출을 보려면 전날 근처 숙소 예약 필수.
"""

# 파일 생성
with open("jeju_guide.txt", "w", encoding="utf-8") as f:
    f.write(jeju_content)
print("제주도 가이드북 파일 생성 완료")
```

### RAG 실습 준비

`RAG 실습 준비`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ==========================================, RAG 체인을 완성 흐름이 주석과 함께 드러납니다.

```python
# ==========================================
# RAG 체인을 완성
# ==========================================
print("\n 답변 생성 준비 중...")

retriever = vectorstore.as_retriever()

# LLM 설정
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 프롬프트 템플릿
template = """
당신은 제주도 여행 가이드입니다.
[정보]를 바탕으로 여행객의 질문에 답변해주세요.

[정보]
{context}

[질문]: {question}
"""
prompt = PromptTemplate.from_template(template)
```

### RAG 실습 준비

`RAG 실습 준비`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ==========================================, 테스트 실행 흐름이 주석과 함께 드러납니다.

```python
# ==========================================
# 테스트 실행
# ==========================================
# 질문하기
query = "흑돼지 먹으려면 어디로 가야 해? 그리고 성산일출봉 입장료는 얼마야?"
print(f"\n 질문: {query}")

# 답변 출력
response = rag_chain.invoke(query)
print("\n=== AI 가이드의 답변 ===")
print(response)
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 (실습)여행_가이드_봇_만들기_혼자실습.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 (실습)여행_가이드_봇_만들기_혼자실습.ipynb`, `3-5 (실습)여행_가이드_봇_만들기_혼자실습.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
