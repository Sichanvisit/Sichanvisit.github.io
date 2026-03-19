---
title: "코딩실습17 11.차원축소(KMeans+PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습17_11.차원축소(KMeans+PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습17_11.차원축소(KMeans+PCA).md"
excerpt: "=> K=3일때 실루엣 스코어가 가장 높다!"
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
| Libraries | `sklearn`, `matplotlib`, `pandas` |
| Source Note | `250901_코딩실습17_11.차원축소(KMeans+PCA)` |

## What I Worked On

- 표준화
- PCA 적용
- 스크리플롯
- 설명 비율 출력
- PCA 적용 - 2차원 축소

## Implementation Flow

1. 표준화
2. PCA 적용
3. 스크리플롯
4. 설명 비율 출력
5. PCA 적용 - 2차원 축소
6. Kmeans

## Code Highlights

### from sklearn.datasets import load_wine

```python
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score
```

### 스크리 플랏

```python
# 스크리 플랏

sse = []                                            # SSE 저장용 빈 리스트
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(X_pca_2d)
    sse.append(kmeans.inertia_)                      # inertia_: 각 클러스터 중심에서 데이터까지 거리 제곱합

plt.figure(figsize=(8,4))
plt.plot(k_range, sse, marker='o', linestyle='--')
plt.title('Elbow Method')
plt.grid(True)
plt.xticks(k_range)
plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250901_코딩실습17_11.차원축소(KMeans+PCA).md`
- Source formats: `ipynb`, `md`
- Companion files: `250901_코딩실습17_11.차원축소(KMeans+PCA).ipynb`, `250901_코딩실습17_11.차원축소(KMeans+PCA).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> => K=3일때 실루엣 스코어가 가장 높다!
