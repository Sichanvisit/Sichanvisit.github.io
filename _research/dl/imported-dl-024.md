---
title: "CNN 이미지 분류 part1 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-2_CNN_이미지 분류_part1 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-2_CNN_이미지 분류_part1 - 공유.md"
excerpt: "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다"
research_summary: "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다. 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포). `md` 원본과 29개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다."
research_artifacts: "md · 코드 29개 · 실행 16개"
code_block_count: 29
execution_block_count: 16
research_focus:
  - "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다."
  - "데이터 소개"
  - "학습 데이터"
research_stack:
  - "numpy"
  - "torch"
  - "torchvision"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다. 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포). `md` 원본과 29개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋..., 데이터 소개, 학습 데이터.

**남겨둔 자료**: `md` 원본과 29개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**주요 스택**: `numpy`, `torch`, `torchvision`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 29 |
| Execution Cells | 16 |
| Libraries | `numpy`, `torch`, `torchvision`, `matplotlib` |
| Source Note | `4-2_CNN_이미지 분류_part1 - 공유` |

## What This Note Covers

### 데이터 소개

Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.

### 데이터셋 특징

학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)

### 클래스 정보

0번부터 9번까지 다음과 같은 패션 아이템으로 구성됩니다

### 데이터 불러오기

TorchVision은 PyTorch에서 제공하는 컴퓨터 비전용 라이브러리입니다. - 다양한 데이터셋, 모델, 이미지 전처리 및 증강 기능을 지원합니다. - 이번 강의에서는 TorchVision의 datasets 모듈을 활용합니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. 데이터 소개: Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.
2. 데이터셋 특징: 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)
3. 클래스 정보: 0번부터 9번까지 다음과 같은 패션 아이템으로 구성됩니다
4. 데이터 불러오기: TorchVision은 PyTorch에서 제공하는 컴퓨터 비전용 라이브러리입니다. - 다양한 데이터셋, 모델, 이미지 전처리 및 증강 기능을 지원합니다. - 이번 강의에서는 TorchVision의 datasets 모듈을 활용합니다.

## Code Highlights

### 데이터 구조

`데이터 구조`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 시각화 흐름이 주석과 함께 드러납니다.

```python
# 시각화
import matplotlib.pyplot as plt

def visualize_data(image, label):
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    plt.figure(figsize=(1,1))
    plt.imshow(image, cmap='gray')
    plt.xlabel(class_names[label])
    plt.show()
```

### 데이터셋 생성 시 전처리 적용

`데이터셋 생성 시 전처리 적용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. Fashion MNIST 데이터셋을 생성할 때, 전처리(transform)를 바로 적용할 수 있습니다.

```python
train_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=True,
    download=True,
    transform=transforms,
)

test_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=False,
    download=True,
    transform=transforms,
)
```

### DNN 모델

`DNN 모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋 로드 및 전처리, GPU 설정, DNN 모델 정의 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# 데이터셋 로드 및 전처리
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # 픽셀 값을 [-1, 1]로 정규화
])

train_dataset = datasets.FashionMNIST(
    root="./data", train=True, transform=transform, download=True
)
test_dataset = datasets.FashionMNIST(
    root="./data", train=False, transform=transform, download=True
)

train_dataloader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# GPU 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# DNN 모델 정의
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/4-2_CNN_이미지 분류_part1 - 공유.md`
- Source formats: `md`
- Companion files: `4-2_CNN_이미지 분류_part1 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> Fashion MNIST는 다양한 **패션 아이템 이미지**가 포함된 데이터셋입니다.
> - **학습 데이터**: 6만 개 - **테스트 데이터**: 1만 개 - **이미지 크기**: 28×28 (그레이스케일) - **클래스**: 총 10개 (각 클래스에 데이터 균등 분포)
