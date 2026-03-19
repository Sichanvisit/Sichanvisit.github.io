---
title: "PyTorch DNN기초"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_DNN기초"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_DNN기초.md"
excerpt: "DL Archive Note: 실제 데이터 모델링, 이진 분류, 다중 분류"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 25 |
| Execution Cells | 24 |
| Libraries | `torch`, `sklearn`, `matplotlib`, `torchmetrics` |
| Source Note | `(실습)PyTorch_DNN기초` |

## What I Worked On

- 실제 데이터 모델링
- 이진 분류
- step 1: 데이터 수집
- step 2 : 모델 만들기
- print(losses)

## Implementation Flow

1. 실제 데이터 모델링
2. 이진 분류
3. step 1: 데이터 수집
4. step 2 : 모델 만들기
5. print(losses)
6. step 4 모델 테스트

## Code Highlights

### import torch

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import torch
from torch.utils.data import DataLoader, TensorDataset
```

### 다중 분류

```python
losses=[]
val_losses=[]

# 학습루프
for epoch in range(epochs):
    model.train()
    for batch in train_dataloader:
        X, y = batch[0].to(device), batch[1].to(device)
        preds = model(X)
        loss = loss_fn(preds, y)
        loss.backward()
        opt.step()
        opt.zero_grad()
    losses.append(loss.item())

    # 검증
    model.eval()
    with torch.no_grad():
        val_loss=0
        for val_batch in val_dataloader:
            val_X, val_y = val_batch[0].to(device), val_batch[1].to(device)
            val_preds = model(val_X)
            val_loss += loss_fn(val_preds, val_y).item()
        val_losses.append(val_loss / len(val_dataloader))
        print(len(val_dataloader))
        break
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)PyTorch_DNN기초.md`
- Source formats: `md`
- Companion files: `(실습)PyTorch_DNN기초.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
