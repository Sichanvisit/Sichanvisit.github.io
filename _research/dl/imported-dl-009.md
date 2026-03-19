---
title: "PyTorch 데이터"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_데이터"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_데이터.md"
excerpt: "scikit-learn에서 California Housing 데이터셋을 불러온 뒤, 입력은 input_data에 저장하고 타깃은 target_data에 저장하세요.이때 input_data와 target_data 모두 데이터 타입은 float32로 지정해주세요."
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

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

## What I Worked On

- CSV 데이터 활용
- 이미지 데이터 활용
- 실습
- data 분할
- 데이터를 학습, 검증, 테스트 데이터로 나누기

## Implementation Flow

1. CSV 데이터 활용
2. 이미지 데이터 활용
3. 실습
4. data 분할
5. 데이터를 학습, 검증, 테스트 데이터로 나누기
6. 표준화

## Code Highlights

### data 분할

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
