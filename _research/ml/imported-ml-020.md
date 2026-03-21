---
title: "2 Hotel Booking Demand - AI5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]2 Hotel Booking Demand - AI5 강사 답안.md"
excerpt: "Hotel Booking Demand를 중심으로 피처 엔지니어링 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "Hotel Booking Demand를 중심으로 피처 엔지니어링 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 데이터 불러오고 확인하기, (2) 결측치 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 95개 코드 블록, 95개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, pandas, numpy입니다."
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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>2015.07.01부터 2017.08.31까지의 Resort Hotel과 City Hotel의 예약 데이터</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>피처 엔지니어링</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>데이터 불러오고 확인하기 -&gt; (2) 결측치 -&gt; (2) 시각화</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 95 · 실행 95</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>matplotlib, warnings, pandas, numpy 외 1</td>
    </tr>
    </tbody>
  </table>
</div>

## What I Studied

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--notes">
    <thead>
      <tr>
        <th>개념</th>
        <th>핵심 설명</th>
        <th>코드에서 확인한 것</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">피처 엔지니어링</th>
      <td>피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.</td>
      <td>이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.</td>
    </tr>
    </tbody>
  </table>
</div>

## How I Implemented It

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--steps">
    <thead>
      <tr>
        <th>단계</th>
        <th>구현 내용</th>
        <th>핵심 API</th>
        <th>코드 포인트</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">Step 1 · 데이터 불러오기</th>
      <td>
        <strong class="research-compact-table__main">데이터 불러오고 확인하기</strong>
        <span class="research-compact-table__sub">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</span>
      </td>
      <td><code>pd.read_csv</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 전처리</th>
      <td>
        <strong class="research-compact-table__main">(2) 결측치</strong>
        <span class="research-compact-table__sub">결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>결측치 행 제거 - company</td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 피처 가공</th>
      <td>
        <strong class="research-compact-table__main">(2) 시각화</strong>
        <span class="research-compact-table__sub">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</span>
      </td>
      <td><code>matplotlib</code> <code>seaborn</code></td>
      <td>상관행렬 계산 · 히트맵 시각화</td>
    </tr>
    <tr>
      <th scope="row">Step 4 · 시각화</th>
      <td>
        <strong class="research-compact-table__main">🧪 분석 방향</strong>
        <span class="research-compact-table__sub">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</span>
      </td>
      <td><code>matplotlib</code> <code>seaborn</code></td>
      <td>lead_time 시각화 · 단위 구간으로 나누어 범주형 변수 생성</td>
    </tr>
    <tr>
      <th scope="row">Step 5 · 시각화</th>
      <td>
        <strong class="research-compact-table__main">데이터 분포 시각화</strong>
        <span class="research-compact-table__sub">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</span>
      </td>
      <td><code>matplotlib</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 6 · 구현 코드</th>
      <td>
        <strong class="research-compact-table__main">(3) 이상치</strong>
        <span class="research-compact-table__sub">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>babies 이상치 최빈값으로 채우기</td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

### 데이터 불러오고 확인하기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 4기/공유폴더/Data/hotel_data_modified.csv')
df
```

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

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

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

### (3) 이상치

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# babies 이상치 최빈값으로 채우기
most_common_babies = df['babies'].mode()[0]
df.loc[df['babies'] > 8, 'babies'] = most_common_babies
```

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
