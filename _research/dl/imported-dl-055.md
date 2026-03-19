---
title: "U-Net - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "U-Net - 공유"
source_path: "12_Deep_Learning/Code_Snippets/U-Net - 공유.md"
excerpt: "DL Shared Note: PennFudanPed Dataset, 예시: transform 함수 (resize, tensor 변환), UNet 모델 정의"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 7 |
| Execution Cells | 5 |
| Libraries | `os`, `numpy`, `PIL`, `torch`, `torchvision`, `matplotlib` |
| Source Note | `U-Net - 공유` |

## What I Worked On

- PennFudanPed Dataset
- 예시: transform 함수 (resize, tensor 변환)
- UNet 모델 정의
- 학습 및 평가 루프
- 메인 실행 코드

## Implementation Flow

1. PennFudanPed Dataset
2. 예시: transform 함수 (resize, tensor 변환)
3. UNet 모델 정의
4. 학습 및 평가 루프
5. 메인 실행 코드
6. 하이퍼파라미터 설정

## Code Highlights

### import os

```python
import os
import numpy as np
from PIL import Image
import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import torchvision.transforms.functional as TF
import matplotlib.pyplot as plt

# ======================
# PennFudanPed Dataset
# ======================
class PennFudanDataset(Dataset):
    def __init__(self, root, transform=None):
        """
        root: PennFudanPed 폴더의 상위 경로 (예: "./data/PennFudanPed")
        transform: 이미지 및 마스크에 적용할 transform (동일하게 적용)
        """
        self.root = root
        self.imgs_dir = os.path.join(root, "PNGImages")
        self.masks_dir = os.path.join(root, "PedMasks")
        self.imgs = list(sorted(os.listdir(self.imgs_dir)))
        self.masks = list(sorted(os.listdir(self.masks_dir)))
        self.transform = transform

    def __len__(self):
# ... trimmed ...
```

### ======================

```python
# ======================
# 메인 실행 코드
# ======================

# 하이퍼파라미터 설정
num_epochs = 25
batch_size = 4
learning_rate = 1e-4

# device 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Dataset 및 DataLoader
dataset = PennFudanDataset(root="./data/PennFudanPed", transform=joint_transform)

# 학습/검증 분할 (예: 80% train, 20% val)
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])
train_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=2)

# 모델, 손실함수, optimizer
model = UNet(n_channels=3, n_classes=2).to(device)
criterion = nn.CrossEntropyLoss()  # output: [B, 2, H, W], mask: [B, H, W] (각 픽셀 0 또는 1)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# 학습 루프
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/U-Net - 공유.md`
- Source formats: `md`
- Companion files: `U-Net - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`

## Note Preview

> No prose preview was available in the source note.
