---
title: "RNN 시계열예측 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-5_RNN_시계열예측 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-5_RNN_시계열예측 - 공유.md"
excerpt: "- **데이터셋 정보** - 예나 날씨 데이터 - **2009년부터 2016년까지** 독일 예나 도시의 날씨 데이터를 10분 간격으로 기록. - **14개 칼럼**: 기온(°C), 기압(hPa), 습도(%), 바람 속도 등 다양한 정보 포함."
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
| Code Blocks | 18 |
| Execution Cells | 16 |
| Libraries | `torch`, `pandas`, `matplotlib`, `numpy`, `sklearn` |
| Source Note | `4-5_RNN_시계열예측 - 공유` |

## What I Worked On

- 데이터셋 소개
- 데이터 불러오기
- 시각화
- 시계열 데이터 준비하기
- 데이터 처리

## Implementation Flow

1. 데이터셋 소개
2. 데이터 불러오기
3. 시각화
4. 시계열 데이터 준비하기
5. 데이터 처리
6. @title to numpy

## Code Highlights

### 데이터 처리

```python
# @title 데이터셋 객체 만들기
import torch
from torch.utils.data import Dataset

class JenaTemperatureDataset(Dataset):
    def __init__(self, temperatures, sequence_length):
      self.temperatures = temperatures
      self.sequence_length = sequence_length

    def __len__(self):
      #원본 데이터 개수에서 시퀀스 길이를 뺀 만큼
      return len(self.temperatures) - self.sequence_length

    def __getitem__(self, index):
      inputs = self.temperatures[index:index+self.sequence_length]
      targets = self.temperatures[index+1:index+self.sequence_length+1]

      return torch.tensor(inputs), torch.tensor(targets)
```

### 데이터 처리

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
