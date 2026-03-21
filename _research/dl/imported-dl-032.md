---
title: "GoogLeNet - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-5_GoogLeNet - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-5_GoogLeNet - 공유.md"
excerpt: "다음은 GoogLeNet 논문(“Going Deeper with Convolutions”, 2014)과 PyTorch 구현(예: torchvision의 구현) 간의 주요 차이점입니다(일부 항목은 구현에 따라 달라질 수 있음)"
research_summary: "다음은 GoogLeNet 논문(“Going Deeper with Convolutions”, 2014)과 PyTorch 구현(예: torchvision의 구현) 간의 주요 차이점입니다(일부 항목은 구현에 따라 달라질 수 있음). https://pytorch.org/vision/main/models/generated/torchvision.models.googlenet.html#torchvision.models.GoogLeNet_Weights. `md` 원본과 5개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, time, copy입니다."
research_artifacts: "md · 코드 5개 · 실행 3개"
code_block_count: 5
execution_block_count: 3
research_focus:
  - "다음은 GoogLeNet 논문(“Going Deeper with Convolutions”, 2014)과..."
  - "https"
  - "사전 훈련된 모델"
research_stack:
  - "torch"
  - "torchvision"
  - "time"
  - "copy"
  - "torchinfo"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

다음은 GoogLeNet 논문(“Going Deeper with Convolutions”, 2014)과 PyTorch 구현(예: torchvision의 구현) 간의 주요 차이점입니다(일부 항목은 구현에 따라 달라질 수 있음). https://pytorch.org/vision/main/models/generated/torchvision.models.googlenet.html#torchvision.models.GoogLeNet_Weights. `md` 원본과 5개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, time, copy입니다.

**빠르게 볼 수 있는 포인트**: 다음은 GoogLeNet 논문(“Going Deeper with Con..., https, 사전 훈련된 모델.

**남겨둔 자료**: `md` 원본과 5개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, time, copy입니다.

**주요 스택**: `torch`, `torchvision`, `time`, `copy`, `torchinfo`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 5 |
| Execution Cells | 3 |
| Libraries | `torch`, `torchvision`, `time`, `copy`, `torchinfo` |
| Source Note | `5-5_GoogLeNet - 공유` |

## What This Note Covers

### Overview

다음은 GoogLeNet 논문(“Going Deeper with Convolutions”, 2014)과 PyTorch 구현(예: torchvision의 구현) 간의 주요 차이점입니다(일부 항목은 구현에 따라 달라질 수 있음)

### 사전 훈련된 모델

https://pytorch.org/vision/main/models/generated/torchvision.models.googlenet.html#torchvision.models.GoogLeNet_Weights

### 출처

https://pytorch.org/vision/0.8/_modules/torchvision/models/googlenet.html#googlenet - https://pytorch.org/vision/0.8/models.html#id1

### Key Step

BasicConv2d: 합성곱 + BatchNorm + ReLU (공식 구현 참고)

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

1. Overview: 다음은 GoogLeNet 논문(“Going Deeper with Convolutions”, 2014)과 PyTorch 구현(예: torchvision의 구현) 간의 주요 차이점입니다(일부 항목은 구현에 따라 달라질 수 있음)
2. 사전 훈련된 모델: https://pytorch.org/vision/main/models/generated/torchvision.models.googlenet.html#torchvision.models.GoogLeNet_Weights
3. 출처: https://pytorch.org/vision/0.8/_modules/torchvision/models/googlenet.html#googlenet - https://pytorch.org/vision/0.8/models.html#id1
4. Key Step: BasicConv2d: 합성곱 + BatchNorm + ReLU (공식 구현 참고)

## Code Highlights

### import torch

`import torch`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 BasicConv2d: 합성곱 + BatchNorm + ReLU (공식 구현 참고), Inception 모듈 (BasicConv2d 사용), Auxiliary Classifier (옵션) 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import time
import copy

# --------------------------
# BasicConv2d: 합성곱 + BatchNorm + ReLU (공식 구현 참고)
# --------------------------
class BasicConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, **kwargs):
        super(BasicConv2d, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, bias=False, **kwargs)
        self.bn = nn.BatchNorm2d(out_channels, eps=0.001)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return F.relu(x, inplace=True)

# --------------------------
# Inception 모듈 (BasicConv2d 사용)
# --------------------------
class Inception(nn.Module):
# ... trimmed ...
```

### --------------------------

`--------------------------`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 GoogLeNet (Inception v1) 모델 (공식 구현 참고), (필요 시 입력 변환 코드 추가), 224x224 크기의 입력을 예상 흐름이 주석과 함께 드러납니다.

```python
# --------------------------
# GoogLeNet (Inception v1) 모델 (공식 구현 참고)
# --------------------------
class GoogLeNet(nn.Module):
    def __init__(self, num_classes=10, aux_logits=False, transform_input=False):
        super(GoogLeNet, self).__init__()
        self.aux_logits = aux_logits
        self.transform_input = transform_input

        self.conv1 = BasicConv2d(3, 64, kernel_size=7, stride=2, padding=3)
        self.maxpool1 = nn.MaxPool2d(kernel_size=3, stride=2, ceil_mode=True)
        self.conv2 = BasicConv2d(64, 64, kernel_size=1)
        self.conv3 = BasicConv2d(64, 192, kernel_size=3, padding=1)
        self.maxpool2 = nn.MaxPool2d(kernel_size=3, stride=2, ceil_mode=True)

        self.inception3a = Inception(192, 64, 96, 128, 16, 32, 32)      # 출력: 256 채널
        self.inception3b = Inception(256, 128, 128, 192, 32, 96, 64)     # 출력: 480 채널
        self.maxpool3 = nn.MaxPool2d(kernel_size=3, stride=2, ceil_mode=True)

        self.inception4a = Inception(480, 192, 96, 208, 16, 48, 64)      # 출력: 512 채널
        self.inception4b = Inception(512, 160, 112, 224, 24, 64, 64)     # 출력: 512 채널
        self.inception4c = Inception(512, 128, 128, 256, 24, 64, 64)     # 출력: 512 채널
        self.inception4d = Inception(512, 112, 144, 288, 32, 64, 64)     # 출력: 528 채널
        self.inception4e = Inception(528, 256, 160, 320, 32, 128, 128)    # 출력: 832 채널
        self.maxpool4 = nn.MaxPool2d(kernel_size=3, stride=2, ceil_mode=True)

        self.inception5a = Inception(832, 256, 160, 320, 32, 128, 128)    # 출력: 832 채널
        self.inception5b = Inception(832, 384, 192, 384, 48, 128, 128)    # 출력: 1024 채널
# ... trimmed ...
```

### 사전 훈련된 모델

`사전 훈련된 모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. https://pytorch.org/vision/main/models/generated/torchvision.models.googlenet.html#torchvision.models.GoogLeNet_Weights.

```python
from torchinfo import summary
num_classes = 10

model = GoogLeNet(num_classes=num_classes, aux_logits=False)
summary(model, input_size=(2,3,224,224), device='cpu')
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/5-5_GoogLeNet - 공유.md`
- Source formats: `md`
- Companion files: `5-5_GoogLeNet - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `pytorch.org`

## Note Preview

> 다음은 GoogLeNet 논문(“Going Deeper with Convolutions”, 2014)과 PyTorch 구현(예: torchvision의 구현) 간의 주요 차이점입니다(일부 항목은 구현에 따라 달라질 수 있음):
> - Batch Normalization 사용
