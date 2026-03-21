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

## Why This Matters

### RAG 검색 파이프라인

- 왜 필요한가: LLM이 외부 지식을 안정적으로 참조하게 하려면, 생성 전에 관련 문서를 정확히 찾아오는 검색 단계가 먼저 필요합니다.
- 왜 이 방식을 쓰는가: 이 방식은 모델 파라미터만 믿지 않고 최신 문서나 도메인 지식을 붙일 수 있어서 실제 서비스형 QA에 적합합니다.
- 원리: 문서를 청크로 나누고 임베딩한 뒤, 질문과 가까운 벡터를 검색해 프롬프트에 함께 넣는 구조로 동작합니다.

### 순차 데이터 모델링

- 왜 필요한가: 문장, 시계열처럼 순서가 중요한 데이터는 현재 입력만이 아니라 앞선 맥락까지 함께 봐야 합니다.
- 왜 이 방식을 쓰는가: LSTM/GRU는 기본 RNN보다 긴 문맥을 더 안정적으로 다룰 수 있어 텍스트 분류나 시계열 예측 실습에 자주 쓰입니다.
- 원리: 이전 시점의 은닉 상태를 다음 입력과 함께 업데이트하며, 게이트 구조로 필요한 정보는 남기고 불필요한 정보는 줄입니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

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

### 시각화

`시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
import matplotlib.pyplot as plt

temperatures = df['T (degC)']
temperatures.index = df['Date Time'] # 시간을 인덱스로 설정

plt.figure(figsize=(10, 5))  # 그래프 크기 조정
temperatures.plot()

plt.xticks(rotation=20)  # x축 눈금 회전 (예: 45도)
plt.xlabel("Date Time")  # x축 라벨 추가
plt.ylabel("Temperature (°C)")  # y축 라벨 추가
plt.title("Temperature Over Time")  # 제목 추가

plt.show()
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
