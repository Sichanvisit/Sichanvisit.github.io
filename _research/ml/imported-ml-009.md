---
title: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md"
excerpt: "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html"
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
| Code Blocks | 7 |
| Execution Cells | 6 |
| Libraries | `sklearn`, `numpy` |
| Source Note | `250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)` |

## What I Worked On

- 1990년 캘리포니아 주택 데이터
- 데이터 로드
- RMSE 함수 정의
- 파라미터 그리드 정의
- 그리드 서치 설정 및 학습

## Implementation Flow

1. 1990년 캘리포니아 주택 데이터
2. 데이터 로드
3. RMSE 함수 정의
4. 파라미터 그리드 정의
5. 그리드 서치 설정 및 학습
6. 결과 출력

## Code Highlights

### from sklearn.datasets import fetch_california_housing

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np
```

### 1990년 캘리포니아 주택 데이터

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
