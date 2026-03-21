---
title: "코딩실습13 10.결정트리와 앙상블(XGBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습13_10.결정트리와 앙상블(XGBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md"
excerpt: "XGBoost 회귀, XGBoost 분류 중심으로 구현 과정을 정리한 코딩실습13 10.결정트리와 앙상블(XGBoost) 기록입니다"
research_summary: "XGBoost 회귀, XGBoost 분류 중심으로 구현 과정을 정리한 코딩실습13 10.결정트리와 앙상블(XGBoost) 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다."
research_artifacts: "ipynb/md · 코드 12개 · 실행 11개"
code_block_count: 12
execution_block_count: 11
research_focus:
  - "XGBoost 회귀"
  - "XGBoost 분류"
research_stack:
  - "sklearn"
  - "xgboost"
  - "numpy"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

XGBoost 회귀, XGBoost 분류 중심으로 구현 과정을 정리한 코딩실습13 10.결정트리와 앙상블(XGBoost) 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다.

**빠르게 볼 수 있는 포인트**: XGBoost 회귀, XGBoost 분류.

**남겨둔 자료**: `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다.

**주요 스택**: `sklearn`, `xgboost`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 12 |
| Execution Cells | 11 |
| Libraries | `sklearn`, `xgboost`, `numpy` |
| Source Note | `250827_코딩실습13_10.결정트리와 앙상블(XGBoost)` |

## What I Studied

- XGBoost 회귀
- XGBoost 분류

## What I Tried in Code

1. 데이터 불러오기: XGBoost 회귀
2. 모델 구성: XGBoost 회귀
3. 환경 준비: XGBoost 회귀
4. 모델 구성: XGBoost 분류
5. 환경 준비: XGBoost 분류

## Code Evidence

### XGBoost 회귀

**직접 해본 단계**: 데이터 불러오기

`XGBoost 회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
data = fetch_california_housing()
X = data.data
y = data.target
```

### XGBoost 회귀

**직접 해본 단계**: 모델 구성

`XGBoost 회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4
)
model.fit(X_train, y_train)
```

### XGBoost 회귀

**직접 해본 단계**: 환경 준비

`XGBoost 회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sklearn.metrics import mean_squared_error
import numpy as np
```

### XGBoost 분류

**직접 해본 단계**: 모델 구성

`XGBoost 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
model = xgb.XGBClassifier(
    objective='multi:softmax',                  # 다중 클래스 분류
    num_class=3                                 # objective='multi:softmax'와 num_class는 같이 써야함
)
model.fit(X_train, y_train)
```

### XGBoost 분류

**직접 해본 단계**: 환경 준비

`XGBoost 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```

### XGBoost 회귀

**직접 해본 단계**: 모델 구성

`XGBoost 회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실험의 중심이 되는 모델 구조를 정의하고 비교 기준을 세우는 코드입니다.

```python
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
rmse
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `XGBoost 회귀` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `XGBoost 회귀`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).ipynb`, `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
