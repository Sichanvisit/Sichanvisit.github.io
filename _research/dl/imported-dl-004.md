---
title: "Faster R-CNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Faster R-CNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Faster R-CNN.md"
excerpt: "Faster R-CNN에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 COCO Data, 모델 순서로 핵심 장면을 먼저 훑고, COCO Data, 데이터셋, Custom Collator가 필요한 이유 같은 코드로 실제 구현을 이어서 확인할 수 있습니..."
research_summary: "Faster R-CNN에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 COCO Data, 모델 순서로 핵심 장면을 먼저 훑고, COCO Data, 데이터셋, Custom Collator가 필요한 이유 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 18개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, future입니다."
research_artifacts: "md · 코드 18개 · 실행 17개"
code_block_count: 18
execution_block_count: 17
research_focus:
  - "COCO Data"
  - "모델"
research_stack:
  - "kagglehub"
  - "os"
  - "shutil"
  - "future"
  - "json"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

Faster R-CNN에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 COCO Data, 모델 순서로 핵심 장면을 먼저 훑고, COCO Data, 데이터셋, Custom Collator가 필요한 이유 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 18개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, future입니다.

**빠르게 볼 수 있는 포인트**: COCO Data, 모델.

**남겨둔 자료**: `md` 원본과 18개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, future입니다.

**주요 스택**: `kagglehub`, `os`, `shutil`, `__future__`, `json`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 18 |
| Execution Cells | 17 |
| Libraries | `kagglehub`, `os`, `shutil`, `__future__`, `json`, `torch`, `PIL`, `torchvision` |
| Source Note | `(실습)Faster R-CNN` |

## What This Note Covers

### COCO Data

COCO API : https://github.com/cocodataset/cocoapi MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다.

- 읽을 포인트: 세부 흐름: 데이터셋, Custom Collator가 필요한 이유

#### 데이터셋

COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images 각 이미지에 대한 정보가 담긴 리스트 - 각 항목은 이미지의 고유 id, 파일명, 너비, 높이 등의 정보를 포함합니다.

#### Custom Collator가 필요한 이유

아래에 기본 collate 함수의 출력과 custom collate를 적용한 최종 출력 형태를 요약했습니다. 기본 collate 함수 (원래 형태): - 출력: - 이미지 텐서: 모든 이미지가 동일한 크기라면, 자동으로 스택되어 하나의 텐서로 만들어집니다. 예: (batch_siz...

### 모델

모델 코드를 직접 따라가며 모델 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. COCO Data: 데이터셋, Custom Collator가 필요한 이유
2. 모델: 모델 코드를 직접 따라가며 모델 흐름을 확인했습니다.

## Code Highlights

### COCO Data

`COCO Data`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다.

```python
print(os.listdir('./'))
```

### 데이터셋

`데이터셋`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 COCODataset class, customCOCO를 이용해 annotation 파일 정보 수지, 이미지 파일 경로 설정 흐름이 주석과 함께 드러납니다.

```python
#@title COCODataset class

class COCODataset(Dataset):
    def __init__(self, root, train, transform=None):
        super().__init__()
        directory = "train" if train else "val"

        annotations_file = os.path.join(root, 'annotations', f"{directory}_annotations.json")

        # customCOCO를 이용해 annotation 파일 정보 수지
        self.coco = CustomCOCO(annotations_file)
        # 이미지 파일 경로 설정
        self.image_path = os.path.join(root, directory)
        self.transform = transform

        # COCO 데이터셋의 카테고리 정보를 저장 -->0번은 배경
        self.categories = {0:'backgroud'}
        for cat_id, cat in self.coco.cats.items():
            self.categories[cat_id] = cat['name']

        self.data = self._load_data()

    def _load_data(self):
        data = []
        for _id, img_info in self.coco.images.items():
            file_name = img_info["file_name"]
            image_path = os.path.join(self.image_path, file_name)
            image = Image.open(image_path).convert("RGB")
# ... trimmed ...
```

### Custom Collator가 필요한 이유

`Custom Collator가 필요한 이유`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기본 collator, > (image1, image2), (target1, target2), custom collator 흐름이 주석과 함께 드러납니다.

```python
import torch
from torch.utils.data import DataLoader

image1 = torch.randn(3,300,300)
target1 ={
    'boxes' : torch.tensor([[50,50,200,200]], dtype=torch.float32),
    'labels' : torch.tensor([1])
}

image2 = torch.randn(3,400,300)
target2 ={
    'boxes' : torch.tensor([[100,100,350,350], [20,20,100,100]], dtype=torch.float32),
    'labels' : torch.tensor([2,3])
}

sample_data = [(image1,target1), (image2, target2)]

#기본 collator
loader_wo_collator = DataLoader(sample_data, batch_size=2)
# --> (image1, image2), (target1, target2)

try:
    for batch in loader_wo_collator:
        images, targets = batch
        print("Batch images shape", images.shape)
except Exception as e:
    print("기본 collator함수 사용시 에러 ", e)

# ... trimmed ...
```

### 모델

`모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 사전 학습 vgg16의 feature extractor 를 backbone으로 활용, RPN에서 사용할 앵커 생성기 설정, POI Pooling 흐름이 주석과 함께 드러납니다.

```python
from torchvision import models
from torchvision import ops
from torchvision.models.detection import rpn
from torchvision.models.detection import FasterRCNN

# 사전 학습 vgg16의 feature extractor 를 backbone으로 활용
backbone = models.vgg16(weights="VGG16_Weights.IMAGENET1K_V1").features
backbone.out_channels = 512

# RPN에서 사용할 앵커 생성기 설정
anchor_generator = rpn.AnchorGenerator(
    sizes=((32,64,128,256,512),),
    aspect_ratios=((0.5, 1.0, 2.0),)
)

# POI Pooling
roi_pooler = ops.MultiScaleRoIAlign(
    featmap_names=["0"],
    output_size=(7,7),
    sampling_ratio=2
)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = FasterRCNN(
    backbone=backbone,
    num_classes=3, #강이지, 고양이, 배경
    rpn_anchor_generator=anchor_generator,
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)Faster R-CNN.md`
- Source formats: `md`
- Companion files: `(실습)Faster R-CNN.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `50,50,200,200`, `12_Deep_Learning_Code_Summary.md`
- External references: `github.com`, `localhost`

## Note Preview

> - COCO API : https://github.com/cocodataset/cocoapi
> MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다.
