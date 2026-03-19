---
title: "PyTorch 데이터 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-2_PyTorch_데이터 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-2_PyTorch_데이터 - 공유.md"
excerpt: "Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다"
research_summary: "Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다. 커스텀 데이터셋을 정의하면, 데이터셋의 크기와 특정 인덱스 데이터를 쉽게 확인할 수 있습니다. 실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다. `md` 원본과 54개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다."
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

Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다. 커스텀 데이터셋을 정의하면, 데이터셋의 크기와 특정 인덱스 데이터를 쉽게 확인할 수 있습니다. 실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다. `md` 원본과 54개 코드 블록, 24개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다.

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

### Dataset 클래스 만들기

Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다. 커스텀 데이터셋을 정의하면, 데이터셋의 크기와 특정 인덱스 데이터를 쉽게 확인할 수 있습니다.

### CSV 데이터 활용하기

실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다.

### 이미지 데이터

데이터 크기가 너무 커서 메모리에 모두 올리기 어려운 경우를 대비해 PyTorch Dataset 클래스를 활용하는 방법을 배워봅니다.

### 실습

scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요.

## Implementation Flow

1. Dataset 클래스 만들기: Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다. 커스텀 데이터셋을 정의하면, 데이터셋의 크기와 특정 인덱스 데이터를 쉽게 확인할 수 있습니다.
2. CSV 데이터 활용하기: 실제 데이터를 담고 있는 CSV 파일을 활용하여 PyTorch의 Dataset 클래스를 정의하고 사용하는 방법을 배워보겠습니다.
3. 이미지 데이터: 데이터 크기가 너무 커서 메모리에 모두 올리기 어려운 경우를 대비해 PyTorch Dataset 클래스를 활용하는 방법을 배워봅니다.
4. 실습: scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요.

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
