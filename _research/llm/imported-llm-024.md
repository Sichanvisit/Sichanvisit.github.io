---
title: "사내 규정 챗봇"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)사내_규정_챗봇"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)사내_규정_챗봇.md"
excerpt: "LLM Archive Note: 사내 규정 챗봇 만들기, RAG 실습 준비, RAG 실습 시작 - LangChain 사용"
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
| Code Blocks | 12 |
| Execution Cells | 8 |
| Libraries | `os`, `langchain_community`, `langchain_text_splitters`, `langchain_openai`, `langchain_chroma`, `langchain_core`, `getpass` |
| Source Note | `3-5 (실습)사내_규정_챗봇` |

## What I Worked On

- 사내 규정 챗봇 만들기
- RAG 실습 준비
- 0. 초기 설정
- OpenAI API key
- API키 설정

## Implementation Flow

1. 사내 규정 챗봇 만들기
2. RAG 실습 준비
3. 0. 초기 설정
4. OpenAI API key
5. API키 설정
6. 실습용 가상 데이터 생성 (사내 규정 문서)

## Code Highlights

### RAG 실습 준비

```python
# 실습용 가상 데이터 생성 (사내 규정 문서)
# 실제로는 PDF나 txt 파일이 있는 경우가 많지만, 실습 편의를 위해 즉석에서 파일을 만듭니다.
policy_content = """
[주식회사 랭체인 인사 규정]
제1조 (근무 시간)
1. 근무 시간은 오전 9시부터 오후 6시까지로 한다.
2. 유연 근무제를 시행하며, 코어 타임(오전 11시~오후 3시)을 준수해야 한다.

제2조 (휴가)
1. 연차 휴가는 입사 1년 후 15일이 발생한다.
2. 3년 이상 근속 시 안식월 1개월을 유급으로 제공한다.
3. 반차, 반반차 사용이 가능하며 당일 신청도 가능하다.
4. 여름 휴가는 7월~8월 중 5일을 별도로 제공한다.

제3조 (복지)
1. 도서 구입비는 월 10만원 한도 내에서 무제한 지원한다.
2. 야근 시 택시비와 식대는 법인 카드로 결제한다.
"""

# 파일을 저장합니다.
with open("company_policy.txt", "w", encoding="utf-8") as f:
    f.write(policy_content)

print("[준비 완료] 사내 규정 문서가 생성되었습니다.")
```

### 임베딩 & 벡터 저장소 생성 (Indexing)

```python
# ==========================================
# 3. 임베딩 & 벡터 저장소 생성 (Indexing)
# ==========================================
print("\n 문서를 벡터로 변환하여 저장합니다...")
# OpenAI의 가성비 임베딩 모델 사용
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings(model="text-embedding-3-small")
)
print("   -> Chroma DB에 저장 완료!")
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-5 (실습)사내_규정_챗봇.md`
- Source formats: `ipynb`, `md`
- Companion files: `3-5 (실습)사내_규정_챗봇.ipynb`, `3-5 (실습)사내_규정_챗봇.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
