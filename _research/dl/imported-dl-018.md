---
title: "사전훈련모델"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)사전훈련모델"
source_path: "12_Deep_Learning/Code_Snippets/(실습)사전훈련모델.md"
excerpt: "CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다"
research_summary: "CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 36개 코드 블록, 30개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 36개 · 실행 30개"
code_block_count: 36
execution_block_count: 30
research_focus:
  - "CIFAR-100 사전학습"
  - "코드 설명"
  - "사전 함수"
research_stack:
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "numpy"
  - "math"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 36개 코드 블록, 30개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: CIFAR-100 사전학습, 코드 설명, 사전 함수.

**남겨둔 자료**: `md` 원본과 36개 코드 블록, 30개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `numpy`, `math`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 36 |
| Execution Cells | 30 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy`, `math`, `PIL`, `tqdm`, `os` |
| Source Note | `(실습)사전훈련모델` |

## What This Note Covers

### 코드 설명

CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다.

### Key Step

모델 초기화, 손실함수, 옵티마이저

### Key Step

def train(model, dd,,d,d,d,d)

### Key Step

train_loss, train_acc = train_epoch(model_cifar, cifar_train_loader, loss_fn, optim_cifar)

## Implementation Flow

1. 코드 설명: CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다.
2. Key Step: 모델 초기화, 손실함수, 옵티마이저
3. Key Step: def train(model, dd,,d,d,d,d)
4. Key Step: train_loss, train_acc = train_epoch(model_cifar, cifar_train_loader, loss_fn, optim_cifar)

## Code Highlights

### 사전 함수

`사전 함수`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
def visualize_one_per_category(dataset, dataset_name="Dataset", cmap=None):

    samples= {} # key : label, value : 이미지
    targets = dataset.targets if hasattr(dataset, 'targets') else dataset.train_labels

    for idx in range(len(dataset)):
        img, label = dataset[idx]
        if torch.is_tensor(label):
            label = label.item()
        if label not in samples:
            samples[label] = img
        if len(samples) >= len(dataset.classes):
            break

    n_categories = len(dataset.classes)
    print(f'{dataset_name} 카테고리 개수 : {n_categories}')

    cols = 10 if n_categories >= 10 else n_categories # min(10, n_categories)
    rows = math.ceil(n_categories / cols)

    fig, axes = plt.subplots(rows, cols, figsize = (cols*2, rows*2))
    if rows * cols > 1:
        axes = axes.flatten()
    else:
        axes = [axes]

    for i, label in enumerate(sorted(samples.keys())):
        ax = axes[i]
# ... trimmed ...
```

### 모델 설계

`모델 설계`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 > nn.Linear(256, 10) MNIST에서 동작 흐름이 주석과 함께 드러납니다.

```python
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, 1, 1),  # 3 --> 32
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2),            # 32x32 --> 16x16

            nn.Conv2d(32, 64, 3, 1, 1),  # 32 --> 64
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),            # 16x16 --> 8x8

            nn.Conv2d(64, 128, 3,1,1),  # 64 --> 128
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2),            # 8x8 --> 4x4
        )
        self.classifier = nn.Sequential(
            nn.Linear(128*4*4, 256),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(256, 100)  # CIFAR100의 클래스가 100개
            # --> nn.Linear(256, 10) MNIST에서 동작
        )

    def forward(self, x):
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)사전훈련모델.md`
- Source formats: `md`
- Companion files: `(실습)사전훈련모델.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 1. **CIFAR-100 사전학습:** CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다.
> 2. **MNIST 데이터 전처리:** MNIST 이미지를 32×32, 3채널로 변환하여 CIFAR-100 모델에 맞게 전처리합니다.
