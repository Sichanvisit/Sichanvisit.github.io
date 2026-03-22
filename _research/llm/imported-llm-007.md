---
title: "Attention 1"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)Attention_1"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)Attention_1.md"
excerpt: "Seq2seq + Attention..., 감정 분류을 위한 Attention... 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 Seq2seq + Attention..., 감정 분류을 위한 Attention... 순서로 핵심..."
research_summary: "Seq2seq + Attention..., 감정 분류을 위한 Attention... 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 Seq2seq + Attention..., 감정 분류을 위한 Attention... 순서로 핵심 장면을 먼저 훑고, 모델링, 모델 학습(train) + 평가(val..., 디코더 구성 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 14개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, google, pandas, numpy입니다."
research_artifacts: "md · 코드 14개 · 실행 12개"
code_block_count: 14
execution_block_count: 12
research_focus:
  - "Seq2seq + Attention (질의응답 챗봇)"
  - "감정 분류을 위한 Attention 순환 신경망: BiLSTM + Attention"
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

Seq2seq + Attention..., 감정 분류을 위한 Attention... 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 Seq2seq + Attention..., 감정 분류을 위한 Attention... 순서로 핵심 장면을 먼저 훑고, 모델링, 모델 학습(train) + 평가(val..., 디코더 구성 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 14개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, google, pandas, numpy입니다.

**빠르게 볼 수 있는 포인트**: Seq2seq + Attention (질의응답 챗봇), 감정 분류을 위한 Attention 순환 신경망: BiLSTM + At....

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

### Seq2seq + Attention (질의응답 챗봇)

간단한 Seq2seq 모델을 구축하여 질의로 부터 응답을 생성해내는 모델 아케텍처를 만듭니다. 이때 Attention을 추가하여 입력 시퀀스의 각 토큰에 대한 중요도를 계산하여 모든 토큰을 균등하게 처리하는 것이 아니라, 중요한 토큰에 더 집중할 수 있게 합니다.

- 읽을 포인트: 세부 흐름: 모델링 > 인코더 구성, 모델링 > 디코더 구성, 모델링 > 모델 학습

#### 모델링 > 인코더 구성

인코더는 입력된 텍스트에 대한 가중치를 만들어내는 작업만 진행하기 때문에 기존 임베딩+RNN 모델 구조와 유사하게 구현됩니다. 디코더와 연결을 위해 LSTM의 출력 결과와 히든 상태를 전부 return 합니다.

#### 모델링 > 디코더 구성

디코더는 생성 하고자 하는 문장의 직적 토큰으로 부터 다음 토큰을 생성하는 역할을 합니다. 이때 인코더가 만들어낸 입력 텍스트의 순환특성과 함께 직전 토큰을 입력 받아 새로운 토큰을 만들어 냅니다.

#### 모델링 > 모델 학습

Seq2seq 모델은 구성한 Eencoder와 Decoder를 동시학습 합니다. 입력 데이터인 질문 토큰을 인코더에 입력 2. 인코더의 출력과 히든 상태, 셀 상태를 디코더의 초기 입력으로 설정 3. 디코더는 타겟 데이터인 응답 토큰이 모두 생성될 때 까지 반복하여 토큰을 생성 4...

### 감정 분류을 위한 Attention 순환 신경망: BiLSTM + Attention

기존 Embedding + BiLSTM 모델 아키텍처에 Bahdanau Attention(Additive)을 추가 BiLSTM 층을 통과해 나온 특성 벡터를 폴링 하지 않고 Attention을 통해 문장 전체에서 가장 중요한 토큰들의 정보가 압축된 컨텍스트 벡터(context vector)를 만듦

- 읽을 포인트: 세부 흐름: 모델링, 모델 학습, 모델 학습(train) + 평가(validation) 단계

#### 모델링

임베딩 레이어 사용 - 토큰의 정수 인덱스로 부터 Embedding 레이어를 통 정수를 해당하는 임베딩 벡터로 매핑 Bi-LSTM (Bidirectional LSTM) 레이어 - 입력된 임베딩 벡터를 시간 축을 따라 처리하여, 시퀀스 데이터의 문맥 정보를 학습 - 양방향 LSTM은...

#### 모델 학습

AIHUB에서 제공하는 한국어 감성 대화 말뭉치 데이터세트를 부분적으로 활용하여 감정 분류 학습

#### 모델 학습(train) + 평가(validation) 단계

단순 RNN 위에 Attention을 추가했을때 성능 향상은 있지만 여전히 과적합에는 취약하다

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

1. Seq2seq + Attention (질의응답 챗봇): 모델링 > 인코더 구성, 모델링 > 디코더 구성
2. 감정 분류을 위한 Attention 순환 신경망: BiLSTM + Attention: 모델링, 모델 학습

## Code Highlights

### 모델링

`모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 임베딩 레이어, 양방향 LSTM 레이어, 어텐션 레이어 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn

class BiLSTMWithAttention(nn.Module):
  def __init__(self, vocab_size, embedding_dim, hidden_size=12, num_layers=4, num_classes=2):
    super(BiLSTMWithAttention, self).__init__()

    # 임베딩 레이어
    self.embedding = nn.Embedding(vocab_size, embedding_dim)

    # 양방향 LSTM 레이어
    self.lstm = nn.LSTM(
        input_size=embedding_dim,
        hidden_size=hidden_size,
        num_layers=num_layers,
        batch_first = True,
        bidirectional = True
    )


    # 어텐션 레이어
    self.attention = nn.Linear(hidden_size*2, hidden_size*2) # 양방향이므로 hidden_size * 2
    self.context_vector = nn.Linear(hidden_size * 2, 1, bias=False)

    self.layer_norm = nn.LayerNorm(hidden_size*2)
    self.dropout = nn.Dropout(p=0.2)

    # 출력 레이어 num_classes로 출력
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

`디코더 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Bahdanau(가산) 어텐션 레이어와 컨텍스트 벡터 계산, 최종 출력 (단어 분포), 어텐션 가중치 계산 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from math import e

class Decoder(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_size=128, num_layers=1, dropout=0.1):
        super(Decoder, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(
            input_size=embedding_dim + hidden_size,  # 디코더 입력: [이전 단어 임베딩 + 컨텍스트 벡터]
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
        )

        # Bahdanau(가산) 어텐션 레이어와 컨텍스트 벡터 계산
        self.attention1 = nn.Linear(hidden_size, hidden_size)
        self.attention2 = nn.Linear(hidden_size, hidden_size)
        self.v = nn.Linear(hidden_size, 1, bias=False)

        # 최종 출력 (단어 분포)
        self.fc_out = nn.Linear(hidden_size, vocab_size)

        self.dropout = nn.Dropout(dropout)
        self.hidden_size = hidden_size

    def forward(self, input_token, hidden, cell, encoder_outputs):
# ... trimmed ...
```

### 모델 학습

`모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 인코더 순전파, 디코더 초기 hidden을 인코더 hidden으로 설정, 디코더 첫 입력: 토큰 흐름이 주석과 함께 드러납니다.

```python
for e in range(num_epochs):
    encoder.train()
    decoder.train()
    total_loss = 0.0
    for i, (inp, tar) in enumerate(dataloader):
        inp = inp.long().to(device)
        tar = tar.long().to(device)

        optimizer.zero_grad()

        # ------ 인코더 순전파 ------
        enc_output, h, c = encoder(inp)

        # 디코더 초기 hidden을 인코더 hidden으로 설정

        # 디코더 첫 입력: <bos> 토큰
        dec_input = tar[:,0]
        dec_hidden = h
        dec_cell = c
        loss = 0.0

        # 교사 강요(teacher forcing) - 다음 입력으로 타겟을 피딩(feeding)
        for t in range(1, tar.size(1)):
            # 디코더 순전파 (dec_input: [batch_size, 1] - 직전 토큰)
            pred, dec_hidden, dec_cell = decoder(dec_input, dec_hidden, dec_cell, enc_output)

            # 정답 토큰과 손실
            step_loss = loss_fn(pred, tar[:, t])
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
