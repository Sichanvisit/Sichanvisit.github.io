---
title: "PyTorch 데이터"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_데이터"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_데이터.md"
excerpt: "실습, CSV 데이터 활용 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실습, CSV 데이터 활용, 이미지 데이터 활용 순서로 핵심 장면을 먼저 훑고, class CustomDataset(D..., 이미지 데이터 활용, 실습 같은..."
research_summary: "실습, CSV 데이터 활용 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실습, CSV 데이터 활용, 이미지 데이터 활용 순서로 핵심 장면을 먼저 훑고, class CustomDataset(D..., 이미지 데이터 활용, 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 58개 코드 블록, 54개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다."
research_artifacts: "md · 코드 58개 · 실행 54개"
code_block_count: 58
execution_block_count: 54
research_focus:
  - "실습"
  - "CSV 데이터 활용"
  - "이미지 데이터 활용"
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
  - archive-note
---

실습, CSV 데이터 활용 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실습, CSV 데이터 활용, 이미지 데이터 활용 순서로 핵심 장면을 먼저 훑고, class CustomDataset(D..., 이미지 데이터 활용, 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 58개 코드 블록, 54개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다.

**빠르게 볼 수 있는 포인트**: 실습, CSV 데이터 활용, 이미지 데이터 활용.

**남겨둔 자료**: `md` 원본과 58개 코드 블록, 54개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다.

**주요 스택**: `torch`, `numpy`, `pandas`, `PIL`, `glob`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 58 |
| Execution Cells | 54 |
| Libraries | `torch`, `numpy`, `pandas`, `PIL`, `glob`, `matplotlib`, `sklearn` |
| Source Note | `(실습)PyTorch_데이터` |

## What This Note Covers

### 실습

scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요. California Housing 데이터셋의 입력과 타깃을 짝지어 관리하는...

- 읽을 포인트: 실습 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### CSV 데이터 활용

CSV 데이터 활용 코드를 직접 따라가며 CSV 데이터 활용 흐름을 확인했습니다.

- 읽을 포인트: CSV 데이터 활용 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 이미지 데이터 활용

이미지 데이터 활용 코드를 직접 따라가며 이미지 데이터 활용 흐름을 확인했습니다.

- 읽을 포인트: 이미지 데이터 활용 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### data 분할

data 분할 코드를 직접 따라가며 data 분할 흐름을 확인했습니다.

- 읽을 포인트: data 분할 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 표준화

표준화 코드를 직접 따라가며 표준화 흐름을 확인했습니다.

- 읽을 포인트: 표준화 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 데이터 로더

데이터 로더 코드를 직접 따라가며 데이터 로더 흐름을 확인했습니다.

- 읽을 포인트: 데이터 로더 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. 실습: scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세...
2. CSV 데이터 활용: CSV 데이터 활용 코드를 직접 따라가며 CSV 데이터 활용 흐름을 확인했습니다.
3. 이미지 데이터 활용: 이미지 데이터 활용 코드를 직접 따라가며 이미지 데이터 활용 흐름을 확인했습니다.
4. data 분할: data 분할 코드를 직접 따라가며 data 분할 흐름을 확인했습니다.
5. 표준화: 표준화 코드를 직접 따라가며 표준화 흐름을 확인했습니다.
6. 데이터 로더: 데이터 로더 코드를 직접 따라가며 데이터 로더 흐름을 확인했습니다.

## Code Highlights

### class CustomDataset(Dataset)

`class CustomDataset(Dataset)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 데이터를 모델이 바로 받을 수 있는 샘플 구조로 바꾸기 위해 커스텀 Dataset을 정의하는 부분입니다.

```python
class CustomDataset(Dataset):
    def __init__(self):
        self.x =[
            [10,20],
            [10,20],
            [10,20],
            [10,20],
            [10,20]
        ]
        self.y = [0,0,1,1,1]

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        input_data = self.x[index]
        label = self.y[index]
        return torch.tensor(input_data), torch.tensor(label)
```

### 이미지 데이터 활용

`이미지 데이터 활용`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 데이터를 모델이 바로 받을 수 있는 샘플 구조로 바꾸기 위해 커스텀 Dataset을 정의하는 부분입니다.

```python
class FlowerDataset(Dataset):
    def __init__(self, image_paths):
        self.image_paths = image_paths

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):
        image_path=self.image_paths[index]
        image = Image.open(image_path)
        image_np = np.array(image)
        return torch.tensor(image_np)
```

### 실습

`실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 마지막 부분에서 0번 인덱스 데이터를 출력했을 때 다음과 같은 결과가 나와야 합니다.

```python
class CalHousingDataset(Dataset):
    def __init__(self):
        cal_housing = datasets.fetch_california_housing()
        self.input_data = cal_housing.data.astype(np.float32)
        self.target_data = cal_housing.target.astype(np.float32)

    def __len__(self):
        return len(self.input_data)

    def __getitem__(self, index):
        input_tensor = torch.tensor(self.input_data[index])
        target_tensor = torch.tensor(self.target_data[index])
        return input_tensor, target_tensor
```

### 표준화

`표준화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋 클래스 정의, # 데이터 표준화 수행, if self.scaler 흐름이 주석과 함께 드러납니다.

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

        self.inputs = self.scale_transform(inputs)
        # # 데이터 표준화 수행
        # if self.scaler:
        #     self.inputs = self.scaler.transform(inputs)
        # else:
        #     self.inputs = inputs

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, index):
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)PyTorch_데이터.md`
- Source formats: `md`
- Companion files: `(실습)PyTorch_데이터.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요.
> California Housing 데이터셋의 입력과 타깃을 짝지어 관리하는 커스텀 Dataset 클래스 CaliforniaHousingDataset을 정의해 주세요.
