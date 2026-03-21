---
title: "3 Bike Rental System - AI 5기 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]3_Bike Rental System - AI 5기 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md"
excerpt: "Bike Rental System의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 미션 설명, 데이터, 분석 드릴다운 순서로 큰 장을 먼저 훑고, train/test CSV 불러오기, StandardScaler 스케일링 같은 코드로 실제 구현을 이어서 확인..."
research_summary: "Bike Rental System의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 미션 설명, 데이터, 분석 드릴다운 순서로 큰 장을 먼저 훑고, train/test CSV 불러오기, StandardScaler 스케일링 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다."
research_artifacts: "ipynb/md · 코드 108개 · 실행 107개"
code_block_count: 108
execution_block_count: 107
research_focus:
  - "자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화..."
  - "🚲 미션 설명"
  - "$$ RMSLE = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} \\left( \\log(p..."
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

| 항목 | 내용 |
|------|------|
| 문제 설정 | 자전거 대여 시스템의 운영 담당자. 자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 |
| 원본 구조 | 미션 설명 -> 데이터 -> 분석 드릴다운 -> 데이터 확인 -> 데이터 전처리 |
| 데이터 맥락 | train.csv - 자전거 대여 수요를 예측하기 위한 데이터 포함 - 종속 변수: count test.csv |
| 주요 장 | 미션 설명 · 데이터 · 분석 드릴다운 · 데이터 확인 |
| 구현 흐름 | train/test CSV 불러오기 -> StandardScaler 스케일링 -> 파생 변수 추가 |
| 자료 | ipynb / md · 코드 108 · 실행 107 |
| 주요 스택 | matplotlib, warnings, numpy, pandas 외 1 |

## 원본 노트 흐름

### 미션 설명

자전거 대여 시스템의 운영 담당자 - 자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것

- 읽을 포인트: 세부 흐름: RMSLE 공식

#### RMSLE 공식

$$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(p_i + 1) - \log(a_i + 1) \right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값

### 데이터

train.csv - 자전거 대여 수요를 예측하기 위한 데이터 포함 - 종속 변수: count test.csv

- 읽을 포인트: 세부 흐름: 파일 설명

#### 파일 설명

train.csv - 자전거 대여 수요를 예측하기 위한 데이터 포함 - 종속 변수: count test.csv

### 분석 드릴다운

독립 변수로 볼 수 있는 값 중에 큰 치우침이 있는 데이터는 없는 것으로 확인 단, 몇 변수는 주의해서 데이터를 살펴봐야함 1. temp와 atemp: 최소 기온은 괜찮으나, 최고 기온이 41도, 45도 일반적이지 않음 => 데이터 살펴볼 필요성 있음 2. humidity: 최소 습도가 0과 최대가 100인 값이 존재할 수 있을지 확...

- 읽을 포인트: 세부 흐름: 공유 시스템 이해, 공유 시스템 이해 > 1차 데이터 확인 결과, 공유 시스템 이해 > EDA 포인트

#### 공유 시스템 이해

공유할 대상이 존재해야함 - 물리적 관점: 사용자가 찾는 시간과 장소에 자전거 없음 (퇴근 시간에 지하철역에 자전거 부족 등) - 관념적 관점: 사용하고 싶지 않게 만드는 요인을 제거 - 예: 자전거가 녹슬어 있음, 안장이 젖어 있음, 기종이 불편함, 과금 정책이 불투명 - 운영...

#### 공유 시스템 이해 > 1차 데이터 확인 결과

독립 변수로 볼 수 있는 값 중에 큰 치우침이 있는 데이터는 없는 것으로 확인 단, 몇 변수는 주의해서 데이터를 살펴봐야함 1. temp와 atemp: 최소 기온은 괜찮으나, 최고 기온이 41도, 45도 일반적이지 않음 => 데이터 살펴볼 필요성 있음 2. humidity: 최소...

#### 공유 시스템 이해 > EDA 포인트

holiday와 weekday의 대여 분포도 확인 - 날씨별 대여 확인 - 시간대별 대여 확인 - 계절별 대여 확인 - casual, registered는 제외하고 count만 종속변수로 확인 [1차 가설] 1. 자전거 대여 수요는 날씨와 시간의 영향을 가장 크게 받을 것이다. -...

### 데이터 확인

RMSLE 점수를 안정적으로 계산하기 위해 count 변수 모두 로그 변환 필요 모델이 큰 수에 맞춰 학습을 하면 RMSLE기준 불균형성이 확인될 수 있기 때문 - 모델이 로그 공간 안에서 예측하면 같은 스케일이 보장되기 때문에 안정적 학습 가능

- 읽을 포인트: 세부 흐름: 시각화: count의 분포 확인, season 데이터 확인

#### 시각화: count의 분포 확인

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

#### season 데이터 확인

데이터 확인 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

### 데이터 전처리

보퍼트 풍력계처럼 명확한 단계별 명칭 체계는 존재하지 않음. 단, 여러 단체에서 권장하는 습도 기준은 이정도 낮은 습도 1. 건조한 사막 습도 10~20% 언급 뉴스기사 - https://weekly.chosun.com/news/articleView.html?idxno=28844 2. 극한의 건조한 지역에 대한 습도 2% 언급 뉴스기...

- 읽을 포인트: 세부 흐름: (3) datetime 데이터 타입 변환, (5) 계절 변화 - season 컬럼 정리, (6) 이상치 제거

#### (3) datetime 데이터 타입 변환

입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.

#### (5) 계절 변화 - season 컬럼 정리

입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.

#### (6) 이상치 제거

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

### 데이터 시각화

새벽 시간과 저녁시간 대여량 급감 => 출퇴근 시간 대여 급증

- 읽을 포인트: 세부 흐름: (1) 변수별 대여량 다각도 시각화, (2) 상관관계 시각화, (3) 습도와 풍속 구간별 대여량

#### (1) 변수별 대여량 다각도 시각화

새벽 시간과 저녁시간 대여량 급감 => 출퇴근 시간 대여 급증

#### (2) 상관관계 시각화

모델링 전에 변수들 파악하기 위해 진행

#### (3) 습도와 풍속 구간별 대여량

=> 습도가 너무 낮을땐 자전거 대여 총합이 작고, 중간과 높을 때 대여량이 많다 - 일반적으로 육지는 겨울의 경우 매우 낮아지는 경우가 대부분 - 해양성 기후 혹은 상대적 우리나라 가을날씨를 겨울로 부르는 곳은 겨울에 습도가 높아지기도 함. 하지만 대개는 겨울에 습도가 낮아짐 -...

## 구현 흐름

### 1. train/test CSV 불러오기

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: `pd.read_csv`
- 코드 포인트: -

### 2. StandardScaler 스케일링

- 단계: 전처리
- 구현 의도: 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.
- 핵심 API: `StandardScaler`
- 코드 포인트: 표준화 - from sklearn.preprocessin...

### 3. 파생 변수 추가

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: `matplotlib`, `seaborn`
- 코드 포인트: 시간대별 정보로 다시 시각화 · 오전 여부

### 4. XGBoost 모델 구성

- 단계: 모델 구성
- 구현 의도: XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: `XGBoost`
- 코드 포인트: -

### 5. GridSearchCV 모델 학습

- 단계: 학습
- 구현 의도: 하이퍼파라미터 탐색이나 교차검증을 통해 단순 실행이 아니라 성능 비교까지 해본 학습 코드입니다.
- 핵심 API: `GridSearchCV`, `RMSLE`, `RMSE`
- 코드 포인트: 최종 모델 결과 저장 리스트 · 모델별 학습 및 평가

### 6. RMSLE 기준 성능 평가

- 단계: 평가
- 구현 의도: 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.
- 핵심 API: `RMSLE`, `RMSE`
- 코드 포인트: -

## 코드로 확인한 내용

### train/test CSV 불러오기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
train = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_train.csv')
test = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_test.csv')
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

### XGBoost 모델 구성

**직접 해본 단계**: 모델 구성

**핵심 API**: `XGBoost`

XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
from xgboost import XGBRegressor

model_xg = XGBRegressor()
model_xg.fit(X5_train, y5_train)
y5_pred_log = model_xg.predict(X5_val)
y5_pred = np.expm1(y5_pred_log)
y5_true = np.expm1(y5_val)
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

### RMSLE 기준 성능 평가

**직접 해본 단계**: 평가

**핵심 API**: `RMSLE`, `RMSE`

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
mae = mean_absolute_error(y5_true, y5_pred)
mse = mean_squared_error(y5_true, y5_pred)
rmse = np.sqrt(mean_squared_error(y5_true, y5_pred))
rmsle = np.sqrt(mean_squared_log_error(y5_true, y5_pred))
r2 = r2_score(y5_true, y5_pred)
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
