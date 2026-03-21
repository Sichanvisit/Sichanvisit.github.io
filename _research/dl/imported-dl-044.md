---
title: "FCN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "FCN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/FCN - 공유.md"
excerpt: "실습, Step 1, Step 2 중심으로 구현 과정을 정리한 FCN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시..."
research_summary: "실습, Step 1, Step 2 중심으로 구현 과정을 정리한 FCN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다."
research_artifacts: "md · 코드 11개 · 실행 8개"
code_block_count: 11
execution_block_count: 8
research_focus:
  - "실습"
  - "Step 1"
  - "Step 2"
research_stack:
  - "os"
  - "json"
  - "torch"
  - "numpy"
  - "PIL"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

실습, Step 1, Step 2 중심으로 구현 과정을 정리한 FCN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: 실습, Step 1, Step 2.

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**주요 스택**: `os`, `json`, `torch`, `numpy`, `PIL`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 11 |
| Execution Cells | 8 |
| Libraries | `os`, `json`, `torch`, `numpy`, `PIL`, `torchvision`, `matplotlib`, `tqdm` |
| Source Note | `FCN - 공유` |

## What This Note Covers

- 실습
- Step 1
- Step 2
- 이미지 변환
- PIL 이미지를 tensor로 변환

## Why This Matters

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

## Implementation Flow

1. Key Step: Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기
2. Key Step: Step 2: 이미지와 마스크에 적용할 전처리(Transform) 정의하기
3. Key Step: PIL 이미지를 tensor로 변환
4. Key Step: tensor의 데이터 타입을 float로 변경

## Code Highlights

### import os

`import os`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기, train이면 'train', 아니면 'val' 이미지를 선택합니다., torchvision의 VOCSegmentation 클래스를 사용하여 VOC 데이터셋을... 흐름이 주석과 함께 드러납니다.

```python
import os
import json
import torch
import numpy as np
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, datasets
import matplotlib.pyplot as plt

###############################################
# Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기
###############################################
class SegmentationDataset(Dataset):
    def __init__(self, root, train=True, transform=None, target_transform=None, download=False):
        """
        VOCSegmentation 데이터셋을 로드하고, 이미지와 pixel-level segmentation mask를 반환하는 Dataset 클래스입니다.

        Args:
            root (str): 데이터셋이 저장될 루트 경로
            train (bool): True이면 training 데이터를, False이면 validation 데이터를 사용
            transform: 입력 이미지에 적용할 변환(예: 크기 조정, tensor 변환 등)
            target_transform: segmentation mask에 적용할 변환(보통 크기 조정 등, 클래스 값 보존을 위해 nearest interpolation 사용)
            download (bool): 데이터가 없으면 자동으로 다운로드할지 여부
        """
        # train이면 'train', 아니면 'val' 이미지를 선택합니다.
        image_set = 'train' if train else 'val'

        # torchvision의 VOCSegmentation 클래스를 사용하여 VOC 데이터셋을 불러옵니다.
# ... trimmed ...
```

### 하이퍼파라미터 및 디바이스 설정

`하이퍼파라미터 및 디바이스 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 하이퍼파라미터 및 디바이스 설정, 옵티마이저와 손실 함수 설정, 학습 loop (tqdm으로 진행 상황 표시) 흐름이 주석과 함께 드러납니다.

```python
# 하이퍼파라미터 및 디바이스 설정
num_classes = 21
device = "cuda" if torch.cuda.is_available() else "cpu"
model = FCN8s(num_classes=num_classes).to(device)

# 옵티마이저와 손실 함수 설정
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9, weight_decay=0.0005)
criterion = nn.CrossEntropyLoss()

# 학습 loop (tqdm으로 진행 상황 표시)
num_epochs = 20
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, targets in tqdm(train_dataloader, desc=f"Epoch {epoch+1}/{num_epochs}"):
        images = images.to(device)
        targets = targets.to(device)  # targets shape: [B, H, W]

        # 타겟의 차원 확인 후 squeeze
        if targets.dim() == 4 and targets.size(1) == 1:
            targets = targets.squeeze(1)


        optimizer.zero_grad()
        outputs = model(images)  # outputs shape: [B, num_classes, H, W]
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
# ... trimmed ...
```

### 실습

`실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
!wget https://www.cis.upenn.edu/~jshi/ped_html/PennFudanPed.zip -P data
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/FCN - 공유.md`
- Source formats: `md`
- Companion files: `FCN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`

## Note Preview

> -
