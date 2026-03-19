---
title: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md"
excerpt: "**해석** 1. 나이가 1살 많을 수록 소득은 4.41 증가 2. 성별 1->2 바뀌면 소득이 8.71 증가 3. 경력이 1년 늘어나면 소득은 2.83 하락"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

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

## What I Worked On

- 1. 선형회귀
- 실습1 문제 코드 - 선형 회귀 + MSE
- import matplotlib.pyplot as plt # 한글파일 문제없는 분들은 맨 앞 주석 빼고 진행
- 입력 변수 (집 크기)와 출력 변수 (집 가격)
- 1. 선형 회귀 수식 구하기

## Implementation Flow

1. 1. 선형회귀
2. 실습1 문제 코드 - 선형 회귀 + MSE
3. import matplotlib.pyplot as plt # 한글파일 문제없는 분들은 맨 앞 주석 빼고 진행
4. 입력 변수 (집 크기)와 출력 변수 (집 가격)
5. 1. 선형 회귀 수식 구하기
6. 2. 예측값 계산

## Code Highlights

### 1. 선형회귀

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
# ... trimmed ...
```

### 1. 선형회귀

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
