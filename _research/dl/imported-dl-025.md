---
title: "CNN 이미지 분류 part2 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-3_CNN_이미지 분류_part2 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-3_CNN_이미지 분류_part2 - 공유.md"
excerpt: "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다. Fashion MNIST 데이터셋을 대상으로 전처리 과정을 진행하며, 텐서 변환, 스케일링, 표준화, 그리고 전처리를 데이터셋에 적용하는 방법을 살펴봅니다. Fashion MNIST 데이터를 불러오면 이미지가 Pillow..."
research_summary: "Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다. Fashion MNIST 데이터셋을 대상으로 전처리 과정을 진행하며, 텐서 변환, 스케일링, 표준화, 그리고 전처리를 데이터셋에 적용하는 방법을 살펴봅니다. Fashion MNIST 데이터를 불러오면 이미지가 Pillow(PIL) 형식으로 제공됩니다. `md` 원본과 60개 코드 블록, 27개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다."
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

Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다. Fashion MNIST 데이터셋을 대상으로 전처리 과정을 진행하며, 텐서 변환, 스케일링, 표준화, 그리고 전처리를 데이터셋에 적용하는 방법을 살펴봅니다. Fashion MNIST 데이터를 불러오면 이미지가 Pillow(PIL) 형식으로 제공됩니다. `md` 원본과 60개 코드 블록, 27개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

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

### 데이터 소개 > 데이터셋 특징

학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)

### 데이터 소개 > 클래스 정보

0번부터 9번까지 다음과 같은 패션 아이템으로 구성됩니다 0: T-shirt/top - 1: Trouser - 2: Pullover - 3: Dress - 4: Coat - 5: Sandal - 6: Shirt - 7: Sneaker - 8: Bag - 9: Ankle boot

### 데이터 소개 > 데이터 불러오기

PyTorch의 TorchVision 라이브러리 TorchVision은 PyTorch에서 제공하는 컴퓨터 비전용 라이브러리입니다. - 다양한 데이터셋, 모델, 이미지 전처리 및 증강 기능을 지원합니다. - 이번 강의에서는 TorchVision의 datasets 모듈을 활용합니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. 데이터 소개: Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.
2. 데이터 소개 > 데이터셋 특징: 학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)
3. 데이터 소개 > 클래스 정보: 0번부터 9번까지 다음과 같은 패션 아이템으로 구성됩니다 0: T-shirt/top - 1: Trouser - 2: Pullover - 3: Dress - 4: Coat - 5: Sandal - 6: Shirt - 7: Sneaker - 8: Bag - 9: Ankle...
4. 데이터 소개 > 데이터 불러오기: PyTorch의 TorchVision 라이브러리 TorchVision은 PyTorch에서 제공하는 컴퓨터 비전용 라이브러리입니다. - 다양한 데이터셋, 모델, 이미지 전처리 및 증강 기능을 지원합니다. - 이번 강의에서는 TorchVision의 datasets 모듈...

## Code Highlights

### CNN 모델 만들기

`CNN 모델 만들기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 생성 및 테스트, x = torch.randn(2, 1, 28, 28), output = model(x) 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, 3, 1, 1)
        self.conv2 = nn.Conv2d(32, 64, 3, 1, 1)
        self.maxpool = nn.MaxPool2d(2, 2)
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(64*7*7, 64)
        self.linear2 = nn.Linear(64, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))  # 첫 번째 컨볼루션 + 렐루 활성화
        x = self.maxpool(x)  # 맥스풀링
        x = F.relu(self.conv2(x))  # 두 번째 컨볼루션 + 렐루 활성화
        x = self.maxpool(x)  # 맥스풀링
        x = self.flatten(x)  # 피처맵을 벡터로 펼침
        x = F.relu(self.linear1(x))  # 첫 번째 리니어 + 렐루 활성화
        output = self.linear2(x)  # 두 번째 리니어
        return output  # 최종 출력

# 모델 생성 및 테스트
model = CNNModel()
# x = torch.randn(2, 1, 28, 28)
# output = model(x)
# ... trimmed ...
```

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
