---
title: "Faster R-CNN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "6-1_Faster R-CNN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/6-1_Faster R-CNN - 공유.md"
excerpt: "Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn COCO API : https://github.com/cocodataset/c..."
research_summary: "Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn COCO API : https://github.com/cocodataset/cocoapi. MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다. `md` 원본과 28개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, json입니다."
research_artifacts: "md · 코드 28개 · 실행 14개"
code_block_count: 28
execution_block_count: 14
research_focus:
  - "Faster RCNN"
  - "Faster R-CNN(coco_pytorch)"
  - "MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기..."
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

Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn COCO API : https://github.com/cocodataset/cocoapi. MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다. `md` 원본과 28개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, json입니다.

**빠르게 볼 수 있는 포인트**: Faster RCNN, Faster R-CNN(coco_pytorch), MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로....

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

### Faster R-CNN(coco_pytorch) > 데이터 다운로드

MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다.

### Faster R-CNN(coco_pytorch) > 데이터셋

COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images 각 이미지에 대한 정보가 담긴 리스트 - 각 항목은 이미지의 고유 id, 파일명, 너비, 높이 등의 정보를 포함합니다.

### 데이터셋 > Custom Collator가 필요한 이유

아래에 기본 collate 함수의 출력과 custom collate를 적용한 최종 출력 형태를 요약했습니다. 기본 collate 함수 (원래 형태): - 출력: - 이미지 텐서: 모든 이미지가 동일한 크기라면, 자동으로 스택되어 하나의 텐서로 만들어집니다. 예: (batch_size, channels, height, width) - 타겟(라벨) 텐서/딕셔너리: 동일한 방식으로 스택 또는...

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

1. Faster R-CNN(coco_pytorch): Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn COCO API : http...
2. Faster R-CNN(coco_pytorch) > 데이터 다운로드: MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다.
3. Faster R-CNN(coco_pytorch) > 데이터셋: COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images 각 이미지에 대한 정보가 담긴 리스트 - 각 항목은 이미지의 고유 id, 파일명, 너비, 높이 등의 정보를 포함합니다.
4. 데이터셋 > Custom Collator가 필요한 이유: 아래에 기본 collate 함수의 출력과 custom collate를 적용한 최종 출력 형태를 요약했습니다. 기본 collate 함수 (원래 형태): - 출력: - 이미지 텐서: 모든 이미지가 동일한 크기라면, 자동으로 스택되어 하나의 텐서로...

## Code Highlights

### 데이터셋

`데이터셋`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 COCO 데이터셋의 JSON 파일을 직접 파싱하기 위한 사용자 정의 클래스, JSON 파일을 열어서 데이터를 읽습니다., 이미지 정보를 'id'를 키로 하는 딕셔너리로 저장합니다. 흐름이 주석과 함께 드러납니다.

```python
import os              # 파일 및 디렉토리 경로를 다루기 위한 표준 라이브러리
import json            # JSON 파일을 읽고 쓰기 위한 표준 라이브러리
import torch           # 딥러닝 라이브러리 PyTorch (텐서 연산 등)
from PIL import Image  # 이미지를 다루기 위한 Pillow 라이브러리
from torch.utils.data import Dataset  # PyTorch의 Dataset 클래스를 상속받기 위한 모듈

# COCO 데이터셋의 JSON 파일을 직접 파싱하기 위한 사용자 정의 클래스
class CustomCOCO:
    def __init__(self, annotation_file):
        """
        CustomCOCO 클래스 초기화 함수.
        :param annotation_file: COCO 데이터셋의 어노테이션(JSON) 파일 경로
        """
        # JSON 파일을 열어서 데이터를 읽습니다.
        with open(annotation_file, 'r') as f:
            self.data = json.load(f)

        # 이미지 정보를 'id'를 키로 하는 딕셔너리로 저장합니다.
        # 각 이미지 정보는 JSON 파일의 "images" 리스트에 저장되어 있습니다.
        self.images = {img["id"]: img for img in self.data.get("images", [])}

        # 어노테이션(annotation) 정보를 이미지 id별로 그룹화합니다.
        # JSON 파일의 "annotations" 리스트를 순회하며, 각 어노테이션을 해당 이미지 id 아래에 저장합니다.
        self.annotations = {}
        for ann in self.data.get("annotations", []):
            img_id = ann["image_id"]
            if img_id not in self.annotations:
                self.annotations[img_id] = []
# ... trimmed ...
```

### 모델링(Pycocotools 활용)

`모델링(Pycocotools 활용)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 필요한 라이브러리들을 임포트합니다., COCO 데이터셋을 처리하기 위한 사용자 정의 Dataset 클래스, 'train'이 True면 'train' 디렉토리, 아니면 'val' 디렉토리를 사용합니다. 흐름이 주석과 함께 드러납니다.

```python
# 필요한 라이브러리들을 임포트합니다.
import torch
from PIL import Image                   # 이미지 처리를 위한 Pillow 라이브러리
from pycocotools.coco import COCO         # COCO 데이터셋을 다루기 위한 라이브러리
from torch.utils.data import Dataset      # PyTorch의 Dataset 클래스를 상속받기 위해 사용


# COCO 데이터셋을 처리하기 위한 사용자 정의 Dataset 클래스
class COCODataset(Dataset):
    def __init__(self, root, train, transform=None):
        """
        초기화 함수:
        - root: 데이터셋의 최상위 경로
        - train: 학습용 데이터(True)와 검증용 데이터(False) 구분
        - transform: 이미지 전처리를 위한 변환 함수 (예: tensor 변환)
        """
        super().__init__()
        # 'train'이 True면 'train' 디렉토리, 아니면 'val' 디렉토리를 사용합니다.
        directory = "train" if train else "val"
        # 해당 디렉토리의 주석(annotation) 파일 경로를 설정합니다.
        annotations = os.path.join(root, "annotations", f"{directory}_annotations.json")

        # COCO 형식의 주석 데이터를 불러옵니다.
        self.coco = COCO(annotations)
        # 이미지가 저장된 경로 설정 (train 또는 val 디렉토리)
        self.image_path = os.path.join(root, directory)
        # 이미지 전처리 변환 함수 저장
        self.transform = transform
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
