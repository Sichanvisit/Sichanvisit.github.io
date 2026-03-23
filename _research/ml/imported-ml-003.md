---
title: "4.데이터사이언스 Toolkit"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250812_코드실습3_4.데이터사이언스 Toolkit"
source_path: "11_Machine_Learning/Code_Snippets/250812_코드실습3_4.데이터사이언스 Toolkit.md"
excerpt: "4.데이터사이언스 Toolkit의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 마크다운 실습, Numpy 실습, 판다스 실습 순서로 큰 장을 먼저 훑고, CSV 데이터 불러오기, 데이터 분포 시각화 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `..."
research_summary: "4.데이터사이언스 Toolkit의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 마크다운 실습, Numpy 실습, 판다스 실습 순서로 큰 장을 먼저 훑고, CSV 데이터 불러오기, 데이터 분포 시각화 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 60개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, google, pandas, matplotlib입니다."
research_artifacts: "ipynb/md · 코드 60개 · 실행 59개"
code_block_count: 60
execution_block_count: 59
research_focus:
  - "matplotlib 실습"
  - "마크다운으로 매일 학습 기록을 남기는 습관 만들기!"
  - "나의 목표"
research_stack:
  - "numpy"
  - "google"
  - "pandas"
  - "matplotlib"
  - "warnings"
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
    <div class="research-overview__value">마크다운으로 매일 학습 기록을 남기는 습관 만들기!</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">마크다운 실습 -&gt; Numpy 실습 -&gt; 판다스 실습 -&gt; matplotlib 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">csv파일 불러오는 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">마크다운 실습 · Numpy 실습 · 판다스 실습 · matplotlib 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">CSV 데이터 불러오기 -&gt; 데이터 분포 시각화</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 60 · 실행 59</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">numpy, google, pandas, matplotlib 외 1</div>
  </div>
</div>

<!-- #region id="h1v8Z5usq7p_" -->
# 1. 마크다운 실습
<!-- #endregion -->

<!-- #region id="BDIkeatBrASE" -->
## **자기소개 마크다운 미션**


### 이름

조하나

### 요즘 배우는 것

- 파이썬 기초 문법
- 마크다운 정리법
- 데이터 시각화
- AI 엔지니어링

### 나의 목표

> 마크다운으로 매일 학습 기록을 남기는 습관 만들기!

----------------------
----------------------
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="6AacqC2iqz2T" executionInfo={"status": "ok", "timestamp": 1754962662112, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6e4c40d1-842c-4019-82b2-b0ad8b5fa62d"
import numpy as np

arr = np.array([[2, 3, 4,], [5, 6, 7]])

arr
```

```python colab={"base_uri": "https://localhost:8080/"} id="msvMgfCN6-qe" executionInfo={"status": "ok", "timestamp": 1754962664682, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="15e18395-a22e-4bd3-f4b0-1b7810e6aea6"
arr[:,0]
```

```python colab={"base_uri": "https://localhost:8080/"} id="y5BAiHb97GQr" executionInfo={"status": "ok", "timestamp": 1754962791531, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ef92f7b4-469e-4871-9b7f-a949344f0847"
arr[1,0]
```

```python colab={"base_uri": "https://localhost:8080/"} id="CEuwX14w7Ujm" executionInfo={"status": "ok", "timestamp": 1754962696524, "user_tz": -540, "elapsed": 20, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fe93664f-fa3a-44dc-a16a-9f0084c4c644"
arr[1, 0:2]
```

```python colab={"base_uri": "https://localhost:8080/"} id="VUkO87_U-dW5" executionInfo={"status": "ok", "timestamp": 1754963506579, "user_tz": -540, "elapsed": 38, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="1ab86bf6-1f41-4d97-aee4-8ff34f6feae1"
arr[0:0,:]
```

<!-- #region id="cmYqpth59aSG" -->
# 2. Numpy 실습
<!-- #endregion -->

<!-- #region id="oyLyTVT99gpO" -->
### 기본 함수들
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="2vNYh9xs7Zhc" executionInfo={"status": "ok", "timestamp": 1754964190038, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ab2d97e7-60dd-4fdf-f8e8-56e1038a3c05"
# np.array(): 넘파이 배열로 바꿔주는 함수

import numpy as np

arr = np.array([1,3,5,7,9])
arr
```

```python colab={"base_uri": "https://localhost:8080/"} id="h0p-VCa1BGJc" executionInfo={"status": "ok", "timestamp": 1754964326500, "user_tz": -540, "elapsed": 20, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="000187d1-9263-4c06-e9b1-a7697c200e12"
# np.arange()

arr = np.arange(10)
print(arr)
```

```python colab={"base_uri": "https://localhost:8080/"} id="rVkT4KWKBneE" executionInfo={"status": "ok", "timestamp": 1754964439271, "user_tz": -540, "elapsed": 21, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="038d1659-b7f2-4828-fca1-5840ec846cab"
# 2씩 텀 주기
np.arange(3, 10, 2)
```

```python colab={"base_uri": "https://localhost:8080/"} id="rNOcqtF2CDAZ" executionInfo={"status": "ok", "timestamp": 1754964496909, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b8c08dde-78a7-418e-9025-c4c2fe6f5824"
# np.zeros()
np.zeros((2,3))
```

```python id="Z0VEZ-bdCREf" executionInfo={"status": "ok", "timestamp": 1754964814661, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 1차원 배열 인덱싱

arr_ex1 = np.array([1,2,3,4,5,6,7,8,9])
```

```python colab={"base_uri": "https://localhost:8080/"} id="vsr5eIyBDep1" executionInfo={"status": "ok", "timestamp": 1754964859971, "user_tz": -540, "elapsed": 21, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="77fa436c-9cb2-447f-b793-185634246891"
print(arr_ex1[2])
```

```python colab={"base_uri": "https://localhost:8080/"} id="jpj5jDqJDl7I" executionInfo={"status": "ok", "timestamp": 1754964885902, "user_tz": -540, "elapsed": 20, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fc4c055a-a89d-4667-80aa-9b4638e99db0"
arr_ex1[-3]
```

```python colab={"base_uri": "https://localhost:8080/"} id="JPovmPzxDwCX" executionInfo={"status": "ok", "timestamp": 1754964934088, "user_tz": -540, "elapsed": 42, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="cce7e604-ddfd-463f-df66-14b9795f46d8"
arr_ex1[2:6]
```

```python id="v2MurBg4D8Xq" executionInfo={"status": "ok", "timestamp": 1754964970327, "user_tz": -540, "elapsed": 44, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 2차원 인덱싱

arr_ex2 = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
```

```python colab={"base_uri": "https://localhost:8080/"} id="Zgjx9GyMEEpA" executionInfo={"status": "ok", "timestamp": 1754965004062, "user_tz": -540, "elapsed": 24, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5c75c61b-d8c2-493e-e2df-cf39221890c1"
arr_ex2[0,1]
```

```python colab={"base_uri": "https://localhost:8080/"} id="vZvFAbaAEM4w" executionInfo={"status": "ok", "timestamp": 1754965052368, "user_tz": -540, "elapsed": 60, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a81a39d5-c2e8-4700-e999-e26c901351dc"
# 두번째 행 출력
arr_ex2[1,:]
```

```python colab={"base_uri": "https://localhost:8080/"} id="mo64Pwl1Ea8H" executionInfo={"status": "ok", "timestamp": 1754965191336, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="45a82732-68ce-4016-9392-e66195a4aa05"
# 세번째 열 출력
arr_ex2[:,2]
```

```python colab={"base_uri": "https://localhost:8080/"} id="YZ9hw1_WE6m9" executionInfo={"status": "ok", "timestamp": 1754965242506, "user_tz": -540, "elapsed": 24, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4966dde7-41a6-4230-ad73-3efb22e94a2b"
# 0~1행, 1~2열 부분 배열
arr_ex2[0:2, 1:3]
```

```python colab={"base_uri": "https://localhost:8080/"} id="1OpAO4tXFHGg" executionInfo={"status": "ok", "timestamp": 1754965274171, "user_tz": -540, "elapsed": 39, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="60aff46c-89c4-4921-aebb-7cf4cb433772"
arr_ex1
```

```python colab={"base_uri": "https://localhost:8080/"} id="nUOmnr86FO0x" executionInfo={"status": "ok", "timestamp": 1754965276515, "user_tz": -540, "elapsed": 26, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="94ec142f-5ebd-4e2f-d4fb-c3d367023523"
arr_ex2
```

```python colab={"base_uri": "https://localhost:8080/"} id="HOxfbCw7FPZv" executionInfo={"status": "ok", "timestamp": 1754965304144, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f2d1d0be-065b-43d7-8264-e1f251537db6"
arr_ex1.min()
```

```python colab={"base_uri": "https://localhost:8080/"} id="-wAG9pcTFWIz" executionInfo={"status": "ok", "timestamp": 1754965316174, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6186b09b-2028-4932-f765-9fbf1aa16caf"
arr_ex1.max()
```

```python colab={"base_uri": "https://localhost:8080/"} id="_dbhePxpFZFr" executionInfo={"status": "ok", "timestamp": 1754965338588, "user_tz": -540, "elapsed": 11, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="25ce8232-adf0-454e-d092-121f7f666984"
arr_ex2.max()
```

```python colab={"base_uri": "https://localhost:8080/"} id="PfcxrD1lFeis" executionInfo={"status": "ok", "timestamp": 1754965352711, "user_tz": -540, "elapsed": 32, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="81483ca5-de1b-41b3-ad54-c63045559c5b"
arr_ex1.mean()
```

```python colab={"base_uri": "https://localhost:8080/"} id="DohT2GU4FiAL" executionInfo={"status": "ok", "timestamp": 1754965379475, "user_tz": -540, "elapsed": 37, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bedf56f2-87e2-450e-b7c7-e84526706243"
arr_ex2.mean()
```

```python colab={"base_uri": "https://localhost:8080/"} id="9alClM77Foic" executionInfo={"status": "ok", "timestamp": 1754965429658, "user_tz": -540, "elapsed": 42, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c4ea3844-ac01-4836-b515-7bb4ed02d589"
# 리스트에서 평균값 구하기
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list
```

```python colab={"base_uri": "https://localhost:8080/", "height": 145} id="fWqS5ByTFz2D" executionInfo={"status": "error", "timestamp": 1754965436539, "user_tz": -540, "elapsed": 42, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c0edd366-5a76-4767-9c79-4b7188b3e2de"
my_list.mean()
```

```python colab={"base_uri": "https://localhost:8080/"} id="o7F6LRUPF2dL" executionInfo={"status": "ok", "timestamp": 1754965505391, "user_tz": -540, "elapsed": 42, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4a9e0708-f6ca-41dc-916c-47cec824e5c0"
sum(my_list) / len(my_list)
```

```python colab={"base_uri": "https://localhost:8080/"} id="YTU4DQmCGHRo" executionInfo={"status": "ok", "timestamp": 1754965602718, "user_tz": -540, "elapsed": 41, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4ffd0f79-9c88-4056-85bf-679c224a30ca"
# 넘파이 배열 스칼라(=>값) 곱

arr_ex1 * 3
```

```python colab={"base_uri": "https://localhost:8080/"} id="vIKBNOIxGfB2" executionInfo={"status": "ok", "timestamp": 1754965621294, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5fb57b90-3baa-4c43-838f-13414f17b061"
arr_ex1
```

```python id="MgDo4iYXGjlC" executionInfo={"status": "ok", "timestamp": 1754965635028, "user_tz": -540, "elapsed": 10, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
arr_ex1 = arr_ex1*3
```

```python colab={"base_uri": "https://localhost:8080/"} id="nemNLEY3Gm7C" executionInfo={"status": "ok", "timestamp": 1754965638272, "user_tz": -540, "elapsed": 42, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f33673fa-aacc-40a0-bc3b-3867c374ccf9"
arr_ex1
```

```python colab={"base_uri": "https://localhost:8080/"} id="WtN_Kd65Gntj" executionInfo={"status": "ok", "timestamp": 1754965656127, "user_tz": -540, "elapsed": 60, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="1de9e786-fcaa-4934-b4dd-1ba85dbb531d"
arr_ex2*7
```

```python colab={"base_uri": "https://localhost:8080/"} id="1Koj7MLbGssi" executionInfo={"status": "ok", "timestamp": 1754965660285, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7658c901-b68f-48e6-b386-61b3c1fbc157"
arr_ex2
```

```python colab={"base_uri": "https://localhost:8080/"} id="uy0S9JuqGtFd" executionInfo={"status": "ok", "timestamp": 1754965674441, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9c5aa838-0096-45d5-fd94-44e8f290b32c"
arr_ex22 = arr_ex2*7
arr_ex22
```

```python colab={"base_uri": "https://localhost:8080/"} id="c9-I_KCzGwix" executionInfo={"status": "ok", "timestamp": 1754965742502, "user_tz": -540, "elapsed": 46, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d6186637-b083-42c8-ea99-70705e937155"
# 배열끼리 빼기

arr_ex22 - arr_ex2
```

```python colab={"base_uri": "https://localhost:8080/"} id="DKujyAvLHBJ1" executionInfo={"status": "ok", "timestamp": 1754965815118, "user_tz": -540, "elapsed": 42, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a5ae336a-98ee-41a8-e798-643f08855be1"
# 예외 - 넘파이 배열 리스트로 바꾸기

ml = arr_ex1.tolist()
ml
```

```python colab={"base_uri": "https://localhost:8080/"} id="BCiRRKhPHZV3" executionInfo={"status": "ok", "timestamp": 1754965869766, "user_tz": -540, "elapsed": 67, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e41d5aef-f1b2-4dbe-af90-f33a83940754"
arr_ex22 = np.array([[10, 20], [30, 40]])
arr_ex22
```

```python colab={"base_uri": "https://localhost:8080/", "height": 180} id="MRf7DAq2HS4r" executionInfo={"status": "error", "timestamp": 1754965876257, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9ab2517b-c0da-48ae-a974-03b9def0a851"
# 배열끼리 빼기

arr_ex22 - arr_ex2
```

```python colab={"base_uri": "https://localhost:8080/"} id="iSnpiPVcHjne" executionInfo={"status": "ok", "timestamp": 1754966008305, "user_tz": -540, "elapsed": 47, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="8aa78d71-0778-4b58-957c-ce3cd3aa55a8"
ml
```

```python colab={"base_uri": "https://localhost:8080/"} id="s-WFxVV3IGPL" executionInfo={"status": "ok", "timestamp": 1754966958186, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c45d21df-6ac1-4319-8989-f83dc5e0509b"
#실습 과제1 - 상품 매출액 계산 답안

item = ["비누", "후드티", "청바지", "점퍼", "냄비", "소고기", "커피믹스"]
price = [3700, 54000, 67000, 99000, 89000, 24500, 12000]
quantity = [270, 35, 52, 5, 8, 23, 34]

price_arr = np.array(price)
quantity_arr = np.array(quantity)

price_arr2 = price_arr[1:5]
quantity_arr2 = quantity_arr[1:5]

sales = price_arr2 * quantity_arr2
print("상품별 매출액: ", sales)
print("전체 매출액: ", sales.sum())
```

<!-- #region id="Nhyyxuh6ZvpF" -->
# 3. 판다스 실습
<!-- #endregion -->

<!-- #region id="yZOdhUBSyhod" -->
#### __csv파일 불러오는 실습__
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="fwFuKLIuITp3" executionInfo={"status": "ok", "timestamp": 1754977220154, "user_tz": -540, "elapsed": 30477, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="866abe57-4fd1-4b79-bc58-23c144aaded0"
# 드라이브 마운트 코드
from google.colab import drive
drive.mount('/content/drive')
```

```python colab={"base_uri": "https://localhost:8080/", "height": 423} id="PXU1SuhgITnF" executionInfo={"status": "ok", "timestamp": 1754977540559, "user_tz": -540, "elapsed": 445, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f69799c2-0330-4900-f5b8-805d8c9efaa5"
# CSV 파일 불러오기 실습

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/body.csv')
df
```

```python colab={"base_uri": "https://localhost:8080/", "height": 206} id="6vSpZN4Q02QH" executionInfo={"status": "ok", "timestamp": 1754978351860, "user_tz": -540, "elapsed": 74, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5fb12ea4-7b23-4289-c60f-298e6749b39f"
df.head()
```

<!-- #region id="MuuW9UwB0-mu" -->
# 4. matplotlib 실습
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 237} id="7cYfsatw05Bm" executionInfo={"status": "ok", "timestamp": 1754978677439, "user_tz": -540, "elapsed": 227, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="cf619eed-1801-44c1-8093-728f8b0c02fd"
import matplotlib.pyplot as plt

plt.figure(figsize=(3,2))
plt.plot([1,3,5], [20, 25, 27])
plt.title("Example of line plot")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 333} id="QfzdkscF3-Tk" executionInfo={"status": "ok", "timestamp": 1754979532219, "user_tz": -540, "elapsed": 319, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="11f7c176-fca7-4e25-86bf-180d2aa608e9"
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(5,3))
plt.plot(x, y)
plt.title("Sine Curve")
plt.xlabel('X')
plt.ylabel('sin(X)')
plt.grid(True)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 549} id="jciPsOzx5ODc" executionInfo={"status": "ok", "timestamp": 1754980053829, "user_tz": -540, "elapsed": 644, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="92269665-2001-4bc6-e813-c16d1be22928"
# 데이터
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
sales = np.array([120, 135, 160, 180, 175, 200, 220, 210, 230, 250])

plt.figure(figsize=(4,3))
plt.plot(years, sales, linestyle='-', marker='o', color='green')
plt.title('연도별 판매액')
plt.grid(True)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/"} id="HlssRE_j8NoW" executionInfo={"status": "ok", "timestamp": 1754980271042, "user_tz": -540, "elapsed": 32385, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="cb4d3b6d-72f4-49ee-ad89-43d69b01e204"
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

```python colab={"base_uri": "https://localhost:8080/", "height": 313} id="D0-hwkHF-dkt" executionInfo={"status": "ok", "timestamp": 1754980296829, "user_tz": -540, "elapsed": 155, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fab54547-dca8-4dbd-92af-fdc24324d569"
# 데이터
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
sales = np.array([120, 135, 160, 180, 175, 200, 220, 210, 230, 250])

plt.figure(figsize=(4,3))
plt.plot(years, sales, linestyle='-', marker='o', color='green')
plt.title('연도별 판매액')
plt.grid(True)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 332} id="KbmB0_iN-dY6" executionInfo={"status": "ok", "timestamp": 1754980870498, "user_tz": -540, "elapsed": 164, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="57b57cac-2524-4c8b-df35-c6b2e63f4cc4"
# 막대 그래프 - 범주형 데이터를 비교할 때 좋은 그래프

categories = ["A", "B", "C", "D"]
values = np.array([23, 45, 12, 31])

plt.figure(figsize=(4,3))
plt.bar(categories, values, color='orange', edgecolor='black', linewidth=1.5, width=0.6)
plt.title('막대 그래프')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 342} id="h8Jjc3PFAjRC" executionInfo={"status": "ok", "timestamp": 1754981354880, "user_tz": -540, "elapsed": 158, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9ff7a8a6-90eb-44ca-b58b-7afff037615b"
# 산점도 - 두 값의 "관계"를 시각화할 때 사용

x = np.random.rand(100)
y = x + np.random.normal(0, 0.1, 100)

plt.figure(figsize=(4,3))
plt.scatter(x, y, alpha=0.5, color='teal', s=40)
plt.title('산점도')
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(rotation=45)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 313} id="ywbV7OHkBUlq" executionInfo={"status": "ok", "timestamp": 1754982845144, "user_tz": -540, "elapsed": 420, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2e157d4c-9cd4-4863-b0e2-c17efa3a5cd9"
# 히스토그램

data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(4,3))
plt.hist(data, bins=30, density=True, color='red')
# density=True: 확률밀도 그래프로 변경
plt.title('히스토그램')
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 289} id="0mTsg8_gF0q9" executionInfo={"status": "ok", "timestamp": 1754982819541, "user_tz": -540, "elapsed": 143, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e758c3e1-ba11-4cde-d5fb-4d7333fa0bf3"
# 파이 차트

y = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]

plt.figure(figsize=(4,3))
plt.pie(sizes, labels=y)
plt.title("파이 차트")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 407} id="i8Ds6rzxIKPT" executionInfo={"status": "ok", "timestamp": 1754983936865, "user_tz": -540, "elapsed": 210, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e7bc3067-cea8-4611-bec5-c75752ae529e"
labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
explode = (0, 0.1, 0, 0)

plt.figure(figsize=(4,4))
plt.pie(
    sizes,
    labels = labels,
    colors = colors,
    autopct='%1.1f%%',              # 파이 조각 위에 "퍼센트" 보여주기
    startangle=90,                  # 시작 각도 조절
    explode=explode,                # 특정 조각 강조
    shadow=True,                    # 그림자 효과
    counterclock=False              # 시계 방향으로 돌려 보기
)
plt.title('커스터 마이징된 파이차트', fontsize=30, fontweight='bold')
plt.tight_layout()                  # 그래프 겹쳐보이기 금지
plt.show()
```

<!-- #region id="746NqYDTK4xv" -->
| 포맷 문자열    | 설명       | 예시 출력    |
| --------- | -------- | -------- |
| `%1.0f%%` | 정수로 표시   | `25%`    |
| `%1.1f%%` | 소수점 한 자리 | `25.0%`  |
| `%1.2f%%` | 소수점 두 자리 | `25.00%` |
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 307} id="ufly9qvyKFV4" executionInfo={"status": "ok", "timestamp": 1754984416815, "user_tz": -540, "elapsed": 1016, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="91cd8fb3-778b-4f21-d1fd-0e6e1f3d642e"
# 다중 레이아웃 - subplot(행, 열, 순번) 기본

x = np.linspace(0, 2*np.pi, 100)

plt.figure(figsize=(6,3))

plt.subplot(1, 2, 1)
plt.plot(x, np.sin(x))
plt.title('사인 그래프')

plt.subplot(1, 2, 2)
plt.plot(x, np.cos(x))
plt.title('코사인 그래프')

plt.tight_layout()
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 707} id="spBaVyeLOQEj" executionInfo={"status": "ok", "timestamp": 1754985042908, "user_tz": -540, "elapsed": 1528, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d2e97022-9a8d-47d8-89be-48d6b7fab838"
# 다중 레이아웃 - subplot(행, 열, 순번) 응용

x = np.linspace(0, 2*np.pi, 100)

plt.figure(figsize=(7,7))

for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.plot(x, np.sin(x+i), label=f"sin(x+{i})")
    plt.title(f"{i+1} 사인 그래프")
    #plt.xticks([])
    #plt.yticks([])
    plt.legend()

plt.tight_layout()
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 423} id="iCVxjmXMW8PQ" executionInfo={"status": "ok", "timestamp": 1754986696407, "user_tz": -540, "elapsed": 62, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="aa32d845-f42f-449e-e2d2-8a3f61440e14"
df
```

```python colab={"base_uri": "https://localhost:8080/", "height": 307} id="MsTLxkThPuEm" executionInfo={"status": "ok", "timestamp": 1754985845051, "user_tz": -540, "elapsed": 337, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="876adbb3-2cf9-46ee-9936-b82e4acff950"
# 실습 2 - 키와 몸무게 두 그래프 시각화

plt.figure(figsize=(6, 3))

plt.subplot(1, 2, 1)
plt.hist(df['height'], bins=15, edgecolor = "black")
plt.title("키 히스토그램")

plt.subplot(1, 2, 2)
plt.hist(df['weight'], bins=15, edgecolor = "black")
plt.title("몸무게 히스토그램")

plt.tight_layout()
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 272} id="-3CmZQQ1TYRt" executionInfo={"status": "ok", "timestamp": 1754987520651, "user_tz": -540, "elapsed": 1613, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e13fc131-c772-4d15-9865-0496f804cbe8"
# 실습3 - 여러 그래프 시각화

plt.figure(figsize=(15, 4))

# 1. 키 분포
plt.subplot(1, 3, 1)
plt.hist(df['height'], bins=20)
plt.title("키 히스토그램")

# 2. 몸무게 분포
plt.subplot(1, 3, 2)
plt.hist(df['weight'], bins=20, color='gray')
plt.title("몸무게 히스토그램")

# 3. 산점도
plt.subplot(1, 3, 3)
plt.scatter(df['height'], df['weight'], alpha=0.6)
plt.title("키와 몸무게 산점도")

plt.tight_layout()
plt.show()
```

```python id="Sf9OkPgTaFrq"

```
