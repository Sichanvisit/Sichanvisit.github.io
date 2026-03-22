---
title: "사전훈련모델"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)사전훈련모델"
source_path: "12_Deep_Learning/Code_Snippets/(실습)사전훈련모델.md"
excerpt: "코드 설명, 사전 함수 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 코드 설명, 사전 함수, 1ch --> 3ch 순서로 핵심 장면을 먼저 훑고, 사전 함수, 1ch --> 3ch, 모델 설계 같은 코드로 실제 구현을 이어서 확인..."
research_summary: "코드 설명, 사전 함수 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 코드 설명, 사전 함수, 1ch --> 3ch 순서로 핵심 장면을 먼저 훑고, 사전 함수, 1ch --> 3ch, 모델 설계 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 36개 코드 블록, 30개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 36개 · 실행 30개"
code_block_count: 36
execution_block_count: 30
research_focus:
  - "코드 설명"
  - "사전 함수"
  - "1ch --> 3ch"
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

코드 설명, 사전 함수 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 코드 설명, 사전 함수, 1ch --> 3ch 순서로 핵심 장면을 먼저 훑고, 사전 함수, 1ch --> 3ch, 모델 설계 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 36개 코드 블록, 30개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: 코드 설명, 사전 함수, 1ch --> 3ch.

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

CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다. MNIST 데이터 전처리: MNIST 이미지를 32×32, 3채널로 변환하여 CIFAR-100 모델에 맞게 전처리합니다.

- 읽을 포인트: 코드 설명에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### 사전 함수

사전 함수 코드를 직접 따라가며 사전 함수 흐름을 확인했습니다.

- 읽을 포인트: 사전 함수 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 1ch --> 3ch

1ch --> 3ch 코드를 직접 따라가며 1ch --> 3ch 흐름을 확인했습니다.

- 읽을 포인트: 1ch --> 3ch 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 모델 설계

모델 설계 코드를 직접 따라가며 모델 설계 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### 학습/검증 함수

학습/검증 함수 코드를 직접 따라가며 학습/검증 함수 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

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

1. 코드 설명: CIFAR-100 사전학습: CIFAR-100 데이터셋을 사용해 SimpleCNN 모델을 5 에폭 동안 학습한 후, 가중치를 저장합니다. MNIST 데이터 전처리: MNIST 이미지를 32×32, 3채널로 변환하여 CIFAR-100 모델에 맞게 전처리...
2. 사전 함수: 사전 함수 코드를 직접 따라가며 사전 함수 흐름을 확인했습니다.
3. 1ch --> 3ch: 1ch --> 3ch 코드를 직접 따라가며 1ch --> 3ch 흐름을 확인했습니다.
4. 모델 설계: 모델 설계 코드를 직접 따라가며 모델 설계 흐름을 확인했습니다.
5. 학습/검증 함수: 학습/검증 함수 코드를 직접 따라가며 학습/검증 함수 흐름을 확인했습니다.

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

### 1ch --> 3ch

`1ch --> 3ch`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
from PIL import Image

gray_img_array = mnist_train.data[0].numpy()
gray_img_pil = Image.fromarray(gray_img_array, mode="L")

transform_to3 = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor()
])
img_method1 = transform_to3(gray_img_pil)
print(img_method1.shape)

img_method2 = transforms.ToTensor()(gray_img_pil.convert('RGB'))
print(img_method2.shape)
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

### 학습/검증 함수

`학습/검증 함수`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 preds = torch.argmax(outputs, dim=1) 흐름이 주석과 함께 드러납니다.

```python
def train_epoch(model, dataloader, loss_fn, opt):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for inputs, labels in tqdm(dataloader, leave=False, desc="Train"):
        inputs = inputs.to(device)
        labels = labels.to(device)

        opt.zero_grad()
        outputs = model(inputs)
        loss = loss_fn(outputs, labels)
        loss.backward()
        opt.step()

        running_loss += loss.item() * inputs.size(0)
        _, preds = torch.max(outputs, dim=1)
        # preds = torch.argmax(outputs, dim=1)
        correct += (preds == labels).sum().item()
        total += labels.size(0)

    epoch_loss = running_loss / total
    epoch_acc = correct / total
    return epoch_loss, epoch_acc
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
