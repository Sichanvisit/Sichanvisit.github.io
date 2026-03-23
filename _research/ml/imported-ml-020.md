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

```python colab={"base_uri": "https://localhost:8080/"} id="UF7Qop1zq5NB" outputId="ee37c0db-6915-4fbe-e684-3b33f2667004" executionInfo={"status": "ok", "timestamp": 1755651666672, "user_tz": -540, "elapsed": 45398, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
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

<!-- #region id="DZF4xEgAa_SS" -->
# 🏨 데이터 설명

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
<!-- #endregion -->

<!-- #region id="r8ufWsp-bxpr" -->
# 1. 데이터 불러오고 확인하기
<!-- #endregion -->

```python id="MAig-3QwZiyv" executionInfo={"status": "ok", "timestamp": 1755651668266, "user_tz": -540, "elapsed": 1588, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 라이브러리 임포트
import pandas as pd
import numpy as np
import seaborn as sns
```

```python colab={"base_uri": "https://localhost:8080/"} id="0A7pZwe-dSEF" executionInfo={"status": "ok", "timestamp": 1755651688381, "user_tz": -540, "elapsed": 20121, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ba28208f-c70e-4033-c7cf-40c3c1db44bb"
# 드라이브 마운트 코드
from google.colab import drive
drive.mount('/content/drive/')
```

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="J1m3vJelcZB5" executionInfo={"status": "ok", "timestamp": 1755651693330, "user_tz": -540, "elapsed": 4953, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f37aa8c8-26c7-4dfa-ccdf-0defd801fc90"
df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 4기/공유폴더/Data/hotel_data_modified.csv')
df
```

```python colab={"base_uri": "https://localhost:8080/"} id="cwzf0emYcb1e" executionInfo={"status": "ok", "timestamp": 1755651693463, "user_tz": -540, "elapsed": 81, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="14df42bb-5e40-414a-8f04-eb297f5d3ed1"
df.info()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 993} id="VVZUUq_ndfQB" executionInfo={"status": "ok", "timestamp": 1755651693499, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7440e445-429a-4390-c407-c8c4d28ad5f5"
# Data type 확인하는 추가 코드
df.dtypes
```

```python colab={"base_uri": "https://localhost:8080/", "height": 320} id="VjTAE9mncnrc" executionInfo={"status": "ok", "timestamp": 1755651693724, "user_tz": -540, "elapsed": 223, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c7a3e2c8-7868-4d56-a638-994f540e558d"
df.describe()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 461} id="kbNLIur2dXRj" executionInfo={"status": "ok", "timestamp": 1755651693964, "user_tz": -540, "elapsed": 234, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="14f5a2a1-f4e5-4c30-c89f-fa4344a0df9a"
#  include=all: 범주형도 포함
df.describe(include="all")
```

```python colab={"base_uri": "https://localhost:8080/", "height": 645} id="E4gNaPyKAg1u" executionInfo={"status": "ok", "timestamp": 1755651694115, "user_tz": -540, "elapsed": 146, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e987b348-38c1-4769-b584-2ebc47df472d"
# 컬럼 편하게 보기 - 전치행렬 변환
df.describe().T
```

<!-- #region id="DPYU0SrTdop8" -->
**<데이터 1차 확인 결과>**
- 전체 119390행 29열의 구조
- company 열에 결측치가 많음 (agent도 일부 결측치 확인)
- 8월에 여행을 많이 함 => (arrival_date_month의 top 참조)
--------------------------------------

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
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 506} id="Kz57k2tRoU57" executionInfo={"status": "ok", "timestamp": 1755651698330, "user_tz": -540, "elapsed": 4220, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fad94d14-0272-437c-d209-10f61155db33"
plt.figure(figsize=(13,3))
sns.heatmap(df.isnull(),  yticklabels=False, cbar=False)
plt.title("호텔 데이터 결측치 시각화")
#plt.xticks(rotation=45)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 209} id="4A5L8lFiwEoe" executionInfo={"status": "ok", "timestamp": 1755651698475, "user_tz": -540, "elapsed": 144, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f75bb27a-f517-4177-be69-ef0776459ef1"
# 결측치 비율 확인 - 0인 컬럼이 많아 0보다 큰 값만 보기로 결정
(df.isnull().sum()/len(df) * 100)[lambda x: x > 0].sort_values(ascending=False)
```

```python colab={"base_uri": "https://localhost:8080/"} id="cxYsiuz9wG3U" executionInfo={"status": "ok", "timestamp": 1755651698551, "user_tz": -540, "elapsed": 72, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d0602094-68b5-490c-9572-2002294efa8c"
df['children'].unique()
```

```python colab={"base_uri": "https://localhost:8080/"} id="iL6klPAbwOig" executionInfo={"status": "ok", "timestamp": 1755651698577, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="12ce4665-bfa9-4722-faf9-5edf8cf27692"
print(df['children'].isnull().sum())
```

```python colab={"base_uri": "https://localhost:8080/"} id="DUXKiFjOwW7u" executionInfo={"status": "ok", "timestamp": 1755651698593, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ef7caf00-52ad-4002-d2a2-36b57c2025b5"
print(df['country'].isnull().sum())
```

<!-- #region id="FX0X4lxEwd1R" -->
**결론**

- company와 agent는 결측치의 비율이 높아 열 삭제 결정

    => agent로 따로 할 분석 주제를 지정하지 않았기 때문에 삭제하는 방향으로 결정
- children의 결측치는 아래에서 중복행 삭제 후 다시 확인한 뒤, 결측치는 다른 값으로 넣어줄 예정
- country 역시 중복행 삭제 후 다시 확인한 뒤 방향성 결정

<!-- #endregion -->

<!-- #region id="nn-7tnXLnyqp" -->
-------------------------------------
# 2. 데이터 전처리
<!-- #endregion -->

<!-- #region id="kLdJ54yXbbVf" -->
### (1) 중복값
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="MFmEfGTHlfAo" executionInfo={"status": "ok", "timestamp": 1755651698608, "user_tz": -540, "elapsed": 13, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="be018e20-d40a-4443-9d12-dee69db0bc07"
# 중복행 확인
print(df.duplicated().sum())
```

```python colab={"base_uri": "https://localhost:8080/"} id="U2YfwyxAw_fa" executionInfo={"status": "ok", "timestamp": 1755651698629, "user_tz": -540, "elapsed": 18, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ec73b50c-9b0b-4610-97c1-8d4bd2100c66"
# 중복값 비율 계산 - 이런건 분석 보고서에는 포함하지 않음
33130/len(df) * 100
```

```python id="vex3B1uWxB1_" executionInfo={"status": "ok", "timestamp": 1755651698753, "user_tz": -540, "elapsed": 121, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 중복 제거
df.drop_duplicates(inplace=True)
```

```python colab={"base_uri": "https://localhost:8080/"} id="QI5qKCsMxKRH" executionInfo={"status": "ok", "timestamp": 1755651698759, "user_tz": -540, "elapsed": 126, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3ba48b8a-f83d-4772-e690-1ac6727cd45c"
# 중복 제거 확인
df.shape
```

<!-- #region id="bSa3gcY9xXY4" -->
### (2) 결측치
<!-- #endregion -->

```python id="kxDW3S_exaj4" executionInfo={"status": "ok", "timestamp": 1755651698766, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 결측치가 많은 컬럼 제거
df.drop(columns=['company', 'agent'], axis=1, inplace=True)
```

```python colab={"base_uri": "https://localhost:8080/"} id="TUqfuqFTxxoe" executionInfo={"status": "ok", "timestamp": 1755651698799, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="953a161d-6d37-4115-d9c9-ac4bac0bd6eb"
# 컬럼 삭제 되었는지 확인
df.columns
```

```python colab={"base_uri": "https://localhost:8080/"} id="EeojXYYZxNss" executionInfo={"status": "ok", "timestamp": 1755651698815, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="774f4923-d1dd-4f45-b032-cd1fcc28ff81"
print(df['children'].isnull().sum())
```

```python colab={"base_uri": "https://localhost:8080/"} id="tQjweJSlxToV" executionInfo={"status": "ok", "timestamp": 1755651698830, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f61490d2-4ac1-46ea-b376-237649ca0615"
print(df['country'].isnull().sum())
```

```python colab={"base_uri": "https://localhost:8080/"} id="_twscvEQ2F3v" executionInfo={"status": "ok", "timestamp": 1755651698881, "user_tz": -540, "elapsed": 49, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="df0837d7-0473-471e-d864-b7850db5ed82"
# country열의 결측치 비율 계산
451/len(df) * 100
```

```python colab={"base_uri": "https://localhost:8080/", "height": 272} id="3XwpUFFI3I2B" executionInfo={"status": "ok", "timestamp": 1755651698891, "user_tz": -540, "elapsed": 7, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3e4f3461-55b1-40bf-b6b3-6bd30a5006e2"
df['children'].value_counts()
```

```python id="sf2jTGdo2CUY" executionInfo={"status": "ok", "timestamp": 1755651698896, "user_tz": -540, "elapsed": 7, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# children열 결측치 최빈값으로 채우기
df["children"] = df["children"].fillna(df["children"].mode()[0])
```

```python colab={"base_uri": "https://localhost:8080/", "height": 930} id="wPiZEQ6O82fD" executionInfo={"status": "ok", "timestamp": 1755651698968, "user_tz": -540, "elapsed": 63, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="34b77c98-85b9-4d22-c0d9-1a58e5a81924"
# 결측치 행 제거 - company
df.dropna(inplace=True)
df.isnull().sum()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="8MJ8E2le9nHv" executionInfo={"status": "ok", "timestamp": 1755651699010, "user_tz": -540, "elapsed": 50, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5e6550fa-db52-4c8c-a430-31f5f2677574"
# adults가 0인데 children 또는 babies가 1명 이상인 경우 필터링
df[(df['adults'] == 0) & ((df['children'] > 0) | (df['babies'] > 0))]
```

```python colab={"base_uri": "https://localhost:8080/"} id="siQhZB8B9o5W" executionInfo={"status": "ok", "timestamp": 1755651699014, "user_tz": -540, "elapsed": 47, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="888407a0-a99f-4ac1-9852-3cf00676f74b"
# 아이만 있고 어른이 없는 예약건 전체 비율 확인
(len(df[(df['adults'] == 0) & ((df['children'] > 0) | (df['babies'] > 0))]) / len(df)) * 100
```

<!-- #region id="Rn23LRN79skF" -->
=> 어른의 수가 0명일 때, 어린이나 아기가 포함되는 여행은 존재하지 않음

- 법적인 문제 발생
- 대부분의 호텔은 적어도 성인 1명당 어린아이 투숙을 허용
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="nWQd17OX9udc" executionInfo={"status": "ok", "timestamp": 1755651699037, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2bec2371-670a-4636-cea8-0218832fc15d"
# 어른 데이터가 0으로 잘못 입력 혹은 결측치로 판단하고 해당 값 삭제
df = df[~((df['adults'] == 0) & ((df['children'] > 0) | (df['babies'] > 0)))]
len(df)
```

```python colab={"base_uri": "https://localhost:8080/"} id="acAYHZl89LFn" executionInfo={"status": "ok", "timestamp": 1755651699038, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3193c985-19c3-48bd-87c9-4dcbfba2d17e"
# 결측 제거 후 남은 데이터 비율 확인 - 이런건 분석 보고서에는 포함하지 않음
85619/86287 * 100
```

<!-- #region id="O9yIUB1N9Fsv" -->
### (3) 이상치
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 320} id="60ncH_ry2jiy" executionInfo={"status": "ok", "timestamp": 1755651699052, "user_tz": -540, "elapsed": 18, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="da5a6a1b-0e12-4faf-abfc-78d8534266e3"
# 최대값이 독특해 보이는 컬럼만 확인
df[["adults", "booking_changes", "children", "babies","required_car_parking_spaces", "booking_changes", "days_in_waiting_list", "total_of_special_requests", "previous_bookings_not_canceled", "previous_cancellations"]].describe()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 554} id="o0bUXXU8-iPe" executionInfo={"status": "ok", "timestamp": 1755651699065, "user_tz": -540, "elapsed": 11, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="42e940b1-2814-4348-b9d6-900c045c6349"
df["adults"].value_counts().sort_index()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 896} id="VPOPq1xA-_Tl" executionInfo={"status": "ok", "timestamp": 1755651699097, "user_tz": -540, "elapsed": 25, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="72f2e99a-da0d-457d-f137-b5d9f9265305"
df[df['adults'] > 30].T
```

<!-- #region id="OyZSVoq9O4t0" -->
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
<!-- #endregion -->

```python id="WkFun35nSdDn" executionInfo={"status": "ok", "timestamp": 1755651699202, "user_tz": -540, "elapsed": 101, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 어른의 수가 30 미만인 데이터만 남기고 삭제
df = df[df["adults"] < 30]
```

```python colab={"base_uri": "https://localhost:8080/", "height": 272} id="hfTmlnyL_EY6" executionInfo={"status": "ok", "timestamp": 1755651699203, "user_tz": -540, "elapsed": 98, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6ff7aace-3c35-4e64-dd4e-60b9b680bf64"
df["babies"].value_counts().sort_index()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 896} id="e42c7QHw_EWY" executionInfo={"status": "ok", "timestamp": 1755651699204, "user_tz": -540, "elapsed": 15, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9e1a4287-64e7-4794-b2ab-729ab9efa3c0"
df[df['babies'] > 8].T
```

<!-- #region id="11F_OtZoSgbf" -->
**babies**

- 어른 한 명당 아이가 여러명인 것은 이상한 데이터라고 판단
- 아이가 9명과 10명인 경우 오류 데이터라고 생각해 최빈값으로 대체

 - babies 데이터는 unique가 각 0, 1, 2, 9, 10이며, 9값 부터 일반적인 범주로 볼 수 없다고 판단
 - 이 부분은 계속 고민이 필요한 영역일 수도 있으나, unique의 독특한 분포와 데이터의 전체 수를 기반해 판단한 결정
<!-- #endregion -->

```python id="tpV7A7J1Swoh" executionInfo={"status": "ok", "timestamp": 1755651699205, "user_tz": -540, "elapsed": 6, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# babies 이상치 최빈값으로 채우기
most_common_babies = df['babies'].mode()[0]
df.loc[df['babies'] > 8, 'babies'] = most_common_babies
```

```python colab={"base_uri": "https://localhost:8080/", "height": 896} id="AHPmA82FTlMg" executionInfo={"status": "ok", "timestamp": 1755651699235, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ab7c100b-42ff-4411-a770-66326f6baad1"
# 잘 바뀌었는지 확인
df.loc[[46619, 7000]].T
```

```python colab={"base_uri": "https://localhost:8080/", "height": 272} id="5OeHmkl4_ETl" executionInfo={"status": "ok", "timestamp": 1755651699242, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="8c79a696-b332-4968-de27-c1a87558f6e2"
df["required_car_parking_spaces"].value_counts().sort_index()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 896} id="eMboFjGJRRlU" executionInfo={"status": "ok", "timestamp": 1755651699272, "user_tz": -540, "elapsed": 28, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="512bc694-e8b7-4710-9f5d-202cc8ffb2d2"
df[df['required_car_parking_spaces'] > 7].T
```

<!-- #region id="F5SvPI06_Bc0" -->
**required_car_parking_spaces**
- 어른 2명의 여행에 주차공간 8은 입력을 잘못한 것으로 판단
- 0으로 대체
<!-- #endregion -->

```python id="6_tkFp5ARbti" executionInfo={"status": "ok", "timestamp": 1755651699279, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 주차 공간 8인 값 0으로 바꾸기
df.loc[df['required_car_parking_spaces'] == 8, 'required_car_parking_spaces'] = 0
```

```python colab={"base_uri": "https://localhost:8080/", "height": 896} id="LPf26nb7UwEx" executionInfo={"status": "ok", "timestamp": 1755651699367, "user_tz": -540, "elapsed": 83, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b8a95baa-b997-4da0-b62d-97d28b5f4e30"
# 잘 바뀌었는지 확인
df.loc[[29045, 29046]].T
```

```python colab={"base_uri": "https://localhost:8080/"} id="7gND20JZ93T8" executionInfo={"status": "ok", "timestamp": 1755651699393, "user_tz": -540, "elapsed": 31, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5e7cf0db-c62b-4c95-9535-9f65b0d38fc8"
df["booking_changes"].unique()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 774} id="0EdrzeW2-dB-" executionInfo={"status": "ok", "timestamp": 1755651699409, "user_tz": -540, "elapsed": 10, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3cd703c4-08cb-4726-c686-6cc3e8803ecd"
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["booking_changes"].value_counts().sort_index()
```

<!-- #region id="ietNQrQnzCGn" -->
**booking_changes**
- 일반적으로 21건의 예약 변경을 할 수 있을까?
- booking_changes가 10 초과인 값이 굉장히 적음
- 다른 데이터상 문제 없지만 컬럼만 봤을땐 이상하므로 10회 이상 요청 데이터는 삭제
    - AI 4기의 현업 경험이 있으신 분의 조언을 기반한 결정
<!-- #endregion -->

```python id="3XptjnFozb8n" executionInfo={"status": "ok", "timestamp": 1755651699427, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
df = df[df['booking_changes'] < 11]
```

```python id="ZuF0mDJ1R7rr" executionInfo={"status": "ok", "timestamp": 1755651699436, "user_tz": -540, "elapsed": 13, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# booking_changes 이상치 제거
df = df[df['booking_changes'] < 21]
```

```python colab={"base_uri": "https://localhost:8080/", "height": 303} id="N7GBp99uVSsP" executionInfo={"status": "ok", "timestamp": 1755651699523, "user_tz": -540, "elapsed": 90, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7f525426-bfd6-4ba8-c657-275c5922dfcf"
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["total_of_special_requests"].value_counts().sort_index()
```

<!-- #region id="7r18wZQfYdEE" -->
**total_of_special_requests**
- 특별 요청이 많아지는 것을 이상치라 판단할 수 없음
    - 도메인 지식 기반 판단
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 489} id="AfLTeAI6Yc0m" executionInfo={"status": "ok", "timestamp": 1755651699524, "user_tz": -540, "elapsed": 10, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="97c67d0a-fffd-4c49-922a-2fc6ccbc1817"
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df['previous_bookings_not_canceled'].value_counts().sort_index()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 950} id="jguSB9LYVbeE" executionInfo={"status": "ok", "timestamp": 1755651699548, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ff44aa74-6bd1-4cd7-e327-3a7ddd996725"
df[df['previous_bookings_not_canceled'] > 60].T
```

<!-- #region id="Yp9AOBPXZcms" -->
**previous_bookings_not_canceled**
- 60개 이상인 값을 확인한 결과
    - 어른 1명이 city hotel 묶음
    - marget_segment와 distribution_channel: 예약의 방식을 보여주는 컬럼

    => 두 값 모두 Corporate
    - 나라 모두 PRT 동일

> 한 에이전시를 통해 출장 예약건에 대해 반복적 기록이라 판단 => 이상치 X

<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 585} executionInfo={"status": "ok", "timestamp": 1755651699551, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a0da1cc4-f4d9-46de-8169-2043f12c3e67" id="3ECk5Fi9aIEf"
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df['previous_cancellations'].value_counts().sort_index()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 965} executionInfo={"status": "ok", "timestamp": 1755651699574, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4647d102-3d5f-4323-a854-498f4de79263" id="xJbk0hB0aIEh"
df[df['previous_cancellations'] > 12].T
```

```python colab={"base_uri": "https://localhost:8080/", "height": 489} id="JR47ye88YtgZ" executionInfo={"status": "ok", "timestamp": 1755651699575, "user_tz": -540, "elapsed": 15, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d7e6b826-2cec-47da-ec20-f79ec252ecb4"
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["days_in_waiting_list"].value_counts().sort_index()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 950} id="iiTyunnWfmch" executionInfo={"status": "ok", "timestamp": 1755651699585, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="89b03cb1-abd9-4aa7-e9ca-82f5489dd77a"
df[df['days_in_waiting_list'] > 300].T
```

```python colab={"base_uri": "https://localhost:8080/"} id="ff-2Ng-WVWB5" executionInfo={"status": "ok", "timestamp": 1755651699638, "user_tz": -540, "elapsed": 51, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bb241e63-27ba-4891-8e64-8ee4a05618c6"
len(df[df['days_in_waiting_list'] > 0])
```

```python colab={"base_uri": "https://localhost:8080/"} id="BadwmwZgV5cC" executionInfo={"status": "ok", "timestamp": 1755651699649, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="8e8dba7a-f71c-4f53-d362-cf23916d75c5"
831/len(df) * 100
```

<!-- #region id="BSQv9JpqfYED" -->
**days_in_waiting_list**

- 가장 고민이 많았던 부분
- 특정 숙소가 맘에 들 경우, 예약 대기를 걸어놓을 수는 있을거 같은데, 수백일의 예약 대기가 의미가 있을까?
- 예약 대기일이 있는경우는 전체 데이터의 0.97%
- 결론: days_in_waiting_list의 상위 1% 데이터를 삭제한다
<!-- #endregion -->

```python id="SiTemp4OYtdI" executionInfo={"status": "ok", "timestamp": 1755651699662, "user_tz": -540, "elapsed": 11, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 상위 1%에 해당하는 값 계산
threshold = df['days_in_waiting_list'].quantile(0.99)
```

```python id="5QxVKNWWgIDY" executionInfo={"status": "ok", "timestamp": 1755651699664, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 상위 1% 값 제거
df = df[df['days_in_waiting_list'] <= threshold]
```

```python colab={"base_uri": "https://localhost:8080/", "height": 489} id="iKghM6uyrVCz" executionInfo={"status": "ok", "timestamp": 1755651699704, "user_tz": -540, "elapsed": 45, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="814f6389-4392-4f74-b478-5ab0a7510801"
# 빈도수 기준으로 정렬된 고유값과 개수 확인
df["lead_time"].value_counts().sort_index()
```

```python colab={"base_uri": "https://localhost:8080/"} id="zzH_Ql2frd3Y" executionInfo={"status": "ok", "timestamp": 1755651699705, "user_tz": -540, "elapsed": 36, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b96577dc-d9e7-48d2-f64c-6e1f89a7521f"
np.sort(df["lead_time"].unique())
```

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="43bYYRxvrorj" executionInfo={"status": "ok", "timestamp": 1755651699721, "user_tz": -540, "elapsed": 20, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6fe57de7-0699-4dba-bf48-dc04f0a64dea"
df[df['lead_time'] > 365].T
```

```python colab={"base_uri": "https://localhost:8080/"} id="5pZSE9wluIIt" executionInfo={"status": "ok", "timestamp": 1755651699794, "user_tz": -540, "elapsed": 71, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9258b7e4-7995-453c-f393-21a3585b8cdd"
507/len(df) * 100
```

<!-- #region id="dF0d8XtrrwnT" -->
**lead_time**
- 예약 시점까지 2년 이상 기다린다는 것이 말이 될까?
- airbnb, agoda, Hilton호텔 등 많은 사이트들이 대개 1년의 예약을 열어둠
- 1년 이상인 데이터값 자체의 문제는 보이지 않으나, 일반적 상황으로 맞추기 위해 이상치라 판단하고 제거
- 이상치 역시 507건(전체 데이터의 약 0.5%)으로 데이터 전체의 품질에 영향을 미치지 않을 것으로 판단

<!-- #endregion -->

```python id="vqBPR7HTt0G4" executionInfo={"status": "ok", "timestamp": 1755651699803, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# lead_time 이상치 제거
df = df[df['lead_time'] < 366]
```

```python colab={"base_uri": "https://localhost:8080/"} id="HdqXaGpTgPEd" executionInfo={"status": "ok", "timestamp": 1755651699818, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="778dc713-8f83-4f05-b404-9453b6204a59"
# 전처리 후 최종 데이터 비율 - 실제 분석보고서에선 이런 부분 추가하지 않음
len(df)/119390 * 100
```

<!-- #region id="_HPZiHcRHfQq" -->
#### <그 외 이상치 의심 데이터>

**일반적으로 "여행"이라는 상황에서 잘못 되었다고 의심할 수 있는 데이터**
1. 예약 박수(stays_in_weekend_nights + stays_in_week_nights)가 전부 0
 - https://www.dayuse.com/s/portugal/porto?selectedAddress=Porto&checkinDate=2025-08-22
2. 사람(adults + children + babies)의 수 총합이 0인 데이터
3. 전 예약건수가 극도로 높은 값
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="uN3MjMydIe4A" executionInfo={"status": "ok", "timestamp": 1755651699829, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ccf90e08-94bc-4fe8-bfe9-8435a578fa59"
# 1. 예약 박수(stays_in_weekend_nights + stays_in_week_nights)가 전부 0
df[(df['stays_in_weekend_nights']==0) & (df['stays_in_week_nights']==0)]
```

```python id="bOLcekNqI_ac" executionInfo={"status": "ok", "timestamp": 1755651699831, "user_tz": -540, "elapsed": 6, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 전체 데이터 중 해당 데이터의 양이 적으므로 삭제 결정
df = df[~((df['stays_in_weekend_nights']==0) & (df['stays_in_week_nights']==0))]
```

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="i-N0wuKwIT72" executionInfo={"status": "ok", "timestamp": 1755651699841, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6992969d-25b9-4306-f5a4-6d995bbc9865"
# 2. 사람(adults + children + babies)의 수 총합이 0인 데이터 확인

df[(df['adults']==0) & (df['children']==0) & (df['babies']==0)]
```

```python id="k8lVzG2oJlft" executionInfo={"status": "ok", "timestamp": 1755651699848, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 전체 데이터 중 해당 데이터의 양이 적으므로 삭제 결정
df = df[~((df['adults']==0) & (df['children']==0) & (df['babies']==0))]
```

```python colab={"base_uri": "https://localhost:8080/"} id="ZIdhcIE9Jr79" executionInfo={"status": "ok", "timestamp": 1755651699865, "user_tz": -540, "elapsed": 15, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e502413a-0b5c-458e-a265-bdea5522a4e0"
# 이전 예약건 수가 극도로 높은값 확인하기 위해 이전 예약건 확인

np.sort(df['previous_bookings_not_canceled'].unique())
```

```python colab={"base_uri": "https://localhost:8080/"} id="BOH_175JJ13X" executionInfo={"status": "ok", "timestamp": 1755651699879, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a3d7a0ad-8291-47de-a8ed-ad2117edcf54"
np.sort(df['previous_cancellations'].unique())
```

<!-- #region id="ZocYqTQGKYXG" -->
- 전 예약이 취소가 되었거나 취소가 되지 않았을 때, 데이터가 이상치 일까?

    - 회사에서 출장을 여행사 통해 한다면, 한 고객에 대해 반복적인 숙박, 취소가 이뤄지지 않는가?
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 896} id="qfnsXkTEKtLv" executionInfo={"status": "ok", "timestamp": 1755651699885, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ebcaea34-32f4-4993-985f-0517b20ef7e7"
# 데이터 확인
df[df['previous_bookings_not_canceled'] > 69].T
```

```python colab={"base_uri": "https://localhost:8080/", "height": 896} id="5Jf0o9CbK16y" executionInfo={"status": "ok", "timestamp": 1755651699990, "user_tz": -540, "elapsed": 100, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="0028883a-f249-4c1d-ee4d-4767e6f4a9a0"
# 데이터 확인
df[df['previous_cancellations'] > 19].T
```

<!-- #region id="Ey1FMAeVLEen" -->
**결론**

1. 출장의 경우 한 고객의 요청으로 반복 예약 들어올 수 있다고 판단
    - 이전 예약이 극도로 큰 값이 있을 수 있다고 결정

2. 만약 신혼여행을, 대행사가 대신 예약을 걸어놓는다면 이전의 예약 취소가 빈번하게 적혀진 건 정말 오류일까?

> 해당 상황에 대한 명확하고 객관적인 근거가 없으므로 극단적인 이전 예약 수와 관련한 값은 이상치라 판단하지 않음
<!-- #endregion -->

<!-- #region id="sCbavjsDgcLi" -->
# 3. 데이터 시각화
<!-- #endregion -->

<!-- #region id="i2SdzeF3gfqa" -->
### (1) 시각화 위한 데이터 탐색
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 178} id="s2OyVQjXgRbw" executionInfo={"status": "ok", "timestamp": 1755651700053, "user_tz": -540, "elapsed": 61, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2cf3aa3b-df61-4828-e3ed-4b9316558d29"
# 예약 취소 건수 확인
df['is_canceled'].value_counts()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 209} id="WRTGWd1agik_" executionInfo={"status": "ok", "timestamp": 1755651700063, "user_tz": -540, "elapsed": 7, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d0f17b30-6026-4c4f-9521-37f2dadd062c"
# 예약 상태 확인
df['reservation_status'].value_counts()
```

<!-- #region id="nOmd0FPbg63E" -->
is_canceled==0와 reservation_status =='Check-out'의 데이터가 같은건지 확인 필요
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="sta7D-3Lgrl4" executionInfo={"status": "ok", "timestamp": 1755651700115, "user_tz": -540, "elapsed": 49, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9cd585a7-1ef2-40b2-ac6b-af3e19a2dce4"
df[(df['is_canceled'] == 0) & (df['reservation_status'] =='Check-Out')]
```

<!-- #region id="Pt08ut0ggpM3" -->
**결론**

- is_canceled==0와 reservation_status =='Check-out'의 데이터가 같음
    - 취소하지 않은 예약건은 모두 reservation_status가 체크아웃!
- 예약이 취소되는 상황은 "예약 취소" + "No-show" 포함이 됨
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 241} id="zzZ4XO0XgmpU" executionInfo={"status": "ok", "timestamp": 1755651700122, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2d67c8a7-5ae0-4dfc-d2fd-b03a6fe8a3be"
# 호텔별 취소 건수 비교
df.groupby(by='hotel')['is_canceled'].value_counts()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 241} id="IoVpX_tPhYWy" executionInfo={"status": "ok", "timestamp": 1755651700128, "user_tz": -540, "elapsed": 5, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d5121f99-ce1c-4bd8-fc9a-14a22dd636fd"
# 호텔별 취소 건수 비율 비교
df.groupby(by='hotel')['is_canceled'].value_counts(normalize=True) * 100
```

<!-- #region id="F_k6ogLThciL" -->
=> City hotel 예약건의 수가 많고 취소도 많으며 취소 비율이 더 높다.
<!-- #endregion -->

<!-- #region id="-2D6Dq7Eheac" -->
### (2) 시각화
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 806} id="2FLY4ZmPhaMz" executionInfo={"status": "ok", "timestamp": 1755651701036, "user_tz": -540, "elapsed": 904, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="40ea5bde-3b4d-4f73-80d1-4ed373440f69"
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

<!-- #region id="7wqhPprviE0V" -->
=> days_in_waiting_list값은 0만 있으므로 상관도 계산 불가 (피어슨 상관계수의 식 - 표준편차로 나눠줘야 함!)

- 해당 변수 제외하고 다시 상관관계 히트맵 그리기
<!-- #endregion -->

```python id="TygPjPfJjMaZ" executionInfo={"status": "ok", "timestamp": 1755651701066, "user_tz": -540, "elapsed": 78, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 히트맵 폰트 관련 이슈때문에 실행하는 셀
import matplotlib as mpl
mpl.rcParams['axes.unicode_minus'] = False
```

```python colab={"base_uri": "https://localhost:8080/"} id="kr-hc8G9hpvx" executionInfo={"status": "ok", "timestamp": 1755651701069, "user_tz": -540, "elapsed": 69, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c35f85f3-59c6-4a13-a511-6a7c9ca10859"
# 수치형 변수만 먼저 추출하고 컬럼 이름 확인
numeric_df = df.select_dtypes(include="number")
numeric_df.columns
```

```python colab={"base_uri": "https://localhost:8080/", "height": 806} id="yN1Lex9TiWab" executionInfo={"status": "ok", "timestamp": 1755651701892, "user_tz": -540, "elapsed": 863, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b251efd9-9492-4509-ae34-3af83b7b0071"
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

<!-- #region id="EOXTfduNkq-J" -->
#### **상관관계 해석**

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


---------------------------
---------------------------
<!-- #endregion -->

<!-- #region id="ChofYs0o4mbB" -->
# **🧪 분석 방향**
> is_canceled와 연관이 높은 컬럼들을 다루고, 취소에 영향을 미치는 요인이 뭔지 알아본다!

<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 530} id="eb4uD895ik21" executionInfo={"status": "ok", "timestamp": 1755651702136, "user_tz": -540, "elapsed": 239, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3ae0de01-a403-413d-f46b-311a011e3d70"
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

```python colab={"base_uri": "https://localhost:8080/", "height": 409} id="ivpzXdR50WQF" executionInfo={"status": "ok", "timestamp": 1755651702838, "user_tz": -540, "elapsed": 695, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5b8e437c-ec13-4fcb-c19d-fa66267bf518"
# lead_time에 따른 취소율 시각화 - kde 플롯
plt.figure(figsize=(6, 4))
sns.kdeplot(data=df, x='lead_time', hue='is_canceled', fill=True)
plt.title("리드타임에 따른 취소율 시각화 - KDE 플롯")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 409} id="YouN97RA0nok" executionInfo={"status": "ok", "timestamp": 1755651703240, "user_tz": -540, "elapsed": 409, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3b3408e0-0bde-4f92-bab6-faef6860446f"
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

```python colab={"base_uri": "https://localhost:8080/", "height": 332} id="4HfGziKeWii6" executionInfo={"status": "ok", "timestamp": 1755651703431, "user_tz": -540, "elapsed": 190, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c0fb3fe0-58d7-45d0-9b18-aec82f57b189"
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

```python colab={"base_uri": "https://localhost:8080/", "height": 417} id="naYUzwgWWie3" executionInfo={"status": "ok", "timestamp": 1755651703922, "user_tz": -540, "elapsed": 493, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9cbc10ed-2ccd-4a5e-f453-4f0c3c580ad3"
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

<!-- #region id="MYFQY3MSYSCm" -->
**stays_in_week_nights**

- 한 달 미만(< 30): 숙박일이 길 수록 취소율이 높아지는 경향성이 있다.

    => 하루 이틀 정도 묵는 사람들보다 좀 더 오래 머무를 계획을 가진 고객이 예약을 더 많이 취소하는 경향이 있다고 볼 수 있다.
<!-- #endregion -->

```python id="gM27nciHx_u5" executionInfo={"status": "ok", "timestamp": 1755651703926, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# is_repeated_guest 시각화

# 그룹별 평균 취소율
repeat_cancel = df.groupby('is_repeated_guest')['is_canceled'].mean().reset_index()
repeat_cancel['is_repeated_guest'] = repeat_cancel['is_repeated_guest'].map({0: '신규 고객', 1: '재방문 고객'})
repeat_cancel.columns = ['고객 유형', '평균 취소율']
```

```python colab={"base_uri": "https://localhost:8080/", "height": 409} id="5zaw-3biyDxa" executionInfo={"status": "ok", "timestamp": 1755651704129, "user_tz": -540, "elapsed": 202, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="faaf71d0-649e-48ae-aec4-c25079804e34"
# 시각화
plt.figure(figsize=(4, 4))
sns.barplot(data=repeat_cancel, x='고객 유형', y='평균 취소율', color='teal')
plt.title('재방문 여부에 따른 평균 예약 취소율')
plt.ylim(0, 0.3)
plt.grid(True, axis='y', linestyle='--', alpha=0.3)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 332} id="YvJMormMWiaq" executionInfo={"status": "ok", "timestamp": 1755651704410, "user_tz": -540, "elapsed": 277, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a1327cc4-3ff3-4744-a517-c8928196388c"
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

<!-- #region id="x9ofy9lxagXj" -->
**required_car_parking_spaces**

- 주차 공간을 요청하지 않은 고객의 취소율은 높다.

> 근데 과연, 주차를 요청한 경우의 예약이 많을것인가?
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 241} id="AxgcTT544xeR" executionInfo={"status": "ok", "timestamp": 1755651704412, "user_tz": -540, "elapsed": 38, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="00ececae-e4b5-4036-bc9a-66e478271acd"
df['required_car_parking_spaces'].value_counts()
```

```python colab={"base_uri": "https://localhost:8080/"} id="YNy-4D2r5NQv" executionInfo={"status": "ok", "timestamp": 1755651704413, "user_tz": -540, "elapsed": 16, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d6e71418-ea6a-4d7a-8603-70419f2c8c7d"
# 비율 확인 - 이런건 실제 보고에는 포함하지 X

(len(df) - 77122)/len(df) * 100
```

<!-- #region id="QnzTaAF95Uxx" -->
**required_car_parking_spaces**

- 주차 공간을 요청한 예약은 전체의 8%

- 전체 예약건 중, 주차 공간을 요청하는 것은 매우 적다.

- 하지만, 전체적인 트렌드를 읽어주는 것은 의미있을 듯

    - 주차 공간을 요청한 고객들은 예약을 100% 유지한다.

        => 고객들이 차량을 이용할 만큼 강한 방문 의지가 있는 경우라고 해석할 수 있음
<!-- #endregion -->

```python id="x0JLOxZNynTw" executionInfo={"status": "ok", "timestamp": 1755651704436, "user_tz": -540, "elapsed": 5, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# booking_changes 시각화

# 그룹별 평균 취소율 계산
booking_cancel = df.groupby('booking_changes')['is_canceled'].mean().reset_index()
booking_cancel.columns = ['예약 변경 횟수', '평균 취소율']
```

```python colab={"base_uri": "https://localhost:8080/", "height": 486} id="WCR-GVnQynLM" executionInfo={"status": "ok", "timestamp": 1755651704715, "user_tz": -540, "elapsed": 282, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="338bdf32-9515-4a6a-b24c-6fb825a955c8"
# 시각화
plt.figure(figsize=(8, 5))
sns.barplot(data=booking_cancel, x='예약 변경 횟수', y='평균 취소율', color='#FE8330')
plt.title('예약 변경 횟수에 따른 평균 예약 취소율')
plt.ylim(0, 0.35)
plt.show()
```

```python id="AHBl2bGSwb8P" executionInfo={"status": "ok", "timestamp": 1755651704763, "user_tz": -540, "elapsed": 46, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# total_of_special_requests 시각화

# 그룹별 평균 취소율 계산 - 여기서부턴 따로 변수 지정해 계산
special_cancel = df.groupby('total_of_special_requests')['is_canceled'].mean().reset_index()
special_cancel.columns = ['요청 수', '평균 취소율']
```

```python colab={"base_uri": "https://localhost:8080/", "height": 332} id="5GamPVamxNns" executionInfo={"status": "ok", "timestamp": 1755651704959, "user_tz": -540, "elapsed": 193, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="565ff3b4-6b68-4c74-eb26-0b827c48a7c8"
# 시각화
plt.figure(figsize=(5, 3))
sns.barplot(data=special_cancel,x='요청 수', y='평균 취소율', color='skyblue')
plt.title('특별 요청 수에 따른 평균 예약 취소율')
plt.ylim(0, 0.4)
plt.show()
```

<!-- #region id="upeiYNVFwESe" -->
# 4. 결론

### **변수별 취소율 분석 요약**

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


-------------------------
-------------------------
<!-- #endregion -->

<!-- #region id="PCnN-vM82Bmu" -->
# 5. 인사이트 (Action Plan)

#### **1. Lead Time이 길수록 취소율 증가**

=> 리드타임(예약 후 도착까지 기간)이 길수록 고객의 일정 변경 가능성도 높아지며, 300일 이상인 경우 취소율이 50%를 초과함

**💡 Action Plan**

- 장기 예약에 대해 더 강력한 보증 정책 적용

    => 일정 이상 리드타임 고객에게 선결제, 부분 환불 조건 등 적용 고려

- 예약 리마인드 이메일/문자 자동화

    =>30일 전, 7일 전, 1일 전 등 고객 일정 재확인을 유도

- 예치금 기반 예약 정책 검토

    => 취소 방지를 위한 유연한 예치금 정책 도입


#### **2. 주중 장기 숙박일 수록 예약 취소율 증가**

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

#### **3. 재방문 고객은 확실히 충성도 높고 취소율 낮음**
=> 신규 고객의 취소율은 37%, 재방문 고객은 10% 이하 → 매우 안정적이고 충성도 높음

**💡 Action Plan**

- 재방문 고객 대상 특별 혜택 정책 강화

    => 할인, 우선 배정, 얼리체크인/레이트체크아웃 제공

- 충성고객 리텐션 프로그램 운영

    => 스탬프 적립, 멤버십 포인트 혹은 멤버쉽 등급제 도입 등

    - 예) 멤버쉽 등급별로 할인율 차등 지급하며 이 사실 광고에 유입

- 재방문 여부를 리스크 모델의 중요 변수로 활용

    => 신규 고객 위주의 과도한 예약 확대로 인한 리스크 방지

#### **4. 주차 공간 요청한 고객은 취소율이 매우 낮다**

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

#### **5. 특별 요청을 많이 하는 고객은 예약을 잘 지킨다**
=> 특별 요청이 0건인 고객은 취소율이 높은 반면, 1건 이상 요청한 고객은 신뢰도 높은 패턴을 보임

**💡 Action Plan**

- 고객의 요청을 적극 유도하는 UI&UX 개선

    => 예약 시점에 "요청사항이 있으신가요?"와 같은 질문 배치

- 요청 입력 유도 고객에게 리마인드 제공

    => "트윈 침대, 고층, 베이비 침대 요청을 준비 중입니다" 같은 메시지로 체류 의사 고취

- 요청 정보 기반 개인화 마케팅

    => 특정 요청을 자주 하는 고객군 대상 맞춤형 혜택 제공
    - 예) 아이와 자주 여행한 과거 기록이 있는 여행자의 경우 가족단위가 가기 좋은 호텔의 프로모션 발생시 팝업 더 자주 띄우기

-------------------------
-------------------------
<!-- #endregion -->

<!-- #region id="X9x2yBhRwxpc" -->
# 추가 분석 Point

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


<!-- #endregion -->

```python id="hTcu2MajxNEJ" executionInfo={"status": "ok", "timestamp": 1755651705043, "user_tz": -540, "elapsed": 82, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}

```
