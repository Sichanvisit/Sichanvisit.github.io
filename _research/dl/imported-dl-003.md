---
title: "CNN 이미지 분류1"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)CNN_이미지 분류1"
source_path: "12_Deep_Learning/Code_Snippets/(실습)CNN_이미지 분류1.md"
excerpt: "풀링 레이어는 데이터를 다운샘플링하여 크기를 줄이고, 중요한 정보를 추출합니다. 맥스 풀링(Max Pooling): 윈도우 내 최댓값 선택. - 애버리지 풀링(Average Pooling): 윈도우 내 평균값 선택. 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (..."
research_summary: "풀링 레이어는 데이터를 다운샘플링하여 크기를 줄이고, 중요한 정보를 추출합니다. 맥스 풀링(Max Pooling): 윈도우 내 최댓값 선택. - 애버리지 풀링(Average Pooling): 윈도우 내 평균값 선택. 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포). `md` 원본과 76개 코드 블록, 72개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다."
research_artifacts: "md · 코드 76개 · 실행 72개"
code_block_count: 76
execution_block_count: 72
research_focus:
  - "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다."
  - "학습 데이터"
  - "데이터셋"
research_stack:
  - "numpy"
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "types"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

풀링 레이어는 데이터를 다운샘플링하여 크기를 줄이고, 중요한 정보를 추출합니다. 맥스 풀링(Max Pooling): 윈도우 내 최댓값 선택. - 애버리지 풀링(Average Pooling): 윈도우 내 평균값 선택. 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포). `md` 원본과 76개 코드 블록, 72개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋..., 학습 데이터, 데이터셋.

**남겨둔 자료**: `md` 원본과 76개 코드 블록, 72개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**주요 스택**: `numpy`, `torch`, `torchvision`, `matplotlib`, `types`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 76 |
| Execution Cells | 72 |
| Libraries | `numpy`, `torch`, `torchvision`, `matplotlib`, `types`, `PIL`, `torchinfo`, `sklearn` |
| Source Note | `(실습)CNN_이미지 분류1` |

## What This Note Covers

### Overview

Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.

### 데이터셋

학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)

### 클래스 정보

0번부터 9번까지 다음과 같은 패션 아이템으로 구성됩니다 0: T-shirt/top - 1: Trouser - 2: Pullover - 3: Dress - 4: Coat - 5: Sandal - 6: Shirt - 7: Sneaker - 8: Bag - 9: Ankle boot

### CNN 모델에 사용되는 레이어 > 주요 파라미터

in_channels: 입력 데이터의 채널 수. - out_channels: 출력 데이터의 채널 수 = 필터 개수. - kernel_size: 필터 크기. (정사각형) - stride: 필터 이동 간격. (기본값: 1) - padding: 입력 가장자리를 채워 크기를 조정. - 0: 패딩 없음 (valid), - 1: 출력 크기 = 입력 크기 (same은 스트라이드 1에서만 적용 가능).

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

1. Overview: Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.
2. 데이터셋: 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)
3. 클래스 정보: 0번부터 9번까지 다음과 같은 패션 아이템으로 구성됩니다 0: T-shirt/top - 1: Trouser - 2: Pullover - 3: Dress - 4: Coat - 5: Sandal - 6: Shirt - 7: Sneaker - 8: Bag - 9: Ankle boot
4. CNN 모델에 사용되는 레이어 > 주요 파라미터: in_channels: 입력 데이터의 채널 수. - out_channels: 출력 데이터의 채널 수 = 필터 개수. - kernel_size: 필터 크기. (정사각형) - stride: 필터 이동 간격. (기본값: 1) - padding: 입력 가장...

## Code Highlights

### DNN 모델

`DNN 모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 GPU 설정, 데이터셋 로드 + 전처리, uint8 --> float32 흐름이 주석과 함께 드러납니다.

```python
from types import CoroutineType
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# GPU 설정
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using Device : {device}")

# 데이터셋 로드 + 전처리
transforms = v2.Compose(
    [
        v2.ToImage(), # PIL -> Tensor (TV Tensor Image)
        v2.ToDtype(dtype=torch.float32, scale=True) #dtype변환 , 값을 0~1로 설정
        # uint8 --> float32
    ]
)

# 데이터 셋 생성 + transforms 적용
train_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=True,
    download=True,
    transform=transforms
)
# ... trimmed ...
```

### CNN 모델 만들기

`CNN 모델 만들기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실험의 중심이 되는 모델 아키텍처를 정의하는 코드입니다.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1,32,3,1,1)
        self.conv2 = nn.Conv2d(32,64,3,1,1)
        self.maxpool = nn.MaxPool2d(2,2)
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(64*7*7, 64)
        self.linear2 = nn.Linear(64, 10)

    def _func1(self,x):
        return x*x
        pass

    def func2(self,x):
        y = self._func1(x)
        print(y)

    def forward(self, x):
        x = F.relu(self.conv1(x))   # conv+relu (b,1,28,28) -> (b,32,28,28)
        x = self.maxpool(x)         # maxpool   (b,32,28,28)-> (b,32,14,14)
        x = F.relu(self.conv2(x))   # conv+relu (b,32,14,14)-> (b,64,14,14)
        x = self.maxpool(x)         # maxpool   (b,64,14,14)-> (b,64,7,7)

# ... trimmed ...
```

### CNN 모델 학습

`CNN 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 device 설정, 모델 준비, ch 1->32->pool->64->pool->flatten->64->10 흐름이 주석과 함께 드러납니다.

```python
# device 설정
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using Device : {device}")

#모델 준비
class CNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        # ch 1->32->pool->64->pool->flatten->64->10
        self.conv1 = nn.Conv2d(1,32,3,1,1)
        self.conv2 = nn.Conv2d(32,64,3,1,1)
        self.maxpool = nn.MaxPool2d(2,2)
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(64*7*7, 64)
        self.linear2 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.maxpool(x)
        x = F.relu(self.conv2(x))
        x = self.maxpool(x)

        x = self.flatten(x)
        x = F.relu(self.linear1(x))
        output = self.linear2(x)
        return output

model = CNNModel().to(device)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)CNN_이미지 분류1.md`
- Source formats: `md`
- Companion files: `(실습)CNN_이미지 분류1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> Fashion MNIST는 다양한 **패션 아이템 이미지**가 포함된 데이터셋입니다.
> - **학습 데이터**: 6만 개 - **테스트 데이터**: 1만 개 - **이미지 크기**: 28×28 (그레이스케일) - **클래스**: 총 10개 (각 클래스에 데이터 균등 분포)
