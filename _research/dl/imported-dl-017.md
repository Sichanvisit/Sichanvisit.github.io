---
title: "YOLOv1"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)YOLOv1"
source_path: "12_Deep_Learning/Code_Snippets/(실습)YOLOv1.md"
excerpt: "YOLOv1에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, 논문에 제시된 아키텍처 구성 (YOLOv1), class YOLOv1(nn.Module), @title NMS 같은 코드로 실제 구현을 이어서 확인할 수 있습니..."
research_summary: "YOLOv1에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, 논문에 제시된 아키텍처 구성 (YOLOv1), class YOLOv1(nn.Module), @title NMS 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 9개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch입니다."
research_artifacts: "md · 코드 9개 · 실행 9개"
code_block_count: 9
execution_block_count: 9
research_focus:
  - "YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의..."
  - "논문에 제시된 아키텍처 구성 (YOLOv1)"
research_stack:
  - "torch"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

YOLOv1에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, 논문에 제시된 아키텍처 구성 (YOLOv1), class YOLOv1(nn.Module), @title NMS 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 9개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch입니다.

**빠르게 볼 수 있는 포인트**: YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fu..., 논문에 제시된 아키텍처 구성 (YOLOv1).

**남겨둔 자료**: `md` 원본과 9개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch입니다.

**주요 스택**: `torch`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 9 |
| Execution Cells | 9 |
| Libraries | `torch` |
| Source Note | `(실습)YOLOv1` |

## What This Note Covers

### Overview

YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다.

### Key Step

논문에 제시된 아키텍처 구성 (YOLOv1)

## Why This Matters

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. Overview: YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다.
2. Key Step: 논문에 제시된 아키텍처 구성 (YOLOv1)

## Code Highlights

### 논문에 제시된 아키텍처 구성 (YOLOv1)

`논문에 제시된 아키텍처 구성 (YOLOv1)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 논문에 제시된 아키텍처 구성 (YOLOv1) 흐름이 주석과 함께 드러납니다.

```python
# 논문에 제시된 아키텍처 구성 (YOLOv1)
architecture_config = [
    (7, 64, 2, 3),       # (kernel_size, filters, stride, padding)
    "M",                 # maxpool
    (3, 192, 1, 1),
    "M",
    (1, 128, 1, 0),
    (3, 256, 1, 1),
    (1, 256, 1, 0),
    (3, 512, 1, 1),
    "M",
    [(1, 256, 1, 0), (3, 512, 1, 1), 4],  # 해당 블록을 4번 반복
    (1, 512, 1, 0),
    (3, 1024, 1, 1),
    "M",
    [(1, 512, 1, 0), (3, 1024, 1, 1), 2],  # 해당 블록을 2번 반복
    (3, 1024, 1, 1),
    (3, 1024, 2, 1),
    (3, 1024, 1, 1),
    (3, 1024, 1, 1)
]
```

### class YOLOv1(nn.Module)

`class YOLOv1(nn.Module)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 입력 이미지가 448 인경우 마지막 컨볼루션 feature map 7x7 흐름이 주석과 함께 드러납니다.

```python
class YOLOv1(nn.Module):
    def __init__(self, in_channels=3, num_classes=20, split_size=7, num_boxes=2):
        super().__init__()
        self.conv_layers = create_conv_layers(architecture_config, in_channels)

        # 입력 이미지가 448 인경우 마지막 컨볼루션 feature map 7x7
        self.fc_layers = nn.Sequential(
            nn.Flatten(),
            nn.Linear(1024*7*7, 4096),
            nn.LeakyReLU(0.1),
            nn.Dropout(0.5),
            nn.Linear(4096, split_size * split_size * (num_classes + num_boxes * 5))
        )
        self.split_size = split_size
        self.num_boxes = num_boxes
        self.num_classes = num_classes
    def forward(self, x):
        x = self.conv_layers(x)
        x = self.fc_layers(x)
        return x
```

### @title NMS

`@title NMS`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 NMS 흐름이 주석과 함께 드러납니다.

```python
#@title NMS
def nms(bboxes, iou_th, conf_th):
    """
    bboxes: 각 요소가 [pred_class, confidence, x1, y1, x2, y2] 형태인 리스트
    iou_threshold: IoU 임계치
    conf_threshold: confidence 임계치 이하인 박스 제거
    """
    bboxes = [box for box in bboxes if box[1] > conf_th]
    bboxes = sorted(bboxes, key=lambda x: x[1], reverse=True)
    bboxes_nms = []

    while bboxes:
        chosen_box = bboxes.pop(O)
        bboxes = [box for box in bboxes
                  if box[0] != chosen_box[0] or iou(torch.tensor(chosen_box[2:]).unsqueeze(0),
                                                    torch.tensor(box[2:]).unsqueeze(0)).item()< iou_th]
        bboxes_nms.append(chosen_box)
    return bboxes_nms
```

### @title Loss

`@title Loss`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Loss, width, height에 sqrt 적용 (음수 방지를 위해 클램핑), Object loss (물체가 있을 때 confidence 손실) 흐름이 주석과 함께 드러납니다.

```python
#@title Loss
def yolo_loss(predictions, target, S=7,B=2,C=20, lambda_coord=5, lambda_noobj=0.5):
    """
    predictions: [batch, 7*7*30] 형태의 텐서
    target: [batch, 7, 7, 30] 형태의 텐서
    """
    predictions = predictions.view(-1, S, S, C+B*5)
    iou_b1 = iou(predictions[...,21:25], target[..., 21:25])
    iou_b2 = iou(predictions[...,26:30], target[..., 21:25])
    ious = torch.cat([iou_b1.unsqueeze(0), iou_b2.unsqueeze(0)], dim=0)

    iou_maxes, bestbox = torch.max(ious, dim=0)
    bestbox = bestbox.float().unsqueeze(-1)

    exists_box = target[..., 20].unsqueeze(-1)

    box_pred = exists_box * (bestbox * predictions[..., 26:30] + (1-bestbox) * predictions[..., 21:25])
    box_target = exists_box * target[...,21:25]

    # width, height에 sqrt 적용 (음수 방지를 위해 클램핑)
    box_pred_wh = torch.sqrt(torch.clamp(box_pred[..., 2:4], min=1e-6))
    box_target_wh = torch.sqrt(torch.clamp(box_target[..., 2:4], min=1e-6))
    box_pred = torch.cat([box_pred[..., :2], box_pred_wh], dim=-1)
    box_target = torch.cat([box_target[..., :2], box_target_wh], dim=-1)

    box_loss = torch.sum((box_pred - box_target) ** 2)

    # Object loss (물체가 있을 때 confidence 손실)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)YOLOv1.md`
- Source formats: `md`
- Companion files: `(실습)YOLOv1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 모델 부분:
> YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다.
