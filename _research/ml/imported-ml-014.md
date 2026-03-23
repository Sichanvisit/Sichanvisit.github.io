---
title: "10.결정트리와 앙상블(보팅배깅부스팅스태킹)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습14_10.결정트리와 앙상블(보팅배깅부스팅스태킹).md"
excerpt: "10.결정트리와 앙상블(보팅배깅부스팅스태킹)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 전처리와 입력 정리, 분류 문제, 결정 트리와 앙상블 순서로 큰 장을 먼저 훑고, DecisionTree 모델 학습, 예측 결과 점검 같은 코드로 실제 구현을 이어..."
research_summary: "10.결정트리와 앙상블(보팅배깅부스팅스태킹)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 전처리와 입력 정리, 분류 문제, 결정 트리와 앙상블 순서로 큰 장을 먼저 훑고, DecisionTree 모델 학습, 예측 결과 점검 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다."
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
  - archive-note
---

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">시각화를 위한 헬퍼 함수 (이전 실습에서 사용한 것과 동일)</div>
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
    <div class="research-overview__value">전처리와 입력 정리 · 분류 문제 · 결정 트리와 앙상블 · 피처 엔지니어링</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">학습/검증 데이터 분리 -&gt; DecisionTree 모델 학습 -&gt; 예측 결과 점검</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 8 · 실행 7</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">numpy, matplotlib, sklearn</div>
  </div>
</div>

```python id="Uy1gma0Nz5VE" executionInfo={"status": "ok", "timestamp": 1756286203283, "user_tz": -540, "elapsed": 4439, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
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

```python id="WH2660aa0E3w" executionInfo={"status": "ok", "timestamp": 1756286213226, "user_tz": -540, "elapsed": 6, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
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

```python id="nvwdV7_J0NtR" executionInfo={"status": "ok", "timestamp": 1756286240251, "user_tz": -540, "elapsed": 45, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)
```

```python id="HOFwFw-z2NqO" executionInfo={"status": "ok", "timestamp": 1756286769690, "user_tz": -540, "elapsed": 78, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```python id="8JMt-MiZ0VBa" executionInfo={"status": "ok", "timestamp": 1756286317066, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 모델별 정확도 저장 딕셔너리
accuracies ={}
```

```python colab={"base_uri": "https://localhost:8080/", "height": 914} id="BpDu2Osf0U-R" executionInfo={"status": "ok", "timestamp": 1756287816927, "user_tz": -540, "elapsed": 2744, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="839a37fd-8ee8-4bbd-e669-d5ec2a77018a"
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
    learning_rate=0.1,
    max_depth=3
)
gb_clf.fit(X_train, y_train)
y_pred_boosting = gb_clf.predict(X_test)
accuracy_boosting = accuracy_score(y_test, y_pred_boosting)
accuracies['Boosting'] = accuracy_boosting
plot_decision_boundary(gb_clf, X_test, y_test, axes[2], f'Boosting (Acc:{accuracy_boosting:.4f})')

# 4. 스태킹
# 4-1. 기본 모델 설정
estimators=[
    ('lr', LogisticRegression()),
    ('dt', DecisionTreeClassifier(max_depth=5)),
    ('KNN', KNeighborsClassifier(n_neighbors=5))
]
# 4-2. 메타 모델 설정
stacking_clf = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression(),
    cv=5
)
stacking_clf.fit(X_train, y_train)
y_pred_stacking = stacking_clf.predict(X_test)
accuracy_stacking = accuracy_score(y_test, y_pred_stacking)
accuracies['Stacking'] = accuracy_stacking
plot_decision_boundary(stacking_clf, X_test, y_test, axes[3], f'Stacking (Acc:{accuracy_stacking:.4f})')
```

```python colab={"base_uri": "https://localhost:8080/"} id="uW7QKCif0Uzf" executionInfo={"status": "ok", "timestamp": 1756287985064, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="25b39e74-d4e2-4199-ed01-0f552c268864"
for model_name, acc in accuracies.items():
    print(f'{model_name}: {acc:.4f}')
```

```python id="y_LxFRm_67Uu"

```
