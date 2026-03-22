---
title: "CNN 이미지 분류 part2 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "4-3_CNN_이미지 분류_part2 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/4-3_CNN_이미지 분류_part2 - 공유.md"
excerpt: "CNN 이미지 분류 part2 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 이미지 데이터 증강하기, 이미지 데이터 전처리하기, 데이터 소개 순서로 핵심 장면을 먼저 훑고, 데이터셋 생성 시 전처리 적용, Compose, 모델 학습시키기 같..."
research_summary: "CNN 이미지 분류 part2 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 이미지 데이터 증강하기, 이미지 데이터 전처리하기, 데이터 소개 순서로 핵심 장면을 먼저 훑고, 데이터셋 생성 시 전처리 적용, Compose, 모델 학습시키기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 60개 코드 블록, 27개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다."
research_artifacts: "md · 코드 60개 · 실행 27개"
code_block_count: 60
execution_block_count: 27
research_focus:
  - "이미지 데이터 증강하기"
  - "이미지 데이터 전처리하기"
  - "데이터 소개"
research_stack:
  - "numpy"
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "PIL"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

CNN 이미지 분류 part2 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 이미지 데이터 증강하기, 이미지 데이터 전처리하기, 데이터 소개 순서로 핵심 장면을 먼저 훑고, 데이터셋 생성 시 전처리 적용, Compose, 모델 학습시키기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 60개 코드 블록, 27개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: 이미지 데이터 증강하기, 이미지 데이터 전처리하기, 데이터 소개.

**남겨둔 자료**: `md` 원본과 60개 코드 블록, 27개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, torch, torchvision, matplotlib입니다.

**주요 스택**: `numpy`, `torch`, `torchvision`, `matplotlib`, `PIL`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 60 |
| Execution Cells | 27 |
| Libraries | `numpy`, `torch`, `torchvision`, `matplotlib`, `PIL`, `torchinfo`, `sklearn` |
| Source Note | `4-3_CNN_이미지 분류_part2 - 공유` |

## What This Note Covers

### 이미지 데이터 증강하기

데이터 증강은 학습 데이터를 변형하여 데이터 다양성을 높이고, 오버피팅 방지 및 모델 일반화 성능 향상을 목표로 합니다.

- 읽을 포인트: 세부 흐름: 데이터 증강이란?, 데이터 증강의 효과, 데이터 증강의 효과 > 주의사항

#### 데이터 증강이란?

기존 학습 데이터를 변형하여 데이터 양을 효과적으로 늘리는 방법입니다. - 이미지 데이터의 경우, 이미지 반전, 회전, 자르기, 밝기 조정 등 다양한 방식으로 증강할 수 있습니다.

#### 데이터 증강의 효과

학습 데이터 다양성을 높여 오버피팅 방지. - 모델의 일반화 성능 향상.

#### 데이터 증강의 효과 > 주의사항

학습 데이터: 증강 및 전처리 적용. - 테스트 데이터: 증강 없이 전처리만 적용.

### 이미지 데이터 전처리하기

Fashion MNIST 데이터셋을 대상으로 전처리 과정을 진행하며, 텐서 변환, 스케일링, 표준화, 그리고 전처리를 데이터셋에 적용하는 방법을 살펴봅니다. Fashion MNIST 데이터를 불러오면 이미지가 Pillow(PIL) 형식으로 제공됩니다.

- 읽을 포인트: 세부 흐름: 텐서변환, 데이터 타입 변환 및 스케일링, 데이터셋 생성 시 전처리 적용

#### 텐서변환

결과 타입: torchvision.tv_tensors._image.Image - 크기: 텐서의 첫 번째 차원은 채널 수(1, 그레이스케일). - 변환 후에도 픽셀값은 0~255

#### 데이터 타입 변환 및 스케일링

딥러닝 모델 학습을 위해 픽셀값을 0~1 범위의 실수(float)로 변환해야 합니다. dtype: 텐서의 데이터 타입(예: torch.float32). - scale=True: 픽셀값을 0~1로 스케일링.

#### 데이터셋 생성 시 전처리 적용

Fashion MNIST 데이터셋을 생성할 때, 전처리(transform)를 바로 적용할 수 있습니다.

### 데이터 소개

Fashion MNIST는 다양한 패션 아이템 이미지가 포함된 데이터셋입니다.

- 읽을 포인트: 세부 흐름: 데이터셋 특징, 데이터 불러오기, 데이터 구조

#### 데이터셋 특징

학습 데이터: 6만 개 - 테스트 데이터: 1만 개 - 이미지 크기: 28×28 (그레이스케일) - 클래스: 총 10개 (각 클래스에 데이터 균등 분포)

#### 데이터 불러오기

PyTorch의 TorchVision 라이브러리 TorchVision은 PyTorch에서 제공하는 컴퓨터 비전용 라이브러리입니다. - 다양한 데이터셋, 모델, 이미지 전처리 및 증강 기능을 지원합니다. - 이번 강의에서는 TorchVision의 datasets 모듈을 활용합니다.

#### 데이터 구조

각 데이터는 튜플 형태: 1. 이미지 데이터 (PIL.Image 객체) 2. 레이블 (정수 값) 입력값: 이미지 데이터(image), 클래스 레이블(label). - 출력값: 이미지를 그레이스케일로 시각화하며, 클래스 이름 표시.

### CNN 모델에 사용되는 레이어

Conv2d > 주요 파라미터, Pooling Layer, Pooling Layer > 주요... 같은 코드를 직접 따라가며 CNN 모델에 사용되는 레이어 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Conv2d > 주요 파라미터, Pooling Layer, Pooling Layer > 주요 파라미터

#### Conv2d > 주요 파라미터

in_channels: 입력 데이터의 채널 수. - out_channels: 출력 데이터의 채널 수 = 필터 개수. - kernel_size: 필터 크기. (정수 → 정사각형, 튜플 → 직사각형 가능) - stride: 필터 이동 간격. (기본값: 1) - padding: 입력 가...

#### Pooling Layer

풀링 레이어는 데이터를 다운샘플링하여 크기를 줄이고, 중요한 정보를 추출합니다. 맥스 풀링(Max Pooling): 윈도우 내 최댓값 선택. - 애버리지 풀링(Average Pooling): 윈도우 내 평균값 선택.

#### Pooling Layer > 주요 파라미터

kernel_size: 풀링 윈도우 크기. - stride: 윈도우 이동 간격. - padding: 가장자리 패딩 크기. 배치 크기와 채널 수: 동일. - 높이와 너비: kernel_size와 stride에 따라 축소.

### CNN 모델 만들기

주요 파라미터, 모델의 특징 요약 같은 코드를 직접 따라가며 CNN 모델 만들기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 주요 파라미터, 모델의 특징 요약

#### 주요 파라미터

nn.Conv2d - in_channels: 입력 채널 수 (예: 1 → 그레이스케일 이미지). - out_channels: 출력 채널 수 (필터 개수). - kernel_size: 필터 크기. - stride: 필터 이동 간격. - padding: 가장자리 패딩 크기. - nn....

#### 모델의 특징 요약

두 개의 컨볼루셔널 레이어와 맥스풀링 레이어를 사용. 2. 중간에 드롭아웃 레이어로 오버피팅 방지. 3. 최종적으로 Flatten과 리니어 레이어로 10개의 클래스를 예측.

### 모델 학습시키기

모델 학습시키기 코드를 직접 따라가며 모델 학습시키기 흐름을 확인했습니다.

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

1. 이미지 데이터 증강하기: 데이터 증강이란?, 데이터 증강의 효과
2. 이미지 데이터 전처리하기: 텐서변환, 데이터 타입 변환 및 스케일링
3. 데이터 소개: 데이터셋 특징, 데이터 불러오기
4. CNN 모델에 사용되는 레이어: Conv2d > 주요 파라미터, Pooling Layer
5. CNN 모델 만들기: 주요 파라미터, 모델의 특징 요약
6. 모델 학습시키기: 모델 학습시키기 코드를 직접 따라가며 모델 학습시키기 흐름을 확인했습니다.

## Code Highlights

### 데이터셋 생성 시 전처리 적용

`데이터셋 생성 시 전처리 적용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. Fashion MNIST 데이터셋을 생성할 때, 전처리(transform)를 바로 적용할 수 있습니다.

```python
train_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=True,
    download=True,
    transform=transforms,
)

test_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=False,
    download=True,
    transform=transforms,
)
```

### Compose

`Compose`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. TorchVision의 Compose 객체를 활용해 여러 전처리 및 증강 기법을 결합할 수 있습니다.

```python
from torchvision import datasets

train_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=True,
    download=True,
    transform=transforms_train,
)

test_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=False,
    download=True,
    transform=transforms_test,
)
```

### 모델 학습시키기

`모델 학습시키기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋과 전처리, 학습 데이터에는 이미지 증강을 포함하고, 검증 데이터와 테스트 데이터는 단순 전처리만 적... 흐름이 주석과 함께 드러납니다.

```python
# 데이터셋과 전처리
# 학습 데이터에는 이미지 증강을 포함하고, 검증 데이터와 테스트 데이터는 단순 전처리만 적용합니다.

transforms_train = v2.Compose(
    [
        v2.ToImage(),
        v2.RandomHorizontalFlip(),
        v2.RandomResizedCrop(size=28),
        v2.RandomRotation(degrees=10),
        v2.ToDtype(dtype=torch.float32, scale=True),
        v2.Normalize(mean=[0.286], std=[0.353]),
    ]
)

transforms_test = v2.Compose(
    [
        v2.ToImage(),
        v2.ToDtype(dtype=torch.float32, scale=True),
        v2.Normalize(mean=[0.286], std=[0.353]),
    ]
)

train_dataset = datasets.FashionMNIST(
    root='./fashion_mnist',
    train=True,
    download=True,
    transform=transforms_train,
)
# ... trimmed ...
```

### (참고) ImageFolder

`(참고) ImageFolder`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터 증강 및 전처리 정의, 훈련 데이터 전용: 증강 포함, 검증 및 테스트 데이터 전용: 증강 없음 흐름이 주석과 함께 드러납니다.

```python
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Subset
from sklearn.model_selection import train_test_split

# 1. 데이터 증강 및 전처리 정의
# 훈련 데이터 전용: 증강 포함
transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),  # 랜덤 좌우 반전
    transforms.RandomRotation(30),          # 랜덤 회전 (-30도 ~ 30도)
    transforms.RandomResizedCrop(224),      # 랜덤 자르기 후 크기 조정
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),  # 밝기/대비/채도 조정
    transforms.ToTensor(),                  # 텐서로 변환
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])    # 정규화
])

# 검증 및 테스트 데이터 전용: 증강 없음
transform_test = transforms.Compose([
    transforms.Resize(256),                 # 크기 조정
    transforms.CenterCrop(224),             # 중앙 자르기
    transforms.ToTensor(),                  # 텐서로 변환
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])    # 정규화
])

# 2. 데이터셋 로드
original_dataset = datasets.ImageFolder(root="flower_photos")

# 3. 데이터셋 인덱스 추출 및 분할
indices = list(range(len(original_dataset)))
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/4-3_CNN_이미지 분류_part2 - 공유.md`
- Source formats: `md`
- Companion files: `4-3_CNN_이미지 분류_part2 - 공유.md`
- Note type: `resource-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> Fashion MNIST는 다양한 **패션 아이템 이미지**가 포함된 데이터셋입니다.
> - **학습 데이터**: 6만 개 - **테스트 데이터**: 1만 개 - **이미지 크기**: 28×28 (그레이스케일) - **클래스**: 총 10개 (각 클래스에 데이터 균등 분포)
