---
title: "RNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)RNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)RNN.md"
excerpt: "PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다"
research_summary: "PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]). `md` 원본과 17개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다."
research_artifacts: "md · 코드 17개 · 실행 16개"
code_block_count: 17
execution_block_count: 16
research_focus:
  - "PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를..."
  - "out"
  - "LSTM"
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
  - archive-note
---

PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]). `md` 원본과 17개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: PyTorch에서는 torch.nn.RNN, torch.nn.LSTM,..., out, LSTM.

**남겨둔 자료**: `md` 원본과 17개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다.

**주요 스택**: `torch`, `numpy`, `matplotlib`

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

## What This Note Covers

### RNN

PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다.

### LSTM

out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size])

### GRU

out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size])

### Key Step

"나는" --> torch.randn(10)

## Implementation Flow

1. RNN: PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다.
2. LSTM: out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size])
3. GRU: out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size])
4. Key Step: "나는" --> torch.randn(10)

## Code Highlights

### RNN

`RNN`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. bidirectional: 양방향 RNN 사용 여부 (기본값 False).

```python
import torch
import torch.nn as nn

rnn = nn.RNN(input_size=10, hidden_size=20, num_layers=1, batch_first=False)

x = torch.randn(3,32,10) # --> (Seq_len, batch_size, input_size)
out, hidden =rnn(x)
print(out.shape, hidden.shape)
```

### 시계열 데이터 실습

`시계열 데이터 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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
