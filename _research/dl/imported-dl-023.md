---
title: "PyTorch DNN기초 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-1_PyTorch_DNN기초 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-1_PyTorch_DNN기초 - 공유.md"
excerpt: "각 레이어의 노드는 100개 일때, 아래 모델들을 실험해보세요"
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
| Code Blocks | 20 |
| Execution Cells | 13 |
| Libraries | `torch`, `sklearn`, `matplotlib`, `torchmetrics`, `numpy` |
| Source Note | `4-1_PyTorch_DNN기초 - 공유` |

## What I Worked On

- 실제 데이터 모델링
- Step1 : 데이터 수집
- Step 2 : 모델 만들기
- Step 3. 모델 학습시키기
- Step 4 모델 테스트하기

## Implementation Flow

1. 실제 데이터 모델링
2. Step1 : 데이터 수집
3. Step 2 : 모델 만들기
4. Step 3. 모델 학습시키기
5. Step 4 모델 테스트하기
6. Accuracy metric 객체 생성

## Code Highlights

### 실제 데이터 모델링

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
