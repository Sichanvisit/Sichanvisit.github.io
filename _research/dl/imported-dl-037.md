---
title: "SSD"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-3_SSD"
source_path: "12_Deep_Learning/Code_Snippets/6-3_SSD.md"
excerpt: "먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다"
research_summary: "먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다. 사전 학습된 ResNet34를 기반으로 SSD 백본을 구성하고, SSD 모델 및 앵커 박스 생성자를 정의합니다. `md` 원본과 14개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 shutil, os, torch, collections입니다."
research_artifacts: "md · 코드 14개 · 실행 7개"
code_block_count: 14
execution_block_count: 7
research_focus:
  - "먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbo..."
  - "SSD 백본(Backbone) 정의"
  - "사전 학습된 ResNet34를 기반으로 SSD 백본을 구성하고, SSD 모델 및 앵커 박스 생성자를 정..."
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

먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다. 사전 학습된 ResNet34를 기반으로 SSD 백본을 구성하고, SSD 모델 및 앵커 박스 생성자를 정의합니다. `md` 원본과 14개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 shutil, os, torch, collections입니다.

**빠르게 볼 수 있는 포인트**: 먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여..., SSD 백본(Backbone) 정의, 사전 학습된 ResNet34를 기반으로 SSD 백본을 구성하고, SSD....

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

### SSD 백본(Backbone) 정의

먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다.

### 모델과 앵커 생성자(Anchor Generator) 초기화

사전 학습된 ResNet34를 기반으로 SSD 백본을 구성하고, SSD 모델 및 앵커 박스 생성자를 정의합니다.

### COCO 데이터셋 클래스 정의

COCO 데이터셋의 이미지와 어노테이션(JSON 파일)을 읽어와서 모델 학습에 사용할 수 있도록 Dataset 클래스를 정의합니다.

### DataLoader와 데이터 전처리

이미지를 텐서로 변환하는 transform과 함께 학습 및 테스트 데이터셋을 로드합니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. SSD 백본(Backbone) 정의: 먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다.
2. 모델과 앵커 생성자(Anchor Generator) 초기화: 사전 학습된 ResNet34를 기반으로 SSD 백본을 구성하고, SSD 모델 및 앵커 박스 생성자를 정의합니다.
3. COCO 데이터셋 클래스 정의: COCO 데이터셋의 이미지와 어노테이션(JSON 파일)을 읽어와서 모델 학습에 사용할 수 있도록 Dataset 클래스를 정의합니다.
4. DataLoader와 데이터 전처리: 이미지를 텐서로 변환하는 transform과 함께 학습 및 테스트 데이터셋을 로드합니다.

## Code Highlights

### SSD 백본(Backbone) 정의

`SSD 백본(Backbone) 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 backbone의 초기 층: conv1, bn1, relu를 하나의 sequential로..., ResNet의 레이어들 (layer1 ~ layer4)를 저장, features는 layer0부터 layer3까지 연결한 것입니다. 흐름이 주석과 함께 드러납니다.

```python
from torch import nn
from collections import OrderedDict

class SSDBackbone(nn.Module):
    def __init__(self, backbone):
        super().__init__()
        # backbone의 초기 층: conv1, bn1, relu를 하나의 sequential로 묶습니다.
        layer0 = nn.Sequential(backbone.conv1, backbone.bn1, backbone.relu)
        # ResNet의 레이어들 (layer1 ~ layer4)를 저장
        layer1 = backbone.layer1
        layer2 = backbone.layer2
        layer3 = backbone.layer3
        layer4 = backbone.layer4

        # features는 layer0부터 layer3까지 연결한 것입니다.
        self.features = nn.Sequential(layer0, layer1, layer2, layer3)

        # upsampling 모듈: features의 출력 채널 수를 변경하고 활성화 함수(ReLU)를 적용합니다.
        self.upsampling= nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=1),
            nn.ReLU(inplace=True),
        )

        # extra 모듈: SSD에서는 다양한 크기의 특징맵(feature map)을 사용하기 위해 추가적인 계층을 만듭니다.
        # ModuleList에 여러 sequential 블록을 추가하여 점진적으로 다운샘플링 하면서 채널 수를 조정합니다.
        self.extra = nn.ModuleList(
            [
                # 첫 번째 extra block: layer4와 1x1 conv를 사용해 채널 수를 늘립니다.
# ... trimmed ...
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

### 모델 학습

`모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 가능한 파라미터만 모아서 optimizer에 전달, 총 10 에폭 동안 학습, tqdm으로 training loop 진행 상황 표시 흐름이 주석과 함께 드러납니다.

```python
from torch import optim
from tqdm import tqdm

# 학습 가능한 파라미터만 모아서 optimizer에 전달
params = [p for p in model.parameters() if p.requires_grad]
optimizer = optim.SGD(params, lr=0.001, momentum=0.9, weight_decay=0.0005)
lr_scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.1)

# 총 10 에폭 동안 학습
for epoch in range(10):
    train_cost = 0.0
    model.train()  # 학습 모드
    # tqdm으로 training loop 진행 상황 표시
    for images, targets in tqdm(train_dataloader, desc=f"Training Epoch {epoch+1}"):
        # 배치의 각 이미지와 어노테이션을 device(GPU/CPU)로 이동
        images = [image.to(device) for image in images]
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        # 모델에 입력하여 손실(loss) 계산
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())

        # 역전파 및 파라미터 업데이트
        optimizer.zero_grad()
        losses.backward()
        optimizer.step()

        # loss.item()을 사용하여 스칼라 값을 누적
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
