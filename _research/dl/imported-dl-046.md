---
title: "Mask R-CNN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "Mask R-CNN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/Mask R-CNN - 공유.md"
excerpt: "TV tensors : https://pytorch.org/vision/main/tv_tensors.html"
research_summary: "TV tensors : https://pytorch.org/vision/main/tv_tensors.html. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다."
research_artifacts: "md · 코드 11개 · 실행 6개"
code_block_count: 11
execution_block_count: 6
research_focus:
  - "TV tensors"
  - "데이터셋 정의 (PennFudanDataset)"
  - "PennFudan 데이터셋은 보행자 이미지와 각 이미지에 대한 마스크(분할 정보)를 포함..."
research_stack:
  - "os"
  - "torch"
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

TV tensors : https://pytorch.org/vision/main/tv_tensors.html. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: TV tensors, 데이터셋 정의 (PennFudanDataset), PennFudan 데이터셋은 보행자 이미지와 각 이미지에 대한 마스크(....

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다.

**주요 스택**: `os`, `torch`, `torchvision`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 11 |
| Execution Cells | 6 |
| Libraries | `os`, `torch`, `torchvision`, `matplotlib` |
| Source Note | `Mask R-CNN - 공유` |

## What This Note Covers

### Overview

TV tensors : https://pytorch.org/vision/main/tv_tensors.html

### Key Step

데이터셋 정의 (PennFudanDataset)

### Key Step

PennFudan 데이터셋은 보행자 이미지와 각 이미지에 대한 마스크(분할 정보)를 포함합니다.

### Key Step

모델 정의 (COCO 사전 학습된 Mask R-CNN 사용)

## Implementation Flow

1. Overview: TV tensors : https://pytorch.org/vision/main/tv_tensors.html
2. Key Step: 데이터셋 정의 (PennFudanDataset)
3. Key Step: PennFudan 데이터셋은 보행자 이미지와 각 이미지에 대한 마스크(분할 정보)를 포함합니다.
4. Key Step: 모델 정의 (COCO 사전 학습된 Mask R-CNN 사용)

## Code Highlights

### import os

`import os`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋 정의 (PennFudanDataset), PennFudan 데이터셋은 보행자 이미지와 각 이미지에 대한 마스크(분할 정보)를 포함..., PNGImages 폴더와 PedMasks 폴더 내의 파일 이름을 정렬해서 리스트로 저장 흐름이 주석과 함께 드러납니다.

```python
import os
import torch
import torchvision
import matplotlib.pyplot as plt
from torchvision.io import read_image
from torchvision.ops.boxes import masks_to_boxes
from torchvision import tv_tensors
from torchvision.transforms.v2 import functional as F
from torchvision.transforms import v2 as T


# 1. 데이터셋 정의 (PennFudanDataset)
# PennFudan 데이터셋은 보행자 이미지와 각 이미지에 대한 마스크(분할 정보)를 포함합니다.
class PennFudanDataset(torch.utils.data.Dataset):
    def __init__(self, root, transforms):
        """
        root: 데이터셋의 루트 폴더 (예: './PennFudanPed')
        transforms: 이미지와 타겟에 적용할 변환 함수
        """
        self.root = root
        self.transforms = transforms
        # PNGImages 폴더와 PedMasks 폴더 내의 파일 이름을 정렬해서 리스트로 저장
        self.imgs = sorted(os.listdir(os.path.join(root, "PNGImages")))
        self.masks = sorted(os.listdir(os.path.join(root, "PedMasks")))

    def __getitem__(self, idx):
        # idx번째 이미지와 마스크의 파일 경로 생성
        img_path = os.path.join(self.root, "PNGImages", self.imgs[idx])
# ... trimmed ...
```

### 5. 간단한 학습 루프 (2 에폭 예시)

`5. 간단한 학습 루프 (2 에폭 예시)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 간단한 학습 루프 (2 에폭 예시), 학습 가능한 파라미터만 모아 옵티마이저에 전달, 학습률 스케줄러: 3 에폭마다 학습률을 0.1배 감소 흐름이 주석과 함께 드러납니다.

```python
# 5. 간단한 학습 루프 (2 에폭 예시)
# 학습 가능한 파라미터만 모아 옵티마이저에 전달
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)
# 학습률 스케줄러: 3 에폭마다 학습률을 0.1배 감소
lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

num_epochs = 2  # 학습 에폭 수
for epoch in range(num_epochs):
    model.train()  # 모델을 학습 모드로 전환 (Dropout, BatchNorm 등이 학습 모드로 작동)
    epoch_loss = 0  # 에폭별 손실 누적 변수
    for images, targets in data_loader:
        # 각 이미지와 타겟을 device(GPU 또는 CPU)로 이동
        images = [img.to(device) for img in images]
        # 타겟은 dict 형식이며, tensor인 항목만 to(device) 처리
        targets = [{k: (v.to(device) if torch.is_tensor(v) else v) for k, v in t.items()} for t in targets]

        # 모델에 이미지와 타겟을 전달하면, 학습 모드에서는 손실(loss) dict를 반환합니다.
        loss_dict = model(images, targets)
        # dict의 모든 손실값을 합산하여 총 손실을 계산합니다.
        losses = sum(loss for loss in loss_dict.values())
        epoch_loss += losses.item()  # 손실 값을 float로 누적

        optimizer.zero_grad()  # 이전 배치의 기울기(gradient) 초기화
        losses.backward()      # 역전파를 통해 기울기 계산
        optimizer.step()       # 옵티마이저가 파라미터를 업데이트

    lr_scheduler.step()  # 에폭마다 학습률 업데이트
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/Mask R-CNN - 공유.md`
- Source formats: `md`
- Companion files: `Mask R-CNN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`, `pytorch.org`

## Note Preview

> - TV tensors : https://pytorch.org/vision/main/tv_tensors.html
> 현재 torchvision.models.detection.maskrcnn_resnet50_fpn 모델은 COCO 데이터셋으로 학습되어 있으나, PennFudanDataset은 배경과 객체만 구분하므로 모델을 수정해주어야 합니다.
