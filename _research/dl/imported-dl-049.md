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

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 평가 지표 해석

- 왜 필요한가: 정확도 하나만으로는 모델이 실제로 무엇을 잘하고 무엇을 놓치는지 충분히 설명할 수 없습니다.
- 왜 이 방식을 쓰는가: 문제 유형에 맞는 지표를 함께 보면 불균형 데이터, 오차 크기, 재현율 같은 중요한 관점을 놓치지 않을 수 있습니다.
- 원리: 예측 결과를 정답과 비교해 오차나 클래스별 성능을 수치화하고, 그 수치로 모델 선택과 개선 방향을 판단합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

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

### CNN 모델 정의

`CNN 모델 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기본 모델 정의, Custom CNN 모델 정의 흐름이 주석과 함께 드러납니다.

```python
# @title 기본 모델 정의
import torch
import torch.nn as nn
import torch.nn.functional as F

# Custom CNN 모델 정의
class CustomCNN(nn.Module):
    def __init__(self, num_classes=2):
        super(CustomCNN, self).__init__()

        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(64)

        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(128)
        self.conv4 = nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1)
        self.bn4 = nn.BatchNorm2d(128)

        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.global_avg_pool = nn.AdaptiveAvgPool2d((1, 1))

        self.fc1 = nn.Linear(128, 64)
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(64, num_classes)

    def forward(self, x):
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
