---
title: "코딩실습17 11.차원축소(KMeans+PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습17_11.차원축소(KMeans+PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습17_11.차원축소(KMeans+PCA).md"
excerpt: "=> K=3일때 실루엣 스코어가 가장 높다! 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다"
research_summary: "=> K=3일때 실루엣 스코어가 가장 높다! 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, pandas입니다."
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

=> K=3일때 실루엣 스코어가 가장 높다! 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, pandas입니다.

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

## What This Note Covers

### Overview

=> K=3일때 실루엣 스코어가 가장 높다!

### Key Step

클러스터링 평가 (실루엣 스코어)

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

## Implementation Flow

1. Overview: => K=3일때 실루엣 스코어가 가장 높다!
2. Key Step: 클러스터링 평가 (실루엣 스코어)

## Code Highlights

### from sklearn.datasets import load_wine

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

### 스크리플롯

`스크리플롯`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 스크리플롯 흐름이 주석과 함께 드러납니다.

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

### 스크리 플랏

`스크리 플랏`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 스크리 플랏 흐름이 주석과 함께 드러납니다.

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
