---
title: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md"
excerpt: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)를 중심으로 회귀 문제, 피처 엔지니어링 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)를 중심으로 회귀 문제, 피처 엔지니어링 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 1990년 캘리포니아 주택 데이터, from sklearn.datasets... 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, numpy입니다."
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

<div class="research-doc-hero">
  <div class="research-doc-summary">
    <p class="research-doc-summary__label">문제 설정</p>
    <p class="research-doc-summary__body">https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html</p>
  </div>
  <div class="research-doc-meta">
<div class="research-doc-card">
  <p class="research-doc-card__label">데이터 맥락</p>
  <p class="research-doc-card__value">https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">핵심 개념</p>
  <p class="research-doc-card__value">회귀 문제 · 피처 엔지니어링 · 평가 지표 해석</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">구현 포인트</p>
  <p class="research-doc-card__value">1990년 캘리포니아 주택 데이터 · from sklearn.datasets import fetch_california_hou...</p>
</div>
  </div>
  <div class="research-doc-stats">
<div class="research-doc-stat">
  <span>소스</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-stat">
  <span>자료</span>
  <strong>코드 7 · 실행 6</strong>
</div>
<div class="research-doc-stat">
  <span>주요 스택</span>
  <strong>sklearn, numpy</strong>
</div>
  </div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">회귀 문제</p>
  <p class="research-note-card__body">회귀는 연속적인 수치를 예측하는 문제입니다. 예측값과 실제값의 차이를 오차로 계산해 모델 성능을 판단합니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 수요량, 가격, 점수처럼 숫자 타깃을 예측하는 실습과 이어집니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">피처 엔지니어링</p>
  <p class="research-note-card__body">피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">평가 지표 해석</p>
  <p class="research-note-card__body">평가 지표는 예측 결과를 수치화해 모델의 강점과 약점을 읽게 해주는 기준입니다. 문제 유형에 맞는 지표를 골라야 실험 비교가 가능합니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 F1, Recall, Accuracy, RMSLE 같은 지표를 실제 코드에서 계산하는 흐름으로 연결됩니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">함수 분해와 로직 구성</p>
  <p class="research-note-card__body">함수는 입력, 처리, 반환을 분리해 로직을 재사용하기 쉽게 만들고, 문제를 작은 단위로 나누는 기본 도구입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 문제 풀이를 함수 단위로 쪼개고 입출력을 나눠 보는 실습과 연결됩니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-list">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">1990년 캘리포니아 주택 데이터</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 데이터 로드</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 환경 준비</p>
  <p class="research-step-card__title">from sklearn.datasets import fetch_california_housing</p>
  <p class="research-step-card__body">지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>GridSearchCV</code> <code>RMSE</code></p>

</div>
</div>

## Code Evidence

### 1990년 캘리포니아 주택 데이터

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 데이터 로드
X, y = fetch_california_housing(return_X_y=True)
```

### from sklearn.datasets import fetch_california_housing

**직접 해본 단계**: 환경 준비

**핵심 API**: `GridSearchCV`, `RMSE`

지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np
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
