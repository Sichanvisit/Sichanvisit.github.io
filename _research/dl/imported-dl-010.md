---
title: "PyTorch 모델"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_모델"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_모델.md"
excerpt: "PyTorch 모델에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 만들기, 모델 학습 하기, 모델 저장 순서로 핵심 장면을 먼저 훑고, Autograd, 복잡한 모델 설계, 모델 학습 하기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다...."
research_summary: "PyTorch 모델에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 만들기, 모델 학습 하기, 모델 저장 순서로 핵심 장면을 먼저 훑고, Autograd, 복잡한 모델 설계, 모델 학습 하기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 66개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다."
research_artifacts: "md · 코드 66개 · 실행 59개"
code_block_count: 66
execution_block_count: 59
research_focus:
  - "모델 만들기"
  - "모델 학습 하기"
  - "모델 저장"
research_stack:
  - "torch"
  - "numpy"
  - "pandas"
  - "sklearn"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

PyTorch 모델에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 만들기, 모델 학습 하기, 모델 저장 순서로 핵심 장면을 먼저 훑고, Autograd, 복잡한 모델 설계, 모델 학습 하기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 66개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다.

**빠르게 볼 수 있는 포인트**: 모델 만들기, 모델 학습 하기, 모델 저장.

**남겨둔 자료**: `md` 원본과 66개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다.

**주요 스택**: `torch`, `numpy`, `pandas`, `sklearn`, `matplotlib`

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

## What This Note Covers

### 모델 만들기

torch.nn, nn.Module로 모델 만들기, 모델 정보 확인하기 같은 코드를 직접 따라가며 모델 만들기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: torch.nn, nn.Module로 모델 만들기, 모델 정보 확인하기

#### torch.nn

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

#### nn.Module로 모델 만들기

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

#### 모델 정보 확인하기

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### 모델 학습 하기

모델 학습 하기 코드를 직접 따라가며 모델 학습 하기 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### 모델 저장

모델 저장 코드를 직접 따라가며 모델 저장 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

## Why This Matters

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

## Implementation Flow

1. 모델 만들기: torch.nn, nn.Module로 모델 만들기
2. 모델 학습 하기: 모델 학습 하기 코드를 직접 따라가며 모델 학습 하기 흐름을 확인했습니다.
3. 모델 저장: 모델 저장 코드를 직접 따라가며 모델 저장 흐름을 확인했습니다.

## Code Highlights

### Autograd

`Autograd`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 backward(), 1.텐서 정의, 초기화, 수식 흐름이 주석과 함께 드러납니다.

```python
# backward()

import torch
import torch.optim as optim

# 1.텐서 정의, 초기화
x1 = torch.tensor(2., requires_grad=True)
x2 = torch.tensor(3., requires_grad=True)
x3 = torch.tensor(1., requires_grad=True)
x4 = torch.tensor(4., requires_grad=True)

opt = optim.SGD(params=[x1,x2,x3,x4], lr = 0.001) # optimizer 설정

for i in range(3):
    opt.zero_grad()                               # 기울기 초기화

    # 2. 수식
    z1 = x1 * x2
    z2 = x3 * x4
    f = z1 + z2

    # 3. backward 기울기 계산 -> 모든 변수의 기울기를 자동으로 계산 + 저장
    f.backward()
    # opt.step() # 파라미터 업데이트

    # 4. 결과
    print(f"gradients")
    print(f"gradients of x1 = {x1.grad}")
# ... trimmed ...
```

### 복잡한 모델 설계

`복잡한 모델 설계`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실험의 중심이 되는 모델 아키텍처를 정의하는 코드입니다.

```python
class ComplexModel2(nn.Module):
    def __init__(self):
        super().__init__()
        self.dense1 = nn.Linear(10,16)
        self.dense2 = nn.Linear(5,16)
        self.dense3 = nn.Linear(32,32)
        self.dense4 = nn.Linear(32,32)

        self.relu = nn.ReLU()

        self.aux_output = nn.Linear(16,1)
        self.main_output = nn.Linear(32,1)

    def forward(self, input1, input2):
        x1 = self.relu(self.dense1(input1))
        out1 = self.aux_output(x1)

        x2 = self.relu(self.dense2(input2))
        x2 = torch.cat([x1,x2],dim=1)
        x2 = self.relu(self.dense3(x2))
        x2 = self.relu(self.dense4(x2))
        out2 = self.main_output(x2)

        return out1, out2
```

### 모델 학습 하기

`모델 학습 하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 x_train, y_train = train_batch, pred 와 y_train 간의 loss 계산, print(pred.size()) 흐름이 주석과 함께 드러납니다.

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

`모델 저장`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 x_train, y_train = train_batch, if old_loss > loss, torch.save(model.state_dict(), 'model_best.pt') 흐름이 주석과 함께 드러납니다.

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
