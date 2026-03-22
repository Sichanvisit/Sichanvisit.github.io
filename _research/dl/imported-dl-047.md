---
title: "Mission 9 이미지 생성"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission 9_이미지 생성"
source_path: "12_Deep_Learning/Code_Snippets/Mission 9_이미지 생성.md"
excerpt: "Mission 9 이미지 생성에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 평가, 미션 소개, 데이터 소개 순서로 핵심 장면을 먼저 훑고, 데이터 전처리, 모델 생성, 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md`..."
research_summary: "Mission 9 이미지 생성에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 평가, 미션 소개, 데이터 소개 순서로 핵심 장면을 먼저 훑고, 데이터 전처리, 모델 생성, 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 20개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 20개 · 실행 15개"
code_block_count: 20
execution_block_count: 15
research_focus:
  - "모델 평가"
  - "미션 소개"
  - "데이터 소개"
research_stack:
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "numpy"
  - "random"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

Mission 9 이미지 생성에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 모델 평가, 미션 소개, 데이터 소개 순서로 핵심 장면을 먼저 훑고, 데이터 전처리, 모델 생성, 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 20개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: 모델 평가, 미션 소개, 데이터 소개.

**남겨둔 자료**: `md` 원본과 20개 코드 블록, 15개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `numpy`, `random`

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

## What This Note Covers

### 모델 평가

Fréchet Inception Distance 생성 분포와 실제 데이터 분포간의 거리 측정 - 거리가 가까울수록 (FID 값이 작을 수록) 실제 분포와 유사한 데이터가 생성

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### 미션 소개

이번 미션에서는 모델을 활용하여 FashionMNIST 데이터셋의 각 패션 아이템(예: 티셔츠, 바지, 스니커즈 등)을 조건부로 생성하는 작업을 수행합니다. 각 클래스에 해당하는 이미지를 생성하는 cGAN (Conditional GAN) 모델을 직접 설계하고 학습시켜 보세요.

- 읽을 포인트: 미션 소개에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### 데이터 소개

데이터 링크: torchvision..., 데이터 구성 같은 코드를 직접 따라가며 데이터 소개 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 데이터 링크: torchvision.datasets.FashionMNIST, 데이터 구성

#### 데이터 링크: torchvision.datasets.FashionMNIST

이미지 입력을 배치로 묶고 증강하며 학습 가능한 형태로 만드는 구간입니다.

#### 데이터 구성

훈련 데이터: 60,000장의 이미지 테스트 데이터: 10,000장의 이미지 28×28 크기의 흑백 이미지 (10개 클래스) 11개 클래스가 포함되어 있습니다. - T-shirt/top - Trouser - Pullover - Dress - Coat - Sandal - Shirt...

### Setting

Setting 코드를 직접 따라가며 Setting 흐름을 확인했습니다.

- 읽을 포인트: Setting 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 데이터 전처리

데이터 전처리 코드를 직접 따라가며 데이터 전처리 흐름을 확인했습니다.

- 읽을 포인트: 이미지 입력을 배치로 묶고 증강하며 학습 가능한 형태로 만드는 구간입니다.

### 모델 생성

모델 학습 같은 코드를 직접 따라가며 모델 생성 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 모델 학습

#### 모델 학습

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

1. 모델 평가: Fréchet Inception Distance 생성 분포와 실제 데이터 분포간의 거리 측정 - 거리가 가까울수록 (FID 값이 작을 수록) 실제 분포와 유사한 데이터가 생성
2. 미션 소개: 이번 미션에서는 모델을 활용하여 FashionMNIST 데이터셋의 각 패션 아이템(예: 티셔츠, 바지, 스니커즈 등)을 조건부로 생성하는 작업을 수행합니다. 각 클래스에 해당하는 이미지를 생성하는 cGAN (Conditional GAN) 모델을 직접...
3. 데이터 소개: 데이터 링크: torchvision.datasets.FashionMNIST, 데이터 구성
4. Setting: Setting 코드를 직접 따라가며 Setting 흐름을 확인했습니다.
5. 데이터 전처리: 데이터 전처리 코드를 직접 따라가며 데이터 전처리 흐름을 확인했습니다.
6. 모델 생성: 모델 학습

## Code Highlights

### 데이터 전처리

`데이터 전처리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 하이퍼파라미터 및 환경 설정 흐름이 주석과 함께 드러납니다.

```python
#@title 하이퍼파라미터 및 환경 설정

image_size = 28      # Fashion MNIST 이미지 크기
num_classes = 10     # 10개 클래스
latent_dim = 100     # 잠재 공간 차원
batch_size = 64      # 학습 배치 크기
num_epochs = 200     # 전체 학습 에폭 수
lr = 0.0002          # 학습률 (Learning Rate): GAN 학습 안정화를 위해 일반적으로 낮은 값 사용
beta1 = 0.5          # Adam optimizer beta1: DCGAN 논문에서 제안된 값으로 GAN 학습 안정화에 도움
beta2 = 0.999        # Adam optimizer beta2: Adam optimizer의 기본값
```

### 모델 생성

`모델 생성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Generator Model, 레이블 임베딩: num_classes (10) 개의 클래스에 대해 각각 num_class..., 초기 크기 계산: 이미지 크기 (28) 를 4로 나눈 값 (7) 흐름이 주석과 함께 드러납니다.

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

`모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 한 에폭 학습 함수, 모델을 학습 모드로 설정, 데이터 로더에서 이미지와 레이블 가져오기 흐름이 주석과 함께 드러납니다.

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

### 모델 평가

`모델 평가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 평가지표 확인, 학습 종료 후 평가 (예: 1000개 샘플 사용), 생성 이미지 준비 흐름이 주석과 함께 드러납니다.

```python
#@title 평가지표 확인

# 학습 종료 후 평가 (예: 1000개 샘플 사용)
n_eval = 1000

# 생성 이미지 준비
z = torch.randn(n_eval, latent_dim, device=device) # 평가에 사용할 노이즈 벡터 생성
eval_labels = torch.randint(0, num_classes, (n_eval,), device=device) # 평가에 사용할 랜덤 레이블 생성
gen_imgs = generator(z, eval_labels) # 생성자에 노이즈와 레이블을 입력하여 이미지 생성
gen_imgs = (gen_imgs + 1) / 2.0  # [-1,1] -> [0,1] 범위로 스케일링

# 실제 이미지 준비 (test dataset에서 n_eval개 샘플)
real_imgs_list = []
for imgs, _ in test_loader:
    real_imgs_list.append(imgs)
    if len(real_imgs_list) * imgs.size(0) >= n_eval:
        break
real_imgs = torch.cat(real_imgs_list, 0)[:n_eval].to(device) # 테스트 데이터셋에서 실제 이미지 샘플링
real_imgs = (real_imgs + 1) / 2.0  # [-1,1] -> [0,1] 범위로 스케일링

# FID 계산
fid_score = calculate_fid(real_imgs, gen_imgs, inception_model_fid, batch_size=32, device=device)
# Inception Score 계산
inception_score, inception_std = calculate_inception_score(gen_imgs, inception_model_is, batch_size=32, splits=10, device=device)

print(f"FID score: {fid_score:.4f}")
print(f"Inception Score: Mean = {inception_score:.4f}, Std = {inception_std:.4f}")
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
