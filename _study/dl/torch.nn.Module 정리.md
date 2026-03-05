---
title: "torch.nn.Module 정리"
date: 2025-09-12
study_tab: "DL"
tags:
  - DL
  - PyTorch
  - nn.Module
  - Deep-Learning-Basics
excerpt: "torch.nn.Module의 정의, 역할, 코드 구조, nn.functional과의 차이를 한 번에 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

## 1. 정의

- PyTorch에서 딥러닝 모델을 설계/학습하는 기반 클래스
- 신경망 계층, 활성화 함수, 손실 함수 등 구성 요소를 포함
- 사용자 정의 모델은 보통 `nn.Module`을 상속해 구현

## 2. 주요 역할

### 신경망 구축 및 학습 지원

- 레이어: `nn.Linear`, `nn.Conv2d`, `nn.LSTM`
- 활성화: `nn.ReLU`, `nn.Sigmoid`, `nn.Softmax`
- 손실 함수: `nn.MSELoss`, `nn.CrossEntropyLoss`
- 정규화: `nn.BatchNorm1d/2d`, `nn.LayerNorm`

### 사용자 정의 모델 설계

- `__init__`: 모델 구조(레이어/파라미터) 정의
- `forward`: 입력 데이터의 연산 흐름 정의
- `super().__init__()` 호출로 부모 클래스 초기화

### 파라미터 관리

- 가중치/편향 자동 추적
- `.parameters()`로 학습 파라미터 제공
- `.to(device)` / `.cuda()`로 장치 전환

## 3. 코드 구성 방식

### 기본 예시

```python
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
```

- `__init__`: 레이어 정의
- `forward`: 입력→연산→출력
- `model(x)` 호출 시 `forward`가 자동 실행

### 모듈 중첩과 블록화

- `nn.Sequential`로 여러 레이어를 블록처럼 묶기 가능
- 다른 `nn.Module`을 서브모듈로 포함해 계층적 설계 가능

## 4. nn.Module vs torch.nn.functional

| 구분 | `nn.Module` | `torch.nn.functional` |
|---|---|---|
| 형태 | 클래스 기반 | 함수 기반 |
| 파라미터 | 학습 가능한 파라미터 포함 가능 | 파라미터 없음(연산 함수 중심) |
| 사용 예 | `nn.Linear`, `nn.Conv2d` | `F.relu`, `F.softmax` |
| 장점 | 구조화/재사용/파라미터 관리 용이 | 가볍고 유연한 연산 구성 |

## 5. 핵심 요약

- `torch.nn.Module`은 딥러닝 모델의 설계도 역할
- 구조 정의 + 파라미터 관리 + 모듈화 지원
- `__init__`에서 재료(레이어)를 정의하고 `forward`에서 조리법(연산 흐름)을 작성

## 생각해볼 질문

- Q1. `nn.Module`을 상속하지 않고 모델을 만들면 어떤 불편함이 생길까?
- Q2. `nn.Sequential` 기반 구성과 직접 `forward` 구현 방식의 차이는?
- Q3. `torch.nn.functional`만으로 모델 구현이 가능하다면 장단점은?

