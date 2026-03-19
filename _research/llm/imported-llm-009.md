---
title: "Seq2Seq Attention Transformer"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)Seq2Seq_Attention_Transformer"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)Seq2Seq_Attention_Transformer.md"
excerpt: "LLM Archive Note: 데이터 전처리, Seq2Seq, Attention"
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
| Code Blocks | 15 |
| Execution Cells | 9 |
| Libraries | `kagglehub`, `pandas`, `torch`, `sklearn`, `random` |
| Source Note | `3-2 (실습)Seq2Seq_Attention_Transformer` |

## What I Worked On

- Download latest version
- Reviews.csv 파일에서 'Text'와 'Summary' 컬럼을 50000줄만 불러오기
- 데이터의 일부 확인
- 데이터 전처리
- Reviews.csv 파일에서 "Text"와 "Summary" 컬럼 추출하여 리스트로 변환

## Implementation Flow

1. Download latest version
2. Reviews.csv 파일에서 'Text'와 'Summary' 컬럼을 50000줄만 불러오기
3. 데이터의 일부 확인
4. 데이터 전처리
5. Reviews.csv 파일에서 "Text"와 "Summary" 컬럼 추출하여 리스트로 변환
6. 하이퍼파라미터 및 전역 변수 정의

## Code Highlights

### 데이터 전처리

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

### Transformer

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

> No prose preview was available in the source note.
