---
title: "FCN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)FCN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)FCN.md"
excerpt: "모델, FCN-8s --> backbone 중심으로 구현 과정을 정리한 FCN 기록입니다"
research_summary: "모델, FCN-8s --> backbone 중심으로 구현 과정을 정리한 FCN 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 12개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다."
research_artifacts: "md · 코드 12개 · 실행 12개"
code_block_count: 12
execution_block_count: 12
research_focus:
  - "모델"
  - "FCN-8s --> backbone"
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

모델, FCN-8s --> backbone 중심으로 구현 과정을 정리한 FCN 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 12개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: 모델, FCN-8s --> backbone.

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

- 모델
- FCN-8s --> backbone

## Implementation Flow

1. Key Step: FCN-8s --> backbone : VGG16

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
