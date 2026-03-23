---
title: "9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md"
excerpt: "9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 1990년 캘리포니아 주택 데이터 순서로 큰 장을 먼저 훑고, GridSearchCV 모델 학습, 회귀 성능 평가 같은 코드로 실제 구현을 이어서 확..."
research_summary: "9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 1990년 캘리포니아 주택 데이터 순서로 큰 장을 먼저 훑고, GridSearchCV 모델 학습, 회귀 성능 평가 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, numpy입니다."
research_artifacts: "ipynb/md · 코드 7개 · 실행 6개"
code_block_count: 7
execution_block_count: 6
research_focus:
  - "1990년 캘리포니아 주택 데이터"
  - "https"
  - "RMSE 함수 정의"
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
  - archive-note
---

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html 데이터 피쳐 설명</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">1990년 캘리포니아 주택 데이터</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html 데이터 피쳐 설명</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">1990년 캘리포니아 주택 데이터</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">California Housing 불러오기 -&gt; GridSearchCV 모델 학습 -&gt; 회귀 성능 평가</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 7 · 실행 6</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn, numpy</div>
  </div>
</div>

```python id="8kNv1FJLFS00" executionInfo={"status": "ok", "timestamp": 1755854693875, "user_tz": -540, "elapsed": 3610, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np
```

<!-- #region id="wHBkw2wPGI1C" -->
# 1990년 캘리포니아 주택 데이터

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html

| 항목        | 내용                                                                           |
| --------- | ---------------------------------------------------------------------------- |
| 데이터 크기    | 총 20,640개의 샘플                                                                |
| 입력 특성 (X) | 8개의 수치형 변수                                                                   |
| 타겟 (y)    | 1인당 평균 주택 가격 (단위: 100,000 달러)                                                |
| 사용 목적     | **회귀 문제** (주택 가격 예측 등)                                                       |
| 출처        | UCI Machine Learning Repository (California Housing Dataset, 1996 Census 기반) |

데이터 피쳐 설명

| 열 이름         | 설명                        |
| ------------ | ------------------------- |
| `MedInc`     | 블록 내 중간 소득 (단위: 10,000달러) |
| `HouseAge`   | 주택 연식의 중앙값                |
| `AveRooms`   | 가구당 평균 방 개수               |
| `AveBedrms`  | 가구당 평균 침실 개수              |
| `Population` | 블록 내 인구 수                 |
| `AveOccup`   | 가구당 평균 인원 수               |
| `Latitude`   | 위도                        |
| `Longitude`  | 경도                        |
<!-- #endregion -->

```python id="8IYlGS6fGBS6" executionInfo={"status": "ok", "timestamp": 1755854841671, "user_tz": -540, "elapsed": 3244, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 데이터 로드
X, y = fetch_california_housing(return_X_y=True)
```

```python id="2OjGwMn6Gpn6" executionInfo={"status": "ok", "timestamp": 1755855238269, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# RMSE 함수 정의
def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

rmse_scorer = make_scorer(rmse, greater_is_better=False)
```

```python id="9CHmTVqwHkwC" executionInfo={"status": "ok", "timestamp": 1755855239287, "user_tz": -540, "elapsed": 5, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 파라미터 그리드 정의
param_grid = {'alpha' : [0.01, 0.1, 1, 10, 100]}
```

```python colab={"base_uri": "https://localhost:8080/", "height": 164} id="UCNfGF5kHt1q" executionInfo={"status": "ok", "timestamp": 1755855240070, "user_tz": -540, "elapsed": 166, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="874cf2d8-ef22-4871-aa0d-539962b09cd4"
# 그리드 서치 설정 및 학습
grid = GridSearchCV(Ridge(), param_grid, scoring=rmse_scorer, cv=5)         # cv=5: cross validation
grid.fit(X,y)
```

```python colab={"base_uri": "https://localhost:8080/"} id="-uAj6csZIJ0z" executionInfo={"status": "ok", "timestamp": 1755855391587, "user_tz": -540, "elapsed": 40, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="1993688f-a871-416c-ac60-1af37505b4cd"
# 결과 출력
print("최적의 alpha: ", grid.best_params_['alpha'])     # best_params_: 모델의 최적 파라미터 값 반환
print("RMSE: ", grid.best_score_)                       # best_score_: 최적 모델의 점수
```

<!-- #region id="pswuM2DQJbqj" -->
=> RMSE가 0.75라는건,

모델의 예측값이 실제값과 평균적으로 약 7만 5천달러 정도 차이가 난다! (Why? 기본 단위가 100,000달러)
<!-- #endregion -->

```python id="t6cdTo6XJOrz"

```
