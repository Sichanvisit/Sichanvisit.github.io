---
title: "SSD"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-3_SSD"
source_path: "12_Deep_Learning/Code_Snippets/6-3_SSD.md"
excerpt: "COCO 데이터셋 클래스 정의, SSD 백본(Backbone) 정의 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 COCO 데이터셋 클래스 정의, SSD 백본(Backbone) 정의, 모델과 앵커 생성자(Anchor G... 순서로..."
research_summary: "COCO 데이터셋 클래스 정의, SSD 백본(Backbone) 정의 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 COCO 데이터셋 클래스 정의, SSD 백본(Backbone) 정의, 모델과 앵커 생성자(Anchor G... 순서로 핵심 장면을 먼저 훑고, 모델과 앵커 생성자(Anchor Gen..., COCO 데이터셋 클래스 정의, DataLoader와 데이터 전처리 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 14개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 shutil, os, torch, collections입니다."
research_artifacts: "md · 코드 14개 · 실행 7개"
code_block_count: 14
execution_block_count: 7
research_focus:
  - "COCO 데이터셋 클래스 정의"
  - "SSD 백본(Backbone) 정의"
  - "모델과 앵커 생성자(Anchor Generator) 초기화"
research_stack:
  - "shutil"
  - "os"
  - "torch"
  - "collections"
  - "torchvision"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

COCO 데이터셋 클래스 정의, SSD 백본(Backbone) 정의 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 COCO 데이터셋 클래스 정의, SSD 백본(Backbone) 정의, 모델과 앵커 생성자(Anchor G... 순서로 핵심 장면을 먼저 훑고, 모델과 앵커 생성자(Anchor Gen..., COCO 데이터셋 클래스 정의, DataLoader와 데이터 전처리 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 14개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 shutil, os, torch, collections입니다.

**빠르게 볼 수 있는 포인트**: COCO 데이터셋 클래스 정의, SSD 백본(Backbone) 정의, 모델과 앵커 생성자(Anchor Generator) 초기화.

**남겨둔 자료**: `md` 원본과 14개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 shutil, os, torch, collections입니다.

**주요 스택**: `shutil`, `os`, `torch`, `collections`, `torchvision`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 14 |
| Execution Cells | 7 |
| Libraries | `shutil`, `os`, `torch`, `collections`, `torchvision`, `PIL`, `pycocotools`, `tqdm` |
| Source Note | `6-3_SSD` |

## What This Note Covers

### COCO 데이터셋 클래스 정의

COCO 데이터셋의 이미지와 어노테이션(JSON 파일)을 읽어와서 모델 학습에 사용할 수 있도록 Dataset 클래스를 정의합니다. _get_categories(): COCO 어노테이션 파일에서 카테고리 정보를 읽어와서, 배경 클래스(0번)와 함께 딕셔너리 형태로 저장합니다. - _load_data(): 각 이미지 파일과 해당 이미지...

- 읽을 포인트: COCO 데이터셋 클래스 정의 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### SSD 백본(Backbone) 정의

먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다. features: ResNet의 앞부분(layer0~layer3)으로 입력 이미지의 기본 특징(feature)을 추출합니다. - upsampling: 기본 특징맵의 채널 수를 512로 변환합니다. - extra:...

- 읽을 포인트: SSD 백본(Backbone) 정의 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 모델과 앵커 생성자(Anchor Generator) 초기화

사전 학습된 ResNet34를 기반으로 SSD 백본을 구성하고, SSD 모델 및 앵커 박스 생성자를 정의합니다. ResNet34를 사전 학습된 가중치와 함께 불러오고, 이를 SSDBackbone으로 감싸 SSD에 맞게 구성합니다. - DefaultBoxGenerator를 통해 SSD에서 사용할 여러 크기의 앵커 박스를 설정합니다. -...

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### COCO 평가 (COCOeval)

모델의 검출 성능을 COCO 평가 방식으로 계산합니다.

- 읽을 포인트: 예측 결과를 확인하고 어떤 부분이 잘 동작했는지 해석하는 구간입니다.

### 객체 검출 결과 시각화

테스트 데이터셋을 이용해 모델이 예측한 바운딩 박스를 시각화합니다. 빨간색은 모델의 예측 결과, 파란색은 실제 정답(ground truth)을 나타냅니다. 모델 예측 결과에서 점수가 일정 임계값 이상인 박스들만 선택하여 시각화합니다. - draw_bbox 함수로 각 박스와 텍스트(클래스 이름 및 점수 혹은 정답)를 그림에 표시합니다.

- 읽을 포인트: 예측 결과를 확인하고 어떤 부분이 잘 동작했는지 해석하는 구간입니다.

### 백본 출력 채널 확인 함수

모델의 백본에서 각 단계별 출력 채널 수를 확인하기 위한 헬퍼 함수입니다. 더미 입력 이미지를 백본에 통과시켜서 각 단계에서 생성되는 특징맵의 채널 수(Depth)를 반환합니다. - 이 함수는 모델의 구조를 이해하거나 디버깅할 때 유용합니다.

- 읽을 포인트: 백본 출력 채널 확인 함수 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

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

1. COCO 데이터셋 클래스 정의: COCO 데이터셋의 이미지와 어노테이션(JSON 파일)을 읽어와서 모델 학습에 사용할 수 있도록 Dataset 클래스를 정의합니다. _get_categories(): COCO 어노테이션 파일에서 카테고리 정보를 읽어와서, 배경 클래...
2. SSD 백본(Backbone) 정의: 먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다. features: ResNet의 앞부분(layer0~layer3)으로 입력 이미지의 기본 특징(feat...
3. 모델과 앵커 생성자(Anchor Generator) 초기화: 사전 학습된 ResNet34를 기반으로 SSD 백본을 구성하고, SSD 모델 및 앵커 박스 생성자를 정의합니다. ResNet34를 사전 학습된 가중치와 함께 불러오고, 이를 SSDBackbone으로 감싸...
4. COCO 평가 (COCOeval): 모델의 검출 성능을 COCO 평가 방식으로 계산합니다.
5. 객체 검출 결과 시각화: 테스트 데이터셋을 이용해 모델이 예측한 바운딩 박스를 시각화합니다. 빨간색은 모델의 예측 결과, 파란색은 실제 정답(ground truth)을 나타냅니다. 모델 예측 결과에서 점수가 일정 임계값 이상인 박스들만 선택하여 시각화합니다. -...
6. 백본 출력 채널 확인 함수: 모델의 백본에서 각 단계별 출력 채널 수를 확인하기 위한 헬퍼 함수입니다. 더미 입력 이미지를 백본에 통과시켜서 각 단계에서 생성되는 특징맵의 채널 수(Depth)를 반환합니다. - 이 함수는 모델의 구조를 이해하거나 디버깅할 때 유용...

## Code Highlights

### 모델과 앵커 생성자(Anchor Generator) 초기화

`모델과 앵커 생성자(Anchor Generator) 초기화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 사전 학습된 ResNet34 모델을 불러옵니다., 위에서 정의한 SSDBackbone으로 ResNet34의 일부 층을 래핑합니다., DefaultBoxGenerator: SSD의 앵커 박스를 생성하기 위한 객체 흐름이 주석과 함께 드러납니다.

```python
import torch
from torchvision.models import resnet34
from torchvision.models.detection import ssd
from torchvision.models.detection.anchor_utils import DefaultBoxGenerator

# 사전 학습된 ResNet34 모델을 불러옵니다.
backbone_base = resnet34(weights="ResNet34_Weights.IMAGENET1K_V1")
# 위에서 정의한 SSDBackbone으로 ResNet34의 일부 층을 래핑합니다.
backbone = SSDBackbone(backbone_base)

# DefaultBoxGenerator: SSD의 앵커 박스를 생성하기 위한 객체
anchor_generator = DefaultBoxGenerator(
    aspect_ratios=[[2], [2, 3], [2, 3], [2, 3], [2, 3], [2], [2]],
    scales=[0.07, 0.15, 0.33, 0.51, 0.69, 0.87, 1.05, 1.20],
    steps=[8, 16, 32, 64, 100, 300, 512],
)

# 사용 가능한 device(CPU 또는 GPU)를 선택합니다.
device = "cuda" if torch.cuda.is_available() else "cpu"

# SSD 모델 생성: backbone, 앵커 생성자, 입력 이미지 크기, 클래스 수를 지정합니다.
model = ssd.SSD(
    backbone=backbone,
    anchor_generator=anchor_generator,
    size=(512, 512),
    num_classes=3
).to(device)
```

### COCO 데이터셋 클래스 정의

`COCO 데이터셋 클래스 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습/검증 데이터를 구분하여 파일 경로 설정, COCO 어노테이션 파일을 읽어옵니다., 카테고리 정보 및 데이터셋의 이미지-어노테이션 페어를 로드합니다. 흐름이 주석과 함께 드러납니다.

```python
import os
import torch
from PIL import Image
from pycocotools.coco import COCO
from torch.utils.data import Dataset

class COCODataset(Dataset):
    def __init__(self, root, train, transform=None):
        super().__init__()
        # 학습/검증 데이터를 구분하여 파일 경로 설정
        directory = "train" if train else "val"
        annotations = os.path.join(root, "annotations", f"{directory}_annotations.json")

        # COCO 어노테이션 파일을 읽어옵니다.
        self.coco = COCO(annotations)
        self.image_path = os.path.join(root, directory)
        self.transform = transform

        # 카테고리 정보 및 데이터셋의 이미지-어노테이션 페어를 로드합니다.
        self.categories = self._get_categories()
        self.data = self._load_data()

    def _get_categories(self):
        # COCO의 카테고리 정보를 {id: name} 형태의 딕셔너리로 저장합니다.
        categories = {0: "background"}
        for category in self.coco.cats.values():
            categories[category["id"]] = category["name"]
        return categories
# ... trimmed ...
```

### DataLoader와 데이터 전처리

`DataLoader와 데이터 전처리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 DataLoader가 배치 데이터를 올바르게 묶을 수 있도록 custom collator..., 이미지 전처리: PIL 이미지를 텐서로 변환하고 데이터 타입을 float으로 변환, 학습 및 테스트 데이터셋 초기화 (datasets 경로는 사용자 환경에 맞게 수정 필요) 흐름이 주석과 함께 드러납니다.

```python
from torchvision import transforms
from torch.utils.data import DataLoader

# DataLoader가 배치 데이터를 올바르게 묶을 수 있도록 custom collator 함수 정의
def collator(batch):
    return tuple(zip(*batch))

# 이미지 전처리: PIL 이미지를 텐서로 변환하고 데이터 타입을 float으로 변환
transform = transforms.Compose(
    [
        transforms.PILToTensor(),
        transforms.ConvertImageDtype(dtype=torch.float)
    ]
)

# 학습 및 테스트 데이터셋 초기화 (datasets 경로는 사용자 환경에 맞게 수정 필요)
train_dataset = COCODataset("../datasets/coco", train=True, transform=transform)
test_dataset = COCODataset("../datasets/coco", train=False, transform=transform)

# DataLoader: 배치 크기, 셔플링 여부, collate 함수 등을 지정
train_dataloader = DataLoader(
    train_dataset, batch_size=4, shuffle=True, drop_last=True, collate_fn=collator
)
test_dataloader = DataLoader(
    test_dataset, batch_size=1, shuffle=True, drop_last=True, collate_fn=collator
)
```

### COCO 평가 (COCOeval)

`COCO 평가 (COCOeval)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 각 이미지에 대해 image_id, 박스, 점수, 레이블 추출, COCO 형식에 맞게 박스 좌표 (x, y, w, h)로 변환, COCO ground truth와 검출 결과를 로드하여 평가를 수행 흐름이 주석과 함께 드러납니다.

```python
import numpy as np
from pycocotools.cocoeval import COCOeval

with torch.no_grad():
    model.eval()
    coco_detections = []
    for images, targets in test_dataloader:
        images = [img.to(device) for img in images]
        outputs = model(images)

        for i in range(len(targets)):
            # 각 이미지에 대해 image_id, 박스, 점수, 레이블 추출
            image_id = targets[i]["image_id"].data.cpu().numpy().tolist()[0]
            boxes = outputs[i]["boxes"].data.cpu().numpy()
            # COCO 형식에 맞게 박스 좌표 (x, y, w, h)로 변환
            boxes[:, 2] = boxes[:, 2] - boxes[:, 0]
            boxes[:, 3] = boxes[:, 3] - boxes[:, 1]
            scores = outputs[i]["scores"].data.cpu().numpy()
            labels = outputs[i]["labels"].data.cpu().numpy()

            for instance_id in range(len(boxes)):
                box = boxes[instance_id, :].tolist()
                prediction = np.array(
                    [
                        image_id,
                        box[0],
                        box[1],
                        box[2],
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/6-3_SSD.md`
- Source formats: `md`
- Companion files: `6-3_SSD.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다.
> - features: ResNet의 앞부분(layer0~layer3)으로 입력 이미지의 기본 특징(feature)을 추출합니다. - upsampling: 기본 특징맵의 채널 수를 512로 변환합니다. - extra: SSD에서 여러 크기의 특징맵을 사용하기 위한 추가 계층들로, 점진적으로 해상도를 줄이면서 채널 수를 조정합니다. - forward: 입력 이미지를 차례로 features, upsampling, extra 모듈에 통과시켜 여러 수준의 특징맵을 생성한 후, 이를 OrderedDict로 반환합니다.
