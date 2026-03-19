---
title: "AlexNet - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-3_AlexNet - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-3_AlexNet - 공유.md"
excerpt: "당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다"
research_summary: "당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU에는 10 GB 이상 메모리가 흔해 통합 구조가 더 단순·빠르다. PyTorch torchvision.models.alexnet은 저자가 단일 GPU용으로 다시 공개한 Caffe 모델을 그대로 옮긴 버전. 파이토치에서 제공하는 알렉스넷 모델 : https://pytorch.org/vision/main/models/generated/torchvision.models.alexnet.html. `md` 원본과 13개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, torchvision, requests입니다."
research_artifacts: "md · 코드 13개 · 실행 9개"
code_block_count: 13
execution_block_count: 9
research_focus:
  - "당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU..."
  - "AlexNet 구현"
  - "파이토치에서 제공하는 알렉스넷 모델"
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
  - shared-note
---

당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU에는 10 GB 이상 메모리가 흔해 통합 구조가 더 단순·빠르다. PyTorch torchvision.models.alexnet은 저자가 단일 GPU용으로 다시 공개한 Caffe 모델을 그대로 옮긴 버전. 파이토치에서 제공하는 알렉스넷 모델 : https://pytorch.org/vision/main/models/generated/torchvision.models.alexnet.html. `md` 원본과 13개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, torchvision, requests입니다.

**빠르게 볼 수 있는 포인트**: 당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를..., AlexNet 구현, 파이토치에서 제공하는 알렉스넷 모델.

**남겨둔 자료**: `md` 원본과 13개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, torchvision, requests입니다.

**주요 스택**: `torch`, `torchinfo`, `torchvision`, `requests`, `PIL`

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

## What This Note Covers

### AlexNet 구현

당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU에는 10 GB 이상 메모리가 흔해 통합 구조가 더 단순·빠르다. PyTorch torchvision.models.alexnet은 저자가 단일 GPU용으로 다시 공개한 Caffe 모델을 그대로 옮긴 버전

### 사전 훈련된 모델 활용

파이토치에서 제공하는 알렉스넷 모델 : https://pytorch.org/vision/main/models/generated/torchvision.models.alexnet.html

### AlexNet_Weights.IMAGENET1K_V1

이 가중치는 논문의 결과를 간단한 학습 방법을 사용하여 거의 동일하게 재현한 것입니다. 또한 AlexNet_Weights.DEFAULT로도 제공됩니다.

### 모델 성능 (ImageNet-1K 기준)

Top-1 정확도 (acc@1): 56.522% - Top-5 정확도 (acc@5): 79.066% - 총 파라미터 수: 61,100,840 - 최소 입력 이미지 크기: 높이 63px, 너비 63px - 분류 가능한 카테고리: - 예시: tench(숭어), goldfish(금붕어), great white shark(백상아리) 등 (총 1000개 중 997개 생략) - 학습 방법 (rec...

## Implementation Flow

1. AlexNet 구현: 당시 GTX 580 3 GB 두 장으로만 훈련 가능해 모델 파라미터를 반씩 나눠 실행했다. 현대 GPU에는 10 GB 이상 메모리가 흔해 통합 구조가 더 단순·빠르다. PyTorch torchvision.models.alexnet은 저자가 단일 GPU용으로 다시 공개한 Caff...
2. 사전 훈련된 모델 활용: 파이토치에서 제공하는 알렉스넷 모델 : https://pytorch.org/vision/main/models/generated/torchvision.models.alexnet.html
3. AlexNet_Weights.IMAGENET1K_V1: 이 가중치는 논문의 결과를 간단한 학습 방법을 사용하여 거의 동일하게 재현한 것입니다. 또한 AlexNet_Weights.DEFAULT로도 제공됩니다.
4. 모델 성능 (ImageNet-1K 기준): Top-1 정확도 (acc@1): 56.522% - Top-5 정확도 (acc@5): 79.066% - 총 파라미터 수: 61,100,840 - 최소 입력 이미지 크기: 높이 63px, 너비 63px - 분류 가능한 카테고리: - 예시: tench(숭어),...

## Code Highlights

### AlexNet 구현

`AlexNet 구현`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 첫 번째 Convolution: 입력 채널 3, 출력 채널 64, 커널 크기 11, st..., 두 번째 Convolution: 입력 64, 출력 192, 커널 크기 5, padding 2, 세 번째 Convolution: 입력 192, 출력 384, 커널 크기 3, padding 1 흐름이 주석과 함께 드러납니다.

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

`실습 단계`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 GPU 사용 가능 여부 확인, 데이터셋 다운로드 및 전처리, 데이터 전처리: 이미지 크기 조정, 데이터 증강, 텐서 변환, 정규화 흐름이 주석과 함께 드러납니다.

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
