---
title: "YOLOv1"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-2_YOLOv1"
source_path: "12_Deep_Learning/Code_Snippets/6-2_YOLOv1.md"
excerpt: "출처 : https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO"
research_summary: "출처 : https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO. YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다. `md` 원본과 9개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다."
research_artifacts: "md · 코드 9개 · 실행 8개"
code_block_count: 9
execution_block_count: 8
research_focus:
  - "출처"
  - "yolov1_implementation"
  - "YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의..."
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

출처 : https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO. YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다. `md` 원본과 9개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다.

**빠르게 볼 수 있는 포인트**: 출처, yolov1_implementation, YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fu....

**남겨둔 자료**: `md` 원본과 9개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다.

**주요 스택**: `torch`, `torchinfo`

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

## What This Note Covers

### yolov1_implementation

출처 : https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO

### Architecture

YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다.

### IOU

주어진 두 박스의 중심 좌표와 크기를 바탕으로 좌측상단, 우측하단 좌표를 계산하고, 교집합 영역을 통해 IoU를 계산합니다.

### NMS

confidence가 낮은 박스 제거 후, 가장 높은 confidence 박스를 선택하고 나머지 박스들과 IoU를 계산하여 제거합니다. - 박스 간의 IoU 계산 시, 텐서 변환 및 .item() 호출로 스칼라 값을 사용합니다.

## Implementation Flow

1. yolov1_implementation: 출처 : https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO
2. Architecture: YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다.
3. IOU: 주어진 두 박스의 중심 좌표와 크기를 바탕으로 좌측상단, 우측하단 좌표를 계산하고, 교집합 영역을 통해 IoU를 계산합니다.
4. NMS: confidence가 낮은 박스 제거 후, 가장 높은 confidence 박스를 선택하고 나머지 박스들과 IoU를 계산하여 제거합니다. - 박스 간의 IoU 계산 시, 텐서 변환 및 .item() 호출로 스칼라 값을 사용합니다.

## Code Highlights

### Architecture

`Architecture`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 튜플 형태: (kernel_size, filters, stride, padding), 리스트 형태: [ conv1 튜플, conv2 튜플, 반복 횟수 ], 첫 번째 컨볼루션 흐름이 주석과 함께 드러납니다.

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

`Loss`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Loss 함수 (YOLOv1 손실 함수 구현), 두 박스에 대해 IoU 계산 (bbox 좌표 부분: 21:25와 26:30), Box coordinate loss (좌표 손실) 흐름이 주석과 함께 드러납니다.

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
