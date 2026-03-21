---
title: "코딩실습10 10.결정트리와 앙상블(DT)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습10_10.결정트리와 앙상블(DT)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md"
excerpt: "코딩실습10 10.결정트리와 앙상블(DT)를 중심으로 회귀 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습10 10.결정트리와 앙상블(DT)를 중심으로 회귀 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 DT 회귀 실습, DT 분류 실습 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다."
research_artifacts: "ipynb/md · 코드 26개 · 실행 25개"
code_block_count: 26
execution_block_count: 25
research_focus:
  - "_reg"
  - "DT 회귀 실습"
  - "DT 분류 실습"
research_stack:
  - "matplotlib"
  - "warnings"
  - "sklearn"
  - "pandas"
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
  <strong>코드 26 · 실행 25</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>matplotlib, warnings, sklearn, pandas</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">_reg: 회귀의 관례적 표현. _clf: 분류의 관례적 표현</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">회귀 문제 · 결정 트리와 앙상블 · 전처리와 입력 정리</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">데이터 불러오기 -&gt; 피처 가공 -&gt; 모델 구성</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
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
<div class="research-note-card">
  <p class="research-note-card__label">피처 엔지니어링</p>
  <p class="research-note-card__body">피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.</p>
  <p class="research-note-card__meta">이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-grid">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">DT 회귀 실습</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 위 코드 판다스로 지정해 불러올 때</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 피처 가공</p>
  <p class="research-step-card__title">DT 분류 실습</p>
  <p class="research-step-card__body">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>DecisionTree</code> <code>matplotlib</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 모델 구성</p>
  <p class="research-step-card__title">DT 회귀 실습</p>
  <p class="research-step-card__body">DecisionTree 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>DecisionTree</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 평가</p>
  <p class="research-step-card__title">DT 회귀 실습</p>
  <p class="research-step-card__body">예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>RMSE</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 시각화</p>
  <p class="research-step-card__title">데이터 분포 시각화</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 환경 준비</p>
  <p class="research-step-card__title">DT 회귀 실습</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>train_test_split</code> <code>DecisionTree</code> <code>RMSE</code></p>

</div>
</div>

## Code Evidence

### DT 회귀 실습

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 위 코드 판다스로 지정해 불러올 때

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)

X_reg = df.values
y_reg = data.target
```

### DT 분류 실습

**직접 해본 단계**: 피처 가공

**핵심 API**: `DecisionTree`, `matplotlib`

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
dt_clf = DecisionTreeClassifier(random_state=42)
dt_clf.fit(X_clf, y_clf)

plt.figure(figsize=(20,10))
plot_tree(
    dt_clf,
    feature_names=feature_names_clf,
    class_names=class_names_clf,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("결정 트리 분류")
plt.show()
```

### DT 회귀 실습

**직접 해본 단계**: 모델 구성

**핵심 API**: `DecisionTree`

DecisionTree 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
dt_reg = DecisionTreeRegressor()    # max_depth를 지정할 수 있음
dt_reg.fit(X_train, y_train)
```

### DT 회귀 실습

**직접 해본 단계**: 평가

**핵심 API**: `RMSE`

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
y_pred = dt_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("평균 제곱 오차(MSE): ", mse)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

!apt-get update -qq
!apt-get install fonts-nanum* -qq

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings(action='ignore')

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf' # 나눔 고딕
font_name = fm.FontProperties(fname=path, size=10).get_name() # 기본 폰트 사이즈 : 10
plt.rc('font', family=font_name)

fm.fontManager.addfont(path)
```

### DT 회귀 실습

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `DecisionTree`, `RMSE`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습10_10.결정트리와 앙상블(DT).ipynb`, `250827_코딩실습10_10.결정트리와 앙상블(DT).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - _reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현
