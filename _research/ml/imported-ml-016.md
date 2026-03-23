---
title: "SVM"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250901_SVM"
source_path: "11_Machine_Learning/Code_Snippets/250901_SVM.md"
excerpt: "SVM의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 객체지향 설계, 함수 분해와 로직 구성 순서로 큰 장을 먼저 훑고, SVM 모델 학습, 예측 결과 점검 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 8개 코드 블록,..."
research_summary: "SVM의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 객체지향 설계, 함수 분해와 로직 구성 순서로 큰 장을 먼저 훑고, SVM 모델 학습, 예측 결과 점검 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 8개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다."
research_artifacts: "ipynb/md · 코드 8개 · 실행 8개"
code_block_count: 8
execution_block_count: 8
research_focus:
  - "centers=2"
  - "C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절"
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
    <div class="research-overview__value">C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절</div>
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
    <div class="research-overview__value">객체지향 설계 · 함수 분해와 로직 구성</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">SVM 모델 학습 -&gt; 예측 결과 점검 -&gt; 데이터 분포 시각화</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 8 · 실행 8</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">numpy, matplotlib, sklearn</div>
  </div>
</div>

```python id="HhGdqQykQZBZ" executionInfo={"status": "ok", "timestamp": 1756718627791, "user_tz": -540, "elapsed": 3554, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
```

```python id="GFZ-aVcMQfBQ" executionInfo={"status": "ok", "timestamp": 1756718627798, "user_tz": -540, "elapsed": 21, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X_blob, y_blob = make_blobs(n_samples=50, centers=2, random_state=6)
# centers=2: 2차원으로 만들기 위한 것. centers=3이면 시각화 어려움
```

```python colab={"base_uri": "https://localhost:8080/", "height": 80} id="Ja0lLQTkQkAg" executionInfo={"status": "ok", "timestamp": 1756718878486, "user_tz": -540, "elapsed": 46, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fa741fea-3036-430c-c875-7b7775f7e6c3"
model_svc = SVC(kernel='rbf', C=10, gamma=0.001)          # C와 gamma설정 중요!
# C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절
model_svc.fit(X_blob, y_blob)
```

```python id="K3255CKGQpx2" executionInfo={"status": "ok", "timestamp": 1756718879134, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
xx, yy = np.meshgrid(np.linspace(X_blob[:, 0].min()-1, X_blob[:, 0].max()+1, 500),
                     np.linspace(X_blob[:, 1].min()-1, X_blob[:, 1].max()+1, 500))
```

```python id="2qj7xbwlQtvm" executionInfo={"status": "ok", "timestamp": 1756718880078, "user_tz": -540, "elapsed": 182, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
Z = model_svc.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
```

```python id="e4s5MJTKQy6j" executionInfo={"status": "ok", "timestamp": 1756718882306, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
def plot_decision_boundary(clf, X, y, ax, title):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

    ax.contourf(xx, yy, Z, alpha=0.3, cmap=cmap_light)
    ax.scatter(X[:, 0][y==0], X[:, 1][y==0], c='red', marker='o', label='Class 0')
    ax.scatter(X[:, 0][y==1], X[:, 1][y==1], c='blue', marker='x', label='Class 1')

    ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1],
               s=150, facecolors='none', edgecolors='black', linewidths=2, label='Support Vectors')

    ax.set_title(title)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend()
    ax.grid(True)

```

```python colab={"base_uri": "https://localhost:8080/", "height": 585} id="ynYMkkjCR9KC" executionInfo={"status": "ok", "timestamp": 1756718889856, "user_tz": -540, "elapsed": 402, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b15a6a0b-6875-464c-d4ea-fda27a6d8d91"
fig, ax = plt.subplots(figsize=(7, 6))
plot_decision_boundary(model_svc, X_blob, y_blob, ax, "SVM \nC=10, gamma=0.01")
plt.show()
```

```python id="XM-h7uT_QcOu" executionInfo={"status": "ok", "timestamp": 1756718628803, "user_tz": -540, "elapsed": 5, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}

```
