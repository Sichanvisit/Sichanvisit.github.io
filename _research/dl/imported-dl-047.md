---
title: "Mission 9 이미지 생성"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission 9_이미지 생성"
source_path: "12_Deep_Learning/Code_Snippets/Mission 9_이미지 생성.md"
excerpt: "- 이번 미션에서는 모델을 활용하여 FashionMNIST 데이터셋의 각 패션 아이템(예: 티셔츠, 바지, 스니커즈 등)을 조건부로 생성하는 작업을 수행합니다. 각 클래스에 해당하는 이미지를 생성하는 cGAN (Conditional GAN) 모델을 직접 설계하고..."
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Mission |
| Source Files | `md` |
| Code Blocks | 20 |
| Execution Cells | 15 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy`, `random`, `google`, `os`, `scipy` |
| Source Note | `Mission 9_이미지 생성` |

## What I Worked On

- 미션 소개
- 데이터 소개
- 데이터 링크: torchvision.datasets.FashionMNIST
- 데이터 구성
- **1. Setting**

## Implementation Flow

1. 미션 소개
2. 데이터 소개
3. 데이터 링크: torchvision.datasets.FashionMNIST
4. 데이터 구성
5. **1. Setting**
6. **2. 데이터 전처리**

## Code Highlights

### **3. 모델 생성**

```python
#@title Generator Model
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        # 레이블 임베딩: num_classes (10) 개의 클래스에 대해 각각 num_classes (10) 차원의 임베딩 벡터 생성
        self.label_emb = nn.Embedding(num_classes, num_classes)

        # 초기 크기 계산: 이미지 크기 (28) 를 4로 나눈 값 (7)
        self.init_size = image_size // 4  # 28/4 = 7

        # 첫 번째 선형 레이어: 잠재 공간 차원 (100) + 레이블 임베딩 차원 (10) 을 입력으로 받아
        # 128 * init_size * init_size (128 * 7 * 7 = 6272) 차원의 출력 생성
        self.l1 = nn.Sequential(
            nn.Linear(latent_dim + num_classes, 128 * self.init_size * self.init_size),
            nn.ReLU(inplace=True)
        )

        # Conv 블록: Linear 레이어 출력 (128 * 7 * 7) 을 2D 텐서로 reshape 한 후,
        # 업샘플링 및 Conv2d 연산을 통해 이미지 생성
        self.conv_blocks = nn.Sequential(
            # BatchNorm2d: 채널 수 128에 대한 배치 정규화. momentum=0.8은 running statistics 업데이트 비율 제어.
            # GAN 학습 시 불안정성을 줄이는 데 도움을 줄 수 있음.
            nn.BatchNorm2d(128, momentum=0.8),
            # Upsample: 스케일 팩터 2로 업샘플링 (7x7 → 14x14)
            nn.Upsample(scale_factor=2),  # 7 → 14
            # Conv2d: 입력 채널 128, 출력 채널 128, 커널 크기 3, 스트라이드 1, 패딩 1
            nn.Conv2d(128, 128, kernel_size=3, stride=1, padding=1),

# ... trimmed ...
```

### 모델 학습

```python
#@title 한 에폭 학습 함수

import torch
import matplotlib.pyplot as plt

def train_one_epoch(generator, discriminator,
                    optimizer_G, optimizer_D,
                    adversarial_loss,
                    train_loader,
                    device, latent_dim, num_classes):
    """
    한 에폭 동안 Generator·Discriminator 학습하고
    평균 손실 및 판별자 출력 통계 반환
    """
    g_loss_sum = d_loss_sum = d_real_sum = d_fake_sum = 0.0
    num_batches = 0

    # 모델을 학습 모드로 설정
    generator.train()
    discriminator.train()

    # 데이터 로더에서 이미지와 레이블 가져오기
    for imgs, labels in train_loader:
        batch_size = imgs.size(0)
        imgs, labels = imgs.to(device), labels.to(device)

        # 실제 이미지(valid)와 가짜 이미지(fake)에 대한 레이블 생성
        valid = torch.ones(batch_size, 1, device=device)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/Mission 9_이미지 생성.md`
- Source formats: `md`
- Companion files: `Mission 9_이미지 생성.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - 이번 미션에서는 모델을 활용하여 FashionMNIST 데이터셋의 각 패션 아이템(예: 티셔츠, 바지, 스니커즈 등)을 조건부로 생성하는 작업을 수행합니다. 각 클래스에 해당하는 이미지를 생성하는 cGAN (Conditional GAN) 모델을 직접 설계하고 학습시켜 보세요.
> 훈련 데이터: 60,000장의 이미지 테스트 데이터: 10,000장의 이미지 28×28 크기의 흑백 이미지 (10개 클래스) 11개 클래스가 포함되어 있습니다. - T-shirt/top - Trouser - Pullover - Dress - Coat - Sandal - Shirt - Sneaker - Bag - Ankle boot
