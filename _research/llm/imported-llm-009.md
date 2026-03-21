---
title: "Seq2Seq Attention Transformer"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)Seq2Seq_Attention_Transformer"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)Seq2Seq_Attention_Transformer.md"
excerpt: "데이터 전처리, Seq2Seq, Attention 중심으로 구현 과정을 정리한 Seq2Seq Attention Transformer 기록입니다"
research_summary: "데이터 전처리, Seq2Seq, Attention 중심으로 구현 과정을 정리한 Seq2Seq Attention Transformer 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 15개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, pandas, torch, sklearn입니다."
research_artifacts: "md · 코드 15개 · 실행 9개"
code_block_count: 15
execution_block_count: 9
research_focus:
  - "데이터 전처리"
  - "Seq2Seq"
  - "Attention"
research_stack:
  - "kagglehub"
  - "pandas"
  - "torch"
  - "sklearn"
  - "random"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

데이터 전처리, Seq2Seq, Attention 중심으로 구현 과정을 정리한 Seq2Seq Attention Transformer 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 15개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, pandas, torch, sklearn입니다.

**빠르게 볼 수 있는 포인트**: 데이터 전처리, Seq2Seq, Attention.

**남겨둔 자료**: `md` 원본과 15개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, pandas, torch, sklearn입니다.

**주요 스택**: `kagglehub`, `pandas`, `torch`, `sklearn`, `random`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 15 |
| Execution Cells | 9 |
| Libraries | `kagglehub`, `pandas`, `torch`, `sklearn`, `random` |
| Source Note | `3-2 (실습)Seq2Seq_Attention_Transformer` |

## What This Note Covers

- 데이터 전처리
- Seq2Seq
- Attention
- Transformer
- Download latest version

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

1. Key Step: Reviews.csv 파일에서 'Text'와 'Summary' 컬럼을 50000줄만 불러오기
2. Key Step: Reviews.csv 파일에서 "Text"와 "Summary" 컬럼 추출하여 리스트로 변환
3. Key Step: 하이퍼파라미터 및 전역 변수 정의
4. Key Step: 특수 토큰 정의 (텍스트 요약에서는 target에 SOS, EOS가 필요)

## Code Highlights

### 데이터 전처리

`데이터 전처리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 하이퍼파라미터 및 전역 변수 정의, 특수 토큰 정의 (텍스트 요약에서는 target에 SOS, EOS가 필요), Lang 클래스 (특수 토큰을 미리 등록) 흐름이 주석과 함께 드러납니다.

```python
import torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler
from sklearn.model_selection import train_test_split

# 하이퍼파라미터 및 전역 변수 정의
MAX_LENGTH = 100  # 최대 시퀀스 길이 (원문과 요약 모두에 적용)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 특수 토큰 정의 (텍스트 요약에서는 target에 SOS, EOS가 필요)
SOS_token = 0
EOS_token = 1
PAD_token = 2
UNK_token = 3

# Lang 클래스 (특수 토큰을 미리 등록)
class Lang:
    def __init__(self, name):
        self.name = name
        # 초기에는 PAD, SOS, EOS, UNK 토큰을 미리 등록 (단어 → 인덱스)
        self.word2index = {"PAD": PAD_token, "SOS": SOS_token, "EOS": EOS_token, "<unk>": UNK_token}
        self.index2word = {PAD_token: "PAD", SOS_token: "SOS", EOS_token: "EOS", UNK_token: "<unk>"}
        self.word2count = {}
        self.n_words = 4  # PAD, SOS, EOS, UNK 포함

    def addSentence(self, sentence, tokenizer):
        for word in tokenizer(sentence):
            self.addWord(word)

# ... trimmed ...
```

### Seq2Seq

`Seq2Seq`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Teacher forcing: Feed the target as the next input, Without teacher forcing: use its own predictions... 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import random
import torch.nn.functional as F

class EncoderRNN(nn.Module):
    def __init__(self, input_size, hidden_size, dropout_p=0.1):
        super(EncoderRNN, self).__init__()
        self.hidden_size = hidden_size

        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, batch_first=True)
        self.dropout = nn.Dropout(dropout_p)

    def forward(self, input, hidden):
        embedded = self.dropout(self.embedding(input))  # [batch_size, seq_len, hidden_size]
        output, hidden = self.gru(embedded, hidden)
        return output, hidden

class DecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size):
        super(DecoderRNN, self).__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size, batch_first=True)
        self.out = nn.Linear(hidden_size, output_size)

    def forward(self, encoder_outputs, encoder_hidden, target_tensor=None):
# ... trimmed ...
```

### Transformer

`Transformer`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 포지셔널 인코딩 정의 (단어 위치 정보 반영), 인코더 정의, 디코더 정의 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# 포지셔널 인코딩 정의 (단어 위치 정보 반영)
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) * (-torch.log(torch.tensor(10000.0)) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe.unsqueeze(0))

    def forward(self, x):
        return x + self.pe[:, :x.size(1)]

# 인코더 정의
class TransformerEncoder(nn.Module):
    def __init__(self, vocab_size, emb_size, n_heads, ff_dim, num_layers, dropout=0.1):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, emb_size, padding_idx=PAD_token)
        self.pos_encoding = PositionalEncoding(emb_size)
        encoder_layer = nn.TransformerEncoderLayer(d_model=emb_size, nhead=n_heads, dim_feedforward=ff_dim, dropout=dropout, batch_first=True)
        self.encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.hidden_size = emb_size

# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-2 (실습)Seq2Seq_Attention_Transformer.md`
- Source formats: `md`
- Companion files: `3-2 (실습)Seq2Seq_Attention_Transformer.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
