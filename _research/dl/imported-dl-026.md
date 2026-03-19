---
title: "RNN 레이어 설명 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-4_RNN 레이어 설명 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-4_RNN 레이어 설명 - 공유.md"
excerpt: "PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다."
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
| Code Blocks | 23 |
| Execution Cells | 18 |
| Libraries | `torch`, `numpy`, `matplotlib` |
| Source Note | `4-4_RNN 레이어 설명 - 공유` |

## What I Worked On

- 1. PyTorch에서 RNN, LSTM, GRU 사용법
- RNN
- LSTM
- GRU
- 시계열 데이터 실습

## Implementation Flow

1. 1. PyTorch에서 RNN, LSTM, GRU 사용법
2. RNN
3. LSTM
4. GRU
5. 시계열 데이터 실습
6. 간단한 데이터 생성

## Code Highlights

### 간단한 데이터 생성

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
