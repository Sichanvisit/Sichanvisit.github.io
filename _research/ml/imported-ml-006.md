---
title: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md"
excerpt: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 선형회귀, Salary 데이터로 선형회..., Salary 데이터로 선형회... 순서로 큰 장을 먼저 훑고, Salary 데이터로 선형회귀 기본..."
research_summary: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 선형회귀, Salary 데이터로 선형회..., Salary 데이터로 선형회... 순서로 큰 장을 먼저 훑고, Salary 데이터로 선형회귀 기본 코..., 선형회귀 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 35개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, sklearn입니다."
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

## 글 한눈에 보기

| 항목 | 내용 |
|------|------|
| 문제 설정 | 코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)에서 선형회귀, Salary 데이터로 선형회..., Salary 데이터로 선형회... 흐름을 직접 따라가며 구현했습니다. |
| 원본 구조 | 선형회귀 -> Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X) -> Salary 데이터로 선형회귀 - 사이킷런 이용 코딩 |
| 데이터 맥락 | Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X) |
| 주요 장 | 선형회귀 · Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X) · Salary 데이터로 선형회귀 - 사이킷런 이용 코딩 |
| 구현 흐름 | Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X) -> 선형회귀 -> Salary 데이터로 선형회귀 - 사이킷런 이용 코딩 |
| 자료 | ipynb / md · 코드 35 · 실행 35 |
| 주요 스택 | matplotlib, warnings, numpy, sklearn 외 1 |

## 원본 노트 흐름

### 선형회귀

실습1 문제 코드 - 선형 회귀 +..., 실습2 문제 코드 - 기울기 하강법..., 실습3 문제 코드 - 다중 선형 회귀 같은 코드를 직접 따라가며 선형회귀 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 실습1 문제 코드 - 선형 회귀 + MSE, 실습2 문제 코드 - 기울기 하강법으로 선형 회귀 실습, 실습3 문제 코드 - 다중 선형 회귀

#### 실습1 문제 코드 - 선형 회귀 + MSE

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

#### 실습2 문제 코드 - 기울기 하강법으로 선형 회귀 실습

훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.

#### 실습3 문제 코드 - 다중 선형 회귀

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

### Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)

해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락

- 읽을 포인트: 세부 흐름: (1) 첫번째 모델 - 절편 없음, (2) 두번째 모델링 - 절편 추가

#### (1) 첫번째 모델 - 절편 없음

해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락

#### (2) 두번째 모델링 - 절편 추가

데이터 구조와 주의할 변수부터 읽고 실험 방향을 정리하는 구간입니다.

### Salary 데이터로 선형회귀 - 사이킷런 이용 코딩

모델링, 모델 학습, 모델 평가 - 기본 평가 점수 - R^2 같은 코드를 직접 따라가며 Salary 데이터로 선형회귀 - 사이킷런 이용 코딩 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 모델링, 모델 학습, 모델 평가 - 기본 평가 점수 - R^2

#### 모델링

LinearRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

#### 모델 학습

훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.

#### 모델 평가 - 기본 평가 점수 - R^2

Salary 데이터로 선형회귀 - 사이킷런 이용 코딩 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

## 구현 흐름

### 1. Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: `pd.read_csv`
- 코드 포인트: -

### 2. 선형회귀

- 단계: 모델 구성
- 구현 의도: LinearRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: `LinearRegression`, `matplotlib`
- 코드 포인트: 추가 - 다중 선형 회귀 실습 코드 예시 (Python... · 데이터 정의

### 3. Salary 데이터로 선형회귀 - 사이킷런 이용 코딩

- 단계: 평가
- 구현 의도: 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.
- 핵심 API: -
- 코드 포인트: -

### 4. (1) 첫번째 모델 - 절편 없음

- 단계: 구현 코드
- 구현 의도: (1) 첫번째 모델 - 절편 없음 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: np.linalg.inv(X.T @ X) => (X^T*... · T@y =>X^T*y

### 5. (2) 두번째 모델링 - 절편 추가

- 단계: 구현 코드
- 구현 의도: (2) 두번째 모델링 - 절편 추가 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: -

## 코드로 확인한 내용

### Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
data = pd.read_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/training_test_data.csv")
data
```

### 선형회귀

**직접 해본 단계**: 모델 구성

**핵심 API**: `LinearRegression`, `matplotlib`

LinearRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

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

### Salary 데이터로 선형회귀 - 사이킷런 이용 코딩

**직접 해본 단계**: 평가

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
r2_score(y_test, model.predict(X_test))
```

### (1) 첫번째 모델 - 절편 없음

**직접 해본 단계**: 구현 코드

(1) 첫번째 모델 - 절편 없음 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python
b = np.dot(np.linalg.inv(X.T @ X), X.T@y)

# np.linalg.inv(X.T @ X) => (X^T*X)^-1
# X.T@y   =>X^T*y
```

### (2) 두번째 모델링 - 절편 추가

**직접 해본 단계**: 구현 코드

(2) 두번째 모델링 - 절편 추가 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python
X2 = np.c_[np.ones(100), X]
X2
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md`
- Source formats: `ipynb`, `md`
- Companion files: `250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).ipynb`, `250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## 원문 미리보기

> +
> **해석** 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락
