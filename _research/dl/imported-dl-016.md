---
title: "VGGNet"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)VGGNet"
source_path: "12_Deep_Learning/Code_Snippets/(실습)VGGNet.md"
excerpt: "실습, VGG Network 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실습, VGG Network, 사전 훈련 모델 활용 순서로 핵심 장면을 먼저 훑고, VGG Network, 사전 훈련 모델 활용, Dataset 확인 같은..."
research_summary: "실습, VGG Network 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실습, VGG Network, 사전 훈련 모델 활용 순서로 핵심 장면을 먼저 훑고, VGG Network, 사전 훈련 모델 활용, Dataset 확인 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, os, torchvision입니다."
research_artifacts: "md · 코드 25개 · 실행 25개"
code_block_count: 25
execution_block_count: 25
research_focus:
  - "실습"
  - "VGG Network"
  - "사전 훈련 모델 활용"
research_stack:
  - "torch"
  - "torchinfo"
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

실습, VGG Network 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실습, VGG Network, 사전 훈련 모델 활용 순서로 핵심 장면을 먼저 훑고, VGG Network, 사전 훈련 모델 활용, Dataset 확인 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, os, torchvision입니다.

**빠르게 볼 수 있는 포인트**: 실습, VGG Network, 사전 훈련 모델 활용.

**남겨둔 자료**: `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, os, torchvision입니다.

**주요 스택**: `torch`, `torchinfo`, `os`, `torchvision`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 25 |
| Execution Cells | 25 |
| Libraries | `torch`, `torchinfo`, `os`, `torchvision`, `matplotlib`, `tqdm`, `collections`, `random` |
| Source Note | `(실습)VGGNet` |

## What This Note Covers

### 실습

데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법 입력 이미지 크기를 224로 바로 리사이즈 할 수도 있지만, 그러면 검출하려는 객체의 크기가 더 작아질 수 있음

- 읽을 포인트: 세부 흐름: Dataset 확인, 모델 활용

#### Dataset 확인

이미지 입력을 배치로 묶고 증강하며 학습 가능한 형태로 만드는 구간입니다.

#### 모델 활용

모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### VGG Network

VGG Network 코드를 직접 따라가며 VGG Network 흐름을 확인했습니다.

- 읽을 포인트: VGG Network 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 사전 훈련 모델 활용

사전 훈련 모델 활용 코드를 직접 따라가며 사전 훈련 모델 활용 흐름을 확인했습니다.

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. 실습: Dataset 확인, 모델 활용
2. VGG Network: VGG Network 코드를 직접 따라가며 VGG Network 흐름을 확인했습니다.
3. 사전 훈련 모델 활용: 사전 훈련 모델 활용 코드를 직접 따라가며 사전 훈련 모델 활용 흐름을 확인했습니다.

## Code Highlights

### VGG Network

`VGG Network`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 'A': [64, 'M', 128, 'M', 256, 256, 'M', 512, 512,... 흐름이 주석과 함께 드러납니다.

```python
class VGG(nn.Module):
    def __init__(self, cfg, batch_norm, num_classes=1000, init_weights=True):
        super().__init__()
        self.features = self.make_layers(cfg, batch_norm)
        self.avgpool = nn.AdaptiveAvgPool2d((7,7))
        self.classifier = nn.Sequential(
            nn.Linear(512*7*7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, num_classes)
        )
        if init_weights:
            self._initialize_weigths()

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x,1)
        x = self.classifier(x)
        return x

    def _initialize_weigths(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
# ... trimmed ...
```

### 사전 훈련 모델 활용

`사전 훈련 모델 활용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델, 'D': [64, 64, 'M', 128, 128, 'M', 256, 256, 256,..., model = torchvision.models.vgg16_bn(pretrained =... 흐름이 주석과 함께 드러납니다.

```python
# 모델
# 'D': [64, 64, 'M', 128, 128, 'M', 256, 256, 256, 'M', 512, 512, 512, 'M', 512, 512, 512, 'M'],
# model = torchvision.models.vgg16_bn(pretrained = True)
model = torchvision.models.vgg16_bn(weights="VGG16_BN_Weights.IMAGENET1K_V1")
summary(model, input_size = (2,3,224,224), device='cpu')
```

### Dataset 확인

`Dataset 확인`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 OxfordIIITPet 데이터셋 로드 흐름이 주석과 함께 드러납니다.

```python
#OxfordIIITPet 데이터셋 로드
dataset = torchvision.datasets.OxfordIIITPet(
    root='data',
    download=True,
    target_types="binary-category", # 0:Cat, 1:Dog
    split='trainval',
    transform=transforms.Compose([
        transforms.Resize((256,256)),
        transforms.ToTensor()
    ])
)
```

### 모델 활용

`모델 활용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 train, val 흐름이 주석과 함께 드러납니다.

```python
train_acc_hist, val_acc_hist = [], []
EPOCHS = 10
for epoch in range(EPOCHS):
    # train
    model.train()
    corr = 0
    tot = 0  # correct =0, total =0
    for x,y in tqdm(train_loader, desc=f"E{epoch+1}/{EPOCHS}"):
        x,y = x.to(device), y.to(device)
        opt.zero_grad()
        out = model(x)
        loss = loss_fn(out, y)
        loss.backward()
        opt.step()

        corr += (out.argmax(1) == y).sum().item()
        tot += y.size(0)
    train_acc_hist.append(corr/tot)

    #val
    model.eval()
    corr = 0
    tot = 0
    with torch.no_grad():
        for x, y in val_loader:
            x,y = x.to(device), y.to(device)
            out = model(x)
            corr += (out.argmax(1)==y).sum().item()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)VGGNet.md`
- Source formats: `md`
- Companion files: `(실습)VGGNet.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법
> - 입력 이미지 크기를 224로 바로 리사이즈 할 수도 있지만, 그러면 검출하려는 객체의 크기가 더 작아질 수 있음
