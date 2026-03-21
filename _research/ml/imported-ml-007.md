---
title: "코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md"
excerpt: "코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge)를 중심으로 선형 모델과 정규화, 전처리와 입력 정리 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge)를 중심으로 선형 모델과 정규화, 전처리와 입력 정리 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 데이터 불러오기, LinearRegression 모델 구성 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "데이터 불러오기"
  - "위와 같은 코드"
  - "테스트 데이터 트레이닝 데이터 분할"
research_stack:
  - "sklearn"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

<div class="research-doc-hero">
  <div class="research-doc-hero__meta">
<div class="research-doc-hero__meta-item">
  <span>Source</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Artifacts</span>
  <strong>코드 19 · 실행 18</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>sklearn</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">테스트 데이터 트레이닝 데이터 분할</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Data Context</p>
  <p class="research-doc-card__value">테스트 데이터 트레이닝 데이터 분할</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">선형 모델과 정규화 · 전처리와 입력 정리</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">데이터 불러오기 -&gt; 모델 구성 -&gt; 학습</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">선형 모델과 정규화</p>
  <p class="research-note-card__body">선형 모델은 입력 특성의 선형 결합으로 예측을 만들고, 정규화는 가중치 크기를 제어해 과적합을 줄이는 역할을 합니다.</p>
  <p class="research-note-card__meta">이 글에서는 LinearRegression, LogisticRegression, Ridge, Lasso 실습과 연결해 해석할 수 있습니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">전처리와 입력 정리</p>
  <p class="research-note-card__body">머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.</p>
  <p class="research-note-card__meta">이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-grid">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">데이터 불러오기</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 데이터 불러오기</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 모델 구성</p>
  <p class="research-step-card__title">LinearRegression 모델 구성</p>
  <p class="research-step-card__body">LinearRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>LinearRegression</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 모델링</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 학습</p>
  <p class="research-step-card__title">Ridge 모델 학습</p>
  <p class="research-step-card__body">훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>Ridge</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 릿지 회귀 모델링</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 평가</p>
  <p class="research-step-card__title">회귀 성능 평가</p>
  <p class="research-step-card__body">예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>RMSE</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 환경 준비</p>
  <p class="research-step-card__title">from sklearn.datasets import fetch_california_housing</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 구현 코드</p>
  <p class="research-step-card__title">테스트 데이터 트레이닝 데이터 분할</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>train_test_split</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 테스트 데이터 트레이닝 데이터 분할</p>
</div>
</div>

## Code Evidence

### 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 데이터 불러오기
X, y = fetch_california_housing(return_X_y = True)
```

### LinearRegression 모델 구성

**직접 해본 단계**: 모델 구성

**핵심 API**: `LinearRegression`

LinearRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
# 모델링
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
```

### Ridge 모델 학습

**직접 해본 단계**: 학습

**핵심 API**: `Ridge`

훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.

```python
# 릿지 회귀 모델링
model_ridge = Ridge(alpha=0.9)
model_ridge.fit(X_train, y_train)
```

### 회귀 성능 평가

**직접 해본 단계**: 평가

**핵심 API**: `RMSE`

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
print("LR MSE: ", mean_squared_error(y_test, model_lr.predict(X_test)))
print("Ridge MSE: ", mean_squared_error(y_test, model_ridge.predict(X_test)))
print("Lasso MSE: ", mean_squared_error(y_test, model_lasso.predict(X_test)))
print("Elastic MSE: ", mean_squared_error(y_test, model_elastic.predict(X_test)))
```

### from sklearn.datasets import fetch_california_housing

**직접 해본 단계**: 환경 준비

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
from sklearn.datasets import fetch_california_housing
```

### 테스트 데이터 트레이닝 데이터 분할

**직접 해본 단계**: 구현 코드

**핵심 API**: `train_test_split`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
# 테스트 데이터 트레이닝 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md`
- Source formats: `ipynb`, `md`
- Companion files: `250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).ipynb`, `250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
