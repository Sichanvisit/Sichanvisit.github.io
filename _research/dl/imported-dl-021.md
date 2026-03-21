---
title: "PyTorch 데이터 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-2_PyTorch_데이터 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-2_PyTorch_데이터 - 공유.md"
excerpt: "실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다. 전복(Abalone) 데이터셋을 판다스를 사용해 읽어옵니다. 데이터 크기가 너무 커서 메모리에 모두 올리기 어려운 경우를 대비해 PyTorch Dataset 클래스를 활용..."
research_summary: "실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다. 전복(Abalone) 데이터셋을 판다스를 사용해 읽어옵니다. 데이터 크기가 너무 커서 메모리에 모두 올리기 어려운 경우를 대비해 PyTorch Dataset 클래스를 활용하는 방법을 배워봅니다. `md` 원본과 54개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다."
research_artifacts: "md · 코드 54개 · 실행 24개"
code_block_count: 54
execution_block_count: 24
research_focus:
  - "PyTorch에서 데이터 다루기"
  - "Dataset 살펴보기"
  - "Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다..."
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

실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다. 전복(Abalone) 데이터셋을 판다스를 사용해 읽어옵니다. 데이터 크기가 너무 커서 메모리에 모두 올리기 어려운 경우를 대비해 PyTorch Dataset 클래스를 활용하는 방법을 배워봅니다. `md` 원본과 54개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다.

**빠르게 볼 수 있는 포인트**: PyTorch에서 데이터 다루기, Dataset 살펴보기, Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주....

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

### Dataset 살펴보기 : 간단한 데이터 > Dataset 클래스 만들기

Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다. 커스텀 데이터셋을 정의하면, 데이터셋의 크기와 특정 인덱스 데이터를 쉽게 확인할 수 있습니다. 이번 예제에서는 간단한 2차원 데이터와 이진 레이블을 활용해 Dataset 클래스를 만들어보겠습니다.

### PyTorch에서 데이터 다루기 > CSV 데이터 활용하기

실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다. 전복(Abalone) 데이터셋을 판다스를 사용해 읽어옵니다.

### PyTorch에서 데이터 다루기 > 이미지 데이터

데이터 크기가 너무 커서 메모리에 모두 올리기 어려운 경우를 대비해 PyTorch Dataset 클래스를 활용하는 방법을 배워봅니다.

### PyTorch에서 데이터 다루기 > 실습

scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요. California Housing 데이터셋의 입력과 타깃을 짝지어 관리하는 커스텀 Dataset 클래스 CaliforniaHou...

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. Dataset 살펴보기 : 간단한 데이터 > Dataset 클래스 만들기: Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다. 커스텀 데이터셋을 정의하면, 데이터셋의 크기와 특정 인덱스 데이터를 쉽게 확인할 수 있습니다. 이번 예제에서는 간단한...
2. PyTorch에서 데이터 다루기 > CSV 데이터 활용하기: 실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다. 전복(Abalone) 데이터셋을 판다스를 사용해 읽어옵니다.
3. PyTorch에서 데이터 다루기 > 이미지 데이터: 데이터 크기가 너무 커서 메모리에 모두 올리기 어려운 경우를 대비해 PyTorch Dataset 클래스를 활용하는 방법을 배워봅니다.
4. PyTorch에서 데이터 다루기 > 실습: scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세...

## Code Highlights

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

`데이터 로더(Data Loader)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 딥러닝 모델 학습에서는 데이터를 하나씩 처리하지 않고, 미니 배치 단위로 묶어서 처리합니다. PyTorch에서는 이러한 작업을 손쉽게 처리할 수 있도록 DataLoader 클래스를 제공합니다.

```python
abalone_df = pd.read_csv(
    'https://storage.googleapis.com/download.tensorflow.org/data/abalone_train.csv',
    names=['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
           'Viscera weight', 'Shell weight', 'Age']
)

input_data = abalone_df.drop(columns=['Age']).to_numpy().astype(np.float32)
target_data = abalone_df['Age'].to_numpy().astype(np.float32)

class AbaloneDataset(Dataset):
    def __init__(self, input_data, target_data):
        self.input_data = input_data
        self.target_data = target_data

    def __len__(self):
        return len(self.input_data)

    def __getitem__(self, index):
        input_tensor = torch.tensor(self.input_data[index])
        target_tensor = torch.tensor(self.target_data[index])
        return input_tensor, target_tensor

train_size = int(len(input_data) * 0.8)
val_size = int(len(input_data) * 0.1)

train_inputs = input_data[:train_size]
train_targets = target_data[:train_size]

# ... trimmed ...
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
