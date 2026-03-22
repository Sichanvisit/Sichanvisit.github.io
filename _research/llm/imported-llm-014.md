---
title: "BERT 사전학습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)BERT_사전학습"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)BERT_사전학습.md"
excerpt: "BERT 사전학습에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 사전 학습을 위한 데이터세트 구성, BERT 모델링 순서로 핵심 장면을 먼저 훑고, NSP 학습을 위한 두문장 토큰, MLM 학습을 위한 마스킹 처리, 최종 모델 구현 같은 코드로 실..."
research_summary: "BERT 사전학습에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 사전 학습을 위한 데이터세트 구성, BERT 모델링 순서로 핵심 장면을 먼저 훑고, NSP 학습을 위한 두문장 토큰, MLM 학습을 위한 마스킹 처리, 최종 모델 구현 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, copy, sentencepiece입니다."
research_artifacts: "md · 코드 13개 · 실행 13개"
code_block_count: 13
execution_block_count: 13
research_focus:
  - "사전 학습을 위한 데이터세트 구성"
  - "BERT 모델링"
research_stack:
  - "google"
  - "torch"
  - "copy"
  - "sentencepiece"
  - "pandas"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

BERT 사전학습에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 사전 학습을 위한 데이터세트 구성, BERT 모델링 순서로 핵심 장면을 먼저 훑고, NSP 학습을 위한 두문장 토큰, MLM 학습을 위한 마스킹 처리, 최종 모델 구현 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, copy, sentencepiece입니다.

**빠르게 볼 수 있는 포인트**: 사전 학습을 위한 데이터세트 구성, BERT 모델링.

**남겨둔 자료**: `md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, copy, sentencepiece입니다.

**주요 스택**: `google`, `torch`, `copy`, `sentencepiece`, `pandas`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 13 |
| Execution Cells | 13 |
| Libraries | `google`, `torch`, `copy`, `sentencepiece`, `pandas`, `numpy`, `os`, `math` |
| Source Note | `3-3 (실습)BERT_사전학습` |

## What This Note Covers

### 사전 학습을 위한 데이터세트 구성

BERT 모델은 사전학습과 미세조정(Fine-Tuning)이 확실하게 나눠지는 대표적인 모델입니다. 미세조정은 자연어 Task에 따라 다양하게 진행 될 수 있지만, 사전 학습은 대부분 NSP 학습과 MLM 학습으로 진행이 됩니다. 해당 예시에서는 AIHUB 한국어 감성 대화 말뭉치를 부분적으로 활용하여 질의->응답 으로 NSP와 ML...

- 읽을 포인트: 세부 흐름: NSP 학습을 위한 두문장 토큰, MLM 학습을 위한 마스킹 처리

#### NSP 학습을 위한 두문장 토큰

BERT 사전학습에 있어서 먼저 NSP 학습이 가능하게 하기 위해 2개의 문장을 연결하여 적절하게 연결된 문장과 비적절하게 연결된 문장을 이진 분류 할 수 있게 구성해 줍니다. 이때 데이터세트에서 만들 최종 토큰은 다음과 같습니다.

#### MLM 학습을 위한 마스킹 처리

MLM 마스킹 처리는 데이터세트 내부에서 진행하지 않고 학습 로직에 적용할 함수로 구현합니다. NPS 데이터세트 출력에 랜덤하게 15퍼센트의 토큰을 선택하고 마스킹 처리를 하되, 선택된 모든 토큰을 마스킹 하지 않고 다음 과정으로 진행합니다.

### BERT 모델링

BERT 모델은 pytorch의 nn.MultiheadAttention 레이어를 활용하여 Transformer의 인코더와 동일한 아키텍처로 구성합니다.

- 읽을 포인트: 세부 흐름: 최종 모델 구현, 모델 학습하기(MLM + NSP), NSP 결과를 평가

#### 최종 모델 구현

입력된 토큰을 임베딩 하는 nn.Embedding 레이어와 포지션 인코딩, 멀티헤드 블록을 순차적으로 통과시키는 BERT 모델을 구성합니다. 이때 멀티헤드 블록을 통과한 결과 임베딩을 활용하여 MLM 예측을 위한 선형레이어와 CLS토큰을 통해 이진분류를 하는 NSP 선형레이어 두가...

#### 모델 학습하기(MLM + NSP)

구현한 BERT 모델과 데이터세트, MLM 함수를 활용하여 MLM, NSP 사전학습을 동시에 진행합니다. 따라서 MLM 예측의 손실과 NSP 예측 손실이 각각 구성되어야 합니다.

#### NSP 결과를 평가

Train Loss는 지속적으로 감소하며, Test Accuracy는 꾸준히 증가하여 약 80%까지 도달합니다. 이는 모델이 안정적으로 학습되었고, 과적합 없이 일반화 성능이 향상되고 있음을 의미합니다. NSP 라벨에서 0과 1의 의미

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. 사전 학습을 위한 데이터세트 구성: NSP 학습을 위한 두문장 토큰, MLM 학습을 위한 마스킹 처리
2. BERT 모델링: 최종 모델 구현, 모델 학습하기(MLM + NSP)

## Code Highlights

### NSP 학습을 위한 두문장 토큰

`NSP 학습을 위한 두문장 토큰`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 두개의 문장을 담을 리스트, 적절하게 연결되 문장은 라벨 1로 설정, 비적절한 연결을 만들기 위해 랜덤한 인덱스 생성 흐름이 주석과 함께 드러납니다.

```python
class SPDataSet(Dataset):
    def __init__(self, sp, max_len):
        self.max_len = max_len
        self.df = pd.read_csv(f'./train.csv')
        self.sp = sp

        # 두개의 문장을 담을 리스트
        self.pairs = []

        # 적절하게 연결되 문장은 라벨 1로 설정
        for _, item in df.iterrows():
            sent1 = item['HS01']
            sent2 = item['SS01']
            self.pairs.append((sent1, sent2, 1))

        # 비적절한 연결을 만들기 위해 랜덤한 인덱스 생성
        n_lines = len(df)
        rand_indices = np.random.randint(0, n_lines, size=(n_lines-1,))

        # 랜덤하게 연결된 문장은 라벨을 0으로 설정
        for i, rand_idx in enumerate(rand_indices):
            if i == rand_idx:
                continue
            sent1 = df.iloc[i]['HS01']
            sent2 = df.iloc[rand_idx]['SS01']
            self.pairs.append((sent1, sent2, 0))

        # 앞뒤 10개 문장쌍
# ... trimmed ...
```

### MLM 학습을 위한 마스킹 처리

`MLM 학습을 위한 마스킹 처리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 입력 텐서 크기(B,L) 가져오기, mlm 라벨(-100 기본값) 준비, 라벨 토큰을 위해 동일 형사의 -100 텐서 생성 흐름이 주석과 함께 드러납니다.

```python
def mask_tokens_for_mlm(input_ids, special_tokens_ids, mask_token_id,
                        vocab_size, mlm_prob=0.15):
    """
    🧠 동작 순서
    1) 입력 텐서 크기(B,L) 가져오기
    2) mlm 라벨(-100 기본값) 준비
    3) special token 위치 체크
    4) 15% 토큰 마스킹할 위치 선택
    5) (80/10/10) 규칙에 따라 mask하거나 random하거나 그대로
    6) 최종 masked input + 정답 라벨 반환

    100% 토큰
    └── 15% → 마스킹 대상 (to_mask=True)
      ├── 80% → [MASK] 토큰으로 바꿈
      ├── 10% → 랜덤 토큰으로 바꿈
      └── 10% → 원래 토큰 그대로 유지

    """
    device = input_ids.device
    # 1) 입력 텐서 크기(B,L) 가져오기
    B, L = input_ids.shape                  # batch_size(문장 갯수), seqnece_length(각문장 길이)
    masked_input_ids = input_ids.clone()

    # 2) mlm 라벨(-100 기본값) 준비
    #   라벨 토큰을 위해 동일 형사의 -100 텐서 생성
    mlm_labels = torch.full_like(input_ids, -100)       # -100은 라벨에서 무시되는 토큰으로 사용

    # 3) special token 위치 체크
# ... trimmed ...
```

### 최종 모델 구현

`최종 모델 구현`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 임베딩 (Token + Position), 여러개의 Transformer Encoder Block, MLM 헤드(토큰별 vocab 분류) 흐름이 주석과 함께 드러납니다.

```python
class SimpleBERT(nn.Module):
    def __init__(self, vocab_size, embed_dim=128, num_heads=4,
                 feed_dim=256, num_layers=4, num_classes=2, dropout=0.1):
        super().__init__()
        self.embed_dim = embed_dim

        # 임베딩 (Token + Position)
        self.token_emb = nn.Embedding(vocab_size, embed_dim)
        self.pos_encoding = PositionalEncoding(embed_dim)

        # 여러개의 Transformer Encoder Block
        self.layers = nn.ModuleList([
            MTBlock(embed_dim, num_heads, feed_dim, dropout=dropout)
            for _ in range(num_layers)
        ])
        self.dropout = nn.Dropout(dropout)

        # MLM 헤드(토큰별 vocab 분류)
        self.mlm_head = nn.Linear(embed_dim, vocab_size)

        # NSP 헤드([CLS] 위치 이진 분류)
        self.nsp_head = nn.Linear(embed_dim, 2)

    def forward(self, x, mask=None, mode='both'):
        # x: (batch, seq_len)
        batch_size, seq_len = x.shape
        device = x.device

# ... trimmed ...
```

### 모델 학습하기(MLM + NSP)

`모델 학습하기(MLM + NSP)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 하이퍼파라미터 정의, MLM 변환 함수에 넣어줄 스페셜 토큰 정의, 마스크 토큰이 추가되므로 토큰개수에 + 1 흐름이 주석과 함께 드러납니다.

```python
# 하이퍼파라미터 정의
seq_len = 100        # 입력 문장의 최대 길이(토큰 수). 모든 문장을 길이 100으로 패딩/잘라냄
embed_dim = 128      # 임베딩 차원: 각 토큰을 128차원 벡터로 변환
num_heads = 4        # Multi-Head Attention의 헤드 수 (embed_dim은 head 수로 나눠떨어져야 함)
feed_dim = 256       # FFN(Feed Forward Network) 내부 확장 차원 (128 → 256 → 128)
num_layers = 4       # Transformer Encoder 블록 개수. 깊이가 깊을수록 표현력 증가
num_classes = 2      # 분류 클래스 수(예: 이진 분류 = 2)
num_epochs = 50      # 전체 학습 데이터셋을 반복 학습할 횟수 (training epochs)
batch_size = 64      # 한 번에 처리하는 문장 개수(mini-batch 크기)
lr = 1e-4            # 학습률(Learning Rate). 모델 파라미터 업데이트 속도 조절

# MLM 변환 함수에 넣어줄 스페셜 토큰 정의
mask_id = sp.get_piece_size()
special_tokens_ids = [sp.bos_id(), sp.eos_id(), 0]

# 마스크 토큰이 추가되므로 토큰개수에 + 1
sp = spm.SentencePieceProcessor(model_file=f'./bpe/spm_krsent.model')
vocab_size = sp.get_piece_size() + 1

# 데이터세트 분할
dataset = SPDataSet(sp, seq_len)
generator1 = torch.Generator().manual_seed(42)
test_dataset, train_dataset = random_split(dataset, [0.2, 0.8], generator=generator1)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

print(f'train dataset size: {len(train_dataset)}')
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-3 (실습)BERT_사전학습.md`
- Source formats: `md`
- Companion files: `3-3 (실습)BERT_사전학습.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `HS01'',''SS01`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `www.aihub.or.kr`, `localhost`, `drive.google.com`

## Note Preview

> BERT 모델은 사전학습과 미세조정(Fine-Tuning)이 확실하게 나눠지는 대표적인 모델입니다. 미세조정은 자연어 Task에 따라 다양하게 진행 될 수 있지만, 사전 학습은 대부분 NSP 학습과 MLM 학습으로 진행이 됩니다.
> 해당 예시에서는 AIHUB 한국어 감성 대화 말뭉치를 부분적으로 활용하여 질의->응답 으로 NSP와 MLM 사전 학습을 동시 진행해봅니다.
