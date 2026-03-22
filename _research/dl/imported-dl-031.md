---
title: "VGGNet - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-4_VGGNet - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-4_VGGNet - 공유.md"
excerpt: "사전 훈련된 모델 활용, 실습 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 사전 훈련된 모델 활용, 실습 순서로 핵심 장면을 먼저 훑고, class VGG(nn.Module), 사전 훈련된 모델 활용, 실습 같은 코드로 실제 구현..."
research_summary: "사전 훈련된 모델 활용, 실습 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 사전 훈련된 모델 활용, 실습 순서로 핵심 장면을 먼저 훑고, class VGG(nn.Module), 사전 훈련된 모델 활용, 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 14개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, os, torchvision입니다."
research_artifacts: "md · 코드 14개 · 실행 11개"
code_block_count: 14
execution_block_count: 11
research_focus:
  - "사전 훈련된 모델 활용"
  - "실습"
research_stack:
  - "torch"
  - "torchinfo"
  - "os"
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

사전 훈련된 모델 활용, 실습 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 사전 훈련된 모델 활용, 실습 순서로 핵심 장면을 먼저 훑고, class VGG(nn.Module), 사전 훈련된 모델 활용, 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 14개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, os, torchvision입니다.

**빠르게 볼 수 있는 포인트**: 사전 훈련된 모델 활용, 실습.

**남겨둔 자료**: `md` 원본과 14개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, os, torchvision입니다.

**주요 스택**: `torch`, `torchinfo`, `os`, `torchvision`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 14 |
| Execution Cells | 11 |
| Libraries | `torch`, `torchinfo`, `os`, `torchvision`, `matplotlib`, `tqdm`, `collections`, `random` |
| Source Note | `5-4_VGGNet - 공유` |

## What This Note Covers

### 사전 훈련된 모델 활용

파이토치 : https://pytorch.org/vision/main/models.html#table-of-all-available-classification-weights - VGG-16 with ImageNet & BN : https://pytorch.org/vision/main/models/generated/torchvision...

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### 실습

데이터 셋 : https://pytorch.org/vision/main/generated/torchvision.datasets.OxfordIIITPet.html 데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을...

- 읽을 포인트: 세부 흐름: 출처

#### 출처

vgg-16 : https://pytorch.org/vision/0.8/_modules/torchvision/models/vgg.html

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. 사전 훈련된 모델 활용: 파이토치 : https://pytorch.org/vision/main/models.html#table-of-all-available-classification-weights - VGG-16 with ImageNet & BN : https:...
2. 실습: 출처

## Code Highlights

### class VGG(nn.Module)

`class VGG(nn.Module)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실험의 중심이 되는 모델 아키텍처를 정의하는 코드입니다.

```python
class VGG(nn.Module):

    def __init__(self, cfg, batch_norm, num_classes=1000, init_weights=True):
        super(VGG, self).__init__()
        self.features = self.make_layers(cfg, batch_norm)
        self.avgpool = nn.AdaptiveAvgPool2d((7, 7)) # 7x7 avg poolng (flatten 노드 개수 통일을 위해 adaptive pooling 사용)
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, num_classes),
        )
        if init_weights:
            self._initialize_weights()

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
# ... trimmed ...
```

### 사전 훈련된 모델 활용

`사전 훈련된 모델 활용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 model = torchvision.models.vgg16_bn(pretrained=True) 흐름이 주석과 함께 드러납니다.

```python
# model = torchvision.models.vgg16_bn(pretrained=True)
model = torchvision.models.vgg16_bn(weights='VGG16_BN_Weights.IMAGENET1K_V1')
model
```

### 실습

`실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 라벨 해석 함수: 0 -> Cat, 1 -> Dog, 카테고리별로 n개의 샘플 이미지를 수집하여 시각화하는 함수, 데이터셋을 순회하면서 각 카테고리별로 n_samples 개씩 수집 흐름이 주석과 함께 드러납니다.

```python
import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from collections import defaultdict

# 라벨 해석 함수: 0 -> Cat, 1 -> Dog
def label_to_str(label):
    return "Cat" if label == 0 else "Dog"

# 카테고리별로 n개의 샘플 이미지를 수집하여 시각화하는 함수
def visualize_by_category(dataset, n_samples=5, cmap=None):
    samples = defaultdict(list)
    # 데이터셋을 순회하면서 각 카테고리별로 n_samples 개씩 수집
    for img, label in dataset:
        if len(samples[label]) < n_samples:
            samples[label].append(img)
        # 두 카테고리 모두 n_samples가 모이면 종료
        if len(samples) == 2 and all(len(imgs) >= n_samples for imgs in samples.values()):
            break

    # 수집된 각 카테고리별로 이미지 그리드 생성 및 시각화
    for label, imgs in samples.items():
        # make_grid를 사용하기 전에 각 이미지의 크기가 동일한지 확인합니다.
        grid_img = torchvision.utils.make_grid(imgs, nrow=n_samples, padding=2)
        plt.figure(figsize=(n_samples * 2, 4))
        # (C, H, W) -> (H, W, C)
        plt.imshow(grid_img.permute(1, 2, 0).numpy(), cmap=cmap)
# ... trimmed ...
```

### 실습

`실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 → 초반에는 빠르게 학습하고, 일정 단계 이후에는 작은 lr로 미세 조정, Train, Val 흐름이 주석과 함께 드러납니다.

```python
import torch.nn as nn
from torchvision.models import vgg16, VGG16_Weights
from tqdm.auto import tqdm
import matplotlib.pyplot as plt

device = "cuda" if torch.cuda.is_available() else "cpu"

model = vgg16(weights=VGG16_Weights.IMAGENET1K_V1)  # 사전학습 가중치 로드 [oai_citation:6‡docs.pytorch.org](https://docs.pytorch.org/vision/main/models/generated/torchvision.models.vgg16.html?utm_source=chatgpt.com)
model.classifier[6] = nn.Linear(4096, 2)            # 1000→2 클래스로 교체
model = model.to(device)

crit = nn.CrossEntropyLoss()
optim = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=1e-4)  # AdamW: decoupled WD [oai_citation:7‡docs.pytorch.org](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html?utm_source=chatgpt.com)
sched = torch.optim.lr_scheduler.StepLR(optim, step_size=5, gamma=0.1) # 학습률 스케줄러: 5 epoch마다 lr를 1/10로 감소
                                                                       # → 초반에는 빠르게 학습하고, 일정 단계 이후에는 작은 lr로 미세 조정

train_acc_hist, val_acc_hist = [], []
EPOCHS = 10
for epoch in range(EPOCHS):
    # ---- Train ----
    model.train()
    corr = tot = 0
    for x,y in tqdm(train_loader, desc=f"E{epoch+1}/{EPOCHS}"):
        x,y = x.to(device), y.to(device)
        optim.zero_grad()
        out = model(x)
        loss = crit(out, y)
        loss.backward()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/5-4_VGGNet - 공유.md`
- Source formats: `md`
- Companion files: `5-4_VGGNet - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `stackoverflow.com`, `docs.pytorch.org`, `localhost`, `pytorch.org`, `www.microsoft.com`

## Note Preview

> --
> - 파이토치 : https://pytorch.org/vision/main/models.html#table-of-all-available-classification-weights - VGG-16 with ImageNet & BN : https://pytorch.org/vision/main/models/generated/torchvision.models.vgg16_bn.html#torchvision.models.VGG16_BN_Weights
