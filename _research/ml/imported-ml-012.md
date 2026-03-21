---
title: "코딩실습12 10.결정트리와 앙상블(AdaBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습12_10.결정트리와 앙상블(AdaBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md"
excerpt: "코딩실습12 10.결정트리와 앙상블(AdaBoost)에서 다룬 구현 흐름과 참고 소스를 다시 볼 수 있게 정리한 ML 아카이브 노트입니다"
research_summary: "코딩실습12 10.결정트리와 앙상블(AdaBoost)에서 다룬 구현 흐름과 참고 소스를 다시 볼 수 있게 정리한 ML 아카이브 노트입니다. 문제 맥락과 구현 흔적을 한 화면에서 빠르게 파악할 수 있도록 핵심 정보부터 배치했습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
research_artifacts: "ipynb/md · 코드 8개 · 실행 7개"
code_block_count: 8
execution_block_count: 7
research_focus: []
research_stack:
  - "sklearn"
  - "matplotlib"
  - "numpy"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

코딩실습12 10.결정트리와 앙상블(AdaBoost)에서 다룬 구현 흐름과 참고 소스를 다시 볼 수 있게 정리한 ML 아카이브 노트입니다. 문제 맥락과 구현 흔적을 한 화면에서 빠르게 파악할 수 있도록 핵심 정보부터 배치했습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다.

**남겨둔 자료**: `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다.

**주요 스택**: `sklearn`, `matplotlib`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 8 |
| Execution Cells | 7 |
| Libraries | `sklearn`, `matplotlib`, `numpy` |
| Source Note | `250827_코딩실습12_10.결정트리와 앙상블(AdaBoost)` |

## What This Note Covers

- 이 기록은 `ML` 트랙의 `Practice` 아카이브로 정리되어 있습니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 평가 지표 해석

- 왜 필요한가: 정확도 하나만으로는 모델이 실제로 무엇을 잘하고 무엇을 놓치는지 충분히 설명할 수 없습니다.
- 왜 이 방식을 쓰는가: 문제 유형에 맞는 지표를 함께 보면 불균형 데이터, 오차 크기, 재현율 같은 중요한 관점을 놓치지 않을 수 있습니다.
- 원리: 예측 결과를 정답과 비교해 오차나 클래스별 성능을 수치화하고, 그 수치로 모델 선택과 개선 방향을 판단합니다.

## Implementation Flow

1. 원본 노트의 문제 정의를 먼저 확인합니다.
2. 핵심 코드 블록과 구현 단계를 따라갑니다.
3. 필요하면 이 흐름을 별도 케이스 스터디로 확장합니다.

## Code Highlights

### from sklearn.ensemble import AdaBoostClassifier

`from sklearn.ensemble import AdaBoostClassifier`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap           # 결정 경계 시각화 하기 위한 라이브러리
```

### base_estimator = DecisionTreeClassifier(max_depth=1) # Stump생성

`base_estimator = DecisionTreeClassifier(max_depth=1) # Stump생성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
base_estimator = DecisionTreeClassifier(max_depth=1)      # Stump생성
ada_clf = AdaBoostClassifier(
    estimator=base_estimator,
    n_estimators=1000,
    learning_rate=0.1
)
ada_clf.fit(X_train, y_train)
```

### def plot_decision_boundary(model, X, y, title="Decision Boundary")

`def plot_decision_boundary(model, X, y, title="Decision Boundary")`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 학습된 모델로 추론을 수행하고 예측 결과를 점검하는 코드입니다.

```python
def plot_decision_boundary(model, X, y, title="Decision Boundary"):
    cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#0000FF'])

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=30)
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.grid(True)
    plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).ipynb`, `250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
