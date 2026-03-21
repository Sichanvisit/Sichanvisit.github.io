---
title: "Attention 1"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)Attention_1"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)Attention_1.md"
excerpt: "Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가"
research_summary: "Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가. 기존 Embedding + BiLSTM 모델 아키텍처에 Bahdanau Attention(Additive)을 추가. `md` 원본과 14개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, google, pandas, numpy입니다."
research_artifacts: "md · 코드 14개 · 실행 12개"
code_block_count: 14
execution_block_count: 12
research_focus:
  - "Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가"
  - "기존 Embedding + BiLSTM 모델 아키텍처에 Bahdanau Attention(Additiv..."
  - "감정 분류을 위한 Attention 순환 신경망: BiLSTM + At..."
research_stack:
  - "torch"
  - "google"
  - "pandas"
  - "numpy"
  - "sentencepiece"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가. 기존 Embedding + BiLSTM 모델 아키텍처에 Bahdanau Attention(Additive)을 추가. `md` 원본과 14개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, google, pandas, numpy입니다.

**빠르게 볼 수 있는 포인트**: Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하..., 기존 Embedding + BiLSTM 모델 아키텍처에 Bahdanau..., 감정 분류을 위한 Attention 순환 신경망: BiLSTM + At....

**남겨둔 자료**: `md` 원본과 14개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, google, pandas, numpy입니다.

**주요 스택**: `torch`, `google`, `pandas`, `numpy`, `sentencepiece`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 14 |
| Execution Cells | 12 |
| Libraries | `torch`, `google`, `pandas`, `numpy`, `sentencepiece`, `os`, `math` |
| Source Note | `3-2 (실습)Attention_1` |

## What This Note Covers

### Overview

Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가

### 감정 분류을 위한 Attention 순환 신경망: BiLSTM + Attention

기존 Embedding + BiLSTM 모델 아키텍처에 Bahdanau Attention(Additive)을 추가

### 단계

모델 정의: BiLSTMWithAttention 클래스를 만듭니다.

### 모델링

임베딩 레이어 사용 - 토큰의 정수 인덱스로 부터 Embedding 레이어를 통 정수를 해당하는 임베딩 벡터로 매핑

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

1. Overview: Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가
2. 감정 분류을 위한 Attention 순환 신경망: BiLSTM + Attention: 기존 Embedding + BiLSTM 모델 아키텍처에 Bahdanau Attention(Additive)을 추가
3. 단계: 모델 정의: BiLSTMWithAttention 클래스를 만듭니다.
4. 모델링: 임베딩 레이어 사용 - 토큰의 정수 인덱스로 부터 Embedding 레이어를 통 정수를 해당하는 임베딩 벡터로 매핑

## Code Highlights

### SentencePiece 토크나이저를 이용해서 만든 PyTorch Dataset 클래스

`SentencePiece 토크나이저를 이용해서 만든 PyTorch Dataset 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 배열을 활용하여 최적화된 패딩함수 구축, 라벨 인코딩, 문장 인코딩 (앞뒤오 시작토큰과 끝 토큰을 붙임) 흐름이 주석과 함께 드러납니다.

```python
from torch.utils.data import Dataset
import pandas as pd
import numpy as np
import sentencepiece as spm
import torch
import torch.nn as nn


class SPDataSet(Dataset):
  """
  SentencePiece 토크나이저를 이용해서 만든 PyTorch Dataset 클래스
  모델이 학습할 수 있는 형태로 **문장(text)과 라벨(label)**을 숫자 텐서로 변환하는 역할
  """
  def __init__(self, df, sp, max_len):
    self.max_len = max_len
    self.df = df
    self.sp = sp
    self.class_name = {'E1':0, 'E6':1, 'E3':2, 'E5':3, 'E2':4, 'E4':5}

  # 배열을 활용하여 최적화된 패딩함수 구축
  def zero_pad(self, tok):
    if len(tok) >= self.max_len:
      return tok[:self.max_len]
    else:
      padding = np.zeros(self.max_len)
      padding[:len(tok)] = tok
      return padding

# ... trimmed ...
```

### 모델 학습(train) + 평가(validation) 단계

`모델 학습(train) + 평가(validation) 단계`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 입력데이터 준비, 순전파, 역전파 및 옵티마아지 업데이트 흐름이 주석과 함께 드러납니다.

```python
criterion = nn.CrossEntropyLoss() # 다중 클래스 분류
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

history = {'train_loss': [],
           'val_loss': [],
           'val_acc': []
           }

for epoch in range(num_epochs):
  model.train() # 모델을 학습모드로 설정
  total_loss = 0.0

  for input, labels in train_loader:
    # 입력데이터 준비
    input_ids = input.long().to(device) # [batch_size, seq_len]
    labels = labels.to(device)
    # 순전파
    outputs = model(input_ids)          # [batch_size, num_calsses]
    loss = criterion(outputs, labels)   # 손실 계산

    # 역전파 및 옵티마아지 업데이트
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    total_loss += loss.item()

  avg_loss = total_loss / len(train_loader)
# ... trimmed ...
```

### 디코더 구성

`디코더 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 제로 패딩, 질의는 단어 토큰만 활용, 응답에는 시작 토큰과 끝 토큰을 추가하여 문장의 시작과 끝을 알림 흐름이 주석과 함께 드러납니다.

```python
from torch.utils.data import Dataset, DataLoader, random_split
import sentencepiece as spm
import numpy as np

class SPDataSet(Dataset):
    def __init__(self, sp, max_len):
        self.max_len = max_len
        self.df = pd.read_csv(f'train.csv')[['HS01','SS01']]
        self.sp = sp

    # 제로 패딩
    def zero_pad(self, tok):
        if len(tok) >= self.max_len:
            return tok[:self.max_len]
        else:
            padding = np.zeros(self.max_len)
            padding[:len(tok)] = tok
            return padding

    def __len__(self):
        return (len(self.df))

    def __getitem__(self, i):
        sent = self.df.iloc[i]
        sent1 = self.sp.encode_as_ids(sent['HS01'])
        sent2 = self.sp.encode_as_ids(sent['SS01'])

        # 질의는 단어 토큰만 활용
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-2 (실습)Attention_1.md`
- Source formats: `md`
- Companion files: `3-2 (실습)Attention_1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `label'',''HS01`, `HS01'', ''SS01`, `HS01'',''SS01`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `www.aihub.or.kr`, `drive.google.com`, `localhost`

## Note Preview

> Attention
> Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가
