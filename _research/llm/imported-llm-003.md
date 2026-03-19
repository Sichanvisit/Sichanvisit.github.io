---
title: "데이터전처리"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)데이터전처리"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)데이터전처리.md"
excerpt: "사람이 텍스트를 이해 할 때는 문장 안의 단어를 보며 문장을 파악하고 이해를 합니다. 컴퓨터 또한 텍스트를 분석하기 위해서는 텍스트를 특정 의미 단위로 분할하여 문장을 파악할수 있게 합니다. 이러한 의미 단위을 토큰이라고 합니다."
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
| Code Blocks | 19 |
| Execution Cells | 16 |
| Libraries | `google`, `pandas`, `re`, `sentencepiece`, `os` |
| Source Note | `3-1(실습)데이터전처리` |

## What I Worked On

- 텍스트 전처리
- 1. 토큰화
- 2. 텍스트 정제(Cleaning)
- 3. 형태소 분석 및 품사 태깅
- 4. 바이트페어 변환

## Implementation Flow

1. 텍스트 전처리
2. 1. 토큰화
3. 2. 텍스트 정제(Cleaning)
4. 3. 형태소 분석 및 품사 태깅
5. 4. 바이트페어 변환
6. 문자로 토큰화

## Code Highlights

### 전체 데이터에 클렌징 적용

```python
import re

stopwords = ['', '진짜','않지만']

def cleaning(review):
  review = re.sub(r'[^\w\s]', '', review)       # 특수문자 제거
  review = re.sub(r'[\n\t]', ' ', review)       # 줄바꿈, 탭 제거
  review = re.sub(r'\s+', ' ', review)          # 연속된 공백 제거
  review= review.strip()                        # 문장 양끝 공백 제거

  # 불용어 제거
  review = ' '.join([w for w in review.split(' ') if w not in stopwords])
  # 한글자 제거
  review = ' '.join([w for w in review.split(' ') if len(w) > 1])

  return review

# 클렌징 함수 적용
df['clean'] = df['text'].apply(cleaning)
df[['text', 'clean']]
```

### 텍스트 뭉치 데이터를 텍스트 파일로 생성

```python
import sentencepiece as spm
import pandas as pd
import re

df = pd.read_csv("nreview_mask.csv")

# 추가 쓰기모드로 텍스트 파일 열기
with open('nreview_mask.txt', 'a', encoding='utf-8') as f:
  for text in df['text']:
        text = str(text)
        text = re.sub(r'[^\w\s]', '', text)  # 특수문자 제거
        text = re.sub(r'[\n\t]', ' ', text)  # 줄바꿈, 탭 제거
        text = re.sub(r'\s+', ' ', text)  # 연속된 공백 제거
        text= text.strip() # 문장 양끝 공백 제거
        try:
            f.write(text+'\n')
        except:
                pass
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-1(실습)데이터전처리.md`
- Source formats: `md`
- Companion files: `3-1(실습)데이터전처리.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `text'', ''clean`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `github.com`, `localhost`

## Note Preview

> 사람이 텍스트를 이해 할 때는 문장 안의 단어를 보며 문장을 파악하고 이해를 합니다. 컴퓨터 또한 텍스트를 분석하기 위해서는 텍스트를 특정 의미 단위로 분할하여 문장을 파악할수 있게 합니다. 이러한 의미 단위을 토큰이라고 합니다.
> 토큰화 방식중 가장 간단하게 접근하는 방식은 띄어쓰기를 기준으로 단어를 구분 하는 것입니다. 파이썬에서는 split() 함수를 이용하면 쉽게 토큰화가 가능합니다.
