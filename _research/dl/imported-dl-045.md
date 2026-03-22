---
title: "GAN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "GAN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/GAN - 공유.md"
excerpt: "MNIST 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 MNIST 순서로 핵심 장면을 먼저 훑고, import torch, MNIST 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 6개 코드 블록, 3개 실..."
research_summary: "MNIST 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 MNIST 순서로 핵심 장면을 먼저 훑고, import torch, MNIST 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 6개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, os입니다."
research_artifacts: "md · 코드 6개 · 실행 3개"
code_block_count: 6
execution_block_count: 3
research_focus:
  - "MNIST"
research_stack:
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "os"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

MNIST 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 MNIST 순서로 핵심 장면을 먼저 훑고, import torch, MNIST 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 6개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, os입니다.

**빠르게 볼 수 있는 포인트**: MNIST.

**남겨둔 자료**: `md` 원본과 6개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, os입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `os`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 6 |
| Execution Cells | 3 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `os`, `numpy` |
| Source Note | `GAN - 공유` |

## What This Note Covers

### MNIST

MNIST 코드를 직접 따라가며 MNIST 흐름을 확인했습니다.

- 읽을 포인트: MNIST 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

## Implementation Flow

1. MNIST: MNIST 코드를 직접 따라가며 MNIST 흐름을 확인했습니다.

## Code Highlights

### import torch

`import torch`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, utils
from torchvision.utils import save_image
import matplotlib.pyplot as plt
import os
import numpy as np
```

### MNIST

`MNIST`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 MNIST 데이터셋 준비 및 DataLoader 설정 흐름이 주석과 함께 드러납니다.

```python
# MNIST 데이터셋 준비 및 DataLoader 설정
dataloader = torch.utils.data.DataLoader(
    datasets.MNIST('./data/mnist', train=True, download=True,
                   transform=transforms.Compose([
                       transforms.Resize(28),
                       transforms.ToTensor(),  # 데이터 [0,1]로 정규화
                       transforms.Normalize([0.5], [0.5])  # [-1, 1] 범위로 변환
                   ])),
    batch_size=64, shuffle=True)
```

### MNIST

`MNIST`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Generator 네트워크 정의 (생성기), Discriminator 네트워크 정의 (판별기) 흐름이 주석과 함께 드러납니다.

```python
# Generator 네트워크 정의 (생성기)
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(100, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.Linear(1024, 28*28),
            nn.Tanh()  # 출력값을 [-1, 1] 범위로 맞춤
        )

    def forward(self, z):
        return self.model(z).view(-1, 1, 28, 28)

# Discriminator 네트워크 정의 (판별기)
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(28*28, 1024),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2),
# ... trimmed ...
```

### MNIST

`MNIST`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 장치 설정 (GPU 사용 가능하면 GPU 사용), 생성기와 판별기 초기화, 옵티마이저 설정 (Adam 사용) 흐름이 주석과 함께 드러납니다.

```python
# 장치 설정 (GPU 사용 가능하면 GPU 사용)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 생성기와 판별기 초기화
generator = Generator().to(device)
discriminator = Discriminator().to(device)

# 옵티마이저 설정 (Adam 사용)
optimizer_G = optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

# 손실 함수: Binary Cross Entropy Loss 사용
criterion = nn.BCELoss()

# 에포크 수 설정
num_epochs = 100

# 평가를 위해 고정된 노이즈 벡터 생성 (이미지 생성 비교용)
fixed_noise = torch.randn(64, 100, device=device)

# 결과 저장을 위한 폴더 생성
os.makedirs('./images', exist_ok=True)
os.makedirs('./results', exist_ok=True)

# GAN 학습 루프 (에포크 단위)
for epoch in range(num_epochs):
    generator.train()
    discriminator.train()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/GAN - 공유.md`
- Source formats: `md`
- Companion files: `GAN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
