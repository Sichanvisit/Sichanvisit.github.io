---
title: "텍스트벡터화"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)텍스트벡터화"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)텍스트벡터화.md"
excerpt: "백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다. BoW, TF-IDF에서는 단어의 순서, 주변단어 등 문맥에 대한 정보가 제대로 반영되지 않습니다. 즉 단어의 문백적인 의미를 파악할 수 없다는 문제가 존재합니다. 임베딩 기법은 단어를 저차원 벡터 공간에 매핑하여 단어간 의미적 유사도를 학습하여..."
research_summary: "백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다. BoW, TF-IDF에서는 단어의 순서, 주변단어 등 문맥에 대한 정보가 제대로 반영되지 않습니다. 즉 단어의 문백적인 의미를 파악할 수 없다는 문제가 존재합니다. 임베딩 기법은 단어를 저차원 벡터 공간에 매핑하여 단어간 의미적 유사도를 학습하여 벡터의 값을 설정합니다. - 단어 간의 의미 관계 학습: 의미가 유사하거나 관련이 있는... `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다."
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

백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다. BoW, TF-IDF에서는 단어의 순서, 주변단어 등 문맥에 대한 정보가 제대로 반영되지 않습니다. 즉 단어의 문백적인 의미를 파악할 수 없다는 문제가 존재합니다. 임베딩 기법은 단어를 저차원 벡터 공간에 매핑하여 단어간 의미적 유사도를 학습하여 벡터의 값을 설정합니다. - 단어 간의 의미 관계 학습: 의미가 유사하거나 관련이 있는... `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다.

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

### 텍스트 벡터화 > Bag-of-Word(BoW)

단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움

### 텍스트 벡터화 > TD-IDF(Term Frequency-Inverse Document Frequency)

단어 빈도(TF)와 전체 문서에서의 희소성(IDF)을 결합하여 단어의 중요도 측정 - 비교적 BoW보다 문서내에서의 의미 있는 단어 식별

### 텍스트 벡터화 > Word Embedding

Word2Vec, Glove등 각 단어를 저차원 벡터로 표현 - 단어간의 의미적 유사성을 벡터 공간에서 반영

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

## Implementation Flow

1. 텍스트 벡터화: 백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다.
2. 텍스트 벡터화 > Bag-of-Word(BoW): 단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움
3. 텍스트 벡터화 > TD-IDF(Term Frequency-Inverse Document Frequency): 단어 빈도(TF)와 전체 문서에서의 희소성(IDF)을 결합하여 단어의 중요도 측정 - 비교적 BoW보다 문서내에서의 의미 있는 단어 식별
4. 텍스트 벡터화 > Word Embedding: Word2Vec, Glove등 각 단어를 저차원 벡터로 표현 - 단어간의 의미적 유사성을 벡터 공간에서 반영

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

### 산점도 시각화

`산점도 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 설치된 나눔고딕 폰트를 불러와 Matplotlib의 기본 폰트로 설정, 음수 부호 사용, 산점도 그리기 흐름이 주석과 함께 드러납니다.

```python
import matplotlib.pyplot as plt

# 설치된 나눔고딕 폰트를 불러와 Matplotlib의 기본 폰트로 설정
plt.rc('font', family='NanumBarunGothic')
# 음수 부호 사용
plt.rcParams['axes.unicode_minus'] = False

# 산점도 그리기
plt.figure(figsize=(10, 8))

for i, word in enumerate(words):
    plt.scatter(reduced_vectors[i, 0], reduced_vectors[i, 1])
    plt.annotate(word, (reduced_vectors[i, 0] + 0.02, reduced_vectors[i, 1] + 0.02))

plt.title(f"Word2Vec Similarity: {keyword}")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.grid(True)
plt.show()
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
