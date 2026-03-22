---
title: "GAN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)GAN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)GAN.md"
excerpt: "GAN, CGAN 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 GAN, CGAN 순서로 핵심 장면을 먼저 훑고, GAN, CGAN 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 12개 코드 블록, 11개 실..."
research_summary: "GAN, CGAN 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 GAN, CGAN 순서로 핵심 장면을 먼저 훑고, GAN, CGAN 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, os입니다."
research_artifacts: "md · 코드 12개 · 실행 11개"
code_block_count: 12
execution_block_count: 11
research_focus:
  - "GAN"
  - "CGAN"
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

GAN, CGAN 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 GAN, CGAN 순서로 핵심 장면을 먼저 훑고, GAN, CGAN 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, os입니다.

**빠르게 볼 수 있는 포인트**: GAN, CGAN.

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

### GAN

GAN 코드를 직접 따라가며 GAN 흐름을 확인했습니다.

- 읽을 포인트: GAN 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### CGAN

CGAN 코드를 직접 따라가며 CGAN 흐름을 확인했습니다.

- 읽을 포인트: CGAN 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. GAN: GAN 코드를 직접 따라가며 GAN 흐름을 확인했습니다.
2. CGAN: CGAN 코드를 직접 따라가며 CGAN 흐름을 확인했습니다.

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

`CGAN`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 device 설정, 데이터셋 및 DataLoader 설정, MNIST 데이터셋 사용 흐름이 주석과 함께 드러납니다.

```python
# device 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 데이터셋 및 DataLoader 설정
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # [-1, 1] 범위로 정규화
])

# MNIST 데이터셋 사용
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset  = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader  = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)

# 클래스 이름 (MNIST는 0~9 숫자)
idx_to_class = {i: str(i) for i in range(10)}
print(idx_to_class)

image_size = 28      # MNIST 이미지 크기
num_classes = 10     # 10개 클래스 (0~9)
latent_dim = 100     # 잠재 공간 차원
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
