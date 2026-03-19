---
title: "FCN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "FCN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/FCN - 공유.md"
excerpt: "DL Shared Note: 실습"
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
| Code Blocks | 11 |
| Execution Cells | 8 |
| Libraries | `os`, `json`, `torch`, `numpy`, `PIL`, `torchvision`, `matplotlib`, `tqdm` |
| Source Note | `FCN - 공유` |

## What I Worked On

- Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기
- Step 2: 이미지와 마스크에 적용할 전처리(Transform) 정의하기
- 이미지 변환:
- 1. PIL 이미지를 tensor로 변환
- 2. tensor의 데이터 타입을 float로 변경

## Implementation Flow

1. Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기
2. Step 2: 이미지와 마스크에 적용할 전처리(Transform) 정의하기
3. 이미지 변환:
4. 1. PIL 이미지를 tensor로 변환
5. 2. tensor의 데이터 타입을 float로 변경
6. 3. 이미지 크기를 (224, 224)로 조정

## Code Highlights

### import os

```python
import os
import json
import torch
import numpy as np
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, datasets
import matplotlib.pyplot as plt

###############################################
# Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기
###############################################
class SegmentationDataset(Dataset):
    def __init__(self, root, train=True, transform=None, target_transform=None, download=False):
        """
        VOCSegmentation 데이터셋을 로드하고, 이미지와 pixel-level segmentation mask를 반환하는 Dataset 클래스입니다.

        Args:
            root (str): 데이터셋이 저장될 루트 경로
            train (bool): True이면 training 데이터를, False이면 validation 데이터를 사용
            transform: 입력 이미지에 적용할 변환(예: 크기 조정, tensor 변환 등)
            target_transform: segmentation mask에 적용할 변환(보통 크기 조정 등, 클래스 값 보존을 위해 nearest interpolation 사용)
            download (bool): 데이터가 없으면 자동으로 다운로드할지 여부
        """
        # train이면 'train', 아니면 'val' 이미지를 선택합니다.
        image_set = 'train' if train else 'val'

        # torchvision의 VOCSegmentation 클래스를 사용하여 VOC 데이터셋을 불러옵니다.
# ... trimmed ...
```

### 하이퍼파라미터 및 디바이스 설정

```python
# 하이퍼파라미터 및 디바이스 설정
num_classes = 21
device = "cuda" if torch.cuda.is_available() else "cpu"
model = FCN8s(num_classes=num_classes).to(device)

# 옵티마이저와 손실 함수 설정
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9, weight_decay=0.0005)
criterion = nn.CrossEntropyLoss()

# 학습 loop (tqdm으로 진행 상황 표시)
num_epochs = 20
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, targets in tqdm(train_dataloader, desc=f"Epoch {epoch+1}/{num_epochs}"):
        images = images.to(device)
        targets = targets.to(device)  # targets shape: [B, H, W]

        # 타겟의 차원 확인 후 squeeze
        if targets.dim() == 4 and targets.size(1) == 1:
            targets = targets.squeeze(1)


        optimizer.zero_grad()
        outputs = model(images)  # outputs shape: [B, num_classes, H, W]
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/FCN - 공유.md`
- Source formats: `md`
- Companion files: `FCN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`

## Note Preview

> -
