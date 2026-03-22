---
title: "PyTorch DNN기초"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_DNN기초"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_DNN기초.md"
excerpt: "PyTorch DNN기초에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실제 데이터 모델링 순서로 핵심 장면을 먼저 훑고, device = torch.device..., 이진 분류, 다중 분류 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `..."
research_summary: "PyTorch DNN기초에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실제 데이터 모델링 순서로 핵심 장면을 먼저 훑고, device = torch.device..., 이진 분류, 다중 분류 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 25개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, sklearn, matplotlib, torchmetrics입니다."
research_artifacts: "md · 코드 25개 · 실행 24개"
code_block_count: 25
execution_block_count: 24
research_focus:
  - "실제 데이터 모델링"
research_stack:
  - "torch"
  - "sklearn"
  - "matplotlib"
  - "torchmetrics"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

PyTorch DNN기초에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실제 데이터 모델링 순서로 핵심 장면을 먼저 훑고, device = torch.device..., 이진 분류, 다중 분류 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 25개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, sklearn, matplotlib, torchmetrics입니다.

**빠르게 볼 수 있는 포인트**: 실제 데이터 모델링.

**남겨둔 자료**: `md` 원본과 25개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, sklearn, matplotlib, torchmetrics입니다.

**주요 스택**: `torch`, `sklearn`, `matplotlib`, `torchmetrics`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 25 |
| Execution Cells | 24 |
| Libraries | `torch`, `sklearn`, `matplotlib`, `torchmetrics` |
| Source Note | `(실습)PyTorch_DNN기초` |

## What This Note Covers

### 실제 데이터 모델링

이진 분류, 다중 분류 같은 코드를 직접 따라가며 실제 데이터 모델링 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 이진 분류, 다중 분류

#### 이진 분류

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

#### 다중 분류

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

## Implementation Flow

1. 실제 데이터 모델링: 이진 분류, 다중 분류

## Code Highlights

### device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

`device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
```

### 이진 분류

`이진 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 print(losses) 흐름이 주석과 함께 드러납니다.

```python
losses = []
for epoch in range(epochs):
    for batch in dataloader:
        batch_X, batch_y = batch[0].to(device), batch[1].to(device)
        preds = model(batch_X).squeeze()
        loss = loss_fn(preds, batch_y)
        loss.backward()
        opt.step()
        opt.zero_grad()
    losses.append(loss.item())

# print(losses)
plt.plot(range(1,epochs+1), losses)
plt.xlabel("epoch")
plt.ylabel('loss')
plt.show()
```

### 다중 분류

`다중 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습루프, 검증 흐름이 주석과 함께 드러납니다.

```python
losses=[]
val_losses=[]

# 학습루프
for epoch in range(epochs):
    model.train()
    for batch in train_dataloader:
        X, y = batch[0].to(device), batch[1].to(device)
        preds = model(X)
        loss = loss_fn(preds, y)
        loss.backward()
        opt.step()
        opt.zero_grad()
    losses.append(loss.item())

    # 검증
    model.eval()
    with torch.no_grad():
        val_loss=0
        for val_batch in val_dataloader:
            val_X, val_y = val_batch[0].to(device), val_batch[1].to(device)
            val_preds = model(val_X)
            val_loss += loss_fn(val_preds, val_y).item()
        val_losses.append(val_loss / len(val_dataloader))
        print(len(val_dataloader))
        break
```

### 다중 분류

`다중 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 및 검증 흐름이 주석과 함께 드러납니다.

```python
# 학습 및 검증
plt.plot(range(1,epochs+1), losses, label='train loss')
plt.plot(range(1,epochs+1), val_losses, label="val loss")
plt.xlabel("Epoch")
plt.ylabel('Loss')
plt.legend()
plt.show()
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)PyTorch_DNN기초.md`
- Source formats: `md`
- Companion files: `(실습)PyTorch_DNN기초.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
