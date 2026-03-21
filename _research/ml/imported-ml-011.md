---
title: "코딩실습11 10.결정트리와 앙상블(RF)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습11_10.결정트리와 앙상블(RF)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md"
excerpt: "코딩실습11 10.결정트리와 앙상블(RF)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 단일 디시전 트리 실습, 랜덤 포레스트 실습 순서로 큰 장을 먼저 훑고, 단일 디시전 트리 실습, 랜덤 포레스트 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습..."
research_summary: "코딩실습11 10.결정트리와 앙상블(RF)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 단일 디시전 트리 실습, 랜덤 포레스트 실습 순서로 큰 장을 먼저 훑고, 단일 디시전 트리 실습, 랜덤 포레스트 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 16개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn, graphviz입니다."
research_artifacts: "ipynb/md · 코드 16개 · 실행 16개"
code_block_count: 16
execution_block_count: 16
research_focus:
  - "단일 디시전 트리 실습"
  - "랜덤 포레스트 실습"
  - "make_moons 데이터 불러오기 - 암기 X"
research_stack:
  - "numpy"
  - "matplotlib"
  - "sklearn"
  - "graphviz"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

## 글 한눈에 보기

| 항목 | 내용 |
|------|------|
| 문제 설정 | 코딩실습11 10.결정트리와 앙상블(RF)에서 단일 디시전 트리 실습, 랜덤 포레스트 실습 흐름을 직접 따라가며 구현했습니다. |
| 원본 구조 | 단일 디시전 트리 실습 -> 랜덤 포레스트 실습 |
| 데이터 맥락 | make_moons 데이터 불러오기 - 암기 X |
| 주요 장 | 단일 디시전 트리 실습 · 랜덤 포레스트 실습 |
| 구현 흐름 | 단일 디시전 트리 실습 -> 랜덤 포레스트 실습 -> import numpy as np |
| 자료 | ipynb / md · 코드 16 · 실행 16 |
| 주요 스택 | numpy, matplotlib, sklearn, graphviz |

## 원본 노트 흐름

### 단일 디시전 트리 실습

make_moons 데이터 불러오기..., 데이터셋 시각화 (어떻게 생겼는지..., 정확도 계산 같은 코드를 직접 따라가며 단일 디시전 트리 실습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: make_moons 데이터 불러오기 - 암기 X, 데이터셋 시각화 (어떻게 생겼는지 눈으로 확인), 정확도 계산

#### make_moons 데이터 불러오기 - 암기 X

단일 디시전 트리 실습 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

#### 데이터셋 시각화 (어떻게 생겼는지 눈으로 확인)

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

#### 정확도 계산

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

### 랜덤 포레스트 실습

n_estimators 중요! 같은 코드를 직접 따라가며 랜덤 포레스트 실습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: n_estimators 중요!

#### n_estimators 중요!

RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

## 구현 흐름

### 1. 단일 디시전 트리 실습

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: `matplotlib`
- 코드 포인트: 산점도 시각화할 함수 정의 · 컬러맵 정의

### 2. 랜덤 포레스트 실습

- 단계: 모델 구성
- 구현 의도: RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: `RandomForest`
- 코드 포인트: n_estimators 중요!

### 3. import numpy as np

- 단계: 환경 준비
- 구현 의도: 넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.
- 핵심 API: `train_test_split`, `DecisionTree`, `RandomForest`, `accuracy_score`
- 코드 포인트: -

## 코드로 확인한 내용

### 단일 디시전 트리 실습

**직접 해본 단계**: 피처 가공

**핵심 API**: `matplotlib`

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
# 산점도 시각화할 함수 정의

def plot_decision_boundary(model, X, y, title="Decision Boundary"):
    # 컬러맵 정의
    cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])  # 배경 색
    cmap_bold = ListedColormap(['#FF0000', '#0000FF'])   # 점 색

    # 그리드 영역 설정
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    # 모델로 예측한 결정 경계
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # 시각화
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=cmap_light)  # 결정 경계 색
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=30)
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.grid(True)
    plt.show()
```

### 랜덤 포레스트 실습

**직접 해본 단계**: 모델 구성

**핵심 API**: `RandomForest`

RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=5, n_jobs=-1)
# n_estimators 중요!
rf_clf.fit(X_train, y_train)
```

### import numpy as np

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `DecisionTree`, `RandomForest`, `accuracy_score`

넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap              # 결정 경계 시각화위한 라이브러리
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습11_10.결정트리와 앙상블(RF).ipynb`, `250827_코딩실습11_10.결정트리와 앙상블(RF).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## 원문 미리보기

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
