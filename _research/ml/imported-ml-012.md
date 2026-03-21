---
title: "코딩실습12 10.결정트리와 앙상블(AdaBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습12_10.결정트리와 앙상블(AdaBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md"
excerpt: "코딩실습12 10.결정트리와 앙상블(AdaBoost)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 분류 문제, 결정 트리와 앙상블, 전처리와 입력 정리 순서로 큰 장을 먼저 훑고, 파생 변수 추가, DecisionTree / AdaBoo... 같은 코드..."
research_summary: "코딩실습12 10.결정트리와 앙상블(AdaBoost)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 분류 문제, 결정 트리와 앙상블, 전처리와 입력 정리 순서로 큰 장을 먼저 훑고, 파생 변수 추가, DecisionTree / AdaBoo... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
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

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">코딩실습12 10.결정트리와 앙상블(AdaBoost)를 중심으로 학습한 내용을 정리한 ML 실습입니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">원본 마크다운의 큰 섹션 흐름을 기준으로 이 실습을 다시 읽을 수 있게 정리했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">원본 노트에서 데이터를 설명한 부분을 기준으로 실습 맥락을 정리했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">분류 문제 · 결정 트리와 앙상블 · 전처리와 입력 정리 · 피처 엔지니어링</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">파생 변수 추가 -&gt; DecisionTree / AdaBoost 모델 구성 -&gt; 분류 성능 평가</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 8 · 실행 7</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn, matplotlib, numpy</div>
  </div>
</div>

## 원본 노트 흐름

### 분류 문제

분류는 입력 특성으로 클래스나 반응 여부를 예측하는 문제입니다. 모델은 각 샘플이 어떤 범주에 속하는지 확률 또는 라벨로 출력합니다.

- 읽을 포인트: 이 글에서는 가입 여부, 품종, 레이블 예측처럼 범주형 타깃을 다루는 실습 맥락으로 연결됩니다.

### 결정 트리와 앙상블

결정 트리는 조건 분기로 예측 규칙을 만들고, 앙상블은 여러 모델의 예측을 묶어 편향과 분산을 함께 줄이는 접근입니다.

- 읽을 포인트: 이 글에서는 Decision Tree, RandomForest, XGBoost, Voting, Stacking 코드를 통해 여러 모델을 비교해 볼 수 있습니다.

### 전처리와 입력 정리

머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.

- 읽을 포인트: 이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.

### 피처 엔지니어링

피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.

- 읽을 포인트: 이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.

## 구현 흐름

### 1. 파생 변수 추가

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: `matplotlib`
- 코드 포인트: -

### 2. DecisionTree / AdaBoost 모델 구성

- 단계: 모델 구성
- 구현 의도: DecisionTree / AdaBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: `DecisionTree`, `AdaBoost`
- 코드 포인트: -

### 3. 분류 성능 평가

- 단계: 평가
- 구현 의도: 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.
- 핵심 API: `accuracy_score`
- 코드 포인트: -

### 4. from sklearn.ensemble import AdaBoostClassifier

- 단계: 환경 준비
- 구현 의도: 넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.
- 핵심 API: `train_test_split`, `DecisionTree`, `AdaBoost`, `accuracy_score`
- 코드 포인트: -

### 5. X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)

- 단계: 구현 코드
- 구현 의도: X, y = make_moons(n_samples=1000,... 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: -

### 6. X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, rand...

- 단계: 구현 코드
- 구현 의도: 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.
- 핵심 API: `train_test_split`
- 코드 포인트: -

## 코드로 확인한 내용

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

넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.

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

X, y = make_moons(n_samples=1000,... 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

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

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).ipynb`, `250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## 원문 미리보기

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
