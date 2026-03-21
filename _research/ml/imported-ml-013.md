---
title: "코딩실습13 10.결정트리와 앙상블(XGBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습13_10.결정트리와 앙상블(XGBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md"
excerpt: "코딩실습13 10.결정트리와 앙상블(XGBoost)를 중심으로 분류 문제, 회귀 문제 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습13 10.결정트리와 앙상블(XGBoost)를 중심으로 분류 문제, 회귀 문제 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 XGBoost 회귀, XGBoost 회귀 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다."
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
  <strong>코드 12 · 실행 11</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>sklearn, xgboost, numpy</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">코딩실습13 10.결정트리와 앙상블(XGBoost)를 중심으로 학습한 내용을 정리한 ML 실습입니다.</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">분류 문제 · 회귀 문제 · 결정 트리와 앙상블</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">데이터 불러오기 -&gt; 모델 구성 -&gt; 환경 준비</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">분류 문제</p>
  <p class="research-note-card__body">분류는 입력 특성으로 클래스나 반응 여부를 예측하는 문제입니다. 모델은 각 샘플이 어떤 범주에 속하는지 확률 또는 라벨로 출력합니다.</p>
  <p class="research-note-card__meta">이 글에서는 가입 여부, 품종, 레이블 예측처럼 범주형 타깃을 다루는 실습 맥락으로 연결됩니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">회귀 문제</p>
  <p class="research-note-card__body">회귀는 연속적인 수치를 예측하는 문제입니다. 예측값과 실제값의 차이를 오차로 계산해 모델 성능을 판단합니다.</p>
  <p class="research-note-card__meta">이 글에서는 수요량, 가격, 점수처럼 숫자 타깃을 예측하는 실습과 이어집니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">결정 트리와 앙상블</p>
  <p class="research-note-card__body">결정 트리는 조건 분기로 예측 규칙을 만들고, 앙상블은 여러 모델의 예측을 묶어 편향과 분산을 함께 줄이는 접근입니다.</p>
  <p class="research-note-card__meta">이 글에서는 Decision Tree, RandomForest, XGBoost, Voting, Stacking 코드를 통해 여러 모델을 비교해 볼 수 있습니다.</p>
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
  <p class="research-step-card__title">XGBoost 회귀</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 모델 구성</p>
  <p class="research-step-card__title">XGBoost 회귀</p>
  <p class="research-step-card__body">XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>XGBoost</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 환경 준비</p>
  <p class="research-step-card__title">XGBoost 회귀</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>train_test_split</code> <code>XGBoost</code> <code>RMSE</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 모델 구성</p>
  <p class="research-step-card__title">XGBoost 분류</p>
  <p class="research-step-card__body">XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>XGBoost</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 환경 준비</p>
  <p class="research-step-card__title">XGBoost 분류</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>train_test_split</code> <code>XGBoost</code> <code>accuracy_score</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 모델 구성</p>
  <p class="research-step-card__title">XGBoost 회귀</p>
  <p class="research-step-card__body">실험의 중심이 되는 모델 구조를 정의하고 비교 기준을 세우는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>RMSE</code></p>

</div>
</div>

## Code Evidence

### XGBoost 회귀

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
data = fetch_california_housing()
X = data.data
y = data.target
```

### XGBoost 회귀

**직접 해본 단계**: 모델 구성

**핵심 API**: `XGBoost`

XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4
)
model.fit(X_train, y_train)
```

### XGBoost 회귀

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `XGBoost`, `RMSE`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import numpy as np
```

### XGBoost 분류

**직접 해본 단계**: 모델 구성

**핵심 API**: `XGBoost`

XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
model = xgb.XGBClassifier(
    objective='multi:softmax',                  # 다중 클래스 분류
    num_class=3                                 # objective='multi:softmax'와 num_class는 같이 써야함
)
model.fit(X_train, y_train)
```

### XGBoost 분류

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `XGBoost`, `accuracy_score`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

### XGBoost 회귀

**직접 해본 단계**: 모델 구성

**핵심 API**: `RMSE`

실험의 중심이 되는 모델 구조를 정의하고 비교 기준을 세우는 코드입니다.

```python
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
rmse
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).ipynb`, `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
