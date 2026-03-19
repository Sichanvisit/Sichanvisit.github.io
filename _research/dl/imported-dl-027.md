---
title: "RNN 시계열예측 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-5_RNN_시계열예측 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-5_RNN_시계열예측 - 공유.md"
excerpt: "데이터셋 정보 - 예나 날씨 데이터 - 2009년부터 2016년까지 독일 예나 도시의 날씨 데이터를 10분 간격으로 기록"
research_summary: "데이터셋 정보 - 예나 날씨 데이터 - 2009년부터 2016년까지 독일 예나 도시의 날씨 데이터를 10분 간격으로 기록. - 14개 칼럼: 기온(°C), 기압(hPa), 습도(%), 바람 속도 등 다양한 정보 포함. 칼럼 설명 - Date Time: 기록된 시간 - T (degC): 섭씨 온도 - 기타 12개의 기상 요소 포함. `md` 원본과 18개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, pandas, matplotlib, numpy입니다."
research_artifacts: "md · 코드 18개 · 실행 16개"
code_block_count: 18
execution_block_count: 16
research_focus:
  - "데이터셋 정보 - 예나 날씨 데이터 - 2009년부터 2016년까지 독일 예나 도시의 날씨 데이터를 1..."
  - "데이터셋 소개"
  - "칼럼 설명 - Date Time"
research_stack:
  - "torch"
  - "pandas"
  - "matplotlib"
  - "numpy"
  - "sklearn"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

데이터셋 정보 - 예나 날씨 데이터 - 2009년부터 2016년까지 독일 예나 도시의 날씨 데이터를 10분 간격으로 기록. - 14개 칼럼: 기온(°C), 기압(hPa), 습도(%), 바람 속도 등 다양한 정보 포함. 칼럼 설명 - Date Time: 기록된 시간 - T (degC): 섭씨 온도 - 기타 12개의 기상 요소 포함. `md` 원본과 18개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, pandas, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: 데이터셋 정보 - 예나 날씨 데이터 - 2009년부터 2016년까지 독..., 데이터셋 소개, 칼럼 설명 - Date Time.

**남겨둔 자료**: `md` 원본과 18개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, pandas, matplotlib, numpy입니다.

**주요 스택**: `torch`, `pandas`, `matplotlib`, `numpy`, `sklearn`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 18 |
| Execution Cells | 16 |
| Libraries | `torch`, `pandas`, `matplotlib`, `numpy`, `sklearn` |
| Source Note | `4-5_RNN_시계열예측 - 공유` |

## What This Note Covers

### 데이터셋 소개

데이터셋 정보 - 예나 날씨 데이터 - 2009년부터 2016년까지 독일 예나 도시의 날씨 데이터를 10분 간격으로 기록. - 14개 칼럼: 기온(°C), 기압(hPa), 습도(%), 바람 속도 등 다양한 정보 포함.

### 데이터 불러오기

칼럼 설명 - Date Time: 기록된 시간 - T (degC): 섭씨 온도 - 기타 12개의 기상 요소 포함.

### 시각화

계절성 패턴이 뚜렷하게 나타남: - 여름: 기온 상승. - 겨울: 기온 하강. - 변동성: 짧은 시간 간격에서도 기온 변동이 관측됨.

### 데이터 처리

데이터프레임에서 기온 데이터를 numpy array 형식으로 변환

## Implementation Flow

1. 데이터셋 소개: 데이터셋 정보 - 예나 날씨 데이터 - 2009년부터 2016년까지 독일 예나 도시의 날씨 데이터를 10분 간격으로 기록. - 14개 칼럼: 기온(°C), 기압(hPa), 습도(%), 바람 속도 등 다양한 정보 포함.
2. 데이터 불러오기: 칼럼 설명 - Date Time: 기록된 시간 - T (degC): 섭씨 온도 - 기타 12개의 기상 요소 포함.
3. 시각화: 계절성 패턴이 뚜렷하게 나타남: - 여름: 기온 상승. - 겨울: 기온 하강. - 변동성: 짧은 시간 간격에서도 기온 변동이 관측됨.
4. 데이터 처리: 데이터프레임에서 기온 데이터를 numpy array 형식으로 변환

## Code Highlights

### import torch

`import torch`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
```

### 데이터 처리

`데이터 처리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Train loop 흐름이 주석과 함께 드러납니다.

```python
# @title Train loop

epochs = 5
step = 0
for epoch in range(epochs):
    model.train()
    for train_batch in train_dataloader:
        inputs = train_batch[0].to(device)
        targets = train_batch[1].to(device)
        preds = model(inputs)
        loss = loss_fn(preds, targets)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        step += 1
        if step % 100 == 0:
            print(f'step {step}, train loss: {loss.item():.4f}')

    model.eval()
    with torch.no_grad():
        losses = []
        for val_batch in val_dataloader:
            inputs = val_batch[0].to(device)
            targets = val_batch[1].to(device)
            preds = model(inputs)
            loss = loss_fn(preds, targets)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/4-5_RNN_시계열예측 - 공유.md`
- Source formats: `md`
- Companion files: `4-5_RNN_시계열예측 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `T (degC)`, `12_Deep_Learning_Code_Summary.md`
- External references: `www.kaggle.com`, `localhost`, `storage.googleapis.com`

## Note Preview

> -
> - **데이터셋 정보** - 예나 날씨 데이터 - **2009년부터 2016년까지** 독일 예나 도시의 날씨 데이터를 10분 간격으로 기록. - **14개 칼럼**: 기온(°C), 기압(hPa), 습도(%), 바람 속도 등 다양한 정보 포함.
