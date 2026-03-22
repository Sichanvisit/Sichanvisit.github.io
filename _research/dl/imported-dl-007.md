---
title: "Mask R-CNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Mask R-CNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Mask R-CNN.md"
excerpt: "Mask R-CNN에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, class PennFudanDatase..., num_classes = 2, in_features_mask = mo... 같은 코드로 실제 구현을 이어서..."
research_summary: "Mask R-CNN에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, class PennFudanDatase..., num_classes = 2, in_features_mask = mo... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다."
research_artifacts: "md · 코드 11개 · 실행 10개"
code_block_count: 11
execution_block_count: 10
research_focus:
  - "데이터셋 준비"
  - "데이터셋을 학습용과 테스트용으로 나눕니다."
  - "DataLoader 생성"
research_stack:
  - "os"
  - "torch"
  - "torchvision"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

Mask R-CNN에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, class PennFudanDatase..., num_classes = 2, in_features_mask = mo... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: 데이터셋 준비, 데이터셋을 학습용과 테스트용으로 나눕니다., DataLoader 생성.

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다.

**주요 스택**: `os`, `torch`, `torchvision`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 11 |
| Execution Cells | 10 |
| Libraries | `os`, `torch`, `torchvision`, `matplotlib` |
| Source Note | `(실습)Mask R-CNN` |

## What This Note Covers

- 데이터셋 준비
- 데이터셋을 학습용과 테스트용으로 나눕니다.
- DataLoader 생성
- 간단한 학습 루프 (2 에폭 예시)
- 학습 가능한 파라미터만 모아 옵티마이저에 전달

## Why This Matters

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. Key Step: 데이터셋 준비: PennFudan 데이터셋의 경로와 변환 함수 지정
2. Key Step: 데이터셋을 학습용과 테스트용으로 나눕니다.
3. Key Step: 여기서는 무작위로 선택하여 마지막 50개 이미지를 테스트셋으로 사용합니다.
4. Key Step: DataLoader 생성: 배치 크기, 셔플 여부, 그리고 collate_fn 지정

## Code Highlights

### class  PennFudanDataset(torch.utils.data.Dataset)

`class  PennFudanDataset(torch.utils.data.Dataset)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 마스크에 포함된 클래스를 확인 -> 그중에 0은 배경으로 제외, 각 객체 인스턴스에 대해 binary mask를 생성합니다., mask == obj_ids[:, None, None]는 각 인스턴스마다 True/Fal... 흐름이 주석과 함께 드러납니다.

```python
class  PennFudanDataset(torch.utils.data.Dataset):
    def __init__(self, root, transform):
        self.root = root
        self.transform = transform

        self.imgs = sorted(os.listdir(os.path.join(root, "PNGImages")))
        self.masks = sorted(os.listdir(os.path.join(root, "PedMasks")))

    def __getitem__(self, idx):
        img_path = os.path.join(self.root, "PNGImages", self.imgs[idx])
        mask_path = os.path.join(self.root, "PedMasks", self.masks[idx])

        img = read_image(img_path)
        mask = read_image(mask_path)

        # 마스크에 포함된 클래스를 확인 -> 그중에 0은 배경으로 제외
        obj_ids = torch.unique(mask)[1:]

        # 각 객체 인스턴스에 대해 binary mask를 생성합니다.
        # mask == obj_ids[:, None, None]는 각 인스턴스마다 True/False 마스크를 만듭니다.
        # .to(dtype=torch.uint8)로 자료형을 8비트 정수형으로 변환합니다.
        masks = (mask == obj_ids[:,None, None]).to(dtype=torch.uint8)
        boxes = masks_to_boxes(masks)
        labels = torch.ones((len(obj_ids),),dtype=torch.int64)
        image_id = idx
        area = (boxes[:,3] - boxes[:,1]) * (boxes[:,2] - boxes[:,0])
        iscrowd = torch.zeros((len(obj_ids),), dtype=torch.int64)

# ... trimmed ...
```

### num_classes = 2

`num_classes = 2`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
num_classes = 2
device = "cuda" if torch.cuda.is_available() else 'cpu'

model = torchvision.models.detection.maskrcnn_resnet50_fpn(weights="DEFAULT")
```

### in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels

`in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
in_features_mask = model.roi_heads.mask_predictor.conv5_mask.in_channels
in_features_mask

model.roi_heads.mask_predictor = torchvision.models.detection.mask_rcnn.MaskRCNNPredictor(in_features_mask, 256, num_classes)
model.roi_heads.mask_predictor
model.to(device)
```

### def collate_fn(batch)

`def collate_fn(batch)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋 준비: PennFudan 데이터셋의 경로와 변환 함수 지정, 데이터셋을 학습용과 테스트용으로 나눕니다., 여기서는 무작위로 선택하여 마지막 50개 이미지를 테스트셋으로 사용합니다. 흐름이 주석과 함께 드러납니다.

```python
def collate_fn(batch):
    return tuple(zip(*batch))

# 데이터셋 준비: PennFudan 데이터셋의 경로와 변환 함수 지정
dataset = PennFudanDataset('/content/data/PennFudanPed', get_transform(train=True))
dataset_test = PennFudanDataset('./data/PennFudanPed', get_transform(train=False))

# 데이터셋을 학습용과 테스트용으로 나눕니다.
# 여기서는 무작위로 선택하여 마지막 50개 이미지를 테스트셋으로 사용합니다.
indices = torch.randperm(len(dataset)).tolist()
dataset = torch.utils.data.Subset(dataset, indices[:-50])
dataset_test = torch.utils.data.Subset(dataset_test, indices[-50:])

# DataLoader 생성: 배치 크기, 셔플 여부, 그리고 collate_fn 지정
data_loader = torch.utils.data.DataLoader(dataset, batch_size=2, shuffle=True, collate_fn=collate_fn)
data_loader_test = torch.utils.data.DataLoader(dataset_test, batch_size=1, shuffle=False, collate_fn=collate_fn)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)Mask R-CNN.md`
- Source formats: `md`
- Companion files: `(실습)Mask R-CNN.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2025.10.1,2,13,14.md`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
