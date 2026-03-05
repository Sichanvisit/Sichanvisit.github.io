---
title: "LSTM(Long Short-Term Memory) 사용 방법 정리 – PyTorch 기반"
date: 2025-09-11
study_tab: "DL"
tags:
  - DL
  - LSTM
  - PyTorch
  - RNN
  - Time-Series
  - NLP
  - GRU
excerpt: "LSTM의 핵심 아이디어와 PyTorch 구현(데이터 준비, 모델 정의, 학습, 평가), RNN과의 비교를 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

RNN은 순차 데이터 처리에 강력하지만, 장기 의존성(Long-term Dependency) 학습에서 기울기 소실 문제가 발생하기 쉽습니다.  
이를 해결하기 위해 등장한 모델이 **LSTM(Long Short-Term Memory)**입니다.

## LSTM의 핵심 아이디어

기본 RNN은 이전 은닉 상태 중심으로 정보를 전달하지만, LSTM은 **셀 상태(Cell State)**를 추가해 장기 정보를 더 안정적으로 유지합니다.

이를 제어하는 구조가 게이트(Gate)입니다.

- 입력 게이트(Input Gate): 새 정보 반영 정도 결정
- 망각 게이트(Forget Gate): 기존 정보 유지/삭제 결정
- 출력 게이트(Output Gate): 은닉 상태 출력 방식 결정

덕분에 LSTM은 긴 문맥이 필요한 문제(시계열, NLP, 음성 등)에 유리합니다.

## LSTM 활용 단계

### 1. 데이터 준비

RNN과 동일하게 시퀀스를 구성합니다.  
예: `seq_len` 길이 입력 시퀀스 → 다음 시점 값을 라벨로 설정

### 2. 모델 정의

PyTorch에서 `nn.Module` 상속 후 `nn.LSTM`을 사용합니다.

`nn.LSTM` 출력:
- `output`: 모든 시점 은닉 상태
- `h_n`: 마지막 시점 은닉 상태
- `c_n`: 마지막 시점 셀 상태

보통 예측에는 `h_n[-1]`을 활용하고, `nn.Linear`로 최종 출력에 매핑합니다.

### 3. 학습 과정

- 손실 함수:
  - 회귀: `nn.MSELoss`
  - 분류: `nn.CrossEntropyLoss`
- 옵티마이저: 주로 `Adam`
- 학습 루프:
  - `forward -> loss -> backward -> step`

## 코드 예제 (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.utils.data import TensorDataset, DataLoader

# 1. 데이터 준비 (사인파 시계열)
seq_len, hidden_size, num_layers = 40, 64, 1
input_size, output_size = 1, 1

time = np.arange(0, 1000)
data = np.sin(time / 10.0) + np.random.rand(1000) * 0.1

X, Y = [], []
for i in range(len(data) - seq_len):
    X.append(data[i:i+seq_len])
    Y.append(data[i+seq_len])

X = torch.tensor(X, dtype=torch.float32).unsqueeze(-1)
Y = torch.tensor(Y, dtype=torch.float32).unsqueeze(-1)

dataset = TensorDataset(X, Y)
train_loader = DataLoader(dataset, batch_size=64, shuffle=True)

# 2. LSTM 모델 정의
class SimpleLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(SimpleLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        output, (h_n, c_n) = self.lstm(x)
        out = self.fc(h_n[-1, :, :])  # 마지막 레이어 은닉 상태 사용
        return out

model = SimpleLSTM(input_size, hidden_size, num_layers, output_size)

# 3. 학습 설정
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(5):
    model.train()
    total_loss = 0
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f'Epoch [{epoch+1}/5], Loss: {total_loss/len(train_loader):.4f}')

# 4. 평가
model.eval()
with torch.no_grad():
    test_input = X[0].unsqueeze(0)
    predicted = model(test_input)
    print(f'예측값: {predicted.item():.4f}, 실제값: {Y[0].item():.4f}')
```

## RNN vs LSTM 비교

| 항목 | RNN | LSTM |
|---|---|---|
| 기억 범위 | 짧은 시점 중심 | 긴 시점까지 가능 |
| 주요 문제 | 기울기 소실 | 게이트 구조로 완화 |
| 출력 구조 | `(output, h_n)` | `(output, (h_n, c_n))` |
| 활용 분야 | 짧은 패턴 예측 | 장기 시계열, 문장 단위 NLP |

## 마무리

LSTM은 RNN의 한계를 보완해 긴 문맥 학습이 가능한 구조입니다.  
실무에서는 GRU, Transformer까지 확장되지만, LSTM 구조와 학습 흐름을 이해하는 것이 고급 모델로 넘어가는 중요한 기초가 됩니다.

