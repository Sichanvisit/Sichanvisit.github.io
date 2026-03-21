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

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

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

### 잠재 공간 시각화 (2D) 및 테스트 데이터셋 처리 ###

`잠재 공간 시각화 (2D) 및 테스트 데이터셋 처리 ###`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 잠재 공간 시각화 (2D) 및 테스트 데이터셋 처리 ###, 테스트 데이터셋 다운로드 및 로드 (학습 데이터와는 별개), 테스트 데이터셋에 대해 인코딩 및 잠재 변수 샘플링 진행 흐름이 주석과 함께 드러납니다.

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
