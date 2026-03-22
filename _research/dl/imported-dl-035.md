---
title: "Faster R-CNN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "6-1_Faster R-CNN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/6-1_Faster R-CNN - 공유.md"
excerpt: "Faster R-CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Faster R-CNN(coco_p..., 실습(Pascal VOC 2007) 순서로 핵심 장면을 먼저 훑고, 데이터셋, 모델링, 모델링(Pycocotools 활용) 같은..."
research_summary: "Faster R-CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Faster R-CNN(coco_p..., 실습(Pascal VOC 2007) 순서로 핵심 장면을 먼저 훑고, 데이터셋, 모델링, 모델링(Pycocotools 활용) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 28개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, json입니다."
research_artifacts: "md · 코드 28개 · 실행 14개"
code_block_count: 28
execution_block_count: 14
research_focus:
  - "Faster R-CNN(coco_pytorch)"
  - "실습(Pascal VOC 2007)"
research_stack:
  - "kagglehub"
  - "os"
  - "shutil"
  - "json"
  - "torch"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

Faster R-CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Faster R-CNN(coco_p..., 실습(Pascal VOC 2007) 순서로 핵심 장면을 먼저 훑고, 데이터셋, 모델링, 모델링(Pycocotools 활용) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 28개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, json입니다.

**빠르게 볼 수 있는 포인트**: Faster R-CNN(coco_pytorch), 실습(Pascal VOC 2007).

**남겨둔 자료**: `md` 원본과 28개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, json입니다.

**주요 스택**: `kagglehub`, `os`, `shutil`, `json`, `torch`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 28 |
| Execution Cells | 14 |
| Libraries | `kagglehub`, `os`, `shutil`, `json`, `torch`, `PIL`, `torchvision`, `tqdm` |
| Source Note | `6-1_Faster R-CNN - 공유` |

## What This Note Covers

### Faster R-CNN(coco_pytorch)

Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn COCO API : https://github.com/cocodataset/cocoapi

- 읽을 포인트: 세부 흐름: 데이터셋, 모델링, 모델링(Pycocotools 활용)

#### 데이터셋

COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images 각 이미지에 대한 정보가 담긴 리스트 - 각 항목은 이미지의 고유 id, 파일명, 너비, 높이 등의 정보를 포함합니다.

#### 모델링

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

#### 모델링(Pycocotools 활용)

MS COCO 데이터 측에서 제공하는 관련 툴 : https://github.com/cocodataset/cocoapi/tree/master/PythonAPI

### 실습(Pascal VOC 2007)

실습(Pascal VOC 2007) 코드를 직접 따라가며 실습(Pascal VOC 2007) 흐름을 확인했습니다.

- 읽을 포인트: 실습(Pascal VOC 2007) 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

## Why This Matters

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. Faster R-CNN(coco_pytorch): 데이터셋, 모델링
2. 실습(Pascal VOC 2007): 실습(Pascal VOC 2007) 코드를 직접 따라가며 실습(Pascal VOC 2007) 흐름을 확인했습니다.

## Code Highlights

### 데이터셋

`데이터셋`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 torchvision 라이브러리에서 이미지 전처리 도구와 DataLoader를 임포트합니다., 배치 데이터를 생성할 때, 각 배치마다 데이터를 튜플 형태로 묶어주는 함수, coco 데이터 셋은 이미지 내에 여러 객체 정보가 담길 수 있으므로, 데이터의 길이가... 흐름이 주석과 함께 드러납니다.

```python
# torchvision 라이브러리에서 이미지 전처리 도구와 DataLoader를 임포트합니다.
from torchvision import transforms
from torch.utils.data import DataLoader

# 배치 데이터를 생성할 때, 각 배치마다 데이터를 튜플 형태로 묶어주는 함수
# coco 데이터 셋은 이미지 내에 여러 객체 정보가 담길 수 있으므로, 데이터의 길이가 다를 수 있음.
def collator(batch):
    return tuple(zip(*batch))

# 이미지 전처리: PIL 이미지를 텐서로 변환하고, 데이터 타입을 float으로 변환
transform = transforms.Compose(
    [
        transforms.PILToTensor(),
        transforms.ConvertImageDtype(dtype=torch.float)
    ]
)

# 학습 데이터와 테스트(검증) 데이터를 위한 COCO 데이터셋 객체 생성
train_dataset = COCODataset("./coco", train=True, transform=transform)
test_dataset = COCODataset("./coco", train=False, transform=transform)

# DataLoader를 사용하여 데이터셋을 배치 단위로 불러옵니다.
train_dataloader = DataLoader(
    train_dataset, batch_size=4, shuffle=True, drop_last=True, collate_fn=collator
)
test_dataloader = DataLoader(
    test_dataset, batch_size=1, shuffle=True, drop_last=True, collate_fn=collator
)
```

### 모델링

`모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 torchvision 라이브러리에서 사전 학습된 모델과 관련 모듈을 임포트합니다., 사전 학습된 VGG16 모델의 feature extractor(특징 추출기)를 backb..., RPN(Region Proposal Network)에서 사용할 앵커 생성기 설정 흐름이 주석과 함께 드러납니다.

```python
# torchvision 라이브러리에서 사전 학습된 모델과 관련 모듈을 임포트합니다.
from torchvision import models
from torchvision import ops
from torchvision.models.detection import rpn
from torchvision.models.detection import FasterRCNN

# 사전 학습된 VGG16 모델의 feature extractor(특징 추출기)를 backbone으로 사용합니다.
backbone = models.vgg16(weights="VGG16_Weights.IMAGENET1K_V1").features
backbone.out_channels = 512  # backbone의 출력 채널 수 설정

# RPN(Region Proposal Network)에서 사용할 앵커 생성기 설정
anchor_generator = rpn.AnchorGenerator(
    sizes=((32, 64, 128, 256, 512),),       # 각 스케일별 앵커 크기 지정
    aspect_ratios=((0.5, 1.0, 2.0),)         # 각 앵커의 가로 세로 비율 지정
)

# ROI Pooling: 여러 스케일의 특징맵에서 RoI(Region of Interest)를 고정 크기로 변환
roi_pooler = ops.MultiScaleRoIAlign(
    featmap_names=["0"],         # 사용할 특징맵 이름
    output_size=(7, 7),          # 출력 크기 설정 (7x7)
    sampling_ratio=2             # 샘플링 비율 지정
)

# 학습에 사용할 디바이스를 설정 (GPU가 있으면 cuda, 없으면 cpu)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Faster R-CNN 모델을 생성합니다.
# - backbone: 특징 추출기 (VGG16 사용)
# ... trimmed ...
```

### 모델링(Pycocotools 활용)

`모델링(Pycocotools 활용)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 torchvision 라이브러리에서 사전 학습된 모델과 관련 모듈을 임포트합니다., 사전 학습된 VGG16 모델의 feature extractor(특징 추출기)를 backb..., RPN(Region Proposal Network)에서 사용할 앵커 생성기 설정 흐름이 주석과 함께 드러납니다.

```python
# torchvision 라이브러리에서 사전 학습된 모델과 관련 모듈을 임포트합니다.
from torchvision import models
from torchvision import ops
from torchvision.models.detection import rpn
from torchvision.models.detection import FasterRCNN

# 사전 학습된 VGG16 모델의 feature extractor(특징 추출기)를 backbone으로 사용합니다.
backbone = models.vgg16(weights="VGG16_Weights.IMAGENET1K_V1").features
backbone.out_channels = 512  # backbone의 출력 채널 수 설정

# RPN(Region Proposal Network)에서 사용할 앵커 생성기 설정
anchor_generator = rpn.AnchorGenerator(
    sizes=((32, 64, 128, 256, 512),),       # 각 스케일별 앵커 크기 지정
    aspect_ratios=((0.5, 1.0, 2.0),)         # 각 앵커의 가로 세로 비율 지정
)

# ROI Pooling: 여러 스케일의 특징맵에서 RoI(Region of Interest)를 고정 크기로 변환
roi_pooler = ops.MultiScaleRoIAlign(
    featmap_names=["0"],         # 사용할 특징맵 이름
    output_size=(7, 7),          # 출력 크기 설정 (7x7)
    sampling_ratio=2             # 샘플링 비율 지정
)

# 학습에 사용할 디바이스를 설정 (GPU가 있으면 cuda, 없으면 cpu)
device = "cuda" if torch.cuda.is_available() else "cpu"

# Faster R-CNN 모델을 생성합니다.
# - backbone: 특징 추출기 (VGG16 사용)
# ... trimmed ...
```

### 실습(Pascal VOC 2007)

`실습(Pascal VOC 2007)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 VOC 클래스 목록 (첫번째 background 포함), 클래스 이름을 id로 매핑하는 딕셔너리 생성 (ex: 'cat': 9), VOC 데이터셋은 보통 ImageSets/Main 폴더에 train.txt, val.tx... 흐름이 주석과 함께 드러납니다.

```python
import os
import xml.etree.ElementTree as ET
import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from torchvision import transforms, models, ops
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection import rpn
from torch import optim
import matplotlib.pyplot as plt
import numpy as np
from torchvision.transforms.functional import to_pil_image
from tqdm import tqdm

# VOC 클래스 목록 (첫번째 __background__ 포함)
VOC_CLASSES = (
    "__background__",
    "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat",
    "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person",
    "pottedplant", "sheep", "sofa", "train", "tvmonitor"
)
# 클래스 이름을 id로 매핑하는 딕셔너리 생성 (ex: 'cat': 9)
VOC_CLASS_TO_ID = {cls: idx for idx, cls in enumerate(VOC_CLASSES)}

class VOCDataset(Dataset):
    def __init__(self, root, image_set="train", transform=None):
        """
        Args:
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/6-1_Faster R-CNN - 공유.md`
- Source formats: `md`
- Companion files: `6-1_Faster R-CNN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `50, 50, 200, 200`, `12_Deep_Learning_Code_Summary.md`
- External references: `pytorch.org`, `github.com`, `localhost`, `pjreddie.com`

## Note Preview

> - Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn
> - COCO API : https://github.com/cocodataset/cocoapi
