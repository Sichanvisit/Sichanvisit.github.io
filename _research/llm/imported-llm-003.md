---
title: "데이터전처리"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)데이터전처리"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)데이터전처리.md"
excerpt: "사람이 텍스트를 이해 할 때는 문장 안의 단어를 보며 문장을 파악하고 이해를 합니다. 컴퓨터 또한 텍스트를 분석하기 위해서는 텍스트를 특정 의미 단위로 분할하여 문장을 파악할수 있게 합니다. 이러한 의미 단위을 토큰이라고 합니다. 기본적인 토큰화 결과 특수문자나 의미없는 단어들 또한 하나의 토큰으로..."
research_summary: "사람이 텍스트를 이해 할 때는 문장 안의 단어를 보며 문장을 파악하고 이해를 합니다. 컴퓨터 또한 텍스트를 분석하기 위해서는 텍스트를 특정 의미 단위로 분할하여 문장을 파악할수 있게 합니다. 이러한 의미 단위을 토큰이라고 합니다. 기본적인 토큰화 결과 특수문자나 의미없는 단어들 또한 하나의 토큰으로 분리 되었습니다. 이러한 불필요한 토큰은 텍스트 분석에 있어 방해 요소가 됩니다. 따라서 의미 없는 기호, 단어를 제거하는 작업을 먼저 진행하는 클렌징 작업이 필요합니다. `md` 원본과 19개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, re, sentencepiece입니다."
research_artifacts: "md · 코드 19개 · 실행 16개"
code_block_count: 19
execution_block_count: 16
research_focus:
  - "텍스트 전처리"
  - "토큰화"
  - "텍스트 정제(Cleaning)"
research_stack:
  - "google"
  - "pandas"
  - "re"
  - "sentencepiece"
  - "os"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

사람이 텍스트를 이해 할 때는 문장 안의 단어를 보며 문장을 파악하고 이해를 합니다. 컴퓨터 또한 텍스트를 분석하기 위해서는 텍스트를 특정 의미 단위로 분할하여 문장을 파악할수 있게 합니다. 이러한 의미 단위을 토큰이라고 합니다. 기본적인 토큰화 결과 특수문자나 의미없는 단어들 또한 하나의 토큰으로 분리 되었습니다. 이러한 불필요한 토큰은 텍스트 분석에 있어 방해 요소가 됩니다. 따라서 의미 없는 기호, 단어를 제거하는 작업을 먼저 진행하는 클렌징 작업이 필요합니다. `md` 원본과 19개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, re, sentencepiece입니다.

**빠르게 볼 수 있는 포인트**: 텍스트 전처리, 토큰화, 텍스트 정제(Cleaning).

**남겨둔 자료**: `md` 원본과 19개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, re, sentencepiece입니다.

**주요 스택**: `google`, `pandas`, `re`, `sentencepiece`, `os`

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

## What This Note Covers

### 텍스트 전처리 > 토큰화

사람이 텍스트를 이해 할 때는 문장 안의 단어를 보며 문장을 파악하고 이해를 합니다. 컴퓨터 또한 텍스트를 분석하기 위해서는 텍스트를 특정 의미 단위로 분할하여 문장을 파악할수 있게 합니다. 이러한 의미 단위을 토큰이라고 합니다.

### 토큰화 > 문자로 토큰화

토큰화 방식중 가장 간단하게 접근하는 방식은 띄어쓰기를 기준으로 단어를 구분 하는 것입니다. 파이썬에서는 split() 함수를 이용하면 쉽게 토큰화가 가능합니다.

### 토큰화 > 숫자 인코딩 --> 벡터화

토큰화 이후 컴퓨터가 이를 분석 하기 위해선 문자로 나타나는 토큰을 벡터형태의 데이터로 바꾸어 주어야 합니다. 토큰을 여러 숫자의 조합인 벡터로 최종 변환하기 이전에 토큰에 고유한 숫자를 부여하여 인코딩 과정을 선행 해주어야 합니다. *토큰화 => 숫자 인코딩 => 백터화* 인코딩: 문자 토큰을 숫자 토큰으로 변환 - 디코딩: 숫자 토큰을 문자 토큰으로 변환

### 텍스트 전처리 > 텍스트 정제(클리닝)

기본적인 토큰화 결과 특수문자나 의미없는 단어들 또한 하나의 토큰으로 분리 되었습니다. 이러한 불필요한 토큰은 텍스트 분석에 있어 방해 요소가 됩니다. 따라서 의미 없는 기호, 단어를 제거하는 작업을 먼저 진행하는 클렌징 작업이 필요합니다.

## Why This Matters

### LLM 실험 구조화

- 왜 필요한가: LLM 실습은 프롬프트 한 줄보다 검색, 컨텍스트, 모델 호출 순서를 함께 봐야 실제 동작을 이해할 수 있습니다.
- 왜 이 방식을 쓰는가: 그래서 이 기록은 체인 구성과 보조 코드까지 함께 남겨, 단순 결과보다 시스템 흐름을 읽을 수 있게 만들었습니다.
- 원리: 입력 가공, 컨텍스트 주입, 모델 호출, 출력 후처리가 연결되면서 하나의 응답 파이프라인이 만들어집니다.

## Implementation Flow

1. 텍스트 전처리 > 토큰화: 사람이 텍스트를 이해 할 때는 문장 안의 단어를 보며 문장을 파악하고 이해를 합니다. 컴퓨터 또한 텍스트를 분석하기 위해서는 텍스트를 특정 의미 단위로 분할하여 문장을 파악할수 있게 합니다. 이러한 의미 단위을 토큰이라고 합니다.
2. 토큰화 > 문자로 토큰화: 토큰화 방식중 가장 간단하게 접근하는 방식은 띄어쓰기를 기준으로 단어를 구분 하는 것입니다. 파이썬에서는 split() 함수를 이용하면 쉽게 토큰화가 가능합니다.
3. 토큰화 > 숫자 인코딩 --> 벡터화: 토큰화 이후 컴퓨터가 이를 분석 하기 위해선 문자로 나타나는 토큰을 벡터형태의 데이터로 바꾸어 주어야 합니다. 토큰을 여러 숫자의 조합인 벡터로 최종 변환하기 이전에 토큰에 고유한 숫자를 부여하여 인코딩 과정을 선행 해주어야 합니다. *토큰화 => 숫자 인코딩...
4. 텍스트 전처리 > 텍스트 정제(클리닝): 기본적인 토큰화 결과 특수문자나 의미없는 단어들 또한 하나의 토큰으로 분리 되었습니다. 이러한 불필요한 토큰은 텍스트 분석에 있어 방해 요소가 됩니다. 따라서 의미 없는 기호, 단어를 제거하는 작업을 먼저 진행하는 클렌징 작업이 필요합니다.

## Code Highlights

### 전체 데이터에 클렌징 적용

`전체 데이터에 클렌징 적용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 불용어 제거, 한글자 제거, 클렌징 함수 적용 흐름이 주석과 함께 드러납니다.

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

`텍스트 뭉치 데이터를 텍스트 파일로 생성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 추가 쓰기모드로 텍스트 파일 열기 흐름이 주석과 함께 드러납니다.

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

### 텍스트 파일로부터 토큰 사전 및 sentencepiece 모델 작성

`텍스트 파일로부터 토큰 사전 및 sentencepiece 모델 작성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 저장 경로 생성 흐름이 주석과 함께 드러납니다.

```python
import os

# 저장 경로 생성
os.makedirs('./model', exist_ok=True)

spm.SentencePieceTrainer.train(
    input='nreview_mask.txt',       # 텍스트 뭉치 파일
    model_prefix='./model/spm',     # 출력 모델 파일 이름
    vocab_size=2000                 # 토큰 개수
)
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
