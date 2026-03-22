---
title: "ai5 벡터화 한글폰트이슈"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1 ai5_벡터화_한글폰트이슈"
source_path: "13_LLM_GenAI/Code_Snippets/3-1 ai5_벡터화_한글폰트이슈.md"
excerpt: "ai5 벡터화 한글폰트이슈에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 텍스트 임베딩, 텍스트 벡터화 순서로 핵심 장면을 먼저 훑고, Bag-of-Word(BoW) 빈도 벡터화, Word2Vec 단어 임베딩, Word2Vec 학습하기 같은 코드로..."
research_summary: "ai5 벡터화 한글폰트이슈에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 텍스트 임베딩, 텍스트 벡터화 순서로 핵심 장면을 먼저 훑고, Bag-of-Word(BoW) 빈도 벡터화, Word2Vec 단어 임베딩, Word2Vec 학습하기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 28개 코드 블록, 23개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다."
research_artifacts: "md · 코드 28개 · 실행 23개"
code_block_count: 28
execution_block_count: 23
research_focus:
  - "텍스트 임베딩"
  - "텍스트 벡터화"
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

ai5 벡터화 한글폰트이슈에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 텍스트 임베딩, 텍스트 벡터화 순서로 핵심 장면을 먼저 훑고, Bag-of-Word(BoW) 빈도 벡터화, Word2Vec 단어 임베딩, Word2Vec 학습하기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 28개 코드 블록, 23개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, sklearn, numpy입니다.

**빠르게 볼 수 있는 포인트**: 텍스트 임베딩, 텍스트 벡터화.

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

### 텍스트 임베딩

BoW, TF-IDF에서는 단어의 순서, 주변단어 등 문맥에 대한 정보가 제대로 반영되지 않습니다. 즉 단어의 문백적인 의미를 파악할 수 없다는 문제가 존재합니다. 임베딩 기법은 단어를 저차원 벡터 공간에 매핑하여 단어간 의미적 유사도를 학습하여 벡터의 값을 설정합니다. - 단어 간의 의미 관계 학습: 의미가 유사하거나 관련이 있는...

- 읽을 포인트: 세부 흐름: Word2Vec 단어 임베딩, Word2Vec 단어 임베딩 > Word2Vec 학습하기, FastText, Glove 단어 임베딩 > FastText 학습하기

#### Word2Vec 단어 임베딩

Word2Vec모델은 키워드 간의 유사도를 학습하여 단어 임베딩을 만드는 대표적인 모델입니다. gensim라이브러리를 활용하여 Word2Vec모델을 구성하고 학습합니다

#### Word2Vec 단어 임베딩 > Word2Vec 학습하기

Word2Vec는 같이 자주 등장하는 단어들을 학습하기 위해 중심단어에서 설정한 윈도우 크기안에 들어오는 단어를 주변단어로 설정하여 학습합니다. *윈도우 예시*

#### FastText, Glove 단어 임베딩 > FastText 학습하기

FastText는 단어를 n그램의 서브워드로 쪼개므로 최소 n과 최대 n을 설정해야 합니다. 최소n: 3 최대n: 5

### 텍스트 벡터화

백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다.

- 읽을 포인트: 세부 흐름: Bag-of-Word(BoW), Word Embedding, Bag-of-Word(BoW) 빈도 벡터화

#### Bag-of-Word(BoW)

단어의 출현 여부나 횟수만을 기준으로 텍스트를 벡터화함 - 문맥 정보를 반영하기 어려움

#### Word Embedding

Word2Vec, Glove등 각 단어를 저차원 벡터로 표현 - 단어간의 의미적 유사성을 벡터 공간에서 반영

#### Bag-of-Word(BoW) 빈도 벡터화

빈도벡터화는 텍스트에서 출현한 토큰의 빈도로 벡터를 표현하는 간단한 벡터화 방식입니다 빈도 벡터화는 sklearn의 CountVectorizer를 이용하여 구현합니다 - max_df: 해당 확률 이상으로 빈도가 많은 토큰을 제외 - min_df: 해당 확률 이하로 빈도가 적은 토큰...

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

## Implementation Flow

1. 텍스트 임베딩: Word2Vec 단어 임베딩, Word2Vec 단어 임베딩 > Word2Vec 학습하기
2. 텍스트 벡터화: Bag-of-Word(BoW), Word Embedding

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

### Word2Vec 단어 임베딩

`Word2Vec 단어 임베딩`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 pip install "scipy<1.13" "gensim==4.3.3" 흐름이 주석과 함께 드러납니다.

```python
#pip install "scipy<1.13" "gensim==4.3.3"
!pip install scipy gensim
```

### Word2Vec 학습하기

`Word2Vec 학습하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 임베딩 벡터 사이즈는 클수록 많은 정보를 담지만 토큰의 개수와 텍스트양에 따라 적절한 값을 설정.

```python
keywords = model.wv.index_to_key
keywords[:10]
```

### FastText 학습하기

`FastText 학습하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 FastText 학습 흐름이 주석과 함께 드러납니다.

```python
from gensim.models import FastText

# FastText 학습
fasttext_model = FastText(
    sentences,    # 학습 문장 세트
    vector_size=100,  # 임베딩 벡터 사이즈
    window=5,         # 윈도우 크기
    min_count=2,      # 최소 빈도
    min_n=2,          # n-gram 으로 쪼개질때 최소 글자(최소n)
    max_n=6,          # n-gram 으로 쪼개질때 최대 글자(최대n)
    workers=4,        # 사용 코어 개수
    sg=1,             # 1: Skip-gram, 0: CBOW
    epochs=50         # 전체 학습 반복 횟수
)
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
