---
title: "RNN(순환 신경망) 사용 방법 정리 – PyTorch 기반"
date: 2026-03-05
study_tab: "DL"
tags:
  - DL
  - RNN
  - PyTorch
  - Time-Series
  - NLP
  - LSTM
  - GRU
excerpt: "RNN을 언제 쓰는지부터 PyTorch 구현(데이터 준비, 모델 정의, 학습, 평가)까지 단계별로 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

순환 신경망(Recurrent Neural Network, RNN)은 **순차 데이터(Sequential Data)**를 처리하는 데 특화된 딥러닝 모델입니다.  
이번 글에서는 RNN이 언제 유용한지, 그리고 PyTorch를 활용해 구현/학습하는 과정을 단계별로 정리합니다.

## RNN은 언제 사용할까?

RNN은 각 시점 데이터가 이전 시점과 독립적이지 않은 문제에 적합합니다.

- 자연어 처리(NLP): 문맥 기반 다음 단어 예측
- 음성 인식: 시간 순서 음성 신호 처리
- 시계열 분석: 주가/날씨 예측
- 생물정보학: DNA 염기서열 분석

MLP와 달리, RNN은 시퀀스를 순차적으로 받아 문맥 정보를 반영할 수 있습니다.

## RNN 활용 단계

### 1. 데이터 준비

- 시퀀스 데이터 구성: `seq_len` 길이 입력 → 다음 시점 값을 라벨로 설정
- `DataLoader`로 배치 학습 구성 (`shuffle=True` 권장)

### 2. 모델 정의

PyTorch에서 `nn.Module`을 상속해 모델을 만듭니다.

`nn.RNN` 주요 인자:
- `input_size`: 시점별 입력 벡터 크기
- `hidden_size`: 은닉 상태 크기
- `num_layers`: RNN 층 수
- `batch_first=True`: 입력 텐서 형식 `(batch, seq_len, feature)`

출력층(`nn.Linear`)에서 마지막 은닉 상태를 최종 예측값으로 변환합니다.

### 3. 학습 과정

- 손실 함수:
  - 회귀: `nn.MSELoss`
  - 분류: `nn.CrossEntropyLoss`
- 옵티마이저: 보통 `Adam` 또는 `SGD`
- 학습 루프:
  - `model.train()`
  - `optimizer.zero_grad()`
  - 순전파 → 손실 계산 → 역전파(BPTT) → 파라미터 업데이트

### 4. 평가

- `model.eval()`
- `torch.no_grad()` 블록에서 예측 수행

## 코드 예시 (PyTorch)

```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.utils.data import TensorDataset, DataLoader

# 1. 데이터 준비
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

# 2. 모델 정의
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        output, h_n = self.rnn(x)
        out = self.fc(h_n[-1, :, :])  # 마지막 은닉 상태 사용
        return out

model = SimpleRNN(input_size, hidden_size, num_layers, output_size)

# 3. 학습 설정
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 학습 루프
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

## RNN의 한계와 발전 모델

기본 RNN은 다음 한계가 있습니다.

- 기울기 소실(Vanishing Gradient)
- 장기 의존성(Long-term Dependency) 학습 어려움

개선 모델:
- **LSTM**: 셀 상태 + 게이트로 장기 의존성 강화
- **GRU**: LSTM보다 단순, 학습 속도 유리

실무에서는 LSTM/GRU/Transformer가 더 자주 쓰입니다.

## 마무리

RNN 파이프라인은 `데이터 준비 → 모델 정의 → 학습 → 평가` 순서로 정리할 수 있습니다.  
기본 RNN을 이해한 뒤 LSTM/GRU로 확장하면 실전 활용성이 높아집니다.

