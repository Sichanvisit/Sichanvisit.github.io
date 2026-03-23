---
title: "9.기본 지도학습 알고리즘들(KNN)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN)"
source_path: "11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md"
excerpt: "9.기본 지도학습 알고리즘들(KNN)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 평가 지표 해석, 전처리와 입력 정리, 분류 문제 순서로 큰 장을 먼저 훑고, GridSearchCV 모델 학습, 분류 성능 평가 같은 코드로 실제 구현을 이어서 확인할..."
research_summary: "9.기본 지도학습 알고리즘들(KNN)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 평가 지표 해석, 전처리와 입력 정리, 분류 문제 순서로 큰 장을 먼저 훑고, GridSearchCV 모델 학습, 분류 성능 평가 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
research_artifacts: "ipynb/md · 코드 13개 · 실행 13개"
code_block_count: 13
execution_block_count: 13
research_focus:
  - "사이킷런 링크"
  - "표준화"
  - "최적의 K값으로 학습 및 평가"
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
    <div class="research-overview__value">사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html 클래스 수: 3개. 샘플 수: 총 178개 (class_...</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">원본 마크다운의 큰 섹션 흐름을 기준으로 이 실습을 다시 읽을 수 있게 정리했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html 클래스 수: 3개 - 샘플 수: 총 178개 (class_...</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">평가 지표 해석 · 전처리와 입력 정리 · 분류 문제</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">데이터셋 불러오기 -&gt; GridSearchCV 모델 학습 -&gt; 분류 성능 평가</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 13 · 실행 13</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn</div>
  </div>
</div>

<!-- #region id="LUKfOGlUH4Oj" -->
사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html

- 클래스 수: 3개
- 샘플 수: 총 178개 (class_0: 59, class_1: 71, class_2: 48)
- 피처 수: 13개 (연속형, 모두 양수)
- 출처: UCI 머신러닝 저장소의 Wine 데이터셋 (값 일부 포맷화됨)

| 피처 이름                           | 설명                 |
| ------------------------------- | ------------------ |
| alcohol                         | 알코올 함량             |
| malic\_acid                     | 말산 함량              |
| ash                             | 회분 함량              |
| alcalinity\_of\_ash             | 회분의 알칼리도           |
| magnesium                       | 마그네슘 함량            |
| total\_phenols                  | 총 페놀               |
| flavanoids                      | 플라바노이드             |
| nonflavanoid\_phenols           | 비플라바노이드 페놀         |
| proanthocyanins                 | 프로안토시아니딘           |
| color\_intensity                | 색 농도               |
| hue                             | 색조                 |
| od280/od315\_of\_diluted\_wines | 희석 와인의 OD280/OD315 |
| proline                         | 프롤린                |

<!-- #endregion -->

```python id="dw6Ln0CXHrp9" executionInfo={"status": "ok", "timestamp": 1756341843831, "user_tz": -540, "elapsed": 578, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

```python id="6Il9pCpEIbPw" executionInfo={"status": "ok", "timestamp": 1756341945936, "user_tz": -540, "elapsed": 28, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
wine = load_wine()
X, y = wine.data, wine.target
target_names = wine.target_names
```

```python id="eMxJJj3cI0Tx" executionInfo={"status": "ok", "timestamp": 1756341976919, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```python id="AgyJmATtI74h" executionInfo={"status": "ok", "timestamp": 1756342075245, "user_tz": -540, "elapsed": 27, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 표준화

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
```

```python id="YXBdie3lJT44" executionInfo={"status": "ok", "timestamp": 1756343389337, "user_tz": -540, "elapsed": 15, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
```

```python colab={"base_uri": "https://localhost:8080/"} id="Uw-tOkzzJk2p" executionInfo={"status": "ok", "timestamp": 1756343389809, "user_tz": -540, "elapsed": 40, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="cd3ddde4-2ab6-4335-8a04-b1f7982d1110"
accuracy_score(y_test, y_pred)
```

```python colab={"base_uri": "https://localhost:8080/"} id="wUfsvpqFJo1d" executionInfo={"status": "ok", "timestamp": 1756343390587, "user_tz": -540, "elapsed": 13, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="db55e702-4e17-467c-89de-187523fa7106"
print(classification_report(y_test, y_pred, target_names=target_names))
```

```python id="glM5oidxJ132" executionInfo={"status": "ok", "timestamp": 1756343023064, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.model_selection import GridSearchCV
```

```python colab={"base_uri": "https://localhost:8080/", "height": 164} id="mvTeofIhM7Sw" executionInfo={"status": "ok", "timestamp": 1756343160510, "user_tz": -540, "elapsed": 942, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="306d4f5d-42b6-48d0-8887-0bd606ac1932"
param_grid = {'n_neighbors': range(1, 31)}
grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid.fit(X_train_scaled, y_train)
```

```python colab={"base_uri": "https://localhost:8080/"} id="4l7V8r35Ncnl" executionInfo={"status": "ok", "timestamp": 1756343198814, "user_tz": -540, "elapsed": 35, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5818c69f-464c-40b4-d263-0a286ff586c5"
best_k = grid.best_params_['n_neighbors']
best_k
```

```python id="c6yfxvuyNmMp" executionInfo={"status": "ok", "timestamp": 1756343312765, "user_tz": -540, "elapsed": 25, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 최적의 K값으로 학습 및 평가
best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test_scaled)
```

```python colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1756343340250, "user_tz": -540, "elapsed": 32, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2a7c78e4-a189-4714-d24b-0512476e8220" id="Yqe3DuAqOFaG"
accuracy_score(y_test, y_pred_best)
```

```python colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1756343351398, "user_tz": -540, "elapsed": 28, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="075b7611-5ebe-48c1-f74d-771ff62849a2" id="BnkOnJXyOFaJ"
print(classification_report(y_test, y_pred_best, target_names=target_names))
```
