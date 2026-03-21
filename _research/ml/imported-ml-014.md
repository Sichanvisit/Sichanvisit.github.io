---
title: "코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).md"
excerpt: "시각화를 위한 헬퍼 함수 (이전 실습에서 사용..., 모델별 정확도 저장 딕셔너리, 보팅 중심으로 구현 과정을 정리한 코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹) 기록입니다"
research_summary: "시각화를 위한 헬퍼 함수 (이전 실습에서 사용..., 모델별 정확도 저장 딕셔너리, 보팅 중심으로 구현 과정을 정리한 코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹) 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다."
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

시각화를 위한 헬퍼 함수 (이전 실습에서 사용..., 모델별 정확도 저장 딕셔너리, 보팅 중심으로 구현 과정을 정리한 코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹) 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다.

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

## What This Note Covers

- 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)
- 모델별 정확도 저장 딕셔너리
- 보팅
- 1-1. 기본 모델 세팅
- 1-2. 소프트 보팅

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 평가 지표 해석

- 왜 필요한가: 정확도 하나만으로는 모델이 실제로 무엇을 잘하고 무엇을 놓치는지 충분히 설명할 수 없습니다.
- 왜 이 방식을 쓰는가: 문제 유형에 맞는 지표를 함께 보면 불균형 데이터, 오차 크기, 재현율 같은 중요한 관점을 놓치지 않을 수 있습니다.
- 원리: 예측 결과를 정답과 비교해 오차나 클래스별 성능을 수치화하고, 그 수치로 모델 선택과 개선 방향을 판단합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. Key Step: 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)

## Code Highlights

### import numpy as np

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

### 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)

`시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일) 흐름이 주석과 함께 드러납니다.

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

### fig, axes = plt.subplots(2, 2, figsize=(12,11))

`fig, axes = plt.subplots(2, 2, figsize=(12,11))`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 보팅, 1-1. 기본 모델 세팅, 1-2. 소프트 보팅 흐름이 주석과 함께 드러납니다.

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
# ... trimmed ...
```

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
