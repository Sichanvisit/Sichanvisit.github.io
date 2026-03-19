---
title: "AlexNet"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)AlexNet"
source_path: "12_Deep_Learning/Code_Snippets/(실습)AlexNet.md"
excerpt: "당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU에는 10 GB 이상 메모리가 흔해 통합 구조가 더 단순·빠르다. PyTorch torchvision.models.alexnet은 저자가 단일 GPU용으로 다시..."
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
| Code Blocks | 7 |
| Execution Cells | 7 |
| Libraries | `torch`, `torchinfo`, `torchvision`, `requests`, `PIL`, `io`, `matplotlib` |
| Source Note | `(실습)AlexNet` |

## What I Worked On

- alexnet.py
- from alexnet import AlexNet
- **AlexNet_Weights.IMAGENET1K_V1:**
- **모델 성능 (ImageNet-1K 기준)**
- **추론(Inference) 변환**

## Implementation Flow

1. alexnet.py
2. from alexnet import AlexNet
3. **AlexNet_Weights.IMAGENET1K_V1:**
4. **모델 성능 (ImageNet-1K 기준)**
5. **추론(Inference) 변환**
6. 이미지 다운로드

## Code Highlights

### alexnet.py

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

### **추론(Inference) 변환**

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
