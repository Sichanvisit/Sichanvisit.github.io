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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>회귀 문제 · 피처 엔지니어링 · 평가 지표 해석</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>1990년 캘리포니아 주택 데이터 -&gt; from sklearn.datasets import fetch_california_hou...</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 7 · 실행 6</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>sklearn, numpy</td>
    </tr>
    </tbody>
  </table>
</div>

## What I Studied

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--notes">
    <thead>
      <tr>
        <th>개념</th>
        <th>핵심 설명</th>
        <th>코드에서 확인한 것</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">회귀 문제</th>
      <td>회귀는 연속적인 수치를 예측하는 문제입니다. 예측값과 실제값의 차이를 오차로 계산해 모델 성능을 판단합니다.</td>
      <td>이 글에서는 수요량, 가격, 점수처럼 숫자 타깃을 예측하는 실습과 이어집니다.</td>
    </tr>
    <tr>
      <th scope="row">피처 엔지니어링</th>
      <td>피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.</td>
      <td>이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.</td>
    </tr>
    <tr>
      <th scope="row">평가 지표 해석</th>
      <td>평가 지표는 예측 결과를 수치화해 모델의 강점과 약점을 읽게 해주는 기준입니다. 문제 유형에 맞는 지표를 골라야 실험 비교가 가능합니다.</td>
      <td>이 글에서는 F1, Recall, Accuracy, RMSLE 같은 지표를 실제 코드에서 계산하는 흐름으로 연결됩니다.</td>
    </tr>
    <tr>
      <th scope="row">함수 분해와 로직 구성</th>
      <td>함수는 입력, 처리, 반환을 분리해 로직을 재사용하기 쉽게 만들고, 문제를 작은 단위로 나누는 기본 도구입니다.</td>
      <td>이 글에서는 문제 풀이를 함수 단위로 쪼개고 입출력을 나눠 보는 실습과 연결됩니다.</td>
    </tr>
    </tbody>
  </table>
</div>

## How I Implemented It

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--steps">
    <thead>
      <tr>
        <th>단계</th>
        <th>구현 내용</th>
        <th>핵심 API</th>
        <th>코드 포인트</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">Step 1 · 데이터 불러오기</th>
      <td>
        <strong class="research-compact-table__main">1990년 캘리포니아 주택 데이터</strong>
        <span class="research-compact-table__sub">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>데이터 로드</td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 환경 준비</th>
      <td>
        <strong class="research-compact-table__main">from sklearn.datasets import fetch_california_housing</strong>
        <span class="research-compact-table__sub">지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다.</span>
      </td>
      <td><code>GridSearchCV</code> <code>RMSE</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    </tbody>
  </table>
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
