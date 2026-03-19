---
title: "코딩실습16 11.차원축소(PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습16_11.차원축소(PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md"
excerpt: "사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html"
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
| Code Blocks | 11 |
| Execution Cells | 10 |
| Libraries | `sklearn`, `matplotlib` |
| Source Note | `250901_코딩실습16_11.차원축소(PCA)` |

## What I Worked On

- 데이터 설명
- 데이터 불러오기
- 데이터 표준화
- PCA전 시각화
- 차원 축소

## Implementation Flow

1. 데이터 설명
2. 데이터 불러오기
3. 데이터 표준화
4. PCA전 시각화
5. 차원 축소
6. PCA 후 시각화

## Code Highlights

### 데이터 설명

```python
from sklearn.datasets import load_digits                      # 손글씨 이미지 (64차원)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
```

### 데이터 설명

```python
# 스크리플롯

plt.figure(figsize=(12,4))
plt.plot(
        range(1, len(pca.explained_variance_ratio_)+1),        # X축
        pca.explained_variance_,                               # Y축
        marker='o', linestyle='--'
        )
plt.title("Scree plot")
plt.grid(True)
plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md`
- Source formats: `ipynb`, `md`
- Companion files: `250901_코딩실습16_11.차원축소(PCA).ipynb`, `250901_코딩실습16_11.차원축소(PCA).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## Note Preview

> 64차원의 손글씨 데이터
> 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
