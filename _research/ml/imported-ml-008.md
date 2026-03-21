---
title: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md"
excerpt: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)를 중심으로 구현 중심 학습 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)를 중심으로 구현 중심 학습 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 Iris 데이터로 이진 분류, Iris 데이터로 다중 분류 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "Iris 데이터로 이진 분류"
  - "Iris 데이터로 다중 분류"
  - "Softmax 이용한 다중 분류"
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
  <div class="research-doc-hero__meta">
<div class="research-doc-hero__meta-item">
  <span>Source</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Artifacts</span>
  <strong>코드 19 · 실행 18</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>sklearn, matplotlib, numpy</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">legend_elements(). (handles, label) 두 값을 반환</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Data Context</p>
  <p class="research-doc-card__value">Iris 데이터로 이진 분류</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">구현 중심 학습</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">데이터 불러오기 -&gt; 모델 구성 -&gt; 평가</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">구현 중심 학습</p>
  <p class="research-note-card__body">이 글은 개념 설명과 함께 실제 코드를 통해 학습 흐름을 다시 따라가도록 정리된 ML 실습 기록입니다.</p>
  <p class="research-note-card__meta">데이터 입력, 처리, 모델링, 평가 가운데 실제로 손댄 단계를 중심으로 읽을 수 있습니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-grid">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">Iris 데이터로 이진 분류</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 데이터 로드</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 모델 구성</p>
  <p class="research-step-card__title">Iris 데이터로 다중 분류</p>
  <p class="research-step-card__body">LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>LogisticRegression</code> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 모델링 &amp; 시각화</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 평가</p>
  <p class="research-step-card__title">Iris 데이터로 이진 분류</p>
  <p class="research-step-card__body">예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 시각화용 격자 생성 코드</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 시각화</p>
  <p class="research-step-card__title">Softmax 이용한 다중 분류</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 시각화 · legend 지정 위한 코드</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 환경 준비</p>
  <p class="research-step-card__title">Iris 데이터로 이진 분류</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>LogisticRegression</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 구현 코드</p>
  <p class="research-step-card__title">Iris 데이터로 다중 분류</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 시각화용 격자 생성 코드</p>
</div>
</div>

## Code Evidence

### Iris 데이터로 이진 분류

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 데이터 로드
iris = load_iris()
```

### Iris 데이터로 다중 분류

**직접 해본 단계**: 모델 구성

**핵심 API**: `LogisticRegression`, `matplotlib`

LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
# 모델링 & 시각화

plt.figure(figsize=(10,3))

for i in range(3):
    binary_y = (y==i).astype(int)                  # OvR -> 이진 라벨 생성
    model = LogisticRegression()
    model.fit(X, binary_y)

    Z = model.predict(grid)
    Z = Z.reshape(xx.shape)

    plt.subplot(1, 3, i+1)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
    plt.scatter(X[:,0], X[:,1], c=binary_y, cmap='bwr', edgecolors='black')
    plt.title(f'Class {i} : {class_names[i]} vs Rest')
    plt.grid(True)

plt.tight_layout()
plt.show()
```

### Iris 데이터로 이진 분류

**직접 해본 단계**: 평가

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
# 시각화용 격자 생성 코드

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5          # x축
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5          # y축
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))           # 200X200 격자 생성
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])               # 모델이 예측한 클래스 라벨 계산
Z = Z.reshape(xx.shape)                                        # Z를 격자 형태로 변형 -> 2D
```

### Softmax 이용한 다중 분류

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
# 시각화

plt.figure(figsize=(5,3))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='Set1')
scatter = plt.scatter(X[:,0], X[:,1], c=y, cmap='Set1', edgecolors='black')

# legend 지정 위한 코드
handles, _ = scatter.legend_elements()

plt.title('Softmax')
plt.legend(handles, class_names, title="Classes")
plt.grid(True)
plt.show()
```

### Iris 데이터로 이진 분류

**직접 해본 단계**: 환경 준비

**핵심 API**: `LogisticRegression`

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
```

### Iris 데이터로 다중 분류

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# 시각화용 격자 생성 코드

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5          # x축
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5          # y축
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))           # 200X200 격자 생성
grid = np.c_[xx.ravel(), yy.ravel()]
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Source formats: `ipynb`, `md`
- Companion files: `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).ipynb`, `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`, `matplotlib.org`

## Note Preview

> - **legend_elements()** - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - label: 0, 1, 2처럼 자동 생성된 클래스 이름 문자열 - scatter.legend_elements()는 handles, label을 반환하지만, 클래스 이름을 실제 label로 사용해 보여주고자 함 - handles, _ = scatter.legend_elements()로 변수를 두 개 지정할 때, handles는 가져오고 labels는 무시한다는 의미로 **아래 밑줄**을 사용 - 아래 밑줄: 파이썬의 관례적인 표현 1. 사용하지 않는 값 무시 2. 표현식의 마지막 결과값 저장 3. 내부 문서 의미
