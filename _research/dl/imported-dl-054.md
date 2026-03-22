---
title: "Segmentation 데이터다루기 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "Segmentation_데이터다루기 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/Segmentation_데이터다루기 - 공유.md"
excerpt: "Segmentation 데이터다루기 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 PennFudanPed, VOC2012 다루기, COCO 순서로 핵심 장면을 먼저 훑고, 데이터셋과 데이터로더, 시각화, Instance Segmentatio..."
research_summary: "Segmentation 데이터다루기 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 PennFudanPed, VOC2012 다루기, COCO 순서로 핵심 장면을 먼저 훑고, 데이터셋과 데이터로더, 시각화, Instance Segmentation... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 76개 코드 블록, 52개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다."
research_artifacts: "md · 코드 76개 · 실행 52개"
code_block_count: 76
execution_block_count: 52
research_focus:
  - "PennFudanPed"
  - "VOC2012 다루기"
  - "COCO"
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

Segmentation 데이터다루기 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 PennFudanPed, VOC2012 다루기, COCO 순서로 핵심 장면을 먼저 훑고, 데이터셋과 데이터로더, 시각화, Instance Segmentation... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 76개 코드 블록, 52개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: PennFudanPed, VOC2012 다루기, COCO.

**남겨둔 자료**: `md` 원본과 76개 코드 블록, 52개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**주요 스택**: `os`, `json`, `torch`, `numpy`, `PIL`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 76 |
| Execution Cells | 52 |
| Libraries | `os`, `json`, `torch`, `numpy`, `PIL`, `torchvision`, `matplotlib`, `xml` |
| Source Note | `Segmentation_데이터다루기 - 공유` |

## What This Note Covers

### PennFudanPed

PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. 도심 환경 등 다양한 배경에서 촬영된 이미지들이 포함되어 있으며, 각 이미지에 대해 보행자 영역을 나타내는 마스크(ground truth)가 제공됩니다.

- 읽을 포인트: PennFudanPed 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### VOC2012 다루기

이미지와 마스크, Annotation, 데이터셋과 데이터로더 같은 코드를 직접 따라가며 VOC2012 다루기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 이미지와 마스크, Annotation, 데이터셋과 데이터로더

#### 이미지와 마스크

VOC2012 다루기 > 이미지와 마스크 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

#### Annotation

xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다. XML 파싱: - ET.parse('파일경로.xml')를...

#### 데이터셋과 데이터로더

VOC2012 다루기 > 데이터셋과 데이터로더 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### COCO

Annotation의 유형, COCO API를 활용하기 위해 a..., 마스크 생성하기 > cocotool... 같은 코드를 직접 따라가며 COCO 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Annotation의 유형, COCO API를 활용하기 위해 annotaion 파일을 COCO 객체로 로드하기 > Instance Segmentation 시각화 - COCO API 활용한 시각화, 마스크 생성하기 > cocotools : coco.annToMask()

#### Annotation의 유형

바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공

#### COCO API를 활용하기 위해 annotaion 파일을 COCO 객체로 로드하기 > Instance Segmentation 시각화 - COCO API 활용한 시각화

getAnnIds()로 특정 image에 해당하는 annotation id를 가져온 후에 이 id를 loadAnns()로 입력하여 해당 이미지의 모든 annotation 정보를 가져옴. - segmentation 정보는 polygon 형태로 되어 있음. - annotation 정보...

#### 마스크 생성하기 > cocotools : coco.annToMask()

이 코드는 COCO API에서 제공하는 annToMask() 함수를 사용하여, 주어진 annotation의 polygon 정보를 이진 마스크(binary mask) 형태로 변환하는 과정을 보여줍니다. annToMask()를 사용하여 annotation의 polygon 정보를 이진...

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 픽셀 단위 분할

- 왜 필요한가: 객체의 경계를 세밀하게 다뤄야 할 때는 이미지 전체를 한 번에 분류하는 방식만으로는 부족합니다.
- 왜 이 방식을 쓰는가: Segmentation은 픽셀마다 클래스를 붙여주기 때문에 의료영상, 장면 이해, 배경 제거처럼 경계가 중요한 문제에 잘 맞습니다.
- 원리: 이미지 특징을 추출한 뒤 해상도를 복원하면서 각 픽셀 위치에 대한 클래스 확률을 예측합니다.

## Implementation Flow

1. PennFudanPed: PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. 도심 환경 등 다양한 배경에서 촬영된 이미지들이 포함되어 있으며, 각 이미지에 대해 보행자 영역을 나타내는 마스크(ground t...
2. VOC2012 다루기: 이미지와 마스크, Annotation
3. COCO: Annotation의 유형, COCO API를 활용하기 위해 annotaion 파일을 COCO 객체로 로드하기 > Instance Segmentation 시각화 - COCO API 활용한 시각화

## Code Highlights

### 데이터셋과 데이터로더

`데이터셋과 데이터로더`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기, train이면 'train', 아니면 'val' 이미지를 선택합니다., torchvision의 VOCSegmentation 클래스를 사용하여 VOC 데이터셋을... 흐름이 주석과 함께 드러납니다.

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

### 시각화

`시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Step 4: 시각화 함수 정의하기, 내부 함수: 마스크에 클래스별 색상을 입히는 함수, target: (1, H, W) 텐서를 squeeze하여 (H, W) 형태로 변경 흐름이 주석과 함께 드러납니다.

```python
###############################################
# Step 4: 시각화 함수 정의하기
###############################################
def draw_mask(images, masks, outputs=None, plot_size=4):
    """
    학습 중 또는 결과 확인을 위해, 이미지와 segmentation mask를 시각화합니다.

    Args:
        images (Tensor): 배치 이미지 (shape: [B, C, H, W])
        masks (Tensor): 배치 마스크 (shape: [B, 1, H, W])
        outputs (Tensor, optional): 예측 마스크 (있을 경우)
        plot_size (int): 시각화할 배치의 수
    """
    # 내부 함수: 마스크에 클래스별 색상을 입히는 함수
    def color_mask(image, target):
        # target: (1, H, W) 텐서를 squeeze하여 (H, W) 형태로 변경
        m = target.squeeze().numpy().astype(np.uint8)
        # image와 같은 크기를 가지는 빈 컬러 이미지를 생성 (H, W, 3)
        cm = np.zeros_like(image, dtype=np.uint8)
        # 클래스 1~20에 대해 색상 적용 (background는 0으로 남음)
        for i in range(1, 21):
            cm[m == i] = train_dataset.categories.get(str(i), {"color": [0, 0, 0]})["color"]

        # 마스크에 포함된 클래스 번호를 이용해 클래스 이름 리스트 생성
        classes = [train_dataset.categories.get(str(idx), {"class": f"class_{idx}"})["class"] for idx in np.unique(m)]
        return cm, classes

    # 출력할 열 수: 예측 결과(outputs)가 있으면 3, 없으면 2
# ... trimmed ...
```

### Instance Segmentation 시각화 - COCO API 활용한 시각화

`Instance Segmentation 시각화 - COCO API 활용한 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 showAnns( )는 annotation 정보들을 입력 받아서 Visualization..., coco.showAnns(anns)는 불러온 annotation 정보(anns)를 기반으... 흐름이 주석과 함께 드러납니다.

```python
# showAnns( )는 annotation 정보들을 입력 받아서 Visualization 시켜줌. 단 먼저 matplotlib 객체로 원본 이미지가 먼저 로드되어 있어야 함.
plt.figure(figsize=(12, 14))
plt.imshow(image_array)
plt.axis('off')

# coco.showAnns(anns)는 불러온 annotation 정보(anns)를 기반으로 segmentation 경계 등을 이미지 위에 그려줍니다.
coco.showAnns(anns)
```

### cocotools 사용

`cocotools 사용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 x,y 좌표값이 연이어 되어 있는 list형 polygon segmentation 정보를... 흐름이 주석과 함께 드러납니다.

```python
 # x,y 좌표값이 연이어 되어 있는 list형 polygon segmentation 정보를 x,y 쌍 형태로 변환.
 polygon_x = [x for index, x in enumerate(ann_2_seg) if index % 2 == 0]
 polygon_y = [x for index, x in enumerate(ann_2_seg) if index % 2 == 1]
 print('polygon_x:', polygon_x)
 print('polygon_y:', polygon_y)
 polygon_xy = [[x, y] for x, y in zip(polygon_x, polygon_y)]
 print('polygon_xy:', polygon_xy)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/Segmentation_데이터다루기 - 공유.md`
- Source formats: `md`
- Companion files: `Segmentation_데이터다루기 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `docs.python.org`, `localhost`, `www.cis.upenn.edu`, `github.com`, `cocodataset.org`

## Note Preview

> xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다.
> 1. **XML 파싱:** - ET.parse('파일경로.xml')를 사용하여 XML 파일을 파싱하고, XML 트리 객체를 생성합니다. - tree.getroot()를 호출하여 트리의 최상위(root) 엘리먼트를 가져옵니다.
