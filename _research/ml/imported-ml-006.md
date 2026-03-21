---
title: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습6_9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런).md"
excerpt: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)를 중심으로 회귀 문제, 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습6 9.기본 지도학습 알고리즘들 (선형회귀 - 사이킷런)를 중심으로 회귀 문제, 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 Salary 데이터로 선형회귀 기본 코..., 선형회귀 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 35개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, sklearn입니다."
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

<div class="research-doc-hero">
  <div class="research-doc-summary">
    <p class="research-doc-summary__label">문제 설정</p>
    <p class="research-doc-summary__body">해석 1. 나이가 1살 많을 수록 소득은 4.41 증가 2</p>
  </div>
  <div class="research-doc-meta">
<div class="research-doc-card">
  <p class="research-doc-card__label">데이터 맥락</p>
  <p class="research-doc-card__value">Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">핵심 개념</p>
  <p class="research-doc-card__value">회귀 문제 · 함수 분해와 로직 구성</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">구현 포인트</p>
  <p class="research-doc-card__value">Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X) · 선형회귀 · Salary 데이터로 선형회귀 - 사이킷런 이용 코딩</p>
</div>
  </div>
  <div class="research-doc-stats">
<div class="research-doc-stat">
  <span>소스</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-stat">
  <span>자료</span>
  <strong>코드 35 · 실행 35</strong>
</div>
<div class="research-doc-stat">
  <span>주요 스택</span>
  <strong>matplotlib, warnings, numpy, sklearn 외 1</strong>
</div>
  </div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">회귀 문제</p>
  <p class="research-note-card__body">회귀는 연속적인 수치를 예측하는 문제입니다. 예측값과 실제값의 차이를 오차로 계산해 모델 성능을 판단합니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 수요량, 가격, 점수처럼 숫자 타깃을 예측하는 실습과 이어집니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">함수 분해와 로직 구성</p>
  <p class="research-note-card__body">함수는 입력, 처리, 반환을 분리해 로직을 재사용하기 쉽게 만들고, 문제를 작은 단위로 나누는 기본 도구입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 문제 풀이를 함수 단위로 쪼개고 입출력을 나눠 보는 실습과 연결됩니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-list">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">Salary 데이터로 선형회귀 기본 코딩 (사이킷런 사용 X)</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>pd.read_csv</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 모델 구성</p>
  <p class="research-step-card__title">선형회귀</p>
  <p class="research-step-card__body">LinearRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>LinearRegression</code> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 추가 - 다중 선형 회귀 실습 코드 예시 (Python... · 데이터 정의</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 평가</p>
  <p class="research-step-card__title">Salary 데이터로 선형회귀 - 사이킷런 이용 코딩</p>
  <p class="research-step-card__body">예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 구현 코드</p>
  <p class="research-step-card__title">(1) 첫번째 모델 - 절편 없음</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> np.linalg.inv(X.T @ X) =&gt; (X^T*... · T@y =&gt;X^T*y</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 구현 코드</p>
  <p class="research-step-card__title">(2) 두번째 모델링 - 절편 추가</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
</div>

## Code Evidence

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

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
b = np.dot(np.linalg.inv(X.T @ X), X.T@y)

# np.linalg.inv(X.T @ X) => (X^T*X)^-1
# X.T@y   =>X^T*y
```

### (2) 두번째 모델링 - 절편 추가

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
X2 = np.c_[np.ones(100), X]
X2
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
