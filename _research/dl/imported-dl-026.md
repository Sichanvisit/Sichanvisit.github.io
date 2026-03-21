---
title: "RNN 레이어 설명 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-4_RNN 레이어 설명 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-4_RNN 레이어 설명 - 공유.md"
excerpt: "PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. input_size: 입력 특성의 차원 (예: 피처 개수). out: 모든 타임스텝..."
research_summary: "PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. input_size: 입력 특성의 차원 (예: 피처 개수). out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size]). `md` 원본과 23개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다."
research_artifacts: "md · 코드 23개 · 실행 18개"
code_block_count: 23
execution_block_count: 18
research_focus:
  - "PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를..."
  - "PyTorch에서 RNN, LSTM, GRU 사용법"
  - "out"
research_stack:
  - "torch"
  - "numpy"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. input_size: 입력 특성의 차원 (예: 피처 개수). out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size]). `md` 원본과 23개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: PyTorch에서는 torch.nn.RNN, torch.nn.LSTM,..., PyTorch에서 RNN, LSTM, GRU 사용법, out.

**남겨둔 자료**: `md` 원본과 23개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다.

**주요 스택**: `torch`, `numpy`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 23 |
| Execution Cells | 18 |
| Libraries | `torch`, `numpy`, `matplotlib` |
| Source Note | `4-4_RNN 레이어 설명 - 공유` |

## What This Note Covers

### PyTorch에서 RNN, LSTM, GRU 사용법

PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. input_size: 입력 특성의 차원 (예: 피처 개수)

### PyTorch에서 RNN, LSTM, GRU 사용법 > RNN

out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])

### PyTorch에서 RNN, LSTM, GRU 사용법 > LSTM

out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])

### PyTorch에서 RNN, LSTM, GRU 사용법 > GRU

out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. PyTorch에서 RNN, LSTM, GRU 사용법: PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. input_size: 입력 특...
2. PyTorch에서 RNN, LSTM, GRU 사용법 > RNN: out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])
3. PyTorch에서 RNN, LSTM, GRU 사용법 > LSTM: out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])
4. PyTorch에서 RNN, LSTM, GRU 사용법 > GRU: out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])

## Code Highlights

### RNN

`RNN`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
import torch
import torch.nn as nn

rnn = nn.RNN(input_size=10, hidden_size=20, num_layers=1, batch_first=False)

x = torch.randn(3, 32, 10)  # (seq_len, batch_size, input_size)
out, hidden = rnn(x)
print(out.shape, hidden.shape)
```

### 간단한 데이터 생성

`간단한 데이터 생성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 시계열 데이터를 모델이 학습할 수 있도록 입력과 정답(label)로 변환하는 함수, 주어진 데이터에서 일정 길이(seq_length)만큼의 연속된 데이터를 입력 시퀀스로 만들고,, 해당 시퀀스 바로 다음 값(y값)을 정답으로 설정 흐름이 주석과 함께 드러납니다.

```python
import torch

# 시계열 데이터를 모델이 학습할 수 있도록 입력과 정답(label)로 변환하는 함수
def create_sequences(data, seq_length):
    sequences = []  # 입력 데이터 시퀀스를 저장할 리스트
    labels = []  # 정답 값을 저장할 리스트

    # 주어진 데이터에서 일정 길이(seq_length)만큼의 연속된 데이터를 입력 시퀀스로 만들고,
    # 해당 시퀀스 바로 다음 값(y값)을 정답으로 설정
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i+seq_length]) # seq_length만큼의 데이터를 입력으로 사용
        labels.append(data[i+seq_length]) # 해당 시퀀스의 다음 값을 정답으로 설정

    # 리스트를 NumPy 배열로 변환 후 PyTorch 텐서로 변환
    sequences = torch.tensor(np.array(sequences), dtype=torch.float32).unsqueeze(-1)
    labels = torch.tensor(np.array(labels), dtype=torch.float32)

    return sequences, labels

seq_length = 50
X, y = create_sequences(data, seq_length)
print(X.shape, y.shape)  # 변환된 데이터의 크기 확인
```

### 🔍 설명

`🔍 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습, 예측 및 시각화 흐름이 주석과 함께 드러납니다.

```python
# 모델 학습
num_epochs = 100
for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs.squeeze(), y)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f'Epoch [{epoch}/{num_epochs}], Loss: {loss.item():.4f}')

# 예측 및 시각화
model.eval()
with torch.no_grad():
    predictions = model(X).numpy()
    print(predictions.shape)

plt.figure(figsize=(10, 4))
plt.plot(data, label='Actual')
plt.plot(range(seq_length, seq_length + len(predictions)), predictions, label='Predicted', linestyle='dashed')
plt.legend()
plt.title("Sine Wave Prediction using LSTM")
plt.show()
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/4-4_RNN 레이어 설명 - 공유.md`
- Source formats: `md`
- Companion files: `4-4_RNN 레이어 설명 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다.
> - input_size: 입력 특성의 차원 (예: 피처 개수)
