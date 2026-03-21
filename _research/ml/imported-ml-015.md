---
title: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN)"
source_path: "11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md"
excerpt: "사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html"
research_summary: "사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
research_artifacts: "ipynb/md · 코드 13개 · 실행 13개"
code_block_count: 13
execution_block_count: 13
research_focus:
  - "사이킷런 링크"
  - "표준화"
  - "최적의 K값으로 학습 및 평가"
research_stack:
  - "sklearn"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다.

**빠르게 볼 수 있는 포인트**: 사이킷런 링크, 표준화, 최적의 K값으로 학습 및 평가.

**남겨둔 자료**: `ipynb/md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다.

**주요 스택**: `sklearn`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 13 |
| Execution Cells | 13 |
| Libraries | `sklearn` |
| Source Note | `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN)` |

## What I Studied

### Overview

사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html

### Key Step

최적의 K값으로 학습 및 평가

## What I Tried in Code

1. 데이터 불러오기: wine = load_wine()
2. 전처리: StandardScaler 스케일링
3. 모델 구성: KNN 모델 구성
4. 평가: 예측 결과 점검
5. 환경 준비: from sklearn.datasets import load_wine
6. 구현 코드: best_k = grid.best_params_['n_neighbors']

## Code Evidence

### wine = load_wine()

**직접 해본 단계**: 데이터 불러오기

`wine = load_wine()`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
wine = load_wine()
X, y = wine.data, wine.target
target_names = wine.target_names
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

`StandardScaler 스케일링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다. 코드에는 표준화 같은 처리 포인트도 함께 남아 있습니다.

```python
# 표준화

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
```

### KNN 모델 구성

**직접 해본 단계**: 모델 구성

`KNN 모델 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. KNN 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
```

### 예측 결과 점검

**직접 해본 단계**: 평가

`예측 결과 점검`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다. 코드에는 최적의 K값으로 학습 및 평가 같은 처리 포인트도 함께 남아 있습니다.

```python
# 최적의 K값으로 학습 및 평가
best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test_scaled)
```

### from sklearn.datasets import load_wine

**직접 해본 단계**: 환경 준비

`from sklearn.datasets import load_wine`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

### best_k = grid.best_params_['n_neighbors']

**직접 해본 단계**: 구현 코드

`best_k = grid.best_params_['n_neighbors']`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
best_k = grid.best_params_['n_neighbors']
best_k
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

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `KNN 모델 구성`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

### 지표 계산까지 남긴 이유

- 왜 필요한가: 예측을 했더라도 어떤 기준으로 잘했는지 판단하지 않으면 실험 비교가 성립하지 않습니다.
- 왜 이 방식을 쓰는가: 그래서 `예측 결과 점검` 코드를 통해 정확도, F1, RMSLE 같은 지표를 실제로 어떻게 계산했는지 함께 남겼습니다.
- 원리: 평가 지표는 예측 결과를 수치화해 모델 선택과 개선 방향을 정하는 기준점 역할을 합니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md`
- Source formats: `ipynb`, `md`
- Companion files: `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).ipynb`, `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## Note Preview

> 사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
> - 클래스 수: 3개 - 샘플 수: 총 178개 (class_0: 59, class_1: 71, class_2: 48) - 피처 수: 13개 (연속형, 모두 양수) - 출처: UCI 머신러닝 저장소의 Wine 데이터셋 (값 일부 포맷화됨)
