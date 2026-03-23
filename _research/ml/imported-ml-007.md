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

```python id="5GpSfffr1Nxi" executionInfo={"status": "ok", "timestamp": 1755767117413, "user_tz": -540, "elapsed": 14008, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import fetch_california_housing
```

```python id="vgE0ur4_38EG" executionInfo={"status": "ok", "timestamp": 1755767217317, "user_tz": -540, "elapsed": 1793, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 데이터 불러오기
X, y = fetch_california_housing(return_X_y = True)
```

```python id="16NpzKFb4YNk"
# 위와 같은 코드
data = fetch_california_housing()
X, y = data.data, data.target
```

```python colab={"base_uri": "https://localhost:8080/"} id="dK1gTKwi4lpN" executionInfo={"status": "ok", "timestamp": 1755767298304, "user_tz": -540, "elapsed": 38, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4b04aa9a-cfe9-4a23-859e-7c38232b8413"
X.shape
```

```python id="HQCWt3ZS4lm3" executionInfo={"status": "ok", "timestamp": 1755767503153, "user_tz": -540, "elapsed": 59, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 테스트 데이터 트레이닝 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)
```

```python id="AUfOhYkE4lkN" executionInfo={"status": "ok", "timestamp": 1755767533906, "user_tz": -540, "elapsed": 3, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.linear_model import LinearRegression
```

```python colab={"base_uri": "https://localhost:8080/", "height": 79} id="QBn3kT9r5nB7" executionInfo={"status": "ok", "timestamp": 1755767568887, "user_tz": -540, "elapsed": 152, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e02262c9-df3f-41e2-bae1-2c1a18b056e9"
# 모델링
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
```

```python colab={"base_uri": "https://localhost:8080/"} id="Pphmj_ff5viE" executionInfo={"status": "ok", "timestamp": 1755767584081, "user_tz": -540, "elapsed": 17, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="41a0aa1b-0cc8-4fa3-f320-1da44cabe833"
model_lr.score(X_test, y_test)
```

```python id="rOXQJAHy5zRj" executionInfo={"status": "ok", "timestamp": 1755767617837, "user_tz": -540, "elapsed": 7, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.linear_model import Ridge
```

```python colab={"base_uri": "https://localhost:8080/", "height": 79} id="gGGbhyZx57hB" executionInfo={"status": "ok", "timestamp": 1755768402089, "user_tz": -540, "elapsed": 54, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9fbc109b-4fdd-405c-d22f-90140996e609"
# 릿지 회귀 모델링
model_ridge = Ridge(alpha=0.9)
model_ridge.fit(X_train, y_train)
```

```python colab={"base_uri": "https://localhost:8080/"} id="jHR5hUTt6KQ2" executionInfo={"status": "ok", "timestamp": 1755768402595, "user_tz": -540, "elapsed": 47, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5b0d07c7-0bbf-4ae3-9b13-afdde19903b8"
model_ridge.score(X_test, y_test)
```

```python id="4HV0YNor6Umt" executionInfo={"status": "ok", "timestamp": 1755767735354, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.linear_model import Lasso
```

```python colab={"base_uri": "https://localhost:8080/", "height": 79} id="vtcsWfQF6UkO" executionInfo={"status": "ok", "timestamp": 1755767765024, "user_tz": -540, "elapsed": 83, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="dfce5ed2-228b-45f1-f252-602d3bd0a9db"
model_lasso = Lasso(alpha=0.5)
model_lasso.fit(X_train, y_train)
```

```python colab={"base_uri": "https://localhost:8080/"} id="B_WXfo4m6Uhk" executionInfo={"status": "ok", "timestamp": 1755767799469, "user_tz": -540, "elapsed": 25, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="06264d7f-8ec5-4a22-9bb4-61a79ba332ff"
model_lasso.score(X_test, y_test)
```

```python id="RG7xtxKs6jQH" executionInfo={"status": "ok", "timestamp": 1755767842862, "user_tz": -540, "elapsed": 38, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.linear_model import ElasticNet
```

```python colab={"base_uri": "https://localhost:8080/", "height": 79} id="8_CIgkkr6ydE" executionInfo={"status": "ok", "timestamp": 1755767881087, "user_tz": -540, "elapsed": 323, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="10f4f270-7996-40df-aa88-15f59c017876"
model_elastic = ElasticNet(alpha=0.1, l1_ratio=0.5)
model_elastic.fit(X_train, y_train)
```

```python colab={"base_uri": "https://localhost:8080/"} id="WeqMYaAP67tV" executionInfo={"status": "ok", "timestamp": 1755767888926, "user_tz": -540, "elapsed": 28, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b02971f1-5bd9-4c99-f412-c3b3e593a70b"
model_elastic.score(X_test, y_test)
```

```python id="81yZcw-J7qPL" executionInfo={"status": "ok", "timestamp": 1755768099049, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.metrics import mean_squared_error
```

```python colab={"base_uri": "https://localhost:8080/"} id="G0s7xANn7vWH" executionInfo={"status": "ok", "timestamp": 1755768245948, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3ba8fb79-8106-41e1-db27-71b942b0bfb7"
print("LR MSE: ", mean_squared_error(y_test, model_lr.predict(X_test)))
print("Ridge MSE: ", mean_squared_error(y_test, model_ridge.predict(X_test)))
print("Lasso MSE: ", mean_squared_error(y_test, model_lasso.predict(X_test)))
print("Elastic MSE: ", mean_squared_error(y_test, model_elastic.predict(X_test)))
```
