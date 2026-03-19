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
