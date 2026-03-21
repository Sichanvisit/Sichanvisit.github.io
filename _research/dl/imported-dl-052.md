---
title: "MNIST samplecode"
date: 2026-03-08
research_tab: "DL"
research_kind: "Sample Code"
source_title: "MNIST_samplecode"
source_path: "12_Deep_Learning/Code_Snippets/MNIST_samplecode.md"
excerpt: "데이터 로더, model = MLP(input_size, h..., input_ch, hidden_size, nu... 중심으로 구현 과정을 정리한 MNIST samplecode 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수..."
research_summary: "데이터 로더, model = MLP(input_size, h..., input_ch, hidden_size, nu... 중심으로 구현 과정을 정리한 MNIST samplecode 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 11개 · 실행 11개"
code_block_count: 11
execution_block_count: 11
research_focus:
  - "데이터 로더"
  - "model = MLP(input_size, hidden_size, num_cls).to(..."
  - "input_ch, hidden_size, num_cls"
research_stack:
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - sample-code
---

데이터 로더, model = MLP(input_size, h..., input_ch, hidden_size, nu... 중심으로 구현 과정을 정리한 MNIST samplecode 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: 데이터 로더, model = MLP(input_size, hidden_size, nu..., input_ch, hidden_size, num_cls.

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Sample Code |
| Source Files | `md` |
| Code Blocks | 11 |
| Execution Cells | 11 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy` |
| Source Note | `MNIST_samplecode` |

## What This Note Covers

- 데이터 로더
- model = MLP(input_size, hidden_size, num_cls).to(...
- input_ch, hidden_size, num_cls
- 테스트 셋에서 20개 샘플 추출
- 모델 예측

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

1. Key Step: model = MLP(input_size, hidden_size, num_cls).to(device)
2. Key Step: input_ch, hidden_size, num_cls
3. Key Step: 테스트 셋에서 20개 샘플 추출

## Code Highlights

### class CNN(nn.Module)

`class CNN(nn.Module)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실험의 중심이 되는 모델 아키텍처를 정의하는 코드입니다.

```python
class CNN(nn.Module):
    def __init__(self, input_ch, hidden_size, num_cls):
        super(CNN, self).__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(input_ch, hidden_size, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(hidden_size, hidden_size, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.block3 = nn.Sequential(
            nn.Conv2d(hidden_size, input_ch, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.flatten = nn.Flatten()
        self.output = nn.Linear(784, num_cls)

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)

        x = self.flatten(x)
        out = self.output(x)

        return out
```

### input_size = 784

`input_size = 784`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 model = MLP(input_size, hidden_size, num_cls).to(..., input_ch, hidden_size, num_cls, 데이터를 디바이스로 이동 흐름이 주석과 함께 드러납니다.

```python
input_size = 784
hidden_size = 500
num_cls = 10
epochs = 3

# model = MLP(input_size, hidden_size, num_cls).to(device)

# input_ch, hidden_size, num_cls
model = CNN(1, 16, 10).to(device)

loss_fn = nn.CrossEntropyLoss()
optim = opt.Adam(model.parameters(), lr=0.001)

for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
        # 데이터를 디바이스로 이동
        # images = images.reshape(-1,input_size)
        images = images.to(device)
        labels = labels.to(device)

        # 모델을 실행
        outputs = model(images).squeeze()
        loss = loss_fn(outputs,labels)

        # 역전파 & 옵티마이저
        optim.zero_grad()
        loss.backward()
        optim.step()
# ... trimmed ...
```

### import matplotlib.pyplot as plt

`import matplotlib.pyplot as plt`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 테스트 셋에서 20개 샘플 추출, 모델 예측, image = image.reshape(-1, input_size).to(device) 흐름이 주석과 함께 드러납니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 테스트 셋에서 20개 샘플 추출
sample_indices = np.random.choice(len(test_dataset), 20, replace=False)
sampled_images = [test_dataset[i][0] for i in sample_indices]
sampled_labels = [test_dataset[i][1] for i in sample_indices]

# 모델 예측
model.eval()  # 평가 모드로 설정
predicted_labels = []
with torch.no_grad():
  for image in sampled_images:
    # image = image.reshape(-1, input_size).to(device)
    image = image.to(device)
    output = model(image).argmax()
    predicted_labels.append(output.item())

# 결과 시각화
fig, axes = plt.subplots(4, 5, figsize=(10, 8))
for i, ax in enumerate(axes.flatten()):
  ax.imshow(sampled_images[i].squeeze().numpy(), cmap='gray')
  ax.set_title(f'True: {sampled_labels[i]}\nPred: {predicted_labels[i]}',
               color='green' if sampled_labels[i] == predicted_labels[i] else 'red')
  ax.axis('off')
plt.tight_layout()
plt.show()
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/MNIST_samplecode.md`
- Source formats: `md`
- Companion files: `MNIST_samplecode.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> -
