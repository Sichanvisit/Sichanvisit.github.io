---
title: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md"
excerpt: "legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스..."
research_summary: "legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - l... 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "Iris 데이터로 이진 분류"
  - "Iris 데이터로 다중 분류"
  - "Softmax 이용한 다중 분류"
research_stack:
  - "sklearn"
  - "matplotlib"
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

legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - l... 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: Iris 데이터로 이진 분류, Iris 데이터로 다중 분류, Softmax 이용한 다중 분류.

**남겨둔 자료**: `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다.

**주요 스택**: `sklearn`, `matplotlib`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 19 |
| Execution Cells | 18 |
| Libraries | `sklearn`, `matplotlib`, `numpy` |
| Source Note | `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)` |

## What I Studied

### handles, _ = scatter.legend_elements() 코드 설명

legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - label: 0, 1, 2처럼 자동 생성된 클래스 이름...

### Key Step

Softmax 이용한 다중 분류

## What I Tried in Code

1. 데이터 불러오기: Iris 데이터로 이진 분류
2. 모델 구성: Iris 데이터로 다중 분류
3. 평가: Iris 데이터로 이진 분류
4. 시각화: Softmax 이용한 다중 분류
5. 환경 준비: Iris 데이터로 이진 분류
6. 구현 코드: Iris 데이터로 다중 분류

## Code Evidence

### Iris 데이터로 이진 분류

**직접 해본 단계**: 데이터 불러오기

`Iris 데이터로 이진 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다. 코드에는 데이터 로드 같은 처리 포인트도 함께 남아 있습니다.

```python
# 데이터 로드
iris = load_iris()
```

### Iris 데이터로 다중 분류

**직접 해본 단계**: 모델 구성

`Iris 데이터로 다중 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다. 코드에는 모델링 & 시각화 같은 처리 포인트도 함께 남아 있습니다.

```python
# 모델링 & 시각화

plt.figure(figsize=(10,3))

for i in range(3):
    binary_y = (y==i).astype(int)                  # OvR -> 이진 라벨 생성
    model = LogisticRegression()
    model.fit(X, binary_y)

    Z = model.predict(grid)
    Z = Z.reshape(xx.shape)

    plt.subplot(1, 3, i+1)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
    plt.scatter(X[:,0], X[:,1], c=binary_y, cmap='bwr', edgecolors='black')
    plt.title(f'Class {i} : {class_names[i]} vs Rest')
    plt.grid(True)

plt.tight_layout()
plt.show()
```

### Iris 데이터로 이진 분류

**직접 해본 단계**: 평가

`Iris 데이터로 이진 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다. 코드에는 시각화용 격자 생성 코드 같은 처리 포인트도 함께 남아 있습니다.

```python
# 시각화용 격자 생성 코드

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5          # x축
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5          # y축
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))           # 200X200 격자 생성
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])               # 모델이 예측한 클래스 라벨 계산
Z = Z.reshape(xx.shape)                                        # Z를 격자 형태로 변형 -> 2D
```

### Softmax 이용한 다중 분류

**직접 해본 단계**: 시각화

`Softmax 이용한 다중 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 시각화, legend 지정 위한 코드 같은 처리 포인트도 함께 남아 있습니다.

```python
# 시각화

plt.figure(figsize=(5,3))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='Set1')
scatter = plt.scatter(X[:,0], X[:,1], c=y, cmap='Set1', edgecolors='black')

# legend 지정 위한 코드
handles, _ = scatter.legend_elements()

plt.title('Softmax')
plt.legend(handles, class_names, title="Classes")
plt.grid(True)
plt.show()
```

### Iris 데이터로 이진 분류

**직접 해본 단계**: 환경 준비

`Iris 데이터로 이진 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
```

### Iris 데이터로 다중 분류

**직접 해본 단계**: 구현 코드

`Iris 데이터로 다중 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 시각화용 격자 생성 코드 같은 처리 포인트도 함께 남아 있습니다.

```python
# 시각화용 격자 생성 코드

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5          # x축
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5          # y축
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))           # 200X200 격자 생성
grid = np.c_[xx.ravel(), yy.ravel()]
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `Iris 데이터로 이진 분류` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `Iris 데이터로 다중 분류`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

### 지표 계산까지 남긴 이유

- 왜 필요한가: 예측을 했더라도 어떤 기준으로 잘했는지 판단하지 않으면 실험 비교가 성립하지 않습니다.
- 왜 이 방식을 쓰는가: 그래서 `Iris 데이터로 이진 분류` 코드를 통해 정확도, F1, RMSLE 같은 지표를 실제로 어떻게 계산했는지 함께 남겼습니다.
- 원리: 평가 지표는 예측 결과를 수치화해 모델 선택과 개선 방향을 정하는 기준점 역할을 합니다.

### 시각화를 같이 남긴 이유

- 왜 필요한가: 숫자만 보면 놓치기 쉬운 분포와 이상치를 그래프로 확인해야 다음 전처리나 feature engineering 방향이 또렷해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `Softmax 이용한 다중 분류` 코드를 통해 어떤 그래프를 보고 판단했는지 실습 흔적을 남겼습니다.
- 원리: 시각화는 데이터 분포를 직관적으로 드러내 모델 선택과 변수 설계의 근거를 만들어 줍니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Source formats: `ipynb`, `md`
- Companion files: `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).ipynb`, `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`, `matplotlib.org`

## Note Preview

> - **legend_elements()** - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - label: 0, 1, 2처럼 자동 생성된 클래스 이름 문자열 - scatter.legend_elements()는 handles, label을 반환하지만, 클래스 이름을 실제 label로 사용해 보여주고자 함 - handles, _ = scatter.legend_elements()로 변수를 두 개 지정할 때, handles는 가져오고 labels는 무시한다는 의미로 **아래 밑줄**을 사용 - 아래 밑줄: 파이썬의 관례적인 표현 1. 사용하지 않는 값 무시 2. 표현식의 마지막 결과값 저장 3. 내부 문서 의미
