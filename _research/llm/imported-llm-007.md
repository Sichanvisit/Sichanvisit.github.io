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

## Implementation Flow

1. Overview: Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가
2. 감정 분류을 위한 Attention 순환 신경망: BiLSTM + Attention: 기존 Embedding + BiLSTM 모델 아키텍처에 Bahdanau Attention(Additive)을 추가
3. 단계: 모델 정의: BiLSTMWithAttention 클래스를 만듭니다.
4. 모델링: 임베딩 레이어 사용 - 토큰의 정수 인덱스로 부터 Embedding 레이어를 통 정수를 해당하는 임베딩 벡터로 매핑

## Code Highlights

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
