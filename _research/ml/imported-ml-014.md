---
title: "코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).md"
excerpt: "시각화를 위한 헬퍼 함수 (이전 실습에서 사용..., 모델별 정확도 저장 딕셔너리, 보팅 중심으로 구현 과정을 정리한 코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹) 기록입니다"
research_summary: "시각화를 위한 헬퍼 함수 (이전 실습에서 사용..., 모델별 정확도 저장 딕셔너리, 보팅 중심으로 구현 과정을 정리한 코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹) 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다."
research_artifacts: "ipynb/md · 코드 8개 · 실행 7개"
code_block_count: 8
execution_block_count: 7
research_focus:
  - "시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)"
  - "모델별 정확도 저장 딕셔너리"
  - "보팅"
research_stack:
  - "numpy"
  - "matplotlib"
  - "sklearn"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

시각화를 위한 헬퍼 함수 (이전 실습에서 사용..., 모델별 정확도 저장 딕셔너리, 보팅 중심으로 구현 과정을 정리한 코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹) 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다.

**빠르게 볼 수 있는 포인트**: 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일), 모델별 정확도 저장 딕셔너리, 보팅.

**남겨둔 자료**: `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다.

**주요 스택**: `numpy`, `matplotlib`, `sklearn`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 8 |
| Execution Cells | 7 |
| Libraries | `numpy`, `matplotlib`, `sklearn` |
| Source Note | `250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹)` |

## What I Studied

- 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)
- 모델별 정확도 저장 딕셔너리
- 보팅
- 1-1. 기본 모델 세팅
- 1-2. 소프트 보팅

## What I Tried in Code

1. 피처 가공: 파생 변수 추가
2. 모델 구성: DecisionTree / LogisticRegression 모델 구성
3. 환경 준비: import numpy as np
4. 구현 코드: 모델별 정확도 저장 딕셔너리
5. 구현 코드: for model_name, acc in accuracies.items()
6. 구현 코드: X, y = make_moons(n_samples=1000, noise=0.3, rand...

## Code Evidence

### 파생 변수 추가

**직접 해본 단계**: 피처 가공

`파생 변수 추가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다. 코드에는 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일) 같은 처리 포인트도 함께 남아 있습니다.

```python
# 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)
def plot_decision_boundary(clf, X, y, ax, title):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00'])


    ax.contourf(xx, yy, Z, alpha=0.8, cmap=cmap_light)
    ax.scatter(X[:, 0][y==0], X[:, 1][y==0], c='red', marker='o', label='Class 0')
    ax.scatter(X[:, 0][y==1], X[:, 1][y==1], c='blue', marker='x', label='Class 1')
    ax.set_title(title)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend()
    ax.grid(True)
```

### DecisionTree / LogisticRegression 모델 구성

**직접 해본 단계**: 모델 구성

`DecisionTree / LogisticRegression 모델 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. DecisionTree / LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다. 코드에는 보팅, 1-1. 기본 모델 세팅 같은 처리 포인트도 함께 남아 있습니다.

```python
fig, axes = plt.subplots(2, 2, figsize=(12,11))
axes = axes.flatten()

# 1. 보팅
# 1-1. 기본 모델 세팅
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier(max_depth=5)
clf3 = KNeighborsClassifier(n_neighbors=5)
# 1-2. 소프트 보팅
voting_clf = VotingClassifier(
    estimators=[('lr', clf1), ('dt', clf2), ('KNN', clf3)],
    voting='soft',
    weights=[1,1,1]
)
voting_clf.fit(X_train, y_train)
y_pred_voting = voting_clf.predict(X_test)
accuracy_voting = accuracy_score(y_test, y_pred_voting)
accuracies['Voting'] = accuracy_voting
plot_decision_boundary(voting_clf, X_test, y_test, axes[0], f'Voting (Acc:{accuracy_voting:.4f})')

# 배깅
bagging_clf = BaggingClassifier(
    estimator=DecisionTreeClassifier(max_depth=5),
    n_estimators=100,
    max_samples=0.7,                                             # 각 트리가 훈련 데이터의 70% 사용 (중복 허용)
    bootstrap=True
)
bagging_clf.fit(X_train, y_train)
y_pred_bagging = bagging_clf.predict(X_test)
accuracy_bagging = accuracy_score(y_test, y_pred_bagging)
accuracies['Bagging'] = accuracy_bagging
plot_decision_boundary(bagging_clf, X_test, y_test, axes[1], f'Bagging (Acc:{accuracy_bagging:.4f})')

# 3. 부스팅
gb_clf = GradientBoostingClassifier(
    n_estimators=100,
# ... trimmed ...
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
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaggingClassifier, VotingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
```

### 모델별 정확도 저장 딕셔너리

**직접 해본 단계**: 구현 코드

`모델별 정확도 저장 딕셔너리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 모델별 정확도 저장 딕셔너리 같은 처리 포인트도 함께 남아 있습니다.

```python
# 모델별 정확도 저장 딕셔너리
accuracies ={}
```

### for model_name, acc in accuracies.items():

**직접 해본 단계**: 구현 코드

`for model_name, acc in accuracies.items():`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
for model_name, acc in accuracies.items():
    print(f'{model_name}: {acc:.4f}')
```

### X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)

**직접 해본 단계**: 구현 코드

`X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)
```

## Why These Steps Matter

### 파생 변수를 직접 만든 부분

- 왜 필요한가: 원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `파생 변수 추가` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.
- 원리: 좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `DecisionTree / LogisticRegression 모델 구성`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `모델별 정확도 저장 딕셔너리` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).ipynb`, `250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
