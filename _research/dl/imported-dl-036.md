---
title: "YOLOv1"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-2_YOLOv1"
source_path: "12_Deep_Learning/Code_Snippets/6-2_YOLOv1.md"
excerpt: "출처 : https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO"
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
| Execution Cells | 8 |
| Libraries | `torch`, `torchinfo` |
| Source Note | `6-2_YOLOv1` |

## What I Worked On

- yolov1_implementation
- Architecture
- 논문에 제시된 아키텍처 구성 (YOLOv1)
- IOU
- IoU 계산 함수 (YOLOv1에서 사용하는 bounding box 형식: [x_center, y_center, width, height])

## Implementation Flow

1. yolov1_implementation
2. Architecture
3. 논문에 제시된 아키텍처 구성 (YOLOv1)
4. IOU
5. IoU 계산 함수 (YOLOv1에서 사용하는 bounding box 형식: [x_center, y_center, width, height])
6. NMS

## Code Highlights

### Architecture

```python
def create_conv_layers(config, in_channels):
    layers = []
    for module in config:
        if type(module) == tuple:
            # 튜플 형태: (kernel_size, filters, stride, padding)
            kernel_size, filters, stride, padding = module
            layers.append(nn.Conv2d(in_channels, filters, kernel_size, stride, padding))
            layers.append(nn.LeakyReLU(0.1))
            in_channels = filters
        elif module == "M":
            layers.append(nn.MaxPool2d(kernel_size=2, stride=2))
        elif type(module) == list:
            # 리스트 형태: [ conv1 튜플, conv2 튜플, 반복 횟수 ]
            conv1, conv2, num_repeats = module
            for _ in range(num_repeats):
                # 첫 번째 컨볼루션
                k, f, s, p = conv1
                layers.append(nn.Conv2d(in_channels, f, k, s, p))
                layers.append(nn.LeakyReLU(0.1))
                in_channels = f
                # 두 번째 컨볼루션
                k, f, s, p = conv2
                layers.append(nn.Conv2d(in_channels, f, k, s, p))
                layers.append(nn.LeakyReLU(0.1))
                in_channels = f
    return nn.Sequential(*layers)

class YOLOv1(nn.Module):
# ... trimmed ...
```

### Loss

```python
# Loss 함수 (YOLOv1 손실 함수 구현)
def yolo_loss(predictions, target, S=7, B=2, C=20, lambda_coord=5, lambda_noobj=0.5):
    """
    predictions: [batch, 7*7*30] 형태의 텐서
    target: [batch, 7, 7, 30] 형태의 텐서
    """
    predictions = predictions.view(-1, S, S, C + B * 5)
    # 두 박스에 대해 IoU 계산 (bbox 좌표 부분: 21:25와 26:30)
    iou_b1 = iou(predictions[..., 21:25], target[..., 21:25])
    iou_b2 = iou(predictions[..., 26:30], target[..., 21:25])
    ious = torch.cat([iou_b1.unsqueeze(0), iou_b2.unsqueeze(0)], dim=0)

    iou_maxes, bestbox = torch.max(ious, dim=0)
    bestbox = bestbox.float().unsqueeze(-1)

    exists_box = target[..., 20].unsqueeze(-1)

    # Box coordinate loss (좌표 손실)
    box_pred = exists_box * (bestbox * predictions[..., 26:30] + (1 - bestbox) * predictions[..., 21:25])
    box_target = exists_box * target[..., 21:25]

    # width, height에 sqrt 적용 (음수 방지를 위해 클램핑)
    box_pred_wh = torch.sqrt(torch.clamp(box_pred[..., 2:4], min=1e-6))
    box_target_wh = torch.sqrt(torch.clamp(box_target[..., 2:4], min=1e-6))
    box_pred = torch.cat([box_pred[..., :2], box_pred_wh], dim=-1)
    box_target = torch.cat([box_target[..., :2], box_target_wh], dim=-1)

    box_loss = torch.sum((box_pred - box_target) ** 2)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/6-2_YOLOv1.md`
- Source formats: `md`
- Companion files: `6-2_YOLOv1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `github.com`, `localhost`

## Note Preview

> 출처 : https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO
> 1. architecture 2. IOU 3. loss
