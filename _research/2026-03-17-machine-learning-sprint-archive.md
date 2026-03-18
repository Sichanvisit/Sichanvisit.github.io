---
title: "Machine Learning Sprint Archive"
date: 2026-03-17
research_tab: "ML"
research_kind: "Track Overview"
excerpt: "Python 기초부터 예측과 분류 모델링까지 이어지는 ML 스프린트와 실습 파일을 포트폴리오형 기록으로 정리했습니다."
tags:
  - machine-learning
  - sprint-mission
  - scikit-learn
  - xgboost
header:
  teaser: /assets/images/research/ml-sprint.svg
classes: wide
---

## Research Snapshot

| Item | Summary |
|------|---------|
| Scope | Python 응용, 데이터 전처리, 통계/시각화, 지도학습, 앙상블, 차원 축소 |
| Main Stack | Python, pandas, matplotlib, seaborn, scikit-learn, XGBoost, LightGBM |
| Core Question | 데이터를 어떻게 해석하고, 지표에 맞는 피처와 모델을 어떻게 고를 것인가 |
| Portfolio Angle | "모델 성능 비교"보다 "문제에 맞는 실험 설계"가 보이는 트랙 |

## What I Practiced

- Python 기초 실습에서 자료구조, 클래스, 함수형 사고를 정리했습니다.
- `데이터사이언스 Toolkit`, `기초 통계와 데이터 시각화`, `DF 마스터하기` 노트로 EDA와 전처리 감각을 다졌습니다.
- 선형회귀, Lasso/Ridge, 로지스틱 회귀, KNN, SVM, 결정트리, RandomForest, AdaBoost, XGBoost, PCA, KMeans+PCA까지 폭넓게 다뤘습니다.
- 단순 정확도보다 문제별 평가 지표를 먼저 정하고, 그 지표를 개선하기 위한 피처 엔지니어링과 모델 선택을 반복했습니다.

## Highlighted Artifacts

| Artifact | Focus | Why It Matters |
|----------|-------|----------------|
| `[스프린트미션]2 Hotel Booking Demand` | 예약 취소 데이터 구조 이해, 결측/범주형 처리, 취소 관련 변수 해석 | EDA와 전처리 기준을 세우는 힘이 드러납니다. |
| `[스프린트미션]3_Bike Rental System` | `datetime` 파생 변수, 로그 변환, 다항 회귀, `GridSearchCV`, `XGBoost`, `RMSLE` 최적화 | 회귀 문제에서 지표 중심으로 실험을 설계한 흔적이 가장 선명합니다. |
| `[스프린트미션]4_Portuguese Bank Data Marketing` | 불균형 분류, 앙상블 비교, `Precision/Recall/F1/ROC-AUC`, `scale_pos_weight`, `LightGBM` | 분류 문제에서 비즈니스 기준과 지표 트레이드오프를 함께 고민했습니다. |
| 기초/확장 실습 묶음 | pandas, 통계, 시각화, 교차검증, PCA, 앙상블 | 스프린트 미션을 떠받치는 기본기와 복습 루틴이 보입니다. |

## Concrete Learning Points

### Bike Rental System

이 미션에서는 단순 회귀보다 `RMSLE`에 맞는 전처리와 피처 엔지니어링이 중요했습니다.  
시간 정보를 파생 변수로 분리하고, count 계열 변수를 로그 스케일로 다루며, 다항 회귀와 트리 기반 모델을 비교했습니다.  
실습 노트상 최종적으로는 `XGBoost`가 가장 좋은 결과를 보였고, 풍속 변수 제거 여부까지 실험한 점이 인상적이었습니다.

### Portuguese Bank Data Marketing

이 미션은 "예측을 얼마나 잘했는가"보다 "어떤 오류를 줄이는 것이 더 중요한가"를 먼저 생각하게 만든 사례였습니다.  
`Precision`과 `Recall` 중 무엇이 더 중요한지 비즈니스 관점에서 해석하고, 불균형 데이터 대응을 위해 `scale_pos_weight`, 결측치 처리, 여러 앙상블 모델 비교를 수행했습니다.  
노트에는 `LightGBM`의 Recall이 `0.65`까지 올라간 기록도 남아 있어, 지표 선택이 모델 방향을 어떻게 바꾸는지 잘 보여줍니다.

## What This Track Says About Me

- 데이터를 보기 전에 모델부터 고르기보다, 먼저 지표와 데이터 구조를 확인하는 편입니다.
- 회귀와 분류를 각각 다른 언어로 다뤄야 한다는 점을 실습을 통해 체득했습니다.
- 성능 숫자만 남기기보다, 왜 그 선택을 했는지를 설명 가능한 형태로 남기려는 습관이 생겼습니다.

## Next Experiments

- 불균형 분류 문제에 대해 `threshold tuning`과 `calibration`까지 확장하기
- 회귀 문제에서 시계열 누수 여부를 더 엄격하게 검증하기
- 대표 미션 하나를 별도 프로젝트로 분리해 대시보드형 포트폴리오로 확장하기
