---
title: "GRU 모델 예제 (PyTorch)"
date: 2025-09-11
study_tab: "DL"
tags:
  - DL
  - GRU
  - PyTorch
  - RNN
  - LSTM
  - Time-Series
excerpt: "PyTorch로 GRU 모델을 구현하는 기본 예제와 핵심 코드 설명, LSTM과의 차이를 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

## GRU 모델 예제 (PyTorch)

```python
import torch
import torch.nn as nn

# GRU 모델 정의
class GRUModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(GRUModel, self).__init__()
        # GRU 계층
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
        # 최종 출력 계층 (FC Layer)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # h0 초기 hidden state (num_layers, batch_size, hidden_size)
        h0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)

        # GRU 계층 통과
        out, _ = self.gru(x, h0)  # out: (batch_size, seq_len, hidden_size)

        # 마지막 시점의 hidden state만 사용
        out = self.fc(out[:, -1, :])  # (batch_size, output_size)
        return out


# 하이퍼파라미터 설정
input_size = 10     # 입력 특성 차원
hidden_size = 20    # GRU의 hidden state 크기
num_layers = 2      # GRU 계층 수
output_size = 1     # 출력 차원 (예: 회귀라면 1)

# 모델 초기화
model = GRUModel(input_size, hidden_size, num_layers, output_size)
print(model)

# 예시 입력 (batch_size=5, seq_len=7, input_size=10)
x = torch.randn(5, 7, input_size)
output = model(x)
print("Output shape:", output.shape)  # (5, 1)
```

## 코드 설명

### 1. GRU 정의

`self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)`

- `input_size`: 입력 데이터의 특성 차원
- `hidden_size`: hidden state 크기
- `num_layers`: GRU 레이어 수
- `batch_first=True`: 입력/출력 shape을 `(batch, seq_len, input_size)`로 사용

### 2. 초기 hidden state

`h0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)`

- GRU는 LSTM과 달리 cell state(`c`)가 없고 hidden state(`h`)만 사용
- 따라서 초기 상태도 `h0`만 정의

### 3. GRU forward 연산

`out, _ = self.gru(x, h0)`

- `out`: `(batch_size, seq_len, hidden_size)`
- `_`: 마지막 hidden state `(num_layers, batch_size, hidden_size)`

### 4. 최종 출력

`out = self.fc(out[:, -1, :])`

- 마지막 시점 hidden state를 FC 계층에 통과시켜 최종 출력 생성
- 최종 shape: `(batch_size, output_size)`

## LSTM과 GRU 차이

- **LSTM**: hidden state(`h`) + cell state(`c`) 사용 → 메모리 관리가 더 정교
- **GRU**: hidden state(`h`)만 사용 → 구조 단순, 연산 속도 빠름

실제 성능 우위는 데이터 특성과 문제 설정에 따라 달라집니다.

