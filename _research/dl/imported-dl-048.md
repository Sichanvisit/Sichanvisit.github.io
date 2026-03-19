---
title: "Mission 5 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_5_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_5_강사공유.md"
excerpt: "- 파일 위치 주소 관련 : os - torch : torch, torch.nn, torch.optim. torch.nn.functional - torch.utils.data : Dataset, DataLoader, random_split - torchvision..."
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Mission |
| Source Files | `md` |
| Code Blocks | 44 |
| Execution Cells | 12 |
| Libraries | `os`, `torch`, `numpy`, `cv2`, `matplotlib`, `math`, `torchvision`, `PIL` |
| Source Note | `Mission_5_강사공유` |

## What I Worked On

- 사전처리
- import 추가
- device 설정
- 데이터 처리
- 데이터 설정

## Implementation Flow

1. 사전처리
2. import 추가
3. device 설정
4. 데이터 처리
5. 데이터 설정
6. 데이터 셋 길이와 샘플 출력

## Code Highlights

### import 추가

```python
import os
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import torchvision.transforms.functional as TF
import torch.nn.functional as F

from PIL import Image, ImageEnhance, ImageFilter
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms
from torchvision.transforms import v2
from glob import glob
```

### DataSet Class

```python
class Dataset(Dataset):
  def __init__(self, files, transform=None):
    self.files = files
    self.transform = transform

  def __len__(self):
    return len(self.files)

  def __getitem__(self, idx):
    data_path = os.path.join(self.files[idx])
    img = Image.open(data_path)
    clean_path = data_path.replace("train", "train_cleaned")
    clean_img = Image.open(clean_path)

    if self.transform:
        img, clean_img = self.transform(img, clean_img)

    return img.to(device), clean_img.to(device)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/Mission_5_강사공유.md`
- Source formats: `md`
- Companion files: `Mission_5_강사공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `axes`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - 파일 위치 주소 관련 : os - torch : torch, torch.nn, torch.optim. torch.nn.functional - torch.utils.data : Dataset, DataLoader, random_split - torchvision : torchvision.transform, v2
> * CUDA gpu가 있는 경우 cuda로 디바이스 설정 * mac - Apple 실리콘의 gpu 사용을 위해 mps 설정추가
