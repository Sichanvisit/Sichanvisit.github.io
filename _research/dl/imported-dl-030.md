---
title: "AlexNet - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-3_AlexNet - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-3_AlexNet - 공유.md"
excerpt: "당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU에는 10 GB 이상 메모리가 흔해 통합 구조가 더 단순·빠르다. PyTorch torchvision.models.alexnet은 저자가 단일 GPU용으로 다시..."
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 13 |
| Execution Cells | 9 |
| Libraries | `torch`, `torchinfo`, `torchvision`, `requests`, `PIL`, `io`, `matplotlib`, `time` |
| Source Note | `5-3_AlexNet - 공유` |

## What I Worked On

- AlexNet 구현
- 모델 인스턴스 생성 및 테스트 예시
- 사전 훈련된 모델 활용
- **AlexNet_Weights.IMAGENET1K_V1:**
- **모델 성능 (ImageNet-1K 기준)**

## Implementation Flow

1. AlexNet 구현
2. 모델 인스턴스 생성 및 테스트 예시
3. 사전 훈련된 모델 활용
4. **AlexNet_Weights.IMAGENET1K_V1:**
5. **모델 성능 (ImageNet-1K 기준)**
6. **추론(Inference) 변환**

## Code Highlights

### AlexNet 구현

```python
import torch
import torch.nn as nn

class AlexNet(nn.Module):
    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            # 첫 번째 Convolution: 입력 채널 3, 출력 채널 64, 커널 크기 11, stride 4, padding 2
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),

            # 두 번째 Convolution: 입력 64, 출력 192, 커널 크기 5, padding 2
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),

            # 세 번째 Convolution: 입력 192, 출력 384, 커널 크기 3, padding 1
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),

            # 네 번째 Convolution: 입력 384, 출력 256, 커널 크기 3, padding 1
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),

            # 다섯 번째 Convolution: 입력 256, 출력 256, 커널 크기 3, padding 1
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
# ... trimmed ...
```

### 실습 단계

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torchvision.models import alexnet
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import time
import copy
import os

# GPU 사용 가능 여부 확인
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# --- 1. 데이터셋 다운로드 및 전처리 ---
print("\n--- 1. CIFAR-10 데이터셋 다운로드 및 전처리 ---")

# 데이터 전처리: 이미지 크기 조정, 데이터 증강, 텐서 변환, 정규화
transform_train = transforms.Compose([
    transforms.Resize(224), # AlexNet 입력 크기에 맞춤 (ImageNet 학습 시 사용된 크기)
    transforms.RandomHorizontalFlip(), # 데이터 증강: 이미지를 무작위로 수평 뒤집기
    transforms.ToTensor(), # 이미지를 PyTorch 텐서로 변환
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)) # CIFAR-10 평균 및 표준편차로 정규화
])

transform_val = transforms.Compose([
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/5-3_AlexNet - 공유.md`
- Source formats: `md`
- Companion files: `5-3_AlexNet - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `pytorch.org`, `www.cs.toronto.edu`, `localhost`, `docs.pytorch.org`, `raw.githubusercontent.com`

## Note Preview

> -
> 당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU에는 10 GB 이상 메모리가 흔해 통합 구조가 더 단순·빠르다. PyTorch torchvision.models.alexnet은 저자가 단일 GPU용으로 다시 공개한 Caffe 모델을 그대로 옮긴 버전
