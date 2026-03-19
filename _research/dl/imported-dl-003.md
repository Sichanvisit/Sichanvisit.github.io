---
title: "CNN 이미지 분류1"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)CNN_이미지 분류1"
source_path: "12_Deep_Learning/Code_Snippets/(실습)CNN_이미지 분류1.md"
excerpt: "Fashion MNIST는 다양한 **패션 아이템 이미지**가 포함된 데이터셋입니다."
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
| Code Blocks | 76 |
| Execution Cells | 72 |
| Libraries | `numpy`, `torch`, `torchvision`, `matplotlib`, `types`, `PIL`, `torchinfo`, `sklearn` |
| Source Note | `(실습)CNN_이미지 분류1` |

## What I Worked On

- 데이터셋
- 클래스 정보
- 라이브러리
- 데이터 셋 생성
- 시각화

## Implementation Flow

1. 데이터셋
2. 클래스 정보
3. 라이브러리
4. 데이터 셋 생성
5. 시각화
6. 이미지 --> 텐서로 변환

## Code Highlights

### DNN 모델

```python
from types import CoroutineType
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# GPU 설정
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using Device : {device}")

# 데이터셋 로드 + 전처리
transforms = v2.Compose(
    [
        v2.ToImage(), # PIL -> Tensor (TV Tensor Image)
        v2.ToDtype(dtype=torch.float32, scale=True) #dtype변환 , 값을 0~1로 설정
        # uint8 --> float32
    ]
)

# 데이터 셋 생성 + transforms 적용
train_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=True,
    download=True,
    transform=transforms
)
# ... trimmed ...
```

### CNN 모델 만들기

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class CNNModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1,32,3,1,1)
        self.conv2 = nn.Conv2d(32,64,3,1,1)
        self.maxpool = nn.MaxPool2d(2,2)
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(64*7*7, 64)
        self.linear2 = nn.Linear(64, 10)

    def _func1(self,x):
        return x*x
        pass

    def func2(self,x):
        y = self._func1(x)
        print(y)

    def forward(self, x):
        x = F.relu(self.conv1(x))   # conv+relu (b,1,28,28) -> (b,32,28,28)
        x = self.maxpool(x)         # maxpool   (b,32,28,28)-> (b,32,14,14)
        x = F.relu(self.conv2(x))   # conv+relu (b,32,14,14)-> (b,64,14,14)
        x = self.maxpool(x)         # maxpool   (b,64,14,14)-> (b,64,7,7)

# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)CNN_이미지 분류1.md`
- Source formats: `md`
- Companion files: `(실습)CNN_이미지 분류1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> Fashion MNIST는 다양한 **패션 아이템 이미지**가 포함된 데이터셋입니다.
> - **학습 데이터**: 6만 개 - **테스트 데이터**: 1만 개 - **이미지 크기**: 28×28 (그레이스케일) - **클래스**: 총 10개 (각 클래스에 데이터 균등 분포)
