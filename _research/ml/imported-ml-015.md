---
title: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN)"
source_path: "11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md"
excerpt: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)를 중심으로 분류 문제, 전처리와 입력 정리 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)를 중심으로 분류 문제, 전처리와 입력 정리 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 wine = load_wine(), StandardScaler 스케일링 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
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
  <strong>코드 13 · 실행 13</strong>
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
  <p class="research-doc-card__value">사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Data Context</p>
  <p class="research-doc-card__value">사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">분류 문제 · 전처리와 입력 정리 · 평가 지표 해석</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">데이터 불러오기 -&gt; 전처리 -&gt; 모델 구성</p>
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
  <p class="research-note-card__label">전처리와 입력 정리</p>
  <p class="research-note-card__body">머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.</p>
  <p class="research-note-card__meta">이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">평가 지표 해석</p>
  <p class="research-note-card__body">평가 지표는 예측 결과를 수치화해 모델의 강점과 약점을 읽게 해주는 기준입니다. 문제 유형에 맞는 지표를 골라야 실험 비교가 가능합니다.</p>
  <p class="research-note-card__meta">이 글에서는 F1, Recall, Accuracy, RMSLE 같은 지표를 실제 코드에서 계산하는 흐름으로 연결됩니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-grid">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">wine = load_wine()</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 전처리</p>
  <p class="research-step-card__title">StandardScaler 스케일링</p>
  <p class="research-step-card__body">결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>StandardScaler</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 표준화</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 모델 구성</p>
  <p class="research-step-card__title">KNN 모델 구성</p>
  <p class="research-step-card__body">KNN 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 평가</p>
  <p class="research-step-card__title">예측 결과 점검</p>
  <p class="research-step-card__body">예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 최적의 K값으로 학습 및 평가</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 환경 준비</p>
  <p class="research-step-card__title">from sklearn.datasets import load_wine</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>train_test_split</code> <code>StandardScaler</code> <code>accuracy_score</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 구현 코드</p>
  <p class="research-step-card__title">best_k = grid.best_params_[&#x27;n_neighbors&#x27;]</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
</div>

## Code Evidence

### wine = load_wine()

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
wine = load_wine()
X, y = wine.data, wine.target
target_names = wine.target_names
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

**핵심 API**: `StandardScaler`

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

```python
# 표준화

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
```

### KNN 모델 구성

**직접 해본 단계**: 모델 구성

KNN 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
```

### 예측 결과 점검

**직접 해본 단계**: 평가

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
# 최적의 K값으로 학습 및 평가
best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test_scaled)
```

### from sklearn.datasets import load_wine

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `StandardScaler`, `accuracy_score`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

### best_k = grid.best_params_['n_neighbors']

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
best_k = grid.best_params_['n_neighbors']
best_k
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md`
- Source formats: `ipynb`, `md`
- Companion files: `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).ipynb`, `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## Note Preview

> 사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
> - 클래스 수: 3개 - 샘플 수: 총 178개 (class_0: 59, class_1: 71, class_2: 48) - 피처 수: 13개 (연속형, 모두 양수) - 출처: UCI 머신러닝 저장소의 Wine 데이터셋 (값 일부 포맷화됨)
