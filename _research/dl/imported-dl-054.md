---
title: "Segmentation 데이터다루기 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "Segmentation_데이터다루기 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/Segmentation_데이터다루기 - 공유.md"
excerpt: "PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. 도심 환경 등 다양한 배경에서 촬영된 이미지들이 포함되어 있으며, 각 이미지에 대해 보행자 영역을 나타내는 마스크(ground truth)가 제공됩니다. xml.etree.ElementTre..."
research_summary: "PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. 도심 환경 등 다양한 배경에서 촬영된 이미지들이 포함되어 있으며, 각 이미지에 대해 보행자 영역을 나타내는 마스크(ground truth)가 제공됩니다. xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다. XML 파싱: - ET.parse('파일경로.xml')를 사용하여 XML 파일을 파싱하고, XML 트리 객체를... `md` 원본과 76개 코드 블록, 52개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다."
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

PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. 도심 환경 등 다양한 배경에서 촬영된 이미지들이 포함되어 있으며, 각 이미지에 대해 보행자 영역을 나타내는 마스크(ground truth)가 제공됩니다. xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다. XML 파싱: - ET.parse('파일경로.xml')를 사용하여 XML 파일을 파싱하고, XML 트리 객체를... `md` 원본과 76개 코드 블록, 52개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

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

### VOC2012 다루기 > Annotation

xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다. XML 파싱: - ET.parse('파일경로.xml')를 사용하여 XML 파일을 파싱하고, XML 트리 객체를 생성합니다. - tree.getroot()를 호출하여...

### PennFudanPed

PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. 도심 환경 등 다양한 배경에서 촬영된 이미지들이 포함되어 있으며, 각 이미지에 대해 보행자 영역을 나타내는 마스크(ground truth)가 제공됩니다.

### COCO > 데이터 구조 이해

하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구성 - images: 각 이미지의 파일명, 고유 ID, 해상도 등의 메타데이터 - annotations: 각 이미지에 포함된 객체의 Annotat...

### COCO > Annotation의 유형

바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공

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

1. VOC2012 다루기 > Annotation: xml.etree.ElementTree는 Python 내장 XML 처리 라이브러리로, XML 파일을 파싱하고, 트리 형태로 데이터를 탐색하며 필요한 정보를 추출할 수 있도록 도와줍니다. 대략적인 사용 방법은 다음과 같습니다. XML 파싱: - ET.pa...
2. PennFudanPed: PennFudanPed 데이터셋은 보행자 탐지 및 segmentation(분할) 작업을 위한 데이터셋입니다. 도심 환경 등 다양한 배경에서 촬영된 이미지들이 포함되어 있으며, 각 이미지에 대해 보행자 영역을 나타내는 마스크(ground truth)가 제공됩니다.
3. COCO > 데이터 구조 이해: 하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구성 - images: 각...
4. COCO > Annotation의 유형: 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공

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

### COCO Annotation 정보 확인하기

`COCO Annotation 정보 확인하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 JSON 파일 확인하기 (파이썬 버전), 파일 정보 확인 (ls -lia와 유사하게 파일의 상세 정보를 출력), jq 설치는 파이썬에서는 필요없음 흐름이 주석과 함께 드러납니다.

```python
# JSON 파일 확인하기 (파이썬 버전)
import os
import json

# 1. 파일 정보 확인 (ls -lia와 유사하게 파일의 상세 정보를 출력)
file_path = '/content/data/annotations/instances_val2017.json'
try:
    stat_info = os.stat(file_path)
    print("파일 경로:", file_path)
    print("파일 크기 (바이트):", stat_info.st_size)
    print("수정 시간 (timestamp):", stat_info.st_mtime)
    print("생성 시간 (timestamp):", stat_info.st_ctime)
    print("Inode 번호:", stat_info.st_ino)
except FileNotFoundError:
    print("파일이 존재하지 않습니다:", file_path)

# 2. jq 설치는 파이썬에서는 필요없음
#    파이썬의 내장 json 모듈을 사용하여 JSON을 다룰 수 있습니다.

# 3. JSON 파일을 읽어 사람이 읽기 좋은 포맷으로 output.json 파일에 저장 (jq . ... > output.json 과 동일)
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)  # indent=2 옵션으로 예쁘게 출력

print("\noutput.json 파일이 생성되었습니다.")

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
