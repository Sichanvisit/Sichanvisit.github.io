---
title: "AutoEncoder samplecode"
date: 2026-03-08
research_tab: "DL"
research_kind: "Sample Code"
source_title: "AutoEncoder_samplecode"
source_path: "12_Deep_Learning/Code_Snippets/AutoEncoder_samplecode.md"
excerpt: "Encoder, Decoder, model = AE() 중심으로 구현 과정을 정리한 AutoEncoder samplecode 기록입니다"
research_summary: "Encoder, Decoder, model = AE() 중심으로 구현 과정을 정리한 AutoEncoder samplecode 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 10개 · 실행 10개"
code_block_count: 10
execution_block_count: 10
research_focus:
  - "Encoder"
  - "Decoder"
  - "model = AE()"
research_stack:
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - sample-code
---

Encoder, Decoder, model = AE() 중심으로 구현 과정을 정리한 AutoEncoder samplecode 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: Encoder, Decoder, model = AE().

**남겨둔 자료**: `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Sample Code |
| Source Files | `md` |
| Code Blocks | 10 |
| Execution Cells | 10 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy` |
| Source Note | `AutoEncoder_samplecode` |

## What This Note Covers

- Encoder
- Decoder
- model = AE()
- Training
- images_flat = images.view(images.size(0), -1)

## Implementation Flow

1. Key Step: Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)
2. Key Step: Decoder : Dense(32 -> 64), Dense(64 -> 128), Dense(128 -> 784)
3. Key Step: images_flat = images.view(images.size(0), -1)
4. Key Step: recon_images_flat, encoded = model(images.to(device))

## Code Highlights

### Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)

`Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Encoder : Dense(784 -> 128), Dense(128 -> 64), De..., Decoder : Dense(32 -> 64), Dense(64 -> 128), Dens..., Encoder 흐름이 주석과 함께 드러납니다.

```python
# Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)
# Decoder : Dense(32 -> 64), Dense(64 -> 128), Dense(128 -> 784)

class AE(nn.Module):
    def __init__(self):
        super(AE, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32)
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 784)
        )
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)

        return decoded, encoded
```

### class CNNAE(nn.Module)

`class CNNAE(nn.Module)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Encoder, Decoder 흐름이 주석과 함께 드러납니다.

```python
class CNNAE(nn.Module):
    def __init__(self):
        super(CNNAE, self).__init__()
        #Encoder
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        #Decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(32, 16, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(16, 1, kernel_size=2, stride=2),
            nn.Sigmoid()
        )
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded, encoded
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/AutoEncoder_samplecode.md`
- Source formats: `md`
- Companion files: `AutoEncoder_samplecode.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> -
