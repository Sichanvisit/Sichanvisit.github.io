---
title: "11.차원축소(PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250901_코딩실습16_11.차원축소(PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md"
excerpt: "11.차원축소(PCA)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 설명 순서로 큰 장을 먼저 훑고, StandardScaler 스케일링, 데이터셋 불러오기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 11개..."
research_summary: "11.차원축소(PCA)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 설명 순서로 큰 장을 먼저 훑고, StandardScaler 스케일링, 데이터셋 불러오기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다."
research_artifacts: "ipynb/md · 코드 11개 · 실행 10개"
code_block_count: 11
execution_block_count: 10
research_focus:
  - "사이킷런"
  - "데이터 설명"
  - "스크리플롯"
research_stack:
  - "sklearn"
  - "matplotlib"
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
    <div class="research-overview__value">64차원의 손글씨 데이터 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">데이터 설명</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">64차원의 손글씨 데이터 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">데이터 설명</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">데이터셋 불러오기 -&gt; StandardScaler 스케일링 -&gt; 데이터 분포 시각화</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 11 · 실행 10</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn, matplotlib</div>
  </div>
</div>

<!-- #region id="FuAfhLtylZic" -->
# 데이터 설명

64차원의 손글씨 데이터

사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
<!-- #endregion -->

```python id="L7UPuGyjkjij" executionInfo={"status": "ok", "timestamp": 1756703954733, "user_tz": -540, "elapsed": 47, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import load_digits                      # 손글씨 이미지 (64차원)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
```

```python id="Oq65G6wclhwf" executionInfo={"status": "ok", "timestamp": 1756703955546, "user_tz": -540, "elapsed": 42, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 데이터 불러오기
X, y = load_digits(return_X_y=True)
```

```python colab={"base_uri": "https://localhost:8080/"} id="jTJ1rnY5lpJw" executionInfo={"status": "ok", "timestamp": 1756701843019, "user_tz": -540, "elapsed": 21, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bed374be-6d96-4979-90fa-b52f40f411a8"
X
```

```python colab={"base_uri": "https://localhost:8080/"} id="MhjIEDkVlt1J" executionInfo={"status": "ok", "timestamp": 1756701860317, "user_tz": -540, "elapsed": 28, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="299d63d2-06e7-43fc-bcb2-e870d480e629"
y
```

```python id="38rQCl7vlyDB" executionInfo={"status": "ok", "timestamp": 1756703959619, "user_tz": -540, "elapsed": 5, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 데이터 표준화

X_scaled = StandardScaler().fit_transform(X)
```

```python colab={"base_uri": "https://localhost:8080/"} id="E96safzVmYlZ" executionInfo={"status": "ok", "timestamp": 1756702029582, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fe8fb103-3a35-421d-a2c9-a1ea32c5ed74"
X_scaled
```

```python colab={"base_uri": "https://localhost:8080/", "height": 393} id="ShKHw1q8mbYX" executionInfo={"status": "ok", "timestamp": 1756702213407, "user_tz": -540, "elapsed": 246, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="79256e29-3a2c-4db5-c6a5-f9bcf9b06ade"
# PCA전 시각화

plt.figure(figsize=(6,4))
scatter = plt.scatter(X[:,0], X[:,1], c=y, cmap='tab10', alpha=0.7)
plt.xlabel('X1')
plt.ylabel('X2')
plt.colorbar(scatter, label="Digit Label")
plt.show()
```

```python id="ltGk_u6sm8YB" executionInfo={"status": "ok", "timestamp": 1756703566307, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 차원 축소
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 393} id="aJFOCfFCsSjK" executionInfo={"status": "ok", "timestamp": 1756703619909, "user_tz": -540, "elapsed": 554, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="cb6302f3-6954-4d95-ea45-bb6384c04307"
# PCA 후 시각화

plt.figure(figsize=(6,4))
scatter = plt.scatter(X_pca[:,0], X_pca[:,1], c=y, cmap='tab10', alpha=0.7)
plt.xlabel('X1')
plt.ylabel('X2')
plt.colorbar(scatter, label="Digit Label")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 388} id="eIscz2g3snE1" executionInfo={"status": "ok", "timestamp": 1756703967000, "user_tz": -540, "elapsed": 175, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4a028e81-e4e2-4438-c394-f66540347e51"
# 스크리플롯

plt.figure(figsize=(12,4))
plt.plot(
        range(1, len(pca.explained_variance_ratio_)+1),        # X축
        pca.explained_variance_,                               # Y축
        marker='o', linestyle='--'
        )
plt.title("Scree plot")
plt.grid(True)
plt.show()
```

```python id="SgWQ7Rc_tnI3"

```
