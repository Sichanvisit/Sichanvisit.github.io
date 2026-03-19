---
title: "PyTorch 텐서 살펴보기 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-1_PyTorch_텐서_살펴보기 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-1_PyTorch_텐서_살펴보기 - 공유.md"
excerpt: "Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다"
research_summary: "Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다. PyTorch 텐서는 숫자로 구성된 다차원 배열이며, 텐서 내 모든 숫자는 동일한 데이터 타입을 가집니다. 기본 정수 타입은 torch.int64, 기본 실수 타입은 torch.float32입니다. `md` 원본과 127개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다."
research_artifacts: "md · 코드 127개 · 실행 95개"
code_block_count: 127
execution_block_count: 95
research_focus:
  - "Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다."
  - "텐서만들기"
  - "PyTorch 텐서는 숫자로 구성된 다차원 배열이며, 텐서 내 모든 숫자는 동일한 데이터 타입을 가집니..."
research_stack:
  - "torch"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다. PyTorch 텐서는 숫자로 구성된 다차원 배열이며, 텐서 내 모든 숫자는 동일한 데이터 타입을 가집니다. 기본 정수 타입은 torch.int64, 기본 실수 타입은 torch.float32입니다. `md` 원본과 127개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: Python 리스트를 PyTorch 텐서로 변환하려면 torch.ten..., 텐서만들기, PyTorch 텐서는 숫자로 구성된 다차원 배열이며, 텐서 내 모든 숫....

**남겨둔 자료**: `md` 원본과 127개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다.

**주요 스택**: `torch`, `numpy`

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

## What This Note Covers

### 텐서만들기

Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다.

### 데이터 타입 지정하기

PyTorch 텐서는 숫자로 구성된 다차원 배열이며, 텐서 내 모든 숫자는 동일한 데이터 타입을 가집니다. 기본 정수 타입은 torch.int64, 기본 실수 타입은 torch.float32입니다.

### 데이터 타입 변환하기

.to() 메서드 사용하기 : to() 메서드는 PyTorch에서 가장 일반적으로 사용되는 방식입니다. 장치(Device) 전환과 데이터 타입 변경 모두에 사용 가능합니다.

### 특수한 텐서 생성 함수

PyTorch를 사용하다 보면 특수한 텐서를 만들어야 할 때가 생깁니다. 예를 들어 모든 값을 랜덤하게 초기화할 수도 있고요. 텐서의 모든 값을 0이나 1로 만들 때도 있죠. 이런 경우에 사용할 수 있는 함수를 몇 가지 살펴봅시다.

## Implementation Flow

1. 텐서만들기: Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다.
2. 데이터 타입 지정하기: PyTorch 텐서는 숫자로 구성된 다차원 배열이며, 텐서 내 모든 숫자는 동일한 데이터 타입을 가집니다. 기본 정수 타입은 torch.int64, 기본 실수 타입은 torch.float32입니다.
3. 데이터 타입 변환하기: .to() 메서드 사용하기 : to() 메서드는 PyTorch에서 가장 일반적으로 사용되는 방식입니다. 장치(Device) 전환과 데이터 타입 변경 모두에 사용 가능합니다.
4. 특수한 텐서 생성 함수: PyTorch를 사용하다 보면 특수한 텐서를 만들어야 할 때가 생깁니다. 예를 들어 모든 값을 랜덤하게 초기화할 수도 있고요. 텐서의 모든 값을 0이나 1로 만들 때도 있죠. 이런 경우에 사용할 수 있는 함수를 몇 가지 살펴봅시다.

## Code Highlights

### Tensor의 연산

`Tensor의 연산`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 곱셈하려는 두 텐서의 차원이 적합해야 합니다.

```python
a = torch.tensor(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8],
    ]
)
b = torch.tensor(
    [
        [1, 0, 0],
        [0, 0, 1],
        [1, 1, 0],
    ]
)

print(f'a의 열 개수: {a.shape[1]}')
print(f'b의 행 개수: {b.shape[0]}')
```

### Quiz.

`Quiz.`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 여기에 코드를 작성하세요., 테스트 코드 흐름이 주석과 함께 드러납니다.

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
