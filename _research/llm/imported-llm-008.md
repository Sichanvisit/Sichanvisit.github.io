---
title: "seq2seq 1"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)seq2seq_1"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)seq2seq_1.md"
excerpt: "* torch: 딥러닝 프레임워크 * torchtext: 텍스트 처리를 위한 라이브러리 * spacy: 영어 토큰화 * konlpy: 한국어 토큰화 (Okt 사용)"
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
| Code Blocks | 18 |
| Execution Cells | 6 |
| Libraries | `torch`, `torchtext`, `spacy`, `konlpy`, `random`, `math`, `time`, `io` |
| Source Note | `3-2 (실습)seq2seq_1` |

## What I Worked On

- Seq2Seq 실습 1: 영어-한국어 번역
- 1. 환경 설정 및 라이브러리 설치
- Colab 셀 1: 라이브러리 설치
- torch 및 torchtext의 호환되는 버전을 명시하여 설치
- !pip uninstall -y torch torchtext torchvision torchaudio

## Implementation Flow

1. Seq2Seq 실습 1: 영어-한국어 번역
2. 1. 환경 설정 및 라이브러리 설치
3. Colab 셀 1: 라이브러리 설치
4. torch 및 torchtext의 호환되는 버전을 명시하여 설치
5. !pip uninstall -y torch torchtext torchvision torchaudio
6. konlpy 사용을 위한 자바 설치

## Code Highlights

### 6. Dataset 및 DataLoader 정의

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

### 8.3. 실제 학습 실행 : 약 2분 시간 걸림

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
