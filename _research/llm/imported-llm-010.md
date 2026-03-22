---
title: "트랜스포머"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)트랜스포머"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)트랜스포머.md"
excerpt: "트랜스포머, Transformer 구현 단계별 가이드 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 트랜스포머, Transformer 구현 단계별 가이드 순서로 핵심 장면을 먼저 훑고, 인코더 레이어, 디코더 레이어, 데이터세트..."
research_summary: "트랜스포머, Transformer 구현 단계별 가이드 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 트랜스포머, Transformer 구현 단계별 가이드 순서로 핵심 장면을 먼저 훑고, 인코더 레이어, 디코더 레이어, 데이터세트 준비 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 23개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, math, numpy, matplotlib입니다."
research_artifacts: "md · 코드 23개 · 실행 17개"
code_block_count: 23
execution_block_count: 17
research_focus:
  - "트랜스포머"
  - "Transformer 구현 단계별 가이드"
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

트랜스포머, Transformer 구현 단계별 가이드 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 트랜스포머, Transformer 구현 단계별 가이드 순서로 핵심 장면을 먼저 훑고, 인코더 레이어, 디코더 레이어, 데이터세트 준비 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 23개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, math, numpy, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: 트랜스포머, Transformer 구현 단계별 가이드.

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

### 트랜스포머

Transformer 모델 구조 같은 코드를 직접 따라가며 트랜스포머 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Transformer 모델 구조

#### Transformer 모델 구조

Transformer는 Seq2seq와 비슷하게 기계번역을 해결하기 위한 인코더와 디코더구조를 가지고 있습니다. Seq2seq와는 달리 인코더 와 디코더 내부에는 MultiHeadAttention 블록과 FeedForwaed라는 블록으로 구성 출처: https://arxiv.org...

### Transformer 구현 단계별 가이드

9단계: 추론 및 평가 — *Gen..., 9단계: 추론 및 평가 — *Gen..., Transformer 학습 하기 >... 같은 코드를 직접 따라가며 Transformer 구현 단계별 가이드 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 9단계: 추론 및 평가 — *Generation & BLEU* > 어텐션 마스크, 9단계: 추론 및 평가 — *Generation & BLEU* > 포지션 인코딩, Transformer 학습 하기 > 데이터세트 준비

#### 9단계: 추론 및 평가 — *Generation & BLEU* > 어텐션 마스크

Transformer는 학습 효율을 위해 크게 두가지의 마스크를 활용하여 연산의 효율을 얻습니다. padding mask * 토큰 길이(seq_len)에 못 미쳐 패딩이 된 경우 의미 없는 단어가 연산에 적용되지 않게 하기 위한 마스크 * 인코더와 디코더에서 둘다 사용

#### 9단계: 추론 및 평가 — *Generation & BLEU* > 포지션 인코딩

멀티헤드 어텐션은 입력 순서를 고려하지 않는(Self-Attention) 구조이므로, 단어의 순서 정보 추가 필요합니다. 이러한 순서정보를 추가하기 위해 토큰 임베딩 결과에 순서정보를 더해줍니다. 포지션 인코딩은 각 포지션의 각도를 구한뒤 sin, cos 함수를 적용하여 상대적인...

#### Transformer 학습 하기 > 데이터세트 준비

이전 Seq2seq 모델 학습과 동일하게 준비한 Transformer 모델에 AIHUB 한국어 감성 대화 말뭉치를 부분적으로 활용하여 질의(입력) 응답(타겟) 데이터세트를 학습 합니다.

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

## Implementation Flow

1. 트랜스포머: Transformer 모델 구조
2. Transformer 구현 단계별 가이드: 9단계: 추론 및 평가 — *Generation & BLEU* > 어텐션 마스크, 9단계: 추론 및 평가 — *Generation & BLEU* > 포지션 인코딩

## Code Highlights

### 인코더 레이어

`인코더 레이어`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Transformer 인코더 블록(Encoder Block) 하나를 구현한 코드, 두 개의 서브층(sub-layer): Multi-Head Attention, Feed F..., Multi-head attention: 문맥을 학습 흐름이 주석과 함께 드러납니다.

```python
# Transformer 인코더 블록(Encoder Block) 하나를 구현한 코드
class EncoderLayer(nn.Module):
  '''
  한 개의 Encoder Layer는 ① Multi-Head Attention → ② Feed Forward Network 두 블록으로 구성
  각 블록 뒤에는 Residual Connection(잔차 연결) + Layer Normalization 이 있습니다.
  '''
  def __init__(self, em_dim, num_heads, feed_dim, rate=0.1):
    super(EncoderLayer, self).__init__()
    self.mha = MultiHeadAttention(em_dim, num_heads)
    self.ffn = point_wise_feed_forward_network(em_dim, feed_dim)

    # 두 개의 서브층(sub-layer): Multi-Head Attention, Feed Forward Network
    self.layernorm1 = nn.LayerNorm(em_dim, eps=1e-6)  # 학습을 안정화하고, 입력 분포를 정규화
    self.layernorm2 = nn.LayerNorm(em_dim, eps=1e-6)
    self.dropout1 = nn.Dropout(rate)                  # 과적합 방지용, 일부 뉴런을 확률적으로 비활성화
    self.dropout2 = nn.Dropout(rate)

  def forward(self, x, mask=None):
    # Multi-head attention: 문맥을 학습
    attn_output, _ = self.mha(x, x, x, mask)  # (batch_size, seq_len, em_dim)
    attn_output = self.dropout1(attn_output)
    out1 = self.layernorm1(x + attn_output)   # (batch_size, seq_len, em_dim)

    # Feed Forward: 단어별 표현을 확장
    ffn_output = self.ffn(out1)
    ffn_output = self.dropout2(ffn_output)
    out2 = self.layernorm2(out1 + ffn_output) # (batch_size, seq_len, em_dim)

# ... trimmed ...
```

### 디코더 레이어

`디코더 레이어`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Transformer 디코더 블록(Decoder Block) 하나를 구현한 코드: 인코더..., Masked Multi-Head Self-Attention: 다음 단어를 예측할 때, 아..., 인코더 출력과의 어텐션: 입력 문장(인코더 출력) 의 정보와 현재까지 생성된 디코더 문장... 흐름이 주석과 함께 드러납니다.

```python
# Transformer 디코더 블록(Decoder Block) 하나를 구현한 코드: 인코더 출력을 받아서 다음 단어를 생성할 준비를 하는 핵심 블록
class DecoderLayer(nn.Module):
  '''
    3개의 서브층(sub-layer)
      1) Masked Multi-Head Self-Attention: 디코더 내부 단어들끼리 어텐션 (미래 단어 가리기)
      2) Encoder–Decoder Attention: 인코더의 출력과 어텐션 (입력 문장 참고)
      3) Feed Forward Network (FFN): 각 단어 벡터 독립적으로 비선형 변환
  '''
  def __init__(self, em_dim, num_heads, feed_dim, rate=0.1):
    super(DecoderLayer, self).__init__()
    self.mha1 = MultiHeadAttention(em_dim, num_heads)
    self.mha2 = MultiHeadAttention(em_dim, num_heads)
    self.ffn = point_wise_feed_forward_network(em_dim, feed_dim)

    self.layernorm1 = nn.LayerNorm(em_dim, eps=1e-6)
    self.layernorm2 = nn.LayerNorm(em_dim, eps=1e-6)
    self.layernorm3 = nn.LayerNorm(em_dim, eps=1e-6)

    self.dropout1 = nn.Dropout(rate)
    self.dropout2 = nn.Dropout(rate)
    self.dropout3 = nn.Dropout(rate)

  def forward(self, x, enc_output, look_ahead_mask=None, padding_mask=None):
    # Masked Multi-Head Self-Attention: 다음 단어를 예측할 때, 아직 생성되지 않은 미래 단어를 보지 못하게 하면서 문맥(이전 단어들)만 참고하도록 만듧
    attn1, attn_weights_block1 = self.mha1(x, x, x, look_ahead_mask)    # look_ahead_mask: 미래 단어를 보지 않도록 막는 마스크
    attn1 = self.dropout1(attn1)
    out1 = self.layernorm1(x + attn1)

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
