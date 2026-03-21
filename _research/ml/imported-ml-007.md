---
title: "코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md"
excerpt: "데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할 중심으로 구현 과정을 정리한 코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge) 기록입니다"
research_summary: "데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할 중심으로 구현 과정을 정리한 코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge) 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "데이터 불러오기"
  - "위와 같은 코드"
  - "테스트 데이터 트레이닝 데이터 분할"
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

데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할 중심으로 구현 과정을 정리한 코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge) 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다.

**빠르게 볼 수 있는 포인트**: 데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할.

**남겨둔 자료**: `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다.

**주요 스택**: `sklearn`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 19 |
| Execution Cells | 18 |
| Libraries | `sklearn` |
| Source Note | `250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge)` |

## What I Studied

- 데이터 불러오기
- 위와 같은 코드
- 테스트 데이터 트레이닝 데이터 분할
- 모델링
- 릿지 회귀 모델링

## What I Tried in Code

1. 데이터 불러오기: 데이터 불러오기
2. 모델 구성: LinearRegression 모델 구성
3. 학습: Ridge 모델 학습
4. 평가: 회귀 성능 평가
5. 환경 준비: from sklearn.datasets import fetch_california_hou...
6. 구현 코드: 테스트 데이터 트레이닝 데이터 분할

## Code Evidence

### 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

`데이터 불러오기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다. 코드에는 데이터 불러오기 같은 처리 포인트도 함께 남아 있습니다.

```python
# 데이터 불러오기
X, y = fetch_california_housing(return_X_y = True)
```

### LinearRegression 모델 구성

**직접 해본 단계**: 모델 구성

`LinearRegression 모델 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. LinearRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다. 코드에는 모델링 같은 처리 포인트도 함께 남아 있습니다.

```python
# 모델링
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
```

### Ridge 모델 학습

**직접 해본 단계**: 학습

`Ridge 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다. 코드에는 릿지 회귀 모델링 같은 처리 포인트도 함께 남아 있습니다.

```python
# 릿지 회귀 모델링
model_ridge = Ridge(alpha=0.9)
model_ridge.fit(X_train, y_train)
```

### 회귀 성능 평가

**직접 해본 단계**: 평가

`회귀 성능 평가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
print("LR MSE: ", mean_squared_error(y_test, model_lr.predict(X_test)))
print("Ridge MSE: ", mean_squared_error(y_test, model_ridge.predict(X_test)))
print("Lasso MSE: ", mean_squared_error(y_test, model_lasso.predict(X_test)))
print("Elastic MSE: ", mean_squared_error(y_test, model_elastic.predict(X_test)))
```

### from sklearn.datasets import fetch_california_housing

**직접 해본 단계**: 환경 준비

`from sklearn.datasets import fetch_california_housing`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
from sklearn.datasets import fetch_california_housing
```

### 테스트 데이터 트레이닝 데이터 분할

**직접 해본 단계**: 구현 코드

`테스트 데이터 트레이닝 데이터 분할`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다. 코드에는 테스트 데이터 트레이닝 데이터 분할 같은 처리 포인트도 함께 남아 있습니다.

```python
# 테스트 데이터 트레이닝 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `데이터 불러오기` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `LinearRegression 모델 구성`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

### 학습 코드를 따로 보는 이유

- 왜 필요한가: 모델 선언만으로는 끝나지 않고 fitting, 검증 분리, 하이퍼파라미터 탐색까지 봐야 실제로 해본 실습으로 읽힙니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `Ridge 모델 학습` 코드를 남겨 학습 루프나 GridSearchCV처럼 성능을 끌어올리기 위해 손댄 지점을 보여줍니다.
- 원리: 훈련 과정은 데이터에서 패턴을 찾도록 파라미터를 조정하는 단계이며, 검증이 함께 있어야 과적합 여부도 판단할 수 있습니다.

### 지표 계산까지 남긴 이유

- 왜 필요한가: 예측을 했더라도 어떤 기준으로 잘했는지 판단하지 않으면 실험 비교가 성립하지 않습니다.
- 왜 이 방식을 쓰는가: 그래서 `회귀 성능 평가` 코드를 통해 정확도, F1, RMSLE 같은 지표를 실제로 어떻게 계산했는지 함께 남겼습니다.
- 원리: 평가 지표는 예측 결과를 수치화해 모델 선택과 개선 방향을 정하는 기준점 역할을 합니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md`
- Source formats: `ipynb`, `md`
- Companion files: `250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).ipynb`, `250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
