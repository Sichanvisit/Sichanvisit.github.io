---
title: "YOLOv2"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-4_YOLOv2"
source_path: "12_Deep_Learning/Code_Snippets/6-4_YOLOv2.md"
excerpt: "DL Archive Note: Space-to-Depth 변환 (passthrough 연결), Darknet-19 Backbone (YOLOv2의 기반 네트워크), YOLOv2 전체 모델 (Darknet-19 + passthrough + detection head)"
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
| Code Blocks | 6 |
| Execution Cells | 5 |
| Libraries | `torch`, `torchinfo` |
| Source Note | `6-4_YOLOv2` |

## What I Worked On

- Space-to-Depth 변환 (passthrough 연결)
- Darknet-19 Backbone (YOLOv2의 기반 네트워크)
- YOLOv2 전체 모델 (Darknet-19 + passthrough + detection head)
- 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)

## Implementation Flow

1. Space-to-Depth 변환 (passthrough 연결)
2. Darknet-19 Backbone (YOLOv2의 기반 네트워크)
3. YOLOv2 전체 모델 (Darknet-19 + passthrough + detection head)
4. 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)

## Code Highlights

### import torch

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

# Space-to-Depth 변환 (passthrough 연결)
class SpaceToDepth(nn.Module):
    def __init__(self, block_size):
        super(SpaceToDepth, self).__init__()
        self.block_size = block_size

    def forward(self, x):
        # x: [batch, C, H, W]
        batch, channels, height, width = x.size()
        new_h = height // self.block_size
        new_w = width // self.block_size
        x = x.view(batch, channels, new_h, self.block_size, new_w, self.block_size)
        x = x.permute(0, 3, 5, 1, 2, 4).contiguous()
        x = x.view(batch, channels * (self.block_size ** 2), new_h, new_w)
        return x

# Darknet-19 Backbone (YOLOv2의 기반 네트워크)
class Darknet19(nn.Module):
    def __init__(self):
        super(Darknet19, self).__init__()
        # Layer1: 416x416 -> 208x208
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1, bias=False),
            nn.BatchNorm2d(32),
# ... trimmed ...
```

### class YOLOv2Loss(nn.Module)

```python
class YOLOv2Loss(nn.Module):
    def __init__(self, anchors, num_classes, img_size, lambda_coord=5, lambda_noobj=0.5):
        """
        anchors: [(w, h), ...] 원본 이미지 기준 앵커 박스 크기
        num_classes: 클래스 수
        img_size: 입력 이미지의 크기 (정방형, 예: 416)
        lambda_coord: 좌표 손실 가중치
        lambda_noobj: 물체가 없는 경우의 confidence 손실 가중치
        """
        super(YOLOv2Loss, self).__init__()
        self.anchors = anchors
        self.num_anchors = len(anchors)
        self.num_classes = num_classes
        self.img_size = img_size
        self.lambda_coord = lambda_coord
        self.lambda_noobj = lambda_noobj

    def forward(self, predictions, target):
        """
        predictions: (batch, A*(5+num_classes), grid_h, grid_w)
        target: (batch, grid_h, grid_w, A, 5+num_classes)
          - target[..., 0:4]: 정규화된 box 좌표 (center_x, center_y, w, h)
          - target[..., 4]: 객체 존재 여부 (1 또는 0)
          - target[..., 5:]: one-hot 인코딩된 클래스 벡터

        **주의:** 실제 YOLOv2는 ground truth를 앵커별로 할당하는 전처리 과정이 필요합니다.
        여기서는 target이 이미 해당 형식으로 준비되었다고 가정합니다.
        """
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/6-4_YOLOv2.md`
- Source formats: `md`
- Companion files: `6-4_YOLOv2.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
