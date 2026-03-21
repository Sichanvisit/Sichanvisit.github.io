---
title: "PyTorch DNN기초 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-1_PyTorch_DNN기초 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-1_PyTorch_DNN기초 - 공유.md"
excerpt: "각 레이어의 노드는 100개 일때, 아래 모델들을 실험해보세요"
research_summary: "각 레이어의 노드는 100개 일때, 아래 모델들을 실험해보세요. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 20개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, sklearn, matplotlib, torchmetrics입니다."
research_artifacts: "md · 코드 20개 · 실행 13개"
code_block_count: 20
execution_block_count: 13
research_focus:
  - "실제 데이터 모델링"
  - "다중분류"
  - "각 레이어의 노드는 100개 일때, 아래 모델들을 실험해보세요"
research_stack:
  - "torch"
  - "sklearn"
  - "matplotlib"
  - "torchmetrics"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

각 레이어의 노드는 100개 일때, 아래 모델들을 실험해보세요. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 20개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, sklearn, matplotlib, torchmetrics입니다.

**빠르게 볼 수 있는 포인트**: 실제 데이터 모델링, 다중분류, 각 레이어의 노드는 100개 일때, 아래 모델들을 실험해보세요.

**남겨둔 자료**: `md` 원본과 20개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, sklearn, matplotlib, torchmetrics입니다.

**주요 스택**: `torch`, `sklearn`, `matplotlib`, `torchmetrics`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 20 |
| Execution Cells | 13 |
| Libraries | `torch`, `sklearn`, `matplotlib`, `torchmetrics`, `numpy` |
| Source Note | `4-1_PyTorch_DNN기초 - 공유` |

## What This Note Covers

### 문제: 실험하기

각 레이어의 노드는 100개 일때, 아래 모델들을 실험해보세요

### Key Step

Step 3. 모델 학습시키기

### Key Step

Accuracy metric 객체 생성

### Key Step

데이터 분할: train, validation, test

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. 문제: 실험하기: 각 레이어의 노드는 100개 일때, 아래 모델들을 실험해보세요
2. Key Step: Step 3. 모델 학습시키기
3. Key Step: Accuracy metric 객체 생성
4. Key Step: 데이터 분할: train, validation, test

## Code Highlights

### 실제 데이터 모델링

`실제 데이터 모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Step 3. 모델 학습시키기 흐름이 주석과 함께 드러납니다.

```python
### Step 3. 모델 학습시키기

LR = 1e-1
criterion = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LR)

EPOCH = 100
BATCH_SIZE = 210

dataset = TensorDataset(X_train, y_train)
dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

losses = []

for epoch in range(EPOCH):
    for batch_X, batch_y in dataloader:
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
    losses.append(loss.item())

plt.plot(range(1, EPOCH+1), losses)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()
```

### 다중분류

`다중분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 설정, 데이터 로더 생성, 학습 루프 흐름이 주석과 함께 드러납니다.

```python
# 학습 설정
EPOCH = 50
BATCH_SIZE = 32

# 데이터 로더 생성
dataset_train = TensorDataset(X_train, y_train)
dataset_val = TensorDataset(X_val, y_val)

dataloader_train = DataLoader(dataset_train, batch_size=BATCH_SIZE, shuffle=True)
dataloader_val = DataLoader(dataset_val, batch_size=BATCH_SIZE)

losses = []
val_losses = []

# 학습 루프
for epoch in range(EPOCH):
    model.train()
    for batch_X, batch_y in dataloader_train:
        optimizer.zero_grad()
        outputs = model(batch_X)  # Logits 반환
        loss = criterion(outputs, batch_y)  # CrossEntropyLoss 적용
        loss.backward()
        optimizer.step()
    losses.append(loss.item())

    # 검증 손실 계산
    model.eval()
    with torch.no_grad():
# ... trimmed ...
```

### 와인 데이터

`와인 데이터`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터 로드 및 학습/검증 세트 분리 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# 데이터 로드 및 학습/검증 세트 분리
wine = load_wine()
X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, test_size=0.3, shuffle=True, random_state=42
)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/4-1_PyTorch_DNN기초 - 공유.md`
- Source formats: `md`
- Companion files: `4-1_PyTorch_DNN기초 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `lightning.ai`, `localhost`

## Note Preview

> -
> torchmetrics
