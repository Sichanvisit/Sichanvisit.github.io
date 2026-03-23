---
title: "9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md"
excerpt: "9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 Salary 데이터로 선형회..., Salary 데이터로 선형회..., 선형회귀 순서로 큰 장을 먼저 훑고, 모델 학습 루프, LinearRegressio..."
research_summary: "9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 Salary 데이터로 선형회..., Salary 데이터로 선형회..., 선형회귀 순서로 큰 장을 먼저 훑고, 모델 학습 루프, LinearRegression 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 35개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, sklearn입니다."
research_artifacts: "ipynb/md · 코드 35개 · 실행 35개"
code_block_count: 35
execution_block_count: 35
research_focus:
  - "Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)"
  - "Salary 데이터로 선형회귀 - 사이킷런 이용 코딩"
  - "선형회귀"
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
  - archive-note
---

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">선형회귀 -&gt; Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X) -&gt; Salary 데이터로 선형회귀 - 사이킷런 이용 코딩</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X) · Salary 데이터로 선형회귀 - 사이킷런 이용 코딩 · 선형회귀</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">train/test CSV 불러오기 -&gt; Salary 데이터로 선형회귀 - 사이킷런 이용 코딩 -&gt; 학습/검증 데이터 분리</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 35 · 실행 35</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">matplotlib, warnings, numpy, sklearn 외 1</div>
  </div>
</div>

+
## 1. 선형회귀

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

```python
# 실습1 문제 코드 - 선형 회귀 + MSE
import numpy as np
# import matplotlib.pyplot as plt # 한글파일 문제없는 분들은 맨 앞 주석 빼고 진행

# 입력 변수 (집 크기)와 출력 변수 (집 가격)
house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35, 3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])
house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9, 1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

# 1. 선형 회귀 수식 구하기
w, b = np.polyfit(house_size, house_price, 1)

# 2. 예측값 계산
predicted_price = w * house_size + b

# 3. MSE 계산
mse = np.mean((house_price - predicted_price) ** 2)

# 결과 출력
print(f"기울기 w: {w:.4f}")
print(f"절편 b: {b:.4f}")
print(f"평균 제곱 오차 (MSE): {mse:.4f}")

# 시각화
plt.figure(figsize=(8, 5))
plt.scatter(house_size, house_price, color='blue', label='실제 데이터')
plt.plot(house_size, predicted_price, color='red', label='예측 직선')
plt.title("선형 회귀 모델: 집 크기 vs 집 가격")
plt.xlabel("집 크기")
plt.ylabel("집 가격")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

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
plt.title("경사 하강법으로 학습한 선형 회귀")
plt.xlabel("집 크기 (단위: 축소됨)")
plt.ylabel("집 가격 (단위: 축소됨)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 비용 함수 수렴 시각화
plt.figure(figsize=(8, 4))
plt.plot(cost_list)
plt.title("MSE (비용 함수) 감소 추이")
plt.xlabel("Epoch")
plt.ylabel("Mean Squared Error")
plt.grid(True)
plt.tight_layout()
plt.show()
```

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
plt.grid(True)
plt.tight_layout()
plt.show()
```

## 2. Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)

```python
from google.colab import drive
drive.mount('/content/drive')
```

```python
import pandas as pd
import numpy as np
```

```python
data = pd.read_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/training_test_data.csv")
data
```

```python
data.info()
```

```python
data.describe()
```

```python
# 판다스의 데이터에서 넘파이로 변환 => 머신러닝 모델 학습 위해!
data_np = data.values
```

```python
data_np
```

```python
# 독립변수 종속변수 구분
X = data_np[:,:-1]
y = data_np[:,-1]
```

```python
X
```

```python
y
```

### 1) 첫번째 모델 - 절편 없음

```python
b = np.dot(np.linalg.inv(X.T @ X), X.T@y)

# np.linalg.inv(X.T @ X) => (X^T*X)^-1
# X.T@y   =>X^T*y
```

```python
b
```

**해석**
1. 나이가 1살 많을 수록 소득은 4.41 증가
2. 성별 1->2 바뀌면 소득이 8.71 증가
3. 경력이 1년 늘어나면 소득은 2.83 하락

### 2) 두번째 모델링 - 절편 추가

```python
X2 = np.c_[np.ones(100), X]
X2
```

```python
b_new = np.dot(np.linalg.inv(X2.T @ X2), X2.T@y)
```

```python
b_new
```

## 3. Salary 데이터로 선형회귀 - 사이킷런 이용 코딩

```python
data.head()
```

```python
data_np = data.values
```

```python
data_np
```

```python
X = data_np[:,:-1]
y = data_np[:,-1]
```

```python
from sklearn.model_selection import train_test_split
```

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
```

```python
X_train.shape
```

```python
X_test.shape
```

```python
from sklearn.linear_model import LinearRegression
```

```python
# 모델링
model = LinearRegression()
```

```python
# 모델 학습
model.fit(X_train, y_train)
```

```python
# 모델 평가 - 기본 평가 점수 - R^2
model.score(X_test, y_test)
```

```python
from sklearn.metrics import r2_score
```

```python
r2_score(y_test, model.predict(X_test))
```

```python

```
