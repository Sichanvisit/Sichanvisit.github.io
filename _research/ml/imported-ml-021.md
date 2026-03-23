---
title: "3 Bike Rental System"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]3_Bike Rental System - AI 5기 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]3_Bike Rental System - AI 5기 강사 답안.md"
excerpt: "Bike Rental System의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 전처리, 모델링, 데이터 시각화 순서로 큰 장을 먼저 훑고, GridSearchCV 모델 학습, LinearRegression / Ri... 같은 코드로 실제 구현을..."
research_summary: "Bike Rental System의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 전처리, 모델링, 데이터 시각화 순서로 큰 장을 먼저 훑고, GridSearchCV 모델 학습, LinearRegression / Ri... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 108개 코드 블록, 107개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, pandas입니다."
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
    <div class="research-overview__value">데이터 전처리 · 모델링 · 데이터 시각화 · 결과 저장</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">train/test CSV 불러오기 -&gt; LinearRegression / Ridge 모델 구성 -&gt; RMSLE 기준 성능 평가</div>
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

# 미션 설명

- 자전거 대여 시스템의 운영 담당자
- 🎯자전거 대여 패턴을 분석하여 자전거 배치 및 운영 전략을 최적화하고, 대여 수요를 정확하게 예측하는 것
- 🎯최종 목표: **RMSLE(Root Mean Squared Logarithmic Error)를 최대한 낮추는 것**

---

#### RMSLE 공식
$$
RMSLE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(p_i + 1) - \log(a_i + 1) \right)^2}
$$
- n: 데이터 포인트의 수
- pi: 예측 값
- ai: 실제 값
---

# 데이터

#### 파일 설명
- train.csv
    - 자전거 대여 수요를 예측하기 위한 데이터 포함
    - 종속 변수: count

- test.csv

    - count를 예측할 데이터 (최종 제출용)
    - casual, registered, count 컬럼 없음

| 컬럼명        | 데이터 타입   | 설명                                             |
| ---------- | -------- | ---------------------------------------------- |
| datetime   | datetime | 자전거 대여 기록의 날짜 및 시간. 예시: 2011-01-01 00:00:00    |
| season     | int      | 계절 (1: 봄, 2: 여름, 3: 가을, 4: 겨울)                 |
| holiday    | int      | 공휴일 여부 (0: 평일, 1: 공휴일)                         |
| workingday | int      | 근무일 여부 (0: 주말/공휴일, 1: 근무일)                     |
| weather    | int      | 날씨 상황 (1: 맑음, 2: 구름낌/안개, 3: 약간의 비/눈, 4: 폭우/폭설) |
| temp       | float    | 실측 온도 (섭씨)                                     |
| atemp      | float    | 체감 온도 (섭씨)                                     |
| humidity   | int      | 습도 (%)                                         |
| windspeed  | float    | 풍속 (m/s)                                       |
| casual     | int      | 등록되지 않은 사용자의 대여 수                              |
| registered | int      | 등록된 사용자의 대여 수                                  |
| count      | int      | 총 대여 수 (종속 변수)                                 |

# 분석 드릴다운

### 공유 시스템 이해

1. 공유할 대상이 존재해야함
    - 물리적 관점: 사용자가 찾는 시간과 장소에 자전거 없음 (퇴근 시간에 지하철역에 자전거 부족 등)
    - 관념적 관점: 사용하고 싶지 않게 만드는 요인을 제거
        - 예: 자전거가 녹슬어 있음, 안장이 젖어 있음, 기종이 불편함, 과금 정책이 불투명
    - 운영 전략 관점: 특정 지역에 자전거 몰림, 고장 난 자전거가 장시간 방치

2. 대여/반납이 원할해야함
    - 물리적 관점: UI&UX 및 결제 방식이 간편하고 직관적이어야 함 (예: 간편 결제 혹은 NFC나 QR 인식이 잘 안 됨)
    - 관념적 관점: 대여소의 상태가 쾌적해야 함
        - 예: 자전거가 쓰러져 있음, 대여소에 공간이 없음, 불쾌한 사용자 경험
    - 사회적/심리적 관점: 내것이 아니기에 혹은 대중적으로 사용하기 때문에 대여나 반납에 책임감이 적음

3. 공유 시스템의 지속성 한계
    - 경제적 관점: 단기 대여 수요에만 의존, 유지보수/재배치 인건비 과다
    - 환경적 관점: 방치된 자전거가 오히려 도시 미관 해치거나, 내것이 아니라 함부러 쓰면 짧은 수명
    - 정책적 관점: 지자체/업체 간 역할이 불명확하거나 책임 소재 불명확

```python
# 한글 오류 제거 코드
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

```python
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.pipeline import make_pipeline                                                              # 다항 회귀시 오류때문에 필요
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_squared_log_error
from sklearn.preprocessing import StandardScaler
```

```python
from google.colab import drive
drive.mount('/content/drive')
```

```python
train = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_train.csv')
test = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bike_test.csv')
```

```python
train.head(3)
```

```python
train.info()
```

```python
test.info()
```

```python
train.describe()
```

#### 1차 데이터 확인 결과

**독립 변수**로 볼 수 있는 값 중에 큰 치우침이 있는 데이터는 없는 것으로 확인

단, 몇 변수는 주의해서 데이터를 살펴봐야함
1. temp와 atemp: 최소 기온은 괜찮으나, 최고 기온이 41도, 45도 일반적이지 않음 => 데이터 살펴볼 필요성 있음
2. humidity: 최소 습도가 0과 최대가 100인 값이 존재할 수 있을지 확인 필요
3. windspeed: 최소 0과 최대 57이 가능한 값인지 확인 필요
 - 최대값이 57인데, 75%(Q3)는 17
    - 큰 값이 있다는 뜻
    - 이상치 의심해 봐야함
 - 분산이 큰 편
    - 다른 데이터들은 데이터의 특성에서 이해가 되는 범주인데, windspeed는 분산이 큰 걸로 보아 아예 바람이 안 불거나 쎄게 분 날이 많았다는 판단이 됨

4. Datetime: 문자형(object) -> datetime파싱 필요
 - 시간을 따로 분류해 보여주면 좋지 않을까 판단함
    - 자전거는 시간대별 대여 분포가 다를 것으로 예상

**종속 변수**인 count는 right-skewed가 큼

- 평균(mean) 대비 중앙값(50%)이 차이가 있음
    - 191.6 > 145
- 최댓값 대비 IQR이 좁은 느낌
    - 977은 최대, IQR = 284-42=242

 > ==> 모델 점수가 좋지 못 할 포인트!

- 종속변수의 값 레인지를 EDA하고 그에 따른 스케일링 방법을 사용

#### EDA 포인트
- holiday와 weekday의 대여 분포도 확인
- 날씨별 대여 확인
- 시간대별 대여 확인
- 계절별 대여 확인
- casual, registered는 제외하고 count만 종속변수로 확인

**[1차 가설]**
1. 자전거 대여 수요는 날씨와 시간의 영향을 가장 크게 받을 것이다.
    - 태풍, 비바람 등의 날씨에 자전거를 대여해서 탈 사람은 적을 것이다.
    - 출퇴근 시간에 대여수가 가장 클 것이다.

2. 자전거 대여 수요는 시즌성이 강할 것이다.
    - 추운 계절보다는 따뜻한 계절에 자전거를 더 많이 대여할 것이다.

그 외 EDA 후 최종 가설을 선정할 것임

---
# 1. 데이터 확인

```python
# 시각화: count의 분포 확인

plt.figure(figsize=(5, 3))
sns.histplot(train["count"], bins=50, kde=True)
plt.title("자전거 대여수(종속변수) 시각화")
plt.xlabel("자전거 대여수")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

RMSLE 점수를 안정적으로 계산하기 위해 count 변수 모두 로그 변환 필요

- 모델이 큰 수에 맞춰 학습을 하면 RMSLE기준 불균형성이 확인될 수 있기 때문
- 모델이 로그 공간 안에서 예측하면 같은 스케일이 보장되기 때문에 안정적 학습 가능

```python
# season 데이터 확인

train[train['season']==1].head()
```

- Season 설명에 1: 봄, 2: 여름, 3: 가을, 4: 겨울 이지만 실제 데이터는 2011-01-01에 봄으로 마킹되어 있음

- month데이터 참조하여 3,4,5월을 봄:1, 6,7,8월을 여름:2, 9,10,11월을 가을:3, 12,1,2월을 겨울:4로 바꾸는 것이 필요함

---
# 2. 데이터 전처리

### 1) 결측치 확인

```python
# 결측치 개수 확인
print("------train------")
print(train.isnull().sum())
print("------test------")
print(test.isnull().sum())
```

### 2) 중복값 확인

```python
print('train 중복값: ', train.duplicated().sum())
print('test 중복값: ', test.duplicated().sum())
```

### 3) datetime 데이터 타입 변환

```python
# datetime 파싱 및 hour, month, year 생성
def preprocess_custom_datetime(df):
    df["datetime"] = pd.to_datetime(df["datetime"])
    df["weekday_name"] = df["datetime"].dt.day_name()
    df["weekday_num"] = df["datetime"].dt.weekday
    df["hour"] = df["datetime"].dt.hour
    df["month"] = df["datetime"].dt.month
    df["year"] = df["datetime"].dt.year
    return df
```

```python
# 파생 변수 적용
train = preprocess_custom_datetime(train)
test = preprocess_custom_datetime(test)
```

```python
train.head()
```

```python
test.head()
```

### 4) 종속변수 로그 변환

```python
train["log_count"] = np.log1p(train["count"])                 # log1p: 0이나 작은 값에서의 수치 안정성을 위해 log(1 + x)를 더 정확히 계산해주는 함수. count==0일때 좋음.
train.head()
```

### 5) 계절 변화 - season 컬럼 정리

```python
def redefine_season(month):
    if month in [3, 4, 5]:
        return 1                  # 봄
    elif month in [6, 7, 8]:
        return 2                  # 여름
    elif month in [9, 10, 11]:
        return 3                  # 가을
    else:
        return 4                  # 겨울

train['season'] = train['month'].apply(redefine_season)
test['season'] = test['month'].apply(redefine_season)
```

```python
train.head()
```

### 6) 이상치 제거

```python
# windspeed 시각화

plt.figure(figsize = (4,3))
sns.boxplot(train['windspeed'])
plt.show()
```

```python
np.sort(train['windspeed'].unique())
```

#### Windspeed 조사
 보퍼트 풍력 계급 (위키피디아: https://ko.wikipedia.org/wiki/%EB%B3%B4%ED%8D%BC%ED%8A%B8_%ED%92%8D%EB%A0%A5_%EA%B3%84%EA%B8%89)

 - <0.3 (m/s): 연기가 수직으로 올라가는 고요한 상태
 - 10.8 ~ 13.9(m/s): 우산을 사용하기 어려운 상태
 - 13.9~17.2 (m/s): 바람을 안고 걷기 곤란한 상태
 - 17.2~20.7 (m/s):  작은 나무가지가 꺾이며, 바람을 안고서 걷기 곤란한 상태

 ==> 바람 속도가 극도로 높은 수치는 의심해 봐야함

```python
train[train['windspeed']>=20]
```

```python
1495 /len(train)
```

```python
# windspeed 20보다 큰 train데이터 중, count 컬럼의 합계
print(train[train['windspeed']>=20]['count'].sum())
```

```python
# windspeed 20보다 큰 train데이터 중, count 컬럼의 합계의 비율 확인
train[train['windspeed']>=20]['count'].sum()/train['count'].sum()
```

- 20m/s 이상의 데이터는 **약 14%** 의 비율
- windspeed가 20m/s 이상인 데이터의 count합의 비율은 **약 15%**

##### 결론]
1. 0.0의 값은 계측기로 인한 두번째 소수점 소실로 보고 이상치로 취급하지 않음
2. windspeed가 20을 넘는 값에서 자전거를 탄다는 것은 현실적으로 어렵다고 판단(보퍼트 기준), 20 넘는 수치를 그 외 수치의 평균으로 환산

     - AI 4기의 도메인 지식 기반한 결정

```python
# windspeed 이상치 평균으로 대체

windspeed_mean = round(train[train['windspeed'] <= 20]['windspeed'].mean(), 4)
train.loc[train['windspeed'] >= 20, 'windspeed'] = windspeed_mean
```

```python
np.sort(train['windspeed'].unique())
```

```python
plt.figure(figsize=(5, 3))
sns.histplot(train["windspeed"], bins=50, kde=True)
plt.title("바람 시각화")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

**windspeed**

이상치 바뀐 뒤 데이터 정규성은 보이지 않음
- 선형 회귀는 데이터가 정규성이 보장될 때 성능이 좋은 모델
- 바람의 세기가 0이라는 건 계측기의 측정 방식으로 발생할 수 있는 일이라 판단하고 그대로 진행

---

```python
# humidity 시각화

plt.figure(figsize = (4,3))
sns.boxplot(train['humidity'])
plt.show()
```

```python
plt.figure(figsize=(5, 3))
sns.histplot(train["humidity"], bins=50, kde=True)
plt.title("습도 시각화")
plt.grid(True)
plt.tight_layout()
plt.show()
```

#### Humidity 조사

> 보퍼트 풍력계처럼 명확한 단계별 명칭 체계는 존재하지 않음.
단, 여러 단체에서 권장하는 습도 기준은 이정도

| 기관                         | 권장/기준 범위                              | 설명                 |
| -------------------------- | ------------------------------------- | ------------------ |
| **ASHRAE** (미국 냉난방공조학회)    | **30\~60% RH**                        | 실내 쾌적성 및 곰팡이 방지 기준 |
| **WHO** (세계보건기구)           | **40\~60% RH**                        | 건강한 실내 공기질 유지      |
| **EPA** (미국 환경보호청)         | **30\~50% RH**                        | 곰팡이·먼지 진드기 억제      |
| **KS B ISO 9241-6** (한국표준) | **40\~60% RH**                        | 사무환경 인체공학 기준       |
| **ASHRAE Standard 55**     | 사람의 쾌적함을 위한 환경 조건 → 습도는 **60% 이하 권장** |                    |

---

**낮은 습도**
1. 건조한 사막 습도 10~20% 언급 뉴스기사 - https://weekly.chosun.com/news/articleView.html?idxno=28844
2. 극한의 건조한 지역에 대한 습도 2% 언급 뉴스기사 - https://www.dvidshub.net/news/396765/extreme-dry-heat-mojave-desert-can-deadly-heat-plan-ahead
    - the humidity can be as low as 2 percent on any given summer day
3. 서하프리카 Harmattan 습도 5% 이하 언급 - https://en.wikipedia.org/wiki/Harmattan
    - the relative humidity drops under 5%.

**높은 습도**
1. 이란 Jask의 고습 사례 - https://en.wikipedia.org/wiki/List_of_weather_records
    - which translates to a relative humidity of 94%
    - 해당 위키피디아는 날씨 기록에 대한 리스트
    - 94%를 기록적인 습도로 언급하는 것은 가장 높은 수치에 가까운 것이라 판단할 수 있음

2. 상대습도와 절대습도
- https://ko.wikipedia.org/wiki/%EC%8A%B5%EB%8F%84
- %로 나타내는 것은 상대습도
- 상대습도의 경우 100% 가능하며, 이 경우 반드시 강수가 있는 것은 아님
    - 미국 기상청 내용: https://www.weather.gov/lmk/humidity#:~:text=If%20the%20relative%20humidity%20is,droplets%20suspended%20in%20the%20air
    - If the relative humidity is 100 percent (i.e., dewpoint temperature and actual air temperature are the same), this does NOT necessarily mean that precipitation will occur.

=> 습도의 경우 적은 경우가 이상치

```python
# humidity 이상치 처리
Q1 = train['humidity'].quantile(0.25)
Q3 = train['humidity'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
```

```python
upper_bound
```

- IQR로 진행하면 상단 122값이 upper bound의 기준
- 습도 100이 기준. 100 초과 나올 수 없음

    > IQR 말고 다른 이상치 제거방식으로 진행

```python
np.sort(train['humidity'].unique())
```

```python
len(train[train['humidity']==0])
```

```python
# humidity 최소값의 비율 확인
22/len(train) * 100
```

- List of weather records를 통해 3~100% 내외의 값은 충분히 가능한 것으로 판단
- humidity는 최소값인 0만 삭제

```python
# humidity 값이 0인 데이터 제거
train = train[(train['humidity'] != 0)]
```

```python
# 잘 제거되었나 확인
np.sort(train['humidity'].unique())
```

```python
plt.figure(figsize=(5, 3))
sns.histplot(train["humidity"], bins=50, kde=True)
plt.title("이상치 제거 후 습도 시각화")
plt.grid(True)
plt.tight_layout()
plt.show()
```

---
# 3. 데이터 시각화

### 1) 변수별 대여량 다각도 시각화

```python
# 시간대별 자전거 대여량 - 평균

plt.figure(figsize=(7,4))

sns.barplot(data=train, x="hour", y="count", ci=None)

# 선 넣고 싶어 추가
hourly_avg = train.groupby("hour")["count"].mean().reset_index()  #.groupby()를 하면 그룹핑 기준 컬럼이 인덱스로 설정되기 때문에 .reset_index() 필요
sns.lineplot(data=hourly_avg, x="hour", y="count", color="green", marker="o")

plt.title("시간대별 자전거 대여")
plt.xlabel("시간")
plt.ylabel("count 평균")
plt.show()
```

```python
# 시간대별 자전거 대여량 - 합계

plt.figure(figsize=(7,4))

sns.barplot(data=train, x="hour", y="count", ci=None, estimator=np.sum)    # estimator=np.sum을 통해 합계로 지정

# 선 넣고 싶어 추가
hourly_avg = train.groupby("hour")["count"].sum().reset_index()  #.groupby()를 하면 그룹핑 기준 컬럼이 인덱스로 설정되기 때문에 .reset_index() 필요
sns.lineplot(data=hourly_avg, x="hour", y="count", estimator=np.sum, color="green", marker="o")

plt.title("시간대별 자전거 대여 - 합계")
plt.xlabel("시간")
plt.ylabel("count 합계")
plt.show()
```

새벽 시간과 저녁시간 대여량 급감

**=> 출퇴근 시간 대여 급증**

```python
# 월별 자전거 대여량 - 평균 기준

plt.figure(figsize=(5,3))
sns.barplot(data=train, x="month", y="count", ci=None)           # count의 각 그룹 평균을 내서 계산 (디폴트)
plt.title("월별 자전거 대여량 - 평균 보기")
plt.xlabel("월")
plt.ylabel("평균 대여 건수")
plt.show()
```

```python
# 월별 자전거 대여량 - sum기준

plt.figure(figsize=(5,3))
sns.barplot(data=train, x="month", y="count", estimator=np.sum, ci=None)        #  estimator=np.sum: count의 각 그룹의 총합을 보여줌
plt.title("월별 자전거 대여량 - 총합")
plt.xlabel("월")
plt.ylabel("총 대여량")
plt.show()
```

=> 6-10월에 대여가 높은 트렌드가 있으며, 12-2월은 대여가 매우 적다

```python
# 계절별 자전거 대여량 - 평균 기준

plt.figure(figsize=(5,3))
sns.barplot(data=train, x="season", y="count", ci=None)           # count의 각 그룹 평균을 내서 계산 (디폴트)
plt.title("계절별 자전거 대여량 - 평균 보기")
plt.xlabel("계절")
plt.ylabel("평균 대여 건수")
plt.show()
```

```python
# 계절별 자전거 대여량 - sum기준

plt.figure(figsize=(5,3))
sns.barplot(data=train, x="season", y="count", estimator=np.sum, ci=None)        #  estimator=np.sum: count의 각 그룹의 총합을 보여줌
plt.title("계절별 자전거 대여량 - 총합")
plt.xlabel("계절")
plt.ylabel("총 대여량")
plt.show()
```

=> 여름에 특히 대여랑이 가장 많고, 겨울엔 대여량이 감소하는 경향이 있다

```python
# 요일별 대여 (workingday로 그룹핑)

plt.figure(figsize=(4,3))
sns.barplot(data=train, x="workingday", y="count", ci=None)
plt.title("업무일과 휴일 대여 비교")
plt.xlabel("업무일 (0 = No, 1 = Yes)")
plt.ylabel("평균 자전거 대여량")
plt.show()
```

=> 평일의 대여 건수가 좀더 많으나, 휴일과 큰 차이는 없음

```python
# 풍속별 대여 현황 - 평균

plt.figure(figsize=(8, 4))
sns.barplot(data=train, x="windspeed", y="count", ci=None)
plt.title("풍속별 대여 현황")
plt.ylabel("평균 자전거 대여량")
plt.xticks(rotation=45)
plt.show()
```

```python
# 풍속별 대여 현황 - 합계

plt.figure(figsize=(8, 4))
sns.barplot(data=train, x="windspeed", y="count", ci=None, estimator=np.sum)
plt.title("풍속별 대여 현황")
plt.ylabel("자전거 대여량 합계")
plt.xticks(rotation=45)
plt.show()
```

평균만으로 볼 수 없던 자전거 대여량 추이를 합계를 통해 확인 할 수 있음

1. 이상치 처리를 평균으로 하면서 평균값인 10.5241에 집중 분포된 것 확인
2. 바람의 세기가 세면 대여량 총합이 급감

```python
# 날씨별 대여

plt.figure(figsize=(5,3))
sns.barplot(data=train, x="weather", y="count", ci=None)
plt.title("날씨별 대여 현황")
plt.xlabel("날씨 - 1: 맑음, 2: 구름, 3: 비/눈, 4: 악천후")
plt.ylabel("평균 자전거 대여량")
plt.show()
```

```python
train[train["weather"]==4]
```

=> weather==4인 데이터는 1건

 - 위 그래프만으론 데이터의 추이를 파악하기엔 무리가 있음

```python
# weather별 그루핑해서 데이터 보기
weather_grouped  = train.groupby("weather")["count"].agg(["sum", "count", "mean"]).reset_index()
weather_grouped
```

```python
# 날씨별 대여수 총합 시각화

plt.figure(figsize=(5,6))

# 선 넣고 싶어 추가
sns.lineplot(data=weather_grouped, x="weather", y="sum", color="green", marker="o")

sns.barplot(data=weather_grouped, x="weather", y="sum", ci=None)
plt.title("날씨별 대여수 총합")
plt.xlabel("날씨 - 1: 맑음, 2: 구름, 3: 비/눈, 4: 악천후")
plt.ylabel("자전거 총 대여량")
plt.show()
```

=> 날씨가 좋을때 자전거 대여가 가장 많으며, 비나 눈이 올 경우 대여량이 급감한다

```python
# 온도(temp)에 따른 대여 건수(행 개수) 계산
temp_bins = train.groupby('temp').size().reset_index(name='count')
```

```python
# 온도와 대여량 관계

plt.figure(figsize=(8,3))
plt.plot(temp_bins["temp"], temp_bins["count"], marker="o", label="온도")
plt.title("온도별 대여량")
plt.xlabel("온도")
plt.show()
```

=> 각 온도에 대한 대여량 시각화

count를 세서 나타내는 것이 아닌 단순 빈도수 설정

따라서 온도에 대한 값으로 표현하기는 좀 애매함

---

온도에서 count수 자체가 어떻게 변하는지를 보기 위해, 온도별 count변수의 평균을 보는 방향으로 진행하기로 함

```python
# 온도별 평균 대여량 계산
temp_avg = train.groupby("temp")["count"].mean().reset_index()

# 시각화
plt.figure(figsize=(7, 3))
sns.lineplot(data=temp_avg, x="temp", y="count", marker="o")
plt.title("온도에 따른 평균 자전거 대여량")
plt.xlabel("온도")
plt.ylabel("평균 대여량")
plt.grid(True)
plt.show()
```

=> 36도까진 온도가 올라갈 수록 자전거 대여량이 높아지는 경향이 있음

```python
# 요일별 자전거 대여량 - 평균

plt.figure(figsize=(8,3))
sns.barplot(data=train, x="weekday_name", y="count", ci=None)
plt.title("요일별 대여 현황")
plt.xlabel("요일")
plt.ylabel("평균 자전거 대여량")
plt.show()
```

```python
# 요일별 자전거 대여량 - 총합

plt.figure(figsize=(8,3))
sns.barplot(data=train, x="weekday_name", y="count", ci=None, estimator=np.sum)
plt.title("요일별 대여 현황")
plt.xlabel("요일")
plt.ylabel("평균 자전거 대여량")
plt.show()
```

=> 요일별 대여 현황엔 큰 차이는 없음

### 2) 상관관계 시각화

모델링 전에 변수들 파악하기 위해 진행

```python
# 수치형 변수만 추출해서 전체 상관관계 히트맵 생성
numeric_df = train.select_dtypes(include="number")

# 상관행렬 계산
full_corr_matrix = numeric_df.corr()

# 히트맵 시각화
plt.figure(figsize=(12, 10))
sns.heatmap(full_corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("수치형 변수 상관관계 히트맵")
plt.tight_layout()
plt.show()
```

### 3) 습도와 풍속 구간별 대여량

```python
# 습도 구간화
bins = [0, 30, 60, train['humidity'].max()]                                                         # 저습도, 중간 습도, 고습도
labels = ['Low', 'Medium', 'High']
train['humidity_bin'] = pd.cut(train['humidity'], bins=bins, labels=labels, include_lowest=True)
```

```python
# 구간별 대여량 평균
humidity_analysis = train.groupby('humidity_bin')['count'].mean().reset_index()
humidity_analysis
```

```python
# 습도 구간별 대여량 시각화 - 평균 기준

plt.figure(figsize=(4,3))
sns.barplot(data=humidity_analysis, x='humidity_bin', y='count')
plt.title('습도 구간별 대여량 평균')
plt.xlabel('습도 구간')
plt.ylabel('대여량 평균')
plt.show()
```

```python
# 구간별 대여량 총합
humidity_analysis = train.groupby('humidity_bin')['count'].sum().reset_index()
humidity_analysis
```

```python
# 습도 구간별 대여량 시각화 - 총합 기준

plt.figure(figsize=(4,3))
sns.barplot(data=humidity_analysis, x='humidity_bin', y='count', estimator=np.sum)
plt.title('습도 구간별 대여량 총합')
plt.xlabel('습도 구간')
plt.ylabel('대여량 총합')
plt.show()
```

=> 습도가 너무 낮을땐 자전거 대여 총합이 작고, 중간과 높을 때 대여량이 많다
 - 일반적으로 육지는 겨울의 경우 매우 낮아지는 경우가 대부분
    - 해양성 기후 혹은 상대적 우리나라 가을날씨를 겨울로 부르는 곳은 겨울에 습도가 높아지기도 함. 하지만 대개는 겨울에 습도가 낮아짐
    - 해양성 기후 습도 높아지는 것에 대한 정보: https://geo.libretexts.org/Bookshelves/Geography_%28Physical%29/The_Physical_Environment_%28Ritter%29/09%3A_Climate_Systems/9.05%3A_Midlatitude_and_Subtropical_Climates/9.5.06%3A_Marine_%28Humid%29_West_Coast_Climate
        - Not only is the **marine west coast** noted for its **mild temperatures** but also for its heavy cloud cover and **high humidity** through much of the year.
 - 해당 데이터가 육지에 위치한 도시로 예상

```python
# 풍속 구간화

bins = [0, 5, 10, 15, train['windspeed'].max()]
labels = ['Very Low', 'Low', 'Medium', 'High']

train['windspeed_bin'] = pd.cut(train['windspeed'], bins=bins, labels=labels, include_lowest=True)
```

```python
# 구간별 대여량 평균
windspeed_analysis = train.groupby('windspeed_bin')['count'].mean().reset_index()
windspeed_analysis
```

```python
# 풍속 구간별 대여량 시각화 - 평균 기준
plt.figure(figsize=(4,3))
sns.barplot(data=windspeed_analysis, x='windspeed_bin', y='count')
plt.title('풍속 구간별 대여량 평균')
plt.xlabel('풍속 구간')
plt.ylabel('대여량 평균')
plt.show()
```

```python
# 구간별 대여량 총합
windspeed_analysis = train.groupby('windspeed_bin')['count'].sum().reset_index()
windspeed_analysis
```

```python
# 풍속 구간별 대여량 시각화 - 총합 기준
plt.figure(figsize=(4,3))
sns.barplot(data=windspeed_analysis, x='windspeed_bin', y='count', estimator=np.sum)
plt.title('풍속 구간별 대여량 총합')
plt.xlabel('풍속 구간')
plt.ylabel('대여량 총합')
plt.show()
```

=> 바람은 어떤 트렌드를 발견하긴 어려우나, 바람이 세면 대여량 총합이 떨어지는 것은 확인
- 여기서 풍속은 고민해 볼 필요가 있음
- 해당 지역이 바람부는 날이 워낙 적은가? 혹은 정말 바람이 적은 때 자전거를 잘 안 빌리는가?

    => 바람이 강할수록 자전거를 잘 빌린다는 것은 상식에 어긋남

---
# 4. 모델링

### 1) 1차 모델링

현재까지 전처리한 데이터 기반, 회귀 모델링 실시

```python
# 모델링 타겟 변수 지정
features_1 = ['season', 'holiday', 'workingday', 'weather', 'temp',
       'atemp', 'humidity', 'windspeed', 'weekday_num', 'hour', 'month', 'year']
```

```python
# 데이터 지정
X1_train = train[features_1]
y1_train = train["log_count"]

# 테스트 데이터도 위의 타깃 변수만 지정함
X_test = test[features_1]
```

```python
# 학습/검증 분할
X1_train, X1_val, y1_train, y1_val = train_test_split(X1_train, y1_train, test_size=0.3, random_state=42)
```

```python
# 회귀 모델 정의

models = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1),
    "Lasso": Lasso(alpha=10),
    "ElasticNet": ElasticNet(alpha=0.01, l1_ratio=0.1),
    "Polynomial_2nd": make_pipeline(PolynomialFeatures(degree=2), LinearRegression()),
    "Polynomial_3rd": make_pipeline(PolynomialFeatures(degree=3), LinearRegression())
}
```

```python
# 모델 훈련 - 할 필요없으나 예시로 붙
model_lr = LinearRegression()
model_lr.fit(X1_train, y1_train)

model_ridge = Ridge()
model_ridge.fit(X1_train, y1_train)

model_lasso = Lasso()
model_lasso.fit(X1_train, y1_train)

model_ela = ElasticNet()
model_ela.fit(X1_train, y1_train)

model_2poly = PolynomialFeatures()
model_2poly.fit(X1_train, y1_train)

model_3poly = PolynomialFeatures()
model_3poly.fit(X1_train, y1_train)
```

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

```python
# 모델 결과 확인
results_1 = pd.DataFrame(results_1)
results_1
```

=> 3차 다항 회귀의 결과가 가장 좋음

- 변수가 늘어나면 결국 점수가 나아지는 걸까?!?

기본 모델링이었기 때문에 이후로 점수 올릴 방법론 강구

### 2) 2차 모델링

Ridge, Lasso와 Elasticnet의 하이퍼 파라미터 조정

다항 회귀는 2차만 진행하기로 결정

```python
# 파라미터 그리드 정의
param_grids = {
    "Ridge": {"alpha": [0.001, 0.01, 0.1, 1, 10, 100, 1000]},
    "Lasso": {"alpha": [0.00001, 0.0001, 0.001, 0.01, 0.1, 1, 10]},
    "ElasticNet": {"alpha": [0.0001, 0.001, 0.01, 0.1], "l1_ratio": [0.1, 0.3, 0.5, 0.7, 0.9]},
    "Polynomial_2nd": {
        "polynomialfeatures__degree": [2],
        "linearregression__fit_intercept": [True, False]                        # y절편 학습 여부 설정 (수업때 배운 코드: include_bias=False)
    }
}
```

```python
# 회귀 모델 재정의

models_2 = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1),
    "Lasso": Lasso(alpha=10),
    "ElasticNet": ElasticNet(alpha=0.01, l1_ratio=0.1),
    "Polynomial_2nd": make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
}
```

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

```python
# 모델 결과 확인
results_2 = pd.DataFrame(results_2)
results_2
```

=> 결과의 큰 차이 없음

### 3) 3차 모델링

파생 변수 추가하고 바람 변수만 빼고 모델링하기

```python
# 시간대별 정보를 담은 여러 파생변수 추가

def add_feature_engineering(df):
    df["is_weekend"] = df["weekday"].isin([5, 6]).astype(int)
    df["is_rush_hour"] = df["hour"].isin([7, 8, 9, 17, 18, 19]).astype(int)
    df["is_morning"] = df["hour"].between(6, 11).astype(int)
    df["is_night"] = df["hour"].between(21, 23).astype(int)
    df["is_workhour"] = df["hour"].between(9, 17).astype(int)
    return df
```

```python
# 위 함수 적용
train = add_feature_engineering(train)
test = add_feature_engineering(test)
```

```python
train.head(3)
```

```python
test.head(3)
```

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

=> 오전과 낮에 평균 대여량이 높고, 러시아워에 특히 대여량이 많음

```python
# 모델링 타깃 변수 지정
features_2 = ['season', 'holiday', 'workingday', 'weather', 'temp',
              'atemp', 'humidity', 'hour', 'month','year','week_day',
              'is_weekend', 'is_rush_hour', 'is_morning','is_night',
              'is_workhour']
```

```python
# 독립변수 종속변수 지정

X3_train = train[features_2]
y3_train = train["log_count"]

# 테스트 데이터도 위의 타깃 변수만 지정함
X3_test = test[features_2]
```

```python
# 학습/검증 분할

X3_train, X3_val, y3_train, y3_val = train_test_split(X3_train, y3_train, test_size=0.3, random_state=42)
```

```python
# 모델 학습 및 평가
results_3 = []

for name, model in models_2.items():
    model.fit(X3_train, y3_train)
    y3_pred_log = model.predict(X3_val)
    y3_pred = np.expm1(y3_pred_log)
    y3_true = np.expm1(y3_val)

    mae = mean_absolute_error(y3_true, y3_pred)
    mse = mean_squared_error(y3_true, y3_pred)
    rmse = np.sqrt(mean_squared_error(y3_true, y3_pred))
    rmsle = np.sqrt(mean_squared_log_error(y3_true, y3_pred))
    r2 = r2_score(y3_true, y3_pred)

    results_3.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "RMSLE": rmsle,
        "R제곱" : r2
    })
```

```python
# 모델 결과 확인
results_3 = pd.DataFrame(results_3)
results_3
```

==> 풍속을 제거하기 전과 제거한 후, RMSLE점수가 하락하는 현상 확인

- 제거 전

    - Polynomial_2nd: 0.497600

- 제거 후

    - Polynomial_2nd: 0.497436

### 4) 4차 모델링

이상적인 날씨에 대해 파생변수 만든 뒤 풍속 제거 후 모델링

```python
# 함수 정의
def add_ideal_weather(df):
    # 습도 구간화 및 매핑
    humidity_bins = [0, 30, 60, 100]
    humidity_labels = ['Low', 'Medium', 'High']
    df['humidity_bin'] = pd.cut(df['humidity'], bins=humidity_bins, labels=humidity_labels)
    df['humidity_ideal'] = df['humidity_bin'].map(lambda x: 0 if x == 'Low' else 1)

    # 날씨 매핑
    df["weather_ideal"] = df["weather"].map(lambda x: 1 if x in [1, 2] else 0)

    return df
```

```python
# 함수 적용
train = add_ideal_weather(train)
test = add_ideal_weather(test)
```

```python
# 모델링 타깃 변수 지정
features_3 = ['season', 'holiday', 'workingday', 'weather', 'temp',
              'atemp', 'humidity', 'hour', 'month','year','weekday',
              'is_weekend', 'is_rush_hour', 'is_morning','is_night',
              'is_workhour', 'humidity_ideal','weather_ideal']
```

```python
# 독립변수 종속변수 지정

X4_train = train[features_3]
y4_train = train["log_count"]

# 테스트 데이터도 위의 타깃 변수만 지정함
X4_test = test[features_3]
```

```python
# 학습/검증 분할

X4_train, X4_val, y4_train, y4_val = train_test_split(X4_train, y4_train, test_size=0.3, random_state=42)
```

```python
# 회귀 모델 재정의 - Best Param사용

models_3 = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=10),
    "Lasso": Lasso(alpha=0.001),
    "ElasticNet": ElasticNet(alpha=0.01, l1_ratio=0.3),
    "Polynomial_2nd": make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
}
```

```python
# 모델 학습 및 평가
results_4 = []

for name, model in models_3.items():
    model.fit(X4_train, y4_train)
    y4_pred_log = model.predict(X4_val)
    y4_pred = np.expm1(y4_pred_log)
    y4_true = np.expm1(y4_val)

    mae = mean_absolute_error(y4_true, y4_pred)
    mse = mean_squared_error(y4_true, y4_pred)
    rmse = np.sqrt(mean_squared_error(y4_true, y4_pred))
    rmsle = np.sqrt(mean_squared_log_error(y4_true, y4_pred))
    r2 = r2_score(y4_true, y4_pred)

    results_4.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "RMSLE": rmsle,
        "R제곱" : r2
    })
```

```python
# 모델 결과 확인
results_4 = pd.DataFrame(results_4)
results_4
```

### 5) 5차 모델링

풍속을 표준화 한 다음 타킷 변수에 지정하여 활용

```python
# 표준화 - from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

train["windspeed_z"] = scaler.fit_transform(train[["windspeed"]]).ravel()      # ravel(): Series로 저장하기 위해 필요
test["windspeed_z"] = scaler.fit_transform(test[["windspeed"]]).ravel()
```

```python
# 모델링 타깃 변수 지정
features_4 = ['season', 'holiday', 'workingday', 'weather', 'temp',
              'atemp', 'humidity', 'weekday_num', 'hour', 'month', 'year',
              'week_day', 'is_weekend','is_rush_hour', 'is_morning', 'is_night',
              'is_workhour', 'windspeed_z']
```

```python
# 독립변수 종속변수 지정

X5_train = train[features_4]
y5_train = train["log_count"]

# 테스트 데이터도 위의 타깃 변수만 지정함
X5_test = test[features_4]
```

```python
# 학습/검증 분할

X5_train, X5_val, y5_train, y5_val = train_test_split(X5_train, y5_train, test_size=0.3, random_state=42)
```

```python
# 모델 학습 및 평가
results_5 = []

for name, model in models_2.items():
    model.fit(X5_train, y5_train)
    y5_pred_log = model.predict(X5_val)
    y5_pred = np.expm1(y5_pred_log)
    y5_true = np.expm1(y5_val)

    mae = mean_absolute_error(y5_true, y5_pred)
    mse = mean_squared_error(y5_true, y5_pred)
    rmse = np.sqrt(mean_squared_error(y5_true, y5_pred))
    rmsle = np.sqrt(mean_squared_log_error(y5_true, y5_pred))
    r2 = r2_score(y5_true, y5_pred)

    results_5.append({
        "Model": name,
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "RMSLE": rmsle,
        "R제곱" : r2
    })
```

```python
# 모델 결과 확인
results_5 = pd.DataFrame(results_5)
results_5
```

### 6) 6차 모델링

XGBoost로 위의 변수들 모델링

```python
from xgboost import XGBRegressor

model_xg = XGBRegressor()
model_xg.fit(X5_train, y5_train)
y5_pred_log = model_xg.predict(X5_val)
y5_pred = np.expm1(y5_pred_log)
y5_true = np.expm1(y5_val)
```

```python
mae = mean_absolute_error(y5_true, y5_pred)
mse = mean_squared_error(y5_true, y5_pred)
rmse = np.sqrt(mean_squared_error(y5_true, y5_pred))
rmsle = np.sqrt(mean_squared_log_error(y5_true, y5_pred))
r2 = r2_score(y5_true, y5_pred)
```

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

```python
# 모델 결과 확인
results_6 = pd.DataFrame(results_6)
results_6
```

==> XGBoost를 이용했을때 성능이 가장 좋음

# 5. 결과 저장

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

```python

```
