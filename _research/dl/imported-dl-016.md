---
title: "VGGNet"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)VGGNet"
source_path: "12_Deep_Learning/Code_Snippets/(실습)VGGNet.md"
excerpt: "데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법"
research_summary: "데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, os, torchvision입니다."
research_artifacts: "md · 코드 25개 · 실행 25개"
code_block_count: 25
execution_block_count: 25
research_focus:
  - "VGG Network"
  - "사전 훈련 모델 활용"
  - "데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행..."
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

데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 25개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchinfo, os, torchvision입니다.

**빠르게 볼 수 있는 포인트**: VGG Network, 사전 훈련 모델 활용, 데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠....

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

데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법

### Key Step

'''D'': [64, 64, ''M'', 128, 128, ''M'', 256, 256, 256, ''M'', 512, 512, 512, ''M'',

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. 실습: 데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법
2. Key Step: '''D'': [64, 64, ''M'', 128, 128, ''M'', 256, 256, 256, ''M'', 512, 512, 512, ''M'',

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

### Dataset 확인

`Dataset 확인`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 라벨이 0이면 고양이, 1이면 강아지, 데이터셋을 순회하면서 각 카테로리별로 n_samples만큼 이미지를 수집, "Cat" : [i1, i2, i3, i4, i5], "Dog" : [j1, j2, j3... 흐름이 주석과 함께 드러납니다.

```python
from collections import defaultdict

# 라벨이 0이면 고양이, 1이면 강아지
def label_to_str(label):
    return "Cat" if label == 0 else "Dog"

def visualize_by_category(dataset, n_samples=5, cmap=None):
    samples = defaultdict(list)
    # 데이터셋을 순회하면서 각 카테로리별로 n_samples만큼 이미지를 수집
    for img, label in dataset:
        if len(samples[label]) < n_samples:
            samples[label].append(img)
        if len(samples) == 2 and all(len(imgs) >= n_samples for imgs in samples.values()):
            # "Cat" : [i1, i2, i3, i4, i5], "Dog" : [j1, j2, j3, j4, j5]
            # i, j == image data
            break

    for label, imgs in samples.items():
        grid_img = torchvision.utils.make_grid(imgs, nrow=n_samples, padding=2)
        plt.figure(figsize=(n_samples*2, 4))
        plt.imshow(grid_img.permute(1,2,0).numpy(), cmap=cmap)
        plt.title(f"Category: {label_to_str(label)}")
        plt.axis('off')
        plt.show()
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
