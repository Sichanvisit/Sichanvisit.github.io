---
title: "트랜스포머"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)트랜스포머"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)트랜스포머.md"
excerpt: "Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다"
research_summary: "Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성. 트랜스포머의 심장인 Attention(Q, K, V) 공식을 코드로 직접 구현합니다. `md` 원본과 23개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, math, numpy, matplotlib입니다."
research_artifacts: "md · 코드 23개 · 실행 17개"
code_block_count: 23
execution_block_count: 17
research_focus:
  - "Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고..."
  - "Transformer 모델 구조"
  - "🧩 Transformer 구현 단계별 가이드"
research_stack:
  - "torch"
  - "math"
  - "numpy"
  - "matplotlib"
  - "google"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성. 트랜스포머의 심장인 Attention(Q, K, V) 공식을 코드로 직접 구현합니다. `md` 원본과 23개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, math, numpy, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위..., Transformer 모델 구조, 🧩 Transformer 구현 단계별 가이드.

**남겨둔 자료**: `md` 원본과 23개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, math, numpy, matplotlib입니다.

**주요 스택**: `torch`, `math`, `numpy`, `matplotlib`, `google`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 23 |
| Execution Cells | 17 |
| Libraries | `torch`, `math`, `numpy`, `matplotlib`, `google`, `sentencepiece`, `pandas`, `re` |
| Source Note | `3-2 (실습)트랜스포머` |

## What This Note Covers

### Transformer 모델 구조

Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성

### ⚙️ 1단계: *Scaled Dot-Product Attention*

트랜스포머의 심장인 Attention(Q, K, V) 공식을 코드로 직접 구현합니다.

### 🧠 2단계: *Multi-Head Attention*

1단계에서 만든 어텐션을 여러 개 병렬로 실행하여 “다양한 관점”에서 문장을 바라볼 수 있도록 확장합니다.

### 🛡️ 3단계: *Padding & Look-Ahead Masks*

어텐션이 불필요한 토큰을 무시하고, 디코더가 미래 단어를 미리 엿보지 못하게 합니다.

## Implementation Flow

1. Transformer 모델 구조: Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성
2. ⚙️ 1단계: *Scaled Dot-Product Attention*: 트랜스포머의 심장인 Attention(Q, K, V) 공식을 코드로 직접 구현합니다.
3. 🧠 2단계: *Multi-Head Attention*: 1단계에서 만든 어텐션을 여러 개 병렬로 실행하여 “다양한 관점”에서 문장을 바라볼 수 있도록 확장합니다.
4. 🛡️ 3단계: *Padding & Look-Ahead Masks*: 어텐션이 불필요한 토큰을 무시하고, 디코더가 미래 단어를 미리 엿보지 못하게 합니다.

## Code Highlights

### 데이터세트 준비

`데이터세트 준비`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 이전 Seq2seq 모델 학습과 동일하게 준비한 Transformer 모델에 AIHUB 한국어 감성 대화 말뭉치를 부분적으로 활용하여 질의(입력) 응답(타겟) 데이터세트를 학습 합니다.

```python
class SPDataSet(Dataset):
    def __init__(self, sp, max_len):
        self.max_len = max_len
        self.df = pd.read_csv(f'./train.csv')[['HS01','SS01']]
        self.sp = sp

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

        inp = self.zero_pad(sent1 + [self.sp.eos_id()])
        tar = self.zero_pad([self.sp.bos_id()] + sent2 + [self.sp.eos_id()])

        return torch.Tensor(inp), torch.Tensor(tar)


# ... trimmed ...
```

### 모델 학습

`모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 batch_size, seq_len => batch_size * seq_len 하여 손실 연산, pred shape: (batch_size, seq_len, vocab_size), real shape: (batch_size, seq_len) 흐름이 주석과 함께 드러납니다.

```python
# batch_size, seq_len => batch_size * seq_len 하여 손실 연산
def loss_function(real, pred, pad_token=0):
    # pred shape: (batch_size, seq_len, vocab_size)
    # real shape: (batch_size, seq_len)
    loss_fn = nn.CrossEntropyLoss(ignore_index=pad_token)  # pad=0 무시
    # reshape to (batch_size * seq_len, vocab_size)
    pred_reshaped = pred.view(-1, pred.size(-1))
    real_reshaped = real.reshape(-1)

    return loss_fn(pred_reshaped, real_reshaped)

# 하이퍼파라미터 설정
sp = spm.SentencePieceProcessor(model_file=f'./model/spm_krsent.model')
num_layers = 4
d_model = 128                       # emd_dim
dff = 256                           # feed_dim
num_heads = 4
vocab_size = sp.get_piece_size()
pe_input = 10000
pe_target = 10000
dropout_rate = 0.1
max_len = 60
pad_token = 0
lr = 2e-4
batch_size = 64
epochs = 50

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-2 (실습)트랜스포머.md`
- Source formats: `md`
- Companion files: `3-2 (실습)트랜스포머.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `7, 6, 2, 0, 0`, `True, True, True, False, False`, `[[1, 1, 1, 0, 0`, `1, 2, 3, 4, 5, 6, 0, 0, 0, 0`, `1, 2, 3, 4, 5, 6, 7, 8, 0, 0`
- External references: `www.aihub.or.kr`, `arxiv.org`, `drive.google.com`, `localhost`

## Note Preview

> Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성
> 출처: https://arxiv.org/abs/1706.03762
