---
title: "코드실습3 4.데이터사이언스 Toolkit"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250812_코드실습3_4.데이터사이언스 Toolkit"
source_path: "11_Machine_Learning/Code_Snippets/250812_코드실습3_4.데이터사이언스 Toolkit.md"
excerpt: "파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링"
research_summary: "파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링. 마크다운으로 매일 학습 기록을 남기는 습관 만들기! `ipynb/md` 원본과 60개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, google, pandas, matplotlib입니다."
research_artifacts: "ipynb/md · 코드 60개 · 실행 59개"
code_block_count: 60
execution_block_count: 59
research_focus:
  - "마크다운 실습"
  - "자기소개 마크다운 미션"
  - "이름"
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
  - practice
---

파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링. 마크다운으로 매일 학습 기록을 남기는 습관 만들기! `ipynb/md` 원본과 60개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, google, pandas, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: 마크다운 실습, 자기소개 마크다운 미션, 이름.

**남겨둔 자료**: `ipynb/md` 원본과 60개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, google, pandas, matplotlib입니다.

**주요 스택**: `numpy`, `google`, `pandas`, `matplotlib`, `warnings`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 60 |
| Execution Cells | 59 |
| Libraries | `numpy`, `google`, `pandas`, `matplotlib`, `warnings` |
| Source Note | `250812_코드실습3_4.데이터사이언스 Toolkit` |

## What I Studied

### 요즘 배우는 것

파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링

### 나의 목표

마크다운으로 매일 학습 기록을 남기는 습관 만들기!

### matplotlib 실습

/ 포맷 문자열 / 설명 / 예시 출력 / / --------- / -------- / -------- / / %1.0f%% / 정수로 표시 / 25% / / %1.1f%% / 소수점 한 자리 / 25.0% / / %1.2f%% / 소수점 두 자리 / 25.00% /

### Key Step

np.array(): 넘파이 배열로 바꿔주는 함수

## What I Tried in Code

1. 데이터 불러오기: csv파일 불러오는 실습
2. 시각화: matplotlib 실습
3. 구현 코드: 기본 함수들

## Code Evidence

### csv파일 불러오는 실습

**직접 해본 단계**: 데이터 불러오기

`csv파일 불러오는 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다. 코드에는 CSV 파일 불러오기 실습 같은 처리 포인트도 함께 남아 있습니다.

```python
# CSV 파일 불러오기 실습

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/body.csv')
df
```

### matplotlib 실습

**직접 해본 단계**: 시각화

`matplotlib 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

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

### 기본 함수들

**직접 해본 단계**: 구현 코드

`기본 함수들`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 실습 과제1 - 상품 매출액 계산 답안 같은 처리 포인트도 함께 남아 있습니다.

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

### matplotlib 실습

**직접 해본 단계**: 시각화

`matplotlib 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 실습3 - 여러 그래프 시각화, 키 분포 같은 처리 포인트도 함께 남아 있습니다.

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

### matplotlib 실습

**직접 해본 단계**: 시각화

`matplotlib 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

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

### matplotlib 실습

**직접 해본 단계**: 시각화

`matplotlib 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 다중 레이아웃 - subplot(행, 열, 순번) 응용, plt.xticks([]) 같은 처리 포인트도 함께 남아 있습니다.

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

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `csv파일 불러오는 실습` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 시각화를 같이 남긴 이유

- 왜 필요한가: 숫자만 보면 놓치기 쉬운 분포와 이상치를 그래프로 확인해야 다음 전처리나 feature engineering 방향이 또렷해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `matplotlib 실습` 코드를 통해 어떤 그래프를 보고 판단했는지 실습 흔적을 남겼습니다.
- 원리: 시각화는 데이터 분포를 직관적으로 드러내 모델 선택과 변수 설계의 근거를 만들어 줍니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `기본 함수들` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250812_코드실습3_4.데이터사이언스 Toolkit.md`
- Source formats: `ipynb`, `md`
- Companion files: `250812_코드실습3_4.데이터사이언스 Toolkit.ipynb`, `250812_코드실습3_4.데이터사이언스 Toolkit.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 조하나
> - 파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링
