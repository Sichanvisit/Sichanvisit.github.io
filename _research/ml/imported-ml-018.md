---
title: "코딩실습17 11.차원축소(KMeans+PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습17_11.차원축소(KMeans+PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습17_11.차원축소(KMeans+PCA).md"
excerpt: "코딩실습17 11.차원축소(KMeans+PCA)를 중심으로 군집화, 차원 축소 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습17 11.차원축소(KMeans+PCA)를 중심으로 군집화, 차원 축소 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 wine = load_wine(), StandardScaler 스케일링 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, pandas입니다."
research_artifacts: "ipynb/md · 코드 12개 · 실행 11개"
code_block_count: 12
execution_block_count: 11
research_focus:
  - "=> K=3일때 실루엣 스코어가 가장 높다!"
  - "표준화"
  - "PCA 적용"
research_stack:
  - "sklearn"
  - "matplotlib"
  - "pandas"
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
  <strong>코드 12 · 실행 11</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>sklearn, matplotlib, pandas</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">=&gt; K=3일때 실루엣 스코어가 가장 높다!</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">군집화 · 차원 축소 · 전처리와 입력 정리</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">데이터 불러오기 -&gt; 전처리 -&gt; 학습</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">군집화</p>
  <p class="research-note-card__body">군집화는 정답 라벨 없이 비슷한 샘플끼리 묶어 데이터 구조를 탐색하는 비지도 학습 방법입니다.</p>
  <p class="research-note-card__meta">이 글에서는 KMeans, 군집 시각화, 클러스터 품질 점검 같은 흐름과 연결됩니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">차원 축소</p>
  <p class="research-note-card__body">차원 축소는 많은 변수의 정보를 더 적은 축으로 압축해 시각화, 노이즈 감소, 계산 효율 개선에 활용하는 기법입니다.</p>
  <p class="research-note-card__meta">이 글에서는 PCA처럼 분산을 최대한 보존하는 축을 찾아 데이터를 다시 표현하는 실습과 이어집니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">전처리와 입력 정리</p>
  <p class="research-note-card__body">머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.</p>
  <p class="research-note-card__meta">이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-grid">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">wine = load_wine()</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 전처리</p>
  <p class="research-step-card__title">StandardScaler 스케일링</p>
  <p class="research-step-card__body">결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>StandardScaler</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 표준화</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 학습</p>
  <p class="research-step-card__title">KMeans 모델 학습</p>
  <p class="research-step-card__body">훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>KMeans</code> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 스크리 플랏</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 시각화</p>
  <p class="research-step-card__title">데이터 분포 시각화</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 스크리플롯</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 환경 준비</p>
  <p class="research-step-card__title">from sklearn.datasets import load_wine</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>StandardScaler</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 구현 코드</p>
  <p class="research-step-card__title">Kmeans</p>
  <p class="research-step-card__body">학습된 모델로 추론을 수행하고 예측 결과를 점검하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>KMeans</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> Kmeans</p>
</div>
</div>

## Code Evidence

### wine = load_wine()

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
wine = load_wine()
X, y = wine.data, wine.target
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

**핵심 API**: `StandardScaler`

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

```python
# 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### KMeans 모델 학습

**직접 해본 단계**: 학습

**핵심 API**: `KMeans`, `matplotlib`

훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.

```python
# 스크리 플랏

sse = []                                            # SSE 저장용 빈 리스트
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(X_pca_2d)
    sse.append(kmeans.inertia_)                      # inertia_: 각 클러스터 중심에서 데이터까지 거리 제곱합

plt.figure(figsize=(8,4))
plt.plot(k_range, sse, marker='o', linestyle='--')
plt.title('Elbow Method')
plt.grid(True)
plt.xticks(k_range)
plt.show()
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
# 스크리플롯

plt.figure(figsize=(6,4))
plt.plot(
    range(1, len(pca.explained_variance_ratio_)+1),           # X축
    pca.explained_variance_ratio_,                            # y축
    marker='o', linestyle='--'
)
plt.title('Scree Plot')
plt.xticks(range(1, len(pca.explained_variance_ratio_)+1))
plt.grid(True)
plt.show()
```

### from sklearn.datasets import load_wine

**직접 해본 단계**: 환경 준비

**핵심 API**: `StandardScaler`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score
```

### Kmeans

**직접 해본 단계**: 구현 코드

**핵심 API**: `KMeans`

학습된 모델로 추론을 수행하고 예측 결과를 점검하는 코드입니다.

```python
# Kmeans

k = 3

kmeans = KMeans(n_clusters=k)
clusters = kmeans.fit_predict(X_pca_2d)          # fit_predict(): 학습과 동시에 클러스터 라벨 예측을 한번에 해주는 함수
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250901_코딩실습17_11.차원축소(KMeans+PCA).md`
- Source formats: `ipynb`, `md`
- Companion files: `250901_코딩실습17_11.차원축소(KMeans+PCA).ipynb`, `250901_코딩실습17_11.차원축소(KMeans+PCA).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> => K=3일때 실루엣 스코어가 가장 높다!
