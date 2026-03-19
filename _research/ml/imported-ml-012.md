---
title: "코딩실습12 10.결정트리와 앙상블(AdaBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습12_10.결정트리와 앙상블(AdaBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md"
excerpt: "ML Practice note with implementation details and archived source context."
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

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

## What I Worked On

- This archived note is categorized as `Practice` under `ML`.

## Implementation Flow

1. Review the archived source note.
2. Inspect the main implementation blocks.
3. Reuse the extracted approach in a full project page if needed.

## Code Highlights

### from sklearn.ensemble import AdaBoostClassifier

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

### def plot_decision_boundary(model, X, y, title="Decision Boundary")

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

> No prose preview was available in the source note.
