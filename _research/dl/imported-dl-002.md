---
title: "AutoEncoder"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)AutoEncoder"
source_path: "12_Deep_Learning/Code_Snippets/(실습)AutoEncoder.md"
excerpt: "오토인코더 구현 (MNIST), 모델 생성 및 학습 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 오토인코더 구현 (MNIST), 모델 생성 및 학습 순서로 핵심 장면을 먼저 훑고, 기본 전처리 + 데이터 로드, Basic Auto..."
research_summary: "오토인코더 구현 (MNIST), 모델 생성 및 학습 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 오토인코더 구현 (MNIST), 모델 생성 및 학습 순서로 핵심 장면을 먼저 훑고, 기본 전처리 + 데이터 로드, Basic Auto Encoder, 3D view 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 22개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, torch, torchvision입니다."
research_artifacts: "md · 코드 22개 · 실행 21개"
code_block_count: 22
execution_block_count: 21
research_focus:
  - "오토인코더 구현 (MNIST)"
  - "모델 생성 및 학습"
research_stack:
  - "numpy"
  - "matplotlib"
  - "torch"
  - "torchvision"
  - "plotly"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

오토인코더 구현 (MNIST), 모델 생성 및 학습 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 오토인코더 구현 (MNIST), 모델 생성 및 학습 순서로 핵심 장면을 먼저 훑고, 기본 전처리 + 데이터 로드, Basic Auto Encoder, 3D view 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 22개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, torch, torchvision입니다.

**빠르게 볼 수 있는 포인트**: 오토인코더 구현 (MNIST), 모델 생성 및 학습.

**남겨둔 자료**: `md` 원본과 22개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, torch, torchvision입니다.

**주요 스택**: `numpy`, `matplotlib`, `torch`, `torchvision`, `plotly`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 22 |
| Execution Cells | 21 |
| Libraries | `numpy`, `matplotlib`, `torch`, `torchvision`, `plotly` |
| Source Note | `(실습)AutoEncoder` |

## What This Note Covers

### 오토인코더 구현 (MNIST)

기본 전처리 + 데이터 로드 같은 코드를 직접 따라가며 오토인코더 구현 (MNIST) 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 기본 전처리 + 데이터 로드

#### 기본 전처리 + 데이터 로드

이미지 입력을 배치로 묶고 증강하며 학습 가능한 형태로 만드는 구간입니다.

### 모델 생성 및 학습

Basic Auto Encoder, Basic Auto Encoder..., CNN Auto Encoder 같은 코드를 직접 따라가며 모델 생성 및 학습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Basic Auto Encoder, Basic Auto Encoder > 3D view, CNN Auto Encoder

#### Basic Auto Encoder

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

#### Basic Auto Encoder > 3D view

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

#### CNN Auto Encoder

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

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

1. 오토인코더 구현 (MNIST): 기본 전처리 + 데이터 로드
2. 모델 생성 및 학습: Basic Auto Encoder, Basic Auto Encoder > 3D view

## Code Highlights

### 기본 전처리 + 데이터 로드

`기본 전처리 + 데이터 로드`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
train_dataset = datasets.FashionMNIST(
    root='./fmnist',
    train=True,
    download=True,
    transform=transforms
)

test_dataset = datasets.FashionMNIST(
    root='./fmnist',
    train=False,
    download=True,
    transform=transforms
)
```

### Basic Auto Encoder

`Basic Auto Encoder`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 BasicAutoEncoder, train 흐름이 주석과 함께 드러납니다.

```python
# BasicAutoEncoder
# train
epochs = 10
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for batch in train_loader:
        images = batch[0].to(device)
        images = images.view(images.size(0), -1)
        outputs = model(images)
        loss = loss_fn(outputs, images)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        total_loss += loss.item()
    print(f"Epoch : {epoch+1}/{epochs}, Loss : {total_loss/len(train_loader):.4f}")
```

### 3D view

`3D view`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 BasicAutoEncoder 2, train 흐름이 주석과 함께 드러납니다.

```python
# BasicAutoEncoder 2
# train
epochs = 10
for epoch in range(epochs):
    model2.train()
    total_loss = 0
    for batch in train_loader:
        images = batch[0].to(device)
        images = images.view(images.size(0), -1)
        outputs = model2(images)
        loss = loss_fn(outputs, images)

        loss.backward()
        optimizer2.step()
        optimizer2.zero_grad()

        total_loss += loss.item()
    print(f"Epoch : {epoch+1}/{epochs}, Loss : {total_loss/len(train_loader):.4f}")
```

### CNN Auto Encoder

`CNN Auto Encoder`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습, 학습 루프 흐름이 주석과 함께 드러납니다.

```python
# 모델 학습
model = CNNAutoEncoder().to(device)
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 학습 루프
epochs = 10
num_ch = 5

plt.figure(figsize=(20,10))

for epoch in range(epochs):
    model.train()
    running_loss = 0.
    for data in train_loader:
        inputs = data[0].to(device)
        outputs, encoded = model(inputs)

        loss = loss_fn(outputs,inputs)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        running_loss += loss.item()

    for c in range(num_ch):
        ax = plt.subplot(num_ch, epochs, epoch + c * epochs+1)
        encoded_img_channel = encoded[epoch, c, :,:].detach().cpu().numpy()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)AutoEncoder.md`
- Source formats: `md`
- Companion files: `(실습)AutoEncoder.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2025.10.1,2,13,14.md`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
