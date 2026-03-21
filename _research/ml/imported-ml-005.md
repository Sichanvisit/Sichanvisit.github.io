---
title: "코드실습5 7.DF 마스터하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250814_코드실습5_7.DF 마스터하기"
source_path: "11_Machine_Learning/Code_Snippets/250814_코드실습5_7.DF 마스터하기.md"
excerpt: "코드실습5 7.DF 마스터하기를 중심으로 객체지향 설계 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코드실습5 7.DF 마스터하기를 중심으로 객체지향 설계 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 CSV 데이터 불러오기, 데이터 전처리 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 83개 코드 블록, 69개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, seaborn, matplotlib입니다."
research_artifacts: "ipynb/md · 코드 83개 · 실행 69개"
code_block_count: 83
execution_block_count: 69
research_focus:
  - "Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)"
  - "데이터 확인"
  - "df 기본기"
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
  - practice
---

<div class="research-doc-hero">
  <div class="research-doc-summary">
    <p class="research-doc-summary__label">문제 설정</p>
    <p class="research-doc-summary__body">Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)</p>
  </div>
  <div class="research-doc-meta">
<div class="research-doc-card">
  <p class="research-doc-card__label">데이터 맥락</p>
  <p class="research-doc-card__value">Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">핵심 개념</p>
  <p class="research-doc-card__value">객체지향 설계</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">구현 포인트</p>
  <p class="research-doc-card__value">CSV 데이터 불러오기 · 데이터 전처리 · 정규화/표준화</p>
</div>
  </div>
  <div class="research-doc-stats">
<div class="research-doc-stat">
  <span>소스</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-stat">
  <span>자료</span>
  <strong>코드 83 · 실행 69</strong>
</div>
<div class="research-doc-stat">
  <span>주요 스택</span>
  <strong>google, pandas, seaborn, matplotlib 외 1</strong>
</div>
  </div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">객체지향 설계</p>
  <p class="research-note-card__body">객체지향은 관련 데이터와 동작을 하나의 객체로 묶어 문제를 구조적으로 표현하는 방식입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 클래스, 메서드, 상태 관리 같은 코드가 핵심 학습 포인트로 드러납니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-list">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">CSV 데이터 불러오기</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>pd.read_csv</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 전처리</p>
  <p class="research-step-card__title">데이터 전처리</p>
  <p class="research-step-card__body">결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 여러 변수 박스플롯 그리기</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 피처 가공</p>
  <p class="research-step-card__title">정규화/표준화</p>
  <p class="research-step-card__body">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 날짜로 변환된 데이터 타입 기준 월, 요일 파생변수 생성</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 구현 코드</p>
  <p class="research-step-card__title">추가 - 컬럼명 변경</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 위와 같은 코드 - 딕셔너리 따로 지정</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 구현 코드</p>
  <p class="research-step-card__title">문자 데이터 가공</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 문자열 분리 · n=1</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 구현 코드</p>
  <p class="research-step-card__title">데이터 합치기</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
</div>

## Code Evidence

### CSV 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/Sample_Superstor.csv')
df
```

### 데이터 전처리

**직접 해본 단계**: 전처리

**핵심 API**: `matplotlib`

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

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

### 정규화/표준화

**직접 해본 단계**: 피처 가공

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
# 날짜로 변환된 데이터 타입 기준 월, 요일 파생변수 생성

df['order_month'] = df['order_date'].dt.month
df['order_weekday'] = df['order_date'].dt.day_name()
df['order_year'] = df['order_date'].dt.year

df[['order_date', 'order_year', 'order_month', 'order_weekday']].head(2)
```

### 추가 - 컬럼명 변경

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# 위와 같은 코드 - 딕셔너리 따로 지정
rename_dict = {
    'Order Date': 'order_date',
    'Ship Date': 'ship_date'
    }
df = df.rename(columns = rename_dict)
df.head(2)
```

### 문자 데이터 가공

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# 문자열 분리

name_split = df['Ship Mode'].str.split(' ', n=1, expand=True)
# n=1: ' '기준 한 번 나눈다// expand=True: 두 개의 새로운 컬럼(0, 1)
df['grade'] = name_split[0]
df['status'] = name_split[1]

df[['Ship Mode', 'grade', 'status']].head(2)
```

### 데이터 합치기

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250814_코드실습5_7.DF 마스터하기.md`
- Source formats: `ipynb`, `md`
- Companion files: `250814_코드실습5_7.DF 마스터하기.ipynb`, `250814_코드실습5_7.DF 마스터하기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `0.유튜브`
- External references: `www.kaggle.com`, `localhost`

## Note Preview

> Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)
> 1. 개요
