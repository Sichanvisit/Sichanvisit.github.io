---
title: "SVM"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250901_SVM"
source_path: "11_Machine_Learning/Code_Snippets/250901_SVM.md"
excerpt: "SVM를 중심으로 객체지향 설계, 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "SVM를 중심으로 객체지향 설계, 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 파생 변수 추가, SVM 모델 학습 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 8개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, matplotlib, sklearn입니다."
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

<div class="research-doc-hero">
  <div class="research-doc-summary">
    <p class="research-doc-summary__label">문제 설정</p>
    <p class="research-doc-summary__body">C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절</p>
  </div>
  <div class="research-doc-meta">
<div class="research-doc-card">
  <p class="research-doc-card__label">핵심 개념</p>
  <p class="research-doc-card__value">객체지향 설계 · 함수 분해와 로직 구성</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">구현 포인트</p>
  <p class="research-doc-card__value">파생 변수 추가 · SVM 모델 학습 · 데이터 분포 시각화</p>
</div>
  </div>
  <div class="research-doc-stats">
<div class="research-doc-stat">
  <span>소스</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-stat">
  <span>자료</span>
  <strong>코드 8 · 실행 8</strong>
</div>
<div class="research-doc-stat">
  <span>주요 스택</span>
  <strong>numpy, matplotlib, sklearn</strong>
</div>
  </div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">객체지향 설계</p>
  <p class="research-note-card__body">객체지향은 관련 데이터와 동작을 하나의 객체로 묶어 문제를 구조적으로 표현하는 방식입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 클래스, 메서드, 상태 관리 같은 코드가 핵심 학습 포인트로 드러납니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">함수 분해와 로직 구성</p>
  <p class="research-note-card__body">함수는 입력, 처리, 반환을 분리해 로직을 재사용하기 쉽게 만들고, 문제를 작은 단위로 나누는 기본 도구입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 문제 풀이를 함수 단위로 쪼개고 입출력을 나눠 보는 실습과 연결됩니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-list">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 피처 가공</p>
  <p class="research-step-card__title">파생 변수 추가</p>
  <p class="research-step-card__body">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 학습</p>
  <p class="research-step-card__title">SVM 모델 학습</p>
  <p class="research-step-card__body">훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> C: cost (오분류에 대한 패널티 강도), gamma...</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 시각화</p>
  <p class="research-step-card__title">데이터 분포 시각화</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 환경 준비</p>
  <p class="research-step-card__title">import numpy as np</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 구현 코드</p>
  <p class="research-step-card__title">X_blob, y_blob = make_blobs(n_samples=50, centers=2, random_state=6)</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> centers=2</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 구현 코드</p>
  <p class="research-step-card__title">xx, yy = np.meshgrid(np.linspace(X_blob[:, 0].min()-1, X_blob[:, 0].max()+1,...</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
</div>

## Code Evidence

### 파생 변수 추가

**직접 해본 단계**: 피처 가공

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
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

### SVM 모델 학습

**직접 해본 단계**: 학습

훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.

```python
model_svc = SVC(kernel='rbf', C=10, gamma=0.001)          # C와 gamma설정 중요!
# C: cost (오분류에 대한 패널티 강도), gamma: 커널 곡률 조절
model_svc.fit(X_blob, y_blob)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
fig, ax = plt.subplots(figsize=(7, 6))
plot_decision_boundary(model_svc, X_blob, y_blob, ax, "SVM \nC=10, gamma=0.01")
plt.show()
```

### import numpy as np

**직접 해본 단계**: 환경 준비

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
```

### X_blob, y_blob = make_blobs(n_samples=50, centers=2, random_state=6)

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
X_blob, y_blob = make_blobs(n_samples=50, centers=2, random_state=6)
# centers=2: 2차원으로 만들기 위한 것. centers=3이면 시각화 어려움
```

### xx, yy = np.meshgrid(np.linspace(X_blob[:, 0].min()-1, X_blob[:, 0].max()+1,...

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
xx, yy = np.meshgrid(np.linspace(X_blob[:, 0].min()-1, X_blob[:, 0].max()+1, 500),
                     np.linspace(X_blob[:, 1].min()-1, X_blob[:, 1].max()+1, 500))
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250901_SVM.md`
- Source formats: `ipynb`, `md`
- Companion files: `250901_SVM.ipynb`, `250901_SVM.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
