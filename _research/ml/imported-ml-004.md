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

```python
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

```python
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

```python
# 박스 프롯 - 이상치 확인

plt.figure(figsize=(4,3))
plt.boxplot(x, vert = False)
plt.title("사분위수 시각화")
plt.show()
```

```python
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

```python
# 박스 프롯 - 이상치 확인

plt.figure(figsize=(4,3))
plt.boxplot(x, vert = False)
plt.title("사분위수 시각화")
plt.show()
```

```python
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

```python
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

```python
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

```python
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

```python
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

```python
# KDE plot
import seaborn as sns

x = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]

plt.figure(figsize=(4,3))
sns.kdeplot(x, fill=True)
plt.title("KDE Plot")
plt.grid(True, alpha=0.3)
plt.show()
```

```python
# 드라이브 마운트 코드
from google.colab import drive
drive.mount('/content/drive')
```

```python
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/body.csv')
df
```

```python
# 히스토그램 + KDE 그리기

plt.figure(figsize=(6,4))
sns.histplot(df, kde=True, bins=30, edgecolor='black')
plt.title("Histogram + KDE")
plt.grid(True, alpha = 0.4)
plt.show()
```

```python
plt.figure(figsize=(4,4))
df['height'].plot(kind = 'kde')
plt.show()
```

```python
plt.figure(figsize=(4,4))
df['height'].plot(kind = 'kde', bw_method=0.9)
plt.show()
```

```python
plt.figure(figsize=(4,3))
sns.kdeplot(df['height'])
plt.show()
```

```python
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

```python
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

# Seaborn 실습

```python
# 산점도

plt.figure(figsize=(5,3))
sns.scatterplot(data=df, x='height', y='weight')
plt.title('키 vs 몸무게 산점도')
plt.show()
```

```python
# 히스토그램 - 구간 나누기

df['height_bin'] = pd.cut(df['height'], bins=range(150, 200, 5))
df['weight_bin'] = pd.cut(df['weight'], bins=range(40, 120, 10))
```

```python
# barplot

plt.figure(figsize=(6,3))
sns.barplot(data=df, x='height_bin', y='weight', errorbar=None)
plt.title("키와 몸무게 평균 비교")
plt.xticks(rotation=45)
plt.show()
```

```python
# 박스 플롯 - 구간별로

plt.figure(figsize=(6,3))
sns.boxplot(data=df, x='height_bin', y='weight')
plt.title('키 박스플롯')
plt.xticks(rotation=45)
plt.show()
```

```python
# 바이올린 플롯: 박스플롯 + 데이터 밀도 결합 시각화

plt.figure(figsize=(10,4))
sns.violinplot(data=df, x='height_bin', y='weight')
plt.title('키 바이올린 플롯')
plt.xticks(rotation=45)
plt.show()
```

```python
# 스트립플롯

plt.figure(figsize=(10,4))
sns.stripplot(data=df, x='height_bin', y='weight', jitter=True)
plt.title('키 스트립 플롯')
plt.xticks(rotation=45)
plt.show()
```

```python
# 스왐플롯

plt.figure(figsize=(10,4))
sns.swarmplot(data=df, x='height_bin', y='weight')
plt.title('키 스왐플롯')
plt.xticks(rotation=45)
plt.show()
```

```python
plt.figure(figsize=(5,3))
sns.histplot(data=df, x='height')
plt.title("키 - 히스토그램")
plt.show()
```

```python
# 조인트 플롯

plt.figure(figsize=(4,4))
sns.jointplot(data=df, x='height', y='weight', kind='scatter')
#plt.title('조인트 플롯')
plt.show()
```

```python
# pairplot

sns.pairplot(df)
plt.show()
```

```python
# 씨본 데이터 목록 - 명령문 기억하실 필요 XXXX
sns.get_dataset_names()
```

```python
# 타이타닉 데이터셋 불러오기
titanic_data = sns.load_dataset('titanic')
titanic_data
```

## 씨본 스타일

팔레트

```python
plt.figure(figsize=(4,3))
sns.set_palette(sns.color_palette("pastel")) # pastel, deep, muted....
sns.barplot(data=titanic_data, x='age', y='class', errorbar=None)
plt.show()
```

```python
plt.figure(figsize=(4,3))
sns.set_palette('deep') # pastel, deep, muted....
sns.violinplot(data=titanic_data, x='age')
plt.show()
```

```python
# set_theme()

plt.figure(figsize=(4,3))
sns.set_theme(style='whitegrid')
sns.violinplot(data=titanic_data, x='age')
plt.show()
```

## 상관관계

```python
corr = titanic_data.select_dtypes(include="number").corr()        # 수치형 변수만 선택해서 상관관계

plt.figure(figsize=(6,6))
sns.heatmap(corr, cmap='coolwarm', annot=True)
plt.show()
```

```python
# 결측치를 히트맵으로 시각화

sns.heatmap(titanic_data.isnull(), cbar=False, yticklabels=False)
plt.show()
```

```python

```
