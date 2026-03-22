---
title: "2 Hotel Booking Demand"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md"
excerpt: "Hotel Booking Demand의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 설명, 분석 방향, 데이터 불러오고 확인하기 순서로 큰 장을 먼저 훑고, (2) 결측치, (2) 시각화 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ip..."
research_summary: "Hotel Booking Demand의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 설명, 분석 방향, 데이터 불러오고 확인하기 순서로 큰 장을 먼저 훑고, (2) 결측치, (2) 시각화 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다."
research_artifacts: "ipynb/md · 코드 95개 · 실행 95개"
code_block_count: 95
execution_block_count: 95
research_focus:
  - "is_canceled와 연관도가 있다고 의심할 수 있는 컬럼 (상대적으로 절댓값이 높은 값) - lea..."
  - "2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터"
  - "Lead Time (예약 후 도착까지 기간) - 리드타임이 길수록 예약 취소율이 뚜렷하게 증가함"
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

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터 관련 링크 1. Kaggle: https://www.kaggle.com/datasets/jessemostipak/...</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">데이터 설명 -&gt; 데이터 불러오고 확인하기 -&gt; 데이터 전처리 -&gt; 데이터 시각화 -&gt; 분석 방향</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터 관련 링크 1. Kaggle: https://www.kaggle.com/datasets/jessemostipak/...</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">데이터 설명 · 분석 방향 · 데이터 불러오고 확인하기 · 추가 분석 Point</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">(2) 결측치 -&gt; (2) 시각화 -&gt; 데이터 불러오고 확인하기</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 95 · 실행 95</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">matplotlib, warnings, pandas, numpy 외 1</div>
  </div>
</div>

## 원본 노트 흐름

### 데이터 설명

2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터 관련 링크 1. Kaggle: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand 2. https://www.sciencedirect.com/science/ar...

- 읽을 포인트: 데이터 구조와 주의할 변수부터 읽고 실험 방향을 정리하는 구간입니다.

### 분석 방향

is_canceled와 연관이 높은 컬럼들을 다루고, 취소에 영향을 미치는 요인이 뭔지 알아본다! stays_in_week_nights

- 읽을 포인트: 세부 흐름: lead_time 시각화, lead_time에 따른 취소율 시각화 - kde 플롯, 🧪 분석 방향

#### lead_time 시각화

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

#### lead_time에 따른 취소율 시각화 - kde 플롯

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

#### 🧪 분석 방향

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

### 데이터 불러오고 확인하기

전체 119390행 29열의 구조 - company 열에 결측치가 많음 (agent도 일부 결측치 확인) - 8월에 여행을 많이 함 => (arrival_date_month의 top 참조) canceled는 0과 1의 값으로 이루어져 있는데, 평균이 0.370416인 것으로 보아 취소된 예약건이 적은 데이터로 추정 - reservat...

- 읽을 포인트: 세부 흐름: 라이브러리 임포트, 드라이브 마운트 코드, Data type 확인하는 추가 코드

#### 라이브러리 임포트

넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.

#### 드라이브 마운트 코드

데이터 불러오고 확인하기 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

#### Data type 확인하는 추가 코드

데이터 불러오고 확인하기 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

### 추가 분석 Point

특정 변수들에 따른 분석 진행 - 예약된 어른의 수와 아이 또는 아기의 수를 조합 - 가족여행 - 연인(부부만)의 여행 - 기존에 호텔에 의해 변경된 예약의 경우 취소를 할까? - reserved_room_type과 assigned_room_type 분석 - 호텔별 예약 취소 비교 - Resort Hotel과 City Hotel의 예...

- 읽을 포인트: 추가 분석 Point 아래 코드와 함께 읽으면 구현 의도가 더 잘 보이는 구간입니다.

### 데이터 전처리

(1) 중복값, (2) 결측치, (3) 이상치 같은 코드를 직접 따라가며 데이터 전처리 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: (1) 중복값, (2) 결측치, (3) 이상치

#### (1) 중복값

(1) 중복값 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

#### (2) 결측치

=> 어른의 수가 0명일 때, 어린이나 아기가 포함되는 여행은 존재하지 않음 법적인 문제 발생 - 대부분의 호텔은 적어도 성인 1명당 어린아이 투숙을 허용

#### (3) 이상치

유럽에서 가장 큰 스위트룸 중 하나인 "Royal Residence" 설명 - Basque Luxury - The Royal Residence: the largest suite in Europe: https://basqueluxury.com/en/the-royal-residence...

### 데이터 시각화

(1) 시각화 위한 데이터 탐색, (2) 시각화, (2) 시각화 > 상관관계 해석 같은 코드를 직접 따라가며 데이터 시각화 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: (1) 시각화 위한 데이터 탐색, (2) 시각화, (2) 시각화 > 상관관계 해석

#### (1) 시각화 위한 데이터 탐색

is_canceled==0와 reservation_status =='Check-out'의 데이터가 같은건지 확인 필요 is_canceled==0와 reservation_status =='Check-out'의 데이터가 같음 - 취소하지 않은 예약건은 모두 reservation_sta...

#### (2) 시각화

=> days_in_waiting_list값은 0만 있으므로 상관도 계산 불가 (피어슨 상관계수의 식 - 표준편차로 나눠줘야 함!) 해당 변수 제외하고 다시 상관관계 히트맵 그리기

#### (2) 시각화 > 상관관계 해석

is_canceled와 연관도가 있다고 의심할 수 있는 컬럼 (상대적으로 절댓값이 높은 값) - lead_time - arrival_date_day_of_year - arrival_date_day_of_year은 상대적 상관도는 높으나 의미있는 데이터는 아닐거라고 판단해 is_ca...

### 결론

변수별 취소율 분석 요약 같은 코드를 직접 따라가며 결론 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 변수별 취소율 분석 요약

#### 변수별 취소율 분석 요약

Lead Time (예약 후 도착까지 기간) - 리드타임이 길수록 예약 취소율이 뚜렷하게 증가함 특히 300일 이상 리드타임 구간은 취소율이 50% 이상으로 매우 높음

### 인사이트 (Action Plan)

Lead Time이 길수록 취소율 증가, 주중 장기 숙박일 수록 예약 취소율 증가, 재방문 고객은 확실히 충성도 높고... 같은 코드를 직접 따라가며 인사이트 (Action Plan) 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Lead Time이 길수록 취소율 증가, 주중 장기 숙박일 수록 예약 취소율 증가, 재방문 고객은 확실히 충성도 높고 취소율 낮음

#### Lead Time이 길수록 취소율 증가

=> 리드타임(예약 후 도착까지 기간)이 길수록 고객의 일정 변경 가능성도 높아지며, 300일 이상인 경우 취소율이 50%를 초과함 Action Plan

#### 주중 장기 숙박일 수록 예약 취소율 증가

=> 한달 미만의 예약건 기준, 장기 예약일수록 예약취소율 증가 Action Plan

#### 재방문 고객은 확실히 충성도 높고 취소율 낮음

=> 신규 고객의 취소율은 37%, 재방문 고객은 10% 이하 → 매우 안정적이고 충성도 높음 Action Plan

## 구현 흐름

### 1. (2) 결측치

- 단계: 전처리
- 구현 의도: 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.
- 핵심 API: -
- 코드 포인트: 결측치 행 제거 - company

### 2. (2) 시각화

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: `matplotlib`, `seaborn`
- 코드 포인트: 상관행렬 계산 · 히트맵 시각화

### 3. 데이터 불러오고 확인하기

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: `pd.read_csv`
- 코드 포인트: -

### 4. 🧪 분석 방향

- 단계: 시각화
- 구현 의도: 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.
- 핵심 API: `matplotlib`, `seaborn`
- 코드 포인트: lead_time 시각화 · 단위 구간으로 나누어 범주형 변수 생성

### 5. (3) 이상치

- 단계: 구현 코드
- 구현 의도: (3) 이상치 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: 빈도수 기준으로 정렬된 고유값과 개수 확인

### 6. (1) 시각화 위한 데이터 탐색

- 단계: 구현 코드
- 구현 의도: (1) 시각화 위한 데이터 탐색 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: 호텔별 취소 건수 비교

## 코드로 확인한 내용

### (2) 결측치

**직접 해본 단계**: 전처리

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

```python
# 결측치 행 제거 - company
df.dropna(inplace=True)
df.isnull().sum()
```

### (2) 시각화

**직접 해본 단계**: 피처 가공

**핵심 API**: `matplotlib`, `seaborn`

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

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

### 데이터 불러오고 확인하기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 4기/공유폴더/Data/hotel_data_modified.csv')
df
```

### 🧪 분석 방향

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`, `seaborn`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

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

### (3) 이상치

**직접 해본 단계**: 구현 코드

(3) 이상치 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["lead_time"].value_counts().sort_index()
```

### (1) 시각화 위한 데이터 탐색

**직접 해본 단계**: 구현 코드

(1) 시각화 위한 데이터 탐색 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python
# 호텔별 취소 건수 비교
df.groupby(by='hotel')['is_canceled'].value_counts()
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md`
- Source formats: `ipynb`, `md`
- Companion files: `[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.ipynb`, `[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md`
- Note type: `roadmap`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `"adults", "booking_changes", "children", "babies","required_car_parking_spaces",`
- External references: `localhost`, `www.kaggle.com`, `www.sciencedirect.com`, `basqueluxury.com`, `www.dayuse.com`

## 원문 미리보기

> 2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터
> **관련 링크** 1. Kaggle: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand 2. https://www.sciencedirect.com/science/article/pii/S2352340918315191
