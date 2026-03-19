---
title: "GoogLeNet - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-5_GoogLeNet - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-5_GoogLeNet - 공유.md"
excerpt: "다음은 GoogLeNet 논문(“Going Deeper with Convolutions”, 2014)과 PyTorch 구현(예: torchvision의 구현) 간의 주요 차이점입니다(일부 항목은 구현에 따라 달라질 수 있음):"
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
| Code Blocks | 5 |
| Execution Cells | 3 |
| Libraries | `torch`, `torchvision`, `time`, `copy`, `torchinfo` |
| Source Note | `5-5_GoogLeNet - 공유` |

## What I Worked On

- BasicConv2d: 합성곱 + BatchNorm + ReLU (공식 구현 참고)
- Inception 모듈 (BasicConv2d 사용)
- Auxiliary Classifier (옵션)
- GoogLeNet (Inception v1) 모델 (공식 구현 참고)
- 사전 훈련된 모델

## Implementation Flow

1. BasicConv2d: 합성곱 + BatchNorm + ReLU (공식 구현 참고)
2. Inception 모듈 (BasicConv2d 사용)
3. Auxiliary Classifier (옵션)
4. GoogLeNet (Inception v1) 모델 (공식 구현 참고)
5. 사전 훈련된 모델
6. 출처

## Code Highlights

### import torch

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
