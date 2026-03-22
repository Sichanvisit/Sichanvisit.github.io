---
title: "YOLOv3"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-5_YOLOv3"
source_path: "12_Deep_Learning/Code_Snippets/6-5_YOLOv3.md"
excerpt: "YOLOv3에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, import torch, model = YOLOv3(num_cl..., from torchinfo import... 같은 코드로 실제 구현을 이어서 확인할 수..."
research_summary: "YOLOv3에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, import torch, model = YOLOv3(num_cl..., from torchinfo import... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 5개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다."
research_artifacts: "md · 코드 5개 · 실행 5개"
code_block_count: 5
execution_block_count: 5
research_focus:
  - "기본 Residual Block (Darknet-53 구성 요소)"
  - "실제 훈련을 시키고 싶다면 아래 github 구현체를 확인해보세요 : https://github.com..."
  - "Darknet-53 백본"
research_stack:
  - "torch"
  - "torchinfo"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

YOLOv3에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, import torch, model = YOLOv3(num_cl..., from torchinfo import... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 5개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다.

**빠르게 볼 수 있는 포인트**: 기본 Residual Block (Darknet-53 구성 요소), 실제 훈련을 시키고 싶다면 아래 github 구현체를 확인해보세요 :..., Darknet-53 백본.

**남겨둔 자료**: `md` 원본과 5개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다.

**주요 스택**: `torch`, `torchinfo`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 5 |
| Execution Cells | 5 |
| Libraries | `torch`, `torchinfo` |
| Source Note | `6-5_YOLOv3` |

## What This Note Covers

### Overview

실제 훈련을 시키고 싶다면 아래 github 구현체를 확인해보세요 : https://github.com/eriklindernoren/PyTorch-YOLOv3/blob/master/pytorchyolo/models.py

### Key Step

기본 Residual Block (Darknet-53 구성 요소)

### Key Step

YOLOv3 Detection Head (각 스케일별 예측 모듈)

### Key Step

모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)

## Why This Matters

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. Overview: 실제 훈련을 시키고 싶다면 아래 github 구현체를 확인해보세요 : https://github.com/eriklindernoren/PyTorch-YOLOv3/blob/master/pytorchyolo/models.py
2. Key Step: 기본 Residual Block (Darknet-53 구성 요소)
3. Key Step: YOLOv3 Detection Head (각 스케일별 예측 모듈)
4. Key Step: 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)

## Code Highlights

### import torch

`import torch`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기본 Residual Block (Darknet-53 구성 요소), Darknet-53 백본, Downsampling + residual blocks (논문에 따른 반복 횟수) 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# ---------------------------
# 기본 Residual Block (Darknet-53 구성 요소)
# ---------------------------
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, hidden_channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, hidden_channels, kernel_size=1, bias=False)
        self.bn1 = nn.BatchNorm2d(hidden_channels)
        self.conv2 = nn.Conv2d(hidden_channels, in_channels, kernel_size=3, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(in_channels)
        self.leaky = nn.LeakyReLU(0.1)

    def forward(self, x):
        residual = x
        out = self.leaky(self.bn1(self.conv1(x)))
        out = self.leaky(self.bn2(self.conv2(out)))
        return out + residual

# ---------------------------
# Darknet-53 백본
# ---------------------------
class Darknet53(nn.Module):
    def __init__(self):
        super(Darknet53, self).__init__()
# ... trimmed ...
```

### model = YOLOv3(num_classes=80, num_anchors=3)

`model = YOLOv3(num_classes=80, num_anchors=3)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
model = YOLOv3(num_classes=80, num_anchors=3)
x = torch.randn(1, 3, 416, 416)
outputs = model(x)
print("Small scale output shape (13x13):", outputs[0].shape)
print("Medium scale output shape (26x26):", outputs[1].shape)
print("Large scale output shape (52x52):", outputs[2].shape)
```

### from torchinfo import summary

`from torchinfo import summary`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416) 흐름이 주석과 함께 드러납니다.

```python
from torchinfo import summary

# 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)
summary(model, input_size=(1, 3, 416, 416))
```

### import torch

`import torch`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 좌표에 대해서는 MSE Loss, confidence와 클래스에 대해서는 BCE Loss..., 각 스케일별로 손실을 계산하여 합산, pred: (batch, grid_h, grid_w, num_anchors, 5+num_... 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class YOLOv3Loss(nn.Module):
    def __init__(self, num_classes, lambda_coord=5, lambda_noobj=0.5):
        """
        num_classes: 클래스 수
        lambda_coord: 좌표 손실 가중치
        lambda_noobj: 물체가 없는 영역에 대한 confidence 손실 가중치
        """
        super(YOLOv3Loss, self).__init__()
        self.num_classes = num_classes
        self.lambda_coord = lambda_coord
        self.lambda_noobj = lambda_noobj

        # 좌표에 대해서는 MSE Loss, confidence와 클래스에 대해서는 BCE Loss 사용 (sum reduction)
        self.mse_loss = nn.MSELoss(reduction='sum')
        self.bce_loss = nn.BCEWithLogitsLoss(reduction='sum')

    def forward(self, predictions, targets):
        """
        predictions: 리스트, 각 원소는 한 스케일의 예측 결과로
                     shape = (batch, grid_h, grid_w, num_anchors, 5 + num_classes)
        targets: 리스트, predictions와 동일한 shape로 target 값들이 준비되어 있음.
                 target[..., :2] : cell 내에서 정규화된 x, y (sigmoid 적용 전 값)
                 target[..., 2:4] : w, h (이미 적절히 전처리된 값)
                 target[..., 4] : object 존재 여부 (1 또는 0)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/6-5_YOLOv3.md`
- Source formats: `md`
- Companion files: `6-5_YOLOv3.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `github.com`

## Note Preview

> -
> - 실제 훈련을 시키고 싶다면 아래 github 구현체를 확인해보세요 : https://github.com/eriklindernoren/PyTorch-YOLOv3/blob/master/pytorchyolo/models.py
