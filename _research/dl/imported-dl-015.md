---
title: "VAE"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)VAE"
source_path: "12_Deep_Learning/Code_Snippets/(실습)VAE.md"
excerpt: "VAE에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, class VAE(nn.Module), latent_dim = 2, model.eval() 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 10..."
research_summary: "VAE에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, class VAE(nn.Module), latent_dim = 2, model.eval() 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다."
research_artifacts: "md · 코드 10개 · 실행 10개"
code_block_count: 10
execution_block_count: 10
research_focus:
  - "두 정규분포 $q(z) = {N}(\\mu, \\sigma^2)$와 $p(z) = {N}(0,1)$의 KL..."
  - "VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의 합으로 구성됩니다."
  - "필요한 라이브러리 임포트"
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

VAE에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, class VAE(nn.Module), latent_dim = 2, model.eval() 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, os, torchvision입니다.

**빠르게 볼 수 있는 포인트**: 두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(..., VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의..., 필요한 라이브러리 임포트.

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

두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면 정의부터 시작합니다. 일반적인 KL 발산의 정의는 $ D_{\text{KL}}(q(z) \parallel p(z)) = \int q(z) \log \frac{q(z)}{p(z)} \, dz $ 입니다.

### Key Step

VAE의 손실 함수는 재구성 손실(BCE)과 KL 발산(KLD) 손실의 합으로 구성됩니다.

### Key Step

beta 값은 KL 손실의 가중치를 조절합니다.

### Key Step

잠재 공간을 이용한 새로운 데이터 생성

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

1. Overview: 두 정규분포 $q(z) = {N}(\mu, \sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면 정의부터 시작합니다. 일반적인 KL 발산의 정의는 $ D_{\text{KL}}(q(z) \parallel p(z)) = \int q(z) \log \frac{q...
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

### latent_dim = 2

`latent_dim = 2`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 다변량일 경우 각 차원마다 위와 같은 계산을 진행하면, 최종 식은 $ D_{\text{KL}}(q(z/x) \parallel p(z)) = \frac{1}{2} \sum_{i=1}^{d} \left( \mu_i^2 + \sigma_i^2 - 1 - \log \sigma_i^2 \right) $ 가 됩니다.

```python
latent_dim = 2
model = VAE(latent_dim=latent_dim).to(device)
optim = optim.Adam(model.parameters(), lr=1e-3)
num_epoch = 50

for epoch in range(num_epoch):
    model.train()
    train_loss = 0.
    for data, _ in trainloader :
        data = data.to(device)
        optim.zero_grad()
        recon_batch, mu, logvar = model(data)
        loss = loss_function(recon_batch, data, mu, logvar)
        loss.backward()
        optim.step()

        train_loss += loss.item()
    print(f"Epoch {epoch + 1} : Loss {train_loss / len(trainloader.dataset)}")
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

### 잠재공간 차원을 128D

`잠재공간 차원을 128D`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 잠재공간 차원을 128D 흐름이 주석과 함께 드러납니다.

```python
# 잠재공간 차원을 128D
latent_dim = 128
model = VAE(latent_dim=latent_dim).to(device)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
num_epoch = 50

print("128D 잠재공간")
for epoch in range(num_epoch):
    model.train()
    train_loss = 0.
    for data, _ in trainloader:
        data = data.to(device)
        opt.zero_grad()
        recon_batch, mu, logvar = model(data)
        loss = loss_function(recon_batch, data, mu, logvar)
        loss.backward()
        opt.step()

        train_loss += loss.item()
    print(f"Epoch {epoch+1}, loss :{train_loss / len(trainloader.dataset)}")
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
