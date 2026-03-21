---
title: "U-Net - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "U-Net - 공유"
source_path: "12_Deep_Learning/Code_Snippets/U-Net - 공유.md"
excerpt: "PennFudanPed Dataset, 예시, UNet 모델 정의 중심으로 구현 과정을 정리한 U-Net - 공유 기록입니다"
research_summary: "PennFudanPed Dataset, 예시, UNet 모델 정의 중심으로 구현 과정을 정리한 U-Net - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 7개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, numpy, PIL, torch입니다."
research_artifacts: "md · 코드 7개 · 실행 5개"
code_block_count: 7
execution_block_count: 5
research_focus:
  - "PennFudanPed Dataset"
  - "예시"
  - "UNet 모델 정의"
research_stack:
  - "os"
  - "numpy"
  - "PIL"
  - "torch"
  - "torchvision"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

PennFudanPed Dataset, 예시, UNet 모델 정의 중심으로 구현 과정을 정리한 U-Net - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 7개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, numpy, PIL, torch입니다.

**빠르게 볼 수 있는 포인트**: PennFudanPed Dataset, 예시, UNet 모델 정의.

**남겨둔 자료**: `md` 원본과 7개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, numpy, PIL, torch입니다.

**주요 스택**: `os`, `numpy`, `PIL`, `torch`, `torchvision`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 7 |
| Execution Cells | 5 |
| Libraries | `os`, `numpy`, `PIL`, `torch`, `torchvision`, `matplotlib` |
| Source Note | `U-Net - 공유` |

## What This Note Covers

- PennFudanPed Dataset
- 예시
- UNet 모델 정의
- 학습 및 평가 루프
- 메인 실행 코드

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

### 픽셀 단위 분할

- 왜 필요한가: 객체의 경계를 세밀하게 다뤄야 할 때는 이미지 전체를 한 번에 분류하는 방식만으로는 부족합니다.
- 왜 이 방식을 쓰는가: Segmentation은 픽셀마다 클래스를 붙여주기 때문에 의료영상, 장면 이해, 배경 제거처럼 경계가 중요한 문제에 잘 맞습니다.
- 원리: 이미지 특징을 추출한 뒤 해상도를 복원하면서 각 픽셀 위치에 대한 클래스 확률을 예측합니다.

## Implementation Flow

1. Key Step: 예시: transform 함수 (resize, tensor 변환)
2. Key Step: 학습/검증 분할 (예: 80% train, 20% val)
3. Key Step: 모델, 손실함수, optimizer

## Code Highlights

### import os

`import os`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ======================, PennFudanPed Dataset 흐름이 주석과 함께 드러납니다.

```python
import os
import numpy as np
from PIL import Image
import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import torchvision.transforms.functional as TF
import matplotlib.pyplot as plt

# ======================
# PennFudanPed Dataset
# ======================
class PennFudanDataset(Dataset):
    def __init__(self, root, transform=None):
        """
        root: PennFudanPed 폴더의 상위 경로 (예: "./data/PennFudanPed")
        transform: 이미지 및 마스크에 적용할 transform (동일하게 적용)
        """
        self.root = root
        self.imgs_dir = os.path.join(root, "PNGImages")
        self.masks_dir = os.path.join(root, "PedMasks")
        self.imgs = list(sorted(os.listdir(self.imgs_dir)))
        self.masks = list(sorted(os.listdir(self.masks_dir)))
        self.transform = transform

    def __len__(self):
# ... trimmed ...
```

### ======================

`======================`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ======================, 메인 실행 코드 흐름이 주석과 함께 드러납니다.

```python
# ======================
# 메인 실행 코드
# ======================

# 하이퍼파라미터 설정
num_epochs = 25
batch_size = 4
learning_rate = 1e-4

# device 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Dataset 및 DataLoader
dataset = PennFudanDataset(root="./data/PennFudanPed", transform=joint_transform)

# 학습/검증 분할 (예: 80% train, 20% val)
train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])
train_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=2)

# 모델, 손실함수, optimizer
model = UNet(n_channels=3, n_classes=2).to(device)
criterion = nn.CrossEntropyLoss()  # output: [B, 2, H, W], mask: [B, H, W] (각 픽셀 0 또는 1)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# 학습 루프
# ... trimmed ...
```

### import matplotlib.pyplot as plt

`import matplotlib.pyplot as plt`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 예측: 각 픽셀에서 채널의 argmax (배경:0, 보행자:1) 흐름이 주석과 함께 드러납니다.

```python
import matplotlib.pyplot as plt

def visualize_predictions(model, dataloader, device, num_images=4):
    model.eval()
    with torch.no_grad():
        for imgs, masks in dataloader:
            imgs = imgs.to(device)
            outputs = model(imgs)  # 출력: [B, n_classes, H, W]
            # 예측: 각 픽셀에서 채널의 argmax (배경:0, 보행자:1)
            preds = torch.argmax(outputs, dim=1).cpu().numpy()
            imgs = imgs.cpu().numpy().transpose(0, 2, 3, 1)  # [B, H, W, C]로 변경
            masks = masks.cpu().numpy()

            for i in range(min(num_images, imgs.shape[0])):
                fig, axs = plt.subplots(1, 3, figsize=(15, 5))
                axs[0].imshow(imgs[i])
                axs[0].set_title("Input Image")
                axs[0].axis("off")

                axs[1].imshow(masks[i], cmap="gray")
                axs[1].set_title("Ground Truth")
                axs[1].axis("off")

                axs[2].imshow(preds[i], cmap="gray")
                axs[2].set_title("Predicted Mask")
                axs[2].axis("off")
                plt.show()
            break
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/U-Net - 공유.md`
- Source formats: `md`
- Companion files: `U-Net - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
