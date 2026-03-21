---
title: "코딩실습10 10.결정트리와 앙상블(DT)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습10_10.결정트리와 앙상블(DT)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md"
excerpt: "_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현"
research_summary: "_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다."
research_artifacts: "ipynb/md · 코드 26개 · 실행 25개"
code_block_count: 26
execution_block_count: 25
research_focus:
  - "_reg"
  - "DT 회귀 실습"
  - "DT 분류 실습"
research_stack:
  - "matplotlib"
  - "warnings"
  - "sklearn"
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

_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다.

**빠르게 볼 수 있는 포인트**: _reg, DT 회귀 실습, DT 분류 실습.

**남겨둔 자료**: `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다.

**주요 스택**: `matplotlib`, `warnings`, `sklearn`, `pandas`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 26 |
| Execution Cells | 25 |
| Libraries | `matplotlib`, `warnings`, `sklearn`, `pandas` |
| Source Note | `250827_코딩실습10_10.결정트리와 앙상블(DT)` |

## What I Studied

### DT 회귀 실습

_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현

### Key Step

위 코드 판다스로 지정해 불러올 때

### Key Step

각 특성의 중요도 값 가져오기

## What I Tried in Code

1. 데이터 불러오기: DT 회귀 실습
2. 피처 가공: DT 분류 실습
3. 모델 구성: DT 회귀 실습
4. 평가: DT 회귀 실습
5. 시각화: 데이터 분포 시각화
6. 환경 준비: DT 회귀 실습

## Code Evidence

### DT 회귀 실습

**직접 해본 단계**: 데이터 불러오기

`DT 회귀 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다. 코드에는 위 코드 판다스로 지정해 불러올 때 같은 처리 포인트도 함께 남아 있습니다.

```python
# 위 코드 판다스로 지정해 불러올 때

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)

X_reg = df.values
y_reg = data.target
```

### DT 분류 실습

**직접 해본 단계**: 피처 가공

`DT 분류 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
dt_clf = DecisionTreeClassifier(random_state=42)
dt_clf.fit(X_clf, y_clf)

plt.figure(figsize=(20,10))
plot_tree(
    dt_clf,
    feature_names=feature_names_clf,
    class_names=class_names_clf,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("결정 트리 분류")
plt.show()
```

### DT 회귀 실습

**직접 해본 단계**: 모델 구성

`DT 회귀 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. DecisionTree 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
dt_reg = DecisionTreeRegressor()    # max_depth를 지정할 수 있음
dt_reg.fit(X_train, y_train)
```

### DT 회귀 실습

**직접 해본 단계**: 평가

`DT 회귀 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
y_pred = dt_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("평균 제곱 오차(MSE): ", mse)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

`데이터 분포 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

!apt-get update -qq
!apt-get install fonts-nanum* -qq

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings(action='ignore')

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf' # 나눔 고딕
font_name = fm.FontProperties(fname=path, size=10).get_name() # 기본 폰트 사이즈 : 10
plt.rc('font', family=font_name)

fm.fontManager.addfont(path)
```

### DT 회귀 실습

**직접 해본 단계**: 환경 준비

`DT 회귀 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `DT 회귀 실습` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 파생 변수를 직접 만든 부분

- 왜 필요한가: 원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `DT 분류 실습` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.
- 원리: 좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `DT 회귀 실습`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

### 지표 계산까지 남긴 이유

- 왜 필요한가: 예측을 했더라도 어떤 기준으로 잘했는지 판단하지 않으면 실험 비교가 성립하지 않습니다.
- 왜 이 방식을 쓰는가: 그래서 `DT 회귀 실습` 코드를 통해 정확도, F1, RMSLE 같은 지표를 실제로 어떻게 계산했는지 함께 남겼습니다.
- 원리: 평가 지표는 예측 결과를 수치화해 모델 선택과 개선 방향을 정하는 기준점 역할을 합니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습10_10.결정트리와 앙상블(DT).ipynb`, `250827_코딩실습10_10.결정트리와 앙상블(DT).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - _reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현
