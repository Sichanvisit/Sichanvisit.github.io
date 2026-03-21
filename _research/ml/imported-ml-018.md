---
title: "코딩실습17 11.차원축소(KMeans+PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습17_11.차원축소(KMeans+PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습17_11.차원축소(KMeans+PCA).md"
excerpt: "=> K=3일때 실루엣 스코어가 가장 높다! 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다"
research_summary: "=> K=3일때 실루엣 스코어가 가장 높다! 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, pandas입니다."
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

=> K=3일때 실루엣 스코어가 가장 높다! 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, pandas입니다.

**빠르게 볼 수 있는 포인트**: => K=3일때 실루엣 스코어가 가장 높다!, 표준화, PCA 적용.

**남겨둔 자료**: `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, pandas입니다.

**주요 스택**: `sklearn`, `matplotlib`, `pandas`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 12 |
| Execution Cells | 11 |
| Libraries | `sklearn`, `matplotlib`, `pandas` |
| Source Note | `250901_코딩실습17_11.차원축소(KMeans+PCA)` |

## What I Studied

### Overview

=> K=3일때 실루엣 스코어가 가장 높다!

### Key Step

클러스터링 평가 (실루엣 스코어)

## What I Tried in Code

1. 데이터 불러오기: wine = load_wine()
2. 전처리: StandardScaler 스케일링
3. 학습: KMeans 모델 학습
4. 시각화: 데이터 분포 시각화
5. 환경 준비: from sklearn.datasets import load_wine
6. 구현 코드: Kmeans

## Code Evidence

### wine = load_wine()

**직접 해본 단계**: 데이터 불러오기

`wine = load_wine()`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
wine = load_wine()
X, y = wine.data, wine.target
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

`StandardScaler 스케일링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다. 코드에는 표준화 같은 처리 포인트도 함께 남아 있습니다.

```python
# 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### KMeans 모델 학습

**직접 해본 단계**: 학습

`KMeans 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다. 코드에는 스크리 플랏 같은 처리 포인트도 함께 남아 있습니다.

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

`데이터 분포 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 스크리플롯 같은 처리 포인트도 함께 남아 있습니다.

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

`from sklearn.datasets import load_wine`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

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

`Kmeans`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 학습된 모델로 추론을 수행하고 예측 결과를 점검하는 코드입니다. 코드에는 Kmeans 같은 처리 포인트도 함께 남아 있습니다.

```python
# Kmeans

k = 3

kmeans = KMeans(n_clusters=k)
clusters = kmeans.fit_predict(X_pca_2d)          # fit_predict(): 학습과 동시에 클러스터 라벨 예측을 한번에 해주는 함수
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `wine = load_wine()` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 전처리 코드를 남기는 이유

- 왜 필요한가: 머신러닝에선 모델보다 먼저 입력 데이터의 결측치, 범주형 값, 스케일을 어떻게 다뤘는지가 성능을 크게 바꿉니다.
- 왜 이 방식을 쓰는가: 그래서 `StandardScaler 스케일링` 같은 코드를 통해 실제로 어떤 정제 규칙을 적용했는지 문장보다 코드로 먼저 보여주도록 정리했습니다.
- 원리: 원본 데이터를 모델이 다루기 쉬운 수치 형태로 바꾸면 같은 알고리즘이어도 학습 안정성과 해석 가능성이 함께 올라갑니다.

### 학습 코드를 따로 보는 이유

- 왜 필요한가: 모델 선언만으로는 끝나지 않고 fitting, 검증 분리, 하이퍼파라미터 탐색까지 봐야 실제로 해본 실습으로 읽힙니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `KMeans 모델 학습` 코드를 남겨 학습 루프나 GridSearchCV처럼 성능을 끌어올리기 위해 손댄 지점을 보여줍니다.
- 원리: 훈련 과정은 데이터에서 패턴을 찾도록 파라미터를 조정하는 단계이며, 검증이 함께 있어야 과적합 여부도 판단할 수 있습니다.

### 시각화를 같이 남긴 이유

- 왜 필요한가: 숫자만 보면 놓치기 쉬운 분포와 이상치를 그래프로 확인해야 다음 전처리나 feature engineering 방향이 또렷해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `데이터 분포 시각화` 코드를 통해 어떤 그래프를 보고 판단했는지 실습 흔적을 남겼습니다.
- 원리: 시각화는 데이터 분포를 직관적으로 드러내 모델 선택과 변수 설계의 근거를 만들어 줍니다.

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
