---
title: "PyTorch 텐서 살펴보기"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)PyTorch_텐서_살펴보기"
source_path: "12_Deep_Learning/Code_Snippets/(실습)PyTorch_텐서_살펴보기.md"
excerpt: "PyTorch 텐서 살펴보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 텐서의 형태 바꾸기, 텐서만들기, data 타입 순서로 핵심 장면을 먼저 훑고, 텐서의 변환과 연산, Quiz., 텐서의 형태 바꾸기 같은 코드로 실제 구현을 이어서 확인할..."
research_summary: "PyTorch 텐서 살펴보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 텐서의 형태 바꾸기, 텐서만들기, data 타입 순서로 핵심 장면을 먼저 훑고, 텐서의 변환과 연산, Quiz., 텐서의 형태 바꾸기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 119개 코드 블록, 117개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다."
research_artifacts: "md · 코드 119개 · 실행 117개"
code_block_count: 119
execution_block_count: 117
research_focus:
  - "텐서의 형태 바꾸기"
  - "텐서만들기"
  - "data 타입"
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

PyTorch 텐서 살펴보기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 텐서의 형태 바꾸기, 텐서만들기, data 타입 순서로 핵심 장면을 먼저 훑고, 텐서의 변환과 연산, Quiz., 텐서의 형태 바꾸기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 119개 코드 블록, 117개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: 텐서의 형태 바꾸기, 텐서만들기, data 타입.

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

### 텐서의 형태 바꾸기

view() & contiguous 개념 view() 메소드처럼 메모리를 공유하면서 텐서 형태를 바꾸려면, 텐서 값이 연속된 메모리 공간에 존재해야 합니다. PyTorch에서는 연속된 메모리를 갖는 텐서를 contiguous하다고 표현해요. 즉, contiguous한 텐서에서만 view() 메소드를 사용할 수 있는 겁니다.

- 읽을 포인트: 텐서의 형태 바꾸기 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 텐서만들기

텐서만들기 코드를 직접 따라가며 텐서만들기 흐름을 확인했습니다.

- 읽을 포인트: 텐서만들기 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### data 타입

data 타입 코드를 직접 따라가며 data 타입 흐름을 확인했습니다.

- 읽을 포인트: data 타입 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 특수한 텐서 생성 함수

Quiz. 같은 코드를 직접 따라가며 특수한 텐서 생성 함수 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Quiz.

#### Quiz.

파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다. 이 두 데이터를 PyTorch 텐서로 만들어 주세요. data_list에서 만든 텐서는 tensor_from_list 변수에 저장하고, data_np에서 만든 텐서는 tensor_from_np...

### 텐서의 변환과 연산

브로드캐스팅 동작원리, Quiz. 같은 코드를 직접 따라가며 텐서의 변환과 연산 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 브로드캐스팅 동작원리, Quiz.

#### 브로드캐스팅 동작원리

크기가 1인 차원의 추가 : 차원 수가 적은 텐서는 차원 수가 많은 텐서와 맞추기 위해 크기가 1인 차원을 앞에 추가합니다. 2. 크기가 1인 차원의 확장 : 확장된 텐서에서 크기가 1인 차원은 상대 텐서에 맞춰 값이 복사됩니다.

#### Quiz.

실습 설명 세 개의 텐서 tensor0, tensor1, tensor2가 주어져 있습니다. 다음 단계를 따라 코드를 작성해 주세요. tensor0과 tensor1을 더합니다. 2. 1번 결과와 tensor2를 행렬곱합니다. 3. 2번 결과에서 첫 번째 열에는 2를 더하고, 두 번째...

### 여러 텐서 합치기

여러 텐서 합치기 코드를 직접 따라가며 여러 텐서 합치기 흐름을 확인했습니다.

- 읽을 포인트: 여러 텐서 합치기 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

## Why This Matters

### 표현 학습과 학습 루프

- 왜 필요한가: 딥러닝은 모델 구조만 보는 것이 아니라 입력 텐서, 손실, optimizer가 함께 어떻게 맞물리는지 이해해야 합니다.
- 왜 이 방식을 쓰는가: 그래서 이 아카이브는 모델 정의뿐 아니라 DataLoader와 학습 루프 코드를 같이 남기는 쪽으로 정리했습니다.
- 원리: 입력이 층을 통과하며 표현으로 바뀌고, 손실의 기울기가 역전파되어 가중치가 조금씩 조정되는 구조입니다.

## Implementation Flow

1. 텐서의 형태 바꾸기: view() & contiguous 개념 view() 메소드처럼 메모리를 공유하면서 텐서 형태를 바꾸려면, 텐서 값이 연속된 메모리 공간에 존재해야 합니다. PyTorch에서는 연속된 메모리를 갖는 텐서를 contiguous하다고 표현해요....
2. 텐서만들기: 텐서만들기 코드를 직접 따라가며 텐서만들기 흐름을 확인했습니다.
3. data 타입: data 타입 코드를 직접 따라가며 data 타입 흐름을 확인했습니다.
4. 특수한 텐서 생성 함수: Quiz.
5. 텐서의 변환과 연산: 브로드캐스팅 동작원리, Quiz.
6. 여러 텐서 합치기: 여러 텐서 합치기 코드를 직접 따라가며 여러 텐서 합치기 흐름을 확인했습니다.

## Code Highlights

### 텐서의 변환과 연산

`텐서의 변환과 연산`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
a = torch.tensor(
    [
        [1,2],
        [3,4],
        [5,6],
        [7,8]
    ]
)

b = torch.tensor(
    [
        [1,0,0],
        [0,0,1],
        [1,1,0]]
)
print(f'a의 열개수 : {a.shape[1]}')
print(f'b의 행개수 : {b.shape[0]}')
```

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

### 텐서의 형태 바꾸기

`텐서의 형태 바꾸기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 이미지 처리시에 차원 변경 (H W C)--> (C H W), img_np = numpy --> (256,128,3) 흐름이 주석과 함께 드러납니다.

```python
# 이미지 처리시에 차원 변경 (H W C)--> (C H W)
# img_np = numpy --> (256,128,3)
img = torch.randn(256,128,3)
tensor_img = img.permute(2, 0, 1)
print(tensor_img.shape)
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
