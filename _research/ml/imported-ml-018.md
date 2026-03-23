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

```python id="d6zf4oyt_dAf" executionInfo={"status": "ok", "timestamp": 1756708657867, "user_tz": -540, "elapsed": 5762, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score
```

```python id="Y3oisx2Q_sYs" executionInfo={"status": "ok", "timestamp": 1756708721892, "user_tz": -540, "elapsed": 32, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
wine = load_wine()
X, y = wine.data, wine.target
```

```python id="w010CgkG_sOq" executionInfo={"status": "ok", "timestamp": 1756708766735, "user_tz": -540, "elapsed": 7, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

```python id="YahPoN74AIOW" executionInfo={"status": "ok", "timestamp": 1756708808319, "user_tz": -540, "elapsed": 27, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# PCA 적용

pca = PCA()
X_pca_all = pca.fit_transform(X_scaled)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 391} id="1fQcYu3GASWi" executionInfo={"status": "ok", "timestamp": 1756709081535, "user_tz": -540, "elapsed": 483, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="93325ddf-f80b-41b1-f35b-50af050f98db"
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

```python colab={"base_uri": "https://localhost:8080/"} id="k5BgOv4NA8CN" executionInfo={"status": "ok", "timestamp": 1756709301075, "user_tz": -540, "elapsed": 10, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e8bad4ab-6c8f-4aea-eb14-d78350fc36da"
# 설명 비율 출력
for i, ratio in enumerate(pca.explained_variance_ratio_):
    print(f'PC{i+1}: {ratio:.2f}')
```

```python id="eml-HnQ-CJMe" executionInfo={"status": "ok", "timestamp": 1756710197383, "user_tz": -540, "elapsed": 5, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# PCA 적용 - 2차원 축소

pca = PCA(n_components=2)
X_pca_2d = pca.fit_transform(X_scaled)
```

```python id="nkkEuCeLCYbN" executionInfo={"status": "ok", "timestamp": 1756711412520, "user_tz": -540, "elapsed": 6, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# Kmeans

k = 3

kmeans = KMeans(n_clusters=k)
clusters = kmeans.fit_predict(X_pca_2d)          # fit_predict(): 학습과 동시에 클러스터 라벨 예측을 한번에 해주는 함수
```

```python colab={"base_uri": "https://localhost:8080/"} id="JdLLetxbFoq1" executionInfo={"status": "ok", "timestamp": 1756711413301, "user_tz": -540, "elapsed": 20, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e5b8470a-6c67-4c91-ee40-6a140f00d2f3"
# 클러스터링 평가 (실루엣 스코어)
sil_score = silhouette_score(X_pca_2d, clusters)
print(sil_score)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 391} id="nPdZgCNYF7zT" executionInfo={"status": "ok", "timestamp": 1756711271936, "user_tz": -540, "elapsed": 307, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b5412681-26f9-4a70-a7cc-5abcc529f10c"
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

<!-- #region id="ZSzgQ0DuIquA" -->
=> K=3일때 실루엣 스코어가 가장 높다!
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 718} id="TW1PAGoeHhUf" executionInfo={"status": "ok", "timestamp": 1756711418674, "user_tz": -540, "elapsed": 295, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="45f0a6ce-87d5-4482-c13b-43ec0287723a"
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

```python id="AU2ptnIkJemy"

```
