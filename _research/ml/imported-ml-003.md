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

# 1. 마크다운 실습

## 자기소개 마크다운 미션

### 이름

조하나

### 요즘 배우는 것

- 파이썬 기초 문법
- 마크다운 정리법
- 데이터 시각화
- AI 엔지니어링

### 나의 목표

> 마크다운으로 매일 학습 기록을 남기는 습관 만들기!

---

```python
import numpy as np

arr = np.array([[2, 3, 4,], [5, 6, 7]])

arr
```

```python
arr[:,0]
```

```python
arr[1,0]
```

```python
arr[1, 0:2]
```

```python
arr[0:0,:]
```

# 2. Numpy 실습

### 기본 함수들

```python
# np.array(): 넘파이 배열로 바꿔주는 함수

import numpy as np

arr = np.array([1,3,5,7,9])
arr
```

```python
# np.arange()

arr = np.arange(10)
print(arr)
```

```python
# 2씩 텀 주기
np.arange(3, 10, 2)
```

```python
# np.zeros()
np.zeros((2,3))
```

```python
# 1차원 배열 인덱싱

arr_ex1 = np.array([1,2,3,4,5,6,7,8,9])
```

```python
print(arr_ex1[2])
```

```python
arr_ex1[-3]
```

```python
arr_ex1[2:6]
```

```python
# 2차원 인덱싱

arr_ex2 = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])
```

```python
arr_ex2[0,1]
```

```python
# 두번째 행 출력
arr_ex2[1,:]
```

```python
# 세번째 열 출력
arr_ex2[:,2]
```

```python
# 0~1행, 1~2열 부분 배열
arr_ex2[0:2, 1:3]
```

```python
arr_ex1
```

```python
arr_ex2
```

```python
arr_ex1.min()
```

```python
arr_ex1.max()
```

```python
arr_ex2.max()
```

```python
arr_ex1.mean()
```

```python
arr_ex2.mean()
```

```python
# 리스트에서 평균값 구하기
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list
```

```python
my_list.mean()
```

```python
sum(my_list) / len(my_list)
```

```python
# 넘파이 배열 스칼라(=>값) 곱

arr_ex1 * 3
```

```python
arr_ex1
```

```python
arr_ex1 = arr_ex1*3
```

```python
arr_ex1
```

```python
arr_ex2*7
```

```python
arr_ex2
```

```python
arr_ex22 = arr_ex2*7
arr_ex22
```

```python
# 배열끼리 빼기

arr_ex22 - arr_ex2
```

```python
# 예외 - 넘파이 배열 리스트로 바꾸기

ml = arr_ex1.tolist()
ml
```

```python
arr_ex22 = np.array([[10, 20], [30, 40]])
arr_ex22
```

```python
# 배열끼리 빼기

arr_ex22 - arr_ex2
```

```python
ml
```

```python
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

# 3. 판다스 실습

#### csv파일 불러오는 실습

```python
# 드라이브 마운트 코드
from google.colab import drive
drive.mount('/content/drive')
```

```python
# CSV 파일 불러오기 실습

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/body.csv')
df
```

```python
df.head()
```

# 4. matplotlib 실습

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(3,2))
plt.plot([1,3,5], [20, 25, 27])
plt.title("Example of line plot")
plt.show()
```

```python
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

```python
# 데이터
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
sales = np.array([120, 135, 160, 180, 175, 200, 220, 210, 230, 250])

plt.figure(figsize=(4,3))
plt.plot(years, sales, linestyle='-', marker='o', color='green')
plt.title('연도별 판매액')
plt.grid(True)
plt.show()
```

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

```python
# 데이터
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
sales = np.array([120, 135, 160, 180, 175, 200, 220, 210, 230, 250])

plt.figure(figsize=(4,3))
plt.plot(years, sales, linestyle='-', marker='o', color='green')
plt.title('연도별 판매액')
plt.grid(True)
plt.show()
```

```python
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

```python
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

```python
# 히스토그램

data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(4,3))
plt.hist(data, bins=30, density=True, color='red')
# density=True: 확률밀도 그래프로 변경
plt.title('히스토그램')
plt.show()
```

```python
# 파이 차트

y = ['A', 'B', 'C', 'D']
sizes = [25, 30, 20, 25]

plt.figure(figsize=(4,3))
plt.pie(sizes, labels=y)
plt.title("파이 차트")
plt.show()
```

```python
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

| 포맷 문자열    | 설명       | 예시 출력    |
| --------- | -------- | -------- |
| `%1.0f%%` | 정수로 표시   | `25%`    |
| `%1.1f%%` | 소수점 한 자리 | `25.0%`  |
| `%1.2f%%` | 소수점 두 자리 | `25.00%` |

```python
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

```python
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

```python
df
```

```python
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

```python
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

```python

```
