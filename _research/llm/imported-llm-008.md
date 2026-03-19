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
