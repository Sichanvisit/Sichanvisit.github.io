---
title: "텍스트벡터화"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)텍스트벡터화"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)텍스트벡터화.md"
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
| Code Blocks | 25 |
| Execution Cells | 25 |
| Libraries | `google`, `pandas`, `sklearn`, `numpy`, `matplotlib`, `shutil`, `gensim` |
| Source Note | `3-1(실습)텍스트벡터화` |

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
6. 90% 이상으로 빈도가 많은 토큰을 제외

## Code Highlights

### Bag-of-Word(BoW) 빈도 벡터화

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
