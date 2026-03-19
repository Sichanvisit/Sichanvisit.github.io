---
title: "10 4팀 손성경"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "10_4팀_손성경"
source_path: "13_LLM_GenAI/Code_Snippets/10_4팀_손성경.md"
excerpt: "텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현"
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
| Code Blocks | 84 |
| Execution Cells | 64 |
| Libraries | `gensim`, `os`, `re`, `torch`, `numpy`, `pandas`, `nltk`, `sklearn` |
| Source Note | `10_4팀_손성경` |

## What I Worked On

- 스프린트 미션 10
- 1. **지침**
- 2. **데이터셋 설명**
- 3. **가이드라인**
- 0. 환경준비

## Implementation Flow

1. 스프린트 미션 10
2. 1. **지침**
3. 2. **데이터셋 설명**
4. 3. **가이드라인**
5. 0. 환경준비
6. import

## Code Highlights

### 4. 전처리 비교 실험

```python
# @title 전처리 v1 학습
'''
clean_fns = {
    "v1_minimal": clean_text_v1,
    "v2_special_removed": clean_text_v2,
    "v2_1_patterns_preserved": clean_text_v2_1,
    "v3_stopword_removed": clean_text_v3
}
'''
# ======== 전처리 버전 선택 =========
clean_fn = clean_fns["v1_minimal"]   # ← 여기만 바꿔서 실험
print("사용 중인 전처리 버전:", clean_fn.__name__)
# ==================================

# 1) 텍스트 전처리
train_clean = [clean_fn(t) for t in X_train]
test_clean  = [clean_fn(t) for t in X_test]

# 2) 토큰화
train_tokens = [t.split() for t in train_clean]
test_tokens  = [t.split() for t in test_clean]

# 3) FastText 학습
ft = FastText(
    sentences=train_tokens,
    vector_size=vector_size,
    window=5,
    min_count=1,
# ... trimmed ...
```

### 4. 전처리 비교 실험

```python
# @title 전처리 v2 학습
'''
clean_fns = {
    "v1_minimal": clean_text_v1,
    "v2_special_removed": clean_text_v2,
    "v2_1_patterns_preserved": clean_text_v2_1,
    "v3_stopword_removed": clean_text_v3
}
'''
# ======== 전처리 버전 선택 =========
clean_fn = clean_fns["v2_special_removed"]   # ← 여기만 바꿔서 실험
print("사용 중인 전처리 버전:", clean_fn.__name__)
# ==================================

# 1) 텍스트 전처리
train_clean = [clean_fn(t) for t in X_train]
test_clean  = [clean_fn(t) for t in X_test]

# 2) 토큰화
train_tokens = [t.split() for t in train_clean]
test_tokens  = [t.split() for t in test_clean]

# 3) FastText 학습
ft = FastText(
    sentences=train_tokens,
    vector_size=vector_size,
    window=5,
    min_count=1,
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/10_4팀_손성경.md`
- Source formats: `ipynb`, `md`
- Companion files: `10_4팀_손성경.ipynb`, `10_4팀_손성경.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `nlp.stanford.edu`

## Note Preview

> 텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현
> 18,846개의 뉴스 문서를 20개의 카테고리로 분류한 News Group 20 데이터 (뉴스 기사가 아니라 인터넷 포럼 글 모음집)
