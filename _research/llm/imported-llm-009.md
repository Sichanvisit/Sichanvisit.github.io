---
title: "Seq2Seq Attention Transformer"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)Seq2Seq_Attention_Transformer"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)Seq2Seq_Attention_Transformer.md"
excerpt: "Seq2Seq Attention Transformer에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 데이터 전처리, Seq2Seq, Attention 순서로 핵심 장면을 먼저 훑고, 데이터 전처리, Seq2Seq, Attention 같은 코드로 실..."
research_summary: "Seq2Seq Attention Transformer에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 데이터 전처리, Seq2Seq, Attention 순서로 핵심 장면을 먼저 훑고, 데이터 전처리, Seq2Seq, Attention 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 15개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, pandas, torch, sklearn입니다."
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

Seq2Seq Attention Transformer에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 데이터 전처리, Seq2Seq, Attention 순서로 핵심 장면을 먼저 훑고, 데이터 전처리, Seq2Seq, Attention 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 15개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, pandas, torch, sklearn입니다.

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

### 데이터 전처리

데이터 전처리 코드를 직접 따라가며 데이터 전처리 흐름을 확인했습니다.

- 읽을 포인트: 텍스트 정제와 토큰 구성을 바꾸며 입력 품질을 비교하는 구간입니다.

### Seq2Seq

Seq2Seq 코드를 직접 따라가며 Seq2Seq 흐름을 확인했습니다.

- 읽을 포인트: Seq2Seq 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### Attention

Attention 코드를 직접 따라가며 Attention 흐름을 확인했습니다.

- 읽을 포인트: Attention 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### Transformer

Transformer 코드를 직접 따라가며 Transformer 흐름을 확인했습니다.

- 읽을 포인트: Transformer 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

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

1. 데이터 전처리: 데이터 전처리 코드를 직접 따라가며 데이터 전처리 흐름을 확인했습니다.
2. Seq2Seq: Seq2Seq 코드를 직접 따라가며 Seq2Seq 흐름을 확인했습니다.
3. Attention: Attention 코드를 직접 따라가며 Attention 흐름을 확인했습니다.
4. Transformer: Transformer 코드를 직접 따라가며 Transformer 흐름을 확인했습니다.

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

`Seq2Seq`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 teacher forcing 여부에 따라 target_tensor 전달 흐름이 주석과 함께 드러납니다.

```python
def train_epoch(dataloader, encoder, decoder, encoder_optimizer, decoder_optimizer, criterion, teacher_forcing_ratio=0.3):
    total_loss = 0
    for input_batch, target_batch in dataloader:
        encoder_optimizer.zero_grad()
        decoder_optimizer.zero_grad()

        batch_size = input_batch.size(0)

        encoder_hidden = torch.zeros(1, batch_size, encoder.hidden_size, device=device)
        encoder_outputs, encoder_hidden = encoder(input_batch, encoder_hidden)

        # teacher forcing 여부에 따라 target_tensor 전달
        if random.random() < teacher_forcing_ratio:
            decoder_outputs, _, _ = decoder(encoder_outputs, encoder_hidden, target_tensor=target_batch)
        else:
            decoder_outputs, _, _ = decoder(encoder_outputs, encoder_hidden)

        loss = criterion(
            decoder_outputs.view(-1, decoder_outputs.size(-1)),  # [B*T, vocab]
            target_batch.view(-1)                                # [B*T]
        )
        loss.backward()
        encoder_optimizer.step()
        decoder_optimizer.step()

        total_loss += loss.item()

    return total_loss / len(dataloader)
# ... trimmed ...
```

### Attention

`Attention`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Luong Attention 정의, query: (1, B, H), keys: (B, T, H), 내적 기반 스코어 계산 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# Luong Attention 정의
class LuongAttention(nn.Module):
    def __init__(self, hidden_size):
        super(LuongAttention, self).__init__()
        self.attn = nn.Linear(hidden_size, hidden_size)

    def forward(self, query, keys):
        # query: (1, B, H), keys: (B, T, H)
        # 내적 기반 스코어 계산
        query = query.permute(1, 0, 2)  # (B, 1, H)
        keys_proj = self.attn(keys)     # (B, T, H)
        scores = torch.bmm(query, keys_proj.transpose(1, 2))  # (B, 1, T)
        weights = F.softmax(scores, dim=-1)  # (B, 1, T)
        context = torch.bmm(weights, keys)  # (B, 1, H)
        return context, weights

# Attn 기반 디코더
class AttnDecoderRNN(nn.Module):
    def __init__(self, hidden_size, output_size, dropout_p=0.1):
        super(AttnDecoderRNN, self).__init__()
        self.embedding = nn.Embedding(output_size, hidden_size)
        self.attention = LuongAttention(hidden_size)
        self.gru = nn.GRU(hidden_size * 2, hidden_size, batch_first=True)
        self.out = nn.Linear(hidden_size, output_size)
# ... trimmed ...
```

### Transformer

`Transformer`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 초기화, 옵티마이저와 손실함수, 학습 실행 흐름이 주석과 함께 드러납니다.

```python
# 모델 초기화
input_dim = input_lang.n_words
output_dim = output_lang.n_words
emb_dim = 256
n_heads = 8
ff_dim = 512
num_layers = 3

tf_encoder = TransformerEncoder(input_dim, emb_dim, n_heads, ff_dim, num_layers).to(device)
tf_decoder = TransformerDecoder(output_dim, emb_dim, n_heads, ff_dim, num_layers).to(device)

# 옵티마이저와 손실함수
optimizer_enc = torch.optim.Adam(tf_encoder.parameters(), lr=0.0005)
optimizer_dec = torch.optim.Adam(tf_decoder.parameters(), lr=0.0005)
criterion = nn.CrossEntropyLoss(ignore_index=PAD_token)

# 학습 실행
train_transformer(
    encoder=tf_encoder,
    decoder=tf_decoder,
    dataloader=train_dataloader,
    optimizer_enc=optimizer_enc,
    optimizer_dec=optimizer_dec,
    criterion=criterion,
    num_epochs=10
)
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
