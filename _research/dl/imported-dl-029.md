---
title: ".사전훈련된 모델 활용"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "5-1.사전훈련된 모델 활용"
source_path: "12_Deep_Learning/Code_Snippets/5-1.사전훈련된 모델 활용.md"
excerpt: ".사전훈련된 모델 활용에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 코드 설명 순서로 핵심 장면을 먼저 훑고, 코드 설명 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 16개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐..."
research_summary: ".사전훈련된 모델 활용에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 코드 설명 순서로 핵심 장면을 먼저 훑고, 코드 설명 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 16개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 16개 · 실행 13개"
code_block_count: 16
execution_block_count: 13
research_focus:
  - "코드 설명"
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

.사전훈련된 모델 활용에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 코드 설명 순서로 핵심 장면을 먼저 훑고, 코드 설명 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 16개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: 코드 설명.

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

CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다. MNIST 데이터 전처리: MNIST 이미지를 32×32, 3채널로 변환하여 CIFAR-100 모델에 맞게 전처리합니다.

- 읽을 포인트: 코드 설명 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

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

1. 코드 설명: CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다. MNIST 데이터 전처리: MNIST 이미지를 32×32, 3채널로 변환하여 CIFAR-100 모델에 맞게 전처리...

## Code Highlights

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

### 코드 설명

`코드 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 MNIST 데이터 전처리 (공통) 흐름이 주석과 함께 드러납니다.

```python
# --------------------------------------------------
# MNIST 데이터 전처리 (공통)
# --------------------------------------------------
transform_mnist = transforms.Compose([
    transforms.Resize(32),  # CIFAR-100 모델 입력 크기에 맞춤
    transforms.Grayscale(num_output_channels=3),  # 3채널로 변환
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5],
                         std=[0.5, 0.5, 0.5])
])
mnist_full = torchvision.datasets.MNIST(root='./data', train=True, transform=transform_mnist, download=True)

mnist_train_size = int(0.9 * len(mnist_full))
mnist_val_size = len(mnist_full) - mnist_train_size

mnist_train, mnist_val = random_split(mnist_full, [mnist_train_size, mnist_val_size])
mnist_train_loader = DataLoader(mnist_train, batch_size=128, shuffle=True, num_workers=2)
mnist_val_loader = DataLoader(mnist_val, batch_size=128, shuffle=False, num_workers=2)
```

### 코드 설명

`코드 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 MNIST Full Fine-tuning (전체 레이어 업데이트), MNIST 모델 생성 (우선 CIFAR-100 구조로 생성), CIFAR-100 사전학습된 feature extractor 로드 (features 부분... 흐름이 주석과 함께 드러납니다.

```python
# --------------------------------------------------
# 1. MNIST Full Fine-tuning (전체 레이어 업데이트)
# --------------------------------------------------
print("\n==== MNIST Full Fine-tuning (전체 레이어 업데이트) ====")
# MNIST 모델 생성 (우선 CIFAR-100 구조로 생성)
model_mnist_ft = SimpleCNN().to(device)

# CIFAR-100 사전학습된 feature extractor 로드 (features 부분만 복사)
model_cifar_dict = torch.load('./models/model_cifar100.pth', map_location=device)

model_dict = model_mnist_ft.state_dict()

pretrained_dict = {k: v for k, v in model_cifar_dict.items() if k.startswith("features")}

model_dict.update(pretrained_dict)
model_mnist_ft.load_state_dict(model_dict)


# classifier 교체: 마지막 레이어를 MNIST 분류(10 클래스)에 맞게 변경
model_mnist_ft.classifier[3] = nn.Linear(256, 10).to(device)
print("MNIST Full Fine-tuning 모델:", model_mnist_ft)


# 전체 파라미터 업데이트하므로 feature extractor 고정하지 않음.
# 전체 모델에 대해 작은 학습률 적용 (예: 1e-4)
optimizer_mnist_ft = optim.Adam(model_mnist_ft.parameters(), lr=1e-4)

# metric 저장을 위한 리스트 초기화 (Full Fine-tuning)
# ... trimmed ...
```

### 코드 설명

`코드 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 MNIST Feature Extraction (classifier만 업데이트), MNIST 모델 생성 (초기 CIFAR-100 구조로 생성), feature extractor 고정 흐름이 주석과 함께 드러납니다.

```python
# --------------------------------------------------
# 2. MNIST Feature Extraction (classifier만 업데이트)
# --------------------------------------------------
print("\n==== MNIST Feature Extraction (Classifier 학습) ====")

# MNIST 모델 생성 (초기 CIFAR-100 구조로 생성)
model_mnist_fe = SimpleCNN().to(device)
model_dict_fe = model_mnist_fe.state_dict()
pretrained_dict_fe = {k: v for k, v in model_cifar_dict.items() if k.startswith("features")}
model_dict_fe.update(pretrained_dict_fe)
model_mnist_fe.load_state_dict(model_dict_fe)

# feature extractor 고정
for param in model_mnist_fe.features.parameters():
    param.requires_grad = False

# feature extractor 고정 확인
for name, param in model_mnist_fe.named_parameters():
    print(f"{name}: ", param.requires_grad)
print("\n")

# classifier 교체: 새 분류기로 재정의 (예: 중간층 축소)
model_mnist_fe.classifier = nn.Sequential(
    nn.Linear(128 * 4 * 4, 128),
    nn.ReLU(),
    nn.Linear(128, 10)
).to(device)

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
