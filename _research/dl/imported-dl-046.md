---
title: "Mask R-CNN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "Mask R-CNN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/Mask R-CNN - 공유.md"
excerpt: "Mask R-CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, import os, 데이터 변환 함수 정의, 모델 정의 (COCO 사전 학습된 Ma... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다...."
research_summary: "Mask R-CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, import os, 데이터 변환 함수 정의, 모델 정의 (COCO 사전 학습된 Ma... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 11개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다."
research_artifacts: "md · 코드 11개 · 실행 6개"
code_block_count: 11
execution_block_count: 6
research_focus:
  - "TV tensors"
  - "torchvision에서 COCO 데이터셋으로 사전 학습된 Mask R-CNN 모델 불러오기"
  - "모델 정의 (COCO 사전 학습된 Mask R-CNN 사용)"
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

Mask R-CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, import os, 데이터 변환 함수 정의, 모델 정의 (COCO 사전 학습된 Ma... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 11개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: TV tensors, torchvision에서 COCO 데이터셋으로 사전 학습된 Mask R..., 모델 정의 (COCO 사전 학습된 Mask R-CNN 사용).

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

TV tensors : https://pytorch.org/vision/main/tv_tensors.html 현재 torchvision.models.detection.maskrcnn_resnet50_fpn 모델은 COCO 데이터셋으로 학습되어 있으나, PennFudanDataset은 배경과 객체만 구분하므로 모델을 수정해주어야 합니다.

### Key Step

데이터셋 정의 (PennFudanDataset)

### Key Step

PennFudan 데이터셋은 보행자 이미지와 각 이미지에 대한 마스크(분할 정보)를 포함합니다.

### Key Step

모델 정의 (COCO 사전 학습된 Mask R-CNN 사용)

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

1. Overview: TV tensors : https://pytorch.org/vision/main/tv_tensors.html 현재 torchvision.models.detection.maskrcnn_resnet50_fpn 모델은 COCO 데이터셋으로 학습되어 있으나, PennFudanDataset...
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

### 2. 데이터 변환 함수 정의

`2. 데이터 변환 함수 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터 변환 함수 정의, 학습 시 좌우 반전(data augmentation)을 50% 확률로 적용, 이미지를 float형으로 변환하고 0~1 범위로 스케일 조정 흐름이 주석과 함께 드러납니다.

```python
# 2. 데이터 변환 함수 정의

def get_transform(train):
    """
    train: True이면 학습용 변환을, False이면 검증용 변환을 적용합니다.
    """
    transforms = []
    if train:
        # 학습 시 좌우 반전(data augmentation)을 50% 확률로 적용
        transforms.append(T.RandomHorizontalFlip(0.5))
        transfroms.append(T.RandomVerticalFlip(0.5))
    # 이미지를 float형으로 변환하고 0~1 범위로 스케일 조정
    transforms.append(T.ToDtype(torch.float, scale=True))
    # Tensor로 변환 (이미 ToDtype에서 텐서가 유지되지만, 혹시 모를 변환을 위해 추가)
    transforms.append(T.ToPureTensor())
    return T.Compose(transforms)
```

### 3. 모델 정의 (COCO 사전 학습된 Mask R-CNN 사용)

`3. 모델 정의 (COCO 사전 학습된 Mask R-CNN 사용)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 정의 (COCO 사전 학습된 Mask R-CNN 사용), COCO에서 사전 학습된 Mask R-CNN (ResNet50 FPN 기반) 모델을 사용..., 이 모델은 객체 검출 및 인스턴스 분할을 모두 수행합니다. 흐름이 주석과 함께 드러납니다.

```python
# 3. 모델 정의 (COCO 사전 학습된 Mask R-CNN 사용)

# COCO에서 사전 학습된 Mask R-CNN (ResNet50 FPN 기반) 모델을 사용하여 파인튜닝합니다.
# 이 모델은 객체 검출 및 인스턴스 분할을 모두 수행합니다.
num_classes = 2  # 1 class (person) + background
device = "cuda" if torch.cuda.is_available() else "cpu"

# torchvision에서 COCO 데이터셋으로 사전 학습된 Mask R-CNN 모델 불러오기
model = torchvision.models.detection.maskrcnn_resnet50_fpn(weights="DEFAULT")

# -------------------------
# 박스 예측기 (classification head) 교체
# -------------------------
# 모델의 마지막 계층인 box_predictor의 입력 피처 수를 확인합니다.
in_features = model.roi_heads.box_predictor.cls_score.in_features
# FastRCNNPredictor를 사용하여 새롭게 분류기(head)를 생성합니다.
model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, num_classes)

# -------------------------
# 마스크 예측기 (mask head) 교체
# -------------------------
# mask_predictor의 conv5_mask 레이어의 입력 채널 수 확인
in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
hidden_layer = 256  # 마스크 예측기에서 사용할 숨겨진 레이어의 크기
# MaskRCNNPredictor를 사용하여 마스크 분류기(head)를 새롭게 생성합니다.
model.roi_heads.mask_predictor = torchvision.models.detection.mask_rcnn.MaskRCNNPredictor(in_features_mask, hidden_layer, num_classes)

# 모델을 선택한 디바이스(CPU 또는 GPU)로 이동
# ... trimmed ...
```

### 시각화를 위한 전처리: 이미지의 픽셀 값을 0~255 범위로 정규화하여 uint8 타입으로 변환합니다.

`시각화를 위한 전처리: 이미지의 픽셀 값을 0~255 범위로 정규화하여 uint8 타입으로 변환합니다.`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 시각화를 위한 전처리: 이미지의 픽셀 값을 0~255 범위로 정규화하여 uint8 타입으..., image.min(), image.max()를 이용해 정규화하고 [:3, ...]로 RG..., 예측된 각 박스에 대해, 점수를 포함한 라벨 문자열을 생성합니다. 흐름이 주석과 함께 드러납니다.

```python
# 시각화를 위한 전처리: 이미지의 픽셀 값을 0~255 범위로 정규화하여 uint8 타입으로 변환합니다.

# image.min(), image.max()를 이용해 정규화하고 [:3, ...]로 RGB 채널만 선택합니다.
image_vis = (255.0 * (image - image.min()) / (image.max() - image.min())).to(torch.uint8)[:3, ...]
# 예측된 각 박스에 대해, 점수를 포함한 라벨 문자열을 생성합니다.
pred_labels = [f"ped: {score:.3f}" for score in pred["scores"]]
# 예측된 바운딩 박스 좌표를 정수형(long)으로 변환합니다.
pred_boxes = pred["boxes"].long()
# draw_bounding_boxes: 이미지 위에 박스를 그림. output_image는 Tensor 형태로 반환됩니다.
output_image = torchvision.utils.draw_bounding_boxes(image_vis, pred_boxes, pred_labels, colors="red")


# 마스크 예측 결과: 0.7 이상의 확률을 가진 픽셀을 True로 설정합니다.
# squeeze(1)은 마스크 텐서의 차원을 줄여줍니다.
masks = (pred["masks"] > 0.7).squeeze(1)
# draw_segmentation_masks: 이미지 위에 반투명한 색상의 마스크를 그림.
output_image = torchvision.utils.draw_segmentation_masks(output_image, masks, alpha=0.5, colors="blue")


# 결과 시각화: plt.imshow()에 전달하기 전에 채널 순서를 (채널, 높이, 너비)에서 (높이, 너비, 채널)로 변경합니다.
plt.figure(figsize=(12, 12))
plt.imshow(output_image.permute(1, 2, 0))
plt.title("Prediction Result")
plt.show()
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
