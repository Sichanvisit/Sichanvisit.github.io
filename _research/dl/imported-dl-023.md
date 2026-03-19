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
