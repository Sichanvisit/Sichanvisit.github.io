---
title: "FCN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)FCN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)FCN.md"
excerpt: "모델 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 순서로 핵심 장면을 먼저 훑고, @title VOCSegmentatio..., @title 시각화 함수, 모델 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md`..."
research_summary: "모델 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 순서로 핵심 장면을 먼저 훑고, @title VOCSegmentatio..., @title 시각화 함수, 모델 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 12개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다."
research_artifacts: "md · 코드 12개 · 실행 12개"
code_block_count: 12
execution_block_count: 12
research_focus:
  - "모델"
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
  - archive-note
---

모델 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 순서로 핵심 장면을 먼저 훑고, @title VOCSegmentatio..., @title 시각화 함수, 모델 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 12개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: 모델.

**남겨둔 자료**: `md` 원본과 12개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**주요 스택**: `os`, `json`, `torch`, `numpy`, `PIL`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 12 |
| Execution Cells | 12 |
| Libraries | `os`, `json`, `torch`, `numpy`, `PIL`, `torchvision`, `matplotlib`, `tqdm` |
| Source Note | `(실습)FCN` |

## What This Note Covers

### 모델

모델 코드를 직접 따라가며 모델 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

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

1. 모델: 모델 코드를 직접 따라가며 모델 흐름을 확인했습니다.

## Code Highlights

### @title VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기

`@title VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기, train==True 이면 train 아니면 val, torchvision에서 데이터셋 다운로드 흐름이 주석과 함께 드러납니다.

```python
#@title VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기
class SegmentationDataset(Dataset):
    def __init__(self, root, train=True, transform=None, target_transform=None, download=False):

        # train==True 이면 train 아니면 val
        image_set = 'train' if train else 'val'

        #torchvision에서 데이터셋 다운로드
        self.voc = datasets.VOCSegmentation(
            root=root,
            year='2012',
            image_set=image_set,
            download=download
        )

        # VOC 데이터셋 내에 클래스 정보를 담고있는 json 파일 위치
        classes_json_path = os.path.join(root, "VOCdevkit", "VOC2012", "classes.json")
        if os.path.exists(classes_json_path):
            with open(classes_json_path, 'r') as file:
                self.categories = json.load(file)
        else:
            self.categories = {str(i): {"class": f"class_{i}",
                                        "color": [i * 10 % 256, i * 20 % 256, i * 30 % 256]}
                                for i in range(1,22)}

        self.transform = transform
        self.target_transform = target_transform

# ... trimmed ...
```

### @title 시각화 함수

`@title 시각화 함수`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 시각화 함수, 내부함수 : 마스크에 클래스별 색상을 추가, (1,H,W) --> (H,W) 흐름이 주석과 함께 드러납니다.

```python
#@title 시각화 함수
def draw_mask(images, masks, outputs=None, plot_size=4):

    #내부함수 : 마스크에 클래스별 색상을 추가
    def color_mask(image, target):
        # (1,H,W) --> (H,W)
        m = target.squeeze().numpy().astype(np.uint8)

        # image와 같은 크기의 빈(데이터가 0인) 이미지
        cm = np.zeros_like(image, dtype=np.uint8)

        # 클래스 1~20번 까지 색상을 cm에 적용
        for i in range(1,21):
            cm[m == i] = train_dataset.categories.get(str(i),{"color":[0,0,0]})['color']

        classes = [train_dataset.categories.get(str(idx), {"class":f"class_{idx}"})["class"]
                   for idx in np.unique(m)]
        return cm, classes

    col = 3 if outputs is not None else 2
    figsize = 8 if outputs is not None else 12
    fig, ax = plt.subplots(plot_size, col, figsize=(14, figsize))

    for batch in range(plot_size):
        im = images[batch].numpy().transpose(1,2,0) # (c,h,w) --> (h,w,c)
        ax[batch][0].imshow(im)
        ax[batch][0].set_title("Origin")
        ax[batch][0].axis('off')
# ... trimmed ...
```

### 모델

`모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 FCN-8s --> backbone : VGG16, VGG16에서 중간 feature를 추출, pool3 : features[0:17] 약(1/8 해상도) 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
from tqdm import tqdm
import numpy as np

# FCN-8s --> backbone : VGG16
class FCN8s(nn.Module):
    def __init__(self, num_classes=21):
        super().__init__()
        vgg16 = models.vgg16(pretrained=True)
        features = list(vgg16.features.children())

        #VGG16에서 중간 feature를 추출
        #pool3 : features[0:17] 약(1/8 해상도)
        #pool4 : features[17:24] (1/16)
        #pool5 : features[24:]   (1/32)
        self.pool3 = nn.Sequential(*features[:17])
        self.pool4 = nn.Sequential(*features[17:24])
        self.pool5 = nn.Sequential(*features[24:])

        # 1x1 conv로 ch수를 조정
        self.score_pool3 = nn.Conv2d(256, num_classes, kernel_size=1)
        self.score_pool4 = nn.Conv2d(512, num_classes, kernel_size=1)
        self.score_fr    = nn.Conv2d(512, num_classes, kernel_size=1)

        # Transposed conv
# ... trimmed ...
```

### 모델

`모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 mask는 다음 형태로 (B, H, W) 흐름이 주석과 함께 드러납니다.

```python
num_classes = 21
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = FCN8s(num_classes=num_classes).to(device)

optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9, weight_decay=0.0005)
criterion = nn.CrossEntropyLoss()

num_epochs=10
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0

    for images, targets in tqdm(train_dataloader, desc=f"Epoch {epoch+1}/{num_epochs}"):
        images = images.to(device)
        targets = targets.to(device)

        if targets.dim() == 4 and targets.size(1)==1:
            targets = targets.squeeze(1)
            # mask는 다음 형태로 (B, H, W)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    avg_loss = running_loss / len(train_dataloader)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)FCN.md`
- Source formats: `md`
- Companion files: `(실습)FCN.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2025.10.1,2,13,14.md`, `12_Deep_Learning_Code_Summary.md`
- External references: `data.brainchip.com`, `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
