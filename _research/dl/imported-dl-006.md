---
title: "GAN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)GAN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)GAN.md"
excerpt: "DL Archive Note: GAN, CGAN"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

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

## What I Worked On

- Generator
- 학습 설정
- GAN 학습 루프
- CGAN
- device 설정

## Implementation Flow

1. Generator
2. 학습 설정
3. GAN 학습 루프
4. CGAN
5. device 설정
6. 데이터셋 및 DataLoader 설정

## Code Highlights

### GAN

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

> No prose preview was available in the source note.
