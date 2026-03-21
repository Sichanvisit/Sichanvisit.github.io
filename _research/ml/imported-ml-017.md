---
title: "코딩실습16 11.차원축소(PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습16_11.차원축소(PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md"
excerpt: "사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html"
research_summary: "사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다."
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

사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: 사이킷런, 데이터 설명, 데이터 불러오기.

**남겨둔 자료**: `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다.

**주요 스택**: `sklearn`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 11 |
| Execution Cells | 10 |
| Libraries | `sklearn`, `matplotlib` |
| Source Note | `250901_코딩실습16_11.차원축소(PCA)` |

## What I Studied

### 데이터 설명

사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

## What I Tried in Code

1. 데이터 불러오기: 데이터 설명
2. 전처리: StandardScaler 스케일링
3. 시각화: 데이터 분포 시각화
4. 환경 준비: 데이터 설명
5. 구현 코드: 데이터 설명

## Code Evidence

### 데이터 설명

**직접 해본 단계**: 데이터 불러오기

`데이터 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다. 코드에는 데이터 불러오기 같은 처리 포인트도 함께 남아 있습니다.

```python
# 데이터 불러오기
X, y = load_digits(return_X_y=True)
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

`StandardScaler 스케일링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다. 코드에는 데이터 표준화 같은 처리 포인트도 함께 남아 있습니다.

```python
# 데이터 표준화

X_scaled = StandardScaler().fit_transform(X)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

`데이터 분포 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 스크리플롯 같은 처리 포인트도 함께 남아 있습니다.

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

`데이터 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import load_digits                      # 손글씨 이미지 (64차원)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
```

### 데이터 설명

**직접 해본 단계**: 구현 코드

`데이터 설명`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 차원 축소 같은 처리 포인트도 함께 남아 있습니다.

```python
# 차원 축소
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

`데이터 분포 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 PCA전 시각화 같은 처리 포인트도 함께 남아 있습니다.

```python
# PCA전 시각화

plt.figure(figsize=(6,4))
scatter = plt.scatter(X[:,0], X[:,1], c=y, cmap='tab10', alpha=0.7)
plt.xlabel('X1')
plt.ylabel('X2')
plt.colorbar(scatter, label="Digit Label")
plt.show()
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `데이터 설명` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 전처리 코드를 남기는 이유

- 왜 필요한가: 머신러닝에선 모델보다 먼저 입력 데이터의 결측치, 범주형 값, 스케일을 어떻게 다뤘는지가 성능을 크게 바꿉니다.
- 왜 이 방식을 쓰는가: 그래서 `StandardScaler 스케일링` 같은 코드를 통해 실제로 어떤 정제 규칙을 적용했는지 문장보다 코드로 먼저 보여주도록 정리했습니다.
- 원리: 원본 데이터를 모델이 다루기 쉬운 수치 형태로 바꾸면 같은 알고리즘이어도 학습 안정성과 해석 가능성이 함께 올라갑니다.

### 시각화를 같이 남긴 이유

- 왜 필요한가: 숫자만 보면 놓치기 쉬운 분포와 이상치를 그래프로 확인해야 다음 전처리나 feature engineering 방향이 또렷해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `데이터 분포 시각화` 코드를 통해 어떤 그래프를 보고 판단했는지 실습 흔적을 남겼습니다.
- 원리: 시각화는 데이터 분포를 직관적으로 드러내 모델 선택과 변수 설계의 근거를 만들어 줍니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `데이터 설명` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

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
