---
title: "ai5 벡터화 한글폰트이슈"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1 ai5_벡터화_한글폰트이슈"
source_path: "13_LLM_GenAI/Code_Snippets/3-1 ai5_벡터화_한글폰트이슈.md"
excerpt: "백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다"
research_summary: "백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다. 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움. `md` 원본과 28개 코드 블록, 23개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다."
research_artifacts: "md · 코드 28개 · 실행 23개"
code_block_count: 28
execution_block_count: 23
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

백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다. 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움. `md` 원본과 28개 코드 블록, 23개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다.

**빠르게 볼 수 있는 포인트**: 백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다., 텍스트 벡터화, 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를....

**남겨둔 자료**: `md` 원본과 28개 코드 블록, 23개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다.

**주요 스택**: `google`, `pandas`, `sklearn`, `numpy`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 28 |
| Execution Cells | 23 |
| Libraries | `google`, `pandas`, `sklearn`, `numpy`, `matplotlib`, `shutil`, `gensim` |
| Source Note | `3-1 ai5_벡터화_한글폰트이슈` |

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

`Bag-of-Word(BoW) 빈도 벡터화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. CounterVectorizer에는 fit함수에 문장 목록을 넣어 정보를 입력합니다. 이때 문장에서 띄어쓰기를 기준으로 토큰화하고 사전을 만드므로 미리 필요한 전처리를 진행해주어야 합니다.

```python
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

cvec = CountVectorizer(max_df=0.9, min_df=10)
cvec.fit(df['text_tag'])

token = cvec.get_feature_names_out()
print(token)

names = cvec.vocabulary_
print(names)
```

### TD-IDF 벡터화

`TD-IDF 벡터화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. TD-IDF 벡터는 sklearn모듈의 TfidVectorizer를 이용하여 간단하게 구현할 수 있습니다. 활용방법은 CountVectorizer와 동일합니다. sklearn.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfvec = TfidfVectorizer(max_df=0.9, min_df=10)
tfvec.fit(df['text_tag'])

tokens = tfvec.get_feature_names_out()
print(tokens)

names = tfvec.vocabulary_
print(names)
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-1 ai5_벡터화_한글폰트이슈.md`
- Source formats: `md`
- Companion files: `3-1 ai5_벡터화_한글폰트이슈.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `scikit-learn.org`, `drive.google.com`, `localhost`

## Note Preview

> 백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다.
> - 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움
