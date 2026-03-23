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

### 데이터 설명

64차원의 손글씨 데이터

사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

```python
from sklearn.datasets import load_digits                      # 손글씨 이미지 (64차원)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
```

```python
# 데이터 불러오기
X, y = load_digits(return_X_y=True)
```

```python
X
```

```python
y
```

```python
# 데이터 표준화

X_scaled = StandardScaler().fit_transform(X)
```

```python
X_scaled
```

```python
# PCA전 시각화

plt.figure(figsize=(6,4))
scatter = plt.scatter(X[:,0], X[:,1], c=y, cmap='tab10', alpha=0.7)
plt.xlabel('X1')
plt.ylabel('X2')
plt.colorbar(scatter, label="Digit Label")
plt.show()
```

```python
# 차원 축소
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

```python
# PCA 후 시각화

plt.figure(figsize=(6,4))
scatter = plt.scatter(X_pca[:,0], X_pca[:,1], c=y, cmap='tab10', alpha=0.7)
plt.xlabel('X1')
plt.ylabel('X2')
plt.colorbar(scatter, label="Digit Label")
plt.show()
```

```python
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

```python

```
