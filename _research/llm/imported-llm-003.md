---
title: "데이터전처리"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)데이터전처리"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)데이터전처리.md"
excerpt: "텍스트 전처리 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 텍스트 전처리 순서로 핵심 장면을 먼저 훑고, 텍스트 정제(클리닝), 전체 데이터에 클렌징 적용, 텍스트 파일로부터 토큰 사전 및 sen... 같은 코드로 실제 구현을..."
research_summary: "텍스트 전처리 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 텍스트 전처리 순서로 핵심 장면을 먼저 훑고, 텍스트 정제(클리닝), 전체 데이터에 클렌징 적용, 텍스트 파일로부터 토큰 사전 및 sen... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 19개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, re, sentencepiece입니다."
research_artifacts: "md · 코드 19개 · 실행 16개"
code_block_count: 19
execution_block_count: 16
research_focus:
  - "텍스트 전처리"
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

텍스트 전처리 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 텍스트 전처리 순서로 핵심 장면을 먼저 훑고, 텍스트 정제(클리닝), 전체 데이터에 클렌징 적용, 텍스트 파일로부터 토큰 사전 및 sen... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 19개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, re, sentencepiece입니다.

**빠르게 볼 수 있는 포인트**: 텍스트 전처리.

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

### 텍스트 전처리

텍스트 정제(클리닝), (추가) 바이트페어 변환 > 텍스트..., (추가) 바이트페어 변환 > sen... 같은 코드를 직접 따라가며 텍스트 전처리 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 텍스트 정제(클리닝), (추가) 바이트페어 변환 > 텍스트 파일로부터 토큰 사전 및 sentencepiece 모델 작성, (추가) 바이트페어 변환 > sentencepiece 모델을 활용하여 토큰화

#### 텍스트 정제(클리닝)

기본적인 토큰화 결과 특수문자나 의미없는 단어들 또한 하나의 토큰으로 분리 되었습니다. 이러한 불필요한 토큰은 텍스트 분석에 있어 방해 요소가 됩니다. 따라서 의미 없는 기호, 단어를 제거하는 작업을 먼저 진행하는 클렌징 작업이 필요합니다.

#### (추가) 바이트페어 변환 > 텍스트 파일로부터 토큰 사전 및 sentencepiece 모델 작성

SentencePieceTrainer train() * input: 텍스트 뭉치 파일 경로 * model_prefix: 출력 모델 파일 경로 * vocab_size: 찾아낼 총 토큰 개수(가지고 있는 텍스트 양에 따라 결정)

#### (추가) 바이트페어 변환 > sentencepiece 모델을 활용하여 토큰화

sentencepiece 모델이 만들어진 후, SentencePieceProcessor 객체를 통해 생성된 모델을 다시 프로그램에 로드합니다. 이후 encode() 함수를 사용하여 토큰화 합니다 * 0번 토큰은 학습되지 않은 토큰으로 설정 spm를 활용한 바이트페어 토큰화 결과중...

## Why This Matters

### LLM 실험 구조화

- 왜 필요한가: LLM 실습은 프롬프트 한 줄보다 검색, 컨텍스트, 모델 호출 순서를 함께 봐야 실제 동작을 이해할 수 있습니다.
- 왜 이 방식을 쓰는가: 그래서 이 기록은 체인 구성과 보조 코드까지 함께 남겨, 단순 결과보다 시스템 흐름을 읽을 수 있게 만들었습니다.
- 원리: 입력 가공, 컨텍스트 주입, 모델 호출, 출력 후처리가 연결되면서 하나의 응답 파이프라인이 만들어집니다.

## Implementation Flow

1. 텍스트 전처리: 텍스트 정제(클리닝), (추가) 바이트페어 변환 > 텍스트 파일로부터 토큰 사전 및 sentencepiece 모델 작성

## Code Highlights

### 텍스트 정제(클리닝)

`텍스트 정제(클리닝)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 따라서 의미 없는 기호, 단어를 제거하는 작업을 먼저 진행하는 클렌징 작업이 필요합니다.

```python
text = df.loc[4, 'text']
text
```

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

### 특수 토큰을 추가

`특수 토큰을 추가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. bos_id:문장의 시작을 알리는 토큰 번호 eos_id:문장의 끝을 알리느 토큰 번호 unk_id:학습되지 않은 토큰 번호 pad_id: 패딩 토큰 번호(무시 토큰).

```python
spm.SentencePieceTrainer.train(input='nreview_mask.txt',      # 텍스트 뭉치 파일
                            model_prefix='./model/spm',       # 출력 모델 파일 이름
                            vocab_size=4000,                  # 토큰 개수
                            bos_id=1,
                            eos_id=2,
                            unk_id=1,
                            pad_id=0
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
