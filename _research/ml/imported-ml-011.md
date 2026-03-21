---
title: "코딩실습11 10.결정트리와 앙상블(RF)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습11_10.결정트리와 앙상블(RF)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md"
excerpt: "단일 디시전 트리 실습, 랜덤 포레스트 실습, make_moons 데이터 불러오기 - 암기 X 중심으로 구현 과정을 정리한 코딩실습11 10.결정트리와 앙상블(RF) 기록입니다"
research_summary: "단일 디시전 트리 실습, 랜덤 포레스트 실습, make_moons 데이터 불러오기 - 암기 X 중심으로 구현 과정을 정리한 코딩실습11 10.결정트리와 앙상블(RF) 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 16개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn, graphviz입니다."
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

단일 디시전 트리 실습, 랜덤 포레스트 실습, make_moons 데이터 불러오기 - 암기 X 중심으로 구현 과정을 정리한 코딩실습11 10.결정트리와 앙상블(RF) 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 16개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn, graphviz입니다.

**빠르게 볼 수 있는 포인트**: 단일 디시전 트리 실습, 랜덤 포레스트 실습, make_moons 데이터 불러오기 - 암기 X.

**남겨둔 자료**: `ipynb/md` 원본과 16개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn, graphviz입니다.

**주요 스택**: `numpy`, `matplotlib`, `sklearn`, `graphviz`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 16 |
| Execution Cells | 16 |
| Libraries | `numpy`, `matplotlib`, `sklearn`, `graphviz` |
| Source Note | `250827_코딩실습11_10.결정트리와 앙상블(RF)` |

## What I Studied

- 단일 디시전 트리 실습
- 랜덤 포레스트 실습
- make_moons 데이터 불러오기 - 암기 X
- 데이터셋 시각화 (어떻게 생겼는지 눈으로 확인)
- 정확도 계산

## What I Tried in Code

1. 피처 가공: 단일 디시전 트리 실습
2. 모델 구성: 랜덤 포레스트 실습
3. 평가: 단일 디시전 트리 실습
4. 환경 준비: import numpy as np
5. 구현 코드: 단일 디시전 트리 실습

## Code Evidence

### 단일 디시전 트리 실습

**직접 해본 단계**: 피처 가공

`단일 디시전 트리 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다. 코드에는 산점도 시각화할 함수 정의, 컬러맵 정의 같은 처리 포인트도 함께 남아 있습니다.

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

`랜덤 포레스트 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다. 코드에는 n_estimators 중요! 같은 처리 포인트도 함께 남아 있습니다.

```python
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=5, n_jobs=-1)
# n_estimators 중요!
rf_clf.fit(X_train, y_train)
```

### 단일 디시전 트리 실습

**직접 해본 단계**: 평가

`단일 디시전 트리 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다. 코드에는 정확도 계산 같은 처리 포인트도 함께 남아 있습니다.

```python
# 정확도 계산
accuracy_dt = accuracy_score(y_test, y_pred_dt)
accuracy_dt
```

### import numpy as np

**직접 해본 단계**: 환경 준비

`import numpy as np`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

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

### 단일 디시전 트리 실습

**직접 해본 단계**: 구현 코드

`단일 디시전 트리 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 make_moons 데이터 불러오기 - 암기 X 같은 처리 포인트도 함께 남아 있습니다.

```python
# make_moons 데이터 불러오기 - 암기 X
X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)
```

### 단일 디시전 트리 실습

**직접 해본 단계**: 피처 가공

`단일 디시전 트리 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다. 코드에는 추가 - 보기 좋은 시각화 같은 처리 포인트도 함께 남아 있습니다.

```python
# 추가 - 보기 좋은 시각화

from sklearn.tree import export_graphviz
import graphviz

dot_data = export_graphviz(
    dt_clf,
    feature_names=['Feature1', 'Feature2'],
    class_names=['Class0', 'Class1'],
    filled=True,
    rounded=True
)

graph = graphviz.Source(dot_data)

graph
```

## Why These Steps Matter

### 파생 변수를 직접 만든 부분

- 왜 필요한가: 원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `단일 디시전 트리 실습` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.
- 원리: 좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `랜덤 포레스트 실습`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

### 지표 계산까지 남긴 이유

- 왜 필요한가: 예측을 했더라도 어떤 기준으로 잘했는지 판단하지 않으면 실험 비교가 성립하지 않습니다.
- 왜 이 방식을 쓰는가: 그래서 `단일 디시전 트리 실습` 코드를 통해 정확도, F1, RMSLE 같은 지표를 실제로 어떻게 계산했는지 함께 남겼습니다.
- 원리: 평가 지표는 예측 결과를 수치화해 모델 선택과 개선 방향을 정하는 기준점 역할을 합니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `단일 디시전 트리 실습` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습11_10.결정트리와 앙상블(RF).ipynb`, `250827_코딩실습11_10.결정트리와 앙상블(RF).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
