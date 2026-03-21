---
title: "PyTorch 데이터"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_데이터"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_데이터.md"
excerpt: "scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요"
research_summary: "scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 58개 코드 블록, 54개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다."
research_artifacts: "md · 코드 58개 · 실행 54개"
code_block_count: 58
execution_block_count: 54
research_focus:
  - "CSV 데이터 활용"
  - "이미지 데이터 활용"
  - "scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_..."
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

scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 58개 코드 블록, 54개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, PIL입니다.

**빠르게 볼 수 있는 포인트**: CSV 데이터 활용, 이미지 데이터 활용, scikit-learn에서 California Housing 데이터셋을....

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

scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요.

### Key Step

데이터를 학습, 검증, 테스트 데이터로 나누기

### Key Step

train_dataset.log_statistics()

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. 실습: scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요.
2. Key Step: 데이터를 학습, 검증, 테스트 데이터로 나누기
3. Key Step: train_dataset.log_statistics()

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

### data 분할

`data 분할`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 데이터를 모델이 바로 받을 수 있는 샘플 구조로 바꾸기 위해 커스텀 Dataset을 정의하는 부분입니다.

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
