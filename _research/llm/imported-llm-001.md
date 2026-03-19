---
title: "10 4팀 손성경"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "10_4팀_손성경"
source_path: "13_LLM_GenAI/Code_Snippets/10_4팀_손성경.md"
excerpt: "텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현"
research_summary: "텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현. 18,846개의 뉴스 문서를 20개의 카테고리로 분류한 News Group 20 데이터 (뉴스 기사가 아니라 인터넷 포럼 글 모음집). `ipynb/md` 원본과 84개 코드 블록, 64개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 gensim, os, re, torch입니다."
research_artifacts: "ipynb/md · 코드 84개 · 실행 64개"
code_block_count: 84
execution_block_count: 64
research_focus:
  - "텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현"
  - "18,846개의 뉴스 문서를 20개의 카테고리로 분류한 News Group 20 데이터 (뉴스 기사가..."
  - "데이터 전처리"
research_stack:
  - "gensim"
  - "os"
  - "re"
  - "torch"
  - "numpy"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현. 18,846개의 뉴스 문서를 20개의 카테고리로 분류한 News Group 20 데이터 (뉴스 기사가 아니라 인터넷 포럼 글 모음집). `ipynb/md` 원본과 84개 코드 블록, 64개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 gensim, os, re, torch입니다.

**빠르게 볼 수 있는 포인트**: 텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는..., 18,846개의 뉴스 문서를 20개의 카테고리로 분류한 News Gro..., 데이터 전처리.

**남겨둔 자료**: `ipynb/md` 원본과 84개 코드 블록, 64개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 gensim, os, re, torch입니다.

**주요 스택**: `gensim`, `os`, `re`, `torch`, `numpy`

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

## What This Note Covers

### Problem Brief

텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현

### Dataset Context

18,846개의 뉴스 문서를 20개의 카테고리로 분류한 News Group 20 데이터 (뉴스 기사가 아니라 인터넷 포럼 글 모음집)

### Implementation Guide

데이터 전처리: 텍스트 데이터 -> 토큰화, train/test 적절히 분리 2. 임베딩 적용: Word2Vec, FastText, GloVe 방식으로 입력 데이터를 벡터화 -> 임베딩 행렬 생성 3. 데이터셋 및 로더 구현 4. 모델 구현: - LSTM, GRU 등 RNN 기반의 딥 러닝 모델 사용 - 임베딩 레이어 추가 -> 입력 데이터와 임베딩 벡터를 연결 - 각 임베딩 방식(Wo...

### 데이터 살펴보기

어떤 데이터인지 파악하기 위해 먼저 데이터 타입과 속성을 확인해보았다

## Implementation Flow

1. Problem Brief: 텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현
2. Dataset Context: 18,846개의 뉴스 문서를 20개의 카테고리로 분류한 News Group 20 데이터 (뉴스 기사가 아니라 인터넷 포럼 글 모음집)
3. Implementation Guide: 데이터 전처리: 텍스트 데이터 -> 토큰화, train/test 적절히 분리 2. 임베딩 적용: Word2Vec, FastText, GloVe 방식으로 입력 데이터를 벡터화 -> 임베딩 행렬 생성 3. 데이터셋 및 로더 구현 4. 모델 구현: - LSTM, G...
4. 데이터 살펴보기: 어떤 데이터인지 파악하기 위해 먼저 데이터 타입과 속성을 확인해보았다

## Code Highlights

### 전처리 비교 실험

`전처리 비교 실험`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 전처리 v1 학습, ======== 전처리 버전 선택 =========, ================================== 흐름이 주석과 함께 드러납니다.

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

### 3종 임베딩 실험

`3종 임베딩 실험`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 실험 자동화 파이프라인, ==========================================, 실험할 전처리 버전 2개 선택 흐름이 주석과 함께 드러납니다.

```python
# @title 실험 자동화 파이프라인

# ==========================================
# 0) 실험할 전처리 버전 2개 선택
# ==========================================
target_preprocesses = [
    "v2_1_patterns_preserved",
    "v3_1_stopword_removed_patterns_preserved"
]

target_embeddings = ["word2vec", "fasttext", "glove"]

results_embed = []   # 결과 저장


# ==========================================
# 1) 실험 시작
# ==========================================
for prep_name in target_preprocesses:

    clean_fn = clean_fns[prep_name]
    print(f"\n==============================")
    print("전처리 버전:", prep_name)
    print("==============================")

    # 전처리 → 토큰화
    train_clean = [clean_fn(t) for t in X_train]
    test_clean  = [clean_fn(t) for t in X_test]
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
