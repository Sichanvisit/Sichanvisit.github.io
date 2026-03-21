---
title: "2 Hotel Booking Demand - AI5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md"
excerpt: "2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터"
research_summary: "2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터. 전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인) - 8월에 여행을 많이 함 => (arrival_date_month의 top 참조). `ipynb/md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다."
research_artifacts: "ipynb/md · 코드 95개 · 실행 95개"
code_block_count: 95
execution_block_count: 95
research_focus:
  - "2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터"
  - "🏨 데이터 설명"
  - "전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인..."
research_stack:
  - "matplotlib"
  - "warnings"
  - "pandas"
  - "numpy"
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

2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터. 전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인) - 8월에 여행을 많이 함 => (arrival_date_month의 top 참조). `ipynb/md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다.

**빠르게 볼 수 있는 포인트**: 2015.07.01부터 2017.08.31까지의 Resort Hotel..., 🏨 데이터 설명, 전체 119390행 29열의 구조 - company 열에 결측치가 많음....

**남겨둔 자료**: `ipynb/md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다.

**주요 스택**: `matplotlib`, `warnings`, `pandas`, `numpy`, `seaborn`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 95 |
| Execution Cells | 95 |
| Libraries | `matplotlib`, `warnings`, `pandas`, `numpy`, `seaborn`, `google` |
| Source Note | `[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안` |

## What I Studied

### 🏨 데이터 설명

2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터

### 데이터 불러오고 확인하기

전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인) - 8월에 여행을 많이 함 => (arrival_date_month의 top 참조)

### (2) 결측치

=> 어른의 수가 0명일 때, 어린이나 아기가 포함되는 여행은 존재하지 않음

### (3) 이상치

유럽에서 가장 큰 스위트룸 중 하나인 "Royal Residence" 설명 - Basque Luxury - The Royal Residence: the largest suite in Europe: https://basqueluxury.com/en/the-royal-residence-the-largest-suite-in-europe/

## What I Tried in Code

1. 데이터 불러오기: 데이터 불러오고 확인하기
2. 전처리: (2) 결측치
3. 피처 가공: (2) 시각화
4. 시각화: 🧪 분석 방향
5. 환경 준비: 데이터 불러오고 확인하기
6. 구현 코드: 🧪 분석 방향

## Code Evidence

### 데이터 불러오고 확인하기

**직접 해본 단계**: 데이터 불러오기

`데이터 불러오고 확인하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 4기/공유폴더/Data/hotel_data_modified.csv')
df
```

### (2) 결측치

**직접 해본 단계**: 전처리

`(2) 결측치`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다. 코드에는 결측치 행 제거 - company 같은 처리 포인트도 함께 남아 있습니다.

```python
# 결측치 행 제거 - company
df.dropna(inplace=True)
df.isnull().sum()
```

### (2) 시각화

**직접 해본 단계**: 피처 가공

`(2) 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다. 코드에는 상관행렬 계산, 히트맵 시각화 같은 처리 포인트도 함께 남아 있습니다.

```python
temp_df = df[['is_canceled', 'lead_time', 'arrival_date_year',
       'arrival_date_week_number', 'arrival_date_day_of_month',
       'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children',
       'babies', 'is_repeated_guest', 'previous_cancellations',
       'previous_bookings_not_canceled', 'booking_changes',
       'required_car_parking_spaces','total_of_special_requests']]

# 상관행렬 계산
full_corr_matrix = temp_df.corr()

# 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(full_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("수치형 변수 상관관계 히트맵")
plt.tight_layout()
plt.show()
```

### 🧪 분석 방향

**직접 해본 단계**: 시각화

`🧪 분석 방향`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 lead_time 시각화, 단위 구간으로 나누어 범주형 변수 생성 같은 처리 포인트도 함께 남아 있습니다.

```python
# lead_time 시각화

# 단위 구간으로 나누어 범주형 변수 생성
df["lead_time_bin"] = pd.cut(df["lead_time"], bins=range(0, 390, 30))

# 구간별 평균 취소율 집계후 집계 구간별 라벨 생성
agg = (df.groupby("lead_time_bin", observed=True)["is_canceled"].mean().reset_index())
agg["bin_label"] = agg["lead_time_bin"].astype(str)

plt.figure(figsize=(10,5))
sns.barplot(data=df, x="lead_time_bin", y="is_canceled", errorbar=None)
sns.lineplot(data=agg, x="bin_label", y="is_canceled", marker="o", color="Red")
plt.title('Lead Time 구간별 예약 취소율')
plt.xlabel('Lead Time 구간')
plt.ylabel('취소율')
plt.ylim(0, 0.6)         # 취소율로 y축을 설정하기 위해 필요
plt.xticks(rotation=45)
plt.show()
```

### 데이터 불러오고 확인하기

**직접 해본 단계**: 환경 준비

`데이터 불러오고 확인하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 라이브러리 임포트 같은 처리 포인트도 함께 남아 있습니다.

```python
# 라이브러리 임포트
import pandas as pd
import numpy as np
import seaborn as sns
```

### 🧪 분석 방향

**직접 해본 단계**: 구현 코드

`🧪 분석 방향`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 is_repeated_guest 시각화, 그룹별 평균 취소율 같은 처리 포인트도 함께 남아 있습니다.

```python
# is_repeated_guest 시각화

# 그룹별 평균 취소율
repeat_cancel = df.groupby('is_repeated_guest')['is_canceled'].mean().reset_index()
repeat_cancel['is_repeated_guest'] = repeat_cancel['is_repeated_guest'].map({0: '신규 고객', 1: '재방문 고객'})
repeat_cancel.columns = ['고객 유형', '평균 취소율']
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `데이터 불러오고 확인하기` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 전처리 코드를 남기는 이유

- 왜 필요한가: 머신러닝에선 모델보다 먼저 입력 데이터의 결측치, 범주형 값, 스케일을 어떻게 다뤘는지가 성능을 크게 바꿉니다.
- 왜 이 방식을 쓰는가: 그래서 `(2) 결측치` 같은 코드를 통해 실제로 어떤 정제 규칙을 적용했는지 문장보다 코드로 먼저 보여주도록 정리했습니다.
- 원리: 원본 데이터를 모델이 다루기 쉬운 수치 형태로 바꾸면 같은 알고리즘이어도 학습 안정성과 해석 가능성이 함께 올라갑니다.

### 파생 변수를 직접 만든 부분

- 왜 필요한가: 원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `(2) 시각화` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.
- 원리: 좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.

### 시각화를 같이 남긴 이유

- 왜 필요한가: 숫자만 보면 놓치기 쉬운 분포와 이상치를 그래프로 확인해야 다음 전처리나 feature engineering 방향이 또렷해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `🧪 분석 방향` 코드를 통해 어떤 그래프를 보고 판단했는지 실습 흔적을 남겼습니다.
- 원리: 시각화는 데이터 분포를 직관적으로 드러내 모델 선택과 변수 설계의 근거를 만들어 줍니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md`
- Source formats: `ipynb`, `md`
- Companion files: `[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.ipynb`, `[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md`
- Note type: `roadmap`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `"adults", "booking_changes", "children", "babies","required_car_parking_spaces",`
- External references: `localhost`, `www.kaggle.com`, `www.sciencedirect.com`, `basqueluxury.com`, `www.dayuse.com`

## Note Preview

> 2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터
> **관련 링크** 1. Kaggle: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand 2. https://www.sciencedirect.com/science/article/pii/S2352340918315191
