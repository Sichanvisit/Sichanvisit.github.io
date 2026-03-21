---
title: "3 Bike Rental System - AI 5기 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]3_Bike Rental System - AI 5기 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md"
excerpt: "자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것"
research_summary: "자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것. $$ RMSLE = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} \\left( \\log(p_i + 1) - \\log(a_i + 1) \\right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값. `ipynb/md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다."
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

자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것. $$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(p_i + 1) - \log(a_i + 1) \right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값. `ipynb/md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다.

**빠르게 볼 수 있는 포인트**: 자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자..., 🚲 미션 설명, $$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}....

**남겨둔 자료**: `ipynb/md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다.

**주요 스택**: `matplotlib`, `warnings`, `numpy`, `pandas`, `seaborn`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 108 |
| Execution Cells | 107 |
| Libraries | `matplotlib`, `warnings`, `numpy`, `pandas`, `seaborn`, `datetime`, `sklearn`, `google` |
| Source Note | `[스프린트미션]3_Bike Rental System - AI 5기 강사 답안` |

## What I Studied

### 🚲 미션 설명

자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것

### RMSLE 공식

$$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(p_i + 1) - \log(a_i + 1) \right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값

### 파일 설명

train.csv - 자전거 대여 수요를 예측하기 위한 데이터 포함 - 종속 변수: count

### 공유 시스템 이해

공유할 대상이 존재해야함 - 물리적 관점: 사용자가 찾는 시간과 장소에 자전거 없음 (퇴근 시간에 지하철역에 자전거 부족 등) - 관념적 관점: 사용하고 싶지 않게 만드는 요인을 제거 - 예: 자전거가 녹슬어 있음, 안장이 젖어 있음, 기종이 불편함, 과금 정책이 불투명 - 운영 전략 관점: 특정 지역에 자전거 몰림, 고장 난 자전거가 장시간 방치

## What I Tried in Code

1. 데이터 불러오기: train/test CSV 불러오기
2. 전처리: StandardScaler 스케일링
3. 피처 가공: 파생 변수 추가
4. 모델 구성: XGBoost 모델 구성
5. 학습: GridSearchCV 모델 학습
6. 평가: RMSLE 기준 성능 평가

## Code Evidence

### train/test CSV 불러오기

**직접 해본 단계**: 데이터 불러오기

`train/test CSV 불러오기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
train = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_train.csv')
test = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_test.csv')
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

`StandardScaler 스케일링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다. 코드에는 표준화 - from sklearn.preprocessin... 같은 처리 포인트도 함께 남아 있습니다.

```python
# 표준화 - from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

train["windspeed_z"] = scaler.fit_transform(train[["windspeed"]]).ravel()      # ravel(): Series로 저장하기 위해 필요
test["windspeed_z"] = scaler.fit_transform(test[["windspeed"]]).ravel()
```

### 파생 변수 추가

**직접 해본 단계**: 피처 가공

`파생 변수 추가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다. 코드에는 시간대별 정보로 다시 시각화, 오전 여부 같은 처리 포인트도 함께 남아 있습니다.

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

`XGBoost 모델 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

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

`GridSearchCV 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 하이퍼파라미터 탐색이나 교차검증을 통해 단순 실행이 아니라 성능 비교까지 해본 학습 코드입니다. 코드에는 최종 모델 결과 저장 리스트, 모델별 학습 및 평가 같은 처리 포인트도 함께 남아 있습니다.

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

`RMSLE 기준 성능 평가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
mae = mean_absolute_error(y5_true, y5_pred)
mse = mean_squared_error(y5_true, y5_pred)
rmse = np.sqrt(mean_squared_error(y5_true, y5_pred))
rmsle = np.sqrt(mean_squared_log_error(y5_true, y5_pred))
r2 = r2_score(y5_true, y5_pred)
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `train/test CSV 불러오기` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 전처리 코드를 남기는 이유

- 왜 필요한가: 머신러닝에선 모델보다 먼저 입력 데이터의 결측치, 범주형 값, 스케일을 어떻게 다뤘는지가 성능을 크게 바꿉니다.
- 왜 이 방식을 쓰는가: 그래서 `StandardScaler 스케일링` 같은 코드를 통해 실제로 어떤 정제 규칙을 적용했는지 문장보다 코드로 먼저 보여주도록 정리했습니다.
- 원리: 원본 데이터를 모델이 다루기 쉬운 수치 형태로 바꾸면 같은 알고리즘이어도 학습 안정성과 해석 가능성이 함께 올라갑니다.

### 파생 변수를 직접 만든 부분

- 왜 필요한가: 원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `파생 변수 추가` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.
- 원리: 좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `XGBoost 모델 구성`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md`
- Source formats: `ipynb`, `md`
- Companion files: `[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.ipynb`, `[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `windspeed`
- External references: `localhost`, `ko.wikipedia.org`, `weekly.chosun.com`, `www.dvidshub.net`, `en.wikipedia.org`

## Note Preview

> - 자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: **RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것**
> --------------------------------------------
