---
title: "seq2seq 1"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)seq2seq_1"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)seq2seq_1.md"
excerpt: "* torch: 딥러닝 프레임워크 * torchtext: 텍스트 처리를 위한 라이브러리 * spacy: 영어 토큰화 * konlpy: 한국어 토큰화 (Okt 사용)"
research_summary: "* torch: 딥러닝 프레임워크 * torchtext: 텍스트 처리를 위한 라이브러리 * spacy: 영어 토큰화 * konlpy: 한국어 토큰화 (Okt 사용). Tatoeba 프로젝트의 소규모 영-한 병렬 코퍼스를 사용. `md` 원본과 18개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchtext, spacy, konlpy입니다."
research_artifacts: "md · 코드 18개 · 실행 6개"
code_block_count: 18
execution_block_count: 6
research_focus:
  - "Seq2Seq 실습 1"
  - "* torch"
  - "환경 설정 및 라이브러리 설치"
research_stack:
  - "torch"
  - "torchtext"
  - "spacy"
  - "konlpy"
  - "random"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

* torch: 딥러닝 프레임워크 * torchtext: 텍스트 처리를 위한 라이브러리 * spacy: 영어 토큰화 * konlpy: 한국어 토큰화 (Okt 사용). Tatoeba 프로젝트의 소규모 영-한 병렬 코퍼스를 사용. `md` 원본과 18개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchtext, spacy, konlpy입니다.

**빠르게 볼 수 있는 포인트**: Seq2Seq 실습 1, * torch, 환경 설정 및 라이브러리 설치.

**남겨둔 자료**: `md` 원본과 18개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchtext, spacy, konlpy입니다.

**주요 스택**: `torch`, `torchtext`, `spacy`, `konlpy`, `random`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 18 |
| Execution Cells | 6 |
| Libraries | `torch`, `torchtext`, `spacy`, `konlpy`, `random`, `math`, `time`, `io` |
| Source Note | `3-2 (실습)seq2seq_1` |

## What This Note Covers

### 환경 설정 및 라이브러리 설치

* torch: 딥러닝 프레임워크 * torchtext: 텍스트 처리를 위한 라이브러리 * spacy: 영어 토큰화 * konlpy: 한국어 토큰화 (Okt 사용)

### 데이터 다운로드 및 전처리

Tatoeba 프로젝트의 소규모 영-한 병렬 코퍼스를 사용

### 토크나이저 정의

영어는 spaCy, 한국어는 Okt를 사용해 토크나이저를 정의

### 데이터 로드 및 어휘장(Vocabulary) 구축

다운로드한 kor.txt 파일(탭으로 구분)을 읽고, 영어와 한국어 어휘장을 만듦

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 순차 데이터 모델링

- 왜 필요한가: 문장, 시계열처럼 순서가 중요한 데이터는 현재 입력만이 아니라 앞선 맥락까지 함께 봐야 합니다.
- 왜 이 방식을 쓰는가: LSTM/GRU는 기본 RNN보다 긴 문맥을 더 안정적으로 다룰 수 있어 텍스트 분류나 시계열 예측 실습에 자주 쓰입니다.
- 원리: 이전 시점의 은닉 상태를 다음 입력과 함께 업데이트하며, 게이트 구조로 필요한 정보는 남기고 불필요한 정보는 줄입니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. 환경 설정 및 라이브러리 설치: * torch: 딥러닝 프레임워크 * torchtext: 텍스트 처리를 위한 라이브러리 * spacy: 영어 토큰화 * konlpy: 한국어 토큰화 (Okt 사용)
2. 데이터 다운로드 및 전처리: Tatoeba 프로젝트의 소규모 영-한 병렬 코퍼스를 사용
3. 토크나이저 정의: 영어는 spaCy, 한국어는 Okt를 사용해 토크나이저를 정의
4. 데이터 로드 및 어휘장(Vocabulary) 구축: 다운로드한 kor.txt 파일(탭으로 구분)을 읽고, 영어와 한국어 어휘장을 만듦

## Code Highlights

### Dataset 및 DataLoader 정의

`Dataset 및 DataLoader 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Define device, Collate 함수 및 DataLoader 생성, 토큰화 흐름이 주석과 함께 드러납니다.

```python
import torch
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset, DataLoader

# Define device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")


# Collate 함수 및 DataLoader 생성
def collate_fn(batch):
  """
    PyTorch의 DataLoader는 여러 샘플을 묶어 **하나의 배치(batch)**로 만듭니다.
    하지만 NLP에서는 문장의 길이가 제각각이라 단순히 묶기 어렵습니다.
    collate_fn은 각 문장을 토큰화 → 인덱스 변환 → 패딩(padding) 해서 동일한 길이로 만들어주는 함수
  """
  src_batch, trg_batch = [], []
  for src_sample, trg_sample in batch:
      # 1. 토큰화
      src_tokens = [tok for tok in tokenize_en(src_sample.lower())]
      trg_tokens = [tok for tok in tokenize_ko(trg_sample)]

      # 2. <sos> 및 <eos> 추가
      src_with_eos = src_tokens + ['<eos>']
      trg_with_sos_eos = ['<sos>'] + trg_tokens + ['<eos>']

      # 3. 수치화 (Vocab 사용)
      src_indices = [vocab_en[token] for token in src_with_eos]
# ... trimmed ...
```

### 학습 및 평가 함수 정의

`학습 및 평가 함수 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 함수, 모델 순전파, teacher_forcing_ratio = 0.5 (50% 확률로 Teacher Forc... 흐름이 주석과 함께 드러납니다.

```python
# 학습 함수
def train(model, iterator, optimizer, criterion, clip):
    model.train() # 학습 모드
    epoch_loss = 0

    for i, (src, trg) in enumerate(iterator):
        optimizer.zero_grad()

        # 1. 모델 순전파
        # teacher_forcing_ratio = 0.5 (50% 확률로 Teacher Forcing 사용)
        output = model(src, trg, 0.5)

        # output: (trg_len, batch_size, output_dim)
        # trg: (trg_len, batch_size)

        output_dim = output.shape[-1]

        # 2. 손실 계산
        # CrossEntropyLoss는 (N, C) 형태의 2D 입력과 (N) 형태의 1D 타겟을 기대함
        # <sos> 토큰(인덱스 0)은 예측 대상이 아니므로 [1:] 부터 사용
        output = output[1:].view(-1, output_dim) # ( (trg_len-1) * batch_size, output_dim )
        trg = trg[1:].view(-1)                   # ( (trg_len-1) * batch_size )

        loss = criterion(output, trg)

        # 3. 역전파 및 가중치 업데이트
        loss.backward()

# ... trimmed ...
```

### 실제 학습 실행 : 약 2분 시간 걸림

`실제 학습 실행 : 약 2분 시간 걸림`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 실행, 시간 측정용, Validation loss가 가장 낮은 모델을 저장 흐름이 주석과 함께 드러납니다.

```python
import time
import math
import torch
import random

# 학습 실행
N_EPOCHS = 50
CLIP = 1
best_valid_loss = float('inf')

# 시간 측정용
def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs

for epoch in range(N_EPOCHS):
    start_time = time.time()

    train_loss = train(model, train_loader, optimizer, criterion, CLIP)
    valid_loss = evaluate(model, valid_loader, criterion)

    end_time = time.time()
    epoch_mins, epoch_secs = epoch_time(start_time, end_time)

    # Validation loss가 가장 낮은 모델을 저장
    if valid_loss < best_valid_loss:
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-2 (실습)seq2seq_1.md`
- Source formats: `md`
- Companion files: `3-2 (실습)seq2seq_1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `미션`
- External references: `www.manythings.org`, `localhost`

## Note Preview

> * torch: 딥러닝 프레임워크 * torchtext: 텍스트 처리를 위한 라이브러리 * spacy: 영어 토큰화 * konlpy: 한국어 토큰화 (Okt 사용)
> Tatoeba 프로젝트의 소규모 영-한 병렬 코퍼스를 사용
