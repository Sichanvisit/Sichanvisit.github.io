---
title: "12 언어모델 전이학습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3  12_언어모델 전이학습"
source_path: "13_LLM_GenAI/Code_Snippets/3-3  12_언어모델 전이학습.md"
excerpt: "Hugging Face transformers 라이브러리를 사용하여 문서 요약 모델을 구현하는 미션입니다"
research_summary: "Hugging Face transformers 라이브러리를 사용하여 문서 요약 모델을 구현하는 미션입니다. 데이터 로드 및 전처리부터 요약 모델 실행, 결과 평가까지 전체 파이프라인을 구축해 보세요. 먼저 이번 미션에 사용할 데이터 셋을 다운로드 받아주세요. (약 0.4GB). `md` 원본과 29개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, tqdm, numpy, google입니다."
research_artifacts: "md · 코드 29개 · 실행 15개"
code_block_count: 29
execution_block_count: 15
research_focus:
  - "Hugging Face transformers 라이브러리를 사용하여 문서 요약 모델을 구현하는 미션입니..."
  - "미션 소개"
  - "먼저 이번 미션에 사용할 데이터 셋을 다운로드 받아주세요. (약 0.4GB)"
research_stack:
  - "torch"
  - "tqdm"
  - "numpy"
  - "google"
  - "os"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

Hugging Face transformers 라이브러리를 사용하여 문서 요약 모델을 구현하는 미션입니다. 데이터 로드 및 전처리부터 요약 모델 실행, 결과 평가까지 전체 파이프라인을 구축해 보세요. 먼저 이번 미션에 사용할 데이터 셋을 다운로드 받아주세요. (약 0.4GB). `md` 원본과 29개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, tqdm, numpy, google입니다.

**빠르게 볼 수 있는 포인트**: Hugging Face transformers 라이브러리를 사용하여 문..., 미션 소개, 먼저 이번 미션에 사용할 데이터 셋을 다운로드 받아주세요. (약 0.4GB).

**남겨둔 자료**: `md` 원본과 29개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, tqdm, numpy, google입니다.

**주요 스택**: `torch`, `tqdm`, `numpy`, `google`, `os`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 29 |
| Execution Cells | 15 |
| Libraries | `torch`, `tqdm`, `numpy`, `google`, `os`, `json`, `pandas`, `matplotlib` |
| Source Note | `3-3 12_언어모델 전이학습` |

## What This Note Covers

### 미션 소개

Hugging Face transformers 라이브러리를 사용하여 문서 요약 모델을 구현하는 미션입니다. 데이터 로드 및 전처리부터 요약 모델 실행, 결과 평가까지 전체 파이프라인을 구축해 보세요.

### 사용 데이터셋

먼저 이번 미션에 사용할 데이터 셋을 다운로드 받아주세요. (약 0.4GB)

### 데이터 형식

JSON 파일 형태로 제공되며, 3종류(신문 기사, 사설, 법률)의 문서가 포함되어 있습니다.

### 데이터 구성

각 문서 타입은 train/test 쌍으로 구성되어 있으며, 전체 데이터를 모두 사용하거나 원하는 문서 종류를 선택하여 학습시키면 됩니다.

## Implementation Flow

1. 미션 소개: Hugging Face transformers 라이브러리를 사용하여 문서 요약 모델을 구현하는 미션입니다. 데이터 로드 및 전처리부터 요약 모델 실행, 결과 평가까지 전체 파이프라인을 구축해 보세요.
2. 사용 데이터셋: 먼저 이번 미션에 사용할 데이터 셋을 다운로드 받아주세요. (약 0.4GB)
3. 데이터 형식: JSON 파일 형태로 제공되며, 3종류(신문 기사, 사설, 법률)의 문서가 포함되어 있습니다.
4. 데이터 구성: 각 문서 타입은 train/test 쌍으로 구성되어 있으며, 전체 데이터를 모두 사용하거나 원하는 문서 종류를 선택하여 학습시키면 됩니다.

## Code Highlights

### 학습 코드

`학습 코드`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 SentencePiece 모델 로드, 데이터셋 및 DataLoader 생성, 모델 및 학습 설정 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
from torch.optim import AdamW
from torch.amp import GradScaler, autocast
from tqdm import tqdm
from transformers import get_linear_schedule_with_warmup
import matplotlib.pyplot as plt
import pandas as pd
import os

# SentencePiece 모델 로드
sp = spm.SentencePieceProcessor(model_file='Law_tok.model')

# 데이터셋 및 DataLoader 생성
train_dataset = SPDataSet(sp, train_df, max_len=300, mask_prob=0.15, debug=False)
train_dataloader = DataLoader(train_dataset, batch_size=4, shuffle=True)

valid_dataset = SPDataSet(sp, valid_df, max_len=300, mask_prob=0.15, debug=False)
valid_dataloader = DataLoader(valid_dataset, batch_size=4, shuffle=False)

# 모델 및 학습 설정
# config = BertConfig(
#     vocab_size=32000,
#     hidden_size=768,
#     num_layers=12,
#     num_heads=12,
#     max_len=512,
#     dropout=0.1
# ... trimmed ...
```

### 모델

`모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 forward, 출력은 (batch, seq, vocab) → flatten, Validation 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
from torch.optim import AdamW
from torch.utils.data import DataLoader
from transformers import get_linear_schedule_with_warmup
from tqdm import tqdm
import matplotlib.pyplot as plt
import os

def train_summarization_model(model, train_loader, valid_loader, tokenizer, num_epochs=3, save_path='/content/drive/MyDrive/코드잇/스프린트 미션/data/mission12/models/bart_summarizer.pth'):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    optimizer = AdamW(model.parameters(), lr=5e-5)
    total_steps = len(train_loader) * num_epochs
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=1000, num_training_steps=total_steps)

    loss_fn = nn.CrossEntropyLoss(ignore_index=tokenizer.pad_id())

    train_losses = []
    valid_losses = []

    for epoch in range(num_epochs):
        model.train()
        total_train_loss = 0
        progress = tqdm(train_loader, desc=f"[Epoch {epoch+1}] Training")

        for batch in progress:
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-3 12_언어모델 전이학습.md`
- Source formats: `md`
- Companion files: `3-3  12_언어모델 전이학습.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> Hugging Face transformers 라이브러리를 사용하여 문서 요약 모델을 구현하는 미션입니다. 데이터 로드 및 전처리부터 요약 모델 실행, 결과 평가까지 전체 파이프라인을 구축해 보세요.
> 먼저 이번 미션에 사용할 데이터 셋을 다운로드 받아주세요. (약 0.4GB)
