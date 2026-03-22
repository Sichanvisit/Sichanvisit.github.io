---
title: "VAE - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "8-1_VAE - 공유"
source_path: "12_Deep_Learning/Code_Snippets/8-1_VAE - 공유.md"
excerpt: "VAE - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, VAE (Variational Auto..., 손실 함수 정의 ###, 잠재 공간 차원 확장: 128D로 재학... 같은 코드로 실제 구현을 이어서 확인할..."
research_summary: "VAE - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, VAE (Variational Auto..., 손실 함수 정의 ###, 잠재 공간 차원 확장: 128D로 재학... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 10개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다."
research_artifacts: "md · 코드 10개 · 실행 6개"
code_block_count: 10
execution_block_count: 6
research_focus:
  - "VAE (Variational Autoencoder) 모델 정의 ###"
  - "모델 학습"
  - "VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의 합으로 구성됩니다."
research_stack:
  - "torch"
  - "numpy"
  - "os"
  - "torchvision"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

VAE - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, VAE (Variational Auto..., 손실 함수 정의 ###, 잠재 공간 차원 확장: 128D로 재학... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 10개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다.

**빠르게 볼 수 있는 포인트**: VAE (Variational Autoencoder) 모델 정의 ###, 모델 학습, VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의....

**남겨둔 자료**: `md` 원본과 10개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다.

**주요 스택**: `torch`, `numpy`, `os`, `torchvision`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 10 |
| Execution Cells | 6 |
| Libraries | `torch`, `numpy`, `os`, `torchvision`, `matplotlib`, `random` |
| Source Note | `8-1_VAE - 공유` |

## What This Note Covers

- VAE (Variational Autoencoder) 모델 정의 ###
- 모델 학습
- VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의 합으로 구성됩니다.
- 손실 함수 정의 ###
- 필요한 라이브러리 임포트

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

1. Key Step: device 설정 (GPU가 있으면 GPU 사용)
2. Key Step: 데이터 전처리를 위해 ToTensor 변환을 적용
3. Key Step: 학습용 MNIST 데이터셋 다운로드 및 로드
4. Key Step: VAE (Variational Autoencoder) 모델 정의 ###

## Code Highlights

### VAE (Variational Autoencoder) 모델 정의 ###

`VAE (Variational Autoencoder) 모델 정의 ###`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 VAE (Variational Autoencoder) 모델 정의 ###, 인코더 정의: 입력 이미지를 400 차원의 중간 표현으로 변환, 잠재 변수의 평균과 로그 분산을 출력하는 두 개의 Fully Connected 레이어 흐름이 주석과 함께 드러납니다.

```python
### VAE (Variational Autoencoder) 모델 정의 ###
class VAE(nn.Module):
    def __init__(self, latent_dim=2):
        """
        VAE 모델 초기화 함수.
        매개변수:
            latent_dim : 잠재 공간(latent space)의 차원 (기본값: 2)
        """
        super(VAE, self).__init__()
        # 인코더 정의: 입력 이미지를 400 차원의 중간 표현으로 변환
        self.fc1 = nn.Linear(28 * 28, 400)
        # 잠재 변수의 평균과 로그 분산을 출력하는 두 개의 Fully Connected 레이어
        self.fc21 = nn.Linear(400, latent_dim)  # 잠재 변수의 평균 (mean)
        self.fc22 = nn.Linear(400, latent_dim)  # 잠재 변수의 로그 분산 (log variance)

        # 디코더 정의: 잠재 변수에서 400 차원의 중간 표현을 복원한 후 원래 이미지 크기로 복원
        self.fc3 = nn.Linear(latent_dim, 400)
        self.fc4 = nn.Linear(400, 28 * 28)

    def encode(self, x):
        """
        인코딩 함수: 입력 x를 인코더를 통해 숨은 표현(hidden representation)으로 변환하고,
        잠재 변수의 평균과 로그 분산을 출력합니다.
        """
        h1 = F.relu(self.fc1(x))
        return self.fc21(h1), self.fc22(h1)

    def reparameterize(self, mu, logvar):
# ... trimmed ...
```

### 손실 함수 정의 ###

`손실 함수 정의 ###`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 손실 함수 정의 ###, VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의 합으로 구성됩니다., beta 값은 KL 손실의 가중치를 조절합니다. 흐름이 주석과 함께 드러납니다.

```python
### 손실 함수 정의 ###
# VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의 합으로 구성됩니다.
# beta 값은 KL 손실의 가중치를 조절합니다.
beta = 1.0
def loss_function(recon_x, x, mu, logvar):
    """
    손실 함수:
        - BCE (Binary Cross-Entropy): 입력과 재구성 이미지 간의 차이를 측정.
        - KLD (Kullback-Leibler Divergence): 잠재 공간 분포와 정규 분포 간의 차이를 측정.
    최종 손실 = BCE + beta * KLD
    """
    BCE = F.binary_cross_entropy(recon_x, x.view(-1, 28 * 28), reduction='sum')
    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())
    return BCE + beta*KLD
```

### 잠재 공간 차원 확장: 128D로 재학습 ###

`잠재 공간 차원 확장: 128D로 재학습 ###`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 잠재 공간 차원 확장: 128D로 재학습 ###, 잠재 공간의 차원을 128로 확장하여 학습하면 재구성 품질이 개선될 수 있습니다. 흐름이 주석과 함께 드러납니다.

```python
### 잠재 공간 차원 확장: 128D로 재학습 ###
# 잠재 공간의 차원을 128로 확장하여 학습하면 재구성 품질이 개선될 수 있습니다.
latent_dim = 128
model = VAE(latent_dim=latent_dim).to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-3)
num_epochs = 100

print("128D 잠재 공간으로 학습 시작...")
for epoch in range(num_epochs):
    model.train()
    train_loss = 0
    for data, _ in trainloader:
        data = data.to(device)
        optimizer.zero_grad()
        recon_batch, mu, logvar = model(data)
        loss = loss_function(recon_batch, data, mu, logvar)
        loss.backward()
        train_loss += loss.item()
        optimizer.step()
    print(f'Epoch {epoch + 1}, Loss: {train_loss / len(trainloader.dataset)}')
```

### KL 발산 : N(u, sigma^2), N(0, 1)

`KL 발산 : N(u, sigma^2), N(0, 1)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 다변량일 경우 각 차원마다 위와 같은 계산을 진행하면, 최종 식은 $ D_{\text{KL}}(q(z/x) \parallel p(z)) = \frac{1}{2} \sum_{i=1}^{d} \left( \mu_i^2 + \sigma_i^2 - 1 - \log \sigma_i^2 \right) $ 가 됩니다.

```python

```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/8-1_VAE - 공유.md`
- Source formats: `md`
- Companion files: `8-1_VAE - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `xi, yi`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> --
> 두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면:
