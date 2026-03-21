---
title: "SVM"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250901_SVM"
source_path: "11_Machine_Learning/Code_Snippets/250901_SVM.md"
excerpt: "centers=2, C: cost (오분류에 대한 패널티 강도),.."
research_summary: "centers=2, C: cost (오분류에 대한 패널티 강도),... 중심으로 구현 과정을 정리한 SVM 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 8개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다."
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

centers=2, C: cost (오분류에 대한 패널티 강도),... 중심으로 구현 과정을 정리한 SVM 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 8개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다.

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

## What This Note Covers

- centers=2
- C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. Key Step: centers=2: 2차원으로 만들기 위한 것. centers=3이면 시각화 어려움
2. Key Step: C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절

## Code Highlights

### import numpy as np

`import numpy as np`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
```

### model_svc = SVC(kernel='rbf', C=10, gamma=0.001) # C와 gamma설정 중요!

`model_svc = SVC(kernel='rbf', C=10, gamma=0.001) # C와 gamma설정 중요!`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절 흐름이 주석과 함께 드러납니다.

```python
model_svc = SVC(kernel='rbf', C=10, gamma=0.001)          # C와 gamma설정 중요!
# C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절
model_svc.fit(X_blob, y_blob)
```

### def plot_decision_boundary(clf, X, y, ax, title)

`def plot_decision_boundary(clf, X, y, ax, title)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 학습된 모델로 추론을 수행하고 예측 결과를 점검하는 코드입니다.

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
