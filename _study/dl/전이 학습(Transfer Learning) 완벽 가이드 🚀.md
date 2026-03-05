---
title: "전이 학습(Transfer Learning) 완벽 가이드"
date: 2025-09-30
study_tab: "DL"
tags:
  - DL
  - Transfer-Learning
  - Fine-Tuning
  - Feature-Extraction
  - PyTorch
  - Computer-Vision
excerpt: "사전학습 모델 선택부터 구조 변경, 동결 전략, 전처리, 재학습/평가까지 전이 학습의 실전 5단계 로드맵."
header:
  teaser: /assets/images/profile.png
---

딥러닝 모델을 항상 0부터 학습하는 것은 비용이 큽니다.  
전이 학습은 대규모 데이터셋으로 학습된 모델의 지식을 재사용해 적은 데이터/자원으로 빠르게 성능을 확보하는 실전 전략입니다.

## 1단계: 사전 학습된 모델 선택

새 작업(Task B)에 맞춰, 대규모 데이터(Task A)로 학습된 모델을 고릅니다.

- 대표 사전학습 데이터: ImageNet
- 대표 백본: VGG, ResNet, DenseNet, EfficientNet, MobileNet

선택 기준:
- 연산 자원(GPU/CPU)
- 속도 vs 정확도 트레이드오프
- 배포 환경(서버/모바일)

실전에서는 `torchvision.models`의 pretrained weights를 가장 많이 활용합니다.

## 2단계: 모델 로드 및 구조 변경

사전학습 가중치를 불러오고, 마지막 출력 헤드를 새 문제에 맞게 교체합니다.

```python
from torchvision import models
import torch.nn as nn

model = models.resnet18(pretrained=True)
in_features = model.fc.in_features
model.fc = nn.Linear(in_features, 10)  # 예: 10클래스
```

- 분류: 마지막 FC 교체
- 탐지/분할: task-specific head 교체

## 3단계: 가중치 동결 전략 선택

### 특징 추출 (Feature Extraction)

- 백본 freeze, 새 헤드만 학습
- 데이터가 적을 때 유리, 빠르고 안정적

```python
for p in model.parameters():
    p.requires_grad = False
for p in model.fc.parameters():
    p.requires_grad = True
```

### 미세조정 (Fine-tuning)

- 백본 일부/전체를 낮은 LR로 재학습
- 데이터가 충분하고 최대 성능이 필요할 때 유리

실전 팁:
- 헤드 LR은 크게, 백본 LR은 작게 (파라미터 그룹 분리)

## 4단계: 데이터 준비 및 전처리

사전학습 모델의 입력 규칙을 최대한 유지해야 성능이 안정적입니다.

- 입력 크기 맞춤 (예: 224x224)
- 채널 수 맞춤 (흑백 -> 3채널 확장 필요 시 처리)
- ImageNet mean/std 정규화

```python
import torchvision.transforms as T

transform = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]),
])
```

## 5단계: 재학습 및 평가

기본 학습 루프:

1. Forward  
2. Loss 계산  
3. Backward  
4. Optimizer step  
5. Zero grad

옵티마이저 예시:
- Feature Extraction: `Adam(model.fc.parameters(), lr=1e-3)`
- Fine-tuning: `Adam(model.parameters(), lr=1e-4)` (또는 백본/헤드 분리 LR)

평가 시:

```python
model.eval()
with torch.no_grad():
    # validation/test inference
    pass
```

## 마무리

전이 학습의 핵심은 다음 5단계입니다.

1. 사전학습 모델 선택
2. 구조 변경
3. freeze/fine-tune 전략 선택
4. 전처리 규칙 정합
5. 재학습 및 평가

이 흐름을 지키면 적은 데이터에서도 빠르고 강한 성능을 확보할 수 있습니다.

