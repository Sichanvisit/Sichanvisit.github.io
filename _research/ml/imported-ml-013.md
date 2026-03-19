---
title: "코딩실습13 10.결정트리와 앙상블(XGBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습13_10.결정트리와 앙상블(XGBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md"
excerpt: "ML Practice: 1. XGBoost 회귀, 2. XGBoost 분류"
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
| Code Blocks | 12 |
| Execution Cells | 11 |
| Libraries | `sklearn`, `xgboost`, `numpy` |
| Source Note | `250827_코딩실습13_10.결정트리와 앙상블(XGBoost)` |

## What I Worked On

- 1. XGBoost 회귀
- 2. XGBoost 분류

## Implementation Flow

1. 1. XGBoost 회귀
2. 2. XGBoost 분류

## Code Highlights

### 1. XGBoost 회귀

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import numpy as np
```

### 1. XGBoost 회귀

```python
model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4
)
model.fit(X_train, y_train)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).ipynb`, `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
