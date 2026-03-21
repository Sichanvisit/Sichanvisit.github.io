---
title: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md"
excerpt: "해석 1"
research_summary: "해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 35개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, sklearn입니다."
research_artifacts: "ipynb/md · 코드 35개 · 실행 35개"
code_block_count: 35
execution_block_count: 35
research_focus:
  - "선형회귀"
  - "Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)"
  - "해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가..."
research_stack:
  - "matplotlib"
  - "warnings"
  - "numpy"
  - "sklearn"
  - "google"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 35개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, sklearn입니다.

**빠르게 볼 수 있는 포인트**: 선형회귀, Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X), 해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1-....

**남겨둔 자료**: `ipynb/md` 원본과 35개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, sklearn입니다.

**주요 스택**: `matplotlib`, `warnings`, `numpy`, `sklearn`, `google`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 35 |
| Execution Cells | 35 |
| Libraries | `matplotlib`, `warnings`, `numpy`, `sklearn`, `google`, `pandas` |
| Source Note | `250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)` |

## What This Note Covers

### (1) 첫번째 모델 - 절편 없음

해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락

### Key Step

실습1 문제 코드 - 선형 회귀 + MSE

### Key Step

import matplotlib.pyplot as plt # 한글파일 문제없는 분들은 맨 앞 주석 빼고 진행

### Key Step

입력 변수 (집 크기)와 출력 변수 (집 가격)

## Why This Matters

### 입력과 모델 연결

- 왜 필요한가: 머신러닝 실습에서는 모델 선택만큼 입력 데이터를 어떤 형태로 정리하는지가 결과를 크게 좌우합니다.
- 왜 이 방식을 쓰는가: 이 기록은 전처리와 모델링 코드를 같이 남겨, 학습한 개념이 실제 코드 흐름으로 어떻게 연결되는지 보게 합니다.
- 원리: 데이터 정리, 특징 표현, 학습, 평가가 한 파이프라인으로 이어질 때 비로소 모델 동작을 해석할 수 있습니다.

## Implementation Flow

1. (1) 첫번째 모델 - 절편 없음: 해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락
2. Key Step: 실습1 문제 코드 - 선형 회귀 + MSE
3. Key Step: import matplotlib.pyplot as plt # 한글파일 문제없는 분들은 맨 앞 주석 빼고 진행
4. Key Step: 입력 변수 (집 크기)와 출력 변수 (집 가격)

## Code Highlights

### 선형회귀

`선형회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 추가 - 다중 선형 회귀 실습 코드 예시 (Python - scikit-learn), 데이터 정의, 종속 변수(y): 여기선 임의로 생성 (실제 데이터가 없으니 가상의 가격 데이터 예시) 흐름이 주석과 함께 드러납니다.

```python
# 추가 -  다중 선형 회귀 실습 코드 예시 (Python - scikit-learn)

from sklearn.linear_model import LinearRegression

# 1. 데이터 정의
house_size = np.array([1.0, 1.5, 1.8, 5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 8.5, 9.0, 10.0])
distance_from_station = np.array([5, 4.6, 4.2, 3.9, 3.9, 3.6, 3.5, 3.4, 2.9, 2.8, 2.7, 2.3, 2.0, 1.8, 1.5, 1.0])
number_of_rooms = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])

# 종속 변수(y): 여기선 임의로 생성 (실제 데이터가 없으니 가상의 가격 데이터 예시)
# 실제 분석에서는 진짜 집값 데이터가 필요합니다!
price = np.array([300, 330, 360, 650, 400, 420, 460, 500, 580, 600, 680, 750, 820, 850, 870, 920])

# 2. 특성 행렬 (X) 구성
X = np.column_stack([house_size, distance_from_station, number_of_rooms])

# 3. 모델 학습
model = LinearRegression()
model.fit(X, price)

# 4. 예측
y_pred = model.predict(X)

# 결과 출력
print("계수 (theta):", model.coef_)
print("절편 (intercept):", model.intercept_)
print("R^2 점수:", model.score(X, price))

# ... trimmed ...
```

### Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)

`Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 독립변수 종속변수 구분 흐름이 주석과 함께 드러납니다.

```python
# 독립변수 종속변수 구분
X = data_np[:,:-1]
y = data_np[:,-1]
```

### Salary 데이터로 선형회귀 - 사이킷런 이용 코딩

`Salary 데이터로 선형회귀 - 사이킷런 이용 코딩`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습 흐름이 주석과 함께 드러납니다.

```python
# 모델 학습
model.fit(X_train, y_train)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md`
- Source formats: `ipynb`, `md`
- Companion files: `250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).ipynb`, `250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> +
> **해석** 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락
