---
title: "12 언어모델 전이학습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3  12_언어모델 전이학습"
source_path: "13_LLM_GenAI/Code_Snippets/3-3  12_언어모델 전이학습.md"
excerpt: "Hugging Face transformers 라이브러리를 사용하여 문서 요약 모델을 구현하는 미션입니다. 데이터 로드 및 전처리부터 요약 모델 실행, 결과 평가까지 전체 파이프라인을 구축해 보세요."
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
| Code Blocks | 29 |
| Execution Cells | 15 |
| Libraries | `torch`, `tqdm`, `numpy`, `google`, `os`, `json`, `pandas`, `matplotlib` |
| Source Note | `3-3 12_언어모델 전이학습` |

## What I Worked On

- 미션 소개
- 사용 데이터셋
- 데이터 형식:
- 데이터 구성:
- 가이드라인

## Implementation Flow

1. 미션 소개
2. 사용 데이터셋
3. 데이터 형식:
4. 데이터 구성:
5. 가이드라인
6. 데이터 로드 및 전처리

## Code Highlights

### 학습 코드

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
