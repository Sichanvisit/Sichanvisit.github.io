---
title: "GPT 사전학습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)GPT_사전학습"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)GPT_사전학습.md"
excerpt: "GPT 사전학습에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 GPT 순서로 핵심 장면을 먼저 훑고, Autoregressive 학습을 위한..., 멀티헤드 블록, 생성 함수가 추가된 모델 구현 같은 코드로 실제 구현을 이어서 확인할 수 있습니다...."
research_summary: "GPT 사전학습에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 GPT 순서로 핵심 장면을 먼저 훑고, Autoregressive 학습을 위한..., 멀티헤드 블록, 생성 함수가 추가된 모델 구현 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, sentencepiece, pandas입니다."
research_artifacts: "md · 코드 13개 · 실행 13개"
code_block_count: 13
execution_block_count: 13
research_focus:
  - "GPT"
research_stack:
  - "google"
  - "torch"
  - "sentencepiece"
  - "pandas"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

GPT 사전학습에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 GPT 순서로 핵심 장면을 먼저 훑고, Autoregressive 학습을 위한..., 멀티헤드 블록, 생성 함수가 추가된 모델 구현 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, sentencepiece, pandas입니다.

**빠르게 볼 수 있는 포인트**: GPT.

**남겨둔 자료**: `md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, sentencepiece, pandas입니다.

**주요 스택**: `google`, `torch`, `sentencepiece`, `pandas`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 13 |
| Execution Cells | 13 |
| Libraries | `google`, `torch`, `sentencepiece`, `pandas`, `numpy`, `os`, `math`, `matplotlib` |
| Source Note | `3-3 (실습)GPT_사전학습` |

## What This Note Covers

### GPT

GPT 학습을 위한 데이터세트 구성, GPT 학습을 위한 데이터세트 구성..., GPT 학습을 위한 데이터세트 구성... 같은 코드를 직접 따라가며 GPT 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: GPT 학습을 위한 데이터세트 구성, GPT 학습을 위한 데이터세트 구성 > Autoregressive 학습을 위한 데이터세트, GPT 학습을 위한 데이터세트 구성 > Causal Mask

#### GPT 학습을 위한 데이터세트 구성

GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다. 사전 학습 * 웹 텍스트나 책, 논문, 뉴스 등 다양한 출처의 방대한 텍스트 데이터를 활용하여 사전학습을 진행 * 특수한 라벨이나 태그가 달려 있지 않으며, 자연어 형태(대체로 가공되지 않은(unla...

#### GPT 학습을 위한 데이터세트 구성 > Autoregressive 학습을 위한 데이터세트

GPT는 Transformer의 디코더 구조를 활용한 모델이므로 기본적으로 자기회귀(Autoregressive) 방식으로 왼쪽에서 오른쪽 방향으로 순차적 토큰을 생성합니다. 따라서 학습을 위한 입력 데이터는 캐주얼(Causal) 마스크를 통해 미래 토큰을 가려주어야 하며, 입력-라...

#### GPT 학습을 위한 데이터세트 구성 > Causal Mask

Causal Mask(look-ahead)는 Transformer에서 구현한 방식과 동일하게 bool 타입의 삼각 행렬로 구현하며, 데이터세트 내부가 아닌 모델 내부에서 적용합니다. nn.MultiheadAttention을 사용하므로 마스킹 될 위치를 True로 설정합니다.

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. GPT: GPT 학습을 위한 데이터세트 구성, GPT 학습을 위한 데이터세트 구성 > Autoregressive 학습을 위한 데이터세트

## Code Highlights

### Autoregressive 학습을 위한 데이터세트

`Autoregressive 학습을 위한 데이터세트`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 문장 구분을 위해 bos 토큰과 eos 토큰 추가, 문장이 끝나면 제로 패딩, 입력 토큰을 왼쪽으로 한 칸 쉬프트하여 라벨링 흐름이 주석과 함께 드러납니다.

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

        # 문장 구분을 위해 bos 토큰과 eos 토큰 추가
        inp = sent1 + [self.sp.bos_id()] + sent2 + [self.sp.eos_id()]

        # 문장이 끝나면 제로 패딩
        input_ids = self.zero_pad(inp)

# ... trimmed ...
```

### 멀티헤드 블록

`멀티헤드 블록`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 멀티헤드, Feed Forward, 정규화 흐름이 주석과 함께 드러납니다.

```python
import math
import torch
from torch import nn

class MTBlock (nn.Module):
    """
    🏗️ Multi-Head Transformer Block
    - Transformer의 기본 구성 요소
    - Self-Attention + Feed Forward Network
    """
    def __init__(self, em_dim, nhead, feed_dim=512, gelu=False, dropout=0.):
        super(MTBlock, self).__init__()

        # 멀티헤드
        self.mha = nn.MultiheadAttention(em_dim, nhead, dropout=dropout, batch_first=True)
        self.nhead = nhead

        # Feed Forward
        if gelu:
            self.active = nn.GELU()
        else:
            self.active = nn.ReLU()

        self.ffn = nn.Sequential(
            nn.Linear(em_dim, feed_dim),
            self.active,
            nn.Dropout(dropout),
            nn.Linear(feed_dim, em_dim)
# ... trimmed ...
```

### 생성 함수가 추가된 모델 구현

`생성 함수가 추가된 모델 구현`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 임베딩 및 포지션 인코딩, 여러 층의 멀티헤드 Block, 토큰 분류를 위한 Head(선형레이어) 흐름이 주석과 함께 드러납니다.

```python
class SimpleGPT(nn.Module):
    def __init__(
            self,
            vocab_size,
            embed_dim=128,
            num_heads=4,
            feed_dim=256,
            num_layers=4,
            dropout=0.1
    ):
        super().__init__()
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim

        # 임베딩 및 포지션 인코딩
        self.token_emb = nn.Embedding(vocab_size, embed_dim)
        self.pos_encoding = PositionalEncoding(embed_dim)
        self.dropout = nn.Dropout(dropout)

        # 여러 층의 멀티헤드 Block
        self.layers = nn.ModuleList([
            MTBlock(embed_dim, num_heads, feed_dim, gelu=True, dropout=dropout)
            for _ in range(num_layers)
        ])

        # 토큰 분류를 위한 Head(선형레이어)
        self.lm_head = nn.Linear(embed_dim, vocab_size)

# ... trimmed ...
```

### 모델 학습하기

`모델 학습하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터세트 구성, 모델 생성, 옵티마이져, 손실 생성 흐름이 주석과 함께 드러납니다.

```python
seq_len = 60
embed_dim = 128
num_heads = 4
feed_dim = 256
num_layers = 4
num_epochs = 50
batch_size = 64
lr = 1e-4

# 데이터세트 구성
sp = spm.SentencePieceProcessor(model_file=f'./bpe/spm_krsent.model')
vocab_size = sp.get_piece_size()

dataset = SPDataSet(sp, seq_len)
generator1 = torch.Generator().manual_seed(42)
test_dataset, train_dataset = random_split(dataset, [0.2, 0.8], generator=generator1)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

print(f'train dataset size: {len(train_dataset)}')
print(f'test dataset size: {len(test_dataset)}')

# 모델 생성
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleGPT(vocab_size, embed_dim, num_heads, feed_dim, num_layers).to(device)

# 옵티마이져, 손실 생성
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-3 (실습)GPT_사전학습.md`
- Source formats: `md`
- Companion files: `3-3 (실습)GPT_사전학습.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `HS01'',''SS01`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `www.aihub.or.kr`, `localhost`, `drive.google.com`

## Note Preview

> GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다.
> - **사전 학습** * 웹 텍스트나 책, 논문, 뉴스 등 다양한 출처의 방대한 텍스트 데이터를 활용하여 사전학습을 진행 * 특수한 라벨이나 태그가 달려 있지 않으며, 자연어 형태(대체로 가공되지 않은(unlabeled) 텍스트 형태)로 학습 * 욕설・중복 등 품질이 매우 낮은 텍스트를 걸러내는 등의 기본적인 전처리(cleaning) 작업만 진행
