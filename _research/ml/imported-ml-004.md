---
title: "기초 통계와 데이터 시각화"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250813_코드실습4_5. 기초 통계와 데이터 시각화"
source_path: "11_Machine_Learning/Code_Snippets/250813_코드실습4_5. 기초 통계와 데이터 시각화.md"
excerpt: "기초 통계와 데이터 시각화의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 Seaborn 실습 순서로 큰 장을 먼저 훑고, 파생 변수 추가, CSV 데이터 불러오기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 37개 코드..."
research_summary: "기초 통계와 데이터 시각화의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 Seaborn 실습 순서로 큰 장을 먼저 훑고, 파생 변수 추가, CSV 데이터 불러오기 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 37개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, seaborn입니다."
research_artifacts: "ipynb/md · 코드 37개 · 실행 35개"
code_block_count: 37
execution_block_count: 35
research_focus:
  - "박스 프롯 - 커스터마이징 (1)"
  - "박스 프롯 - 커스터마이징 (2)"
  - "Seaborn 실습"
research_stack:
  - "matplotlib"
  - "warnings"
  - "numpy"
  - "seaborn"
  - "google"
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
    <div class="research-overview__value">기초 통계와 데이터 시각화에서 Seaborn 실습 흐름을 직접 따라가며 구현했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">Seaborn 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">특정 데이터셋 설명보다 Seaborn 실습 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">Seaborn 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">CSV 데이터 불러오기 -&gt; 데이터셋 불러오기 -&gt; 파생 변수 추가</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 37 · 실행 35</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">matplotlib, warnings, numpy, seaborn 외 1</div>
  </div>
</div>

```python colab={"base_uri": "https://localhost:8080/"} id="OzI1-QmxG8vs" executionInfo={"status": "ok", "timestamp": 1755065503979, "user_tz": -540, "elapsed": 36120, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b908ad5a-0786-4ec3-d7f7-9aff9c368c52"
ㄹ!sudo apt-get install -y fonts-nanum
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

```python colab={"base_uri": "https://localhost:8080/"} id="WAtIF-qOKEm9" executionInfo={"status": "ok", "timestamp": 1755050633668, "user_tz": -540, "elapsed": 28, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f1772bd6-f819-4759-a150-576b88c87a61"
import numpy as np

x = [5, 7, 8, 9, 10, 12, 13, 14, 20]

q1 = np.percentile(x, 25)
q2 = np.percentile(x, 50)
q3 = np.percentile(x, 75)
iqr = q3 - q1

print("Q1: ", q1)
print("Q2(중앙값): ", q2)
print("Q3: ", q3)
print('IQR: ', iqr)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 313} id="YYbgBYV2K2ht" executionInfo={"status": "ok", "timestamp": 1755050860795, "user_tz": -540, "elapsed": 113, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="636299ee-527f-4688-c95d-be81efee1872"
# 박스 프롯 - 이상치 확인

plt.figure(figsize=(4,3))
plt.boxplot(x, vert = False)
plt.title("사분위수 시각화")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/"} id="6KHO1wmcLcW5" executionInfo={"status": "ok", "timestamp": 1755050906461, "user_tz": -540, "elapsed": 49, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="cfae9722-4611-4291-8eec-c7941f339a47"
x = [-100, 5, 7, 8, 9, 10, 12, 13, 14, 20, 79]

q1 = np.percentile(x, 25)
q2 = np.percentile(x, 50)
q3 = np.percentile(x, 75)
iqr = q3 - q1

print("Q1: ", q1)
print("Q2(중앙값): ", q2)
print("Q3: ", q3)
print('IQR: ', iqr)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 313} id="-ygWqOXpL7Dx" executionInfo={"status": "ok", "timestamp": 1755050930355, "user_tz": -540, "elapsed": 112, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4ac20d44-2d1c-4c45-83bd-47e371ac5efd"
# 박스 프롯 - 이상치 확인

plt.figure(figsize=(4,3))
plt.boxplot(x, vert = False)
plt.title("사분위수 시각화")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 316} id="XzvNaCxkMEkq" executionInfo={"status": "ok", "timestamp": 1755051516825, "user_tz": -540, "elapsed": 154, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="78188dc6-77fd-44d7-830a-4ea4478bb85c"
# 박스 프롯 - 커스터마이징 (1)

plt.figure(figsize=(7,3))
plt.boxplot(
    x,
    vert = False,
    patch_artist=True,                                        # 박스 색을 채워라
    boxprops=dict(facecolor = 'skyblue', color = 'blue'),     # 박스 스타일
    medianprops=dict(color = 'red', linewidth = 3),           # 중앙값 선 스타일
    whiskerprops=dict(color = 'gray', linestyle = '--'),      # 수염 스타일
    flierprops=dict(marker='*', markersize=8)                 # 이상치 스타일
    )
plt.title("사분위수 시각화", fontsize=15, fontweight='bold')
plt.grid(axis = 'x', linestyle = '--', alpha=0.4)
plt.yticks([1], ['Group A'])
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 316} id="SrU-BRsSNUu5" executionInfo={"status": "ok", "timestamp": 1755051804964, "user_tz": -540, "elapsed": 139, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="899e481e-350b-4740-b960-7db115504fa5"
# 박스 프롯 - 커스터마이징 (2)

box_style=dict(facecolor='skyblue', color='blue')       # 박스 스타일
median_style=dict(color='red', linewidth=3)             # 중앙값 선 스타일
whisker_style=dict(color='gray', linestyle='--')        # 수염 스타일
flier_style=dict(marker='*', markersize=8)              # 이상치 스타일

plt.figure(figsize=(7,3))
plt.boxplot(
    x,
    vert = False,
    patch_artist=True,                                  # 박스 색을 채워라
    boxprops=box_style,
    medianprops=median_style,
    whiskerprops=whisker_style,
    flierprops=flier_style
    )
plt.title("사분위수 시각화", fontsize=15, fontweight='bold')
plt.grid(axis = 'x', linestyle = '--', alpha=0.4)
plt.yticks([1], ['Group A'])
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 390} id="ICEX1N2NSfUX" executionInfo={"status": "ok", "timestamp": 1755052769996, "user_tz": -540, "elapsed": 253, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bec0b07f-d693-4c7e-fa2f-14094fa2fe6a"
# 히스토그램 실습 (1)

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]

plt.figure(figsize=(8,4))

plt.hist(weight, label='bins=10')
plt.hist(weight, bins=20, label='bins=20')

plt.legend()
plt.title("두 개 히스토그램 예시")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 390} id="Odx8Bb9JS_gn" executionInfo={"status": "ok", "timestamp": 1755052880513, "user_tz": -540, "elapsed": 240, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a89fb80a-dabf-43a0-d87d-f935ce8f88c5"
# 히스토그램 실습 (2)

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
x = [50, 66, 60, 53, 70, 76, 80, 90, 100]

plt.figure(figsize=(8,4))

plt.hist(x, label='bins=10 - x')
plt.hist(weight, label='bins=10 - weight', color='red', alpha=0.4)

plt.legend()
plt.title("두 개 히스토그램 예시")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 390} id="XWRckvFoTXZ8" executionInfo={"status": "ok", "timestamp": 1755053100926, "user_tz": -540, "elapsed": 209, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="0bc35412-d4ee-4e59-c5cb-595f169f15f5"
# 히스토그램 실습 (3)

weight = [68, 81, 64, 56, 78, 74, 61, 77, 66, 68, 59, 71,
          80, 59, 67, 81, 69, 73, 69, 74, 70, 65]
x = [50, 66, 60, 53, 70, 76, 80, 90, 100]

plt.figure(figsize=(8,4))

plt.hist([weight, x],label=['weight', '데이터 x'], alpha=0.7)

plt.legend()
plt.title("두 개 히스토그램 예시")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 313} id="ZaJRmeW5D60U" executionInfo={"status": "ok", "timestamp": 1755066124927, "user_tz": -540, "elapsed": 182, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f6a40279-9e6e-497b-bacd-6ead3ee9216f"
# KDE plot
import seaborn as sns

x = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]

plt.figure(figsize=(4,3))
sns.kdeplot(x, fill=True)
plt.title("KDE Plot")
plt.grid(True, alpha=0.3)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/"} id="2OvoO3kKE8k7" executionInfo={"status": "ok", "timestamp": 1755066332618, "user_tz": -540, "elapsed": 2456, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9c206a36-c2d9-471b-e536-0af2b16772db"
# 드라이브 마운트 코드
from google.colab import drive
drive.mount('/content/drive')
```

```python colab={"base_uri": "https://localhost:8080/", "height": 423} id="jXEf_JXdGKvv" executionInfo={"status": "ok", "timestamp": 1755069470634, "user_tz": -540, "elapsed": 54, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="16d7f7dd-fa97-4830-8983-fcf7295e9527"
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/body.csv')
df
```

```python colab={"base_uri": "https://localhost:8080/", "height": 390} id="syaTMk47GYd_" executionInfo={"status": "ok", "timestamp": 1755066548861, "user_tz": -540, "elapsed": 317, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="9a73327c-63b0-4b80-cae5-2db81aa84cc0"
# 히스토그램 + KDE 그리기

plt.figure(figsize=(6,4))
sns.histplot(df, kde=True, bins=30, edgecolor='black')
plt.title("Histogram + KDE")
plt.grid(True, alpha = 0.4)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 368} id="Xs5TG-HqH6G_" executionInfo={"status": "ok", "timestamp": 1755066719824, "user_tz": -540, "elapsed": 383, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4c79b1b7-3d9f-4037-c1ef-c2e0cf4b88bc"
plt.figure(figsize=(4,4))
df['height'].plot(kind = 'kde')
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 368} id="tWvHi7atIIEw" executionInfo={"status": "ok", "timestamp": 1755066845625, "user_tz": -540, "elapsed": 202, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7417091a-c70a-4ed8-cfc0-74442a4723a7"
plt.figure(figsize=(4,4))
df['height'].plot(kind = 'kde', bw_method=0.9)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 311} id="-c5T3K0PIdRw" executionInfo={"status": "ok", "timestamp": 1755066893615, "user_tz": -540, "elapsed": 186, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4a27a558-bd53-4d91-9178-da9269ec53c4"
plt.figure(figsize=(4,3))
sns.kdeplot(df['height'])
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 404} id="XX1WlbVtI0bc" executionInfo={"status": "ok", "timestamp": 1755067052357, "user_tz": -540, "elapsed": 142, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4289c6e2-d83d-4070-bb11-450e919fc6b3"
## 실습1 - 키와 몸무게 이상치 박스플롯 그리기
import numpy as np

# 모범답안 기본 - height
q1 = np.percentile(df['height'], 25)
q2 = np.percentile(df['height'], 50)
q3 = np.percentile(df['height'], 75)
iqr = q3 - q1

print("Q1:", q1)
print("Q2 (중앙값):", q2)
print("Q3:", q3)
print("IQR:", iqr)

plt.figure(figsize=(4,3))
plt.boxplot(df['height'], vert=False)
plt.title("height IQR")
plt.xlabel("값")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 404} id="gwItYwrCJcvQ" executionInfo={"status": "ok", "timestamp": 1755067073750, "user_tz": -540, "elapsed": 73, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="f954d1af-7706-4358-8537-a5f463fce7b8"
# 모범답안 기본 - weight
q1 = np.percentile(df['weight'], 25)
q2 = np.percentile(df['weight'], 50)
q3 = np.percentile(df['weight'], 75)
iqr = q3 - q1

print("Q1:", q1)
print("Q2 (중앙값):", q2)
print("Q3:", q3)
print("IQR:", iqr)

plt.figure(figsize=(4,3))
plt.boxplot(df['weight'], vert=False)
plt.title("weight IQR")
plt.xlabel("값")
plt.show()
```

<!-- #region id="NRB7I6gKQA3O" -->
# Seaborn 실습
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 332} id="PwDnKM1QP8AT" executionInfo={"status": "ok", "timestamp": 1755068906764, "user_tz": -540, "elapsed": 302, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="84363449-c916-42c2-dd17-b3da6f5b3eec"
# 산점도

plt.figure(figsize=(5,3))
sns.scatterplot(data=df, x='height', y='weight')
plt.title('키 vs 몸무게 산점도')
plt.show()
```

```python id="YjBF8wlZQhBG"
# 히스토그램 - 구간 나누기

df['height_bin'] = pd.cut(df['height'], bins=range(150, 200, 5))
df['weight_bin'] = pd.cut(df['weight'], bins=range(40, 120, 10))
```

```python colab={"base_uri": "https://localhost:8080/", "height": 376} id="fBXjhk6bRqXD" executionInfo={"status": "ok", "timestamp": 1755069614667, "user_tz": -540, "elapsed": 296, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5d0aea7b-6c63-480d-c421-864dc211859a"
# barplot

plt.figure(figsize=(6,3))
sns.barplot(data=df, x='height_bin', y='weight', errorbar=None)
plt.title("키와 몸무게 평균 비교")
plt.xticks(rotation=45)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 376} id="DvvUFFm1SZtB" executionInfo={"status": "ok", "timestamp": 1755069917896, "user_tz": -540, "elapsed": 323, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="225978d4-1a98-444e-f2bb-9a4183769176"
# 박스 플롯 - 구간별로

plt.figure(figsize=(6,3))
sns.boxplot(data=df, x='height_bin', y='weight')
plt.title('키 박스플롯')
plt.xticks(rotation=45)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 453} id="I4V3t8VJUR0_" executionInfo={"status": "ok", "timestamp": 1755070103818, "user_tz": -540, "elapsed": 412, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="44430869-7115-4764-8b2f-b0253e046df3"
# 바이올린 플롯: 박스플롯 + 데이터 밀도 결합 시각화

plt.figure(figsize=(10,4))
sns.violinplot(data=df, x='height_bin', y='weight')
plt.title('키 바이올린 플롯')
plt.xticks(rotation=45)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 453} id="x-vzdS_kU7U_" executionInfo={"status": "ok", "timestamp": 1755070350692, "user_tz": -540, "elapsed": 284, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="791c91fc-9423-43f4-a295-4a528aec98b3"
# 스트립플롯

plt.figure(figsize=(10,4))
sns.stripplot(data=df, x='height_bin', y='weight', jitter=True)
plt.title('키 스트립 플롯')
plt.xticks(rotation=45)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 453} id="XgJBrtjCVvXN" executionInfo={"status": "ok", "timestamp": 1755070411723, "user_tz": -540, "elapsed": 2322, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="03d37028-71ff-468e-d3ab-7865ad7be792"
# 스왐플롯

plt.figure(figsize=(10,4))
sns.swarmplot(data=df, x='height_bin', y='weight')
plt.title('키 스왐플롯')
plt.xticks(rotation=45)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 332} id="knxSk-LuWSoc" executionInfo={"status": "ok", "timestamp": 1755070480590, "user_tz": -540, "elapsed": 248, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e4aa28fc-9028-417a-ce0e-61046267e283"
plt.figure(figsize=(5,3))
sns.histplot(data=df, x='height')
plt.title("키 - 히스토그램")
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 625} id="qkZobCHSWfSz" executionInfo={"status": "ok", "timestamp": 1755070705549, "user_tz": -540, "elapsed": 276, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="0d5ca902-fb7e-4c90-ec5f-18445c08d64f"
# 조인트 플롯

plt.figure(figsize=(4,4))
sns.jointplot(data=df, x='height', y='weight', kind='scatter')
#plt.title('조인트 플롯')
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 513} id="HLPWiY2hXKhP" executionInfo={"status": "ok", "timestamp": 1755070992728, "user_tz": -540, "elapsed": 548, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="89055a58-93ef-489f-bdeb-a23273ba5c80"
# pairplot

sns.pairplot(df)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/"} id="HWcmTwDJY0fo" executionInfo={"status": "ok", "timestamp": 1755071167478, "user_tz": -540, "elapsed": 194, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a388b199-084d-4b41-f4f6-b64ac45b1fa2"
# 씨본 데이터 목록 - 명령문 기억하실 필요 XXXX
sns.get_dataset_names()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 443} id="7ys6U4hfZLq5" executionInfo={"status": "ok", "timestamp": 1755071355518, "user_tz": -540, "elapsed": 468, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="40bac287-7499-4465-d8b8-3d63d9fbf0a6"
# 타이타닉 데이터셋 불러오기
titanic_data = sns.load_dataset('titanic')
titanic_data
```

<!-- #region id="5cbEuaPcefiy" -->
## 씨본 스타일

팔레트
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 311} id="hw9FL_GIZ5f9" executionInfo={"status": "ok", "timestamp": 1755072685055, "user_tz": -540, "elapsed": 160, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="de36495f-2dcc-43e3-fb30-8925b6183c2f"
plt.figure(figsize=(4,3))
sns.set_palette(sns.color_palette("pastel")) # pastel, deep, muted....
sns.barplot(data=titanic_data, x='age', y='class', errorbar=None)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 311} id="vz3c25AFeyy0" executionInfo={"status": "ok", "timestamp": 1755072860194, "user_tz": -540, "elapsed": 186, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2496695f-2863-4f55-e35b-598259f0a817"
plt.figure(figsize=(4,3))
sns.set_palette('deep') # pastel, deep, muted....
sns.violinplot(data=titanic_data, x='age')
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 319} id="PrbevT0Sfhb5" executionInfo={"status": "ok", "timestamp": 1755072994314, "user_tz": -540, "elapsed": 189, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ee4f64ab-8273-40ce-ed1d-bee8d6a673b2"
# set_theme()

plt.figure(figsize=(4,3))
sns.set_theme(style='whitegrid')
sns.violinplot(data=titanic_data, x='age')
plt.show()
```

<!-- #region id="AnQ_d5sbgN4H" -->
## 상관관계
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 533} id="qjfZjIQUf9K2" executionInfo={"status": "ok", "timestamp": 1755073203767, "user_tz": -540, "elapsed": 933, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="b5f7d969-8f9b-49d2-cceb-08be3445a6bc"
corr = titanic_data.select_dtypes(include="number").corr()        # 수치형 변수만 선택해서 상관관계

plt.figure(figsize=(6,6))
sns.heatmap(corr, cmap='coolwarm', annot=True)
plt.show()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 523} id="pmCDxt2BgliJ" executionInfo={"status": "ok", "timestamp": 1755073864296, "user_tz": -540, "elapsed": 445, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="efa40cd5-f88f-4846-dc52-e2cbda9b4617"
# 결측치를 히트맵으로 시각화

sns.heatmap(titanic_data.isnull(), cbar=False, yticklabels=False)
plt.show()
```

```python id="By-n04Q4iysp"

```
