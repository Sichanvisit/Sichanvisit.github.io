---
title: "ai5 벡터화 한글폰트이슈"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1 ai5_벡터화_한글폰트이슈"
source_path: "13_LLM_GenAI/Code_Snippets/3-1 ai5_벡터화_한글폰트이슈.md"
excerpt: "백터화는 기본적으로 토큰화와 인코딩 이후 진행됩니다."
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
| Source Files | `md` |
| Code Blocks | 28 |
| Execution Cells | 23 |
| Libraries | `google`, `pandas`, `sklearn`, `numpy`, `matplotlib`, `shutil`, `gensim` |
| Source Note | `3-1 ai5_벡터화_한글폰트이슈` |

## What I Worked On

- 텍스트 벡터화
- 1. Bag-of-Word(BoW)
- 2. TD-IDF(Term Frequency-Inverse Document Frequency)
- 3. Word Embedding
- Bag-of-Word(BoW) 빈도 벡터화

## Implementation Flow

1. 텍스트 벡터화
2. 1. Bag-of-Word(BoW)
3. 2. TD-IDF(Term Frequency-Inverse Document Frequency)
4. 3. Word Embedding
5. Bag-of-Word(BoW) 빈도 벡터화
6. TD-IDF 벡터화

## Code Highlights

### Bag-of-Word(BoW) 빈도 벡터화

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
