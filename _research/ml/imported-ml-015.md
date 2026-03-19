---
title: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN)"
source_path: "11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md"
excerpt: "사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html"
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
| Code Blocks | 13 |
| Execution Cells | 13 |
| Libraries | `sklearn` |
| Source Note | `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN)` |

## What I Worked On

- 표준화
- 최적의 K값으로 학습 및 평가

## Implementation Flow

1. 표준화
2. 최적의 K값으로 학습 및 평가

## Code Highlights

### from sklearn.datasets import load_wine

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

### knn = KNeighborsClassifier(n_neighbors=1)

```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md`
- Source formats: `ipynb`, `md`
- Companion files: `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).ipynb`, `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## Note Preview

> 사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
> - 클래스 수: 3개 - 샘플 수: 총 178개 (class_0: 59, class_1: 71, class_2: 48) - 피처 수: 13개 (연속형, 모두 양수) - 출처: UCI 머신러닝 저장소의 Wine 데이터셋 (값 일부 포맷화됨)
