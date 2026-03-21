---
title: "Mission 8 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_8_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_8_강사공유.md"
excerpt: "Focal Loss - Cross Entropy Loss의 개선된 버전 - 클래스 불균형 문제 해결을 위해 도입 - 쉽게 맞추는 샘플보다 어려운 샘플에 더 큰 가중치를 부여하여 모델이 어려운 샘플을 더 학습하도록 유도"
research_summary: "Focal Loss - Cross Entropy Loss의 개선된 버전 - 클래스 불균형 문제 해결을 위해 도입 - 쉽게 맞추는 샘플보다 어려운 샘플에 더 큰 가중치를 부여하여 모델이 어려운 샘플을 더 학습하도록 유도. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 28개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, random, collections, numpy입니다."
research_artifacts: "md · 코드 28개 · 실행 21개"
code_block_count: 28
execution_block_count: 21
research_focus:
  - "사전설정"
  - "2.데이터 불러오기"
  - "데이터 시각화"
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

Focal Loss - Cross Entropy Loss의 개선된 버전 - 클래스 불균형 문제 해결을 위해 도입 - 쉽게 맞추는 샘플보다 어려운 샘플에 더 큰 가중치를 부여하여 모델이 어려운 샘플을 더 학습하도록 유도. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 28개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, random, collections, numpy입니다.

**빠르게 볼 수 있는 포인트**: 사전설정, 2.데이터 불러오기, 데이터 시각화.

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

Focal Loss - Cross Entropy Loss의 개선된 버전 - 클래스 불균형 문제 해결을 위해 도입 - 쉽게 맞추는 샘플보다 어려운 샘플에 더 큰 가중치를 부여하여 모델이 어려운 샘플을 더 학습하도록 유도

### Key Step

폴더 내부 이미지 모두 가져오기

### Key Step

원본이미지와 fuse이미지, save이미지

### Key Step

사이즈 확인 (H, W, C)

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

1. 4.모델 학습 및 평가: Focal Loss - Cross Entropy Loss의 개선된 버전 - 클래스 불균형 문제 해결을 위해 도입 - 쉽게 맞추는 샘플보다 어려운 샘플에 더 큰 가중치를 부여하여 모델이 어려운 샘플을 더 학습하도록 유도
2. Key Step: 폴더 내부 이미지 모두 가져오기
3. Key Step: 원본이미지와 fuse이미지, save이미지
4. Key Step: 사이즈 확인 (H, W, C)

## Code Highlights

### 마스크 라벨링

`마스크 라벨링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋 전체의 고유 색상 수집, 클래스 개수가 max_classes를 넘으면 중단, 모든 마스크에서 등장하는 색상 수집 흐름이 주석과 함께 드러납니다.

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

### 데이터셋

`데이터셋`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋 클래스 정의, 원본 이미지 로드, 마스크 로드 (RGB 모드) 흐름이 주석과 함께 드러납니다.

```python
# 데이터셋 클래스 정의
class FootballDataset(Dataset):
    def __init__(self, image_files, mask_files, image_folder, color_to_label, transform=None):
        self.image_files = image_files
        self.mask_files = mask_files
        self.image_folder = image_folder
        self.color_to_label = color_to_label  # 고정된 클래스 매핑
        self.transform = transform

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_path = os.path.join(self.image_folder, self.image_files[idx])
        mask_path = os.path.join(self.image_folder, self.mask_files[idx])

        # 원본 이미지 로드
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 마스크 로드 (RGB 모드)
        mask = cv2.imread(mask_path, cv2.IMREAD_COLOR)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

        # 트랜스폼 분기
        if self.transform is None:
            img = cv2.resize(img, (256, 256)) / 255.0  # 정규화
            img = torch.tensor(img, dtype=torch.float32).permute(2, 0, 1)  # (H, W, C) → (C, H, W)
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
