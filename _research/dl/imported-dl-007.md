---
title: "Mask R-CNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Mask R-CNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Mask R-CNN.md"
excerpt: "데이터셋 준비, 데이터셋을 학습용과 테스트용으로 나눕니다., DataLoader 생성 중심으로 구현 과정을 정리한 Mask R-CNN 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개..."
research_summary: "데이터셋 준비, 데이터셋을 학습용과 테스트용으로 나눕니다., DataLoader 생성 중심으로 구현 과정을 정리한 Mask R-CNN 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다."
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

데이터셋 준비, 데이터셋을 학습용과 테스트용으로 나눕니다., DataLoader 생성 중심으로 구현 과정을 정리한 Mask R-CNN 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, torchvision, matplotlib입니다.

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

### 5. 간단한 학습 루프 (2 에폭 예시)

`5. 간단한 학습 루프 (2 에폭 예시)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 간단한 학습 루프 (2 에폭 예시), 학습 가능한 파라미터만 모아 옵티마이저에 전달, 학습률 스케줄러: 3 에폭마다 학습률을 0.1배 감소 흐름이 주석과 함께 드러납니다.

```python
# 5. 간단한 학습 루프 (2 에폭 예시)
# 학습 가능한 파라미터만 모아 옵티마이저에 전달
params = [p for p in model.parameters() if p.requires_grad]
optimizer = torch.optim.SGD(params, lr=0.005, momentum=0.9, weight_decay=0.0005)
# 학습률 스케줄러: 3 에폭마다 학습률을 0.1배 감소
lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=3, gamma=0.1)

num_epochs = 2  # 학습 에폭 수
for epoch in range(num_epochs):
    model.train()  # 모델을 학습 모드로 전환 (Dropout, BatchNorm 등이 학습 모드로 작동)
    epoch_loss = 0  # 에폭별 손실 누적 변수
    for images, targets in data_loader:
        # 각 이미지와 타겟을 device(GPU 또는 CPU)로 이동
        images = [img.to(device) for img in images]
        # 타겟은 dict 형식이며, tensor인 항목만 to(device) 처리
        targets = [{k: (v.to(device) if torch.is_tensor(v) else v) for k, v in t.items()} for t in targets]

        # 모델에 이미지와 타겟을 전달하면, 학습 모드에서는 손실(loss) dict를 반환합니다.
        loss_dict = model(images, targets)
        # dict의 모든 손실값을 합산하여 총 손실을 계산합니다.
        losses = sum(loss for loss in loss_dict.values())
        epoch_loss += losses.item()  # 손실 값을 float로 누적

        optimizer.zero_grad()  # 이전 배치의 기울기(gradient) 초기화
        losses.backward()      # 역전파를 통해 기울기 계산
        optimizer.step()       # 옵티마이저가 파라미터를 업데이트

    lr_scheduler.step()  # 에폭마다 학습률 업데이트
# ... trimmed ...
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
