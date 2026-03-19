---
title: "PyTorch 모델링 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-3_PyTorch_모델링 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-3_PyTorch_모델링 - 공유.md"
excerpt: "텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다! torch.autograd.grad는 함수𝑓의 결과(outputs)에 대해 지정된 입력 변수들(inputs) 각각의 기울기를 반환합니다"
research_summary: "텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다! torch.autograd.grad는 함수𝑓의 결과(outputs)에 대해 지정된 입력 변수들(inputs) 각각의 기울기를 반환합니다. - 반환값은 튜플 형태이며, 기울기 값을 직접 확인할 수 있습니다. - 장점: 특정 입력 변수만 선택적으로 기울기를 계산할 수 있습니다. `md` 원본과 120개 코드 블록, 57개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다."
research_artifacts: "md · 코드 120개 · 실행 57개"
code_block_count: 120
execution_block_count: 57
research_focus:
  - "모델 만들기"
  - "텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Bac..."
  - "Autograd"
research_stack:
  - "torch"
  - "numpy"
  - "pandas"
  - "sklearn"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다! torch.autograd.grad는 함수𝑓의 결과(outputs)에 대해 지정된 입력 변수들(inputs) 각각의 기울기를 반환합니다. - 반환값은 튜플 형태이며, 기울기 값을 직접 확인할 수 있습니다. - 장점: 특정 입력 변수만 선택적으로 기울기를 계산할 수 있습니다. `md` 원본과 120개 코드 블록, 57개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다.

**빠르게 볼 수 있는 포인트**: 모델 만들기, 텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forwar..., Autograd.

**남겨둔 자료**: `md` 원본과 120개 코드 블록, 57개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy, pandas, sklearn입니다.

**주요 스택**: `torch`, `numpy`, `pandas`, `sklearn`, `matplotlib`

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

## What This Note Covers

### Autograd

텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다!

### torch.autograd.grad를 이용한 기울기 계산

torch.autograd.grad는 함수𝑓의 결과(outputs)에 대해 지정된 입력 변수들(inputs) 각각의 기울기를 반환합니다. - 반환값은 튜플 형태이며, 기울기 값을 직접 확인할 수 있습니다. - 장점: 특정 입력 변수만 선택적으로 기울기를 계산할 수 있습니다

### backward()를 이용한 기울기 계산

.backward()는 requires_grad=True로 설정된 모든 변수의 기울기를 자동으로 계산하고, 각 변수의 .grad 속성에 저장합니다. - opt.zero_grad()를 사용해 이전 계산의 기울기 값을 초기화해야 누적된 기울기를 방지할 수 있습니다. - 장점: 코드가 간결하며, 다수의 변수에 대해 빠르게 기울기를 계산할 수 있습니다.

### (참고) 초기화 유무 비교

아래는 초기화(opt.zero_grad())를 하지 않는 경우의 예시 코드입니다. 초기화를 생략하면 기존 계산에서 남아있는 기울기가 누적되므로, 기울기 값이 계속 증가하는 것을 확인할 수 있습니다.

## Implementation Flow

1. Autograd: 텐서(Tensor)에서 모든 연산에 대해 자동 미분 순전파(Forward) 그래프에 의해 역전파(Backward) 그래프가 자동으로 정의됩니다!
2. torch.autograd.grad를 이용한 기울기 계산: torch.autograd.grad는 함수𝑓의 결과(outputs)에 대해 지정된 입력 변수들(inputs) 각각의 기울기를 반환합니다. - 반환값은 튜플 형태이며, 기울기 값을 직접 확인할 수 있습니다. - 장점: 특정 입력 변수만 선택적...
3. backward()를 이용한 기울기 계산: .backward()는 requires_grad=True로 설정된 모든 변수의 기울기를 자동으로 계산하고, 각 변수의 .grad 속성에 저장합니다. - opt.zero_grad()를 사용해 이전 계산의 기울기 값을 초기화해야 누적된 기울기를 방지할 수 있습...
4. (참고) 초기화 유무 비교: 아래는 초기화(opt.zero_grad())를 하지 않는 경우의 예시 코드입니다. 초기화를 생략하면 기존 계산에서 남아있는 기울기가 누적되므로, 기울기 값이 계속 증가하는 것을 확인할 수 있습니다.

## Code Highlights

### Training Loop 이해하기

`Training Loop 이해하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터 불러오기, 입력과 타깃 나누기, 데이터셋 클래스 정의 흐름이 주석과 함께 드러납니다.

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

`Training Loop 정리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터 불러오기, 입력과 타깃 나누기, 데이터셋 클래스 정의 흐름이 주석과 함께 드러납니다.

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
