---
title: "RNN samplecode"
date: 2026-03-08
research_tab: "DL"
research_kind: "Sample Code"
source_title: "RNN_samplecode"
source_path: "12_Deep_Learning/Code_Snippets/RNN_samplecode.md"
excerpt: "DL Sample Code: @title 하이퍼파라미터, 사인파 코사인파 주파수를 합성, 저주파 진폭 변조"
tags:
  - research-archive
  - imported-note
  - dl
  - sample-code
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Sample Code |
| Source Files | `md` |
| Code Blocks | 14 |
| Execution Cells | 14 |
| Libraries | `torch`, `numpy`, `matplotlib` |
| Source Note | `RNN_samplecode` |

## What I Worked On

- @title 하이퍼파라미터
- 사인파 코사인파 주파수를 합성
- 저주파 진폭 변조
- 완만한 선형 추세
- 가우시안 노이즈

## Implementation Flow

1. @title 하이퍼파라미터
2. 사인파 코사인파 주파수를 합성
3. 저주파 진폭 변조
4. 완만한 선형 추세
5. 가우시안 노이즈
6. 단일 채널 (2000,1)

## Code Highlights

### @title RNN모델

```python
# @title RNN모델
class RNN(nn.Module):
    def __init__(self,input_size=1,
                 hidden_size=HIDDEN_SIZE,
                 num_layers=NUM_LAYERS,
                 output_size=1):
        super().__init__()
        self.rnn = nn.RNN(input_size=input_size,
                          hidden_size=hidden_size,
                          num_layers=num_layers,
                          batch_first=True) # (batch, seq, feat)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.rnn(x) # RNN 출력 --> (전체 output, h_n)
        out = out[:, -1, :]
        out = self.fc(out)
        return out
```

### @title LSTM모델

```python
# @title LSTM모델
class LSTM(nn.Module):
    def __init__(self,input_size=1,
                 hidden_size=HIDDEN_SIZE,
                 num_layers=NUM_LAYERS,
                 output_size=1):
        super().__init__()
        self.lstm = nn.LSTM(input_size=input_size,
                            hidden_size=hidden_size,
                            num_layers=num_layers,
                            batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.lstm(x) # LSTM 출력 --> (전체 output, h_n)
        out = out[:, -1, :]
        out = self.fc(out)
        return out
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/RNN_samplecode.md`
- Source formats: `md`
- Companion files: `RNN_samplecode.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> -
