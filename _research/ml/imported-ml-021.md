---
title: "3 Bike Rental System"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]3_Bike Rental System - AI 5기 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md"
excerpt: "Bike Rental System의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 전처리, 데이터 시각화, 모델링 순서로 큰 장을 먼저 훑고, XGBoost 모델 구성, GridSearchCV 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있..."
research_summary: "Bike Rental System의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 전처리, 데이터 시각화, 모델링 순서로 큰 장을 먼저 훑고, XGBoost 모델 구성, GridSearchCV 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다."
research_artifacts: "ipynb/md · 코드 108개 · 실행 107개"
code_block_count: 108
execution_block_count: 107
research_focus:
  - "현재까지 전처리한 데이터 기반, 회귀 모델링 실시"
  - "(1) 1차 모델링"
  - "(2) 2차 모델링"
research_stack:
  - "matplotlib"
  - "warnings"
  - "numpy"
  - "pandas"
  - "seaborn"
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
    <div class="research-overview__value">자전거 대여 시스템의 운영 담당자. 자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">미션 설명 -&gt; 데이터 -&gt; 분석 드릴다운 -&gt; 데이터 확인 -&gt; 데이터 전처리</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">train.csv - 자전거 대여 수요를 예측하기 위한 데이터 포함 - 종속 변수: count test.csv</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">데이터 전처리 · 데이터 시각화 · 모델링 · 결과 저장</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">XGBoost 모델 구성 -&gt; GridSearchCV 모델 학습 -&gt; 결과 저장</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 108 · 실행 107</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">matplotlib, warnings, numpy, pandas 외 1</div>
  </div>
</div>

## 원본 노트 흐름

### 데이터 전처리

(3) datetime 데이터 타입 변환, (5) 계절 변화 - season..., (6) 이상치 제거 같은 코드를 직접 따라가며 데이터 전처리 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: (3) datetime 데이터 타입 변환, (5) 계절 변화 - season 컬럼 정리, (6) 이상치 제거

#### (3) datetime 데이터 타입 변환

입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.

#### (5) 계절 변화 - season 컬럼 정리

입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.

#### (6) 이상치 제거

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

### 데이터 시각화

(1) 변수별 대여량 다각도 시각화, (2) 상관관계 시각화, (3) 습도와 풍속 구간별 대여량 같은 코드를 직접 따라가며 데이터 시각화 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: (1) 변수별 대여량 다각도 시각화, (2) 상관관계 시각화, (3) 습도와 풍속 구간별 대여량

#### (1) 변수별 대여량 다각도 시각화

새벽 시간과 저녁시간 대여량 급감 => 출퇴근 시간 대여 급증

#### (2) 상관관계 시각화

모델링 전에 변수들 파악하기 위해 진행

#### (3) 습도와 풍속 구간별 대여량

=> 습도가 너무 낮을땐 자전거 대여 총합이 작고, 중간과 높을 때 대여량이 많다 - 일반적으로 육지는 겨울의 경우 매우 낮아지는 경우가 대부분 - 해양성 기후 혹은 상대적 우리나라 가을날씨를 겨울로 부르는 곳은 겨울에 습도가 높아지기도 함. 하지만 대개는 겨울에 습도가 낮아짐 -...

### 모델링

(1) 1차 모델링, (3) 3차 모델링, (4) 4차 모델링 같은 코드를 직접 따라가며 모델링 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: (1) 1차 모델링, (3) 3차 모델링, (4) 4차 모델링

#### (1) 1차 모델링

현재까지 전처리한 데이터 기반, 회귀 모델링 실시 => 3차 다항 회귀의 결과가 가장 좋음

#### (3) 3차 모델링

파생 변수 추가하고 바람 변수만 빼고 모델링하기 => 오전과 낮에 평균 대여량이 높고, 러시아워에 특히 대여량이 많음

#### (4) 4차 모델링

이상적인 날씨에 대해 파생변수 만든 뒤 풍속 제거 후 모델링

### 결과 저장

X_test 전처리 같은 코드를 직접 따라가며 결과 저장 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: X_test 전처리

#### X_test 전처리

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

## 구현 흐름

### 1. XGBoost 모델 구성

- 단계: 모델 구성
- 구현 의도: XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: `XGBoost`, `RMSLE`, `RMSE`
- 코드 포인트: -

### 2. GridSearchCV 모델 학습

- 단계: 학습
- 구현 의도: 하이퍼파라미터 탐색이나 교차검증을 통해 단순 실행이 아니라 성능 비교까지 해본 학습 코드입니다.
- 핵심 API: `GridSearchCV`, `RMSLE`, `RMSE`
- 코드 포인트: 최종 모델 결과 저장 리스트 · 모델별 학습 및 평가

### 3. 결과 저장

- 단계: 평가
- 구현 의도: 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.
- 핵심 API: -
- 코드 포인트: X_test 전처리 · 예측

### 4. StandardScaler 스케일링

- 단계: 전처리
- 구현 의도: 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.
- 핵심 API: `StandardScaler`
- 코드 포인트: 표준화 - from sklearn.preprocessin...

### 5. 파생 변수 추가

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: `matplotlib`, `seaborn`
- 코드 포인트: 시간대별 정보로 다시 시각화 · 오전 여부

### 6. train/test CSV 불러오기

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: `pd.read_csv`
- 코드 포인트: -

## 코드로 확인한 내용

### XGBoost 모델 구성

**직접 해본 단계**: 모델 구성

**핵심 API**: `XGBoost`, `RMSLE`, `RMSE`

XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
results_6 = []

results_6.append({
    "Model": "XGBRegressor",
    "MAE": mae,
    "MSE": mse,
    "RMSE": rmse,
    "RMSLE": rmsle,
    "R제곱" : r2
    })
```

### GridSearchCV 모델 학습

**직접 해본 단계**: 학습

**핵심 API**: `GridSearchCV`, `RMSLE`, `RMSE`

하이퍼파라미터 탐색이나 교차검증을 통해 단순 실행이 아니라 성능 비교까지 해본 학습 코드입니다.

```python
# 최종 모델 결과 저장 리스트
results_2 = []

# 모델별 학습 및 평가
for name, base_model in models_2.items():
    if name in param_grids:
        grid = GridSearchCV(base_model, param_grids[name], cv=5, scoring='neg_mean_squared_error')
        grid.fit(X1_train, y1_train)
        model = grid.best_estimator_
    else:
        model = base_model
        model.fit(X1_train, y1_train)

    y1_pred_log = model.predict(X1_val)
    y1_pred = np.expm1(y1_pred_log)                                     # np.expm1: 로그 역변환
    y1_true = np.expm1(y1_val)

    mae = mean_absolute_error(y1_true, y1_pred)
    mse = mean_squared_error(y1_true, y1_pred)
    rmse = np.sqrt(mse)
    rmsle = np.sqrt(mean_squared_log_error(y1_true, y1_pred))
    r2 = r2_score(y1_true, y1_pred)

    results_2.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "RMSLE": rmsle,
        "R제곱": r2,
        "Best Params": grid.best_params_ if name in param_grids else "-"
    })
```

### 결과 저장

**직접 해본 단계**: 평가

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
# X_test 전처리
X_final_test = test.loc[:, ~test.columns.isin(["datetime", "windspeed", "humidity_bin", "weekday_name", "humidity_ideal", "weather_ideal"])]

# 예측
y_test_pred_log = model_xg.predict(X_final_test)

# 로그 복원
y_test_pred = np.expm1(y_test_pred_log)

# 결과를 DataFrame으로 만들고 datetime 붙이기
submission = pd.DataFrame({
    "datetime": test["datetime"],
    "count": y_test_pred.round().astype(int)
})

# CSV 파일로 저장
submission.to_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_submission.csv', index=False)
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

**핵심 API**: `StandardScaler`

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

```python
# 표준화 - from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

train["windspeed_z"] = scaler.fit_transform(train[["windspeed"]]).ravel()      # ravel(): Series로 저장하기 위해 필요
test["windspeed_z"] = scaler.fit_transform(test[["windspeed"]]).ravel()
```

### 파생 변수 추가

**직접 해본 단계**: 피처 가공

**핵심 API**: `matplotlib`, `seaborn`

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
# 시간대별 정보로 다시 시각화

plt.figure(figsize=(8, 3))

# 오전 여부
morning_avg = train.groupby("is_morning")["count"].mean().reset_index()
plt.subplot(1, 3, 1)
sns.barplot(data=morning_avg, x="is_morning", y="count")
plt.title("오전 여부에 따른 평균 대여량")
plt.xticks([0, 1], ["오후", "오전"])
plt.ylabel("평균 대여량")

# 밤 여부
night_avg = train.groupby("is_night")["count"].mean().reset_index()
plt.subplot(1, 3, 2)
sns.barplot(data=night_avg, x="is_night", y="count")
plt.title("밤 여부에 따른 평균 대여량")
plt.xticks([0, 1], ["낮", "밤"])
plt.ylabel("평균 대여량")

# 러시아워 여부
rush_avg = train.groupby("is_rush_hour")["count"].mean().reset_index()
plt.subplot(1, 3, 3)
sns.barplot(data=rush_avg, x="is_rush_hour", y="count")
plt.title("러시아워 여부에 따른 평균 대여량")
plt.xticks([0, 1], ["일반 시간대", "러시아워"])
plt.ylabel("평균 대여량")

plt.tight_layout()
plt.show()
```

### train/test CSV 불러오기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
train = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_train.csv')
test = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_test.csv')
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md`
- Source formats: `ipynb`, `md`
- Companion files: `[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.ipynb`, `[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `windspeed`
- External references: `localhost`, `ko.wikipedia.org`, `weekly.chosun.com`, `www.dvidshub.net`, `en.wikipedia.org`

## 원문 미리보기

> - 자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: **RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것**
> $$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(p_i + 1) - \log(a_i + 1) \right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값
