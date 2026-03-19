---
title: "PyTorch 텐서 살펴보기"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_텐서_살펴보기"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_텐서_살펴보기.md"
excerpt: "파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다. 이 두 데이터를 PyTorch 텐서로 만들어 주세요."
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
| Code Blocks | 119 |
| Execution Cells | 117 |
| Libraries | `torch`, `numpy` |
| Source Note | `(실습)PyTorch_텐서_살펴보기` |

## What I Worked On

- 텐서만들기
- 방법 1 : torch.tensor()
- 방법 3: torch.as_tensor()
- torch_from_numpy2 = torch.from_numpy([[1,2],[3,4]])
- data 타입

## Implementation Flow

1. 텐서만들기
2. 방법 1 : torch.tensor()
3. 방법 3: torch.as_tensor()
4. torch_from_numpy2 = torch.from_numpy([[1,2],[3,4]])
5. data 타입
6. gpu_int_tensor = tensor.to(dtype=torch.int32, device='cuda')

## Code Highlights

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
a = tensor0 + tensor1
b = a @ tensor2
c = b + torch.tensor([2,-2])
#[[4,-4]   [[2 -2]
# [-2 2]]  [2 -2]]
# ... trimmed ...
```

### 여러 텐서 합치기

```python
x = torch.tensor(
    [
        [
            [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [1,2,3,4,5],
                [6,7,8,9,10]
            ],
            [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [1,2,3,4,5],
                [6,7,8,9,10]
            ]
        ],
        [
            [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [1,2,3,4,5],
                [6,7,8,9,10]
            ],
            [
                [1,2,3,4,5],
                [6,7,8,9,10],
                [1,2,3,4,5],
                [6,7,8,9,10]
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)PyTorch_텐서_살펴보기.md`
- Source formats: `md`
- Companion files: `(실습)PyTorch_텐서_살펴보기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다. 이 두 데이터를 PyTorch 텐서로 만들어 주세요.
> data_list에서 만든 텐서는 tensor_from_list 변수에 저장하고, data_np에서 만든 텐서는 tensor_from_np_array에 저장해야 합니다.
