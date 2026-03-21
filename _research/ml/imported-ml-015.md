---
title: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN)"
source_path: "11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md"
excerpt: "사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html"
research_summary: "사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
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

사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다.

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

## What This Note Covers

### Overview

사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html

### Key Step

최적의 K값으로 학습 및 평가

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

### 평가 지표 해석

- 왜 필요한가: 정확도 하나만으로는 모델이 실제로 무엇을 잘하고 무엇을 놓치는지 충분히 설명할 수 없습니다.
- 왜 이 방식을 쓰는가: 문제 유형에 맞는 지표를 함께 보면 불균형 데이터, 오차 크기, 재현율 같은 중요한 관점을 놓치지 않을 수 있습니다.
- 원리: 예측 결과를 정답과 비교해 오차나 클래스별 성능을 수치화하고, 그 수치로 모델 선택과 개선 방향을 판단합니다.

## Implementation Flow

1. Overview: 사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
2. Key Step: 최적의 K값으로 학습 및 평가

## Code Highlights

### from sklearn.datasets import load_wine

`from sklearn.datasets import load_wine`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. / 피처 이름 / 설명 / / ------------------------------- / ------------------ / / alcohol / 알코올 함량 / / malic\_acid / 말산 함량 / / ash / 회분 함량 / / alcalinity\_of\_ash / 회분의 알칼리도 / / magnesium / 마그네슘 함량 / / total\_phenols / 총 페놀 / / flavanoids / 플라바노이드 / / nonflavanoid\_phenols / 비플라바노이드 페놀 / / proanthocyanins / 프로안토시아니딘 / / color\_intensity / 색 농도 / / hue / 색조 / / od280/od315\_of\_diluted\_wines / 희석 와인의 OD280/OD315 / / proline / 프롤린 /.

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

### knn = KNeighborsClassifier(n_neighbors=1)

`knn = KNeighborsClassifier(n_neighbors=1)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. / 피처 이름 / 설명 / / ------------------------------- / ------------------ / / alcohol / 알코올 함량 / / malic\_acid / 말산 함량 / / ash / 회분 함량 / / alcalinity\_of\_ash / 회분의 알칼리도 / / magnesium / 마그네슘 함량 / / total\_phenols / 총 페놀 / / flavanoids / 플라바노이드 / / nonflavanoid\_phenols / 비플라바노이드 페놀 / / proanthocyanins / 프로안토시아니딘 / / color\_intensity / 색 농도 / / hue / 색조 / / od280/od315\_of\_diluted\_wines / 희석 와인의 OD280/OD315 / / proline / 프롤린 /.

```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
```

### param_grid = {'n_neighbors': range(1, 31)}

`param_grid = {'n_neighbors': range(1, 31)}`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. / 피처 이름 / 설명 / / ------------------------------- / ------------------ / / alcohol / 알코올 함량 / / malic\_acid / 말산 함량 / / ash / 회분 함량 / / alcalinity\_of\_ash / 회분의 알칼리도 / / magnesium / 마그네슘 함량 / / total\_phenols / 총 페놀 / / flavanoids / 플라바노이드 / / nonflavanoid\_phenols / 비플라바노이드 페놀 / / proanthocyanins / 프로안토시아니딘 / / color\_intensity / 색 농도 / / hue / 색조 / / od280/od315\_of\_diluted\_wines / 희석 와인의 OD280/OD315 / / proline / 프롤린 /.

```python
param_grid = {'n_neighbors': range(1, 31)}
grid = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
grid.fit(X_train_scaled, y_train)
```

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
