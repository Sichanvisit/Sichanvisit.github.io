---
title: "Mission 8 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_8_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_8_강사공유.md"
excerpt: "1. Focal Loss - Cross Entropy Loss의 개선된 버전 - 클래스 불균형 문제 해결을 위해 도입 - 쉽게 맞추는 샘플보다 어려운 샘플에 더 큰 가중치를 부여하여 모델이 어려운 샘플을 더 학습하도록 유도"
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

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

## What I Worked On

- 1. 사전설정
- 드라이브 마운트
- device 설정
- 2.데이터 불러오기
- Download latest version

## Implementation Flow

1. 1. 사전설정
2. 드라이브 마운트
3. device 설정
4. 2.데이터 불러오기
5. Download latest version
6. 폴더 내부 이미지 모두 가져오기

## Code Highlights

### 마스크 라벨링

```python
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, random_split

# 데이터셋 전체의 고유 색상 수집
def get_unique_colors(image_folder, mask_files, max_classes=11):
    """
    데이터셋의 모든 마스크에서 고유한 색상을 추출하는 함수.

    Args:
        image_folder (str): 마스크 이미지가 있는 폴더 경로
        mask_files (list): 마스크 이미지 파일 리스트
        max_classes (int): 최대 클래스 개수 (기본값: 11)

    Returns:
        list: 고유한 색상 리스트 (최대 max_classes개)
    """
    color_set = set()

    for mask_file in mask_files:
        mask_path = os.path.join(image_folder, mask_file)
        mask = cv2.imread(mask_path, cv2.IMREAD_COLOR)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
        unique_colors, _ = np.unique(mask.reshape(-1, 3), axis=0, return_counts=True)   # 고유한 색상 추출 (H * W, 3)

        for color in unique_colors:
# ... trimmed ...
```

### 4.모델 학습 및 평가

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
