---
title: "2 Hotel Booking Demand"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md"
excerpt: "Hotel Booking Demand의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 전처리, 데이터 시각화, 데이터 불러오고 확인하기 순서로 큰 장을 먼저 훑고, 파생 변수 추가, 결측치 정리 같은 코드로 실제 구현을 이어서 확인할 수 있습니다...."
research_summary: "Hotel Booking Demand의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 전처리, 데이터 시각화, 데이터 불러오고 확인하기 순서로 큰 장을 먼저 훑고, 파생 변수 추가, 결측치 정리 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다."
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
    <div class="research-overview__value">데이터 전처리 · 데이터 시각화 · 데이터 불러오고 확인하기 · 분석 방향</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">CSV 데이터 불러오기 -&gt; 결측치 정리 -&gt; (2) 결측치</div>
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

```python
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

!apt-get update -qq
!apt-get install fonts-nanum* -qq

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings(action='ignore')

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf' # 나눔 고딕
font_name = fm.FontProperties(fname=path, size=10).get_name() # 기본 폰트 사이즈 : 10
plt.rc('font', family=font_name)

fm.fontManager.addfont(path)
```

### 데이터 설명

2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터

**관련 링크**
1. Kaggle: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
2. https://www.sciencedirect.com/science/article/pii/S2352340918315191

**호텔 예약 데이터셋 변수 설명표**

| 컬럼명                              | 설명                                                                           |
| -------------------------------- | ---------------------------------------------------------------------------- |
| `hotel`                          | 호텔명 (`Resort Hotel` 또는 `City Hotel`)                                         |
| `is_canceled`                    | 예약 취소 여부 (`1`: 취소, `0`: 취소 아님)                                               |
| `lead_time`                      | 예약일과 도착일 사이 기간 (일 단위)                                                        |
| `arrival_date_year`              | 도착 연도                                                                        |
| `arrival_date_month`             | 도착 월                                                                         |
| `arrival_date_week_number`       | 도착 주차 (예: 셋째 주 → 3)                                                          |
| `arrival_date_day_of_month`      | 도착 일자 (예: 3월 2일 → 2)                                                         |
| `stays_in_weekend_nights`        | 주말 숙박일 수 (토\~일)                                                              |
| `stays_in_week_nights`           | 주중 숙박일 수 (월\~금)                                                              |
| `adults`                         | 어른 수                                                                         |
| `children`                       | 어린이 수                                                                        |
| `babies`                         | 아기 수                                                                         |
| `meal`                           | 식사 옵션<br>- `Undefined`/`SC`: 없음<br>- `BB`: 조식<br>- `HB`: 조식+1식<br>- `FB`: 3식 |
| `country`                        | 투숙객의 출신 국가 (ISO 코드 형식)                                                       |
| `market_segment`                 | 시장 세그먼트 (`TA`: Travel Agent, `TO`: Tour Operator 등)                          |
| `distribution_channel`           | 예약 유통 채널 (`TA`, `TO` 등)                                                      |
| `is_repeated_guest`              | 재방문 여부 (`1`: 재방문, `0`: 첫 방문)                                                 |
| `previous_cancellations`         | 과거 예약 취소 횟수                                                                  |
| `previous_bookings_not_canceled` | 과거 예약 유지 횟수                                                                  |
| `reserved_room_type`             | 예약한 객실 타입 코드                                                                 |
| `assigned_room_type`             | 실제 배정된 객실 타입 코드                                                              |
| `booking_changes`                | 예약 변경 횟수                                                                     |
| `agent`                          | 예약을 담당한 여행사 ID                                                               |
| `company`                        | 예약금 지불 주체 (회사 또는 단체 ID)                                                      |
| `days_in_waiting_list`           | 대기자 명단에 있었던 일수                                                               |
| `required_car_parking_spaces`    | 요구한 주차 공간 수                                                                  |
| `total_of_special_requests`      | 특별 요청 건수 (예: 고층, 트윈베드 등)                                                     |
| `reservation_status`             | 예약 상태 (`Canceled`, `Check-Out`, `No-Show`)                                   |
| `reservation_status_date`        | 마지막 예약 상태가 기록된 날짜                                                            |

**분석 목표**

예약 취소와 관련이 있는 요소들을 파악해보고, 예약 취소율을 줄이기 위한 아이디어를 생각한다. 예약 취소율을 어떻게 하면 개선할 수 있을지 인사이트를 낸다.

## 1. 데이터 불러오고 확인하기

```python
# 라이브러리 임포트
import pandas as pd
import numpy as np
import seaborn as sns
```

```python
# 드라이브 마운트 코드
from google.colab import drive
drive.mount('/content/drive/')
```

```python
df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 4기/공유폴더/Data/hotel_data_modified.csv')
df
```

```python
df.info()
```

```python
# Data type 확인하는 추가 코드
df.dtypes
```

```python
df.describe()
```

```python
#  include=all: 범주형도 포함
df.describe(include="all")
```

```python
# 컬럼 편하게 보기 - 전치행렬 변환
df.describe().T
```

**<데이터 1차 확인 결과>**
- 전체 119390행 29열의 구조
- company 열에 결측치가 많음 (agent도 일부 결측치 확인)
- 8월에 여행을 많이 함 => (arrival_date_month의 top 참조)
---

- canceled는 0과 1의 값으로 이루어져 있는데, 평균이 0.370416인 것으로 보아 취소된 예약건이 적은 데이터로 추정
     - reservation_status을 통해 예약을 취소하지 않은 케이스를 세분화하여 분석할 수 있음
- stays_in_weekend_nights와 stays_in_week_nights로 주말, 주중으로 따로 데이터를 구분해 놓았는데, 주중 주말 연달아 예약하는 건수가 있는지 확인 필요
    - 고객 호텔 도착 일(arrival_date_day_of_month) 참조하면 가능할 것으로 예상

    => 최종적으로 진행하지 않음
- 예약 건당, 예약된 어른의 수와 아이 또는 아기의 수를 조합하여 가족이 온 여행인지, 연인(부부만)의 여행인지 판단 가능
- 이전에 예약을 취소해 본 경험이 있을때 취소율이 높은지 확인 가능
    - previous_cancellations와 previous_bookings_not_canceled 비교
    - previous_bookings_not_canceled 값도 비교해서 볼 수 있음
- 예약 변경이나 수정을 할 경우 예약 취소율이 높은지 비교할 필요 있음
    - booking_changes
- 고객의 특별 예약 요청이 취소율에 영향이 있는지 확인할 필요 있음
    - total_of_special_requests
- 나라별 취소 특징이 있는지 확인할 필요 있음

    => 최종적으로 진행하지 않음
- reservation_status를 보고 데이터의 상태에 따라 "호텔 예약 취소" 기준 마련 가능할 것으로 예상
- reservation_status_date의 데이터를 보고 데이터의 품질 파악 가능할 것으로 예상
- skewed된 데이터 컬럼
    - required_car_parking_spaces 평균: 0.6, 중앙값: 0, Max: 8
    - days_in_waiting_list 평균: 2.32, 중앙값 0, Max: 391
    - company 역시 치우침 발생
    - agent: 대행사별 코드(ID)라서 그런듯
    - booking_changes 평균: 0.22, 중앙값: 0, Max: 21
    - 그 외 total_of_special_requests, previous_bookings_not_canceled, previous_cancellations, babies등 많은 데이터가 right-skwed되어있음

```python
plt.figure(figsize=(13,3))
sns.heatmap(df.isnull(),  yticklabels=False, cbar=False)
plt.title("호텔 데이터 결측치 시각화")
#plt.xticks(rotation=45)
plt.show()
```

```python
# 결측치 비율 확인 - 0인 컬럼이 많아 0보다 큰 값만 보기로 결정
(df.isnull().sum()/len(df) * 100)[lambda x: x > 0].sort_values(ascending=False)
```

```python
df['children'].unique()
```

```python
print(df['children'].isnull().sum())
```

```python
print(df['country'].isnull().sum())
```

**결론**

- company와 agent는 결측치의 비율이 높아 열 삭제 결정

    => agent로 따로 할 분석 주제를 지정하지 않았기 때문에 삭제하는 방향으로 결정
- children의 결측치는 아래에서 중복행 삭제 후 다시 확인한 뒤, 결측치는 다른 값으로 넣어줄 예정
- country 역시 중복행 삭제 후 다시 확인한 뒤 방향성 결정

---
## 2. 데이터 전처리

### 1) 중복값

```python
# 중복행 확인
print(df.duplicated().sum())
```

```python
# 중복값 비율 계산 - 이런건 분석 보고서에는 포함하지 않음
33130/len(df) * 100
```

```python
# 중복 제거
df.drop_duplicates(inplace=True)
```

```python
# 중복 제거 확인
df.shape
```

### 2) 결측치

```python
# 결측치가 많은 컬럼 제거
df.drop(columns=['company', 'agent'], axis=1, inplace=True)
```

```python
# 컬럼 삭제 되었는지 확인
df.columns
```

```python
print(df['children'].isnull().sum())
```

```python
print(df['country'].isnull().sum())
```

```python
# country열의 결측치 비율 계산
451/len(df) * 100
```

```python
df['children'].value_counts()
```

```python
# children열 결측치 최빈값으로 채우기
df["children"] = df["children"].fillna(df["children"].mode()[0])
```

```python
# 결측치 행 제거 - company
df.dropna(inplace=True)
df.isnull().sum()
```

```python
# adults가 0인데 children 또는 babies가 1명 이상인 경우 필터링
df[(df['adults'] == 0) & ((df['children'] > 0) | (df['babies'] > 0))]
```

```python
# 아이만 있고 어른이 없는 예약건 전체 비율 확인
(len(df[(df['adults'] == 0) & ((df['children'] > 0) | (df['babies'] > 0))]) / len(df)) * 100
```

=> 어른의 수가 0명일 때, 어린이나 아기가 포함되는 여행은 존재하지 않음

- 법적인 문제 발생
- 대부분의 호텔은 적어도 성인 1명당 어린아이 투숙을 허용

```python
# 어른 데이터가 0으로 잘못 입력 혹은 결측치로 판단하고 해당 값 삭제
df = df[~((df['adults'] == 0) & ((df['children'] > 0) | (df['babies'] > 0)))]
len(df)
```

```python
# 결측 제거 후 남은 데이터 비율 확인 - 이런건 분석 보고서에는 포함하지 않음
85619/86287 * 100
```

### 3) 이상치

```python
# 최대값이 독특해 보이는 컬럼만 확인
df[["adults", "booking_changes", "children", "babies","required_car_parking_spaces", "booking_changes", "days_in_waiting_list", "total_of_special_requests", "previous_bookings_not_canceled", "previous_cancellations"]].describe()
```

```python
df["adults"].value_counts().sort_index()
```

```python
df[df['adults'] > 30].T
```

**참고**

- 유럽에서 가장 큰 스위트룸 중 하나인 "Royal Residence" 설명
    - Basque Luxury - The Royal Residence: the largest suite in Europe: https://basqueluxury.com/en/the-royal-residence-the-largest-suite-in-europe/

    - 침실 8개, 욕실 8개, 완비된 주방이 있는 다이닝룸, 거실 2개, 오리엔탈룸 1개, 전용 엘리베이터가 있는 차고, 그리고 830m²(250평 이상) 규모의 테라스

**adults**

- 호텔 예약이라는 특수성에 의거하여, 어른의 수가 40명 이상이라는 것은 무리가 있음
    - 일반적인 고객 행동 분석이라면 adults는 10 이상인 경우 필요없음
        - 분석 목적에 따른 데이터 전처리가 필요한 이유!
    - 리조트 예약 한 건이라 할지라도 어른 30명 즉, 적어도 10~15개 이상의 각자 방을 가지는 리조트 형태는 없을 것으로 판단

    => 어른 수 30이상은 이상치로 판단하고 삭제

        - 마찬가지로 AI 4기 현업 경험이 있는 분과 확인한 내용

```python
# 어른의 수가 30 미만인 데이터만 남기고 삭제
df = df[df["adults"] < 30]
```

```python
df["babies"].value_counts().sort_index()
```

```python
df[df['babies'] > 8].T
```

**babies**

- 어른 한 명당 아이가 여러명인 것은 이상한 데이터라고 판단
- 아이가 9명과 10명인 경우 오류 데이터라고 생각해 최빈값으로 대체

 - babies 데이터는 unique가 각 0, 1, 2, 9, 10이며, 9값 부터 일반적인 범주로 볼 수 없다고 판단
 - 이 부분은 계속 고민이 필요한 영역일 수도 있으나, unique의 독특한 분포와 데이터의 전체 수를 기반해 판단한 결정

```python
# babies 이상치 최빈값으로 채우기
most_common_babies = df['babies'].mode()[0]
df.loc[df['babies'] > 8, 'babies'] = most_common_babies
```

```python
# 잘 바뀌었는지 확인
df.loc[[46619, 7000]].T
```

```python
df["required_car_parking_spaces"].value_counts().sort_index()
```

```python
df[df['required_car_parking_spaces'] > 7].T
```

**required_car_parking_spaces**
- 어른 2명의 여행에 주차공간 8은 입력을 잘못한 것으로 판단
- 0으로 대체

```python
# 주차 공간 8인 값 0으로 바꾸기
df.loc[df['required_car_parking_spaces'] == 8, 'required_car_parking_spaces'] = 0
```

```python
# 잘 바뀌었는지 확인
df.loc[[29045, 29046]].T
```

```python
df["booking_changes"].unique()
```

```python
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["booking_changes"].value_counts().sort_index()
```

**booking_changes**
- 일반적으로 21건의 예약 변경을 할 수 있을까?
- booking_changes가 10 초과인 값이 굉장히 적음
- 다른 데이터상 문제 없지만 컬럼만 봤을땐 이상하므로 10회 이상 요청 데이터는 삭제
    - AI 4기의 현업 경험이 있으신 분의 조언을 기반한 결정

```python
df = df[df['booking_changes'] < 11]
```

```python
# booking_changes 이상치 제거
df = df[df['booking_changes'] < 21]
```

```python
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["total_of_special_requests"].value_counts().sort_index()
```

**total_of_special_requests**
- 특별 요청이 많아지는 것을 이상치라 판단할 수 없음
    - 도메인 지식 기반 판단

```python
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df['previous_bookings_not_canceled'].value_counts().sort_index()
```

```python
df[df['previous_bookings_not_canceled'] > 60].T
```

**previous_bookings_not_canceled**
- 60개 이상인 값을 확인한 결과
    - 어른 1명이 city hotel 묶음
    - marget_segment와 distribution_channel: 예약의 방식을 보여주는 컬럼

    => 두 값 모두 Corporate
    - 나라 모두 PRT 동일

> 한 에이전시를 통해 출장 예약건에 대해 반복적 기록이라 판단 => 이상치 X

```python
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df['previous_cancellations'].value_counts().sort_index()
```

```python
df[df['previous_cancellations'] > 12].T
```

```python
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["days_in_waiting_list"].value_counts().sort_index()
```

```python
df[df['days_in_waiting_list'] > 300].T
```

```python
len(df[df['days_in_waiting_list'] > 0])
```

```python
831/len(df) * 100
```

**days_in_waiting_list**

- 가장 고민이 많았던 부분
- 특정 숙소가 맘에 들 경우, 예약 대기를 걸어놓을 수는 있을거 같은데, 수백일의 예약 대기가 의미가 있을까?
- 예약 대기일이 있는경우는 전체 데이터의 0.97%
- 결론: days_in_waiting_list의 상위 1% 데이터를 삭제한다

```python
# 상위 1%에 해당하는 값 계산
threshold = df['days_in_waiting_list'].quantile(0.99)
```

```python
# 상위 1% 값 제거
df = df[df['days_in_waiting_list'] <= threshold]
```

```python
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["lead_time"].value_counts().sort_index()
```

```python
np.sort(df["lead_time"].unique())
```

```python
df[df['lead_time'] > 365].T
```

```python
507/len(df) * 100
```

**lead_time**
- 예약 시점까지 2년 이상 기다린다는 것이 말이 될까?
- airbnb, agoda, Hilton호텔 등 많은 사이트들이 대개 1년의 예약을 열어둠
- 1년 이상인 데이터값 자체의 문제는 보이지 않으나, 일반적 상황으로 맞추기 위해 이상치라 판단하고 제거
- 이상치 역시 507건(전체 데이터의 약 0.5%)으로 데이터 전체의 품질에 영향을 미치지 않을 것으로 판단

```python
# lead_time 이상치 제거
df = df[df['lead_time'] < 366]
```

```python
# 전처리 후 최종 데이터 비율 - 실제 분석보고서에선 이런 부분 추가하지 않음
len(df)/119390 * 100
```

#### 그 외 이상치 의심 데이터>

**일반적으로 "여행"이라는 상황에서 잘못 되었다고 의심할 수 있는 데이터**
1. 예약 박수(stays_in_weekend_nights + stays_in_week_nights)가 전부 0
 - https://www.dayuse.com/s/portugal/porto?selectedAddress=Porto&checkinDate=2025-08-22
2. 사람(adults + children + babies)의 수 총합이 0인 데이터
3. 전 예약건수가 극도로 높은 값

```python
# 1. 예약 박수(stays_in_weekend_nights + stays_in_week_nights)가 전부 0
df[(df['stays_in_weekend_nights']==0) & (df['stays_in_week_nights']==0)]
```

```python
# 전체 데이터 중 해당 데이터의 양이 적으므로 삭제 결정
df = df[~((df['stays_in_weekend_nights']==0) & (df['stays_in_week_nights']==0))]
```

```python
# 2. 사람(adults + children + babies)의 수 총합이 0인 데이터 확인

df[(df['adults']==0) & (df['children']==0) & (df['babies']==0)]
```

```python
# 전체 데이터 중 해당 데이터의 양이 적으므로 삭제 결정
df = df[~((df['adults']==0) & (df['children']==0) & (df['babies']==0))]
```

```python
# 이전 예약건 수가 극도로 높은값 확인하기 위해 이전 예약건 확인

np.sort(df['previous_bookings_not_canceled'].unique())
```

```python
np.sort(df['previous_cancellations'].unique())
```

- 전 예약이 취소가 되었거나 취소가 되지 않았을 때, 데이터가 이상치 일까?

    - 회사에서 출장을 여행사 통해 한다면, 한 고객에 대해 반복적인 숙박, 취소가 이뤄지지 않는가?

```python
# 데이터 확인
df[df['previous_bookings_not_canceled'] > 69].T
```

```python
# 데이터 확인
df[df['previous_cancellations'] > 19].T
```

**결론**

1. 출장의 경우 한 고객의 요청으로 반복 예약 들어올 수 있다고 판단
    - 이전 예약이 극도로 큰 값이 있을 수 있다고 결정

2. 만약 신혼여행을, 대행사가 대신 예약을 걸어놓는다면 이전의 예약 취소가 빈번하게 적혀진 건 정말 오류일까?

> 해당 상황에 대한 명확하고 객관적인 근거가 없으므로 극단적인 이전 예약 수와 관련한 값은 이상치라 판단하지 않음

## 3. 데이터 시각화

### 1) 시각화 위한 데이터 탐색

```python
# 예약 취소 건수 확인
df['is_canceled'].value_counts()
```

```python
# 예약 상태 확인
df['reservation_status'].value_counts()
```

is_canceled==0와 reservation_status =='Check-out'의 데이터가 같은건지 확인 필요

```python
df[(df['is_canceled'] == 0) & (df['reservation_status'] =='Check-Out')]
```

**결론**

- is_canceled==0와 reservation_status =='Check-out'의 데이터가 같음
    - 취소하지 않은 예약건은 모두 reservation_status가 체크아웃!
- 예약이 취소되는 상황은 "예약 취소" + "No-show" 포함이 됨

```python
# 호텔별 취소 건수 비교
df.groupby(by='hotel')['is_canceled'].value_counts()
```

```python
# 호텔별 취소 건수 비율 비교
df.groupby(by='hotel')['is_canceled'].value_counts(normalize=True) * 100
```

=> City hotel 예약건의 수가 많고 취소도 많으며 취소 비율이 더 높다.

### 2) 시각화

```python
# 수치형 변수만 추출해서 전체 상관관계 히트맵 생성
numeric_df = df.select_dtypes(include="number")

# 상관행렬 계산
full_corr_matrix = numeric_df.corr()

# 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(full_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("수치형 변수 상관관계 히트맵")
plt.tight_layout()
plt.show()
```

=> days_in_waiting_list값은 0만 있으므로 상관도 계산 불가 (피어슨 상관계수의 식 - 표준편차로 나눠줘야 함!)

- 해당 변수 제외하고 다시 상관관계 히트맵 그리기

```python
# 히트맵 폰트 관련 이슈때문에 실행하는 셀
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False
```

```python
# 수치형 변수만 먼저 추출하고 컬럼 이름 확인
numeric_df = df.select_dtypes(include="number")
numeric_df.columns
```

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

#### 상관관계 해석

- is_canceled와 연관도가 있다고 의심할 수 있는 컬럼 (상대적으로 절댓값이 높은 값)
    - lead_time
    - arrival_date_day_of_year
        - arrival_date_day_of_year은 상대적 상관도는 높으나 의미있는 데이터는 아닐거라고 판단해 is_canceled와 따로 분석 실시하진 X
    - stays_in_weeknight
    - adults
        - 상관도는 높으나 어른의 예약건이 많아서 발생하는 일이라 판단해 따로 분석 실시하진 X
    - is_repeated_guest
    - booking_changes
    - required_car_parking_spaces
    - total_of_special_requests

- arrival_date_day_of_month와 arrival_date_day_of_year이 음의 상관관계를 보이는 수치이나, 따로 의미가 있다고 생각하긴 어려움
    - 같은 의미의 컬럼: stays_in_weekend_nights과 stays_in_week_nights

- adults와 arrival_date_day_of_year은 수치는 위 컬럼들과 비슷하지만 is_canceled와 맥락상 비슷

- 그 외 상관도가 높은 변수들
    - previous_bookings_not_canceled과 is_repeated_guest

    => 이전에 예약을 취소하지 않은 고객의 재방문률이 높은 편이다.

---

### 분석 방향
> is_canceled와 연관이 높은 컬럼들을 다루고, 취소에 영향을 미치는 요인이 뭔지 알아본다!

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

```python
# lead_time에 따른 취소율 시각화 - kde 플롯
plt.figure(figsize=(6, 4))
sns.kdeplot(data=df, x='lead_time', hue='is_canceled', fill=True)
plt.title("리드타임에 따른 취소율 시각화 - KDE 플롯")
plt.show()
```

```python
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x='lead_time', hue='is_canceled',
             bins=range(0, df['lead_time'].max()+30, 30),       # 0부터 최대값까지 30단위 bin 설정
             multiple='dodge',                                  # multiple='dodge': 막대가 겹치지 않고 나란히 배치,
             shrink=0.8)                                        # shrink: 막대 폭 줄여서 보기 좋게 표현

plt.title("리드타임과 취소 상황 비교 막대 그래프")
plt.xlabel("Lead Time")
plt.ylabel("전체 수")
plt.legend(title="<취소 현황>", labels=["Canceled", "Not Canceled"])
plt.grid(True, axis='y', linestyle='--', alpha=0.3)
plt.show()
```

```python
# stays_in_weeknight 시각화

# 취소 여부에 따른 stays_in_week_nights의 평균 계산
mean_weeknight = df.groupby("is_canceled")["stays_in_week_nights"].mean().reset_index()

# 막대그래프 시각화
plt.figure(figsize=(4, 3))
sns.barplot(x="is_canceled", y="stays_in_week_nights", data=mean_weeknight)
plt.xlabel("취소 여부 (0: No, 1: Yes)")
plt.ylabel("주중 숙박일 평균")
plt.title("취소 여부에 따른 주중 숙박 평균")
plt.show()
```

```python
# stays_in_week_nights별 예약 취소율 계산
cancel_rate_by_stay = df.groupby("stays_in_week_nights")["is_canceled"].mean().reset_index()

# 막대그래프 시각화
plt.figure(figsize=(10, 4))
sns.barplot(data=cancel_rate_by_stay, x="stays_in_week_nights", y="is_canceled", color="salmon")
plt.xlabel("주중 숙박일")
plt.ylabel("취소율")
plt.title("주중 숙박일에 따른 취소율")
plt.xticks(rotation=45)
plt.ylim(0, 1)
plt.grid(True, axis='y', linestyle='--', alpha=0.3)
plt.show()
```

**stays_in_week_nights**

- 한 달 미만(< 30): 숙박일이 길 수록 취소율이 높아지는 경향성이 있다.

    => 하루 이틀 정도 묵는 사람들보다 좀 더 오래 머무를 계획을 가진 고객이 예약을 더 많이 취소하는 경향이 있다고 볼 수 있다.

```python
# is_repeated_guest 시각화

# 그룹별 평균 취소율
repeat_cancel = df.groupby('is_repeated_guest')['is_canceled'].mean().reset_index()
repeat_cancel['is_repeated_guest'] = repeat_cancel['is_repeated_guest'].map({0: '신규 고객', 1: '재방문 고객'})
repeat_cancel.columns = ['고객 유형', '평균 취소율']
```

```python
# 시각화
plt.figure(figsize=(4, 4))
sns.barplot(data=repeat_cancel, x='고객 유형', y='평균 취소율', color='teal')
plt.title('재방문 여부에 따른 평균 예약 취소율')
plt.ylim(0, 0.3)
plt.grid(True, axis='y', linestyle='--', alpha=0.3)
plt.show()
```

```python
# required_car_parking_spaces

# 주차 공간 수별 예약 취소율 계산
cancel_rate_by_parking = df.groupby("required_car_parking_spaces")["is_canceled"].mean().reset_index()

# 막대그래프 시각화
plt.figure(figsize=(5, 3))
sns.barplot(data=cancel_rate_by_parking, x="required_car_parking_spaces", y="is_canceled", color="skyblue")
plt.xlabel("주차 공간 수")
plt.ylabel("취소율")
plt.title("주차 공간 요구에 따른 취소율")
plt.ylim(0, 0.35)
plt.grid(True, axis='y', linestyle='--', alpha=0.3)
plt.show()
```

**required_car_parking_spaces**

- 주차 공간을 요청하지 않은 고객의 취소율은 높다.

> 근데 과연, 주차를 요청한 경우의 예약이 많을것인가?

```python
df['required_car_parking_spaces'].value_counts()
```

```python
# 비율 확인 - 이런건 실제 보고에는 포함하지 X

(len(df) - 77122)/len(df) * 100
```

**required_car_parking_spaces**

- 주차 공간을 요청한 예약은 전체의 8%

- 전체 예약건 중, 주차 공간을 요청하는 것은 매우 적다.

- 하지만, 전체적인 트렌드를 읽어주는 것은 의미있을 듯

    - 주차 공간을 요청한 고객들은 예약을 100% 유지한다.

        => 고객들이 차량을 이용할 만큼 강한 방문 의지가 있는 경우라고 해석할 수 있음

```python
# booking_changes 시각화

# 그룹별 평균 취소율 계산
booking_cancel = df.groupby('booking_changes')['is_canceled'].mean().reset_index()
booking_cancel.columns = ['예약 변경 횟수', '평균 취소율']
```

```python
# 시각화
plt.figure(figsize=(8, 5))
sns.barplot(data=booking_cancel, x='예약 변경 횟수', y='평균 취소율', color='#FE8330')
plt.title('예약 변경 횟수에 따른 평균 예약 취소율')
plt.ylim(0, 0.35)
plt.show()
```

```python
# total_of_special_requests 시각화

# 그룹별 평균 취소율 계산 - 여기서부턴 따로 변수 지정해 계산
special_cancel = df.groupby('total_of_special_requests')['is_canceled'].mean().reset_index()
special_cancel.columns = ['요청 수', '평균 취소율']
```

```python
# 시각화
plt.figure(figsize=(5, 3))
sns.barplot(data=special_cancel,x='요청 수', y='평균 취소율', color='skyblue')
plt.title('특별 요청 수에 따른 평균 예약 취소율')
plt.ylim(0, 0.4)
plt.show()
```

## 4. 결론

### 변수별 취소율 분석 요약

**1. Lead Time (예약 후 도착까지 기간)**
- 리드타임이 길수록 예약 취소율이 뚜렷하게 증가함

- 특히 300일 이상 리드타임 구간은 취소율이 50% 이상으로 매우 높음

    ⇒ 일찍 예약할수록 변동 가능성이 크기 때문으로 해석 가능

**2. stays_in_week_nights (주중 숙박 일 수)**

- 한 달 미만(< 30): 숙박일이 길 수록 취소율이 높아지는 경향성이 있다.

    => 하루 이틀 정도 묵는 사람들보다 좀 더 오래 머무를 계획을 가진 고객이 예약을 더 많이 취소하는 경향이 있다고 볼 수 있다.

**3. is_repeated_guest (재방문 여부)**
- **신규 고객(0)**의 취소율이 약 37%
- **재방문 고객(1)**의 취소율은 10% 미만

    ⇒ 재방문 고객은 호텔에 대한 신뢰가 있어 예약을 잘 지킨다고 볼 수 있음

**4. booking_changes (예약 변경 횟수)**
- 전반적으로 변경 횟수가 0보다 많을수록 취소율이 상승한다고 볼 수는 있음
     - 예약 변경 횟수가 클수록 데이터 수가 차이나기 때문에 그래프만으로는 한계

**5. required_car_parking_spaces**

- 주차 공간을 요청한 고객들은 예약을 100% 유지한다.
- 주차 공간을 요청하지 않은 고객들은 약 35%의 예약 취소율을 보인다.

    => 고객들이 차량을 이용할 만큼 강한 방문 의지가 있는 경우라고 해석할 수 있음

**6. total_of_special_requests (특별 요청 수)**
- 요청이 많을수록 취소율은 낮아짐
- 요청 0건: 높은 취소율
- 요청 1~3건: 급격히 낮아짐

    ⇒ 의도적으로 요구사항을 명확히 한 고객은 예약을 유지할 확률이 높음

---

## 5. 인사이트 (Action Plan)

## 1. Lead Time이 길수록 취소율 증가

=> 리드타임(예약 후 도착까지 기간)이 길수록 고객의 일정 변경 가능성도 높아지며, 300일 이상인 경우 취소율이 50%를 초과함

**💡 Action Plan**

- 장기 예약에 대해 더 강력한 보증 정책 적용

    => 일정 이상 리드타임 고객에게 선결제, 부분 환불 조건 등 적용 고려

- 예약 리마인드 이메일/문자 자동화

    =>30일 전, 7일 전, 1일 전 등 고객 일정 재확인을 유도

- 예치금 기반 예약 정책 검토

    => 취소 방지를 위한 유연한 예치금 정책 도입

## 2. 주중 장기 숙박일 수록 예약 취소율 증가

=> 한달 미만의 예약건 기준, 장기 예약일수록 예약취소율 증가

**💡 Action Plan**

- 사전 리마인드 & 재확인 메시지 발송

    => stays_in_week_nights ≥ 3 이상 고객이 체크인 하기 일주일 전 시점에 리마인드 & 예약 재확인 팝업을 띄움

- 장기 투숙 고객 대상 사전 결제 유도

    => 주중 3일 이상 예약 고객에게 할인 또는 혜택 제공

- 취소 가능 정책의 차등화

    => 장기 숙박 고객에 대해 더 엄격한 취소 정책 적용. 단, 명확히 고지하고 고객 불만 없도록 함

- 예약 시점에서의 리스크 알림

    => 3박 이상 고객에게 “장기 투숙 예약 시 사전 결제를 추천합니다” 등의 알림 문구 삽입하거나 UI&UX에서 자연스럽게 변경 및 취소 위험성을 인지하게 유도

## 3. 재방문 고객은 확실히 충성도 높고 취소율 낮음
=> 신규 고객의 취소율은 37%, 재방문 고객은 10% 이하 → 매우 안정적이고 충성도 높음

**💡 Action Plan**

- 재방문 고객 대상 특별 혜택 정책 강화

    => 할인, 우선 배정, 얼리체크인/레이트체크아웃 제공

- 충성고객 리텐션 프로그램 운영

    => 스탬프 적립, 멤버십 포인트 혹은 멤버쉽 등급제 도입 등

    - 예) 멤버쉽 등급별로 할인율 차등 지급하며 이 사실 광고에 유입

- 재방문 여부를 리스크 모델의 중요 변수로 활용

    => 신규 고객 위주의 과도한 예약 확대로 인한 리스크 방지

## 4. 주차 공간 요청한 고객은 취소율이 매우 낮다

**💡 Action Plan**

=> 주차 공간 요청 고객은 100% 예약 유지, 요청하지 않았을 경우 35%의 취소율을 보이기 때문에 차량을 이용하는 고객일수록 방문 확률이 높음

- 예약 리스크 예측에 반영 (취소 예측 모델 개선)

    => required_car_parking_spaces == 0인 고객에게는 취소 리스크 점수를 높게 부여하여 추후 관련 모델링에서 사용할 변수로 지정하기 위해 DB에 따로 관리

- 사전 결제 혜택 강화 대상 지정

    - 주차 공간 요청하지 않은 고객에게는:

        “사전 결제 시 추가 할인 or 조식 무료 제공” 등의 유인책 제공

    - 주차 공간 요청 고객은 이미 확률이 높으므로 굳이 인센티브를 제공하지 않음

- 주차 공간 요청 유도

    - 예약 시, “필요 시 주차 공간을 미리 신청해주세요” 라는 UI&UX 메시지와 함께 옵션을 자연스럽게 강조

- 주차 공간 수요 예측 및 운영 계획 수립

    - 차량을 동반하는 고객은 방문 확률이 높기 때문에, 이 데이터를 바탕으로 실제 투숙률 기반 주차 공간 확보하고 주차 공간 운영을 최적화 함

- 고객 마케팅 활용

    - 차량 이용 고객은 지역 거주자일 가능성 낮고, 장거리 이동 고객일 가능성이 높음

    - 따라서 지역 기반 타겟팅 시

        - 주차 요청 고객 → 관광 패키지 제안

        - 주차 미요청 고객 → 지역 주민 전용 이벤트, 단기 프로모션 제안

## 5. 특별 요청을 많이 하는 고객은 예약을 잘 지킨다
=> 특별 요청이 0건인 고객은 취소율이 높은 반면, 1건 이상 요청한 고객은 신뢰도 높은 패턴을 보임

**💡 Action Plan**

- 고객의 요청을 적극 유도하는 UI&UX 개선

    => 예약 시점에 "요청사항이 있으신가요?"와 같은 질문 배치

- 요청 입력 유도 고객에게 리마인드 제공

    => "트윈 침대, 고층, 베이비 침대 요청을 준비 중입니다" 같은 메시지로 체류 의사 고취

- 요청 정보 기반 개인화 마케팅

    => 특정 요청을 자주 하는 고객군 대상 맞춤형 혜택 제공
    - 예) 아이와 자주 여행한 과거 기록이 있는 여행자의 경우 가족단위가 가기 좋은 호텔의 프로모션 발생시 팝업 더 자주 띄우기

---

### 추가 분석 Point

1. 특정 변수들에 따른 분석 진행
    - 예약된 어른의 수와 아이 또는 아기의 수를 조합
        - 가족여행
        - 연인(부부만)의 여행
    - 기존에 호텔에 의해 변경된 예약의 경우 취소를 할까?
        -  reserved_room_type과 assigned_room_type 분석
    - 호텔별 예약 취소 비교
        - Resort Hotel과 City Hotel의 예약 취소율은 동일할지 분석
        - City hotel의 취소율이 더 높은걸 가지고 추가 분석할 수 있음
            - City Hotel 예약건 중 상관도가 높은 다른 변수는 무엇인가?
            => City Hotel의 예약 취소 사유는 무엇인가?
            - 해당 변수들에 대한 기술통계 및 인사이트 내기

2. 충성 고객 관리 Deepdive

    - 반복해 오는 고객들의 데이터만 가지고 추가 분석
        - 단골 고객의 예약건 중 상관도가 높은 다른 변수는 무엇인가?
        => 단골 고객의 예약 취소 사유는 무엇인가?
        - 해당 변수들에 대한 기술통계 및 인사이트 내기

3. 특정 기간에 대한 Deepdive

    - 월, week의 데이터만 가지고 추가 분석
        - 특정 예약 기간에 대한 트렌드는 없는가?
        - 기술통계 및 인사이트 내기

4. 특정 국가에 대한 Deepdive

    - 국가 데이터만 가지고 추가 분석
        - 취소율이 높은 국가(포르투갈)의 데이터중 상관도가 높은 다른 변수는 무엇인가?
        - 포르투갈 고객의 예약 취소율이 높은 이유를 설명할만한 다른 트렌드는 없을까?
        - 해당 변수들에 대한 기술통계 및 인사이트 내기

```python

```
