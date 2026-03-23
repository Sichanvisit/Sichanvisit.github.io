---
title: "10.결정트리와 앙상블(AdaBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250827_코딩실습12_10.결정트리와 앙상블(AdaBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습12_10.결정트리와 앙상블(AdaBoost).md"
excerpt: "10.결정트리와 앙상블(AdaBoost)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 전처리와 입력 정리, 분류 문제, 결정 트리와 앙상블 순서로 큰 장을 먼저 훑고, DecisionTree 모델 학습, 분류 성능 평가 같은 코드로 실제 구현을 이어서..."
research_summary: "10.결정트리와 앙상블(AdaBoost)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 전처리와 입력 정리, 분류 문제, 결정 트리와 앙상블 순서로 큰 장을 먼저 훑고, DecisionTree 모델 학습, 분류 성능 평가 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 8개 코드 블록, 7개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
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
  - archive-note
---

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">10.결정트리와 앙상블(AdaBoost)를 중심으로 학습한 내용을 정리한 ML 실습입니다.</div>
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
    <div class="research-overview__value">학습/검증 데이터 분리 -&gt; DecisionTree 모델 학습 -&gt; 분류 성능 평가</div>
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

```python id="Zduh3MdSc0qk" executionInfo={"status": "ok", "timestamp": 1756280202134, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap           # 결정 경계 시각화 하기 위한 라이브러리
```

```python id="dY7Mke0bdAfi" executionInfo={"status": "ok", "timestamp": 1756280247686, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)
```

```python id="H7s7T1P9ddRt" executionInfo={"status": "ok", "timestamp": 1756280361857, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 164} id="f8m7eMsZdluu" executionInfo={"status": "ok", "timestamp": 1756280866975, "user_tz": -540, "elapsed": 2529, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="12a50a7d-ea4b-4325-a000-93a7ec229b43"
base_estimator = DecisionTreeClassifier(max_depth=1)      # Stump생성
ada_clf = AdaBoostClassifier(
    estimator=base_estimator,
    n_estimators=1000,
    learning_rate=0.1
)
ada_clf.fit(X_train, y_train)
```

```python colab={"base_uri": "https://localhost:8080/"} id="d-0qp6XVeYCo" executionInfo={"status": "ok", "timestamp": 1756280868615, "user_tz": -540, "elapsed": 325, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="42194c2d-a94b-44c5-f7ed-0f791d4c29f8"
y_pred = ada_clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
acc
```

```python id="Sl42ov1jeiMr" executionInfo={"status": "ok", "timestamp": 1756280869584, "user_tz": -540, "elapsed": 17, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
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

```python colab={"base_uri": "https://localhost:8080/", "height": 564} id="6JbW8uNSenEq" executionInfo={"status": "ok", "timestamp": 1756280873966, "user_tz": -540, "elapsed": 3142, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="46167329-2d15-4583-8ed7-8554b91e52c6"
plot_decision_boundary(ada_clf, X, y, title="AdaBoost Decision Boundary")
```

```python id="swszcYkIeu-L"

```
