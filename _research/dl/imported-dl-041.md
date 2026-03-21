---
title: "cGAN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "8-3_cGAN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/8-3_cGAN - 공유.md"
excerpt: "예시를 위한 설정, 임의의 이미지 텐서 (여기서는 값은 임의로 생성), 예시 라벨 중심으로 구현 과정을 정리한 cGAN - 공유 기록입니다"
research_summary: "예시를 위한 설정, 임의의 이미지 텐서 (여기서는 값은 임의로 생성), 예시 라벨 중심으로 구현 과정을 정리한 cGAN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 5개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 5개 · 실행 3개"
code_block_count: 5
execution_block_count: 3
research_focus:
  - "예시를 위한 설정"
  - "임의의 이미지 텐서 (여기서는 값은 임의로 생성)"
  - "예시 라벨"
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
  - shared-note
---

예시를 위한 설정, 임의의 이미지 텐서 (여기서는 값은 임의로 생성), 예시 라벨 중심으로 구현 과정을 정리한 cGAN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 5개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: 예시를 위한 설정, 임의의 이미지 텐서 (여기서는 값은 임의로 생성), 예시 라벨.

**남겨둔 자료**: `md` 원본과 5개 코드 블록, 3개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 5 |
| Execution Cells | 3 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy` |
| Source Note | `8-3_cGAN - 공유` |

## What This Note Covers

- 예시를 위한 설정
- 임의의 이미지 텐서 (여기서는 값은 임의로 생성)
- 예시 라벨
- 임베딩 레이어 정의
- 예시를 위해 임베딩 가중치를 고정(쉽게 이해하기 위해)

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. Key Step: 임의의 이미지 텐서 (여기서는 값은 임의로 생성)
2. Key Step: 예시 라벨: [0, 1, 0, 0]
3. Key Step: 임베딩 레이어 정의: 각 클래스당 1차원 벡터 (실제 학습 시엔 임의의 값으로 초기화됨)
4. Key Step: 예시를 위해 임베딩 가중치를 고정(쉽게 이해하기 위해)

## Code Highlights

### @title ##### 텐서 차원 맞추기 연습 #####

`@title ##### 텐서 차원 맞추기 연습 #####`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ##### 텐서 차원 맞추기 연습 #####, 예시를 위한 설정, 임의의 이미지 텐서 (여기서는 값은 임의로 생성) 흐름이 주석과 함께 드러납니다.

```python
#@title ##### 텐서 차원 맞추기 연습 #####

import torch
import torch.nn as nn

# 예시를 위한 설정
image_size = 4   # 시각화를 위해 간단한 4x4 이미지로 가정
num_classes = 2  # 예시에서는 0과 1, 두 개의 클래스만 사용
batch_size = 5   # 배치 크기 4

# 임의의 이미지 텐서 (여기서는 값은 임의로 생성)
img = torch.randn(batch_size, 1, image_size, image_size)
# 예시 라벨: [0, 1, 0, 0]
labels = torch.tensor([0, 1, 0, 0, 1])
print("원본 라벨:", labels)  # tensor([0, 1, 0, 0, 1])

# 임베딩 레이어 정의: 각 클래스당 1차원 벡터 (실제 학습 시엔 임의의 값으로 초기화됨)
label_emb = nn.Embedding(num_classes, 1)
# 예시를 위해 임베딩 가중치를 고정(쉽게 이해하기 위해)
# 클래스 0은 값 0.5, 클래스 1은 값 -0.5라고 가정해보겠습니다.
with torch.no_grad():
    label_emb.weight[0] = torch.tensor([0.5])
    label_emb.weight[1] = torch.tensor([-0.5])

# 1. 라벨 임베딩
embedded = label_emb(labels)
print("임베딩 결과 (shape):", embedded.shape)
print("임베딩 결과 (값):", embedded)
# ... trimmed ...
```

### import torch

`import torch`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 device 설정, 데이터셋 및 DataLoader 설정, MNIST 데이터셋 사용 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

# device 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 데이터셋 및 DataLoader 설정
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # [-1, 1] 범위로 정규화
])

# MNIST 데이터셋 사용
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset  = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader  = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)

# 클래스 이름 (MNIST는 0~9 숫자)
idx_to_class = {i: str(i) for i in range(10)}
print(idx_to_class)

# ... trimmed ...
```

### generator와 discriminator 작동 확인 및 시각화 (라벨, 판별자 결과 포함)

`generator와 discriminator 작동 확인 및 시각화 (라벨, 판별자 결과 포함)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 generator와 discriminator 작동 확인 및 시각화 (라벨, 판별자 결과 포함), 사용자가 직접 입력한 라벨 (예: [0, 2, 4, 6, 8, 1, 3, 5]), 입력 라벨에 맞춰 노이즈 생성 흐름이 주석과 함께 드러납니다.

```python
# generator와 discriminator 작동 확인 및 시각화 (라벨, 판별자 결과 포함)
generator.eval()
discriminator.eval()

# 사용자가 직접 입력한 라벨 (예: [0, 2, 4, 6, 8, 1, 3, 5])
manual_labels = torch.tensor([0, 2, 4, 6, 8, 1, 3, 5], device=device)
batch_size = manual_labels.size(0)

# 입력 라벨에 맞춰 노이즈 생성
noise = torch.randn(batch_size, latent_dim, device=device)

# 생성자와 판별자 실행
with torch.no_grad():
    fake_images = generator(noise, manual_labels)
    disc_output = discriminator(fake_images, manual_labels)

print("생성된 이미지의 shape:", fake_images.shape)  # 예상: [batch_size, 1, 28, 28]
print("판별자 출력의 shape:", disc_output.shape)     # 예상: [batch_size, 1]

# 결과 시각화: 생성된 이미지와 라벨, 판별자 결과를 함께 표시
import matplotlib.pyplot as plt

fake_images_cpu = fake_images.detach().cpu().numpy()
disc_output_cpu = disc_output.detach().cpu().numpy()

fig, axs = plt.subplots(1, batch_size, figsize=(batch_size * 2, 2))
for i in range(batch_size):
    axs[i].imshow(fake_images_cpu[i, 0, :, :], cmap='gray')
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/8-3_cGAN - 공유.md`
- Source formats: `md`
- Companion files: `8-3_cGAN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> -
