---
title: "PyTorch 모델링 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-3_PyTorch_모델링 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-3_PyTorch_모델링 - 공유.md"
excerpt: "- 텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다!"
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
| Code Blocks | 120 |
| Execution Cells | 57 |
| Libraries | `torch`, `numpy`, `pandas`, `sklearn`, `matplotlib` |
| Source Note | `3-3_PyTorch_모델링 - 공유` |

## What I Worked On

- 모델 만들기
- Autograd
- torch.autograd.grad를 이용한 기울기 계산
- 1. 텐서 정의 및 초기화
- 2. 수식 정의

## Implementation Flow

1. 모델 만들기
2. Autograd
3. torch.autograd.grad를 이용한 기울기 계산
4. 1. 텐서 정의 및 초기화
5. 2. 수식 정의
6. 3. autograd.grad로 기울기 계산

## Code Highlights

### Training Loop 이해하기

```python
# 데이터 불러오기
abalone_df = pd.read_csv(
    'https://storage.googleapis.com/download.tensorflow.org/data/abalone_train.csv',
    names=['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
           'Viscera weight', 'Shell weight', 'Age']
)

# 입력과 타깃 나누기
input_data = abalone_df.drop(columns=['Age']).to_numpy().astype(np.float32)
target_data = abalone_df['Age'].to_numpy().astype(np.float32)

# 데이터셋 클래스 정의
class AbaloneDataset(Dataset):
    def __init__(self, input_data, target_data):
        self.input_data = input_data
        self.target_data = target_data

    def __len__(self):
        return len(self.input_data)

    def __getitem__(self, index):
        input_tensor = torch.tensor(self.input_data[index], dtype=torch.float32)
        target_tensor = torch.tensor(self.target_data[index], dtype=torch.float32)
        return input_tensor, target_tensor

# 학습/검증/테스트 데이터 분할
train_size = int(len(input_data) * 0.8)
val_size = int(len(input_data) * 0.1)
# ... trimmed ...
```

### Training Loop 정리

```python
# 데이터 불러오기
abalone_df = pd.read_csv(
    'https://storage.googleapis.com/download.tensorflow.org/data/abalone_train.csv',
    names=['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
           'Viscera weight', 'Shell weight', 'Age']
)

# 입력과 타깃 나누기
input_data = abalone_df.drop(columns=['Age']).to_numpy().astype(np.float32)
target_data = abalone_df['Age'].to_numpy().astype(np.float32)

# 데이터셋 클래스 정의
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

# 학습/검증/테스트 데이터 분할
train_size = int(len(input_data) * 0.8)
val_size = int(len(input_data) * 0.1)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/3-3_PyTorch_모델링 - 공유.md`
- Source formats: `md`
- Companion files: `3-3_PyTorch_모델링 - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2.0, 2.0, 2.0`, `0.0, 0.0, 1.0`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `storage.googleapis.com`

## Note Preview

> - 텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다!
> - torch.autograd.grad는 함수𝑓의 결과(outputs)에 대해 지정된 입력 변수들(inputs) 각각의 기울기를 반환합니다. - 반환값은 튜플 형태이며, 기울기 값을 직접 확인할 수 있습니다. - 장점: 특정 입력 변수만 선택적으로 기울기를 계산할 수 있습니다
