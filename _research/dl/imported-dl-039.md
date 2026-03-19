---
title: "YOLOv3"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-5_YOLOv3"
source_path: "12_Deep_Learning/Code_Snippets/6-5_YOLOv3.md"
excerpt: "- 실제 훈련을 시키고 싶다면 아래 github 구현체를 확인해보세요 : https://github.com/eriklindernoren/PyTorch-YOLOv3/blob/master/pytorchyolo/models.py"
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
| Code Blocks | 5 |
| Execution Cells | 5 |
| Libraries | `torch`, `torchinfo` |
| Source Note | `6-5_YOLOv3` |

## What I Worked On

- 기본 Residual Block (Darknet-53 구성 요소)
- Darknet-53 백본
- YOLOv3 Detection Head (각 스케일별 예측 모듈)
- YOLOv3 전체 모델
- 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)

## Implementation Flow

1. 기본 Residual Block (Darknet-53 구성 요소)
2. Darknet-53 백본
3. YOLOv3 Detection Head (각 스케일별 예측 모듈)
4. YOLOv3 전체 모델
5. 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)
6. 간단한 테스트

## Code Highlights

### import torch

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

### import torch

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
