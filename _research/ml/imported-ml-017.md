---
title: "코딩실습16 11.차원축소(PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습16_11.차원축소(PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md"
excerpt: "사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html"
research_summary: "사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다."
research_artifacts: "ipynb/md · 코드 11개 · 실행 10개"
code_block_count: 11
execution_block_count: 10
research_focus:
  - "사이킷런"
  - "데이터 설명"
  - "데이터 불러오기"
research_stack:
  - "sklearn"
  - "matplotlib"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: 사이킷런, 데이터 설명, 데이터 불러오기.

**남겨둔 자료**: `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다.

**주요 스택**: `sklearn`, `matplotlib`

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

## What This Note Covers

### 데이터 설명

사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

## Implementation Flow

1. 데이터 설명: 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

## Code Highlights

### 데이터 설명

`데이터 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html.

```python
from sklearn.datasets import load_digits                      # 손글씨 이미지 (64차원)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
```

### 데이터 설명

`데이터 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 스크리플롯 흐름이 주석과 함께 드러납니다.

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
