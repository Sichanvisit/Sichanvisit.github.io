---
title: "VAE"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)VAE"
source_path: "12_Deep_Learning/Code_Snippets/(실습)VAE.md"
excerpt: "두 정규분포 $q(z) = {N}(\\mu, \\sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면"
research_summary: "두 정규분포 $q(z) = {N}(\\mu, \\sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다."
research_artifacts: "md · 코드 10개 · 실행 10개"
code_block_count: 10
execution_block_count: 10
research_focus:
  - "두 정규분포 $q(z) = {N}(\\mu, \\sigma^2)$와 $p(z) = {N}(0,1)$의 KL..."
  - "필요한 라이브러리 임포트"
  - "손실 함수 정의 ###"
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
  - archive-note
---

두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다.

**빠르게 볼 수 있는 포인트**: 두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(..., 필요한 라이브러리 임포트, 손실 함수 정의 ###.

**남겨둔 자료**: `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다.

**주요 스택**: `torch`, `numpy`, `os`, `torchvision`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 10 |
| Execution Cells | 10 |
| Libraries | `torch`, `numpy`, `os`, `torchvision`, `matplotlib`, `random` |
| Source Note | `(실습)VAE` |

## What This Note Covers

### Overview

두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면

### Key Step

VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의 합으로 구성됩니다.

### Key Step

beta 값은 KL 손실의 가중치를 조절합니다.

### Key Step

잠재 공간을 이용한 새로운 데이터 생성

## Implementation Flow

1. Overview: 두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면
2. Key Step: VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의 합으로 구성됩니다.
3. Key Step: beta 값은 KL 손실의 가중치를 조절합니다.
4. Key Step: 잠재 공간을 이용한 새로운 데이터 생성

## Code Highlights

### class VAE(nn.Module)

`class VAE(nn.Module)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 인코더 정의 --> 입력을 400 차원으로, 잠재변수의 평균, log분산, 디코더 흐름이 주석과 함께 드러납니다.

```python
class VAE(nn.Module):
    def __init__(self, latent_dim=2):
        super().__init__()

        #인코더 정의 --> 입력을 400 차원으로
        self.fc1 = nn.Linear(28*28, 400)

        #잠재변수의 평균, log분산
        self.fc21 = nn.Linear(400, latent_dim) # 평균
        self.fc22 = nn.Linear(400, latent_dim) # log 분산

        # 디코더
        self.fc3 = nn.Linear(latent_dim, 400)
        self.fc4 = nn.Linear(400, 28*28)

    def encode(self, x):
        h1 = F.relu(self.fc1(x))
        return self.fc21(h1), self.fc22(h1)

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar) # 표준편차 계산 logvar는 log(sigma^2) -->  std = exp((1/2) * log(sigma^2)) = sigma
        eps = torch.randn_like(std)
        return mu + eps * std

    def decode(self, z):
        h3 = F.relu(self.fc3(z))
        return torch.sigmoid(self.fc4(h3))

# ... trimmed ...
```

### model.eval()

`model.eval()`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 다변량일 경우 각 차원마다 위와 같은 계산을 진행하면, 최종 식은 $ D_{\text{KL}}(q(z/x) \parallel p(z)) = \frac{1}{2} \sum_{i=1}^{d} \left( \mu_i^2 + \sigma_i^2 - 1 - \log \sigma_i^2 \right) $ 가 됩니다.

```python
model.eval()
all_z = []
all_labels = []

with torch.no_grad():
    testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    testloader = DataLoader(testset, batch_size=64, shuffle=False)

    for data, labels in testloader:
        data = data.to(device)
        mu, logvar =  model.encode(data.view(-1, 28*28))
        z = model.reparameterize(mu, logvar)
        z = z.cpu().numpy()

        all_z.append(z)
        all_labels.append(labels)
    all_z = np.concatenate(all_z)
    all_labels = np.concatenate(all_labels)

    plt.figure(figsize=(10,8))
    scatter = plt.scatter(all_z[:, 0], all_z[:, 1], c=all_labels, cmap='tab10', alpha=0.5, edgecolors='k', s=20)
    plt.colorbar(scatter, ticks=range(10))
    plt.xlabel('Latent Dimension 1')
    plt.ylabel('Latent Dimension 2')
    plt.title('Latent Space Visualization (2D)')
    plt.grid(True)
    plt.show()
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)VAE.md`
- Source formats: `md`
- Companion files: `(실습)VAE.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `xi, yi`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면:
> 1. **정의부터 시작합니다.** 일반적인 KL 발산의 정의는 $ D_{\text{KL}}(q(z) \parallel p(z)) = \int q(z) \log \frac{q(z)}{p(z)} \, dz $ 입니다.
