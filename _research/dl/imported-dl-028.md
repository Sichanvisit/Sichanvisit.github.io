---
title: "Autoencoder - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-6_Autoencoder - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-6_Autoencoder - 공유.md"
excerpt: "DL Shared Note: 1. 기본적인 오토인코더 구현 실습(MNIST), 라이브러리 불러오기, 데이터 불러오기"
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
| Code Blocks | 23 |
| Execution Cells | 23 |
| Libraries | `numpy`, `matplotlib`, `torch`, `torchvision`, `mpl_toolkits`, `plotly` |
| Source Note | `4-6_Autoencoder - 공유` |

## What I Worked On

- 1. 기본적인 오토인코더 구현 실습(MNIST)
- 라이브러리 불러오기
- 데이터 불러오기
- train_dataset = datasets.MNIST(
- root='./mnist',

## Implementation Flow

1. 1. 기본적인 오토인코더 구현 실습(MNIST)
2. 라이브러리 불러오기
3. 데이터 불러오기
4. train_dataset = datasets.MNIST(
5. root='./mnist',
6. train=True,

## Code Highlights

### 차원축소와 시각화

```python
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets
from torch.utils.data import DataLoader
from torchvision.transforms import v2  # torchvision 0.14 이상에서 사용 가능
from mpl_toolkits.mplot3d import Axes3D  # 3D 시각화를 위해 필요

# 데이터 전처리 (버전 문제 시 transforms.ToTensor()로 대체 가능)
transform = v2.Compose([
    v2.ToImage(),
    v2.ToDtype(dtype=torch.float32, scale=True)
])

# MNIST 데이터셋 불러오기
train_dataset = datasets.MNIST(
    root='./mnist',
    train=True,
    download=True,
    transform=transform
)
test_dataset = datasets.MNIST(
    root='./mnist',
    train=False,
    download=True,
    transform=transform
# ... trimmed ...
```

### 차원축소와 시각화

```python
# latent 공간 시각화를 위한 데이터 추출
model.eval()
all_latents = []
all_labels = []
with torch.no_grad():
    for images, labels in test_dataloader:
        images = images.view(images.size(0), -1).to(device)
        # latent 벡터만 추출 (model.encode() 사용)
        latent = model.encode(images)
        all_latents.append(latent.cpu().numpy())
        all_labels.append(labels.cpu().numpy())

all_latents = np.concatenate(all_latents, axis=0)
all_labels = np.concatenate(all_labels, axis=0)

# 3D 시각화: 전체 분포와 일부 샘플에 텍스트 어노테이션 추가
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# 전체 latent 벡터에 대해 scatter plot (작은 크기와 낮은 불투명도로 분포 확인)
scatter = ax.scatter(all_latents[:, 0], all_latents[:, 1], all_latents[:, 2],
                     c=all_labels, cmap='tab10', s=10, alpha=0.3)

# 각 digit별로 일부 포인트만 선택하여 텍스트 어노테이션 추가
for digit in range(10):
    # 현재 클래스(digit)에 해당하는 인덱스 찾기
    indices = np.where(all_labels == digit)[0]
    # 전체 포인트 중 최대 50개를 무작위로 샘플링 (포인트가 50개 미만인 경우 전체 사용)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/4-6_Autoencoder - 공유.md`
- Source formats: `md`
- Companion files: `4-6_Autoencoder - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
