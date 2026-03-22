---
title: "CAM and Grad-CAM - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-7_CAM_and_Grad-CAM - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-7_CAM_and_Grad-CAM - 공유.md"
excerpt: "CAM and Grad-CAM - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 CAM(Class Activatio..., Grad-CAM 순서로 핵심 장면을 먼저 훑고, CAM(Class Activation..., Hook이란? 같은 코드로..."
research_summary: "CAM and Grad-CAM - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 CAM(Class Activatio..., Grad-CAM 순서로 핵심 장면을 먼저 훑고, CAM(Class Activation..., Hook이란? 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, PIL, requests입니다."
research_artifacts: "md · 코드 11개 · 실행 8개"
code_block_count: 11
execution_block_count: 8
research_focus:
  - "CAM(Class Activation Map)"
  - "Grad-CAM"
research_stack:
  - "torch"
  - "torchvision"
  - "PIL"
  - "requests"
  - "io"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

CAM and Grad-CAM - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 CAM(Class Activatio..., Grad-CAM 순서로 핵심 장면을 먼저 훑고, CAM(Class Activation..., Hook이란? 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, PIL, requests입니다.

**빠르게 볼 수 있는 포인트**: CAM(Class Activation Map), Grad-CAM.

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, PIL, requests입니다.

**주요 스택**: `torch`, `torchvision`, `PIL`, `requests`, `io`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 11 |
| Execution Cells | 8 |
| Libraries | `torch`, `torchvision`, `PIL`, `requests`, `io`, `matplotlib`, `torchinfo` |
| Source Note | `5-7_CAM_and_Grad-CAM - 공유` |

## What This Note Covers

### CAM(Class Activation Map)

CAM(Class Activation... 코드를 직접 따라가며 CAM(Class Activation Map) 흐름을 확인했습니다.

- 읽을 포인트: CAM(Class Activation Map) 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### Grad-CAM

Hook이란? 같은 코드를 직접 따라가며 Grad-CAM 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Hook이란?

#### Hook이란?

Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파(backward) 중 특정 시점에 사용자 정의 함수를 "연결"하여, 그 시점의 입력, 출력 또는 기울기(gradient)를 관찰하거나 수정할 수 있게 해주는 기능입니다. 즉, 모델이 데이터를 처리하는 중간 단계...

## Why This Matters

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. CAM(Class Activation Map): CAM(Class Activation... 코드를 직접 따라가며 CAM(Class Activation Map) 흐름을 확인했습니다.
2. Grad-CAM: Hook이란?

## Code Highlights

### CAM(Class Activation Map)

`CAM(Class Activation Map)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 이미지 다운로드 및 로드, 이미지 시각화 (원본 이미지) 흐름이 주석과 함께 드러납니다.

```python
import torch
from torchvision import models, transforms
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt


# 이미지 다운로드 및 로드
url_1 = 'https://petmedaily.com/wp-content/uploads/2022/12/Featured-Image-do-goldfish-get-lonely-1536x512.png'
url_2 = 'https://pethelpful.com/.image/w_384,q_auto:good,c_limit/MjEwNDM3MjkyNzE4ODI3MzQ1/easy-ways-to-keep-fish-alive-on-a-fish-bowl-without-air-pump.jpg'
response = requests.get(url_1)
img1 = Image.open(BytesIO(response.content)).convert('RGB')  # 확실한 RGB 변환

response = requests.get(url_2)
img2 = Image.open(BytesIO(response.content)).convert('RGB')  # 확실한 RGB 변환

# 이미지 시각화 (원본 이미지)
plt.figure(figsize=(6,6))
plt.imshow(img1)
plt.axis('off')
plt.title("Sample Image")
plt.show()

plt.figure(figsize=(6,6))
plt.imshow(img2)
plt.axis('off')
plt.title("Sample Image")
# ... trimmed ...
```

### CAM(Class Activation Map)

`CAM(Class Activation Map)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 준비: 사전학습된 ResNet-18 로드 및 평가 모드로 전환, 마지막 두 레이어(fc, avgpool) 제외한 feature extractor 구성 흐름이 주석과 함께 드러납니다.

```python
import torch
from torch import nn
from torchvision import models, transforms
from torch.nn import functional as F
from PIL import Image
import matplotlib.pyplot as plt

# 1. 모델 준비: 사전학습된 ResNet-18 로드 및 평가 모드로 전환
model = models.resnet18(weights="ResNet18_Weights.IMAGENET1K_V1").eval()

# 마지막 두 레이어(fc, avgpool) 제외한 feature extractor 구성
features_extractor = nn.Sequential(*list(model.children())[:-2])
```

### CAM(Class Activation Map)

`CAM(Class Activation Map)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 준비: 사전학습된 ResNet-18 로드 및 평가 모드로 전환, 마지막 두 레이어(fc, avgpool) 제외한 feature extractor 구성, 이미지 전처리 정의: ResNet 입력에 맞게 사이즈 조정, 텐서 변환, 정규화 흐름이 주석과 함께 드러납니다.

```python
import torch
from torch import nn
from torchvision import models, transforms
from torch.nn import functional as F
from PIL import Image
import matplotlib.pyplot as plt

# 1. 모델 준비: 사전학습된 ResNet-18 로드 및 평가 모드로 전환
model = models.resnet18(weights="ResNet18_Weights.IMAGENET1K_V1").eval()

# 마지막 두 레이어(fc, avgpool) 제외한 feature extractor 구성
features_extractor = nn.Sequential(*list(model.children())[:-2])

# 2. 이미지 전처리 정의: ResNet 입력에 맞게 사이즈 조정, 텐서 변환, 정규화
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 모델 입력 크기로 조정
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],  # ImageNet 평균값
        std=[0.229, 0.224, 0.225]    # ImageNet 표준편차
    ),
])

# 3. 저장된 이미지 파일 경로 리스트 (예: img1.png, img2.png)
image_paths = ["img1.png", "img2.png"]

# 4. 각 이미지에 대해 CAM 계산 및 시각화
for image_path in image_paths:
# ... trimmed ...
```

### Hook이란?

`Hook이란?`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델의 자식 모듈들을 순회합니다., main_layer_name에 해당하는 모듈 내부에서 마지막 레이어의 자식 모듈들을 순회, forward hook: feature map 저장 흐름이 주석과 함께 드러납니다.

```python
import torch
from torch.nn import functional as F
from torchvision import models, transforms
from PIL import Image
from matplotlib import pyplot as plt


class GradCAM:
    """
    Grad-CAM 구현 클래스.
    모델의 특정 레이어(주로 마지막 컨볼루션 층)에서 feature map과 gradient를 추출하여,
    해당 feature map이 예측에 기여한 정도를 시각화하는 역할을 합니다.
    """
    def __init__(self, model, main_layer_name, sub_layer_name):
        """
        Args:
            model (torch.nn.Module): 사전학습된 모델.
            main_layer_name (str): hook을 등록할 상위 모듈 이름 (예: "layer4").
            sub_layer_name (str): 상위 모듈 내에서 hook을 등록할 하위 모듈 이름 (예: "conv2").
        """
        self.model = model.eval()  # 모델을 평가 모드로 전환
        self.register_hook(main_layer_name, sub_layer_name)  # 관심 있는 레이어에 hook 등록

    def register_hook(self, main_layer_name, sub_layer_name):
        """
        지정한 모듈의 특정 하위 모듈에 forward 및 backward hook을 등록합니다.
        """
        # 모델의 자식 모듈들을 순회합니다.
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/5-7_CAM_and_Grad-CAM - 공유.md`
- Source formats: `md`
- Companion files: `5-7_CAM_and_Grad-CAM - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `petmedaily.com`, `pethelpful.com`

## Note Preview

> Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파(backward) 중 특정 시점에 사용자 정의 함수를 "연결"하여, 그 시점의 입력, 출력 또는 기울기(gradient)를 관찰하거나 수정할 수 있게 해주는 기능입니다. 즉, 모델이 데이터를 처리하는 중간 단계에 "콜백 함수"를 등록하여, 그 정보를 따로 저장하거나 분석할 수 있습니다.
> 실제 예시 - 순전파 Hook (forward hook): - 예를 들어, 여러분이 모델의 특정 레이어가 어떤 특징(feature map)을 출력하는지 보고 싶다면, 그 레이어에 forward hook을 등록할 수 있습니다. - 이렇게 하면, 모델이 순전파를 진행할 때 해당 레이어의 출력값을 캡처할 수 있습니다. - 역전파 Hook (backward hook): - 반대로, 역전파를 할 때 각 레이어에 흐르는 기울기(gradient)를 보고 싶다면, backward hook을 등록하여 그 값을 저장할 수 있습니다. - Grad-CAM에서는 예측에 영향을 준 중요한 영역을 찾기 위해, 마지막 컨볼루션 레이어에서 계산된 gradient를 활용합니다.
