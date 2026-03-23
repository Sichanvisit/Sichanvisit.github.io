---
title: "10.결정트리와 앙상블(XGBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250827_코딩실습13_10.결정트리와 앙상블(XGBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md"
excerpt: "10.결정트리와 앙상블(XGBoost)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 XGBoost 회귀, XGBoost 분류 순서로 큰 장을 먼저 훑고, XGBoost 모델 학습, 회귀 성능 평가 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `..."
research_summary: "10.결정트리와 앙상블(XGBoost)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 XGBoost 회귀, XGBoost 분류 순서로 큰 장을 먼저 훑고, XGBoost 모델 학습, 회귀 성능 평가 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다."
research_artifacts: "ipynb/md · 코드 12개 · 실행 11개"
code_block_count: 12
execution_block_count: 11
research_focus:
  - "XGBoost 회귀"
  - "XGBoost 분류"
research_stack:
  - "sklearn"
  - "xgboost"
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
    <div class="research-overview__value">10.결정트리와 앙상블(XGBoost)에서 XGBoost 회귀, XGBoost 분류 흐름을 직접 따라가며 구현했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">XGBoost 회귀 -&gt; XGBoost 분류</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">특정 데이터셋 설명보다 XGBoost 회귀, XGBoost 분류 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">XGBoost 회귀 · XGBoost 분류</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">California Housing 불러오기 -&gt; XGBoost 모델 학습 -&gt; 회귀 성능 평가</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 12 · 실행 11</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn, xgboost, numpy</div>
  </div>
</div>

# 1. XGBoost 회귀

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import numpy as np
```

```python
data = fetch_california_housing()
X = data.data
y = data.target
```

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```python
model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4
)
model.fit(X_train, y_train)
```

```python
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
rmse
```

# 2. XGBoost 분류

```python
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

```python
iris = load_iris()
X = iris.data
y = iris.target
```

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```python
model = xgb.XGBClassifier(
    objective='multi:softmax',                  # 다중 클래스 분류
    num_class=3                                 # objective='multi:softmax'와 num_class는 같이 써야함
)
model.fit(X_train, y_train)
```

```python
y_pred = model.predict(X_test)
```

```python
acc = accuracy_score(y_test, y_pred)
acc
```

```python

```
