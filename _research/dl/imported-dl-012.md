---
title: "RNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)RNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)RNN.md"
excerpt: "RNN, LSTM 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 RNN, LSTM, GRU 순서로 핵심 장면을 먼저 훑고, RNN, LSTM, GRU 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 17개 코드..."
research_summary: "RNN, LSTM 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 RNN, LSTM, GRU 순서로 핵심 장면을 먼저 훑고, RNN, LSTM, GRU 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 17개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다."
research_artifacts: "md · 코드 17개 · 실행 16개"
code_block_count: 17
execution_block_count: 16
research_focus:
  - "RNN"
  - "LSTM"
  - "GRU"
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

RNN, LSTM 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 RNN, LSTM, GRU 순서로 핵심 장면을 먼저 훑고, RNN, LSTM, GRU 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 17개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: RNN, LSTM, GRU.

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

PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. input_size: 입력 특성의 차원 (예: 피처 개수)

- 읽을 포인트: RNN 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### LSTM

out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])

- 읽을 포인트: LSTM 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### GRU

out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])

- 읽을 포인트: GRU 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 시계열 데이터 실습

시계열 데이터 실습 코드를 직접 따라가며 시계열 데이터 실습 흐름을 확인했습니다.

- 읽을 포인트: 시계열 데이터 실습 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. RNN: PyTorch에서는 torch.nn.RNN, torch.nn.LSTM, torch.nn.GRU 클래스를 사용하여 순환 신경망을 쉽게 구현할 수 있습니다. 각 클래스는 공통적으로 아래와 같은 주요 파라미터를 가집니다. input_size: 입력 특성의 차원...
2. LSTM: out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])
3. GRU: out: 모든 타임스텝의 출력 ([batch_size, seq_len, hidden_size]) hidden: 마지막 타임스텝의 은닉 상태 ([num_layers, batch_size, hidden_size])
4. 시계열 데이터 실습: 시계열 데이터 실습 코드를 직접 따라가며 시계열 데이터 실습 흐름을 확인했습니다.

## Code Highlights

### RNN

`RNN`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 "나는 학교에 간다", "나는 학원에 간다", "나는 회사에 간다" 흐름이 주석과 함께 드러납니다.

```python
# "나는 학교에 간다"
# "나는 학원에 간다"
# "나는 회사에 간다"

# "나는" --> torch.randn(10)
# "학교에" --> torch.randn(10)
```

### LSTM

`LSTM`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실험의 중심이 되는 모델 아키텍처를 정의하는 코드입니다.

```python
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=1, batch_first=True)

x = torch.randn(32,3,10)
out, (hidden, cell) = lstm(x)
print(out.shape, hidden.shape, cell.shape)
```

### GRU

`GRU`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실험의 중심이 되는 모델 아키텍처를 정의하는 코드입니다.

```python
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=1, batch_first=True)
x = torch.randn(32,3,10)
out, hidden = gru(x)
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
