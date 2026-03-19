---
title: "Mission 6 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_6_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_6_강사공유.md"
excerpt: "이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 작업을 수행합니다"
research_summary: "이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 작업을 수행합니다. 이번 미션의 목표는 X-Ray 사진을 입력으로 받아 폐렴 여부를 구분하는 분류(Classification) 모델을 만드는 것입니다. 아래 데이터셋을 활용하여 다양한 이미지 전처리 및 증강 기법과 Transfer Learning과 Fine-Tuni... * 본 프로젝트는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 분류 모델 개발을 목표 * 다양한 이미지 전처리 및 증강 기법을 적용하고, Transfer Learning 및 Fine-Tuning 기법을 활용하여 모델 성능을 평가. `md` 원본과 38개 코드 블록, 38개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, math, glob, warnings입니다."
research_artifacts: "md · 코드 38개 · 실행 38개"
code_block_count: 38
execution_block_count: 38
research_focus:
  - "사전 설정"
  - "이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 작업을 수행합니다. 이번 미션의..."
  - "과제 요약"
research_stack:
  - "os"
  - "math"
  - "glob"
  - "warnings"
  - "random"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 작업을 수행합니다. 이번 미션의 목표는 X-Ray 사진을 입력으로 받아 폐렴 여부를 구분하는 분류(Classification) 모델을 만드는 것입니다. 아래 데이터셋을 활용하여 다양한 이미지 전처리 및 증강 기법과 Transfer Learning과 Fine-Tuni... * 본 프로젝트는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 분류 모델 개발을 목표 * 다양한 이미지 전처리 및 증강 기법을 적용하고, Transfer Learning 및 Fine-Tuning 기법을 활용하여 모델 성능을 평가. `md` 원본과 38개 코드 블록, 38개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, math, glob, warnings입니다.

**빠르게 볼 수 있는 포인트**: 사전 설정, 이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는..., 과제 요약.

**남겨둔 자료**: `md` 원본과 38개 코드 블록, 38개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, math, glob, warnings입니다.

**주요 스택**: `os`, `math`, `glob`, `warnings`, `random`

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

## What This Note Covers

### 과제 요약

이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 작업을 수행합니다. 이번 미션의 목표는 X-Ray 사진을 입력으로 받아 폐렴 여부를 구분하는 분류(Classification) 모델을 만드는 것입니다. 아래 데이터셋을 활용하여 다양한 이미지 전처리 및 증강 기법과 Transfer Learning과 Fine-Tuning 기법을 실험해보고, 모델의 성능을 평가해 보세요.

### 목적

* 본 프로젝트는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 분류 모델 개발을 목표 * 다양한 이미지 전처리 및 증강 기법을 적용하고, Transfer Learning 및 Fine-Tuning 기법을 활용하여 모델 성능을 평가

### 데이터셋

* 본 프로젝트에서는 Chest X-Ray Images (Pneumonia) 데이터셋을 사용하며, 데이터는 훈련(train), 검증(val), 테스트(test)로 구성되어 있다.

### Feature Extraction

* ResNet-18 이용하여 전이 학습

## Implementation Flow

1. 과제 요약: 이번 미션에서는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 작업을 수행합니다. 이번 미션의 목표는 X-Ray 사진을 입력으로 받아 폐렴 여부를 구분하는 분류(Classification) 모델을 만드는 것입니다. 아래 데이터셋을 활용하여 다양한 이미지 전처리 및 증강 기법과 T...
2. 목적: * 본 프로젝트는 흉부 X-Ray 사진을 바탕으로 폐렴 환자를 구분하는 분류 모델 개발을 목표 * 다양한 이미지 전처리 및 증강 기법을 적용하고, Transfer Learning 및 Fine-Tuning 기법을 활용하여 모델 성능을 평가
3. 데이터셋: * 본 프로젝트에서는 Chest X-Ray Images (Pneumonia) 데이터셋을 사용하며, 데이터는 훈련(train), 검증(val), 테스트(test)로 구성되어 있다.
4. Feature Extraction: * ResNet-18 이용하여 전이 학습

## Code Highlights

### 과제 요약

`과제 요약`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다.

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

### 기본 모델 학습

`기본 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 함수 정의, import torch_xla.distributed.parallel_loader as pl, para_train_loader = pl.ParallelLoader(dataloader,... 흐름이 주석과 함께 드러납니다.

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
