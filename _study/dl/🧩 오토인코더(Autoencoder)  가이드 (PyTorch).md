---
title: "초보자를 위한 PyTorch 기반 오토인코더 가이드"
date: 2025-09-11
study_tab: "DL"
tags:
  - DL
  - Autoencoder
  - PyTorch
  - Unsupervised-Learning
  - Fashion-MNIST
  - Feature-Learning
excerpt: "PyTorch로 오토인코더를 구현하는 전 과정을 데이터 준비부터 학습/평가/시각화까지 단계별로 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

## 1. 오토인코더 기본 이해

오토인코더(Autoencoder)는 입력 데이터를 압축(인코더)해 잠재 공간(latent space)에 표현하고, 다시 복원(디코더)하는 비지도 학습 모델입니다.

주요 활용:
- 데이터 압축
- 노이즈 제거
- 특징 학습

## 2. PyTorch 핵심 개념 복습

- 텐서(Tensor): 모델 입력의 기본 단위
- 클래스/`self`: `torch.nn.Module` 상속 구조로 모델 정의
- GPU/CPU: `model.to(device)`, `data.to(device)`로 장치 이동

## 3. 데이터 준비 및 전처리 (Fashion MNIST)

- `torchvision.datasets.FashionMNIST`로 train/test 로드
- `transforms.Compose`로 전처리 파이프라인 구성
- `ToImage()`, `ToDtype(torch.float32, scale=True)`로 텐서화 + 스케일링
- `DataLoader`로 미니배치 학습 (`shuffle=True` 권장)

## 4. 오토인코더 모델 정의

구성:
- 인코더: 입력 이미지 -> 잠재 벡터
- 디코더: 잠재 벡터 -> 원본 크기 복원

간단한 Fashion MNIST에는 선형층 기반(DNN) 오토인코더가 적합합니다.

```python
import torch.nn as nn

class Autoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        # 인코더: 784 -> 128 -> 64 -> 3
        self.encoder = nn.Sequential(
            nn.Linear(28*28, 128), nn.ReLU(),
            nn.Linear(128, 64), nn.ReLU(),
            nn.Linear(64, 3)
        )
        # 디코더: 3 -> 64 -> 128 -> 784
        self.decoder = nn.Sequential(
            nn.Linear(3, 64), nn.ReLU(),
            nn.Linear(64, 128), nn.ReLU(),
            nn.Linear(128, 28*28), nn.Sigmoid()
        )

    def forward(self, x):
        b = x.size(0)
        x = x.view(b, -1)
        reconstructed = self.decoder(self.encoder(x))
        reconstructed = reconstructed.view(b, 1, 28, 28)
        return reconstructed
```

## 5. 모델 학습 루프 구현

- 손실 함수: `nn.MSELoss()` (입력과 복원 이미지 차이 최소화)
- 옵티마이저: `optim.Adam(...)`

```python
import torch.optim as optim

model = Autoencoder().to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(epochs):
    model.train()
    for inputs, _ in train_loader:
        inputs = inputs.to(device)
        optimizer.zero_grad()
        reconstructed = model(inputs)
        loss = criterion(reconstructed, inputs)
        loss.backward()
        optimizer.step()
    print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")
```

## 6. 모델 평가 및 시각화

- `model.eval()` + `torch.no_grad()`로 평가 모드
- 원본/복원 이미지를 `matplotlib`로 비교 시각화
- 시각화 전 `detach().cpu().numpy()` 변환
- (선택) 잠재 벡터를 2D/3D scatter로 시각화

## 7. 팁 및 고려사항

- 모델 저장: `torch.save(model.state_dict(), "model.pth")`
- 모델 로드: `model.load_state_dict(torch.load("model.pth"))`
- 디버깅: 중간 `tensor.shape`를 자주 확인
- 평가 시 반드시 `model.eval()` 사용

## 마무리

오토인코더는 딥러닝의 기본기(모델 구조, 손실 설계, 학습 루프)를 익히기에 좋은 주제입니다.  
이 구조를 이해하면 변분 오토인코더(VAE)나 이상 탐지 모델로도 확장할 수 있습니다.

