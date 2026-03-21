---
title: "코드실습3 4.데이터사이언스 Toolkit"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250812_코드실습3_4.데이터사이언스 Toolkit"
source_path: "11_Machine_Learning/Code_Snippets/250812_코드실습3_4.데이터사이언스 Toolkit.md"
excerpt: "코드실습3 4.데이터사이언스 Toolkit의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 마크다운 실습, Numpy 실습, 판다스 실습 순서로 큰 장을 먼저 훑고, csv파일 불러오는 실습, matplotlib 실습 같은 코드로 실제 구현을 이어서 확인할..."
research_summary: "코드실습3 4.데이터사이언스 Toolkit의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 마크다운 실습, Numpy 실습, 판다스 실습 순서로 큰 장을 먼저 훑고, csv파일 불러오는 실습, matplotlib 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 60개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, google, pandas, matplotlib입니다."
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

## 글 한눈에 보기

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <colgroup>
      <col class="research-compact-table__col research-compact-table__col--label">
      <col class="research-compact-table__col research-compact-table__col--value">
    </colgroup>
    <thead>
      <tr>
        <th>항목</th>
        <th>내용</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">문제 설정</th>
        <td>코드실습3 4.데이터사이언스 Toolkit에서 마크다운 실습, Numpy 실습, 판다스 실습 흐름을 직접 따라가며 구현했습니다.</td>
      </tr>
      <tr>
        <th scope="row">원본 구조</th>
        <td>마크다운 실습 -&gt; Numpy 실습 -&gt; 판다스 실습 -&gt; matplotlib 실습</td>
      </tr>
      <tr>
        <th scope="row">데이터 맥락</th>
        <td>특정 데이터셋 설명보다 마크다운 실습, Numpy 실습, 판다스 실습 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다.</td>
      </tr>
      <tr>
        <th scope="row">주요 장</th>
        <td>마크다운 실습 · Numpy 실습 · 판다스 실습 · matplotlib 실습</td>
      </tr>
      <tr>
        <th scope="row">구현 흐름</th>
        <td>csv파일 불러오는 실습 -&gt; matplotlib 실습 -&gt; 기본 함수들</td>
      </tr>
      <tr>
        <th scope="row">자료</th>
        <td>ipynb / md · 코드 60 · 실행 59</td>
      </tr>
      <tr>
        <th scope="row">주요 스택</th>
        <td>numpy, google, pandas, matplotlib 외 1</td>
      </tr>
    </tbody>
  </table>
</div>

## 원본 노트 흐름

### 마크다운 실습

마크다운으로 매일 학습 기록을 남기는 습관 만들기!

- 읽을 포인트: 세부 흐름: 자기소개 마크다운 미션, 자기소개 마크다운 미션 > 이름, 자기소개 마크다운 미션 > 나의 목표

#### 자기소개 마크다운 미션

마크다운 실습 > 자기소개 마크다운 미션 아래 세부 항목들을 묶어 보는 구간입니다.

#### 자기소개 마크다운 미션 > 이름

자기소개 마크다운 미션 > 이름 아래에 이어질 세부 설명과 코드를 읽기 전 흐름을 잡는 구간입니다.

#### 자기소개 마크다운 미션 > 나의 목표

마크다운으로 매일 학습 기록을 남기는 습관 만들기!

### Numpy 실습

기본 함수들 같은 코드를 직접 따라가며 Numpy 실습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 기본 함수들

#### 기본 함수들

넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.

### 판다스 실습

csv파일 불러오는 실습 같은 코드를 직접 따라가며 판다스 실습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: csv파일 불러오는 실습

#### csv파일 불러오는 실습

csv파일 불러오는 실습 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

### matplotlib 실습

데이터, 막대 그래프 - 범주형 데이터를 비..., 산점도 - 두 값의 "관계"를 시각... 같은 코드를 직접 따라가며 matplotlib 실습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 데이터, 막대 그래프 - 범주형 데이터를 비교할 때 좋은 그래프, 산점도 - 두 값의 "관계"를 시각화할 때 사용

#### 데이터

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

#### 막대 그래프 - 범주형 데이터를 비교할 때 좋은 그래프

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

#### 산점도 - 두 값의 "관계"를 시각화할 때 사용

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

## 구현 흐름

### 1. csv파일 불러오는 실습

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: `pd.read_csv`
- 코드 포인트: CSV 파일 불러오기 실습

### 2. matplotlib 실습

- 단계: 시각화
- 구현 의도: 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.
- 핵심 API: `matplotlib`
- 코드 포인트: -

### 3. 기본 함수들

- 단계: 구현 코드
- 구현 의도: 넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 실습 과제1 - 상품 매출액 계산 답안

### 4. 나의 목표

- 단계: 구현 코드
- 구현 의도: 넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: -

## 코드로 확인한 내용

### csv파일 불러오는 실습

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# CSV 파일 불러오기 실습

import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/body.csv')
df
```

### matplotlib 실습

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

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

넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.

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

### 나의 목표

**직접 해본 단계**: 구현 코드

넘파이 배열 생성, 인덱싱, 수치 연산을 손으로 익히는 기초 실습 코드입니다.

```python
import numpy as np

arr = np.array([[2, 3, 4,], [5, 6, 7]])

arr
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250812_코드실습3_4.데이터사이언스 Toolkit.md`
- Source formats: `ipynb`, `md`
- Companion files: `250812_코드실습3_4.데이터사이언스 Toolkit.ipynb`, `250812_코드실습3_4.데이터사이언스 Toolkit.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## 원문 미리보기

> 조하나
> - 파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링
