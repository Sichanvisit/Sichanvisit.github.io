---
title: "9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md"
excerpt: "9.기본 지도학습 알고리즘들 (Lasso, Ridge)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 전처리와 입력 정리, 선형 모델과 정규화 순서로 큰 장을 먼저 훑고, LinearRegression 모델 학습, Ridge 모델 학습 같은 코드로 실제..."
research_summary: "9.기본 지도학습 알고리즘들 (Lasso, Ridge)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 전처리와 입력 정리, 선형 모델과 정규화 순서로 큰 장을 먼저 훑고, LinearRegression 모델 학습, Ridge 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "테스트 데이터 트레이닝 데이터 분할"
  - "데이터 불러오기"
  - "위와 같은 코드"
research_stack:
  - "sklearn"
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
    <div class="research-overview__value">테스트 데이터 트레이닝 데이터 분할</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">원본 마크다운의 큰 섹션 흐름을 기준으로 이 실습을 다시 읽을 수 있게 정리했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">테스트 데이터 트레이닝 데이터 분할</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">전처리와 입력 정리 · 선형 모델과 정규화</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">California Housing 불러오기 -&gt; LinearRegression 모델 학습 -&gt; 학습/검증 데이터 분리</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 19 · 실행 18</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn</div>
  </div>
</div>

```python
from sklearn.datasets import fetch_california_housing
```

```python
# 데이터 불러오기
X, y = fetch_california_housing(return_X_y = True)
```

```python
# 위와 같은 코드
data = fetch_california_housing()
X, y = data.data, data.target
```

```python
X.shape
```

```python
# 테스트 데이터 트레이닝 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)
```

```python
from sklearn.linear_model import LinearRegression
```

```python
# 모델링
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
```

```python
model_lr.score(X_test, y_test)
```

```python
from sklearn.linear_model import Ridge
```

```python
# 릿지 회귀 모델링
model_ridge = Ridge(alpha=0.9)
model_ridge.fit(X_train, y_train)
```

```python
model_ridge.score(X_test, y_test)
```

```python
from sklearn.linear_model import Lasso
```

```python
model_lasso = Lasso(alpha=0.5)
model_lasso.fit(X_train, y_train)
```

```python
model_lasso.score(X_test, y_test)
```

```python
from sklearn.linear_model import ElasticNet
```

```python
model_elastic = ElasticNet(alpha=0.1, l1_ratio=0.5)
model_elastic.fit(X_train, y_train)
```

```python
model_elastic.score(X_test, y_test)
```

```python
from sklearn.metrics import mean_squared_error
```

```python
print("LR MSE: ", mean_squared_error(y_test, model_lr.predict(X_test)))
print("Ridge MSE: ", mean_squared_error(y_test, model_ridge.predict(X_test)))
print("Lasso MSE: ", mean_squared_error(y_test, model_lasso.predict(X_test)))
print("Elastic MSE: ", mean_squared_error(y_test, model_elastic.predict(X_test)))
```
