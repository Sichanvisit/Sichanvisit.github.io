---
title: "Mask R-CNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Mask R-CNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Mask R-CNN.md"
excerpt: "DL Archive Note: 데이터셋 준비: PennFudan 데이터셋의 경로와 변환 함수 지정, 데이터셋을 학습용과 테스트용으로 나눕니다., 여기서는 무작위로 선택하여 마지막 50개 이미지를 테스트셋으로 사용합니다."
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
| Code Blocks | 11 |
| Execution Cells | 10 |
| Libraries | `os`, `torch`, `torchvision`, `matplotlib` |
| Source Note | `(실습)Mask R-CNN` |

## What I Worked On

- 데이터셋 준비: PennFudan 데이터셋의 경로와 변환 함수 지정
- 데이터셋을 학습용과 테스트용으로 나눕니다.
- 여기서는 무작위로 선택하여 마지막 50개 이미지를 테스트셋으로 사용합니다.
- DataLoader 생성: 배치 크기, 셔플 여부, 그리고 collate_fn 지정
- 5. 간단한 학습 루프 (2 에폭 예시)

## Implementation Flow

1. 데이터셋 준비: PennFudan 데이터셋의 경로와 변환 함수 지정
2. 데이터셋을 학습용과 테스트용으로 나눕니다.
3. 여기서는 무작위로 선택하여 마지막 50개 이미지를 테스트셋으로 사용합니다.
4. DataLoader 생성: 배치 크기, 셔플 여부, 그리고 collate_fn 지정
5. 5. 간단한 학습 루프 (2 에폭 예시)
6. 학습 가능한 파라미터만 모아 옵티마이저에 전달

## Code Highlights

### class  PennFudanDataset(torch.utils.data.Dataset)

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

### 5. 간단한 학습 루프 (2 에폭 예시)

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

> No prose preview was available in the source note.
