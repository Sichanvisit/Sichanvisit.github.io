---
title: "Segmentation 데이터다루기 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "Segmentation_데이터다루기 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/Segmentation_데이터다루기 - 공유.md"
excerpt: "xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다"
research_summary: "xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다. PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. `md` 원본과 76개 코드 블록, 52개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다."
research_artifacts: "md · 코드 76개 · 실행 52개"
code_block_count: 76
execution_block_count: 52
research_focus:
  - "VOC2012 다루기"
  - "이미지와 마스크"
  - "xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파..."
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

xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다. PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. `md` 원본과 76개 코드 블록, 52개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: VOC2012 다루기, 이미지와 마스크, xml.etree.ElementTree는 Python 내장 XML 처리....

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

### Annotation

xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다.

### PennFudanPed

PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다.

### 데이터 구조 이해

하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨

### Annotation의 유형

바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보

## Implementation Flow

1. Annotation: xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다.
2. PennFudanPed: PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다.
3. 데이터 구조 이해: 하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨
4. Annotation의 유형: 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보

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
