---
title: "AutoEncoder"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)AutoEncoder"
source_path: "12_Deep_Learning/Code_Snippets/(실습)AutoEncoder.md"
excerpt: "오토인코더 구현 (MNIST), 기본 전처리 + 데이터 로드, 모델 생성 및 학습 중심으로 구현 과정을 정리한 AutoEncoder 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 22개 코..."
research_summary: "오토인코더 구현 (MNIST), 기본 전처리 + 데이터 로드, 모델 생성 및 학습 중심으로 구현 과정을 정리한 AutoEncoder 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 22개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, torch, torchvision입니다."
research_artifacts: "md · 코드 22개 · 실행 21개"
code_block_count: 22
execution_block_count: 21
research_focus:
  - "오토인코더 구현 (MNIST)"
  - "기본 전처리 + 데이터 로드"
  - "모델 생성 및 학습"
research_stack:
  - "numpy"
  - "matplotlib"
  - "torch"
  - "torchvision"
  - "plotly"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

오토인코더 구현 (MNIST), 기본 전처리 + 데이터 로드, 모델 생성 및 학습 중심으로 구현 과정을 정리한 AutoEncoder 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 22개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, torch, torchvision입니다.

**빠르게 볼 수 있는 포인트**: 오토인코더 구현 (MNIST), 기본 전처리 + 데이터 로드, 모델 생성 및 학습.

**남겨둔 자료**: `md` 원본과 22개 코드 블록, 21개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, torch, torchvision입니다.

**주요 스택**: `numpy`, `matplotlib`, `torch`, `torchvision`, `plotly`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 22 |
| Execution Cells | 21 |
| Libraries | `numpy`, `matplotlib`, `torch`, `torchvision`, `plotly` |
| Source Note | `(실습)AutoEncoder` |

## What This Note Covers

- 오토인코더 구현 (MNIST)
- 기본 전처리 + 데이터 로드
- 모델 생성 및 학습
- 모델 생성
- Basic Auto Encoder

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. Key Step: 오토인코더 구현 (MNIST)
2. Key Step: latent 공간 시각화를 위한 데이터 추출
3. Key Step: 전체 latent 벡터를 scatter plot
4. Key Step: 각 digit별로 일부 포인트에 텍스트 어노테이션 추가

## Code Highlights

### Basic Auto Encoder

`Basic Auto Encoder`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 BasicAutoEncoder, train 흐름이 주석과 함께 드러납니다.

```python
# BasicAutoEncoder
# train
epochs = 10
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for batch in train_loader:
        images = batch[0].to(device)
        images = images.view(images.size(0), -1)
        outputs = model(images)
        loss = loss_fn(outputs, images)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        total_loss += loss.item()
    print(f"Epoch : {epoch+1}/{epochs}, Loss : {total_loss/len(train_loader):.4f}")
```

### 3D view

`3D view`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 BasicAutoEncoder 2 흐름이 주석과 함께 드러납니다.

```python
# BasicAutoEncoder 2
class BasicAutoEncoder2(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(28*28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 3),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(3, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 28*28),
            nn.Sigmoid()
        )
    def forward(self, x):
        latent = self.encoder(x)
        x = self.decoder(latent)
        return x
```

### CNN Auto Encoder

`CNN Auto Encoder`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습, 학습 루프 흐름이 주석과 함께 드러납니다.

```python
# 모델 학습
model = CNNAutoEncoder().to(device)
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 학습 루프
epochs = 10
num_ch = 5

plt.figure(figsize=(20,10))

for epoch in range(epochs):
    model.train()
    running_loss = 0.
    for data in train_loader:
        inputs = data[0].to(device)
        outputs, encoded = model(inputs)

        loss = loss_fn(outputs,inputs)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        running_loss += loss.item()

    for c in range(num_ch):
        ax = plt.subplot(num_ch, epochs, epoch + c * epochs+1)
        encoded_img_channel = encoded[epoch, c, :,:].detach().cpu().numpy()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)AutoEncoder.md`
- Source formats: `md`
- Companion files: `(실습)AutoEncoder.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2025.10.1,2,13,14.md`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
