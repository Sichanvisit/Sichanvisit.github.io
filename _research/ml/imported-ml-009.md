---
title: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md"
excerpt: "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html"
research_summary: "https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, numpy입니다."
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

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, numpy입니다.

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

## What I Studied

### 1990년 캘리포니아 주택 데이터

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html

## What I Tried in Code

1. 데이터 불러오기: 1990년 캘리포니아 주택 데이터
2. 학습: 1990년 캘리포니아 주택 데이터
3. 평가: 1990년 캘리포니아 주택 데이터
4. 환경 준비: from sklearn.datasets import fetch_california_hou...
5. 구현 코드: 1990년 캘리포니아 주택 데이터

## Code Evidence

### 1990년 캘리포니아 주택 데이터

**직접 해본 단계**: 데이터 불러오기

`1990년 캘리포니아 주택 데이터`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다. 코드에는 데이터 로드 같은 처리 포인트도 함께 남아 있습니다.

```python
# 데이터 로드
X, y = fetch_california_housing(return_X_y=True)
```

### 1990년 캘리포니아 주택 데이터

**직접 해본 단계**: 학습

`1990년 캘리포니아 주택 데이터`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 하이퍼파라미터 탐색이나 교차검증을 통해 단순 실행이 아니라 성능 비교까지 해본 학습 코드입니다. 코드에는 그리드 서치 설정 및 학습 같은 처리 포인트도 함께 남아 있습니다.

```python
# 그리드 서치 설정 및 학습
grid = GridSearchCV(Ridge(), param_grid, scoring=rmse_scorer, cv=5)         # cv=5: cross validation
grid.fit(X,y)
```

### 1990년 캘리포니아 주택 데이터

**직접 해본 단계**: 평가

`1990년 캘리포니아 주택 데이터`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다. 코드에는 RMSE 함수 정의 같은 처리 포인트도 함께 남아 있습니다.

```python
# RMSE 함수 정의
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

rmse_scorer = make_scorer(rmse, greater_is_better=False)
```

### from sklearn.datasets import fetch_california_housing

**직접 해본 단계**: 환경 준비

`from sklearn.datasets import fetch_california_housing`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np
```

### 1990년 캘리포니아 주택 데이터

**직접 해본 단계**: 구현 코드

`1990년 캘리포니아 주택 데이터`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 파라미터 그리드 정의 같은 처리 포인트도 함께 남아 있습니다.

```python
# 파라미터 그리드 정의
param_grid = {'alpha' : [0.01, 0.1, 1, 10, 100]}
```

### 1990년 캘리포니아 주택 데이터

**직접 해본 단계**: 평가

`1990년 캘리포니아 주택 데이터`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다. 코드에는 결과 출력 같은 처리 포인트도 함께 남아 있습니다.

```python
# 결과 출력
print("최적의 alpha: ", grid.best_params_['alpha'])     # best_params_: 모델의 최적 파라미터 값 반환
print("RMSE: ", grid.best_score_)                       # best_score_: 최적 모델의 점수
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `1990년 캘리포니아 주택 데이터` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 학습 코드를 따로 보는 이유

- 왜 필요한가: 모델 선언만으로는 끝나지 않고 fitting, 검증 분리, 하이퍼파라미터 탐색까지 봐야 실제로 해본 실습으로 읽힙니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `1990년 캘리포니아 주택 데이터` 코드를 남겨 학습 루프나 GridSearchCV처럼 성능을 끌어올리기 위해 손댄 지점을 보여줍니다.
- 원리: 훈련 과정은 데이터에서 패턴을 찾도록 파라미터를 조정하는 단계이며, 검증이 함께 있어야 과적합 여부도 판단할 수 있습니다.

### 지표 계산까지 남긴 이유

- 왜 필요한가: 예측을 했더라도 어떤 기준으로 잘했는지 판단하지 않으면 실험 비교가 성립하지 않습니다.
- 왜 이 방식을 쓰는가: 그래서 `1990년 캘리포니아 주택 데이터` 코드를 통해 정확도, F1, RMSLE 같은 지표를 실제로 어떻게 계산했는지 함께 남겼습니다.
- 원리: 평가 지표는 예측 결과를 수치화해 모델 선택과 개선 방향을 정하는 기준점 역할을 합니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `1990년 캘리포니아 주택 데이터` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

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
