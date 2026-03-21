---
title: "사내 규정 챗봇"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-5 (실습)사내_규정_챗봇"
source_path: "13_LLM_GenAI/Code_Snippets/3-5 (실습)사내_규정_챗봇.md"
excerpt: "사내 규정 챗봇 만들기, RAG 실습 준비, RAG 실습 시작 - LangChain 사용 중심으로 구현 과정을 정리한 사내 규정 챗봇 기록입니다"
research_summary: "사내 규정 챗봇 만들기, RAG 실습 준비, RAG 실습 시작 - LangChain 사용 중심으로 구현 과정을 정리한 사내 규정 챗봇 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 12개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_community, langchain_text_splitters, langchain_openai입니다."
research_artifacts: "ipynb/md · 코드 12개 · 실행 8개"
code_block_count: 12
execution_block_count: 8
research_focus:
  - "사내 규정 챗봇 만들기"
  - "RAG 실습 준비"
  - "RAG 실습 시작 - LangChain 사용"
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
  - archive-note
---

사내 규정 챗봇 만들기, RAG 실습 준비, RAG 실습 시작 - LangChain 사용 중심으로 구현 과정을 정리한 사내 규정 챗봇 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 12개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_community, langchain_text_splitters, langchain_openai입니다.

**빠르게 볼 수 있는 포인트**: 사내 규정 챗봇 만들기, RAG 실습 준비, RAG 실습 시작 - LangChain 사용.

**남겨둔 자료**: `ipynb/md` 원본과 12개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, langchain_community, langchain_text_splitters, langchain_openai입니다.

**주요 스택**: `os`, `langchain_community`, `langchain_text_splitters`, `langchain_openai`, `langchain_chroma`

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

## What This Note Covers

- 사내 규정 챗봇 만들기
- RAG 실습 준비
- RAG 실습 시작 - LangChain 사용
- 문서 로딩 (Loading)
- 문서 분할 (Splitting)

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

1. Key Step: 실습용 가상 데이터 생성 (사내 규정 문서)
2. Key Step: 실제로는 PDF나 txt 파일이 있는 경우가 많지만, 실습 편의를 위해 즉석에서 파일을 만듭니다.
3. Key Step: RAG 실습 시작 - LangChain 사용
4. Key Step: 문서 분할 (Splitting)

## Code Highlights

### RAG 실습 준비

`RAG 실습 준비`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 실습용 가상 데이터 생성 (사내 규정 문서), 실제로는 PDF나 txt 파일이 있는 경우가 많지만, 실습 편의를 위해 즉석에서 파일을..., 파일을 저장합니다. 흐름이 주석과 함께 드러납니다.

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

`임베딩 & 벡터 저장소 생성 (Indexing)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ==========================================, 임베딩 & 벡터 저장소 생성 (Indexing) 흐름이 주석과 함께 드러납니다.

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

### 검색기(Retriever) 설정 & 생성 (Generation)

`검색기(Retriever) 설정 & 생성 (Generation)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 프롬프트 템플릿 작성, {context}: 검색된 문서 내용이 들어갈 자리, {question}: 사용자 질문이 들어갈 자리 흐름이 주석과 함께 드러납니다.

```python
# 프롬프트 템플릿 작성
# {context}: 검색된 문서 내용이 들어갈 자리
# {question}: 사용자 질문이 들어갈 자리
template = """
당신은 회사의 인사 담당 AI입니다.
아래 [규정]을 참고하여 직원의 질문에 친절하게 답해주세요.
규정에 없는 내용은 "규정에 나와있지 않습니다"라고 답하세요.

[규정]
{context}

[질문]: {question}
"""
prompt = PromptTemplate.from_template(template)
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

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
