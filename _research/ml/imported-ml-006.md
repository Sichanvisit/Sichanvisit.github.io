---
title: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md"
excerpt: "해석 1"
research_summary: "해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 35개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, sklearn입니다."
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

해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 35개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, sklearn입니다.

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

## What I Studied

### (1) 첫번째 모델 - 절편 없음

해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락

### Key Step

실습1 문제 코드 - 선형 회귀 + MSE

### Key Step

import matplotlib.pyplot as plt # 한글파일 문제없는 분들은 맨 앞 주석 빼고 진행

### Key Step

입력 변수 (집 크기)와 출력 변수 (집 가격)

## What I Tried in Code

1. 데이터 불러오기: Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)
2. 모델 구성: 선형회귀
3. 학습: 선형회귀
4. 평가: Salary 데이터로 선형회귀 - 사이킷런 이용 코딩
5. 시각화: 선형회귀
6. 환경 준비: Salary 데이터로 선형회귀 - 사이킷런 이용 코딩

## Code Evidence

### Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)

**직접 해본 단계**: 데이터 불러오기

`Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
data = pd.read_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/training_test_data.csv")
data
```

### 선형회귀

**직접 해본 단계**: 모델 구성

`선형회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. LinearRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다. 코드에는 추가 - 다중 선형 회귀 실습 코드 예시 (Python..., 데이터 정의 같은 처리 포인트도 함께 남아 있습니다.

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

# 시각화 (house_size vs 실제/예측 가격)
plt.figure(figsize=(8, 5))
plt.scatter(house_size, price, color='black', label='Actual Price')
plt.scatter(house_size, y_pred, color='blue', label='Predicted Price', marker='x')
plt.xlabel("House Size (평)")
plt.ylabel("Price")
plt.title("Actual vs Predicted Prices by House Size")
plt.legend()
# ... trimmed ...
```

### 선형회귀

**직접 해본 단계**: 학습

`선형회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다. 코드에는 실습2 문제 코드 - 기울기 하강법으로 선형 회귀 실습, 초기 파라미터 같은 처리 포인트도 함께 남아 있습니다.

```python
# 실습2 문제 코드 - 기울기 하강법으로 선형 회귀 실습
# 초기 파라미터
w = 0.0
b = 0.0
lr = 0.01       # 학습률 (learning rate)
epochs = 1000   # 반복 횟수=> ML/DL에서 최적화할 때 변경하는 수치
n = len(house_size)

# 비용 추적용 리스트
cost_list = []

# 경사 하강법
for epoch in range(epochs):
    y_pred = w * house_size + b
    error = y_pred - house_price

    dw = (2/n) * np.dot(error, house_size)
    db = (2/n) * error.sum()

    w -= lr * dw
    b -= lr * db

    mse = np.mean(error ** 2)
    cost_list.append(mse)

# 최종 결과 출력
print(f"학습 완료! 기울기 w = {w:.4f}, 절편 b = {b:.4f}")
print(f"최종 MSE: {mse:.4f}")

# 회귀선 예측
predicted_price = w * house_size + b

# 실제 데이터와 예측 직선 시각화
plt.figure(figsize=(8, 5))
plt.scatter(house_size, house_price, color='blue', label='실제 데이터')
plt.plot(house_size, predicted_price, color='red', label='예측 직선')
# ... trimmed ...
```

### Salary 데이터로 선형회귀 - 사이킷런 이용 코딩

**직접 해본 단계**: 평가

`Salary 데이터로 선형회귀 - 사이킷런 이용 코딩`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
r2_score(y_test, model.predict(X_test))
```

### 선형회귀

**직접 해본 단계**: 시각화

`선형회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 실습3 문제 코드 - 다중 선형 회귀, 입력 변수 같은 처리 포인트도 함께 남아 있습니다.

```python
#실습3 문제 코드 - 다중 선형 회귀

# 1. 입력 변수
house_size = np.array([1.0, 1.5, 1.8, 5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 8.5, 9.0, 10.0])  # 집 크기
distance_from_station = np.array([5, 4.6, 4.2, 3.9, 3.9, 3.6, 3.5, 3.4, 2.9, 2.8, 2.7, 2.3, 2.0, 1.8, 1.5, 1.0])  # 지하철역으로부터의 거리 (km)
number_of_rooms = np.array([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])  # 방 수

# 2. 설계 행렬 X 정의
X = np.array([
    np.ones(16),                   # np.ones(16): 모든 행마다 1을 추가하기 위해 (총 16개의 1 필요)
    house_size,
    distance_from_station,
    number_of_rooms
]).T

# 3. 파라미터 (임의로 설정)
theta = np.array([1, 2, 3, 4])  # θ₀=1, θ₁=2, θ₂=3, θ₃=4

# 4. 다중 선형 회귀 가설 함수
def prediction(X, theta):
    y = X @ theta
    return y

# 5. 예측값 계산
y_pred = prediction(X, theta)

# 6. 시각화 (집 크기 vs 예측값)
plt.figure(figsize=(8, 5))
plt.scatter(house_size, y_pred, color='blue', label='Predicted Price', s=80)
plt.xlabel("House Size (평)")
plt.ylabel("Predicted Value")
plt.title("Prediction by House Size")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
```

### Salary 데이터로 선형회귀 - 사이킷런 이용 코딩

**직접 해본 단계**: 환경 준비

`Salary 데이터로 선형회귀 - 사이킷런 이용 코딩`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.model_selection import train_test_split
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `선형회귀`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

### 학습 코드를 따로 보는 이유

- 왜 필요한가: 모델 선언만으로는 끝나지 않고 fitting, 검증 분리, 하이퍼파라미터 탐색까지 봐야 실제로 해본 실습으로 읽힙니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `선형회귀` 코드를 남겨 학습 루프나 GridSearchCV처럼 성능을 끌어올리기 위해 손댄 지점을 보여줍니다.
- 원리: 훈련 과정은 데이터에서 패턴을 찾도록 파라미터를 조정하는 단계이며, 검증이 함께 있어야 과적합 여부도 판단할 수 있습니다.

### 지표 계산까지 남긴 이유

- 왜 필요한가: 예측을 했더라도 어떤 기준으로 잘했는지 판단하지 않으면 실험 비교가 성립하지 않습니다.
- 왜 이 방식을 쓰는가: 그래서 `Salary 데이터로 선형회귀 - 사이킷런 이용 코딩` 코드를 통해 정확도, F1, RMSLE 같은 지표를 실제로 어떻게 계산했는지 함께 남겼습니다.
- 원리: 평가 지표는 예측 결과를 수치화해 모델 선택과 개선 방향을 정하는 기준점 역할을 합니다.

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
