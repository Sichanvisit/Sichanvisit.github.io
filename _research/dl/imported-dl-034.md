---
title: "CAM and Grad-CAM - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-7_CAM_and_Grad-CAM - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-7_CAM_and_Grad-CAM - 공유.md"
excerpt: "Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파(backward) 중 특정 시점에 사용자 정의 함수를 \"연결\"하여, 그 시점의 입력, 출력 또는 기울기(gradient)를 관찰하거나 수정할 수 있게 해주는 기능입니다"
research_summary: "Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파(backward) 중 특정 시점에 사용자 정의 함수를 \"연결\"하여, 그 시점의 입력, 출력 또는 기울기(gradient)를 관찰하거나 수정할 수 있게 해주는 기능입니다. 즉, 모델이 데이터를 처리하는 중간 단계에 \"콜백 함수\"를 등록하여, 그 정보를 따로 저장하거... 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, PIL, requests입니다."
research_artifacts: "md · 코드 11개 · 실행 8개"
code_block_count: 11
execution_block_count: 8
research_focus:
  - "CAM(Class Activation Map)"
  - "Grad-CAM"
  - "Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파(backward) 중 특정 시점..."
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

Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파(backward) 중 특정 시점에 사용자 정의 함수를 "연결"하여, 그 시점의 입력, 출력 또는 기울기(gradient)를 관찰하거나 수정할 수 있게 해주는 기능입니다. 즉, 모델이 데이터를 처리하는 중간 단계에 "콜백 함수"를 등록하여, 그 정보를 따로 저장하거... 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, PIL, requests입니다.

**빠르게 볼 수 있는 포인트**: CAM(Class Activation Map), Grad-CAM, Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파....

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

### Hook이란?

Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파(backward) 중 특정 시점에 사용자 정의 함수를 "연결"하여, 그 시점의 입력, 출력 또는 기울기(gradient)를 관찰하거나 수정할 수 있게 해주는 기능입니다. 즉, 모델이 데이터를 처리하는 중간 단계에 "콜백 함수"를 등록하여, 그 정보를 따로 저장하거나 분석할 수 있습니다.

### Key Step

CAM(Class Activation Map)

### Key Step

이미지 시각화 (원본 이미지)

### Key Step

모델 준비: 사전학습된 ResNet-18 로드 및 평가 모드로 전환

## Implementation Flow

1. Hook이란?: Hook은 PyTorch에서 모델의 순전파(forward) 또는 역전파(backward) 중 특정 시점에 사용자 정의 함수를 "연결"하여, 그 시점의 입력, 출력 또는 기울기(gradient)를 관찰하거나 수정할 수 있게 해주는 기능입니다. 즉, 모델이 데이터를 처리하는 중간 단계에...
2. Key Step: CAM(Class Activation Map)
3. Key Step: 이미지 시각화 (원본 이미지)
4. Key Step: 모델 준비: 사전학습된 ResNet-18 로드 및 평가 모드로 전환

## Code Highlights

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
