---
title: "PyTorch 데이터 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-2_PyTorch_데이터 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-2_PyTorch_데이터 - 공유.md"
excerpt: "Dataset 클래스는 데이터셋과 레이블을 관리하기 편리하게 만들어 주는 PyTorch의 유틸리티입니다. 커스텀 데이터셋을 정의하면, 데이터셋의 크기와 특정 인덱스 데이터를 쉽게 확인할 수 있습니다."
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

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

## What I Worked On

- PyTorch에서 데이터 다루기
- Dataset 살펴보기 : 간단한 데이터
- Dataset 클래스 만들기
- Dataset 클래스를 상속받아 커스텀 데이터셋을 정의합니다.
- Dataset 객체 사용하기

## Implementation Flow

1. PyTorch에서 데이터 다루기
2. Dataset 살펴보기 : 간단한 데이터
3. Dataset 클래스 만들기
4. Dataset 클래스를 상속받아 커스텀 데이터셋을 정의합니다.
5. Dataset 객체 사용하기
6. 객체 생성

## Code Highlights

### 데이터셋 클래스에 전처리 코드를 함께 넣는다면?

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
