---
title: "코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).md"
excerpt: "코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹)를 중심으로 분류 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습14 10.결정트리와 앙상블(보팅배깅부스팅스태킹)를 중심으로 분류 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 파생 변수 추가, DecisionTree / Logist... 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다."
research_artifacts: "ipynb/md · 코드 8개 · 실행 7개"
code_block_count: 8
execution_block_count: 7
research_focus:
  - "시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)"
  - "모델별 정확도 저장 딕셔너리"
  - "보팅"
research_stack:
  - "numpy"
  - "matplotlib"
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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>원본 노트에서 데이터를 설명한 부분을 기준으로 실습 맥락을 정리했습니다.</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>분류 문제 · 결정 트리와 앙상블 · 전처리와 입력 정리</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>파생 변수 추가 -&gt; DecisionTree / LogisticRegression 모델 구성 -&gt; import numpy as np</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 8 · 실행 7</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>numpy, matplotlib, sklearn</td>
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
        <strong class="research-compact-table__main">파생 변수 추가</strong>
        <span class="research-compact-table__sub">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)</td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 모델 구성</th>
      <td>
        <strong class="research-compact-table__main">DecisionTree / LogisticRegression 모델 구성</strong>
        <span class="research-compact-table__sub">DecisionTree / LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</span>
      </td>
      <td><code>DecisionTree</code> <code>Bagging</code> <code>Voting</code> <code>Stacking</code></td>
      <td>보팅 · 1-1. 기본 모델 세팅</td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 환경 준비</th>
      <td>
        <strong class="research-compact-table__main">import numpy as np</strong>
        <span class="research-compact-table__sub">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</span>
      </td>
      <td><code>train_test_split</code> <code>DecisionTree</code> <code>RandomForest</code> <code>Bagging</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 4 · 구현 코드</th>
      <td>
        <strong class="research-compact-table__main">모델별 정확도 저장 딕셔너리</strong>
        <span class="research-compact-table__sub">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>모델별 정확도 저장 딕셔너리</td>
    </tr>
    <tr>
      <th scope="row">Step 5 · 구현 코드</th>
      <td>
        <strong class="research-compact-table__main">for model_name, acc in accuracies.items():</strong>
        <span class="research-compact-table__sub">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 6 · 구현 코드</th>
      <td>
        <strong class="research-compact-table__main">X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)</strong>
        <span class="research-compact-table__sub">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

### 파생 변수 추가

**직접 해본 단계**: 피처 가공

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
# 시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)
def plot_decision_boundary(clf, X, y, ax, title):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00'])


    ax.contourf(xx, yy, Z, alpha=0.8, cmap=cmap_light)
    ax.scatter(X[:, 0][y==0], X[:, 1][y==0], c='red', marker='o', label='Class 0')
    ax.scatter(X[:, 0][y==1], X[:, 1][y==1], c='blue', marker='x', label='Class 1')
    ax.set_title(title)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend()
    ax.grid(True)
```

### DecisionTree / LogisticRegression 모델 구성

**직접 해본 단계**: 모델 구성

**핵심 API**: `DecisionTree`, `Bagging`, `Voting`, `Stacking`

DecisionTree / LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
fig, axes = plt.subplots(2, 2, figsize=(12,11))
axes = axes.flatten()

# 1. 보팅
# 1-1. 기본 모델 세팅
clf1 = LogisticRegression()
clf2 = DecisionTreeClassifier(max_depth=5)
clf3 = KNeighborsClassifier(n_neighbors=5)
# 1-2. 소프트 보팅
voting_clf = VotingClassifier(
    estimators=[('lr', clf1), ('dt', clf2), ('KNN', clf3)],
    voting='soft',
    weights=[1,1,1]
)
voting_clf.fit(X_train, y_train)
y_pred_voting = voting_clf.predict(X_test)
accuracy_voting = accuracy_score(y_test, y_pred_voting)
accuracies['Voting'] = accuracy_voting
plot_decision_boundary(voting_clf, X_test, y_test, axes[0], f'Voting (Acc:{accuracy_voting:.4f})')

# 배깅
bagging_clf = BaggingClassifier(
    estimator=DecisionTreeClassifier(max_depth=5),
    n_estimators=100,
    max_samples=0.7,                                             # 각 트리가 훈련 데이터의 70% 사용 (중복 허용)
    bootstrap=True
)
bagging_clf.fit(X_train, y_train)
y_pred_bagging = bagging_clf.predict(X_test)
accuracy_bagging = accuracy_score(y_test, y_pred_bagging)
accuracies['Bagging'] = accuracy_bagging
plot_decision_boundary(bagging_clf, X_test, y_test, axes[1], f'Bagging (Acc:{accuracy_bagging:.4f})')

# 3. 부스팅
gb_clf = GradientBoostingClassifier(
    n_estimators=100,
# ... trimmed ...
```

### import numpy as np

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `DecisionTree`, `RandomForest`, `Bagging`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, BaggingClassifier, VotingClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
```

### 모델별 정확도 저장 딕셔너리

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# 모델별 정확도 저장 딕셔너리
accuracies ={}
```

### for model_name, acc in accuracies.items():

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
for model_name, acc in accuracies.items():
    print(f'{model_name}: {acc:.4f}')
```

### X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).ipynb`, `250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
