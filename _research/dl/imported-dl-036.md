---
title: "YOLOv1"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "6-2_YOLOv1"
source_path: "12_Deep_Learning/Code_Snippets/6-2_YOLOv1.md"
excerpt: "yolov1_implementation 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 yolov1_implementation 순서로 핵심 장면을 먼저 훑고, Architecture, IOU, NMS 같은 코드로 실제 구현을 이어서..."
research_summary: "yolov1_implementation 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 yolov1_implementation 순서로 핵심 장면을 먼저 훑고, Architecture, IOU, NMS 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 9개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다."
research_artifacts: "md · 코드 9개 · 실행 8개"
code_block_count: 9
execution_block_count: 8
research_focus:
  - "yolov1_implementation"
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

yolov1_implementation 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 yolov1_implementation 순서로 핵심 장면을 먼저 훑고, Architecture, IOU, NMS 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 9개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo입니다.

**빠르게 볼 수 있는 포인트**: yolov1_implementation.

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

출처 : https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLO architecture 2. IOU 3. loss

- 읽을 포인트: 세부 흐름: Architecture, IOU, Loss

#### Architecture

YOLOv1 클래스는 여섯 개의 컨볼루션 블록과 두 개의 전결합층(fully connected)을 정의합니다. 각 컨볼루션 블록은 nn.Conv2d, nn.LeakyReLU(0.1), nn.MaxPool2d 등을 사용하여 구성되어 있습니다.

#### IOU

주어진 두 박스의 중심 좌표와 크기를 바탕으로 좌측상단, 우측하단 좌표를 계산하고, 교집합 영역을 통해 IoU를 계산합니다.

#### Loss

예측값을 [batch, 7, 7, 30] 형태로 재구성한 후, 각 grid cell마다 두 박스의 IoU를 계산하고, best box 선택, 그리고 좌표, confidence, 클래스 손실을 각각 계산하여 최종 loss를 반환합니다.

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

1. yolov1_implementation: Architecture, IOU

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

### IOU

`IOU`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 IoU 계산 함수 (YOLOv1에서 사용하는 bounding box 형식: [x_cent..., 좌측 상단, 우측 하단 좌표 계산 흐름이 주석과 함께 드러납니다.

```python
# IoU 계산 함수 (YOLOv1에서 사용하는 bounding box 형식: [x_center, y_center, width, height])
def iou(boxes1, boxes2, eps=1e-6):
    """
    boxes1, boxes2: 텐서, 마지막 차원이 [x_center, y_center, width, height]
    """
    # 좌측 상단, 우측 하단 좌표 계산
    box1_x1 = boxes1[..., 0:1] - boxes1[..., 2:3] / 2
    box1_y1 = boxes1[..., 1:2] - boxes1[..., 3:4] / 2
    box1_x2 = boxes1[..., 0:1] + boxes1[..., 2:3] / 2
    box1_y2 = boxes1[..., 1:2] + boxes1[..., 3:4] / 2

    box2_x1 = boxes2[..., 0:1] - boxes2[..., 2:3] / 2
    box2_y1 = boxes2[..., 1:2] - boxes2[..., 3:4] / 2
    box2_x2 = boxes2[..., 0:1] + boxes2[..., 2:3] / 2
    box2_y2 = boxes2[..., 1:2] + boxes2[..., 3:4] / 2

    x1 = torch.max(box1_x1, box2_x1)
    y1 = torch.max(box1_y1, box2_y1)
    x2 = torch.min(box1_x2, box2_x2)
    y2 = torch.min(box1_y2, box2_y2)

    inter = torch.clamp(x2 - x1, min=0) * torch.clamp(y2 - y1, min=0)
    box1_area = torch.abs((box1_x2 - box1_x1) * (box1_y2 - box1_y1))
    box2_area = torch.abs((box2_x2 - box2_x1) * (box2_y2 - box2_y1))
    iou_val = inter / (box1_area + box2_area - inter + eps)
    return iou_val
```

### NMS

`NMS`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 NMS (Non-Maximum Suppression) 함수: confidence가 낮은... 흐름이 주석과 함께 드러납니다.

```python
# NMS (Non-Maximum Suppression) 함수: confidence가 낮은 박스와 겹치는 박스 제거
def nms(bboxes, iou_threshold, conf_threshold):
    """
    bboxes: 각 요소가 [pred_class, confidence, x1, y1, x2, y2] 형태인 리스트
    iou_threshold: IoU 임계치
    conf_threshold: confidence 임계치 이하인 박스 제거
    """
    bboxes = [box for box in bboxes if box[1] > conf_threshold]
    bboxes = sorted(bboxes, key=lambda x: x[1], reverse=True)
    bboxes_nms = []

    while bboxes:
        chosen_box = bboxes.pop(0)
        bboxes = [
            box for box in bboxes
            if box[0] != chosen_box[0] or iou(torch.tensor(chosen_box[2:]).unsqueeze(0),
                                                 torch.tensor(box[2:]).unsqueeze(0)).item() < iou_threshold
        ]
        bboxes_nms.append(chosen_box)
    return bboxes_nms
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
