---
title: "여행 가이드 봇 만들기 혼자실습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Practice"
source_title: "3-5 (실습)여행_가이드_봇_만들기_혼자실습"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)여행_가이드_봇_만들기_혼자실습.md"
excerpt: "LLM Practice: 여행 가이드 봇 만들기 - 혼자 실습, RAG 실습 준비"
tags:
  - research-archive
  - imported-note
  - llm
  - practice
---

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

## What I Worked On

- 여행 가이드 봇 만들기 - 혼자 실습
- RAG 실습 준비
- 0. 초기 설정
- OpenAI API key
- API키 설정

## Implementation Flow

1. 여행 가이드 봇 만들기 - 혼자 실습
2. RAG 실습 준비
3. 0. 초기 설정
4. OpenAI API key
5. API키 설정
6. 실습용 데이터 (제주도 맛집 가이드)

## Code Highlights

### RAG 실습 준비

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

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 (실습)여행_가이드_봇_만들기_혼자실습.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 (실습)여행_가이드_봇_만들기_혼자실습.ipynb`, `3-5 (실습)여행_가이드_봇_만들기_혼자실습.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
