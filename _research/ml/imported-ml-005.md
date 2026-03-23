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

<!-- #region id="Kf6OImVpGwt2" -->
# 1. 데이터 확인
<!-- #endregion -->

<!-- #region id="LzfTzY72G2eR" -->
Sample Superstore 데이터 설명
(교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)

1. 개요

- 출처: Tableau, Kaggle 등 데이터 시각화·분석 튜토리얼에 널리 사용
- 미국 내 특정 기간 동안의 소매 판매 기록
- 주문(Order) 단위로 구성 — 각 주문에 대한 고객, 상품, 지역, 금액 등의 정보 포함
- 링크: https://www.kaggle.com/datasets/naveenkumar20bps1137/sample-superstore?resource=download
    - Kaggle의 링크와 동일한 데이터는 아니고, 수업을 위해서 일부 수정한 것
<!-- #endregion -->

<!-- #region id="Razo6fjfG-EI" -->
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
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="ManEvG2rGVUM" executionInfo={"status": "ok", "timestamp": 1755134517533, "user_tz": -540, "elapsed": 20331, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="613959e8-0265-4729-9787-b130db00d78c"
# 드라이브 마운트 코드
from google.colab import drive
drive.mount('/content/drive')
```

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="fS12otqGKvsT" executionInfo={"status": "ok", "timestamp": 1755144235458, "user_tz": -540, "elapsed": 201, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="919be6bf-e50c-4651-8ec7-17303eceebde"
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/Sample_Superstor.csv')
df
```

```python colab={"base_uri": "https://localhost:8080/", "height": 389} id="uUvbb54bLXY2" executionInfo={"status": "ok", "timestamp": 1755134673087, "user_tz": -540, "elapsed": 77, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a68838b3-2a42-4bf1-fb02-83e145c365f9"
df.head(3)
```

```python colab={"base_uri": "https://localhost:8080/"} id="UhUuEE8XLZxt" executionInfo={"status": "ok", "timestamp": 1755134700542, "user_tz": -540, "elapsed": 48, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="20e9893f-f2a7-4cd7-d8df-ecc5265eb4a4"
# 데이터의 컬럼별 정보 확인
df.info()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 145} id="Zduv9N6JLiq7" executionInfo={"status": "error", "timestamp": 1755134841931, "user_tz": -540, "elapsed": 80, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ebed1eb9-7da8-45f0-d5bc-032b5eb1c5c7"
df.shape()
```

```python colab={"base_uri": "https://localhost:8080/"} id="L7m-YqIjMFLo" executionInfo={"status": "ok", "timestamp": 1755134873298, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="19cec0f1-d9a5-40d4-d081-a50c8afdc510"
# 행과 열의 갯수 정보
df.shape
```

```python colab={"base_uri": "https://localhost:8080/", "height": 300} id="u_p3sK1zMMc_" executionInfo={"status": "ok", "timestamp": 1755135333922, "user_tz": -540, "elapsed": 43, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="302e8661-4a19-4767-db97-79d8e11a057a"
# 기술 통계 요약
df.describe()
```

```python colab={"base_uri": "https://localhost:8080/"} id="U5cWFOjPMszw" executionInfo={"status": "ok", "timestamp": 1755135383888, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="cf926027-0a54-4e09-ca8f-a613e01a203b"
# 컬럼명 확인
df.columns
```

```python colab={"base_uri": "https://localhost:8080/"} id="ElgYzwBiOH73" executionInfo={"status": "ok", "timestamp": 1755135435526, "user_tz": -540, "elapsed": 13, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5c0353ec-f388-44f2-afaa-592e8243d8ec"
# 컬럼명 정리해서 보기
df.columns.tolist()
```

<!-- #region id="gsG33J2sOaB7" -->
# 2. df 기본기
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="_0ax0zn0OKye" executionInfo={"status": "ok", "timestamp": 1755135647962, "user_tz": -540, "elapsed": 112, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2d111c9d-4617-4904-a48d-60f150baefa9"
# query() 인덱싱
df.query('Category=="Furniture" and Sales > 500')
```

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="ZLerZqZmPBd3" executionInfo={"status": "ok", "timestamp": 1755135665471, "user_tz": -540, "elapsed": 76, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b769f640-203e-4ebf-dcff-8c497bce766c"
df
```

```python colab={"base_uri": "https://localhost:8080/", "height": 371} id="QQn8XKybPOPf" executionInfo={"status": "ok", "timestamp": 1755135710475, "user_tz": -540, "elapsed": 73, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3f366ddd-07fd-4db8-cbfa-7f8f139fe075"
df_q = df.query('Category=="Furniture" and Sales > 500')
df_q.head(3)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="GpJClYvmPZO_" executionInfo={"status": "ok", "timestamp": 1755135913200, "user_tz": -540, "elapsed": 54, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="0d49c485-2fc1-4399-b4ab-7bafb9f1b7c7"
# query()랑 같은 역할
df[(df['Category']=='Furniture') & (df['Sales']>500)]
```

<!-- #region id="JI4Adp6HQ6BY" -->
### loc/iloc

- loc: 레이블기반 데이터 선택
    - df.loc[행 레이블, 열 레이블]

- iloc: 위치(정수)기반 데이터 선택
    - df.iloc[행 위치, 열 위치]
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="o3Xo6f9XPzAz" executionInfo={"status": "ok", "timestamp": 1755137782675, "user_tz": -540, "elapsed": 78, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4ff106ba-a8ec-402e-b9bb-1548e70a8648"
# loc 예시
df.loc[df['Region'].isin(['West'])]
```

```python colab={"base_uri": "https://localhost:8080/", "height": 206} id="6tjVBI1FUp9z" executionInfo={"status": "ok", "timestamp": 1755137818637, "user_tz": -540, "elapsed": 25, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="39f07702-8179-4de3-eaea-dc2bedf1c838"
# iloc 예시
df.iloc[:5, :3]
```

<!-- #region id="uXvRa3CCXpTQ" -->
### 데이터 삭제
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="Mkt6hL9jV4Ua" executionInfo={"status": "ok", "timestamp": 1755137917529, "user_tz": -540, "elapsed": 97, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a1e79cef-f7e3-4a4e-b425-ed43ab7e66db"
# drop()
df.drop(index=0) # 0 행 삭제
#inplace=True
```

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="8IPVjNzjX0Dj" executionInfo={"status": "ok", "timestamp": 1755137938493, "user_tz": -540, "elapsed": 117, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="44397370-4aa3-40f0-c12a-d5b146f504f5"
df
```

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="6aWBlzJSX5K2" executionInfo={"status": "ok", "timestamp": 1755138095068, "user_tz": -540, "elapsed": 76, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="98bf58ef-8fdf-487f-b0be-9903c311d0ed"
df.drop(columns=["Segment"]) # Segment 열 삭제
```

```python id="KXBY-vtTYfN_"
# 위와 같은 코드
df_d = df.drop(df.columns[5], axis=1)
```

<!-- #region id="TTh9fwudYyyT" -->
__.copy()__


<!-- #endregion -->

```python id="AZCtHmJjYv58"
# copy 연습

df_test = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="wJb2VRfWZebQ" executionInfo={"status": "ok", "timestamp": 1755138360061, "user_tz": -540, "elapsed": 39, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="53dddecf-77a5-4af8-afb7-d3fdfc8ea859"
df_test
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="P-aMH8ybZgG9" executionInfo={"status": "ok", "timestamp": 1755138381297, "user_tz": -540, "elapsed": 44, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="01c7dd1b-a99a-4bd4-ba2b-2b4320f4c17a"
df_view = df_test[["a"]]
df_view
```

```python colab={"base_uri": "https://localhost:8080/"} id="pQlOXnPbZkmt" executionInfo={"status": "ok", "timestamp": 1755138407902, "user_tz": -540, "elapsed": 55, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7862c81b-1b50-4440-b385-99578beb1311"
df_view["a"] = df_view["a"] + 10
print(df_test)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="FC80S5xyZ3vh" executionInfo={"status": "ok", "timestamp": 1755138472180, "user_tz": -540, "elapsed": 50, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9817a538-09f7-4411-bdc2-c90ceb6b44d2"
# 오류 피하기
df_view = df_test[["a"]].copy()
df_view
```

```python colab={"base_uri": "https://localhost:8080/"} id="NLab77-DZ3s6" executionInfo={"status": "ok", "timestamp": 1755138478444, "user_tz": -540, "elapsed": 28, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4742a071-4c1d-45de-d9a0-c41664a44e0d"
df_view["a"] = df_view["a"] + 10
print(df_test)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 947} id="i98oAac0Z9A-" executionInfo={"status": "ok", "timestamp": 1755138600649, "user_tz": -540, "elapsed": 73, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="55d7e1c6-2459-4fd8-c383-279cef534c09"
# 데이터 삭제 - loc, iloc
df_2 = df.loc[df["Discount"]==0].copy()
df_2
```

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="nB-hmNIEaa09" executionInfo={"status": "ok", "timestamp": 1755138628423, "user_tz": -540, "elapsed": 97, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="246fdbc2-337c-4a8c-b84c-7d7c6f9f19d2"
df.iloc[100:, :]
```

```python id="3FThLHOnalT9"
# 데이터 내보내기
df_2.to_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/superstore_refined.csv", index=False)
```

<!-- #region id="NwJ4NIKqba8M" -->
# 데이터 다듬기
<!-- #endregion -->

<!-- #region id="fug4Tffobdbk" -->
#### 데이터 전처리
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="Bbouw82palRC" executionInfo={"status": "ok", "timestamp": 1755144708745, "user_tz": -540, "elapsed": 71, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="aad490b6-0c06-42ba-8410-f1cd300f6d8f"
# 결측값 확인
df.isnull().sum()

# df.isna().sum()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="7KVOyOivalOM" executionInfo={"status": "ok", "timestamp": 1755144843662, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c04dde77-3821-4beb-e5e1-0446f72aadd8"
# 전체 결측치 비율 보기
df.isnull().mean().sort_values(ascending=False) * 100
```

```python colab={"base_uri": "https://localhost:8080/", "height": 375} id="WZtXxf7ualLB" executionInfo={"status": "ok", "timestamp": 1755145012858, "user_tz": -540, "elapsed": 443, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fa3a8702-3cb8-4c14-efbd-c44787d334b7"
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(4,3))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="fN8Ra7kmy0A-" executionInfo={"status": "ok", "timestamp": 1755145225931, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="0add2367-aab6-47ab-eac4-7476fc532e40"
# 결측값 처리 예시 - 평균 대체
df['Sales']=df['Sales'].fillna(df['Sales'].mean())
df.isnull().sum()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 617} id="wKStKcWDzM-C" executionInfo={"status": "ok", "timestamp": 1755145411201, "user_tz": -540, "elapsed": 66, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="8b29b530-736d-4125-c2b7-b420044a9e35"
# 결측치 처리 예시 - 최빈값 (범주형 변수)
df['Category']=df['Category'].fillna(df['Category'].mode()[0])
df.isnull().sum()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 389} id="br56Yu1S0Ttv" executionInfo={"status": "ok", "timestamp": 1755145591363, "user_tz": -540, "elapsed": 124, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5f344c9c-6df0-4834-c6ff-a3138b2ca601"
# 실습1 - Discount 어떻게 결측치를 처리하는 것이 좋을까?

df = df.drop(columns=['Discount'])
df.head(3)
```

```python id="Q2e5ALzX1FiJ"
# 예외코드 - 모든 결측값 제거 (행 단위)
df.dropna()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 375} id="5VGjDrah1g38" executionInfo={"status": "ok", "timestamp": 1755145759521, "user_tz": -540, "elapsed": 341, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4b5981af-e2f7-4e0b-805c-92f183aeb622"
# 결측치 제거 잘 되었는지 시각화

plt.figure(figsize=(4,3))
sns.heatmap(df.isnull(), cbar=False, yticklabels=False)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 204} id="apuCDH_91wz8" executionInfo={"status": "ok", "timestamp": 1755145803944, "user_tz": -540, "elapsed": 76, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5d68e46f-af31-4925-8e75-a2b4c6ef7170"
# 중복값 확인
df[df.duplicated()]
```

```python colab={"base_uri": "https://localhost:8080/"} id="bMtKEHPu15dJ" executionInfo={"status": "ok", "timestamp": 1755145915835, "user_tz": -540, "elapsed": 104, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e8561c5a-9f5e-4a77-df96-d59b5c3a668b"
# 중복 행 갯수
print(df.duplicated().sum())
```

```python id="YQSJiWuu2Suu"
# 중복값 처리
df = df.drop_duplicates()
```

```python colab={"base_uri": "https://localhost:8080/"} id="YAzG6BSO2eAd" executionInfo={"status": "ok", "timestamp": 1755146181238, "user_tz": -540, "elapsed": 58, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="8e203487-27ad-4271-f6e1-1dc2978d6974"
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

```python colab={"base_uri": "https://localhost:8080/", "height": 291} id="pM7ygS0M3VkI" executionInfo={"status": "ok", "timestamp": 1755146240900, "user_tz": -540, "elapsed": 101, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7ff652a7-2fbe-4de0-e579-b852bba8861c"
# 박스 플롯 - 단일 변수 이상치 확인

plt.figure(figsize=(5,3))
plt.boxplot(df['Quantity'], vert=False)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 307} id="ny-ryUrB3jgd" executionInfo={"status": "ok", "timestamp": 1755146492992, "user_tz": -540, "elapsed": 366, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="61df2e75-481c-4ed2-f5e3-7e81c6df4967"
# 여러 변수 박스 플롯 그리기
v = ["Quantity", "Sales"]
df[v].plot(kind='box', subplots=True, layout=(1,2), figsize=(7,3))
plt.tight_layout()
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/"} id="1VxmoB3K4hm0" executionInfo={"status": "ok", "timestamp": 1755146605855, "user_tz": -540, "elapsed": 26, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="78f03914-e6ff-4cf0-98a6-5cb09dce955b"
# 특정 데이터 타입의 컬럼만 확인
numerical_cols = df.select_dtypes(include="number").columns
numerical_cols
```

```python colab={"base_uri": "https://localhost:8080/", "height": 307} id="XcXhyEWZ47tB" executionInfo={"status": "ok", "timestamp": 1755146903952, "user_tz": -540, "elapsed": 656, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="79515aee-21a8-431f-b453-b17396c75b09"
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

```python id="bD3EwXbf6CFE"
# IQR 이상치 지정
outliers = (df['Quantity'] < (q1 - 1.5*iqr)) | (df['Quantity'] > (q3 + 1.5*iqr))
```

```python colab={"base_uri": "https://localhost:8080/", "height": 1000} id="zr59FAB19mI7" executionInfo={"status": "ok", "timestamp": 1755147869601, "user_tz": -540, "elapsed": 145, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="69a114e5-29b2-4e57-c54e-ea5b5d14e3c0"
# 이상치 제거
df_no = df[~outliers] # ~: 제외한다
df_no
```

<!-- #region id="jEaTk5X399U5" -->
# 문자 데이터 가공
<!-- #endregion -->

```python id="Se8T7GUW9xvU"
# 대소문자 문자열 처리
df['city_lower'] = df['City'].str.lower()
df['city_upper'] = df['City'].str.upper()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 170} id="B5d-WgBs-HWk" executionInfo={"status": "ok", "timestamp": 1755148027197, "user_tz": -540, "elapsed": 186, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="8fe16037-dc03-479b-84df-320b27cd6231"
df.head(1)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="4JezO6HN-YMh" executionInfo={"status": "ok", "timestamp": 1755148520299, "user_tz": -540, "elapsed": 62, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5b12968f-30f3-4e98-cbcc-94f46915ab1f"
# 문자열 분리

name_split = df['Ship Mode'].str.split(' ', n=1, expand=True)
# n=1: ' '기준 한 번 나눈다// expand=True: 두 개의 새로운 컬럼(0, 1)
df['grade'] = name_split[0]
df['status'] = name_split[1]

df[['Ship Mode', 'grade', 'status']].head(2)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="RGI1Q_O0Aa26" executionInfo={"status": "ok", "timestamp": 1755148814897, "user_tz": -540, "elapsed": 39, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4e57e7b9-f0b9-4bad-e9d6-93385bc948d1"
# replace 문자 제거
df['order_id_refined'] = df['Order ID'].str.replace('-','')

df[['Order ID', 'order_id_refined']].head(2)
```

<!-- #region id="2etP6IfSBowz" -->
### 추가 - 컬럼명 변경
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 300} id="SIXBesMaBYjQ" executionInfo={"status": "ok", "timestamp": 1755149010851, "user_tz": -540, "elapsed": 41, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="0373015b-29a9-4473-da34-995973b1ad9c"
# 컬럼명 변경 예시 - 컬럼명 하나만 변경하기

df.rename(columns={'Order ID':'order_id'}, inplace=True)
df.head(2)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 300} id="c81XGLEiCIX4" executionInfo={"status": "ok", "timestamp": 1755149169935, "user_tz": -540, "elapsed": 120, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7940c4f8-29bf-4cf5-d7f0-c989d9e400ad"
# 위와 같은 코드 - 딕셔너리 따로 지정
rename_dict = {
    'Order Date': 'order_date',
    'Ship Date': 'ship_date'
    }
df = df.rename(columns = rename_dict)
df.head(2)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 199} id="17h8DswlCvNP" executionInfo={"status": "ok", "timestamp": 1755149311039, "user_tz": -540, "elapsed": 68, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="60ca8937-f32d-42e5-c861-1221f18b260e"
# 자동 컬럼명 정리

df.columns = df.columns.str.lower().str.replace(' ', '_')

df.head(1)
```

<!-- #region id="5LRym2RXDqGq" -->
# 정규화/표준화
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="SD08YQECDRp4" executionInfo={"status": "ok", "timestamp": 1755150204956, "user_tz": -540, "elapsed": 71, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="540925c2-419f-4930-e6d8-725fb95fa6c8"
# 1. 정규화 - MinMax

df['sales_norm'] = (df['sales'] - df['sales'].min())/(df['sales'].max() - df['sales'].min())
df[['sales', 'sales_norm']].head(2)
```

```python id="YMFgjhy1GkJG"
# 위와 같은 코드
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['sales_norm'] = scaler.fit_transform(df[['sales']])
```

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="IW-dxhoJIDsx" executionInfo={"status": "ok", "timestamp": 1755151564918, "user_tz": -540, "elapsed": 54, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="58a46bd7-6858-4372-d5b0-2309ca3a1d68"
# 표준화
df['profit_std'] = (df['profit']-df['profit'].mean())/df['profit'].std()

df[['profit','profit_std']].head(2)
```

```python id="iUozH15wMBil"
# 위와 같은 코드
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['profit_std'] = scaler.fit_transform(df[['profit']])
```

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="-PlcWHkXMBQJ" executionInfo={"status": "ok", "timestamp": 1755152000334, "user_tz": -540, "elapsed": 53, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="dc0e134f-ea44-455f-e53f-81399d0089fd"
# cut()
df['sales_bin'] = pd.cut(df['sales'], bins=4, labels=['very_low', 'low', 'high', 'very_high'])
df[['sales', 'sales_bin']].head(2)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="CqJDlCvSL6YG" executionInfo={"status": "ok", "timestamp": 1755152211850, "user_tz": -540, "elapsed": 58, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3e9acdd5-1754-4ee2-eae3-bb0c4397757c"
# apply()
df['state_length'] = df['state'].apply(len)
df[['state', 'state_length']].head(2)
```

```python id="vvVcwDXfObBK"
# 위 코드 람다 버전
df['state_length'] = df['state'].apply(lambda x: len(x))
```

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="x_b3ky7KOgNz" executionInfo={"status": "ok", "timestamp": 1755152388706, "user_tz": -540, "elapsed": 57, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ef7d56ff-9b2c-4f93-8d5c-abd959134346"
# 비교 - map함수
df['state_upper'] = df['state'].map(str.upper)
df[['state', 'state_upper']].head(2)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="i7URrIgvOgKm" executionInfo={"status": "ok", "timestamp": 1755152573361, "user_tz": -540, "elapsed": 99, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e355198d-b08a-4159-e8a1-145b5765234d"
region_map = {
    'East': 'East Region',
    'Central': 'Central Region',
    'West': 'West Region',
    'South': 'South Region'
}

df['region_long'] = df['region'].map(region_map)
df[['region', 'region_long']].head(2)
```

```python id="Gx9ZX0ylPIQ8"
# 날짜 : 문자열 -> datetime

df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')
```

```python colab={"base_uri": "https://localhost:8080/"} id="WodF1m4GQBoC" executionInfo={"status": "ok", "timestamp": 1755152750580, "user_tz": -540, "elapsed": 90, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="eeecf2c8-b043-4c44-9a22-8c7972ca1153"
df.info()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 112} id="AmFK9Dk1QZYS" executionInfo={"status": "ok", "timestamp": 1755152913245, "user_tz": -540, "elapsed": 79, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="15047724-8dee-4f9e-afff-3ff8b9588c51"
# 날짜로 변환된 데이터 타입 기준 월, 요일 파생변수 생성

df['order_month'] = df['order_date'].dt.month
df['order_weekday'] = df['order_date'].dt.day_name()
df['order_year'] = df['order_date'].dt.year

df[['order_date', 'order_year', 'order_month', 'order_weekday']].head(2)
```

<!-- #region id="bUwTod_YRH-l" -->
# 데이터 합치기
<!-- #endregion -->

```python id="QKCInCJRRBGx"
data1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

data2 = pd.DataFrame({
    "id": [4, 5, 6],
    "name": ["David", "Ella", "Frank"]
})
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="XxskQDV8RPd2" executionInfo={"status": "ok", "timestamp": 1755152977144, "user_tz": -540, "elapsed": 72, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3b6567e2-c285-4844-ba14-4c1fdc143d0c"
data1
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="AwD6KgG1RQtz" executionInfo={"status": "ok", "timestamp": 1755152987619, "user_tz": -540, "elapsed": 46, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a98931f3-a3ef-4be2-df7e-61435f6d1f36"
data2
```

```python colab={"base_uri": "https://localhost:8080/", "height": 237} id="gyOA6GRTRTPq" executionInfo={"status": "ok", "timestamp": 1755153111446, "user_tz": -540, "elapsed": 55, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fec426a8-0017-46c3-b22d-342976edf378"
# concat(): 컬럼이 같은 구조인 데이터를 위아래로 붙이기
combined = pd.concat([data2, data1], ignore_index=True)
combined
```

```python id="pshDeLENR3Hy"
left = pd.DataFrame({
    "id": [1, 2, 3],
    "score": [90, 85, 88]
})

right = pd.DataFrame({
    "id": [2, 3, 4],
    "grade": ["B", "A", "C"]
})
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="1c8_B1eXR3po" executionInfo={"status": "ok", "timestamp": 1755153147925, "user_tz": -540, "elapsed": 57, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="0beabd64-4379-4c3f-9617-ff1a42508e51"
left
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="l1Z9MMR1R6Y6" executionInfo={"status": "ok", "timestamp": 1755153160384, "user_tz": -540, "elapsed": 62, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="40a6d7da-57f7-4aac-9c22-a4512c89b6d8"
right
```

```python colab={"base_uri": "https://localhost:8080/", "height": 125} id="z17UIg9KR9bU" executionInfo={"status": "ok", "timestamp": 1755153339294, "user_tz": -540, "elapsed": 90, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bde5e293-3003-48aa-cd70-d591b0bd4445"
merged = pd.merge(left, right, on='id', how='inner') #on: 공통컬럼, 합치는 것에 대한 기준
merged
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="aMkgFDe9SvzG" executionInfo={"status": "ok", "timestamp": 1755153452062, "user_tz": -540, "elapsed": 84, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="49675df3-5728-418e-801e-61aca323db00"
merged_l = pd.merge(left, right, on='id', how='left') #on: 공통컬럼, 합치는 것에 대한 기준
merged_l
```

```python colab={"base_uri": "https://localhost:8080/", "height": 143} id="REcnbz1NTEpn" executionInfo={"status": "ok", "timestamp": 1755153468330, "user_tz": -540, "elapsed": 44, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d7ed1393-6ecc-4ad1-87f3-e3de21aeb792"
merged_r = pd.merge(left, right, on='id', how='right') #on: 공통컬럼, 합치는 것에 대한 기준
merged_r
```

```python colab={"base_uri": "https://localhost:8080/", "height": 174} id="jcS1oGE6TInb" executionInfo={"status": "ok", "timestamp": 1755153501350, "user_tz": -540, "elapsed": 114, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="47c20b40-b41d-49d0-f042-ab81d341d0cc"
merged_o = pd.merge(left, right, on='id', how='outer') #on: 공통컬럼, 합치는 것에 대한 기준
merged_o
```

```python id="P1Qc7aOyTVL7"
# join(): 인덱스 기준 병합

# 인덱스 설정
left_indexed = left.set_index('id')
right_indexed = right.set_index('id')
```

```python colab={"base_uri": "https://localhost:8080/", "height": 174} id="oG--Gt8hTkAK" executionInfo={"status": "ok", "timestamp": 1755153581848, "user_tz": -540, "elapsed": 91, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d8de534c-6da8-4d50-e61a-f9052f981c6b"
left_indexed
```

```python colab={"base_uri": "https://localhost:8080/", "height": 174} id="j9qWI6pbTkVg" executionInfo={"status": "ok", "timestamp": 1755153601512, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a105d599-638d-4485-8dad-e3bd34f6cd7d"
right_indexed
```

```python colab={"base_uri": "https://localhost:8080/", "height": 174} id="LDn33z_fTpJr" executionInfo={"status": "ok", "timestamp": 1755153635935, "user_tz": -540, "elapsed": 62, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a1136dc5-a1ec-4137-a5c2-7a36f72eb4dd"
joined = left_indexed.join(right_indexed, how='left')
joined
```

```python colab={"base_uri": "https://localhost:8080/", "height": 209} id="BfFeO1_NTw-3" executionInfo={"status": "ok", "timestamp": 1755153729807, "user_tz": -540, "elapsed": 123, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="77878f7e-3429-461c-cf95-b2a5d7b5f9e9"
# df - 카테고리별 매출 합계

df.groupby('category')['sales'].sum()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 174} id="m_wxHd3LUIdU" executionInfo={"status": "ok", "timestamp": 1755153819795, "user_tz": -540, "elapsed": 78, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bd9a7b1a-324f-4bc1-8e31-1f2073073076"
# df - 카테고리별 매출&이익 집계

df.groupby('category')[['sales', 'profit']].sum()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 174} id="rHG8IYdLUebl" executionInfo={"status": "ok", "timestamp": 1755153899318, "user_tz": -540, "elapsed": 33, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c7d1ce3a-3a93-4b62-df59-36374f283fac"
# df - 여러 집계 함수 적용
df.groupby('category')['sales'].agg(['sum', 'mean', 'max', 'min'])
```
