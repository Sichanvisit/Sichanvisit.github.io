---
title: "YOLOv1"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)YOLOv1"
source_path: "12_Deep_Learning/Code_Snippets/(실습)YOLOv1.md"
excerpt: "YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다."
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
| Code Blocks | 9 |
| Execution Cells | 9 |
| Libraries | `torch` |
| Source Note | `(실습)YOLOv1` |

## What I Worked On

- 논문에 제시된 아키텍처 구성 (YOLOv1)

## Implementation Flow

1. 논문에 제시된 아키텍처 구성 (YOLOv1)

## Code Highlights

### @title IoU

```python
#@title IoU
def iou(boxes1, boxes2, eps=1e-6):
    # x_center, y_center, w, h
    # 좌상단 w,h --> 좌상단, 우하단 (다른 예시)

    # xc, yc, w, h --> x1, y1, x2, y2
    # 중앙좌표 , w,h -> 좌상단, 우하단
    box1_x1 = boxes1[..., 0:1] - boxes1[..., 2,3] / 2
    box1_y1 = boxes1[..., 1:2] - boxes1[..., 3,4] / 2
    box1_x2 = boxes1[..., 0:1] + boxes1[..., 2,3] / 2
    box1_y2 = boxes1[..., 1:2] + boxes1[..., 3,4] / 2

    box2_x1 = boxes2[..., 0:1] - boxes2[..., 2,3] / 2
    box2_y1 = boxes2[..., 1:2] - boxes2[..., 3,4] / 2
    box2_x2 = boxes2[..., 0:1] + boxes2[..., 2,3] / 2
    box2_y2 = boxes2[..., 1:2] + boxes2[..., 3,4] / 2

    x1 = torch.max(box1_x1, box2_x1)
    y1 = torch.max(box1_y1, box2_y1)
    x2 = torch.min(box1_x2, box2_x2)
    y2 = torch.min(box1_y2, box2_y2)

    inter = torch.clamp(x2-x1, min=0) * torch.clamp(y2-y1, min=0)
    box1_area = torch.abs((box1_x2-box1_x1) * (box1_y2-box1_y1))
    box2_area = torch.abs((box2_x2-box2_x1) * (box2_y2-box2_y1))
    iou_val = inter / (box1_area + box2_area - inter + eps)

    return iou_val
```

### @title Loss

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
