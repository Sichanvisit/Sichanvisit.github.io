---
title: "11.차원축소(KMeans+PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250901_코딩실습17_11.차원축소(KMeans+PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습17_11.차원축소(KMeans+PCA).md"
excerpt: "11.차원축소(KMeans+PCA)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 전처리와 입력 정리, 군집화, 차원 축소 순서로 큰 장을 먼저 훑고, KMeans 모델 학습, StandardScaler 스케일링 같은 코드로 실제 구현을 이어서 확인할 수..."
research_summary: "11.차원축소(KMeans+PCA)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 전처리와 입력 정리, 군집화, 차원 축소 순서로 큰 장을 먼저 훑고, KMeans 모델 학습, StandardScaler 스케일링 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, pandas입니다."
research_artifacts: "ipynb/md · 코드 12개 · 실행 11개"
code_block_count: 12
execution_block_count: 11
research_focus:
  - "스크리 플랏"
  - "=> K=3일때 실루엣 스코어가 가장 높다!"
  - "스크리플롯"
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
  - archive-note
---

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">=&gt; K=3일때 실루엣 스코어가 가장 높다!</div>
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
    <div class="research-overview__value">전처리와 입력 정리 · 군집화 · 차원 축소</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">데이터셋 불러오기 -&gt; KMeans 모델 학습 -&gt; StandardScaler 스케일링</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 12 · 실행 11</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn, matplotlib, pandas</div>
  </div>
</div>

```python
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score
```

```python
wine = load_wine()
X, y = wine.data, wine.target
```

```python
# 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

```python
# PCA 적용

pca = PCA()
X_pca_all = pca.fit_transform(X_scaled)
```

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

```python
# 설명 비율 출력
for i, ratio in enumerate(pca.explained_variance_ratio_):
    print(f'PC{i+1}: {ratio:.2f}')
```

```python
# PCA 적용 - 2차원 축소

pca = PCA(n_components=2)
X_pca_2d = pca.fit_transform(X_scaled)
```

```python
# Kmeans

k = 3

kmeans = KMeans(n_clusters=k)
clusters = kmeans.fit_predict(X_pca_2d)          # fit_predict(): 학습과 동시에 클러스터 라벨 예측을 한번에 해주는 함수
```

```python
# 클러스터링 평가 (실루엣 스코어)
sil_score = silhouette_score(X_pca_2d, clusters)
print(sil_score)
```

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

=> K=3일때 실루엣 스코어가 가장 높다!

```python
# 데이터 시각화

plt.figure(figsize=(10,8))
scatter = plt.scatter(X_pca_2d[:,0], X_pca_2d[:,1], c=clusters, cmap='Set1', alpha=0.7)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('KMeans + PCA')
plt.grid(True, alpha=0.4)
plt.colorbar(scatter, label='Cluster Label')
plt.show()
```

```python

```
