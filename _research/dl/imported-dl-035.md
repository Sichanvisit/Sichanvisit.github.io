---
title: "Faster R-CNN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "6-1_Faster R-CNN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/6-1_Faster R-CNN - 공유.md"
excerpt: "Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn"
research_summary: "Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn. MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다. `md` 원본과 28개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, json입니다."
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

Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn. MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다. `md` 원본과 28개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, json입니다.

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

Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn

### 데이터 다운로드

MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다.

### 데이터셋

COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images

### Custom Collator가 필요한 이유

아래에 기본 collate 함수의 출력과 custom collate를 적용한 최종 출력 형태를 요약했습니다.

## Implementation Flow

1. Faster R-CNN(coco_pytorch): Faster RCNN : https://pytorch.org/vision/0.9/_modules/torchvision/models/detection/faster_rcnn.html#fasterrcnn_resnet50_fpn
2. 데이터 다운로드: MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다.
3. 데이터셋: COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images
4. Custom Collator가 필요한 이유: 아래에 기본 collate 함수의 출력과 custom collate를 적용한 최종 출력 형태를 요약했습니다.

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
