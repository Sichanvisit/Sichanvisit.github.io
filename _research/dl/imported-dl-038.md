---
title: "YOLOv2"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-4_YOLOv2"
source_path: "12_Deep_Learning/Code_Snippets/6-4_YOLOv2.md"
excerpt: "Space-to-Depth 변환 (passth..., Darknet-19 Backbone (YOLO..., YOLOv2 전체 모델 (Darknet-19.."
research_summary: "Space-to-Depth 변환 (passth..., Darknet-19 Backbone (YOLO..., YOLOv2 전체 모델 (Darknet-19... 중심으로 구현 과정을 정리한 YOLOv2 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 6개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다."
research_artifacts: "md · 코드 6개 · 실행 5개"
code_block_count: 6
execution_block_count: 5
research_focus:
  - "Space-to-Depth 변환 (passthrough 연결)"
  - "Darknet-19 Backbone (YOLOv2의 기반 네트워크)"
  - "YOLOv2 전체 모델 (Darknet-19 + passthrough + detectio..."
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

Space-to-Depth 변환 (passth..., Darknet-19 Backbone (YOLO..., YOLOv2 전체 모델 (Darknet-19... 중심으로 구현 과정을 정리한 YOLOv2 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 6개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다.

**빠르게 볼 수 있는 포인트**: Space-to-Depth 변환 (passthrough 연결), Darknet-19 Backbone (YOLOv2의 기반 네트워크), YOLOv2 전체 모델 (Darknet-19 + passthrough....

**남겨둔 자료**: `md` 원본과 6개 코드 블록, 5개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다.

**주요 스택**: `torch`, `torchinfo`

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

## What This Note Covers

- Space-to-Depth 변환 (passthrough 연결)
- Darknet-19 Backbone (YOLOv2의 기반 네트워크)
- YOLOv2 전체 모델 (Darknet-19 + passthrough + detectio...
- 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)

## Why This Matters

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. Key Step: Space-to-Depth 변환 (passthrough 연결)
2. Key Step: Darknet-19 Backbone (YOLOv2의 기반 네트워크)
3. Key Step: YOLOv2 전체 모델 (Darknet-19 + passthrough + detection head)
4. Key Step: 모델 요약 정보 출력 (배치 크기 1, 입력 크기 3x416x416)

## Code Highlights

### import torch

`import torch`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Space-to-Depth 변환 (passthrough 연결), x: [batch, C, H, W], Darknet-19 Backbone (YOLOv2의 기반 네트워크) 흐름이 주석과 함께 드러납니다.

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

### model = YOLOv2(num_classes=20, num_anchors=5)

`model = YOLOv2(num_classes=20, num_anchors=5)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
model = YOLOv2(num_classes=20, num_anchors=5)
x = torch.randn(1, 3, 416, 416)
output = model(x)
print(output.shape)  # 예상: [1, num_anchors*(5+num_classes), 13, 13]
```

### class YOLOv2Loss(nn.Module)

`class YOLOv2Loss(nn.Module)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 predictions를 (batch, grid_h, grid_w, A, 5+num_cla..., prediction shape: (batch, grid_h, grid_w, A, 5+nu..., 예측값 분리 및 활성화 함수 적용 흐름이 주석과 함께 드러납니다.

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

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
