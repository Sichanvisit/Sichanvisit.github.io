---
title: "VAE - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "8-1_VAE - 공유"
source_path: "12_Deep_Learning/Code_Snippets/8-1_VAE - 공유.md"
excerpt: "두 정규분포 $q(z) = {N}(\\mu, \\sigma^2)$와 $p(z) = {N}(0,1)$의 KL 발산을 계산해보면:"
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
| Code Blocks | 10 |
| Execution Cells | 6 |
| Libraries | `torch`, `numpy`, `os`, `torchvision`, `matplotlib`, `random` |
| Source Note | `8-1_VAE - 공유` |

## What I Worked On

- 필요한 라이브러리 임포트
- device 설정 (GPU가 있으면 GPU 사용)
- MNIST 데이터셋 준비
- 데이터 전처리를 위해 ToTensor 변환을 적용
- 학습용 MNIST 데이터셋 다운로드 및 로드

## Implementation Flow

1. 필요한 라이브러리 임포트
2. device 설정 (GPU가 있으면 GPU 사용)
3. MNIST 데이터셋 준비
4. 데이터 전처리를 위해 ToTensor 변환을 적용
5. 학습용 MNIST 데이터셋 다운로드 및 로드
6. VAE (Variational Autoencoder) 모델 정의 ###

## Code Highlights

### VAE (Variational Autoencoder) 모델 정의 ###

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

### 잠재 공간 시각화 (2D) 및 테스트 데이터셋 처리 ###

```python
### 잠재 공간 시각화 (2D) 및 테스트 데이터셋 처리 ###
model.eval()  # 평가 모드로 전환
all_z = []    # 모든 잠재 변수 저장 리스트
all_labels = []  # 해당 이미지의 레이블 저장 리스트

# 테스트 데이터셋 다운로드 및 로드 (학습 데이터와는 별개)
with torch.no_grad():
    testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    testloader = DataLoader(testset, batch_size=64, shuffle=False)

    # 테스트 데이터셋에 대해 인코딩 및 잠재 변수 샘플링 진행
    for data, labels in testloader:
        data = data.to(device)
        mu, logvar = model.encode(data.view(-1, 28 * 28))
        z = model.reparameterize(mu, logvar)
        z = z.cpu().numpy()

        all_z.append(z)
        all_labels.append(labels)

    all_z = np.concatenate(all_z)
    all_labels = np.concatenate(all_labels)

    # 2D 잠재 공간에 대해 산점도(scatter plot) 시각화
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(all_z[:, 0], all_z[:, 1], c=all_labels, cmap='tab10', alpha=0.5, edgecolors='k', s=20)
    plt.colorbar(scatter, ticks=range(10))
    plt.xlabel('Latent Dimension 1')
# ... trimmed ...
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
