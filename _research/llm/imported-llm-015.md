---
title: "GPT 사전학습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)GPT_사전학습"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)GPT_사전학습.md"
excerpt: "GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다"
research_summary: "GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다. GPT는 Transformer의 디코더 구조를 활용한 모델이므로 기본적으로 자기회귀(Autoregressive) 방식으로 왼쪽에서 오른쪽 방향으로 순차적 토큰을 생성합니다. 따라서 학습을 위한 입력 데이터는 캐주얼(Causal) 마스크를 통해 미래 토큰을 가려주어야 하며, 입력-라벨 구조는 단순히 입력 토큰을 왼쪽으로 한칸씩 쉬프트... `md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, sentencepiece, pandas입니다."
research_artifacts: "md · 코드 13개 · 실행 13개"
code_block_count: 13
execution_block_count: 13
research_focus:
  - "GPT"
  - "GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다."
  - "GPT 학습을 위한 데이터세트 구성"
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

GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다. GPT는 Transformer의 디코더 구조를 활용한 모델이므로 기본적으로 자기회귀(Autoregressive) 방식으로 왼쪽에서 오른쪽 방향으로 순차적 토큰을 생성합니다. 따라서 학습을 위한 입력 데이터는 캐주얼(Causal) 마스크를 통해 미래 토큰을 가려주어야 하며, 입력-라벨 구조는 단순히 입력 토큰을 왼쪽으로 한칸씩 쉬프트... `md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, sentencepiece, pandas입니다.

**빠르게 볼 수 있는 포인트**: GPT, GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가..., GPT 학습을 위한 데이터세트 구성.

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

### GPT 학습을 위한 데이터세트 구성

GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다.

### Autoregressive 학습을 위한 데이터세트

GPT는 Transformer의 디코더 구조를 활용한 모델이므로 기본적으로 자기회귀(Autoregressive) 방식으로 왼쪽에서 오른쪽 방향으로 순차적 토큰을 생성합니다. 따라서 학습을 위한 입력 데이터는 캐주얼(Causal) 마스크를 통해 미래 토큰을 가려주어야 하며, 입력-라벨 구조는 단순히 입력 토큰을 왼쪽으로 한칸씩 쉬프트 한 토큰으로 구성이됩니다.

### Causal Mask

Causal Mask(look-ahead)는 Transformer에서 구현한 방식과 동일하게 bool 타입의 삼각 행렬로 구현하며, 데이터세트 내부가 아닌 모델 내부에서 적용합니다.

### GPT 모델링

GPT는 Transformer의 디코더 구조의 아케텍처를 기반으로 합니다. 정확하게는 Transformer디코더는 두개의 멀티헤드 어텐션이 있지만, GPT는 셀프어텐션만 진행하는 하나의 멀티헤드 어텐션만 활용합니다.

## Implementation Flow

1. GPT 학습을 위한 데이터세트 구성: GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다.
2. Autoregressive 학습을 위한 데이터세트: GPT는 Transformer의 디코더 구조를 활용한 모델이므로 기본적으로 자기회귀(Autoregressive) 방식으로 왼쪽에서 오른쪽 방향으로 순차적 토큰을 생성합니다. 따라서 학습을 위한 입력 데이터는 캐주얼(Causal) 마스크를 통해 미래...
3. Causal Mask: Causal Mask(look-ahead)는 Transformer에서 구현한 방식과 동일하게 bool 타입의 삼각 행렬로 구현하며, 데이터세트 내부가 아닌 모델 내부에서 적용합니다.
4. GPT 모델링: GPT는 Transformer의 디코더 구조의 아케텍처를 기반으로 합니다. 정확하게는 Transformer디코더는 두개의 멀티헤드 어텐션이 있지만, GPT는 셀프어텐션만 진행하는 하나의 멀티헤드 어텐션만 활용합니다.

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

### 모델 학습하기

`모델 학습하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 손실 계산시 형상 변환, pred shape: (batch_size, seq_len, vocab_size), tar shape: (batch_size, seq_len) 흐름이 주석과 함께 드러납니다.

```python
# 손실 계산시 형상 변환
def loss_function(tar, pred, pad_token=0):
    # pred shape: (batch_size, seq_len, vocab_size)
    # tar shape: (batch_size, seq_len)
    # pred shape to (batch_size * seq_len, vocab_size)
    pred_reshaped = pred.view(-1, pred.size(-1))
    tar_reshaped = tar.reshape(-1)
    return loss_fn(pred_reshaped, tar_reshaped)

train_loss = []
val_loss = []
for epoch in range(num_epochs):
    model.train()
    total_loss = 0.0
    for step, (input_ids, tar_ids, mask) in enumerate(train_loader):
        input_ids = input_ids.long().to(device)
        tar_ids = tar_ids.long().to(device)
        key_padding_mask = mask.to(device)

        outputs = model(input_ids, key_padding_mask=key_padding_mask)

        loss = loss_function(tar_ids, outputs)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
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
