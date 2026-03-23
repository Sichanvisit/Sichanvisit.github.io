---
title: "10.결정트리와 앙상블(RF)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250827_코딩실습11_10.결정트리와 앙상블(RF)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md"
excerpt: "10.결정트리와 앙상블(RF)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 단일 디시전 트리 실습, 랜덤 포레스트 실습 순서로 큰 장을 먼저 훑고, DecisionTree 모델 학습, RandomForest 모델 학습 같은 코드로 실제 구현을 이어서 확..."
research_summary: "10.결정트리와 앙상블(RF)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 단일 디시전 트리 실습, 랜덤 포레스트 실습 순서로 큰 장을 먼저 훑고, DecisionTree 모델 학습, RandomForest 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 16개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn, graphviz입니다."
research_artifacts: "ipynb/md · 코드 16개 · 실행 16개"
code_block_count: 16
execution_block_count: 16
research_focus:
  - "단일 디시전 트리 실습"
  - "랜덤 포레스트 실습"
  - "산점도 시각화할 함수 정의"
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
  - archive-note
---

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">10.결정트리와 앙상블(RF)에서 단일 디시전 트리 실습, 랜덤 포레스트 실습 흐름을 직접 따라가며 구현했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">단일 디시전 트리 실습 -&gt; 랜덤 포레스트 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">make_moons 데이터 불러오기 - 암기 X</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">단일 디시전 트리 실습 · 랜덤 포레스트 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">학습/검증 데이터 분리 -&gt; DecisionTree 모델 학습 -&gt; 분류 성능 평가</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 16 · 실행 16</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">numpy, matplotlib, sklearn, graphviz</div>
  </div>
</div>

```python id="NSjhgYTnCGPE" executionInfo={"status": "ok", "timestamp": 1756281516348, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap              # 결정 경계 시각화위한 라이브러리
```

<!-- #region id="H1d4vTMwC2ny" -->
# 1. 단일 디시전 트리 실습
<!-- #endregion -->

```python id="7XHY7DDQCgtK" executionInfo={"status": "ok", "timestamp": 1756281516375, "user_tz": -540, "elapsed": 17, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# make_moons 데이터 불러오기 - 암기 X
X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 333} id="hdCrLIH9Cggw" executionInfo={"status": "ok", "timestamp": 1756281517017, "user_tz": -540, "elapsed": 644, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3328eb97-39c5-4533-e45e-a8a266c10c07"
# 데이터셋 시각화 (어떻게 생겼는지 눈으로 확인)
plt.figure(figsize=(4, 3))
plt.scatter(X[:, 0][y==0], X[:, 1][y==0], c='red', marker='o', label='Class 0')
plt.scatter(X[:, 0][y==1], X[:, 1][y==1], c='blue', marker='x', label='Class 1')
plt.title('Original make_moons Dataset')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid(True)
plt.show()
```

```python id="EtGRaBpwDvku" executionInfo={"status": "ok", "timestamp": 1756281517017, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 79} id="CHHyYMBEDv5A" executionInfo={"status": "ok", "timestamp": 1756281517101, "user_tz": -540, "elapsed": 86, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="69f0ae43-cfc9-48ca-ae56-eed6a6603137"
dt_clf = DecisionTreeClassifier(max_depth=5)
dt_clf.fit(X_train, y_train)
```

```python id="3-B44ymNEDU_" executionInfo={"status": "ok", "timestamp": 1756281517104, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
y_pred_dt = dt_clf.predict(X_test)
```

```python colab={"base_uri": "https://localhost:8080/"} id="ABxu3w0qEN7B" executionInfo={"status": "ok", "timestamp": 1756281517122, "user_tz": -540, "elapsed": 16, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ae5ce4a4-e0fa-4d97-9a3b-540ca0486b50"
# 정확도 계산
accuracy_dt = accuracy_score(y_test, y_pred_dt)
accuracy_dt
```

```python colab={"base_uri": "https://localhost:8080/", "height": 645} id="RD7odJSgEWf_" executionInfo={"status": "ok", "timestamp": 1756281518075, "user_tz": -540, "elapsed": 955, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f280532d-d066-4ced-aa07-3d4d6c73b6b5"
from sklearn.tree import plot_tree

plt.figure(figsize=(16,10))
plot_tree(
    dt_clf,
    filled=True,
    rounded=True,
    feature_names=['Feature1', 'Feature2'],
    class_names=['Class0', 'Class1']
)
plt.title("DT")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 935} id="Pv1ejQpeEo-s" executionInfo={"status": "ok", "timestamp": 1756281518116, "user_tz": -540, "elapsed": 39, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="674bb6f0-79e0-49a4-8289-81192ea0da03"
# 추가 - 보기 좋은 시각화

from sklearn.tree import export_graphviz
import graphviz

dot_data = export_graphviz(
    dt_clf,
    feature_names=['Feature1', 'Feature2'],
    class_names=['Class0', 'Class1'],
    filled=True,
    rounded=True
)

graph = graphviz.Source(dot_data)

graph
```

```python id="gMlIaRD0IG1n" executionInfo={"status": "ok", "timestamp": 1756281518132, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
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

```python colab={"base_uri": "https://localhost:8080/", "height": 564} id="VE_ngBJBIjd3" executionInfo={"status": "ok", "timestamp": 1756281518296, "user_tz": -540, "elapsed": 161, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9d8fc96a-b934-42fe-93b4-861d7b17eeac"
plot_decision_boundary(dt_clf, X, y, title="DT Decision Boundary")
```

<!-- #region id="RHFBaG5EJn_O" -->
# 2. 랜덤 포레스트 실습
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 79} id="y1DY5Kr1Iwtx" executionInfo={"status": "ok", "timestamp": 1756281518321, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="28fc4260-d129-4806-abcf-db3d78ac550d"
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=5, n_jobs=-1)
# n_estimators 중요!
rf_clf.fit(X_train, y_train)
```

```python id="P8ciw042KRer" executionInfo={"status": "ok", "timestamp": 1756281518338, "user_tz": -540, "elapsed": 15, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
y_pred_rf = rf_clf.predict(X_test)
```

```python colab={"base_uri": "https://localhost:8080/"} id="sF89RNQlKXVC" executionInfo={"status": "ok", "timestamp": 1756281518340, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="74844f7a-fc66-4a1a-e30a-011340d8ea37"
accuracy_rf = accuracy_score(y_test, y_pred_rf)
accuracy_rf
```

```python colab={"base_uri": "https://localhost:8080/", "height": 564} id="o7_MvHdKKdk7" executionInfo={"status": "ok", "timestamp": 1756281518631, "user_tz": -540, "elapsed": 298, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f9e36fd5-c075-4351-fa61-82e680c47582"
plot_decision_boundary(rf_clf, X, y, title="RF Decision Boundary")
```

```python id="ok8P_haJKlk3" executionInfo={"status": "ok", "timestamp": 1756281518633, "user_tz": -540, "elapsed": 1, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}

```
