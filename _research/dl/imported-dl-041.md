---
title: "cGAN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "8-3_cGAN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/8-3_cGAN - 공유.md"
excerpt: "DL Shared Note: 예시를 위한 설정, 임의의 이미지 텐서 (여기서는 값은 임의로 생성), 예시 라벨: [0, 1, 0, 0]"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 5 |
| Execution Cells | 3 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy` |
| Source Note | `8-3_cGAN - 공유` |

## What I Worked On

- 예시를 위한 설정
- 임의의 이미지 텐서 (여기서는 값은 임의로 생성)
- 예시 라벨: [0, 1, 0, 0]
- 임베딩 레이어 정의: 각 클래스당 1차원 벡터 (실제 학습 시엔 임의의 값으로 초기화됨)
- 예시를 위해 임베딩 가중치를 고정(쉽게 이해하기 위해)

## Implementation Flow

1. 예시를 위한 설정
2. 임의의 이미지 텐서 (여기서는 값은 임의로 생성)
3. 예시 라벨: [0, 1, 0, 0]
4. 임베딩 레이어 정의: 각 클래스당 1차원 벡터 (실제 학습 시엔 임의의 값으로 초기화됨)
5. 예시를 위해 임베딩 가중치를 고정(쉽게 이해하기 위해)
6. 클래스 0은 값 0.5, 클래스 1은 값 -0.5라고 가정해보겠습니다.

## Code Highlights

### @title ##### 텐서 차원 맞추기 연습 #####

```python
#@title ##### 텐서 차원 맞추기 연습 #####

import torch
import torch.nn as nn

# 예시를 위한 설정
image_size = 4   # 시각화를 위해 간단한 4x4 이미지로 가정
num_classes = 2  # 예시에서는 0과 1, 두 개의 클래스만 사용
batch_size = 5   # 배치 크기 4

# 임의의 이미지 텐서 (여기서는 값은 임의로 생성)
img = torch.randn(batch_size, 1, image_size, image_size)
# 예시 라벨: [0, 1, 0, 0]
labels = torch.tensor([0, 1, 0, 0, 1])
print("원본 라벨:", labels)  # tensor([0, 1, 0, 0, 1])

# 임베딩 레이어 정의: 각 클래스당 1차원 벡터 (실제 학습 시엔 임의의 값으로 초기화됨)
label_emb = nn.Embedding(num_classes, 1)
# 예시를 위해 임베딩 가중치를 고정(쉽게 이해하기 위해)
# 클래스 0은 값 0.5, 클래스 1은 값 -0.5라고 가정해보겠습니다.
with torch.no_grad():
    label_emb.weight[0] = torch.tensor([0.5])
    label_emb.weight[1] = torch.tensor([-0.5])

# 1. 라벨 임베딩
embedded = label_emb(labels)
print("임베딩 결과 (shape):", embedded.shape)
print("임베딩 결과 (값):", embedded)
# ... trimmed ...
```

### import torch

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

# device 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 데이터셋 및 DataLoader 설정
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # [-1, 1] 범위로 정규화
])

# MNIST 데이터셋 사용
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset  = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader  = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)

# 클래스 이름 (MNIST는 0~9 숫자)
idx_to_class = {i: str(i) for i in range(10)}
print(idx_to_class)

# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/8-3_cGAN - 공유.md`
- Source formats: `md`
- Companion files: `8-3_cGAN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> -
