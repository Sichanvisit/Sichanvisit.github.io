---
title: "3 Bike Rental System - AI 5기 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]3_Bike Rental System - AI 5기 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md"
excerpt: "자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것"
research_summary: "자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것. $$ RMSLE = \\sqrt{\\frac{1}{n} \\sum_{i=1}^{n} \\left( \\log(p_i + 1) - \\log(a_i + 1) \\right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값. `md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다."
research_artifacts: "md · 코드 108개 · 실행 107개"
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
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - archive-note
---

자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것. $$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(p_i + 1) - \log(a_i + 1) \right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값. `md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다.

**빠르게 볼 수 있는 포인트**: 자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자..., 🚲 미션 설명, $$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}....

**남겨둔 자료**: `md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다.

**주요 스택**: `matplotlib`, `warnings`, `numpy`, `pandas`, `seaborn`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 108 |
| Execution Cells | 107 |
| Libraries | `matplotlib`, `warnings`, `numpy`, `pandas`, `seaborn`, `datetime`, `sklearn`, `google` |
| Source Note | `[스프린트미션]3_Bike Rental System - AI 5기 강사 답안` |

## What This Note Covers

### 🚲 미션 설명

자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것

### RMSLE 공식

$$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(p_i + 1) - \log(a_i + 1) \right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값

### 파일 설명

train.csv - 자전거 대여 수요를 예측하기 위한 데이터 포함 - 종속 변수: count

### 공유 시스템 이해

공유할 대상이 존재해야함 - 물리적 관점: 사용자가 찾는 시간과 장소에 자전거 없음 (퇴근 시간에 지하철역에 자전거 부족 등) - 관념적 관점: 사용하고 싶지 않게 만드는 요인을 제거 - 예: 자전거가 녹슬어 있음, 안장이 젖어 있음, 기종이 불편함, 과금 정책이 불투명 - 운영 전략 관점: 특정 지역에 자전거 몰림, 고장 난 자전거가 장시간 방치

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

### 평가 지표 해석

- 왜 필요한가: 정확도 하나만으로는 모델이 실제로 무엇을 잘하고 무엇을 놓치는지 충분히 설명할 수 없습니다.
- 왜 이 방식을 쓰는가: 문제 유형에 맞는 지표를 함께 보면 불균형 데이터, 오차 크기, 재현율 같은 중요한 관점을 놓치지 않을 수 있습니다.
- 원리: 예측 결과를 정답과 비교해 오차나 클래스별 성능을 수치화하고, 그 수치로 모델 선택과 개선 방향을 판단합니다.

## Implementation Flow

1. 🚲 미션 설명: 자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것
2. RMSLE 공식: $$ RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(p_i + 1) - \log(a_i + 1) \right)^2} $$ - n: 데이터 포인트의 수 - pi: 예측 값 - ai: 실제 값
3. 파일 설명: train.csv - 자전거 대여 수요를 예측하기 위한 데이터 포함 - 종속 변수: count
4. 공유 시스템 이해: 공유할 대상이 존재해야함 - 물리적 관점: 사용자가 찾는 시간과 장소에 자전거 없음 (퇴근 시간에 지하철역에 자전거 부족 등) - 관념적 관점: 사용하고 싶지 않게 만드는 요인을 제거 - 예: 자전거가 녹슬어 있음, 안장이 젖어 있음, 기종이 불편함, 과금 정책이 불투명 - 운영...

## Code Highlights

### (1) 1차 모델링

`(1) 1차 모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습 및 평가 흐름이 주석과 함께 드러납니다.

```python
# 모델 학습 및 평가
results_1 = []

for name, model in models.items():
    model.fit(X1_train, y1_train)
    y1_pred_log = model.predict(X1_val)
    y1_pred = np.expm1(y1_pred_log)                                     # np.expm1: 로그 역변환
    y1_true = np.expm1(y1_val)

    mae = mean_absolute_error(y1_true, y1_pred)
    mse = mean_squared_error(y1_true, y1_pred)
    rmse = np.sqrt(mean_squared_error(y1_true, y1_pred))
    rmsle = np.sqrt(mean_squared_log_error(y1_true, y1_pred))
    r2 = r2_score(y1_true, y1_pred)

    results_1.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "RMSLE": rmsle,
        "R제곱" : r2
    })
```

### (2) 2차 모델링

`(2) 2차 모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 최종 모델 결과 저장 리스트, 모델별 학습 및 평가 흐름이 주석과 함께 드러납니다.

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
# ... trimmed ...
```

### (3) 3차 모델링

`(3) 3차 모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 시간대별 정보로 다시 시각화, 오전 여부, 밤 여부 흐름이 주석과 함께 드러납니다.

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

# ... trimmed ...
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md`
- Source formats: `md`
- Companion files: `[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `windspeed`
- External references: `localhost`, `ko.wikipedia.org`, `weekly.chosun.com`, `www.dvidshub.net`, `en.wikipedia.org`

## Note Preview

> - 자전거 대여 시스템의 운영 담당자 - 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것 - 🎯최종 목표: **RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것**
> --------------------------------------------
