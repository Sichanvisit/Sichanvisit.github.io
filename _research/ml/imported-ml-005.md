---
title: "7.DF 마스터하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250814_코드실습5_7.DF 마스터하기"
source_path: "11_Machine_Learning/Code_Snippets/250814_코드실습5_7.DF 마스터하기.md"
excerpt: "7.DF 마스터하기의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 확인, 데이터 다듬기, 문자 데이터 가공 순서로 큰 장을 먼저 훑고, 예측 결과 저장, datetime 파생 변수 생성 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipy..."
research_summary: "7.DF 마스터하기의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 확인, 데이터 다듬기, 문자 데이터 가공 순서로 큰 장을 먼저 훑고, 예측 결과 저장, datetime 파생 변수 생성 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 83개 코드 블록, 69개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, seaborn, matplotlib입니다."
research_artifacts: "ipynb/md · 코드 83개 · 실행 69개"
code_block_count: 83
execution_block_count: 69
research_focus:
  - "df 기본기"
  - "데이터 전처리"
  - "loc"
research_stack:
  - "google"
  - "pandas"
  - "seaborn"
  - "matplotlib"
  - "numpy"
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
    <div class="research-overview__value">Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋) 출처: Tableau, Kaggle 등 데이터 시각화·분석 튜토리얼에 널리 사용. 미국 내 특정 기간 동안의 소매 판매 기...</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">데이터 확인 -&gt; df 기본기 -&gt; 데이터 다듬기 -&gt; 문자 데이터 가공 -&gt; 정규화/표준화</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">loc: 레이블기반 데이터 선택 - df.loc[행 레이블, 열 레이블] iloc: 위치(정수)기반 데이터 선택 - df.iloc[행 위치, 열 위치]</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">데이터 확인 · 데이터 다듬기 · 문자 데이터 가공 · 데이터 합치기</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">CSV 데이터 불러오기 -&gt; 데이터 전처리 -&gt; 결측치 정리</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 83 · 실행 69</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">google, pandas, seaborn, matplotlib 외 1</div>
  </div>
</div>

## 1. 데이터 확인

Sample Superstore 데이터 설명
(교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)

1. 개요

- 출처: Tableau, Kaggle 등 데이터 시각화·분석 튜토리얼에 널리 사용
- 미국 내 특정 기간 동안의 소매 판매 기록
- 주문(Order) 단위로 구성 — 각 주문에 대한 고객, 상품, 지역, 금액 등의 정보 포함
- 링크: https://www.kaggle.com/datasets/naveenkumar20bps1137/sample-superstore?resource=download
    - Kaggle의 링크와 동일한 데이터는 아니고, 수업을 위해서 일부 수정한 것

| 컬럼명               | 설명                        | 데이터 타입 예시                                          |
| ----------------- | ------------------------- | -------------------------------------------------- |
| **Order ID**      | 주문 고유 식별자                 | 문자열 (`CA-2016-152156`)                             |
| **Order Date**    | 주문일                       | 문자열(날짜 형식)                                         |
| **Ship Date**     | 배송일                       | 문자열(날짜 형식)                                         |
| **Ship Mode**     | 배송 방식                     | 범주형 (`Second Class`, `Standard Class` 등)           |
| **Customer ID**   | 고객 고유 식별자                 | 문자열                                                |
| **Segment**       | 고객 세그먼트                   | 범주형 (`Consumer`, `Corporate`, `Home Office`)       |
| **Country**       | 국가명 (대부분 `United States`) | 문자열                                                |
| **City**          | 도시명                       | 문자열                                                |
| **State**         | 주(State)                  | 문자열                                                |
| **Postal Code**   | 우편번호                      | 숫자 또는 문자열                                          |
| **Region**        | 지역 구분                     | 범주형 (`East`, `West`, `Central`, `South`)           |
| **Product ID**    | 상품 고유 식별자                 | 문자열                                                |
| **Category**      | 상품 대분류                    | 범주형 (`Furniture`, `Office Supplies`, `Technology`) |
| **Sub-Category**  | 상품 소분류                    | 범주형 (`Chairs`, `Binders`, `Phones` 등)              |
| **Product Name**  | 상품명                       | 문자열                                                |
| **Sales**         | 매출액                       | 수치형 (float)                                        |
| **Quantity**      | 수량                        | 정수형                                                |
| **Discount**      | 할인율                       | float (0.0 \~ 1.0)                                 |
| **Profit**        | 이익액                       | float (음수 가능 — 손실 발생 시)                            |

```python
# 드라이브 마운트 코드
from google.colab import drive
drive.mount('/content/drive')
```

```python
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/Sample_Superstor.csv')
df
```

```python
df.head(3)
```

```python
# 데이터의 컬럼별 정보 확인
df.info()
```

```python
df.shape()
```

```python
# 행과 열의 갯수 정보
df.shape
```

```python
# 기술 통계 요약
df.describe()
```

```python
# 컬럼명 확인
df.columns
```

```python
# 컬럼명 정리해서 보기
df.columns.tolist()
```

## 2. df 기본기

```python
# query() 인덱싱
df.query('Category=="Furniture" and Sales > 500')
```

```python
df
```

```python
df_q = df.query('Category=="Furniture" and Sales > 500')
df_q.head(3)
```

```python
# query()랑 같은 역할
df[(df['Category']=='Furniture') & (df['Sales']>500)]
```

### loc/iloc

- loc: 레이블기반 데이터 선택
    - df.loc[행 레이블, 열 레이블]

- iloc: 위치(정수)기반 데이터 선택
    - df.iloc[행 위치, 열 위치]

```python
# loc 예시
df.loc[df['Region'].isin(['West'])]
```

```python
# iloc 예시
df.iloc[:5, :3]
```

### 데이터 삭제

```python
# drop()
df.drop(index=0) # 0 행 삭제
#inplace=True
```

```python
df
```

```python
df.drop(columns=["Segment"]) # Segment 열 삭제
```

```python
# 위와 같은 코드
df_d = df.drop(df.columns[5], axis=1)
```

__.copy()__

```python
# copy 연습

df_test = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
```

```python
df_test
```

```python
df_view = df_test[["a"]]
df_view
```

```python
df_view["a"] = df_view["a"] + 10
print(df_test)
```

```python
# 오류 피하기
df_view = df_test[["a"]].copy()
df_view
```

```python
df_view["a"] = df_view["a"] + 10
print(df_test)
```

```python
# 데이터 삭제 - loc, iloc
df_2 = df.loc[df["Discount"]==0].copy()
df_2
```

```python
df.iloc[100:, :]
```

```python
# 데이터 내보내기
df_2.to_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/superstore_refined.csv", index=False)
```

## 데이터 다듬기

#### 데이터 전처리

```python
# 결측값 확인
df.isnull().sum()

# df.isna().sum()
```

```python
# 전체 결측치 비율 보기
df.isnull().mean().sort_values(ascending=False) * 100
```

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(4,3))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
plt.show()
```

```python
# 결측값 처리 예시 - 평균 대체
df['Sales']=df['Sales'].fillna(df['Sales'].mean())
df.isnull().sum()
```

```python
# 결측치 처리 예시 - 최빈값 (범주형 변수)
df['Category']=df['Category'].fillna(df['Category'].mode()[0])
df.isnull().sum()
```

```python
# 실습1 - Discount 어떻게 결측치를 처리하는 것이 좋을까?

df = df.drop(columns=['Discount'])
df.head(3)
```

```python
# 예외코드 - 모든 결측값 제거 (행 단위)
df.dropna()
```

```python
# 결측치 제거 잘 되었는지 시각화

plt.figure(figsize=(4,3))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
plt.show()
```

```python
# 중복값 확인
df[df.duplicated()]
```

```python
# 중복 행 갯수
print(df.duplicated().sum())
```

```python
# 중복값 처리
df = df.drop_duplicates()
```

```python
# 이상치 - IQR 단일 변수
import numpy as np

q1 = np.percentile(df['Quantity'],25)
q2 = np.percentile(df['Quantity'],50)
q3 = np.percentile(df['Quantity'],75)
iqr = q3 - q1

print("Q1: ", q1)
print("Q2: ", q2)
print("Q3: ", q3)
```

```python
# 박스 플롯 - 단일 변수 이상치 확인

plt.figure(figsize=(5,3))
plt.boxplot(df['Quantity'], vert=False)
plt.show()
```

```python
# 여러 변수 박스 플롯 그리기
v = ["Quantity", "Sales"]
df[v].plot(kind='box', subplots=True, layout=(1,2), figsize=(7,3))
plt.tight_layout()
plt.show()
```

```python
# 특정 데이터 타입의 컬럼만 확인
numerical_cols = df.select_dtypes(include="number").columns
numerical_cols
```

```python
# 여러 변수 박스플롯 그리기
selected_cols = ['Sales', 'Quantity', 'Profit']

plt.figure(figsize=(8,3))

for i, col in enumerate(selected_cols):
    plt.subplot(1, 3, i)
    plt.boxplot(df[col].dropna()) # .dropna(): 데이터에 결측치가 있다면 빼고 그려 (안정성을 위해서)
    plt.title(f'{col}')

plt.tight_layout()
plt.show()
```

```python
# IQR 이상치 지정
outliers = (df['Quantity'] < (q1 - 1.5*iqr)) | (df['Quantity'] > (q3 + 1.5*iqr))
```

```python
# 이상치 제거
df_no = df[~outliers] # ~: 제외한다
df_no
```

## 문자 데이터 가공

```python
# 대소문자 문자열 처리
df['city_lower'] = df['City'].str.lower()
df['city_upper'] = df['City'].str.upper()
```

```python
df.head(1)
```

```python
# 문자열 분리

name_split = df['Ship Mode'].str.split(' ', n=1, expand=True)
# n=1: ' '기준 한 번 나눈다// expand=True: 두 개의 새로운 컬럼(0, 1)
df['grade'] = name_split[0]
df['status'] = name_split[1]

df[['Ship Mode', 'grade', 'status']].head(2)
```

```python
# replace 문자 제거
df['order_id_refined'] = df['Order ID'].str.replace('-','')

df[['Order ID', 'order_id_refined']].head(2)
```

### 추가 - 컬럼명 변경

```python
# 컬럼명 변경 예시 - 컬럼명 하나만 변경하기

df.rename(columns={'Order ID':'order_id'}, inplace=True)
df.head(2)
```

```python
# 위와 같은 코드 - 딕셔너리 따로 지정
rename_dict = {
    'Order Date': 'order_date',
    'Ship Date': 'ship_date'
    }
df = df.rename(columns = rename_dict)
df.head(2)
```

```python
# 자동 컬럼명 정리

df.columns = df.columns.str.lower().str.replace(' ', '_')

df.head(1)
```

## 정규화/표준화

```python
# 1. 정규화 - MinMax

df['sales_norm'] = (df['sales'] - df['sales'].min())/(df['sales'].max() - df['sales'].min())
df[['sales', 'sales_norm']].head(2)
```

```python
# 위와 같은 코드
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['sales_norm'] = scaler.fit_transform(df[['sales']])
```

```python
# 표준화
df['profit_std'] = (df['profit']-df['profit'].mean())/df['profit'].std()

df[['profit','profit_std']].head(2)
```

```python
# 위와 같은 코드
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['profit_std'] = scaler.fit_transform(df[['profit']])
```

```python
# cut()
df['sales_bin'] = pd.cut(df['sales'], bins=4, labels=['very_low', 'low', 'high', 'very_high'])
df[['sales', 'sales_bin']].head(2)
```

```python
# apply()
df['state_length'] = df['state'].apply(len)
df[['state', 'state_length']].head(2)
```

```python
# 위 코드 람다 버전
df['state_length'] = df['state'].apply(lambda x: len(x))
```

```python
# 비교 - map함수
df['state_upper'] = df['state'].map(str.upper)
df[['state', 'state_upper']].head(2)
```

```python
region_map = {
    'East': 'East Region',
    'Central': 'Central Region',
    'West': 'West Region',
    'South': 'South Region'
}

df['region_long'] = df['region'].map(region_map)
df[['region', 'region_long']].head(2)
```

```python
# 날짜 : 문자열 -> datetime

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')
```

```python
df.info()
```

```python
# 날짜로 변환된 데이터 타입 기준 월, 요일 파생변수 생성

df['order_month'] = df['order_date'].dt.month
df['order_weekday'] = df['order_date'].dt.day_name()
df['order_year'] = df['order_date'].dt.year

df[['order_date', 'order_year', 'order_month', 'order_weekday']].head(2)
```

## 데이터 합치기

```python
data1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

data2 = pd.DataFrame({
    "id": [4, 5, 6],
    "name": ["David", "Ella", "Frank"]
})
```

```python
data1
```

```python
data2
```

```python
# concat(): 컬럼이 같은 구조인 데이터를 위아래로 붙이기
combined = pd.concat([data2, data1], ignore_index=True)
combined
```

```python
left = pd.DataFrame({
    "id": [1, 2, 3],
    "score": [90, 85, 88]
})

right = pd.DataFrame({
    "id": [2, 3, 4],
    "grade": ["B", "A", "C"]
})
```

```python
left
```

```python
right
```

```python
merged = pd.merge(left, right, on='id', how='inner') #on: 공통컬럼, 합치는 것에 대한 기준
merged
```

```python
merged_l = pd.merge(left, right, on='id', how='left') #on: 공통컬럼, 합치는 것에 대한 기준
merged_l
```

```python
merged_r = pd.merge(left, right, on='id', how='right') #on: 공통컬럼, 합치는 것에 대한 기준
merged_r
```

```python
merged_o = pd.merge(left, right, on='id', how='outer') #on: 공통컬럼, 합치는 것에 대한 기준
merged_o
```

```python
# join(): 인덱스 기준 병합

# 인덱스 설정
left_indexed = left.set_index('id')
right_indexed = right.set_index('id')
```

```python
left_indexed
```

```python
right_indexed
```

```python
joined = left_indexed.join(right_indexed, how='left')
joined
```

```python
# df - 카테고리별 매출 합계

df.groupby('category')['sales'].sum()
```

```python
# df - 카테고리별 매출&이익 집계

df.groupby('category')[['sales', 'profit']].sum()
```

```python
# df - 여러 집계 함수 적용
df.groupby('category')['sales'].agg(['sum', 'mean', 'max', 'min'])
```
