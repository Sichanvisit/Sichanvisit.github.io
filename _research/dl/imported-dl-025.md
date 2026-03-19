---
title: "CNN 이미지 분류 part2 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-3_CNN_이미지 분류_part2 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-3_CNN_이미지 분류_part2 - 공유.md"
excerpt: "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다"
research_summary: "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다. 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포). `md` 원본과 60개 코드 블록, 27개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다."
research_artifacts: "md · 코드 60개 · 실행 27개"
code_block_count: 60
execution_block_count: 27
research_focus:
  - "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다."
  - "데이터 소개"
  - "학습 데이터"
research_stack:
  - "numpy"
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "PIL"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다. 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포). `md` 원본과 60개 코드 블록, 27개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋..., 데이터 소개, 학습 데이터.

**남겨둔 자료**: `md` 원본과 60개 코드 블록, 27개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**주요 스택**: `numpy`, `torch`, `torchvision`, `matplotlib`, `PIL`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 60 |
| Execution Cells | 27 |
| Libraries | `numpy`, `torch`, `torchvision`, `matplotlib`, `PIL`, `torchinfo`, `sklearn` |
| Source Note | `4-3_CNN_이미지 분류_part2 - 공유` |

## What This Note Covers

### 데이터 소개

Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.

### 데이터셋 특징

학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)

### 클래스 정보

0번부터 9번까지 다음과 같은 패션 아이템으로 구성됩니다

### 데이터 불러오기

TorchVision은 PyTorch에서 제공하는 컴퓨터 비전용 라이브러리입니다. - 다양한 데이터셋, 모델, 이미지 전처리 및 증강 기능을 지원합니다. - 이번 강의에서는 TorchVision의 datasets 모듈을 활용합니다.

## Implementation Flow

1. 데이터 소개: Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.
2. 데이터셋 특징: 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)
3. 클래스 정보: 0번부터 9번까지 다음과 같은 패션 아이템으로 구성됩니다
4. 데이터 불러오기: TorchVision은 PyTorch에서 제공하는 컴퓨터 비전용 라이브러리입니다. - 다양한 데이터셋, 모델, 이미지 전처리 및 증강 기능을 지원합니다. - 이번 강의에서는 TorchVision의 datasets 모듈을 활용합니다.

## Code Highlights

### 모델 학습시키기

`모델 학습시키기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 루프 작성 흐름이 주석과 함께 드러납니다.

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 학습 루프 작성

epochs = 2
step = 0
for epoch in range(epochs):
    model.train()
    for train_batch in train_dataloader:
        optimizer.zero_grad()
        inputs = train_batch[0].to(device)
        labels = train_batch[1].to(device)
        preds = model(inputs)
        loss = loss_fn(preds, labels)

        loss.backward()
        optimizer.step()

        step += 1
        if step % 100 == 0:
            print(f'step {step}, train loss: {loss.item():.4f}')

    val_loss, val_acc = evaluate(val_dataloader, model, loss_fn)
    print(f'epoch {epoch+1}/{epochs}, val loss: {val_loss:.4f}, val acc: {val_acc:.4f}')

print('Training finished!')
```

### (참고) ImageFolder

`(참고) ImageFolder`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터 증강 및 전처리 정의, 훈련 데이터 전용: 증강 포함, 검증 및 테스트 데이터 전용: 증강 없음 흐름이 주석과 함께 드러납니다.

```python
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset
from sklearn.model_selection import train_test_split

# 1. 데이터 증강 및 전처리 정의
# 훈련 데이터 전용: 증강 포함
transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),  # 랜덤 좌우 반전
    transforms.RandomRotation(30),          # 랜덤 회전 (-30도 ~ 30도)
    transforms.RandomResizedCrop(224),      # 랜덤 자르기 후 크기 조정
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),  # 밝기/대비/채도 조정
    transforms.ToTensor(),                  # 텐서로 변환
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])    # 정규화
])

# 검증 및 테스트 데이터 전용: 증강 없음
transform_test = transforms.Compose([
    transforms.Resize(256),                 # 크기 조정
    transforms.CenterCrop(224),             # 중앙 자르기
    transforms.ToTensor(),                  # 텐서로 변환
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])    # 정규화
])

# 2. 데이터셋 로드
original_dataset = datasets.ImageFolder(root="flower_photos")

# 3. 데이터셋 인덱스 추출 및 분할
indices = list(range(len(original_dataset)))
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/4-3_CNN_이미지 분류_part2 - 공유.md`
- Source formats: `md`
- Companion files: `4-3_CNN_이미지 분류_part2 - 공유.md`
- Note type: `resource-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> Fashion MNIST는 다양한 **패션 아이템 이미지**가 포함된 데이터셋입니다.
> - **학습 데이터**: 6만 개 - **테스트 데이터**: 1만 개 - **이미지 크기**: 28×28 (그레이스케일) - **클래스**: 총 10개 (각 클래스에 데이터 균등 분포)
