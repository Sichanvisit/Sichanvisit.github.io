---
title: "PyTorch 모델"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_모델"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_모델.md"
excerpt: "텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다!"
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
| Code Blocks | 66 |
| Execution Cells | 59 |
| Libraries | `torch`, `numpy`, `pandas`, `sklearn`, `matplotlib` |
| Source Note | `(실습)PyTorch_모델` |

## What I Worked On

- 모델 만들기
- Autograd
- 1.텐서 정의, 초기화
- 2. 수식
- 3. autograd.grad 기울기 계산

## Implementation Flow

1. 모델 만들기
2. Autograd
3. 1.텐서 정의, 초기화
4. 2. 수식
5. 3. autograd.grad 기울기 계산
6. 4. 결과

## Code Highlights

### 모델 학습 하기

```python
import torch.optim as optim

epochs = 10
step = 0
loss_fn = nn.MSELoss()
opt = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

for epoch in range(epochs):
    model.train()
    for train_batch in train_dataloader:
        # x_train, y_train = train_batch
        x_train, y_train = train_batch[0].to(device), train_batch[1].to(device)
        pred = model(x_train).squeeze() # 추론

        # pred 와 y_train 간의 loss 계산
        # print(pred.size())
        # print(y_train.size())
        # break
        loss = loss_fn(pred, y_train)
        loss.backward() # 그래디언트 계산

        opt.step() # 파라미터 업데이트
        opt.zero_grad() #그래디언트 초기화

        step += 1

        if step % 100 == 0:
            print(f"epoch : {epoch+1}, step : {step}, train loss: {loss.item():.4f}")
# ... trimmed ...
```

### 모델 저장

```python
import torch.optim as optim

epochs = 10
step = 0
loss_fn = nn.MSELoss()
opt = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

for epoch in range(epochs):
    model.train()
    for train_batch in train_dataloader:
        # x_train, y_train = train_batch
        x_train, y_train = train_batch[0].to(device), train_batch[1].to(device)
        pred = model(x_train).squeeze() # 추론
        loss = loss_fn(pred, y_train)
        loss.backward() # 그래디언트 계산

        opt.step() # 파라미터 업데이트
        opt.zero_grad() #그래디언트 초기화
        step += 1

        if step % 100 == 0:
            print(f"epoch : {epoch+1}, step : {step}, train loss: {loss.item():.4f}")

    model.eval()
    with torch.no_grad():
        losses = []
        for val_batch in val_dataloader:
            x_val, y_val = val_batch[0].to(device), val_batch[1].to(device)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)PyTorch_모델.md`
- Source formats: `md`
- Companion files: `(실습)PyTorch_모델.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> 텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다!
> .backward()는 requires_grad=True로 설정된 모든 변수의 기울기를 자동으로 계산하고, 각 변수의 .grad 속성에 저장합니다. opt.zero_grad()를 사용해 이전 계산의 기울기 값을 초기화해야 누적된 기울기를 방지할 수 있습니다. 장점: 코드가 간결하며, 다수의 변수에 대해 빠르게 기울기를 계산할 수 있습니다.
