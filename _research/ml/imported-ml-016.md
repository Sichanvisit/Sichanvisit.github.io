---
title: "SVM"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250901_SVM"
source_path: "11_Machine_Learning/Code_Snippets/250901_SVM.md"
excerpt: "ML Archive Note: centers=2: 2차원으로 만들기 위한 것. centers=3이면 시각화 어려움, C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절"
tags:
  - research-archive
  - imported-note
  - ml
  - archive-note
---

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

## What I Worked On

- centers=2: 2차원으로 만들기 위한 것. centers=3이면 시각화 어려움
- C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절

## Implementation Flow

1. centers=2: 2차원으로 만들기 위한 것. centers=3이면 시각화 어려움
2. C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절

## Code Highlights

### import numpy as np

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
```

### def plot_decision_boundary(clf, X, y, ax, title)

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

> No prose preview was available in the source note.
