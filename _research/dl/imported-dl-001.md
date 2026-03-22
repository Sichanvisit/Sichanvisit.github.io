---
title: "AlexNet"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)AlexNet"
source_path: "12_Deep_Learning/Code_Snippets/(실습)AlexNet.md"
excerpt: "추론(Inference) 변환, AlexNet_Weights.IMA... 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 추론(Inference) 변환, AlexNet_Weights.IMA... 순서로 핵심 장면을 먼저 훑고, ale..."
research_summary: "추론(Inference) 변환, AlexNet_Weights.IMA... 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 추론(Inference) 변환, AlexNet_Weights.IMA... 순서로 핵심 장면을 먼저 훑고, alexnet.py, 추론(Inference) 변환 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 7개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, torchvision, requests입니다."
research_artifacts: "md · 코드 7개 · 실행 7개"
code_block_count: 7
execution_block_count: 7
research_focus:
  - "추론(Inference) 변환"
  - "AlexNet_Weights.IMAGENET1K_V1"
research_stack:
  - "torch"
  - "torchinfo"
  - "torchvision"
  - "requests"
  - "PIL"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

추론(Inference) 변환, AlexNet_Weights.IMA... 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 추론(Inference) 변환, AlexNet_Weights.IMA... 순서로 핵심 장면을 먼저 훑고, alexnet.py, 추론(Inference) 변환 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 7개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, torchvision, requests입니다.

**빠르게 볼 수 있는 포인트**: 추론(Inference) 변환, AlexNet_Weights.IMAGENET1K_V1.

**남겨둔 자료**: `md` 원본과 7개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, torchvision, requests입니다.

**주요 스택**: `torch`, `torchinfo`, `torchvision`, `requests`, `PIL`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 7 |
| Execution Cells | 7 |
| Libraries | `torch`, `torchinfo`, `torchvision`, `requests`, `PIL`, `io`, `matplotlib` |
| Source Note | `(실습)AlexNet` |

## What This Note Covers

### 추론(Inference) 변환

AlexNet_Weights.IMAGENET1K_V1.transforms에서 제공하는 변환(transforms)은 다음과 같은 전처리 과정을 수행합니다. 입력 형식: - PIL.Image 객체 - 배치(batch) 형식: (B, C, H, W) - 단일(single) 이미지 형식: (C, H, W)

- 읽을 포인트: 예측 결과를 확인하고 어떤 부분이 잘 동작했는지 해석하는 구간입니다.

### AlexNet_Weights.IMAGENET1K_V1

이 가중치는 논문의 결과를 간단한 학습 방법을 사용하여 거의 동일하게 재현한 것입니다. 또한 AlexNet_Weights.DEFAULT로도 제공됩니다.

- 읽을 포인트: 세부 흐름: 모델 성능 (ImageNet-1K 기준)

#### 모델 성능 (ImageNet-1K 기준)

Top-1 정확도 (acc@1): 56.522% - Top-5 정확도 (acc@5): 79.066% - 총 파라미터 수: 61,100,840 - 최소 입력 이미지 크기: 높이 63px, 너비 63px - 분류 가능한 카테고리: - 예시: tench(숭어), goldfish(금붕어)...

## Why This Matters

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. 추론(Inference) 변환: AlexNet_Weights.IMAGENET1K_V1.transforms에서 제공하는 변환(transforms)은 다음과 같은 전처리 과정을 수행합니다. 입력 형식: - PIL.Image 객체 - 배치(batch) 형식: (B, C...
2. AlexNet_Weights.IMAGENET1K_V1: 모델 성능 (ImageNet-1K 기준)

## Code Highlights

### alexnet.py

`alexnet.py`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 alexnet.py, from alexnet import AlexNet, 1 conv :입력 3, 출력 64, 커널 11 stride 4, padding2 흐름이 주석과 함께 드러납니다.

```python
# alexnet.py
# from alexnet import AlexNet

import torch
import torch.nn as nn

class AlexNet(nn.Module):
    def __init__(self, num_classes=1000):
        super().__init__()
        self.features = nn.Sequential(
            # 1 conv :입력 3, 출력 64, 커널 11 stride 4, padding2
            nn.Conv2d(3,64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),

            # 2 conv : in 64, out 192, k=5, padding 2
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(True),
            nn.MaxPool2d(3,2),

            # 3 conv : in 192, out 384, k=3, padding=1
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(True),

            # 4 conv : in 384, out 256, k=3, padding=1
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(True),

# ... trimmed ...
```

### 추론(Inference) 변환

`추론(Inference) 변환`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 이러한 전처리는 모델이 학습된 데이터와 동일한 입력 형태를 유지하도록 하기 위해 필요합니다.

```python
from torchvision import models
model = models.alexnet(weights='AlexNet_Weights.IMAGENET1K_V1')
print(model)
```

### 추론(Inference) 변환

`추론(Inference) 변환`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 이러한 전처리는 모델이 학습된 데이터와 동일한 입력 형태를 유지하도록 하기 위해 필요합니다.

```python
import requests

url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"

response = requests.get(url)
print(response)

imagenet_classes = response.text.strip().split("\n")
print(imagenet_classes)
```

### 추론(Inference) 변환

`추론(Inference) 변환`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 이미지 다운로드, 이미지 시각화, 전처리 흐름이 주석과 함께 드러납니다.

```python
import torch
from torchvision import models, transforms
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

# 이미지 다운로드
url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPqUIvVs_Q2veVfJXJgmU4HqJDedpaLTb5Vg&s'
response = requests.get(url)
img = Image.open(BytesIO(response.content)).convert('RGB')

# 이미지 시각화
plt.figure(figsize=(6,6))
plt.imshow(img)
plt.axis('off')
plt.show()

# 전처리
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std = [0.229, 0.224, 0.225])
])

img_t = preprocess(img)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)AlexNet.md`
- Source formats: `md`
- Companion files: `(실습)AlexNet.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `pytorch.org`, `docs.pytorch.org`, `raw.githubusercontent.com`, `encrypted-tbn0.gstatic.com`

## Note Preview

> 당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU에는 10 GB 이상 메모리가 흔해 통합 구조가 더 단순·빠르다. PyTorch torchvision.models.alexnet은 저자가 단일 GPU용으로 다시 공개한 Caffe 모델을 그대로 옮긴 버전
> 파이토치에서 제공하는 알렉스넷 모델 : https://pytorch.org/vision/main/models/generated/torchvision.models.alexnet.html
