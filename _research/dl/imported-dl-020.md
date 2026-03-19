---
title: "PyTorch 텐서 살펴보기 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-1_PyTorch_텐서_살펴보기 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-1_PyTorch_텐서_살펴보기 - 공유.md"
excerpt: "Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다."
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
| Code Blocks | 127 |
| Execution Cells | 95 |
| Libraries | `torch`, `numpy` |
| Source Note | `3-1_PyTorch_텐서_살펴보기 - 공유` |

## What I Worked On

- 01. 텐서만들기
- 임포트할 때 파이토치가 아니라 그냥 토치라고 써야 합니다.
- 방법 1 : torch.tensor()
- 방법 2 : torch.from_numpy()
- 방법 3 : torch.as_tensor()

## Implementation Flow

1. 01. 텐서만들기
2. 임포트할 때 파이토치가 아니라 그냥 토치라고 써야 합니다.
3. 방법 1 : torch.tensor()
4. 방법 2 : torch.from_numpy()
5. 방법 3 : torch.as_tensor()
6. 데이터 타입 지정하기

## Code Highlights

### Quiz.

```python
import numpy as np
import torch

data_list = [
    [1, 1],
    [-1, -1],
]
data_np = np.array(
    [
        [3, 4],
        [5, 6]
    ]
)

# 여기에 코드를 작성하세요.
tensor_from_list = torch.tensor(data_list)
# tensor_from_np_array = torch.np_
# 테스트 코드
print(tensor_from_list)
print(tensor_from_np_array)
```

### Quiz.

```python
import numpy as np
import torch

tensor0 = torch.tensor(
    [
        [1, 1],
        [-1, -1]
    ]
)
tensor1 = torch.tensor(
    [
        [1, 1],
        [0, 0]
    ]
)
tensor2 = torch.tensor(
    [
        [1, -1],
        [1, -1]
    ]
)

# 여기에 코드를 작성하세요.

# 테스트 코드
print(final_np_array)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/3-1_PyTorch_텐서_살펴보기 - 공유.md`
- Source formats: `md`
- Companion files: `3-1_PyTorch_텐서_살펴보기 - 공유.md`
- Note type: `concept-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `deeplearninguniversity.com`, `www.nvidia.com`

## Note Preview

> Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다.
> 변환된 텐서는 리스트와 동일한 값을 가지며, tensor() 함수를 통해 PyTorch의 텐서 객체로 만들어집니다
