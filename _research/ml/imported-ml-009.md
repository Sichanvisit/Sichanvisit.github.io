---
title: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md"
excerpt: "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html"
research_summary: "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, numpy입니다."
research_artifacts: "ipynb/md · 코드 7개 · 실행 6개"
code_block_count: 7
execution_block_count: 6
research_focus:
  - "https"
  - "1990년 캘리포니아 주택 데이터"
  - "데이터 로드"
research_stack:
  - "sklearn"
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

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, numpy입니다.

**빠르게 볼 수 있는 포인트**: https, 1990년 캘리포니아 주택 데이터, 데이터 로드.

**남겨둔 자료**: `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, numpy입니다.

**주요 스택**: `sklearn`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 7 |
| Execution Cells | 6 |
| Libraries | `sklearn`, `numpy` |
| Source Note | `250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)` |

## What This Note Covers

### 1990년 캘리포니아 주택 데이터

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html

## Implementation Flow

1. 1990년 캘리포니아 주택 데이터: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html

## Code Highlights

### from sklearn.datasets import fetch_california_housing

`from sklearn.datasets import fetch_california_housing`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np
```

### 1990년 캘리포니아 주택 데이터

`1990년 캘리포니아 주택 데이터`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 RMSE 함수 정의 흐름이 주석과 함께 드러납니다.

```python
# RMSE 함수 정의
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

rmse_scorer = make_scorer(rmse, greater_is_better=False)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md`
- Source formats: `ipynb`, `md`
- Companion files: `250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).ipynb`, `250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## Note Preview

> https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html
> / 항목 / 내용 / / --------- / ---------------------------------------------------------------------------- / / 데이터 크기 / 총 20,640개의 샘플 / / 입력 특성 (X) / 8개의 수치형 변수 / / 타겟 (y) / 1인당 평균 주택 가격 (단위: 100,000 달러) / / 사용 목적 / **회귀 문제** (주택 가격 예측 등) / / 출처 / UCI Machine Learning Repository (California Housing Dataset, 1996 Census 기반) /
