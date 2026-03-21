---
title: "Mission 5 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_5_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_5_강사공유.md"
excerpt: "num_images_in_item = len(dataset[index]) fig, axes = plt.subplots(num_images_to_show, num_images_in_item, figsize=(num_images_in_item * 5, num_images_to_show * 3)). if..."
research_summary: "num_images_in_item = len(dataset[index]) fig, axes = plt.subplots(num_images_to_show, num_images_in_item, figsize=(num_images_in_item * 5, num_images_to_show * 3)). if num_images_to_show == 1 and num_images_in_item == 1: axes = np.array([[axes]]) elif num_images_to_show == 1: axes = np.array([axes]) elif num_images_in_item == 1: axes = np.array(axes)... `md` 원본과 44개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, numpy, cv2입니다."
research_artifacts: "md · 코드 44개 · 실행 12개"
code_block_count: 44
execution_block_count: 12
research_focus:
  - "사전처리"
  - "파일 위치 주소 관련"
  - "import 추가"
research_stack:
  - "os"
  - "torch"
  - "numpy"
  - "cv2"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

num_images_in_item = len(dataset[index]) fig, axes = plt.subplots(num_images_to_show, num_images_in_item, figsize=(num_images_in_item * 5, num_images_to_show * 3)). if num_images_to_show == 1 and num_images_in_item == 1: axes = np.array([[axes]]) elif num_images_to_show == 1: axes = np.array([axes]) elif num_images_in_item == 1: axes = np.array(axes)... `md` 원본과 44개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, numpy, cv2입니다.

**빠르게 볼 수 있는 포인트**: 사전처리, 파일 위치 주소 관련, import 추가.

**남겨둔 자료**: `md` 원본과 44개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, numpy, cv2입니다.

**주요 스택**: `os`, `torch`, `numpy`, `cv2`, `matplotlib`

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

## What This Note Covers

### 사전처리 > import 추가

파일 위치 주소 관련 : os - torch : torch, torch.nn, torch.optim. torch.nn.functional - torch.utils.data : Dataset, DataLoader, random_split - torchvision : torchvision.transform, v2

### 사전처리 > device 설정

* CUDA gpu가 있는 경우 cuda로 디바이스 설정 * mac - Apple 실리콘의 gpu 사용을 위해 mps 설정추가

### 데이터 처리 > 데이터 설정

* 데이터 매인 폴더와 데이터 파일 리스트 생성 * 데이터 길이와 내용 일부 확인 * Train dataset 크기와 Val dataset 크기 설정

### 데이터 처리 > Image Size check 함수

* 이미지 file 리스트를 입력해 이미지의 shape 리스트 확인 * unique를 통해 중복 제거 def check_image_shapes(image_paths): shapes = [] for path in image_paths: img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) if img is not None: shapes.append(img.sha...

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. 사전처리 > import 추가: 파일 위치 주소 관련 : os - torch : torch, torch.nn, torch.optim. torch.nn.functional - torch.utils.data : Dataset, DataLoader, random_split - torchvision : t...
2. 사전처리 > device 설정: * CUDA gpu가 있는 경우 cuda로 디바이스 설정 * mac - Apple 실리콘의 gpu 사용을 위해 mps 설정추가
3. 데이터 처리 > 데이터 설정: * 데이터 매인 폴더와 데이터 파일 리스트 생성 * 데이터 길이와 내용 일부 확인 * Train dataset 크기와 Val dataset 크기 설정
4. 데이터 처리 > Image Size check 함수: * 이미지 file 리스트를 입력해 이미지의 shape 리스트 확인 * unique를 통해 중복 제거 def check_image_shapes(image_paths): shapes = [] for path in image_paths: img =...

## Code Highlights

### import 추가

`import 추가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 파일 위치 주소 관련 : os - torch : torch, torch.nn, torch.optim. torch.nn.functional - torch.utils.data : Dataset, DataLoader, random_split - torchvision : torchvision.transform, v2.

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

### Transform 설정

`Transform 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. * PadToSize class를 적용할 수 있음.

```python
transform_train = v2.Compose(
    [
        v2.ToImage(),
        v2.ToDtype(torch.float32, scale=True),
        v2.Normalize(mean=[0], std=[1.0]),
        v2.RandomRotation(10),
        v2.RandomHorizontalFlip(),
        v2.RandomVerticalFlip(),
        Grayscale(),
        PadToSize(target_size=set_size),
    ]
)
transform_test = v2.Compose(
    [
        v2.ToImage(),
        v2.ToDtype(torch.float32, scale=True),
        v2.Normalize(mean=[0], std=[1.0]),
        Grayscale(),
        PadToSize(target_size=set_size),

    ]
)
```

### DataSet Class

`DataSet Class`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. * Train 이미지와 Train_cleaned 데이터를 pair로 묶어 데이터 셋 설정 * 입력으로 이미지 파일 리스트와 transform 추가 * pad to size 함수를 입력으로 받아와 처리.

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
