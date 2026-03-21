---
title: "트랜스포머"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)트랜스포머"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)트랜스포머.md"
excerpt: "Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성 출처: https://arxiv.org/abs/1706...."
research_summary: "Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성 출처: https://arxiv.org/abs/1706.03762. 트랜스포머의 심장인 Attention(Q, K, V) 공식을 코드로 직접 구현합니다. $$ Attention(Q, K, V) = softmax\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V $$. `md` 원본과 23개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, math, numpy, matplotlib입니다."
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

Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성 출처: https://arxiv.org/abs/1706.03762. 트랜스포머의 심장인 Attention(Q, K, V) 공식을 코드로 직접 구현합니다. $$ Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V $$. `md` 원본과 23개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, math, numpy, matplotlib입니다.

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

### 트랜스포머 > Transformer 모델 구조

Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성 출처: https://arxiv.org/abs/1706.03762

### Transformer 구현 단계별 가이드 > ⚙ 1단계: *Scaled Dot-Product Attention*

트랜스포머의 심장인 Attention(Q, K, V) 공식을 코드로 직접 구현합니다. $$ Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V $$

### Transformer 구현 단계별 가이드 > 2단계: *Multi-Head Attention*

1단계에서 만든 어텐션을 여러 개 병렬로 실행하여 “다양한 관점”에서 문장을 바라볼 수 있도록 확장합니다. 여러 헤드(num_heads)를 통해 병렬 어텐션 수행 - 각 헤드의 출력을 결합(concat) 후 선형 변환

### Transformer 구현 단계별 가이드 > 3단계: *Padding & Look-Ahead Masks*

어텐션이 불필요한 토큰을 무시하고, 디코더가 미래 단어를 미리 엿보지 못하게 합니다. Padding Mask → 위치를 가려 계산 제외 - Look-Ahead Mask → 디코더가 다음 단어를 보지 못하도록 제한

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. 트랜스포머 > Transformer 모델 구조: Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성 출처:...
2. Transformer 구현 단계별 가이드 > ⚙ 1단계: *Scaled Dot-Product Attention*: 트랜스포머의 심장인 Attention(Q, K, V) 공식을 코드로 직접 구현합니다. $$ Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{...
3. Transformer 구현 단계별 가이드 > 2단계: *Multi-Head Attention*: 1단계에서 만든 어텐션을 여러 개 병렬로 실행하여 “다양한 관점”에서 문장을 바라볼 수 있도록 확장합니다. 여러 헤드(num_heads)를 통해 병렬 어텐션 수행 - 각 헤드의 출력을 결합(concat)...
4. Transformer 구현 단계별 가이드 > 3단계: *Padding & Look-Ahead Masks*: 어텐션이 불필요한 토큰을 무시하고, 디코더가 미래 단어를 미리 엿보지 못하게 합니다. Padding Mask → 위치를 가려 계산 제외 - Look-Ahead Mask → 디코더가 다음 단어를...

## Code Highlights

### MultiHead Attention

`MultiHead Attention`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 헤드 분할이 불가능 하면 에러, 임베딩 차원이 헤드 개수로 나누어떨어지는지 확인 (헤드별 동일 차원 보장), 분리된 임베딩 길이 흐름이 주석과 함께 드러납니다.

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, em_dim, num_heads):
        super(MultiHeadAttention, self).__init__()        # 부모 클래스 초기화 함수 호출
        self.num_heads = num_heads      # 헤드 갯수
        self.em_dim = em_dim            # 임베딩 차원

        # 헤드 분할이 불가능 하면 에러
        # 임베딩 차원이 헤드 개수로 나누어떨어지는지 확인 (헤드별 동일 차원 보장)
        assert em_dim % num_heads == 0, "em_dim must be divisible by num_heads"

        # 분리된 임베딩 길이
        self.depth = em_dim // num_heads

        # 선형레이어
        self.wq = nn.Linear(em_dim, em_dim)
        self.wk = nn.Linear(em_dim, em_dim)
        self.wv = nn.Linear(em_dim, em_dim)

        self.dense = nn.Linear(em_dim, em_dim)

    # 헤드 분할 함수: 입력 임베딩을 여러 개의 “헤드(head)”로 나누는 역할
    # 최종 출력 shape: (batch_size, num_heads, seq_len, depth)
    def split_heads(self, x):
        '''
            예)
            [------512차원------]
            ↓ 분할 (8개 헤드)
            [64][64][64][64][64][64][64][64]
# ... trimmed ...
```

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
