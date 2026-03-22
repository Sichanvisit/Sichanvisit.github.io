---
title: "PyTorch 데이터 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-2_PyTorch_데이터 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-2_PyTorch_데이터 - 공유.md"
excerpt: "PyTorch에서 데이터 다루기 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 PyTorch에서 데이터 다루기 순서로 핵심 장면을 먼저 훑고, 이미지 데이터, 데이터셋 클래스에 전처리 코드를 함께..., 데이터 로더(Data Loa..."
research_summary: "PyTorch에서 데이터 다루기 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 PyTorch에서 데이터 다루기 순서로 핵심 장면을 먼저 훑고, 이미지 데이터, 데이터셋 클래스에 전처리 코드를 함께..., 데이터 로더(Data Loader) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 54개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다."
research_artifacts: "md · 코드 54개 · 실행 24개"
code_block_count: 54
execution_block_count: 24
research_focus:
  - "PyTorch에서 데이터 다루기"
research_stack:
  - "torch"
  - "numpy"
  - "pandas"
  - "PIL"
  - "glob"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

PyTorch에서 데이터 다루기 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 PyTorch에서 데이터 다루기 순서로 핵심 장면을 먼저 훑고, 이미지 데이터, 데이터셋 클래스에 전처리 코드를 함께..., 데이터 로더(Data Loader) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 54개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다.

**빠르게 볼 수 있는 포인트**: PyTorch에서 데이터 다루기.

**남겨둔 자료**: `md` 원본과 54개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다.

**주요 스택**: `torch`, `numpy`, `pandas`, `PIL`, `glob`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 54 |
| Execution Cells | 24 |
| Libraries | `torch`, `numpy`, `pandas`, `PIL`, `glob`, `matplotlib`, `sklearn` |
| Source Note | `3-2_PyTorch_데이터 - 공유` |

## What This Note Covers

### PyTorch에서 데이터 다루기

데이터 분할과 표준화, 데이터 분할과 표준화 > 데이터 분할, 데이터 분할과 표준화 > 표준화 같은 코드를 직접 따라가며 PyTorch에서 데이터 다루기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 데이터 분할과 표준화, 데이터 분할과 표준화 > 데이터 분할, 데이터 분할과 표준화 > 표준화

#### 데이터 분할과 표준화

PyTorch에서 데이터셋을 학습, 검증, 테스트로 분할하고, 데이터를 표준화하는 과정을 배웁니다.

#### 데이터 분할과 표준화 > 데이터 분할

여기서 데이터를 분할한다는 건, 학습, 검증, 테스트에 서로 다른 데이터가 사용되도록 나누는 걸 뜻해요. 모델 학습이 얼마나 잘 됐는지 똑바로 평가하려면, 학습 과정에서 이미 사용한 데이터가 아닌 다른 데이터가 필요합니다.

#### 데이터 분할과 표준화 > 표준화

전복 데이터처럼 수치형 데이터를 사용할 때는, 각 피처마다 평균이 0, 표준편차가 1이 되도록 표준화를 해 주는 경우가 많습니다. 그래야 피처의 스케일에 영향을 받지 않고, 모델을 더 안정적으로 학습시킬 수 있거든요.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. PyTorch에서 데이터 다루기: 데이터 분할과 표준화, 데이터 분할과 표준화 > 데이터 분할

## Code Highlights

### 이미지 데이터

`이미지 데이터`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 from torchvision.transforms import ToTensor, ToPI..., totensor = ToTensor(), return totensor(image) 흐름이 주석과 함께 드러납니다.

```python
# from torchvision.transforms import ToTensor, ToPILImage
# totensor = ToTensor()

class FlowerDataset(Dataset):
  def __init__(self):
      self.image_paths = glob.glob('/content/flower_photos/*/*.jpg')

  def __len__(self):
    return len(self.image_paths)

  def __getitem__(self, index):
    image_path = self.image_paths[index]
    image = Image.open(image_path)
    image_np = np.array(image)
    return torch.tensor(image_np)
    # return totensor(image)
```

### 데이터셋 클래스에 전처리 코드를 함께 넣는다면?

`데이터셋 클래스에 전처리 코드를 함께 넣는다면?`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋 클래스 정의, 데이터 표준화 수행, 스케일러가 없는 경우 데이터를 그대로 반환 흐름이 주석과 함께 드러납니다.

```python
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import Dataset

# 데이터셋 클래스 정의
class AbaloneDataset(Dataset):
    def __init__(self, inputs, targets, scaler=None):
        """
        초기화 메서드
        :param inputs: 원본 입력 데이터 (numpy 배열)
        :param targets: 레이블 데이터 (numpy 배열)
        :param scaler: Scikit-learn의 StandardScaler 객체 (선택사항)
        """
        self.original_inputs = inputs  # 복원을 위해 원본 데이터 저장
        self.targets = targets
        self.scaler = scaler

        # 데이터 표준화 수행
        if self.scaler:
            self.inputs = self.scaler.transform(inputs)
        else:
            self.inputs = inputs

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, index):
        input_data = torch.tensor(self.inputs[index], dtype=torch.float32)
# ... trimmed ...
```

### 데이터 로더(Data Loader)

`데이터 로더(Data Loader)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터 셔플링, 데이터 순서를 랜덤하게 섞으려면 shuffle=True를 사용합니다. 흐름이 주석과 함께 드러납니다.

```python
# 데이터 셔플링
# 데이터 순서를 랜덤하게 섞으려면 shuffle=True를 사용합니다.

train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True)

for train_batch in train_dataloader:
    print(f'Input batch\n{train_batch[0]}\n')
    print(f'Target batch\n{train_batch[1]}')
    break
```

### 실습

`실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 CaliforniaHousingDataset 클래스 정의, 학습/검증/테스트 분할, 학습 입력 데이터 기준 표준화 흐름이 주석과 함께 드러납니다.

```python
# CaliforniaHousingDataset 클래스 정의
class CaliforniaHousingDataset(Dataset):
    def __init__(self, input_data, target_data):
        self.input_data = input_data
        self.target_data = target_data

    def __len__(self):
        return len(self.input_data)

    def __getitem__(self, index):
        input_tensor = torch.tensor(self.input_data[index])
        target_tensor = torch.tensor(self.target_data[index])
        return input_tensor, target_tensor

# 학습/검증/테스트 분할
train_size = int(len(input_data) * 0.8)
val_size = int(len(input_data) * 0.1)

train_inputs = input_data[:train_size]
train_targets = target_data[:train_size]

val_inputs = input_data[train_size:train_size + val_size]
val_targets = target_data[train_size:train_size + val_size]

test_inputs = input_data[train_size + val_size:]
test_targets = target_data[train_size + val_size:]

# 학습 입력 데이터 기준 표준화
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/3-2_PyTorch_데이터 - 공유.md`
- Source formats: `md`
- Companion files: `3-2_PyTorch_데이터 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다. 커스텀 데이터셋을 정의하면, 데이터셋의 크기와 특정 인덱스 데이터를 쉽게 확인할 수 있습니다.
> 이번 예제에서는 간단한 2차원 데이터와 이진 레이블을 활용해 Dataset 클래스를 만들어보겠습니다.
