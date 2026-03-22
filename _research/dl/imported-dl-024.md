---
title: "CNN 이미지 분류 part1 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-2_CNN_이미지 분류_part1 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-2_CNN_이미지 분류_part1 - 공유.md"
excerpt: "CNN 이미지 분류 part1 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 이미지 데이터 전처리하기, 데이터 소개, DNN 모델 순서로 핵심 장면을 먼저 훑고, 여러 전처리 묶기 : Compose, 데이터셋 생성 시 전처리 적용, DNN..."
research_summary: "CNN 이미지 분류 part1 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 이미지 데이터 전처리하기, 데이터 소개, DNN 모델 순서로 핵심 장면을 먼저 훑고, 여러 전처리 묶기 : Compose, 데이터셋 생성 시 전처리 적용, DNN 모델 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 29개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다."
research_artifacts: "md · 코드 29개 · 실행 16개"
code_block_count: 29
execution_block_count: 16
research_focus:
  - "이미지 데이터 전처리하기"
  - "데이터 소개"
  - "DNN 모델"
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

CNN 이미지 분류 part1 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 이미지 데이터 전처리하기, 데이터 소개, DNN 모델 순서로 핵심 장면을 먼저 훑고, 여러 전처리 묶기 : Compose, 데이터셋 생성 시 전처리 적용, DNN 모델 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 29개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: 이미지 데이터 전처리하기, 데이터 소개, DNN 모델.

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

### 이미지 데이터 전처리하기

Fashion MNIST 데이터셋을 대상으로 전처리 과정을 진행하며, 텐서 변환, 스케일링, 표준화, 그리고 전처리를 데이터셋에 적용하는 방법을 살펴봅니다. Fashion MNIST 데이터를 불러오면 이미지가 Pillow(PIL) 형식으로 제공됩니다.

- 읽을 포인트: 세부 흐름: 데이터 타입 변환 및 스케일링, 여러 전처리 묶기 : Compose, 데이터셋 생성 시 전처리 적용

#### 데이터 타입 변환 및 스케일링

딥러닝 모델 학습을 위해 픽셀값을 0~1 범위의 실수(float)로 변환해야 합니다. dtype: 텐서의 데이터 타입(예: torch.float32). - scale=True: 픽셀값을 0~1로 스케일링.

#### 여러 전처리 묶기 : Compose

이미지 입력을 배치로 묶고 증강하며 학습 가능한 형태로 만드는 구간입니다.

#### 데이터셋 생성 시 전처리 적용

Fashion MNIST 데이터셋을 생성할 때, 전처리(transform)를 바로 적용할 수 있습니다.

### 데이터 소개

Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.

- 읽을 포인트: 세부 흐름: 데이터셋 특징, 데이터 불러오기, 데이터 구조

#### 데이터셋 특징

학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)

#### 데이터 불러오기

PyTorch의 TorchVision 라이브러리 TorchVision은 PyTorch에서 제공하는 컴퓨터 비전용 라이브러리입니다. - 다양한 데이터셋, 모델, 이미지 전처리 및 증강 기능을 지원합니다. - 이번 강의에서는 TorchVision의 datasets 모듈을 활용합니다.

#### 데이터 구조

각 데이터는 튜플 형태: 1. 이미지 데이터 (PIL.Image 객체) 2. 레이블 (정수 값) 입력값: 이미지 데이터(image), 클래스 레이블(label). - 출력값: 이미지를 그레이스케일로 시각화하며, 클래스 이름 표시.

### DNN 모델

DNN 모델 코드를 직접 따라가며 DNN 모델 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### CNN 모델에 사용되는 레이어

Conv2d, Conv2d > 주요 파라미터, Conv2d > 출력 형태 같은 코드를 직접 따라가며 CNN 모델에 사용되는 레이어 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Conv2d, Conv2d > 주요 파라미터, Conv2d > 출력 형태

#### Conv2d

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

#### Conv2d > 주요 파라미터

in_channels: 입력 데이터의 채널 수. - out_channels: 출력 데이터의 채널 수 = 필터 개수. - kernel_size: 필터 크기. (정수 → 정사각형, 튜플 → 직사각형 가능) - stride: 필터 이동 간격. (기본값: 1) - padding: 입력 가...

#### Conv2d > 출력 형태

배치 크기: 동일 (2) - 채널 수: out_channels (32) - 높이와 너비: 필터 크기, 패딩, 스트라이드에 따라 변화.

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

1. 이미지 데이터 전처리하기: 데이터 타입 변환 및 스케일링, 여러 전처리 묶기 : Compose
2. 데이터 소개: 데이터셋 특징, 데이터 불러오기
3. DNN 모델: DNN 모델 코드를 직접 따라가며 DNN 모델 흐름을 확인했습니다.
4. CNN 모델에 사용되는 레이어: Conv2d, Conv2d > 주요 파라미터

## Code Highlights

### 여러 전처리 묶기 : Compose

`여러 전처리 묶기 : Compose`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 compose 적용, 결과 확인 흐름이 주석과 함께 드러납니다.

```python
# compose 적용
image_tensor_compose = transforms(image_pil)

# 결과 확인
print(f'type: {type(image_tensor_compose)}')  # torchvision.tv_tensors._image.Image
print(f'dtype: {image_tensor_compose.dtype}')  # torch.float32
print(f'max: {image_tensor_compose.max()}')  # 1.0
print(f'min: {image_tensor_compose.min()}')  # 0.0
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

### 기본 설정

`기본 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실험의 중심이 되는 모델 아키텍처를 정의하는 코드입니다.

```python
conv_layer = nn.Conv2d(
    in_channels=3,  # 입력 채널 수 (예: RGB 이미지면 3)
    out_channels=32,  # 출력 채널 수 (필터 개수)
    kernel_size=3,  # 커널 크기 (3x3 필터)
    stride=1,  # 필터 이동 간격
    padding=0,  # 입력 가장자리 패딩 크기
)
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
