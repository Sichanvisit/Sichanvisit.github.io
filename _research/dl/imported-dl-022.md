---
title: "PyTorch 모델링 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-3_PyTorch_모델링 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-3_PyTorch_모델링 - 공유.md"
excerpt: "PyTorch 모델링 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 torch.nn.functional..., nn에서 객체를 활용하는 방식, 모델 만들기 순서로 핵심 장면을 먼저 훑고, PyTorch에서 기본 장치는 CPU, Trainin..."
research_summary: "PyTorch 모델링 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 torch.nn.functional..., nn에서 객체를 활용하는 방식, 모델 만들기 순서로 핵심 장면을 먼저 훑고, PyTorch에서 기본 장치는 CPU, Training Loop 이해하기, Training Loop 정리 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 120개 코드 블록, 57개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다."
research_artifacts: "md · 코드 120개 · 실행 57개"
code_block_count: 120
execution_block_count: 57
research_focus:
  - "torch.nn.functional 활용하기"
  - "nn에서 객체를 활용하는 방식"
  - "모델 만들기"
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
  - shared-note
---

PyTorch 모델링 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 torch.nn.functional..., nn에서 객체를 활용하는 방식, 모델 만들기 순서로 핵심 장면을 먼저 훑고, PyTorch에서 기본 장치는 CPU, Training Loop 이해하기, Training Loop 정리 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 120개 코드 블록, 57개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다.

**빠르게 볼 수 있는 포인트**: torch.nn.functional 활용하기, nn에서 객체를 활용하는 방식, 모델 만들기.

**남겨둔 자료**: `md` 원본과 120개 코드 블록, 57개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다.

**주요 스택**: `torch`, `numpy`, `pandas`, `sklearn`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 120 |
| Execution Cells | 57 |
| Libraries | `torch`, `numpy`, `pandas`, `sklearn`, `matplotlib` |
| Source Note | `3-3_PyTorch_모델링 - 공유` |

## What This Note Covers

### torch.nn.functional 활용하기

그래서 PyTorch에는 모델을 정의하고 학습시킬 때 사용 가능한 '함수'들이 존재합니다. 바로 torch.nn.functional에서 제공하는 함수들인데요. 객체를 만들지 않아도 동일한 연산을 함수 형태로 편리하게 수행할 수 있습니다. torch.nn.functional은 일반적으로 아래처럼 F라는 이름으로 가져옵니다.

- 읽을 포인트: torch.nn.functional 활용하기 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### nn에서 객체를 활용하는 방식

지금까지 모델을 정의할 때 레이어나 활성화 함수를 객체로 만들어 사용했습니다. 모델 안에서 다른 모델을 쓸 때도 객체로 만들어 사용했고요. 모델을 학습시킬 때 손실 함수 역시 객체를 활용했어요. 이 객체들은 모두 nn.Module을 상속받은 클래스로 만들어진 객체였습니다. 모델 구성 요소를 객체로 다루면 nn.Module이 가진 속성...

- 읽을 포인트: nn에서 객체를 활용하는 방식에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### 모델 만들기

torch.nn 살펴보기, nn.Module로 모델 만들기 >..., 복잡한 모델 설계하기 같은 코드를 직접 따라가며 모델 만들기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: torch.nn 살펴보기, nn.Module로 모델 만들기 > 모델 정의 : nn.Module 상속, 복잡한 모델 설계하기

#### torch.nn 살펴보기

PyTorch에서는 딥러닝 모델을 간편하게 만들 수 있도록 torch.nn 모듈을 제공합니다. 이 모듈은 신경망을 구성하는 레이어, 활성화 함수, 손실 함수 등을 쉽게 구현할 수 있도록 다양한 클래스를 포함하고 있습니다. torch.nn 모듈의 주요 기능

#### nn.Module로 모델 만들기 > 모델 정의 : nn.Module 상속

모델 클래스를 정의할 때, 반드시 torch.nn.Module을 상속받아야 합니다. 이로써 PyTorch의 다양한 기능을 활용할 수 있으며, 계층 구조를 손쉽게 설계할 수 있습니다.

#### 복잡한 모델 설계하기

입력과 출력이 여러 개이며, 병렬 구조를 포함하는 복잡한 모델을 설계하는 방법을 배웁니다. PyTorch의 torch.nn.Module을 활용하여 다양한 구조의 모델을 효율적으로 구현할 수 있습니다. 다음은 구현할 모델의 구조입니다.

### 모델 학습시키기

Training Loop 이해하기, Training Loop 이해하기..., Training Loop 정리 같은 코드를 직접 따라가며 모델 학습시키기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Training Loop 이해하기, Training Loop 이해하기 > 모델 설명, Training Loop 정리

#### Training Loop 이해하기

PyTorch를 사용하여 전복(abalone) 데이터를 기반으로 회귀 문제를 푸는 과정을 살펴보겠습니다. 이 교안에서는 데이터 준비, 모델 생성, 그리고 학습 루프의 뼈대를 설명합니다.

#### Training Loop 이해하기 > 모델 설명

구조: Fully Connected Layers로 구성. - 첫 레이어는 입력 피처 7개, 출력 32개. - 마지막 레이어는 출력 1개로, 나이를 예측. - 활성화 함수: ReLU 활성화 함수 사용. - 출력: 회귀 문제에 적합하게 마지막 레이어에서는 활성화 함수를 적용하지 않음.

#### Training Loop 정리

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

## Why This Matters

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

## Implementation Flow

1. torch.nn.functional 활용하기: 그래서 PyTorch에는 모델을 정의하고 학습시킬 때 사용 가능한 '함수'들이 존재합니다. 바로 torch.nn.functional에서 제공하는 함수들인데요. 객체를 만들지 않아도 동일한 연산을 함수 형태로 편리하게...
2. nn에서 객체를 활용하는 방식: 지금까지 모델을 정의할 때 레이어나 활성화 함수를 객체로 만들어 사용했습니다. 모델 안에서 다른 모델을 쓸 때도 객체로 만들어 사용했고요. 모델을 학습시킬 때 손실 함수 역시 객체를 활용했어요. 이 객체들은 모두 nn.Module을...
3. 모델 만들기: torch.nn 살펴보기, nn.Module로 모델 만들기 > 모델 정의 : nn.Module 상속
4. 모델 학습시키기: Training Loop 이해하기, Training Loop 이해하기 > 모델 설명

## Code Highlights

### PyTorch에서 기본 장치는 CPU

`PyTorch에서 기본 장치는 CPU`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. PyTorch에서는 텐서뿐만 아니라 모델도 어떤 장치에서 사용할지 설정할 수 있습니다. 일단 텐서와 마찬가지로 모델도 기본적으로 CPU에 만들어져요.

```python
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear0 = nn.Linear(8, 4)
        self.linear1 = nn.Linear(4, 6)
        self.linear2 = nn.Linear(6, 3)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.linear0(x))
        x = self.relu(self.linear1(x))
        output = self.linear2(x)
        return output

model = MyModel()  # model이 CPU에 만들어짐
```

### Training Loop 이해하기

`Training Loop 이해하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습 흐름이 주석과 함께 드러납니다.

```python
# @title 모델 학습
epochs = 100
lr = 0.001
momentum = 0.9
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)
step=0

for epoch in range(epochs):
  model.train()
  for train_batch in train_dataloader:
    x_train = train_batch[0].to(device)
    y_train = train_batch[1].to(device)

    pred = model(x_train).squeeze()
    loss = loss_fn(pred, y_train)

    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

    step += 1

    if step % 100 == 0:
      print(f'step : {step} // train loss : {loss.item()}')

  model.eval()
  with torch.no_grad():
# ... trimmed ...
```

### Training Loop 정리

`Training Loop 정리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터 불러오기, 입력과 타깃 나누기, 데이터셋 클래스 정의 흐름이 주석과 함께 드러납니다.

```python
# 데이터 불러오기
abalone_df = pd.read_csv(
    'https://storage.googleapis.com/download.tensorflow.org/data/abalone_train.csv',
    names=['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
           'Viscera weight', 'Shell weight', 'Age']
)

# 입력과 타깃 나누기
input_data = abalone_df.drop(columns=['Age']).to_numpy().astype(np.float32)
target_data = abalone_df['Age'].to_numpy().astype(np.float32)

# 데이터셋 클래스 정의
class AbaloneDataset(Dataset):
    def __init__(self, input_data, target_data):
        self.input_data = input_data
        self.target_data = target_data

    def __len__(self):
        return len(self.input_data)

    def __getitem__(self, index):
        input_tensor = torch.tensor(self.input_data[index])
        target_tensor = torch.tensor(self.target_data[index])
        return input_tensor, target_tensor

# 학습/검증/테스트 데이터 분할
train_size = int(len(input_data) * 0.8)
val_size = int(len(input_data) * 0.1)
# ... trimmed ...
```

### 트레이닝 루프에 저장 코드 추가

`트레이닝 루프에 저장 코드 추가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 training loop, 에폭마다 모델 저장 흐름이 주석과 함께 드러납니다.

```python
# training loop
epochs = 10
step = 0
for epoch in range(epochs):
    model.train()
    for train_batch in train_dataloader:
        x_train, y_train = train_batch[0].to(device), train_batch[1].to(device)
        pred = model(x_train).squeeze()
        loss = loss_fn(pred, y_train)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        step += 1

        if step % 100 == 0:
            print(f'Loss at step {step}: {loss.item():.4f}')

    model.eval()
    with torch.no_grad():
        losses = []
        for val_batch in val_dataloader:
            x_val, y_val = val_batch[0].to(device), val_batch[1].to(device)
            pred_val = model(x_val).squeeze()
            loss = loss_fn(pred_val, y_val)
            losses.append(loss.item())

        val_loss_avg = sum(losses) / len(losses)
        print(f'epoch {epoch+1}/{epochs}, validation loss: {val_loss_avg:.4f}\n')
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/3-3_PyTorch_모델링 - 공유.md`
- Source formats: `md`
- Companion files: `3-3_PyTorch_모델링 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2.0, 2.0, 2.0`, `0.0, 0.0, 1.0`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> - 텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다!
> - torch.autograd.grad는 함수𝑓의 결과(outputs)에 대해 지정된 입력 변수들(inputs) 각각의 기울기를 반환합니다. - 반환값은 튜플 형태이며, 기울기 값을 직접 확인할 수 있습니다. - 장점: 특정 입력 변수만 선택적으로 기울기를 계산할 수 있습니다
