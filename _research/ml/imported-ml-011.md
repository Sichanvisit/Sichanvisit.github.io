---
title: "코딩실습11 10.결정트리와 앙상블(RF)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습11_10.결정트리와 앙상블(RF)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md"
excerpt: "코딩실습11 10.결정트리와 앙상블(RF)를 중심으로 분류 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습11 10.결정트리와 앙상블(RF)를 중심으로 분류 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 단일 디시전 트리 실습, 랜덤 포레스트 실습 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 16개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn, graphviz입니다."
research_artifacts: "ipynb/md · 코드 16개 · 실행 16개"
code_block_count: 16
execution_block_count: 16
research_focus:
  - "단일 디시전 트리 실습"
  - "랜덤 포레스트 실습"
  - "make_moons 데이터 불러오기 - 암기 X"
research_stack:
  - "numpy"
  - "matplotlib"
  - "sklearn"
  - "graphviz"
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
      <td>make_moons 데이터 불러오기. 암기 X</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>make_moons 데이터 불러오기 - 암기 X</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>분류 문제 · 결정 트리와 앙상블 · 전처리와 입력 정리</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>단일 디시전 트리 실습 -&gt; 랜덤 포레스트 실습 -&gt; import numpy as np</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 16 · 실행 16</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>numpy, matplotlib, sklearn, graphviz</td>
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
      <th scope="row">분류 문제</th>
      <td>분류는 입력 특성으로 클래스나 반응 여부를 예측하는 문제입니다. 모델은 각 샘플이 어떤 범주에 속하는지 확률 또는 라벨로 출력합니다.</td>
      <td>이 글에서는 가입 여부, 품종, 레이블 예측처럼 범주형 타깃을 다루는 실습 맥락으로 연결됩니다.</td>
    </tr>
    <tr>
      <th scope="row">결정 트리와 앙상블</th>
      <td>결정 트리는 조건 분기로 예측 규칙을 만들고, 앙상블은 여러 모델의 예측을 묶어 편향과 분산을 함께 줄이는 접근입니다.</td>
      <td>이 글에서는 Decision Tree, RandomForest, XGBoost, Voting, Stacking 코드를 통해 여러 모델을 비교해 볼 수 있습니다.</td>
    </tr>
    <tr>
      <th scope="row">전처리와 입력 정리</th>
      <td>머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.</td>
      <td>이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.</td>
    </tr>
    <tr>
      <th scope="row">피처 엔지니어링</th>
      <td>피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.</td>
      <td>이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.</td>
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
      <th scope="row">Step 1 · 피처 가공</th>
      <td>
        <strong class="research-compact-table__main">단일 디시전 트리 실습</strong>
        <span class="research-compact-table__sub">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</span>
      </td>
      <td><code>matplotlib</code></td>
      <td>산점도 시각화할 함수 정의 · 컬러맵 정의</td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 모델 구성</th>
      <td>
        <strong class="research-compact-table__main">랜덤 포레스트 실습</strong>
        <span class="research-compact-table__sub">RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</span>
      </td>
      <td><code>RandomForest</code></td>
      <td>n_estimators 중요!</td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 환경 준비</th>
      <td>
        <strong class="research-compact-table__main">import numpy as np</strong>
        <span class="research-compact-table__sub">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</span>
      </td>
      <td><code>train_test_split</code> <code>DecisionTree</code> <code>RandomForest</code> <code>accuracy_score</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

### 단일 디시전 트리 실습

**직접 해본 단계**: 피처 가공

**핵심 API**: `matplotlib`

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
# 산점도 시각화할 함수 정의

def plot_decision_boundary(model, X, y, title="Decision Boundary"):
    # 컬러맵 정의
    cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])  # 배경 색
    cmap_bold = ListedColormap(['#FF0000', '#0000FF'])   # 점 색

    # 그리드 영역 설정
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    # 모델로 예측한 결정 경계
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # 시각화
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=cmap_light)  # 결정 경계 색
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=30)
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.grid(True)
    plt.show()
```

### 랜덤 포레스트 실습

**직접 해본 단계**: 모델 구성

**핵심 API**: `RandomForest`

RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=5, n_jobs=-1)
# n_estimators 중요!
rf_clf.fit(X_train, y_train)
```

### import numpy as np

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `DecisionTree`, `RandomForest`, `accuracy_score`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap              # 결정 경계 시각화위한 라이브러리
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습11_10.결정트리와 앙상블(RF).ipynb`, `250827_코딩실습11_10.결정트리와 앙상블(RF).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
