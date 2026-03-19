---
title: "GAN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "GAN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/GAN - 공유.md"
excerpt: "DL Shared Note: MNIST"
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
| Code Blocks | 6 |
| Execution Cells | 3 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `os`, `numpy` |
| Source Note | `GAN - 공유` |

## What I Worked On

- MNIST
- MNIST 데이터셋 준비 및 DataLoader 설정
- Generator 네트워크 정의 (생성기)
- Discriminator 네트워크 정의 (판별기)
- 장치 설정 (GPU 사용 가능하면 GPU 사용)

## Implementation Flow

1. MNIST
2. MNIST 데이터셋 준비 및 DataLoader 설정
3. Generator 네트워크 정의 (생성기)
4. Discriminator 네트워크 정의 (판별기)
5. 장치 설정 (GPU 사용 가능하면 GPU 사용)
6. 생성기와 판별기 초기화

## Code Highlights

### MNIST

```python
# Generator 네트워크 정의 (생성기)
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(100, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.Linear(1024, 28*28),
            nn.Tanh()  # 출력값을 [-1, 1] 범위로 맞춤
        )

    def forward(self, z):
        return self.model(z).view(-1, 1, 28, 28)

# Discriminator 네트워크 정의 (판별기)
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(28*28, 1024),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(1024, 512),
            nn.LeakyReLU(0.2),
# ... trimmed ...
```

### MNIST

```python
# 장치 설정 (GPU 사용 가능하면 GPU 사용)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# 생성기와 판별기 초기화
generator = Generator().to(device)
discriminator = Discriminator().to(device)

# 옵티마이저 설정 (Adam 사용)
optimizer_G = optim.Adam(generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))

# 손실 함수: Binary Cross Entropy Loss 사용
criterion = nn.BCELoss()

# 에포크 수 설정
num_epochs = 100

# 평가를 위해 고정된 노이즈 벡터 생성 (이미지 생성 비교용)
fixed_noise = torch.randn(64, 100, device=device)

# 결과 저장을 위한 폴더 생성
os.makedirs('./images', exist_ok=True)
os.makedirs('./results', exist_ok=True)

# GAN 학습 루프 (에포크 단위)
for epoch in range(num_epochs):
    generator.train()
    discriminator.train()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/GAN - 공유.md`
- Source formats: `md`
- Companion files: `GAN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
