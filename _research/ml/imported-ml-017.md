---
title: "코딩실습16 11.차원축소(PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습16_11.차원축소(PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md"
excerpt: "코딩실습16 11.차원축소(PCA)를 중심으로 차원 축소, 전처리와 입력 정리 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습16 11.차원축소(PCA)를 중심으로 차원 축소, 전처리와 입력 정리 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 데이터 설명, StandardScaler 스케일링 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다."
research_artifacts: "ipynb/md · 코드 11개 · 실행 10개"
code_block_count: 11
execution_block_count: 10
research_focus:
  - "사이킷런"
  - "데이터 설명"
  - "데이터 불러오기"
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
  <strong>코드 11 · 실행 10</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>sklearn, matplotlib</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Data Context</p>
  <p class="research-doc-card__value">사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">차원 축소 · 전처리와 입력 정리</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">데이터 불러오기 -&gt; 전처리 -&gt; 시각화</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
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
  <p class="research-step-card__title">데이터 설명</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 데이터 불러오기</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 전처리</p>
  <p class="research-step-card__title">StandardScaler 스케일링</p>
  <p class="research-step-card__body">결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>StandardScaler</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 데이터 표준화</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 시각화</p>
  <p class="research-step-card__title">데이터 분포 시각화</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 스크리플롯</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 환경 준비</p>
  <p class="research-step-card__title">데이터 설명</p>
  <p class="research-step-card__body">전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>StandardScaler</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 구현 코드</p>
  <p class="research-step-card__title">데이터 설명</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>PCA</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 차원 축소</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 시각화</p>
  <p class="research-step-card__title">데이터 분포 시각화</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> PCA전 시각화</p>
</div>
</div>

## Code Evidence

### 데이터 설명

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 데이터 불러오기
X, y = load_digits(return_X_y=True)
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

**핵심 API**: `StandardScaler`

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

```python
# 데이터 표준화

X_scaled = StandardScaler().fit_transform(X)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

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

### 데이터 설명

**직접 해본 단계**: 환경 준비

**핵심 API**: `StandardScaler`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import load_digits                      # 손글씨 이미지 (64차원)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
```

### 데이터 설명

**직접 해본 단계**: 구현 코드

**핵심 API**: `PCA`

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# 차원 축소
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
# PCA전 시각화

plt.figure(figsize=(6,4))
scatter = plt.scatter(X[:,0], X[:,1], c=y, cmap='tab10', alpha=0.7)
plt.xlabel('X1')
plt.ylabel('X2')
plt.colorbar(scatter, label="Digit Label")
plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md`
- Source formats: `ipynb`, `md`
- Companion files: `250901_코딩실습16_11.차원축소(PCA).ipynb`, `250901_코딩실습16_11.차원축소(PCA).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## Note Preview

> 64차원의 손글씨 데이터
> 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
