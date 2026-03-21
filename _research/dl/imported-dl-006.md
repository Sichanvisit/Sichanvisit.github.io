---
title: "GAN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)GAN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)GAN.md"
excerpt: "CGAN, Generator, 학습 설정 중심으로 구현 과정을 정리한 GAN 기록입니다"
research_summary: "CGAN, Generator, 학습 설정 중심으로 구현 과정을 정리한 GAN 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, os입니다."
research_artifacts: "md · 코드 12개 · 실행 11개"
code_block_count: 12
execution_block_count: 11
research_focus:
  - "CGAN"
  - "Generator"
  - "학습 설정"
research_stack:
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "os"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

CGAN, Generator, 학습 설정 중심으로 구현 과정을 정리한 GAN 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, os입니다.

**빠르게 볼 수 있는 포인트**: CGAN, Generator, 학습 설정.

**남겨둔 자료**: `md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, os입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `os`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 12 |
| Execution Cells | 11 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `os`, `numpy`, `logging` |
| Source Note | `(실습)GAN` |

## What This Note Covers

- CGAN
- Generator
- 학습 설정
- GAN 학습 루프
- device 설정

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. Key Step: 데이터셋 및 DataLoader 설정
2. Key Step: 클래스 이름 (MNIST는 0~9 숫자)
3. Key Step: 판별자 (Discriminator)
4. Key Step: 학습 루프 (에포크마다 D(x)와 D(G(z)) 평균 점수 계산)

## Code Highlights

### GAN

`GAN`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 GAN 학습 루프, 판별기 학습, 생성기 학습 흐름이 주석과 함께 드러납니다.

```python
# GAN 학습 루프
for epoch in range(num_epoch):
    generator.train()
    discriminator.train()

    total_d_loss = 0.0
    total_g_loss = 0.0
    total_real_score = 0.0
    total_fake_score = 0.0
    num_batches = 0

    for real_images, _ in dataloader:
        num_batches += 1
        batch_size = real_images.size(0)
        real_labels = torch.ones(batch_size, 1).to(device)
        fake_labels = torch.zeros(batch_size, 1).to(device)

        #판별기 학습
        discriminator.zero_grad()
        outputs_real = discriminator(real_images.to(device))
        d_loss_real = criterion(outputs_real, real_labels) # 진짜 이미지와 1을 비교
        real_score = outputs_real.mean().item()

        noise = torch.randn(batch_size, 100, device=device)
        fake_images = generator(noise)
        outputs_fake = discriminator(fake_images.detach())
        d_loss_fake = criterion(outputs_fake, fake_labels) # 가짜 이미지와 0을 비교
        fake_score = outputs_fake.mean().item()
# ... trimmed ...
```

### CGAN

`CGAN`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 생성자, 레이블 임베딩 흐름이 주석과 함께 드러납니다.

```python
#생성자
class cGenerator(nn.Module):
    def __init__(self):
        super().__init__()

        #레이블 임베딩
        self.label_emb = nn.Embedding(num_classes, num_classes) # 10*10 like one-hot

        self.init_size = image_size // 4 #7

        self.l1=nn.Sequential(
            nn.Linear(latent_dim + num_classes, 128*self.init_size*self.init_size),
            nn.ReLU(True)
        )

        self.conv_blocks = nn.Sequential(
            nn.BatchNorm2d(128),
            nn.Upsample(scale_factor=2), # 7 --> 14
            nn.Conv2d(128, 64, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(64, 0.8),
            nn.ReLU(True),
            nn.Upsample(scale_factor=2), # 14 -->28
            nn.Conv2d(64, 1, kernel_size=3, stride=1, padding=1),
            nn.Tanh()
        )

    def forward(self, noise, labels):
        label_input = self.label_emb(labels)
# ... trimmed ...
```

### CGAN

`CGAN`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 초기화, 학습 루프 (에포크마다 D(x)와 D(G(z)) 평균 점수 계산), 판별자 학습 흐름이 주석과 함께 드러납니다.

```python
# 모델 초기화
generator = Generator().to(device)
discriminator = Discriminator().to(device)

epochs = 30
criterion = nn.BCELoss()
optimizer_G = optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

# 학습 루프 (에포크마다 D(x)와 D(G(z)) 평균 점수 계산)
for epoch in range(epochs):
    running_d_loss = 0.0
    running_g_loss = 0.0
    d_x_total = 0.0
    d_gz_total = 0.0
    total_samples = 0

    for i, (imgs, labels) in enumerate(train_loader):
        batch_size_current = imgs.size(0)
        total_samples += batch_size_current
        imgs = imgs.to(device)
        labels = labels.to(device)

        valid = torch.ones(batch_size_current, 1, device=device)
        fake  = torch.zeros(batch_size_current, 1, device=device)

        # 판별자 학습
        optimizer_D.zero_grad()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)GAN.md`
- Source formats: `md`
- Companion files: `(실습)GAN.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
