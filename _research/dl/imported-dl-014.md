---
title: "UNet"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)UNet"
source_path: "12_Deep_Learning/Code_Snippets/(실습)UNet.md"
excerpt: "UNet에서 다룬 구현 흐름과 참고 소스를 다시 볼 수 있게 정리한 DL 아카이브 노트입니다. 문제 맥락과 구현 흔적을 한 화면에서 빠르게 파악할 수 있도록 핵심 정보부터 배치했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주..."
research_summary: "UNet에서 다룬 구현 흐름과 참고 소스를 다시 볼 수 있게 정리한 DL 아카이브 노트입니다. 문제 맥락과 구현 흔적을 한 화면에서 빠르게 파악할 수 있도록 핵심 정보부터 배치했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, numpy, PIL, torch입니다."
research_artifacts: "md · 코드 11개 · 실행 8개"
code_block_count: 11
execution_block_count: 8
research_focus: []
research_stack:
  - "os"
  - "numpy"
  - "PIL"
  - "torch"
  - "torchvision"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

UNet에서 다룬 구현 흐름과 참고 소스를 다시 볼 수 있게 정리한 DL 아카이브 노트입니다. 문제 맥락과 구현 흔적을 한 화면에서 빠르게 파악할 수 있도록 핵심 정보부터 배치했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, numpy, PIL, torch입니다.

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, numpy, PIL, torch입니다.

**주요 스택**: `os`, `numpy`, `PIL`, `torch`, `torchvision`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 11 |
| Execution Cells | 8 |
| Libraries | `os`, `numpy`, `PIL`, `torch`, `torchvision`, `matplotlib`, `pdb` |
| Source Note | `(실습)UNet` |

## What This Note Covers

- 이 기록은 `DL` 트랙의 `Archive Note` 아카이브로 정리되어 있습니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. 원본 노트의 문제 정의를 먼저 확인합니다.
2. 핵심 코드 블록과 구현 단계를 따라갑니다.
3. 필요하면 이 흐름을 별도 케이스 스터디로 확장합니다.

## Code Highlights

### @title UNet 모델 정의

`@title UNet 모델 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 UNet 모델 정의 흐름이 주석과 함께 드러납니다.

```python
#@title UNet 모델 정의
class DoubleConv(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.double_conv = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, kernel_size=3, padding=1), # 원래 UNet 에서는 패딩을 추가하지 X
            nn.BatchNorm2d(out_ch),
            nn.ReLU(True),

            nn.Conv2d(out_ch, out_ch, kernel_size=3, padding=1),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(True)
        )
    def forward(self, x):
        return self.double_conv(x)

class UNet(nn.Module):
    def __init__(self, n_ch=3, n_classes=2):
        super().__init__()
        self.inc = DoubleConv(n_ch, 64)

        self.down1 = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv(64,128)
        )
        self.down2 = nn.Sequential(
            nn.MaxPool2d(2),
            DoubleConv(128,256)
# ... trimmed ...
```

### from pdb import run

`from pdb import run`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습/평가 함수 흐름이 주석과 함께 드러납니다.

```python
from pdb import run
#@title 학습/평가 함수
def train(model, dataloader, optimizer, criterion, device):
    model.train()
    running_loss = 0.0
    for imgs, masks in dataloader:
        imgs = imgs.to(device)
        masks = masks.to(device)

        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, masks)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * imgs.size(0)
    epoch_loss = running_loss / len(dataloader.dataset)
    return epoch_loss

def evaluate(model, dataloader, criterion, device):
    model.eval()
    running_loss = 0.0
    with torch.no_grad():
        for imgs, masks in dataloader:
            imgs.to(device)
            masks.to(device)
            outputs = model(imgs)
            loss = criterion(outputs, masks)
# ... trimmed ...
```

### @title 학습 루프

`@title 학습 루프`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 루프 흐름이 주석과 함께 드러납니다.

```python
#@title 학습 루프
num_epochs = 2
batch_size = 4
lr = 1e-4

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

dataset = PennFudanDataset(root="/content/data/PennFudanPed", transform=joint_transform)

train_size = int(0.8* len(dataset))
val_size = len(dataset)-train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

model = UNet(n_ch=3, n_classes=2).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

best_val_loss = float('inf')
for epoch in range(num_epochs):
    train_loss = train(model, train_dataloader, optimizer, criterion, device)
    val_loss = evaluate(model, val_dataloader, criterion, device)
    print(f"Epoch {epoch+1}/{num_epochs} , Train Loss : {train_loss:.4f}, Val Loss : {val_loss:.4f}")
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        torch.save(model.state_dict(), 'best_unet.pt')
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)UNet.md`
- Source formats: `md`
- Companion files: `(실습)UNet.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2025.10.1,2,13,14.md`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
