---
title: "VAE - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "8-1_VAE - 공유"
source_path: "12_Deep_Learning/Code_Snippets/8-1_VAE - 공유.md"
excerpt: "두 정규분포 $q(z) = {N}(\\mu, \\sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면"
research_summary: "두 정규분포 $q(z) = {N}(\\mu, \\sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 10개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다."
research_artifacts: "md · 코드 10개 · 실행 6개"
code_block_count: 10
execution_block_count: 6
research_focus:
  - "참고"
  - "두 정규분포 $q(z) = {N}(\\mu, \\sigma^2)$와 $p(z) = {N}(0,1)$의 KL..."
  - "KL 발산"
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

두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 10개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다.

**빠르게 볼 수 있는 포인트**: 참고, 두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(..., KL 발산.

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

### KL 발산 : N(u, sigma^2), N(0, 1)

두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면

### Key Step

device 설정 (GPU가 있으면 GPU 사용)

### Key Step

데이터 전처리를 위해 ToTensor 변환을 적용

### Key Step

학습용 MNIST 데이터셋 다운로드 및 로드

## Implementation Flow

1. KL 발산 : N(u, sigma^2), N(0, 1): 두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면
2. Key Step: device 설정 (GPU가 있으면 GPU 사용)
3. Key Step: 데이터 전처리를 위해 ToTensor 변환을 적용
4. Key Step: 학습용 MNIST 데이터셋 다운로드 및 로드

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
