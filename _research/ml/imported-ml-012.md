---
title: "코딩실습12 10.결정트리와 앙상블(AdaBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습12_10.결정트리와 앙상블(AdaBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md"
excerpt: "코딩실습12 10.결정트리와 앙상블(AdaBoost)를 중심으로 분류 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습12 10.결정트리와 앙상블(AdaBoost)를 중심으로 분류 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 파생 변수 추가, DecisionTree / AdaBoo... 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
research_artifacts: "ipynb/md · 코드 8개 · 실행 7개"
code_block_count: 8
execution_block_count: 7
research_focus: []
research_stack:
  - "sklearn"
  - "matplotlib"
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
    <p class="research-doc-summary__body">코딩실습12 10.결정트리와 앙상블(AdaBoost)를 중심으로 학습한 내용을 정리한 ML 실습입니다.</p>
  </div>
  <div class="research-doc-meta">
<div class="research-doc-card">
  <p class="research-doc-card__label">핵심 개념</p>
  <p class="research-doc-card__value">분류 문제 · 결정 트리와 앙상블 · 전처리와 입력 정리</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">구현 포인트</p>
  <p class="research-doc-card__value">파생 변수 추가 · DecisionTree / AdaBoost 모델 구성 · 분류 성능 평가</p>
</div>
  </div>
  <div class="research-doc-stats">
<div class="research-doc-stat">
  <span>소스</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-stat">
  <span>자료</span>
  <strong>코드 8 · 실행 7</strong>
</div>
<div class="research-doc-stat">
  <span>주요 스택</span>
  <strong>sklearn, matplotlib, numpy</strong>
</div>
  </div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">분류 문제</p>
  <p class="research-note-card__body">분류는 입력 특성으로 클래스나 반응 여부를 예측하는 문제입니다. 모델은 각 샘플이 어떤 범주에 속하는지 확률 또는 라벨로 출력합니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 가입 여부, 품종, 레이블 예측처럼 범주형 타깃을 다루는 실습 맥락으로 연결됩니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">결정 트리와 앙상블</p>
  <p class="research-note-card__body">결정 트리는 조건 분기로 예측 규칙을 만들고, 앙상블은 여러 모델의 예측을 묶어 편향과 분산을 함께 줄이는 접근입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 Decision Tree, RandomForest, XGBoost, Voting, Stacking 코드를 통해 여러 모델을 비교해 볼 수 있습니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">전처리와 입력 정리</p>
  <p class="research-note-card__body">머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">피처 엔지니어링</p>
  <p class="research-note-card__body">피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-list">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 피처 가공</p>
  <p class="research-step-card__title">파생 변수 추가</p>
  <p class="research-step-card__body">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 모델 구성</p>
  <p class="research-step-card__title">DecisionTree / AdaBoost 모델 구성</p>
  <p class="research-step-card__body">DecisionTree / AdaBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>DecisionTree</code> <code>AdaBoost</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 평가</p>
  <p class="research-step-card__title">분류 성능 평가</p>
  <p class="research-step-card__body">예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>accuracy_score</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 환경 준비</p>
  <p class="research-step-card__title">from sklearn.ensemble import AdaBoostClassifier</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>train_test_split</code> <code>DecisionTree</code> <code>AdaBoost</code> <code>accuracy_score</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 구현 코드</p>
  <p class="research-step-card__title">X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 구현 코드</p>
  <p class="research-step-card__title">X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, rand...</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>train_test_split</code></p>

</div>
</div>

## Code Evidence

### 파생 변수 추가

**직접 해본 단계**: 피처 가공

**핵심 API**: `matplotlib`

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
def plot_decision_boundary(model, X, y, title="Decision Boundary"):
    cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#0000FF'])

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=cmap_light)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=30)
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.grid(True)
    plt.show()
```

### DecisionTree / AdaBoost 모델 구성

**직접 해본 단계**: 모델 구성

**핵심 API**: `DecisionTree`, `AdaBoost`

DecisionTree / AdaBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
base_estimator = DecisionTreeClassifier(max_depth=1)      # Stump생성
ada_clf = AdaBoostClassifier(
    estimator=base_estimator,
    n_estimators=1000,
    learning_rate=0.1
)
ada_clf.fit(X_train, y_train)
```

### 분류 성능 평가

**직접 해본 단계**: 평가

**핵심 API**: `accuracy_score`

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
y_pred = ada_clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
acc
```

### from sklearn.ensemble import AdaBoostClassifier

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `DecisionTree`, `AdaBoost`, `accuracy_score`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap           # 결정 경계 시각화 하기 위한 라이브러리
```

### X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)
```

### X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, rand...

**직접 해본 단계**: 구현 코드

**핵심 API**: `train_test_split`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).ipynb`, `250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
