---
title: ".사전훈련된 모델 활용"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "5-1.사전훈련된 모델 활용"
source_path: "12_Deep_Learning/Code_Snippets/5-1.사전훈련된 모델 활용.md"
excerpt: "CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다"
research_summary: "CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 16개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 16개 · 실행 13개"
code_block_count: 16
execution_block_count: 13
research_focus:
  - "CIFAR-100 사전학습"
  - "코드 설명"
  - "이미지 시각화를 위한 함수 (단일 이미지 표시용)"
research_stack:
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "numpy"
  - "math"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 16개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: CIFAR-100 사전학습, 코드 설명, 이미지 시각화를 위한 함수 (단일 이미지 표시용).

**남겨둔 자료**: `md` 원본과 16개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `numpy`, `math`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 16 |
| Execution Cells | 13 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy`, `math`, `PIL`, `tqdm`, `os` |
| Source Note | `5-1.사전훈련된 모델 활용` |

## What This Note Covers

### 코드 설명

CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다.

### Key Step

이미지 시각화를 위한 함수 (단일 이미지 표시용)

### Key Step

CIFAR-100 데이터셋 (3채널 컬러 이미지, 32x32)

### Key Step

MNIST 데이터셋 (1채널 흑백 이미지, 28x28)

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. 코드 설명: CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다.
2. Key Step: 이미지 시각화를 위한 함수 (단일 이미지 표시용)
3. Key Step: CIFAR-100 데이터셋 (3채널 컬러 이미지, 32x32)
4. Key Step: MNIST 데이터셋 (1채널 흑백 이미지, 28x28)

## Code Highlights

### 코드 설명

`코드 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 이미지 시각화를 위한 함수 (단일 이미지 표시용), dataset.targets (또는 train_labels)를 통해 클래스 정보를 확인, sample에 이미지 추가 흐름이 주석과 함께 드러납니다.

```python
import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import math

# 이미지 시각화를 위한 함수 (단일 이미지 표시용)
def imshow(img, title=None, cmap=None):
    npimg = img.numpy()
    if npimg.shape[0] == 1:  # 흑백 이미지의 경우
        npimg = npimg[0]
    else:
        npimg = np.transpose(npimg, (1, 2, 0))
    plt.imshow(npimg, cmap=cmap)
    if title:
        plt.title(title)
    plt.axis('off')

def print_dataset_info(name, train_set, test_set):
    sample_img, sample_label = train_set[0]
    print(f"========== {name} ==========")
    print("Train 샘플 개수:", len(train_set))
    print("Test 샘플 개수:", len(test_set))
    print("샘플 이미지 텐서 shape:", sample_img.shape)  # (채널, 높이, 너비)
    if hasattr(train_set, 'classes'):
        print("클래스 (카테고리) 개수:", len(train_set.classes))
        print("클래스 이름:", train_set.classes)
# ... trimmed ...
```

### 코드 설명

`코드 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 MNIST 데이터셋에서 첫 번째 이미지 로드 (그레이스케일), 3채널 데이터로 변환, 방법 1: transforms.Grayscale(num_output_channels=3) 사용 흐름이 주석과 함께 드러납니다.

```python
import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# MNIST 데이터셋에서 첫 번째 이미지 로드 (그레이스케일)
mnist = datasets.MNIST(root='./data', train=True, download=True)
gray_img_array = mnist.data[0].numpy()  # shape: [28, 28]
gray_img_pil = Image.fromarray(gray_img_array, mode='L')  # PIL 이미지, 모드 'L' (그레이스케일)

# 3채널 데이터로 변환
# 방법 1: transforms.Grayscale(num_output_channels=3) 사용
transform_to3 = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor()
])
img_method1 = transform_to3(gray_img_pil)  # 텐서 shape: [3, 28, 28]

# 방법 2: PIL의 convert("RGB") 사용 후 ToTensor()
img_method2 = transforms.ToTensor()(gray_img_pil.convert("RGB"))  # 텐서 shape: [3, 28, 28]

# 두 결과의 차이 계산
diff = torch.abs(img_method1 - img_method2)
max_diff = diff.max().item()
mean_diff = diff.mean().item()

# ... trimmed ...
```

### 코드 설명

`코드 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 device 설정 (GPU가 있다면 사용), 모델 정의: 간단한 CNN (CIFAR-100 입력에 맞춤), 학습/검증 함수 정의 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
import torchvision
import torchvision.transforms as transforms
from tqdm import tqdm  # 진행 상황을 표시하기 위한 라이브러리
import os

# device 설정 (GPU가 있다면 사용)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("사용 device:", device)

# --------------------------------------------------
# 모델 정의: 간단한 CNN (CIFAR-100 입력에 맞춤)
# --------------------------------------------------
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),  # 3 -> 32 채널
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),  # 32x32 -> 16x16

            nn.Conv2d(32, 64, kernel_size=3, padding=1),  # 32 -> 64 채널
            nn.BatchNorm2d(64),
            nn.ReLU(),
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/5-1.사전훈련된 모델 활용.md`
- Source formats: `md`
- Companion files: `5-1.사전훈련된 모델 활용.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 1. **CIFAR-100 사전학습:** CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다.
> 2. **MNIST 데이터 전처리:** MNIST 이미지를 32×32, 3채널로 변환하여 CIFAR-100 모델에 맞게 전처리합니다.
