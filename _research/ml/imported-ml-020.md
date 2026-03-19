---
title: "2 Hotel Booking Demand - AI5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md"
excerpt: "2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터"
research_summary: "2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터. 전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인) - 8월에 여행을 많이 함 => (arrival_date_month의 top 참조). `md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다."
research_artifacts: "md · 코드 95개 · 실행 95개"
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
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - archive-note
---

2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터. 전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인) - 8월에 여행을 많이 함 => (arrival_date_month의 top 참조). `md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다.

**빠르게 볼 수 있는 포인트**: 2015.07.01부터 2017.08.31까지의 Resort Hotel..., 🏨 데이터 설명, 전체 119390행 29열의 구조 - company 열에 결측치가 많음....

**남겨둔 자료**: `md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다.

**주요 스택**: `matplotlib`, `warnings`, `pandas`, `numpy`, `seaborn`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 95 |
| Execution Cells | 95 |
| Libraries | `matplotlib`, `warnings`, `pandas`, `numpy`, `seaborn`, `google` |
| Source Note | `[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안` |

## What This Note Covers

### 🏨 데이터 설명

2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터

### 데이터 불러오고 확인하기

전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인) - 8월에 여행을 많이 함 => (arrival_date_month의 top 참조)

### (2) 결측치

=> 어른의 수가 0명일 때, 어린이나 아기가 포함되는 여행은 존재하지 않음

### (3) 이상치

유럽에서 가장 큰 스위트룸 중 하나인 "Royal Residence" 설명 - Basque Luxury - The Royal Residence: the largest suite in Europe: https://basqueluxury.com/en/the-royal-residence-the-largest-suite-in-europe/

## Implementation Flow

1. 🏨 데이터 설명: 2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터
2. 데이터 불러오고 확인하기: 전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인) - 8월에 여행을 많이 함 => (arrival_date_month의 top 참조)
3. (2) 결측치: => 어른의 수가 0명일 때, 어린이나 아기가 포함되는 여행은 존재하지 않음
4. (3) 이상치: 유럽에서 가장 큰 스위트룸 중 하나인 "Royal Residence" 설명 - Basque Luxury - The Royal Residence: the largest suite in Europe: https://basqueluxury.com/en/the-royal-residence-...

## Code Highlights

### (2) 시각화

`(2) 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 상관행렬 계산, 히트맵 시각화 흐름이 주석과 함께 드러납니다.

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

`🧪 분석 방향`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 lead_time 시각화, 단위 구간으로 나누어 범주형 변수 생성, 구간별 평균 취소율 집계후 집계 구간별 라벨 생성 흐름이 주석과 함께 드러납니다.

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

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md`
- Source formats: `md`
- Companion files: `[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md`
- Note type: `roadmap`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `"adults", "booking_changes", "children", "babies","required_car_parking_spaces",`
- External references: `localhost`, `www.kaggle.com`, `www.sciencedirect.com`, `basqueluxury.com`, `www.dayuse.com`

## Note Preview

> 2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터
> **관련 링크** 1. Kaggle: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand 2. https://www.sciencedirect.com/science/article/pii/S2352340918315191
