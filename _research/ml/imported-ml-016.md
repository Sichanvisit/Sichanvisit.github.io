---
title: "SVM"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250901_SVM"
source_path: "11_Machine_Learning/Code_Snippets/250901_SVM.md"
excerpt: "centers=2, C: cost (오분류에 대한 패널티 강도),.."
research_summary: "centers=2, C: cost (오분류에 대한 패널티 강도),... 중심으로 구현 과정을 정리한 SVM 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 8개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다."
research_artifacts: "ipynb/md · 코드 8개 · 실행 8개"
code_block_count: 8
execution_block_count: 8
research_focus:
  - "centers=2"
  - "C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절"
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
  - archive-note
---

centers=2, C: cost (오분류에 대한 패널티 강도),... 중심으로 구현 과정을 정리한 SVM 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 8개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다.

**빠르게 볼 수 있는 포인트**: centers=2, C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절.

**남겨둔 자료**: `ipynb/md` 원본과 8개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다.

**주요 스택**: `numpy`, `matplotlib`, `sklearn`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 8 |
| Execution Cells | 8 |
| Libraries | `numpy`, `matplotlib`, `sklearn` |
| Source Note | `250901_SVM` |

## What I Studied

- centers=2
- C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절

## What I Tried in Code

1. 피처 가공: 파생 변수 추가
2. 학습: SVM 모델 학습
3. 시각화: 데이터 분포 시각화
4. 환경 준비: import numpy as np
5. 구현 코드: X_blob, y_blob = make_blobs(n_samples=50, centers...
6. 구현 코드: xx, yy = np.meshgrid(np.linspace(X_blob[:, 0].min...

## Code Evidence

### 파생 변수 추가

**직접 해본 단계**: 피처 가공

`파생 변수 추가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
def plot_decision_boundary(clf, X, y, ax, title):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

    ax.contourf(xx, yy, Z, alpha=0.3, cmap=cmap_light)
    ax.scatter(X[:, 0][y==0], X[:, 1][y==0], c='red', marker='o', label='Class 0')
    ax.scatter(X[:, 0][y==1], X[:, 1][y==1], c='blue', marker='x', label='Class 1')

    ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
               s=150, facecolors='none', edgecolors='black', linewidths=2, label='Support Vectors')

    ax.set_title(title)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend()
    ax.grid(True)
```

### SVM 모델 학습

**직접 해본 단계**: 학습

`SVM 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다. 코드에는 C: cost (오분류에 대한 패널티 강도), gamma... 같은 처리 포인트도 함께 남아 있습니다.

```python
model_svc = SVC(kernel='rbf', C=10, gamma=0.001)          # C와 gamma설정 중요!
# C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절
model_svc.fit(X_blob, y_blob)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

`데이터 분포 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
fig, ax = plt.subplots(figsize=(7, 6))
plot_decision_boundary(model_svc, X_blob, y_blob, ax, "SVM \nC=10, gamma=0.01")
plt.show()
```

### import numpy as np

**직접 해본 단계**: 환경 준비

`import numpy as np`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
```

### X_blob, y_blob = make_blobs(n_samples=50, centers=2, random_state=6)

**직접 해본 단계**: 구현 코드

`X_blob, y_blob = make_blobs(n_samples=50, centers=2, random_state=6)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 centers=2 같은 처리 포인트도 함께 남아 있습니다.

```python
X_blob, y_blob = make_blobs(n_samples=50, centers=2, random_state=6)
# centers=2: 2차원으로 만들기 위한 것. centers=3이면 시각화 어려움
```

### xx, yy = np.meshgrid(np.linspace(X_blob[:, 0].min()-1, X_blob[:, 0].max()+1,...

**직접 해본 단계**: 구현 코드

`xx, yy = np.meshgrid(np.linspace(X_blob[:, 0].min()-1, X_blob[:, 0].max()+1,...`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
xx, yy = np.meshgrid(np.linspace(X_blob[:, 0].min()-1, X_blob[:, 0].max()+1, 500),
                     np.linspace(X_blob[:, 1].min()-1, X_blob[:, 1].max()+1, 500))
```

## Why These Steps Matter

### 파생 변수를 직접 만든 부분

- 왜 필요한가: 원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `파생 변수 추가` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.
- 원리: 좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.

### 학습 코드를 따로 보는 이유

- 왜 필요한가: 모델 선언만으로는 끝나지 않고 fitting, 검증 분리, 하이퍼파라미터 탐색까지 봐야 실제로 해본 실습으로 읽힙니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `SVM 모델 학습` 코드를 남겨 학습 루프나 GridSearchCV처럼 성능을 끌어올리기 위해 손댄 지점을 보여줍니다.
- 원리: 훈련 과정은 데이터에서 패턴을 찾도록 파라미터를 조정하는 단계이며, 검증이 함께 있어야 과적합 여부도 판단할 수 있습니다.

### 시각화를 같이 남긴 이유

- 왜 필요한가: 숫자만 보면 놓치기 쉬운 분포와 이상치를 그래프로 확인해야 다음 전처리나 feature engineering 방향이 또렷해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `데이터 분포 시각화` 코드를 통해 어떤 그래프를 보고 판단했는지 실습 흔적을 남겼습니다.
- 원리: 시각화는 데이터 분포를 직관적으로 드러내 모델 선택과 변수 설계의 근거를 만들어 줍니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `X_blob, y_blob = make_blobs(n_samples=50, centers=2, random_state=6)` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250901_SVM.md`
- Source formats: `ipynb`, `md`
- Companion files: `250901_SVM.ipynb`, `250901_SVM.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
