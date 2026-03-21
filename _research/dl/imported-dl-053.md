---
title: "RNN samplecode"
date: 2026-03-08
research_tab: "DL"
research_kind: "Sample Code"
source_title: "RNN_samplecode"
source_path: "12_Deep_Learning/Code_Snippets/RNN_samplecode.md"
excerpt: "@title 하이퍼파라미터, 사인파 코사인파 주파수를 합성, 저주파 진폭 변조 중심으로 구현 과정을 정리한 RNN samplecode 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 14개..."
research_summary: "@title 하이퍼파라미터, 사인파 코사인파 주파수를 합성, 저주파 진폭 변조 중심으로 구현 과정을 정리한 RNN samplecode 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 14개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다."
research_artifacts: "md · 코드 14개 · 실행 14개"
code_block_count: 14
execution_block_count: 14
research_focus:
  - "@title 하이퍼파라미터"
  - "사인파 코사인파 주파수를 합성"
  - "저주파 진폭 변조"
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
  - sample-code
---

@title 하이퍼파라미터, 사인파 코사인파 주파수를 합성, 저주파 진폭 변조 중심으로 구현 과정을 정리한 RNN samplecode 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 14개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: @title 하이퍼파라미터, 사인파 코사인파 주파수를 합성, 저주파 진폭 변조.

**남겨둔 자료**: `md` 원본과 14개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, matplotlib입니다.

**주요 스택**: `torch`, `numpy`, `matplotlib`

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

## What This Note Covers

- @title 하이퍼파라미터
- 사인파 코사인파 주파수를 합성
- 저주파 진폭 변조
- 완만한 선형 추세
- 가우시안 노이즈

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. Key Step: 사인파 코사인파 주파수를 합성
2. Key Step: @title numpy --> tensor --> dataload

## Code Highlights

### @title RNN모델

`@title RNN모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 RNN모델 흐름이 주석과 함께 드러납니다.

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

`@title LSTM모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 LSTM모델 흐름이 주석과 함께 드러납니다.

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

### @title 모델 학습

`@title 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습 흐름이 주석과 함께 드러납니다.

```python
# @title 모델 학습
loss_fn = nn.MSELoss()
opt = optim.Adam(model.parameters(), lr=LR)

for epoch in range(NUM_EPOCHS):
    model.train()
    epoch_loss = 0
    for batch_X, batch_y in dataloader:
        batch_X.to(device)
        batch_y.to(device)

        opt.zero_grad()                 # 기울기를 초기화
        pred = model(batch_X)           # 모델의 예측 (순전파)
        loss = loss_fn(pred, batch_y)   # loss 계산
        loss.backward()                 # 역전파
        opt.step()                      # parameter 업데이트

        epoch_loss += loss.item() * batch_X.size(0)

    epoch_loss /= len(dataset)
    print(f"Epoch : {epoch} / loss: {epoch_loss}")
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
