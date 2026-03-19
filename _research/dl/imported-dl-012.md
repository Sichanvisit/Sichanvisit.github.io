---
title: "RNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)RNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)RNN.md"
excerpt: "PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다."
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
| Code Blocks | 17 |
| Execution Cells | 16 |
| Libraries | `torch`, `numpy`, `matplotlib` |
| Source Note | `(실습)RNN` |

## What I Worked On

- "나는 학교에 간다"
- "나는 학원에 간다"
- "나는 회사에 간다"
- "나는" --> torch.randn(10)
- "학교에" --> torch.randn(10)

## Implementation Flow

1. "나는 학교에 간다"
2. "나는 학원에 간다"
3. "나는 회사에 간다"
4. "나는" --> torch.randn(10)
5. "학교에" --> torch.randn(10)
6. LSTM

## Code Highlights

### 시계열 데이터 실습

```python
import torch

def creat_sequences(data, seq_length):
    sequence=[]
    labels=[]

    for i in range(len(data)-seq_length):
        sequence.append(data[i:i+seq_length])
        labels.append(data[i+seq_length])

    sequence = torch.tensor(np.array(sequence), dtype=torch.float32).unsqueeze(-1)
    labels = torch.tensor(np.array(labels), dtype=torch.float32)

    return sequence, labels

seq_length =50
X, y =creat_sequences(data, seq_length=seq_length)
print(X.shape, y.shape)
```

### 시계열 데이터 실습

```python
class RNNModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super().__init__()
        self.rnn = nn.RNN(input_size=input_size,
                          hidden_size=hidden_size,
                          num_layers=num_layers,
                          batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _= self.rnn(x)  # out: [450, 50, 20]
        ht = out[:,-1,:]     # ht   [450, 20]
        return self.fc(ht)   # output : [450, 1]
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)RNN.md`
- Source formats: `md`
- Companion files: `(실습)RNN.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다.
> input_size: 입력 특성의 차원 (예: 피처 개수)
