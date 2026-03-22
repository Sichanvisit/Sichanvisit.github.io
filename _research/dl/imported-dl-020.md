---
title: "PyTorch 텐서 살펴보기 - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "3-1_PyTorch_텐서_살펴보기 - 공유"
source_path: "12_Deep_Learning/Code_Snippets/3-1_PyTorch_텐서_살펴보기 - 공유.md"
excerpt: "PyTorch 텐서 살펴보기 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 특수한 텐서 생성 함수, 텐서만들기, 브로드캐스팅 순서로 핵심 장면을 먼저 훑고, 브로드캐스팅, 브로드캐스팅 동작원리, 브로드캐스팅이 불가능한 경우 같은 코드로 실제..."
research_summary: "PyTorch 텐서 살펴보기 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 특수한 텐서 생성 함수, 텐서만들기, 브로드캐스팅 순서로 핵심 장면을 먼저 훑고, 브로드캐스팅, 브로드캐스팅 동작원리, 브로드캐스팅이 불가능한 경우 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 127개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다."
research_artifacts: "md · 코드 127개 · 실행 95개"
code_block_count: 127
execution_block_count: 95
research_focus:
  - "특수한 텐서 생성 함수"
  - "텐서만들기"
  - "브로드캐스팅"
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

PyTorch 텐서 살펴보기 - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 특수한 텐서 생성 함수, 텐서만들기, 브로드캐스팅 순서로 핵심 장면을 먼저 훑고, 브로드캐스팅, 브로드캐스팅 동작원리, 브로드캐스팅이 불가능한 경우 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 127개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: 특수한 텐서 생성 함수, 텐서만들기, 브로드캐스팅.

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

### 특수한 텐서 생성 함수

PyTorch를 사용하다 보면 특수한 텐서를 만들어야 할 때가 생깁니다. 예를 들어 모든 값을 랜덤하게 초기화할 수도 있고요. 텐서의 모든 값을 0이나 1로 만들 때도 있죠. 이런 경우에 사용할 수 있는 함수를 몇 가지 살펴봅시다.

- 읽을 포인트: 세부 흐름: 랜덤한 값으로 만들기, 특정한 값으로 만들기, Quiz.

#### 랜덤한 값으로 만들기

랜덤한 값으로 텐서를 만드는 가장 대표적인 함수는 rand()입니다. 원하는 형태를 입력하면 0과 1 사이의 균등 분포를 바탕으로 난수 텐서가 만들어져요. 텐서 형태는 콤마로 숫자를 구분하여 입력해도 되고, 리스트나 튜플로 모아서 입력해도 됩니다. 만약 min_val과 max_va...

#### 특정한 값으로 만들기

zeros() 함수에 원하는 형태를 입력하면 값이 전부 0인 텐서를 만들 수 있습니다. 그 외의 값을 원한다면 full() 함수에 원하는 형태를 리스트나 튜플로 입력하고, 이어서 어떤 값으로 텐서를 채울지도 입력하면 됩니다.

#### Quiz.

파이썬 리스트 data_list와 NumPy array data_np가 주어져 있습니다. 이 두 데이터를 PyTorch 텐서로 만들어 주세요. data_list에서 만든 텐서는 tensor_from_list 변수에 저장하고, data_np에서 만든 텐서는 tensor_from_np...

### 텐서만들기

Python 리스트를 PyTorch 텐서로 변환하려면 torch.tensor() 함수를 사용합니다. 변환된 텐서는 리스트와 동일한 값을 가지며, tensor() 함수를 통해 PyTorch의 텐서 객체로 만들어집니다

- 읽을 포인트: 세부 흐름: 데이터 타입 지정하기, 데이터 타입 변환하기

#### 데이터 타입 지정하기

PyTorch 텐서는 숫자로 구성된 다차원 배열이며, 텐서 내 모든 숫자는 동일한 데이터 타입을 가집니다. 기본 정수 타입은 torch.int64, 기본 실수 타입은 torch.float32입니다. dtype 매개변수를 사용하여 텐서의 데이터 타입을 명시적으로 설정할 수 있습니다.

#### 데이터 타입 변환하기

.to() 메서드 사용하기 : to() 메서드는 PyTorch에서 가장 일반적으로 사용되는 방식입니다. 장치(Device) 전환과 데이터 타입 변경 모두에 사용 가능합니다. .float(), .int(), .long() 등 메서드 사용

### 브로드캐스팅

PyTorch에서 텐서 연산을 수행할 때, 두 텐서의 shape가 반드시 같을 필요는 없습니다. 셰이프가 다른 텐서 간 연산을 자동으로 처리해 주는 기능이 바로 브로드캐스팅입니다.

- 읽을 포인트: 세부 흐름: 브로드캐스팅 동작원리, 브로드캐스팅이 불가능한 경우, Quiz.

#### 브로드캐스팅 동작원리

크기가 1인 차원의 추가 : 차원 수가 적은 텐서는 차원 수가 많은 텐서와 맞추기 위해 크기가 1인 차원을 앞에 추가합니다. 2. 크기가 1인 차원의 확장 : 확장된 텐서에서 크기가 1인 차원은 상대 텐서에 맞춰 값이 복사됩니다. 출처 : https://deeplearninguni...

#### 브로드캐스팅이 불가능한 경우

브로드캐스팅은 모든 경우에 적용되는 것이 아닙니다. 셰이프가 서로 호환되지 않을 경우 연산이 불가능합니다.

#### Quiz.

실습 설명 세 개의 텐서 tensor0, tensor1, tensor2가 주어져 있습니다. 다음 단계를 따라 코드를 작성해 주세요. tensor0과 tensor1을 더합니다. 2. 1번 결과와 tensor2를 행렬곱합니다. 3. 2번 결과에서 첫 번째 열에는 2를 더하고, 두 번째...

### 텐서의 형태 바꾸기

PyTorch를 사용하다 보면 텐서의 값은 그대로 유지하면서 형태를 바꿔야 하는 경우가 생깁니다. 예를 들어, 다차원 텐서를 1차원으로 펼치거나, 차원을 추가하거나, 불필요한 차원을 제거해야 할 때가 있습니다.

- 읽을 포인트: 세부 흐름: reshape 메소드, squeeze() 메소드, unsqueeze() 메소드

#### reshape 메소드

reshape() 메소드는 텐서의 값을 그대로 두면서 형태를 변경할 수 있습니다. 원소 개수가 일치하지 않는 형태로 변환하려 하면 에러가 발생합니다.

#### squeeze() 메소드

squeeze() 메소드는 크기가 1인 차원을 제거합니다. 특정 차원만 제거하려면 차원의 인덱스를 입력합니다.

#### unsqueeze() 메소드

unsqueeze() 메소드는 크기가 1인 차원을 추가합니다.

### 여러 텐서 합치기

PyTorch를 사용하다 보면 여러 텐서를 하나로 합쳐야 하는 경우가 자주 있습니다. 이번 섹션에서는 이를 위한 두 가지 주요 함수, cat()과 stack()을 살펴보겠습니다.

- 읽을 포인트: 세부 흐름: cat() 함수, stack() 함수, cat() vs stack() 요약

#### cat() 함수

cat() 함수는 여러 텐서를 특정 차원에 따라 이어 붙이는 함수입니다. 이 과정을 컨캐터네이트(concatenate)라고도 부릅니다.

#### stack() 함수

stack() 함수는 여러 텐서를 특정 차원에 따라 쌓는 함수입니다. cat() 함수와 달리, 결과 텐서에는 새로운 차원이 추가됩니다.

#### cat() vs stack() 요약

여러 텐서 합치기 > cat() vs stack() 요약에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### (심화) view() 메소드와 contiguous 개념

view() 메소드도 reshape() 메소드와 마찬가지로 전체 원소 개수를 유지하면서 텐서의 형태를 바꿀 때 사용합니다. 즉, 아래처럼 3x4 텐서가 있다고 하면, 원소 개수가 12개인 형태로 자유롭게 바꿀 수 있습니다. view() 메소드에서도 -1을 넣어 준 차원의 크기는 전체 원소 개수와 나머지 차원의 크기를 고려해 자동으로...

- 읽을 포인트: 세부 흐름: Contiguous란?, transpose() 메소드

#### Contiguous란?

view() 메소드처럼 메모리를 공유하면서 텐서 형태를 바꾸려면, 텐서 값이 연속된 메모리 공간에 존재해야 합니다. PyTorch에서는 연속된 메모리를 갖는 텐서를 contiguous하다고 표현해요. 즉, contiguous한 텐서에서만 view() 메소드를 사용할 수 있는 겁니다...

#### transpose() 메소드

torch.transpose()를 이용하여 특정 dimension을 변경할 수 있습니다.

## Why This Matters

### 표현 학습과 학습 루프

- 왜 필요한가: 딥러닝은 모델 구조만 보는 것이 아니라 입력 텐서, 손실, optimizer가 함께 어떻게 맞물리는지 이해해야 합니다.
- 왜 이 방식을 쓰는가: 그래서 이 아카이브는 모델 정의뿐 아니라 DataLoader와 학습 루프 코드를 같이 남기는 쪽으로 정리했습니다.
- 원리: 입력이 층을 통과하며 표현으로 바뀌고, 손실의 기울기가 역전파되어 가중치가 조금씩 조정되는 구조입니다.

## Implementation Flow

1. 특수한 텐서 생성 함수: 랜덤한 값으로 만들기, 특정한 값으로 만들기
2. 텐서만들기: 데이터 타입 지정하기, 데이터 타입 변환하기
3. 브로드캐스팅: 브로드캐스팅 동작원리, 브로드캐스팅이 불가능한 경우
4. 텐서의 형태 바꾸기: reshape 메소드, squeeze() 메소드
5. 여러 텐서 합치기: cat() 함수, stack() 함수
6. (심화) view() 메소드와 contiguous 개념: Contiguous란?, transpose() 메소드

## Code Highlights

### 브로드캐스팅

`브로드캐스팅`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 이 두 텐서를 더하면 어떻게 될까요?

```python
a = torch.tensor(
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
)
b = torch.tensor(
    [1, -1, 2],
)

print(f'a의 shape: {a.shape}')
print(f'b의 shape: {b.shape}')
```

### 브로드캐스팅 동작원리

`브로드캐스팅 동작원리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 출처 : https://deeplearninguniversity.com/pytorch/pytorch-broadcasting/.

```python
a = torch.tensor(
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
)
b = torch.tensor(
    [1, -1, 2],
)

print(f'a의 shape: {a.shape}')
print(f'b의 shape: {b.shape}')
```

### 브로드캐스팅이 불가능한 경우

`브로드캐스팅이 불가능한 경우`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 셰이프가 서로 호환되지 않을 경우 연산이 불가능합니다.

```python
a = torch.tensor(
    [
        [1, 2, 3],
        [4, 5, 6],
    ]
)
b = torch.tensor(
    [1, -1],
)

print(f'a의 shape: {a.shape}')
print(f'b의 shape: {b.shape}')
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
