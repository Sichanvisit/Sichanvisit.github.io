---
title: "SSD"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-3_SSD"
source_path: "12_Deep_Learning/Code_Snippets/6-3_SSD.md"
excerpt: "먼저, ResNet과 같이 사전 학습된 네트워크의 일부 층을 사용하여 SSD의 특징 추출기(backbone)를 구성합니다."
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

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

## What I Worked On

- 먼저, 압축 파일(pytorch-transformer.zip)을 지정된 경로(현재 디렉토리)로 압축 해제합니다.
- 작업 디렉토리를 변경합니다.
- SSD 백본(Backbone) 정의
- 모델과 앵커 생성자(Anchor Generator) 초기화
- 사전 학습된 ResNet34 모델을 불러옵니다.

## Implementation Flow

1. 먼저, 압축 파일(pytorch-transformer.zip)을 지정된 경로(현재 디렉토리)로 압축 해제합니다.
2. 작업 디렉토리를 변경합니다.
3. SSD 백본(Backbone) 정의
4. 모델과 앵커 생성자(Anchor Generator) 초기화
5. 사전 학습된 ResNet34 모델을 불러옵니다.
6. 위에서 정의한 SSDBackbone으로 ResNet34의 일부 층을 래핑합니다.

## Code Highlights

### COCO 데이터셋 클래스 정의

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
