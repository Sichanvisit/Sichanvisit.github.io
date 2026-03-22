---
title: "Mission 8 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_8_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_8_강사공유.md"
excerpt: "4.모델 학습 및 평가, 사전설정 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 4.모델 학습 및 평가, 사전설정, 2.데이터 불러오기 순서로 핵심 장면을 먼저 훑고, 증강이 있는 데이터셋, 4.모델 학습 및 평가, UNet 같은..."
research_summary: "4.모델 학습 및 평가, 사전설정 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 4.모델 학습 및 평가, 사전설정, 2.데이터 불러오기 순서로 핵심 장면을 먼저 훑고, 증강이 있는 데이터셋, 4.모델 학습 및 평가, UNet 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 28개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, random, collections, numpy입니다."
research_artifacts: "md · 코드 28개 · 실행 21개"
code_block_count: 28
execution_block_count: 21
research_focus:
  - "4.모델 학습 및 평가"
  - "사전설정"
  - "2.데이터 불러오기"
research_stack:
  - "os"
  - "random"
  - "collections"
  - "numpy"
  - "cv2"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

4.모델 학습 및 평가, 사전설정 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 4.모델 학습 및 평가, 사전설정, 2.데이터 불러오기 순서로 핵심 장면을 먼저 훑고, 증강이 있는 데이터셋, 4.모델 학습 및 평가, UNet 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 28개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, random, collections, numpy입니다.

**빠르게 볼 수 있는 포인트**: 4.모델 학습 및 평가, 사전설정, 2.데이터 불러오기.

**남겨둔 자료**: `md` 원본과 28개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, random, collections, numpy입니다.

**주요 스택**: `os`, `random`, `collections`, `numpy`, `cv2`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Mission |
| Source Files | `md` |
| Code Blocks | 28 |
| Execution Cells | 21 |
| Libraries | `os`, `random`, `collections`, `numpy`, `cv2`, `matplotlib`, `torch`, `torchvision` |
| Source Note | `Mission_8_강사공유` |

## What This Note Covers

### 4.모델 학습 및 평가

Focal Loss - Cross Entropy Loss의 개선된 버전 - 클래스 불균형 문제 해결을 위해 도입 - 쉽게 맞추는 샘플보다 어려운 샘플에 더 큰 가중치를 부여하여 모델이 어려운 샘플을 더 학습하도록 유도 Dice Loss - 불균형한 데이터에서 주로 사용되는 Segmentation Loss - IoU(Intersecti...

- 읽을 포인트: 세부 흐름: UNet, Transformed Data

#### UNet

비전 모델이 객체나 픽셀 단위를 어떻게 예측하는지 구현으로 따라가는 구간입니다.

#### Transformed Data

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### 사전설정

사전설정 코드를 직접 따라가며 사전설정 흐름을 확인했습니다.

- 읽을 포인트: 사전설정 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 2.데이터 불러오기

데이터 시각화, 마스크 라벨링, 데이터셋 > 증강이 있는 데이터셋 같은 코드를 직접 따라가며 2.데이터 불러오기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 데이터 시각화, 마스크 라벨링, 데이터셋 > 증강이 있는 데이터셋

#### 데이터 시각화

2.데이터 불러오기 > 데이터 시각화 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

#### 마스크 라벨링

2.데이터 불러오기 > 마스크 라벨링 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

#### 데이터셋 > 증강이 있는 데이터셋

데이터셋 > 증강이 있는 데이터셋 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 3.모델 저장 및 불러오기

3.모델 저장 및 불러오기 코드를 직접 따라가며 3.모델 저장 및 불러오기 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

## Why This Matters

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 픽셀 단위 분할

- 왜 필요한가: 객체의 경계를 세밀하게 다뤄야 할 때는 이미지 전체를 한 번에 분류하는 방식만으로는 부족합니다.
- 왜 이 방식을 쓰는가: Segmentation은 픽셀마다 클래스를 붙여주기 때문에 의료영상, 장면 이해, 배경 제거처럼 경계가 중요한 문제에 잘 맞습니다.
- 원리: 이미지 특징을 추출한 뒤 해상도를 복원하면서 각 픽셀 위치에 대한 클래스 확률을 예측합니다.

## Implementation Flow

1. 4.모델 학습 및 평가: UNet, Transformed Data
2. 사전설정: 사전설정 코드를 직접 따라가며 사전설정 흐름을 확인했습니다.
3. 2.데이터 불러오기: 데이터 시각화, 마스크 라벨링
4. 3.모델 저장 및 불러오기: 3.모델 저장 및 불러오기 코드를 직접 따라가며 3.모델 저장 및 불러오기 흐름을 확인했습니다.

## Code Highlights

### 증강이 있는 데이터셋

`증강이 있는 데이터셋`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 시각화, 이미지를 0~1 범위로 변환 (tv_tensors.Image는 일반적으로 정규화되어 있음), 원본 이미지 출력 흐름이 주석과 함께 드러납니다.

```python
# @title 시각화
import matplotlib.pyplot as plt
import torchvision.transforms.v2.functional as F
from torchvision.utils import draw_segmentation_masks

def visualize_samples(loader, num_samples=3):
    """ 데이터 로더에서 샘플을 가져와 이미지, 마스크, 오버레이 확인하는 함수 """
    data_iter = iter(loader)
    imgs, masks = next(data_iter)  # 배치에서 첫 번째 샘플 가져오기

    fig, axs = plt.subplots(num_samples, 2, figsize=(9, num_samples * 3))  # (num_samples, 3) 크기의 서브플롯

    for i in range(num_samples):
        img = imgs[i]
        mask = masks[i]

        # 이미지를 0~1 범위로 변환 (tv_tensors.Image는 일반적으로 정규화되어 있음)
        img = F.to_dtype(img, torch.uint8, scale=True)

        # 원본 이미지 출력
        axs[i, 0].imshow(img.permute(1, 2, 0).numpy())  # (C, H, W) → (H, W, C)
        axs[i, 0].set_title("Original Image")
        axs[i, 0].axis("off")

        # 마스크 출력 (Grayscale 변환)
        axs[i, 1].imshow(mask.numpy())
        axs[i, 1].set_title("Segmentation Mask")
        axs[i, 1].axis("off")
# ... trimmed ...
```

### 4.모델 학습 및 평가

`4.모델 학습 및 평가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 및 검증 함수, 학습 시작, 학습 진행 흐름이 주석과 함께 드러납니다.

```python
# 학습 및 검증 함수
def train_model(model, model_name, trainloader, valloader, criterion, optimizer, scheduler, num_epochs):
    model.to(device)
    model, start_epoch, best_metric = load_model(model, model_name, optimizer, scheduler)

    print(f"Start with Epoch={start_epoch}, Best Metric={best_metric}")
    for epoch in range(start_epoch, num_epochs):
        # 학습 시작
        model.train()
        train_loss = 0
        avg_train_loss = 0

        # 학습 진행
        train_bar = tqdm(trainloader, desc=f"Training {epoch+1}/{num_epochs}")
        for images, masks in train_bar:
            images, masks = images.to(device), masks.to(device)
            masks = torch.clamp(masks, min=0, max=10) # 0~10 범위 유지

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, masks)
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            train_bar.set_postfix({"Loss": loss.item()})

        avg_train_loss = train_loss / len(trainloader)
# ... trimmed ...
```

### UNet

`UNet`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습 흐름이 주석과 함께 드러납니다.

```python
# 모델 학습
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet(num_classes=11).to(device)

num_epochs = 35
criterion = HybridLoss(alpha=0.5, num_classes=11)
optimizer = optim.Adam(model.parameters(), lr=0.005, weight_decay=1e-4)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=num_epochs, eta_min=1e-6)

train_model(model, "Baseline_UNet", train_loader, val_loader, criterion, optimizer, scheduler, num_epochs)
```

### Transformed Data

`Transformed Data`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습 흐름이 주석과 함께 드러납니다.

```python
# @title 모델 학습
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = UNet(num_classes=11).to(device)

num_epochs = 51
criterion = HybridLoss(alpha=0.5, num_classes=11)
optimizer = optim.Adam(model.parameters(), lr=0.005, weight_decay=1e-4)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=3, threshold=1e-4, min_lr=1e-6)

train_model(model, "Transformed_UNet", train_transformed_loader, val_transformed_loader, criterion, optimizer, scheduler, num_epochs)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/Mission_8_강사공유.md`
- Source formats: `md`
- Companion files: `Mission_8_강사공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 1. Focal Loss - Cross Entropy Loss의 개선된 버전 - 클래스 불균형 문제 해결을 위해 도입 - 쉽게 맞추는 샘플보다 어려운 샘플에 더 큰 가중치를 부여하여 모델이 어려운 샘플을 더 학습하도록 유도
> 2. Dice Loss - 불균형한 데이터에서 주로 사용되는 Segmentation Loss - IoU(Intersection over Union)와 유사한 방식으로 픽셀 간 유사성을 극대화 - 작은 객체나 적은 픽셀 개수를 가진 클래스를 보다 잘 학습할 수 있도록 함
