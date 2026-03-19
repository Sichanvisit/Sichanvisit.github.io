---
title: "Mission 6 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_6_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_6_강사공유.md"
excerpt: "이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 작업을 수행합니다. 이번 미션의 목표는 X-Ray 사진을 입력으로 받아 폐렴 여부를 구분하는 분류(Classification) 모델을 만드는 것입니다. 아래 데이터셋을 활용하여 다양한 이미지 전..."
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
| Code Blocks | 38 |
| Execution Cells | 38 |
| Libraries | `os`, `math`, `glob`, `warnings`, `random`, `shutil`, `numpy`, `pandas` |
| Source Note | `Mission_6_강사공유` |

## What I Worked On

- 사전 설정
- 과제 요약
- @title Device 설정
- GPU 설정
- 1. 데이터 분석

## Implementation Flow

1. 사전 설정
2. 과제 요약
3. @title Device 설정
4. GPU 설정
5. 1. 데이터 분석
6. 데이터

## Code Highlights

### 과제 요약

```python
import os
import math
import glob
import warnings
import random
import shutil

import numpy as np
import pandas as pd
import cv2

import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance, ImageFilter

from sklearn.metrics import classification_report

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, random_split
from torch.utils.data.sampler import WeightedRandomSampler
from torchinfo import summary

import torchvision
import torchvision.models as models
import torchvision.transforms.v2 as v2
from torchvision import transforms, datasets
# ... trimmed ...
```

### 4. 기본 모델 학습

```python
# @title 학습 함수 정의

from tqdm import tqdm
# import torch_xla.distributed.parallel_loader as pl

def train_epoch(model, dataloader, criterion, optimizer, device):
    model.train()
    model.to(device)
    running_loss = 0.
    correct = 0.
    total = 0.

    # para_train_loader = pl.ParallelLoader(dataloader, [device]).per_device_loader(device)

    for inputs, labels in tqdm(dataloader, leave=False, desc="Train"):
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        # xm.optimizer_step(optimizer)  # 이부분이 TPU 쓸때 필요한 코드!!
        optimizer.step()

        running_loss += (loss.item() * inputs.size(0)) # 배치당 평균 손실 x 배치 사이즈 --> 배치 내 모든 샘플의 손실 총합
        _, preds = torch.max(outputs, 1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)

# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/Mission_6_강사공유.md`
- Source formats: `md`
- Companion files: `Mission_6_강사공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `www.codeit.kr`, `localhost`

## Note Preview

> 이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 작업을 수행합니다. 이번 미션의 목표는 X-Ray 사진을 입력으로 받아 폐렴 여부를 구분하는 분류(Classification) 모델을 만드는 것입니다. 아래 데이터셋을 활용하여 다양한 이미지 전처리 및 증강 기법과 Transfer Learning과 Fine-Tuning 기법을 실험해보고, 모델의 성능을 평가해 보세요.
> 데이터 링크
