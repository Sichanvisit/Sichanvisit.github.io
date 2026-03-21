---
title: "ALBERT 사전학습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)ALBERT_사전학습"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)ALBERT_사전학습.md"
excerpt: "기본 적으로 BERT 모델은 인코딩 블록이 깊어질 수 록 파라미터의 규모가 매우 커질 뿐만 아니라, 매우 큰 어휘 사전(vocab)과 임베딩 길이를 사용할 때, 임베딩 매트릭스가 차지하는 파라미터가 너무 커져 버리는 문제가 생깁니다. ALBERT는 크게 2가지 기법을 활용하여 이를 크게 낮추고 모델..."
research_summary: "기본 적으로 BERT 모델은 인코딩 블록이 깊어질 수 록 파라미터의 규모가 매우 커질 뿐만 아니라, 매우 큰 어휘 사전(vocab)과 임베딩 길이를 사용할 때, 임베딩 매트릭스가 차지하는 파라미터가 너무 커져 버리는 문제가 생깁니다. ALBERT는 크게 2가지 기법을 활용하여 이를 크게 낮추고 모델 파라미터 규모를 효과적으로 줄입니다. BERT vs ALBERT 가중치/메모리/성능 비교. `md` 원본과 11개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, copy, sentencepiece입니다."
research_artifacts: "md · 코드 11개 · 실행 6개"
code_block_count: 11
execution_block_count: 6
research_focus:
  - "기본 적으로 BERT 모델은 인코딩 블록이 깊어질 수 록 파라미터의 규모가 매우 커질 뿐만 아니라, 매..."
  - "ALBERT 모델"
  - "학습 데이터세트 구성"
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

기본 적으로 BERT 모델은 인코딩 블록이 깊어질 수 록 파라미터의 규모가 매우 커질 뿐만 아니라, 매우 큰 어휘 사전(vocab)과 임베딩 길이를 사용할 때, 임베딩 매트릭스가 차지하는 파라미터가 너무 커져 버리는 문제가 생깁니다. ALBERT는 크게 2가지 기법을 활용하여 이를 크게 낮추고 모델 파라미터 규모를 효과적으로 줄입니다. BERT vs ALBERT 가중치/메모리/성능 비교. `md` 원본과 11개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, copy, sentencepiece입니다.

**빠르게 볼 수 있는 포인트**: 기본 적으로 BERT 모델은 인코딩 블록이 깊어질 수 록 파라미터의 규..., ALBERT 모델, 학습 데이터세트 구성.

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, copy, sentencepiece입니다.

**주요 스택**: `google`, `torch`, `copy`, `sentencepiece`, `pandas`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 11 |
| Execution Cells | 6 |
| Libraries | `google`, `torch`, `copy`, `sentencepiece`, `pandas`, `numpy`, `math`, `os` |
| Source Note | `3-3 (실습)ALBERT_사전학습` |

## What This Note Covers

### ALBERT 모델

기본 적으로 BERT 모델은 인코딩 블록이 깊어질 수 록 파라미터의 규모가 매우 커질 뿐만 아니라, 매우 큰 어휘 사전(vocab)과 임베딩 길이를 사용할 때, 임베딩 매트릭스가 차지하는 파라미터가 너무 커져 버리는 문제가 생깁니다. ALBERT는 크게 2가지 기법을 활용하여 이를 크게 낮추고 모델 파라미터 규모를 효과적으로 줄입니다.

### ALBERT 모델 > 모델 학습

BERT vs ALBERT 가중치/메모리/성능 비교

### Key Step

BPE :바이트 페어 인코딩(Byte Pair Encoding, BPE)

### Key Step

추가 쓰기모드로 텍스트 파일 열기

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

1. ALBERT 모델: 기본 적으로 BERT 모델은 인코딩 블록이 깊어질 수 록 파라미터의 규모가 매우 커질 뿐만 아니라, 매우 큰 어휘 사전(vocab)과 임베딩 길이를 사용할 때, 임베딩 매트릭스가 차지하는 파라미터가 너무 커져 버리는 문제가 생깁니다. ALBERT는 크게 2가지 기법을 활용하여 이...
2. ALBERT 모델 > 모델 학습: BERT vs ALBERT 가중치/메모리/성능 비교
3. Key Step: BPE :바이트 페어 인코딩(Byte Pair Encoding, BPE)
4. Key Step: 추가 쓰기모드로 텍스트 파일 열기

## Code Highlights

### 학습 데이터세트 구성

`학습 데이터세트 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 SOP 태스크를 위한 (sent1, sent2, label) 리스트, "올바른 순서" => label = 0, "뒤집힌 순서" => label = 1 흐름이 주석과 함께 드러납니다.

```python
class SPDataSet(Dataset):
    def __init__(self, sp, max_len):
        self.max_len = max_len
        self.df = pd.read_csv(f'./train.csv')
        self.sp = sp

        # SOP 태스크를 위한 (sent1, sent2, label) 리스트
        self.pairs = []

        # "올바른 순서" => label = 0
        # "뒤집힌 순서" => label = 1
        for _, item in self.df.iterrows():
            sent1 = item['HS01']
            sent2 = item['SS01']

            # 원래 순서
            self.pairs.append((sent1, sent2, 0))
            # 뒤집힌 순서
            self.pairs.append((sent2, sent1, 1))

        # 10개의 문장쌍만 확인 (디버그 용도)
        print(self.pairs[:10])

    def zero_pad(self, tok):
        """토큰 리스트를 max_len 길이에 맞춰 제로 패딩"""
        if len(tok) >= self.max_len:
            return tok[:self.max_len]
        else:
# ... trimmed ...
```

### 모델링

`모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 작은 차원의 단어 임베딩, 임베딩 프로젝션 → hidden_dim, 위치 인코딩 흐름이 주석과 함께 드러납니다.

```python
class SimpleALBERT(nn.Module):
    def __init__(
        self,
        vocab_size,
        embedding_dim=64,
        hidden_dim=256,
        num_heads=4,
        feed_dim=512,
        num_layers=4,
        num_classes=2,   # SOP 또한 이진 분류
        dropout=0.1
    ):
        super().__init__()

        # 작은 차원의 단어 임베딩
        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)

        # 임베딩 프로젝션 → hidden_dim
        self.embedding_proj = nn.Linear(embedding_dim, hidden_dim)

        # 위치 인코딩
        self.pos_encoding = PositionalEncoding(hidden_dim)
        self.dropout = nn.Dropout(dropout)

        # ALBERT: 모든 레이어 가중치 공유
        self.transformer_block = MTBlock(hidden_dim, num_heads, feed_dim, dropout=dropout)
        self.num_layers = num_layers

# ... trimmed ...
```

### 모델 학습

`모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 하이퍼파라미터 정의, MLM 변환 함수에 넣어줄 스페셜 토큰 정의, 마스크 토큰이 추가되므로 토큰개수에 +1 흐름이 주석과 함께 드러납니다.

```python
# 하이퍼파라미터 정의
seq_len = 100
embed_dim = 64
hidden_dim=128
num_heads = 4
feed_dim = 256
num_layers = 4
num_classes = 2
num_epochs = 50
batch_size = 64
lr = 1e-4

# MLM 변환 함수에 넣어줄 스페셜 토큰 정의
mask_id = sp.get_piece_size()
special_tokens_ids = [sp.bos_id(), sp.eos_id(), 0]

# 마스크 토큰이 추가되므로 토큰개수에 +1
sp = spm.SentencePieceProcessor(model_file=f'./bpe/spm_krsent.model')
vocab_size = sp.get_piece_size() + 1

# 데이터세트 분할
dataset = SPDataSet(sp, seq_len)
generator1 = torch.Generator().manual_seed(42)
test_dataset, train_dataset = random_split(dataset, [0.2, 0.8], generator=generator1)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-3 (실습)ALBERT_사전학습.md`
- Source formats: `md`
- Companion files: `3-3 (실습)ALBERT_사전학습.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `HS01'',''SS01`, `Hugging`
- External references: `localhost`

## Note Preview

> 기본 적으로 BERT 모델은 인코딩 블록이 깊어질 수 록 파라미터의 규모가 매우 커질 뿐만 아니라, 매우 큰 어휘 사전(vocab)과 임베딩 길이를 사용할 때, 임베딩 매트릭스가 차지하는 파라미터가 너무 커져 버리는 문제가 생깁니다.
> ALBERT는 크게 2가지 기법을 활용하여 이를 크게 낮추고 모델 파라미터 규모를 효과적으로 줄입니다.
