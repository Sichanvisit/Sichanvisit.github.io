---
title: "CNN 이미지 분류 part1 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-2_CNN_이미지 분류_part1 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-2_CNN_이미지 분류_part1 - 공유.md"
excerpt: "Fashion MNIST는 다양한 **패션 아이템 이미지**가 포함된 데이터셋입니다."
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 29 |
| Execution Cells | 16 |
| Libraries | `numpy`, `torch`, `torchvision`, `matplotlib` |
| Source Note | `4-2_CNN_이미지 분류_part1 - 공유` |

## What I Worked On

- 데이터 소개
- 데이터셋 특징
- 클래스 정보
- 데이터 불러오기
- 라이브러리 임포트

## Implementation Flow

1. 데이터 소개
2. 데이터셋 특징
3. 클래스 정보
4. 데이터 불러오기
5. 라이브러리 임포트
6. 학습 데이터셋 생성

## Code Highlights

### DNN 모델

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# 데이터셋 로드 및 전처리
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # 픽셀 값을 [-1, 1]로 정규화
])

train_dataset = datasets.FashionMNIST(
    root="./data", train=True, transform=transform, download=True
)
test_dataset = datasets.FashionMNIST(
    root="./data", train=False, transform=transform, download=True
)

train_dataloader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# GPU 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# DNN 모델 정의
# ... trimmed ...
```

### DNN 모델

```python
# 결과 시각화 (테스트 샘플)
def visualize_predictions(model, test_loader, classes):
    model.eval()
    inputs, labels = next(iter(test_loader))
    inputs, labels = inputs.to(device), labels.to(device)

    with torch.no_grad():
        outputs = model(inputs)
        _, preds = torch.max(outputs, 1)

    inputs = inputs.cpu()
    preds = preds.cpu()
    labels = labels.cpu()

    fig, axes = plt.subplots(1, 6, figsize=(15, 5))
    for i in range(6):
        axes[i].imshow(inputs[i].squeeze(), cmap="gray")
        axes[i].set_title(f"Pred: {classes[preds[i]]}\nTrue: {classes[labels[i]]}")
        axes[i].axis("off")
    plt.show()

# 클래스 이름
classes = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

visualize_predictions(model, test_dataloader, classes)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/4-2_CNN_이미지 분류_part1 - 공유.md`
- Source formats: `md`
- Companion files: `4-2_CNN_이미지 분류_part1 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> Fashion MNIST는 다양한 **패션 아이템 이미지**가 포함된 데이터셋입니다.
> - **학습 데이터**: 6만 개 - **테스트 데이터**: 1만 개 - **이미지 크기**: 28×28 (그레이스케일) - **클래스**: 총 10개 (각 클래스에 데이터 균등 분포)
