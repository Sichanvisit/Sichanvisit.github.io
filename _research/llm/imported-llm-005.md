---
title: "텍스트벡터화"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)텍스트벡터화"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)텍스트벡터화.md"
excerpt: "백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다"
research_summary: "백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다. 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움. `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다."
research_artifacts: "md · 코드 25개 · 실행 25개"
code_block_count: 25
execution_block_count: 25
research_focus:
  - "백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다."
  - "텍스트 벡터화"
  - "단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움"
research_stack:
  - "google"
  - "pandas"
  - "sklearn"
  - "numpy"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다. 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움. `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다.

**빠르게 볼 수 있는 포인트**: 백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다., 텍스트 벡터화, 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를....

**남겨둔 자료**: `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다.

**주요 스택**: `google`, `pandas`, `sklearn`, `numpy`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 25 |
| Execution Cells | 25 |
| Libraries | `google`, `pandas`, `sklearn`, `numpy`, `matplotlib`, `shutil`, `gensim` |
| Source Note | `3-1(실습)텍스트벡터화` |

## What This Note Covers

### 텍스트 벡터화

백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다.

### Bag-of-Word(BoW)

단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움

### TD-IDF(Term Frequency-Inverse Document Frequency)

단어 빈도(TF)와 전체 문서에서의 희소성(IDF)을 결합하여 단어의 중요도 측정 - 비교적 BoW보다 문서내에서의 의미 있는 단어 식별

### Word Embedding

Word2Vec, Glove등 각 단어를 저차원 벡터로 표현 - 단어간의 의미적 유사성을 벡터 공간에서 반영

## Implementation Flow

1. 텍스트 벡터화: 백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다.
2. Bag-of-Word(BoW): 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움
3. TD-IDF(Term Frequency-Inverse Document Frequency): 단어 빈도(TF)와 전체 문서에서의 희소성(IDF)을 결합하여 단어의 중요도 측정 - 비교적 BoW보다 문서내에서의 의미 있는 단어 식별
4. Word Embedding: Word2Vec, Glove등 각 단어를 저차원 벡터로 표현 - 단어간의 의미적 유사성을 벡터 공간에서 반영

## Code Highlights

### Bag-of-Word(BoW) 빈도 벡터화

`Bag-of-Word(BoW) 빈도 벡터화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 90% 이상으로 빈도가 많은 토큰을 제외, 10개 이하로 빈도가 적은 토큰을 제외 흐름이 주석과 함께 드러납니다.

```python
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# 90% 이상으로 빈도가 많은 토큰을 제외
# 10개 이하로 빈도가 적은 토큰을 제외
cvec = CountVectorizer(max_df=0.9, min_df=10)
cvec.fit(df['text_tag']) # 토큰생성(띄어쓰기 기반)

tokens = cvec.get_feature_names_out()   # 토큰 목록 확인
names = cvec.vocabulary_                # 토큰 사전 확인

print(len(tokens))
print(names)
```

### TD-IDF 벡터화

`TD-IDF 벡터화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. TD-IDF 벡터는 sklearn모듈의 TfidVectorizer를 이용하여 간단하게 구현할 수 있습니다. 활용방법은 CountVectorizer와 동일합니다. sklearn.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfvec = TfidfVectorizer(max_df=0.9, min_df=10)
tfvec.fit(df['text_tag'])       # 토큰 생성(띄어쓰기 기반)

tokens = tfvec.get_feature_names_out()   # 토큰 목록 확인
names = tfvec.vocabulary_                # 토큰 사전 확인

print(tokens)
print(names)
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-1(실습)텍스트벡터화.md`
- Source formats: `md`
- Companion files: `3-1(실습)텍스트벡터화.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `scikit-learn.org`, `drive.google.com`, `localhost`

## Note Preview

> 백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다.
> - 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움
