---
title: "PyTorch 텐서 살펴보기"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_텐서_살펴보기"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_텐서_살펴보기.md"
excerpt: "파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다"
research_summary: "파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다. 이 두 데이터를 PyTorch 텐서로 만들어 주세요. 크기가 1인 차원의 추가 : 차원 수가 적은 텐서는 차원 수가 많은 텐서와 맞추기 위해 크기가 1인 차원을 앞에 추가합니다. 2. 크기가 1인 차원의 확장 : 확장된 텐서에서 크기가 1인 차원은 상대 텐서에 맞춰 값이 복사됩니다. `md` 원본과 119개 코드 블록, 117개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다."
research_artifacts: "md · 코드 119개 · 실행 117개"
code_block_count: 119
execution_block_count: 117
research_focus:
  - "텐서만들기"
  - "data 타입"
  - "특수한 텐서 생성 함수"
research_stack:
  - "torch"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다. 이 두 데이터를 PyTorch 텐서로 만들어 주세요. 크기가 1인 차원의 추가 : 차원 수가 적은 텐서는 차원 수가 많은 텐서와 맞추기 위해 크기가 1인 차원을 앞에 추가합니다. 2. 크기가 1인 차원의 확장 : 확장된 텐서에서 크기가 1인 차원은 상대 텐서에 맞춰 값이 복사됩니다. `md` 원본과 119개 코드 블록, 117개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: 텐서만들기, data 타입, 특수한 텐서 생성 함수.

**남겨둔 자료**: `md` 원본과 119개 코드 블록, 117개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다.

**주요 스택**: `torch`, `numpy`

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

## What This Note Covers

### Quiz.

파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다. 이 두 데이터를 PyTorch 텐서로 만들어 주세요.

### 브로드캐스팅 동작원리

크기가 1인 차원의 추가 : 차원 수가 적은 텐서는 차원 수가 많은 텐서와 맞추기 위해 크기가 1인 차원을 앞에 추가합니다. 2. 크기가 1인 차원의 확장 : 확장된 텐서에서 크기가 1인 차원은 상대 텐서에 맞춰 값이 복사됩니다.

### 텐서의 형태 바꾸기

view() & contiguous 개념

### Key Step

방법 1 : torch.tensor()

## Implementation Flow

1. Quiz.: 파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다. 이 두 데이터를 PyTorch 텐서로 만들어 주세요.
2. 브로드캐스팅 동작원리: 크기가 1인 차원의 추가 : 차원 수가 적은 텐서는 차원 수가 많은 텐서와 맞추기 위해 크기가 1인 차원을 앞에 추가합니다. 2. 크기가 1인 차원의 확장 : 확장된 텐서에서 크기가 1인 차원은 상대 텐서에 맞춰 값이 복사됩니다.
3. 텐서의 형태 바꾸기: view() & contiguous 개념
4. Key Step: 방법 1 : torch.tensor()

## Code Highlights

### Quiz.

`Quiz.`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 여기에 코드를 작성하세요., [[4,-4] [[2 -2], [-2 2]] [2 -2]] 흐름이 주석과 함께 드러납니다.

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

`여러 텐서 합치기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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
