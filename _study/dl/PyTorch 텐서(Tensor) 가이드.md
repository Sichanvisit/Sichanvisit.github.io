---
title: "PyTorch 텐서(Tensor) 완벽 가이드: NumPy와의 차이부터 실무 활용까지"
date: 2026-03-05
study_tab: "DL"
tags:
  - DL
  - PyTorch
  - Tensor
  - NumPy
  - Autograd
  - GPU
excerpt: "PyTorch 텐서의 핵심 개념, NumPy와의 차이, 자동 미분과 GPU 활용, 실무 주의사항을 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

딥러닝에서 텐서(Tensor)는 단순한 다차원 배열을 넘어, 학습/추론의 핵심 데이터 구조입니다.  
PyTorch 텐서는 NumPy와 유사한 인터페이스를 제공하면서도 자동 미분, GPU 가속, 장치 이동 등 딥러닝에 특화된 기능을 제공합니다.

## 1. 텐서의 정의와 기본 속성

텐서는 숫자로 이루어진 다차원 배열입니다.

- 스칼라(0차원): `torch.tensor(3)`
- 벡터(1차원): `[1, 2, 3]`
- 행렬(2차원): `[[1, 2], [3, 4]]`
- 고차원(3차원 이상): 이미지/시계열/비디오

```python
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(x.ndim)   # 2
print(x.shape)  # torch.Size([2, 3])
print(x.dtype)  # torch.int64
```

## 2. 데이터 타입과 변환

```python
a = torch.tensor([1.0, 2.0], dtype=torch.float32)
b = torch.tensor([1, 2, 3], dtype=torch.int64)

print(b.float())  # int -> float
print(a.int())    # float -> int
```

- 딥러닝 학습 기본 dtype은 보통 `float32`
- 혼합정밀도 학습에서 `float16`/`bfloat16`도 활용

## 3. 메모리 공유와 생성 방식

```python
import numpy as np
arr = np.array([1, 2, 3])
t1 = torch.tensor(arr)         # 복사(메모리 공유 X)
t2 = torch.from_numpy(arr)     # 메모리 공유 O

arr[0] = 99
print(t1)  # tensor([1, 2, 3])
print(t2)  # tensor([99, 2, 3])
```

- `torch.tensor()`: 안전한 복사
- `torch.from_numpy()`: 복사 비용 절약(공유)
- `torch.as_tensor()`: 공유 가능한 경우 공유

## 4. 장치(Device)와 GPU 활용

```python
x = torch.rand(1000, 1000)
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = x.to(device)
```

주의:
- 연산하는 텐서는 같은 장치(CPU/GPU)에 있어야 함
- 대규모 연산에서 GPU 사용 시 큰 속도 이점

## 5. 자동 미분 (Autograd)

```python
x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3*x + 1
y.backward()
print(x.grad)  # 7
```

- `requires_grad=True`인 텐서 연산은 그래프로 추적
- `backward()` 호출 시 기울기 자동 계산
- NumPy는 기본적으로 자동 미분 미지원

## 6. 텐서 연산과 브로드캐스팅

```python
a = torch.tensor([1, 2, 3])
b = torch.tensor([[10], [20], [30]])
print(a + b)
```

출력:

```text
tensor([[11, 12, 13],
        [21, 22, 23],
        [31, 32, 33]])
```

- 차원이 달라도 규칙에 맞으면 자동 확장
- 배치 이미지 텐서 처리에서 자주 활용

## 7. PyTorch Tensor vs NumPy Array

| 특징 | NumPy Array | PyTorch Tensor |
|---|---|---|
| 연산 장치 | CPU 중심 | CPU + GPU |
| 자동 미분 | 기본 미지원 | Autograd 지원 |
| 메모리 공유 | 자체 배열 | NumPy와 공유 가능 |
| 딥러닝 최적화 | 일반 수치 계산 | 학습/추론 최적화 |
| 브로드캐스팅 | 지원 | 지원 |
| 배포 확장 | 제한적 | TorchScript/ONNX 활용 가능 |

## 마무리

PyTorch 텐서는 NumPy의 직관성을 유지하면서도, 딥러닝 실전에 필요한 자동 미분과 GPU 가속을 제공합니다.  
딥러닝 학습/연구를 위해서는 텐서의 dtype, device, 메모리 공유, autograd 동작을 정확히 이해하는 것이 필수입니다.

## 다음 확장 아이디어

- Q1. Autograd 내부 그래프 구조와 역전파 동작을 시각적으로 정리
- Q2. MNIST 이미지 텐서 변환/전처리 실무 예시 추가
- Q3. NumPy vs PyTorch 텐서 속도 비교 벤치마크 실험

