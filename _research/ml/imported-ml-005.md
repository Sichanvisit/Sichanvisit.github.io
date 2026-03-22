---
title: "7.DF 마스터하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250814_코드실습5_7.DF 마스터하기"
source_path: "11_Machine_Learning/Code_Snippets/250814_코드실습5_7.DF 마스터하기.md"
excerpt: "7.DF 마스터하기의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 df 기본기, 데이터 다듬기, 문자 데이터 가공 순서로 큰 장을 먼저 훑고, 데이터 전처리, 정규화/표준화 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과..."
research_summary: "7.DF 마스터하기의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 df 기본기, 데이터 다듬기, 문자 데이터 가공 순서로 큰 장을 먼저 훑고, 데이터 전처리, 정규화/표준화 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 83개 코드 블록, 69개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, seaborn, matplotlib입니다."
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
    <div class="research-overview__value">df 기본기 · 데이터 다듬기 · 문자 데이터 가공 · 정규화/표준화</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">데이터 전처리 -&gt; 정규화/표준화 -&gt; CSV 데이터 불러오기</div>
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

## 원본 노트 흐름

### df 기본기

loc/iloc, 데이터 삭제 같은 코드를 직접 따라가며 df 기본기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: loc/iloc, 데이터 삭제

#### loc/iloc

loc: 레이블기반 데이터 선택 - df.loc[행 레이블, 열 레이블] iloc: 위치(정수)기반 데이터 선택 - df.iloc[행 위치, 열 위치]

#### 데이터 삭제

데이터 삭제 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

### 데이터 다듬기

데이터 전처리 같은 코드를 직접 따라가며 데이터 다듬기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 데이터 전처리

#### 데이터 전처리

데이터 전처리 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

### 문자 데이터 가공

추가 - 컬럼명 변경 같은 코드를 직접 따라가며 문자 데이터 가공 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 추가 - 컬럼명 변경

#### 추가 - 컬럼명 변경

추가 - 컬럼명 변경 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

### 정규화/표준화

정규화 - MinMax, 위와 같은 코드, 표준화 같은 코드를 직접 따라가며 정규화/표준화 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 정규화 - MinMax, 위와 같은 코드, 표준화

#### 정규화 - MinMax

정규화/표준화 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

#### 위와 같은 코드

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

#### 표준화

정규화/표준화 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

### 데이터 합치기

concat(): 컬럼이 같은 구조..., join(): 인덱스 기준 병합, df - 카테고리별 매출 합계 같은 코드를 직접 따라가며 데이터 합치기 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: concat(): 컬럼이 같은 구조인 데이터를 위아래로 붙이기, join(): 인덱스 기준 병합, df - 카테고리별 매출 합계

#### concat(): 컬럼이 같은 구조인 데이터를 위아래로 붙이기

데이터 합치기 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

#### join(): 인덱스 기준 병합

데이터 합치기 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

#### df - 카테고리별 매출 합계

데이터 합치기 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

## 구현 흐름

### 1. 데이터 전처리

- 단계: 전처리
- 구현 의도: 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.
- 핵심 API: `matplotlib`
- 코드 포인트: 여러 변수 박스플롯 그리기

### 2. 정규화/표준화

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 날짜로 변환된 데이터 타입 기준 월, 요일 파생변수 생성

### 3. CSV 데이터 불러오기

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: `pd.read_csv`
- 코드 포인트: -

### 4. 데이터 삭제

- 단계: 구현 코드
- 구현 의도: 데이터 삭제 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: drop() · inplace=True

### 5. 추가 - 컬럼명 변경

- 단계: 구현 코드
- 구현 의도: 추가 - 컬럼명 변경 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: 컬럼명 변경 예시 - 컬럼명 하나만 변경하기

### 6. df 기본기

- 단계: 구현 코드
- 구현 의도: df 기본기 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: query() 인덱싱

## 코드로 확인한 내용

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

### CSV 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/Sample_Superstor.csv')
df
```

### 데이터 삭제

**직접 해본 단계**: 구현 코드

데이터 삭제 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python
# drop()
df.drop(index=0) # 0 행 삭제
#inplace=True
```

### 추가 - 컬럼명 변경

**직접 해본 단계**: 구현 코드

추가 - 컬럼명 변경 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python
# 컬럼명 변경 예시 - 컬럼명 하나만 변경하기

df.rename(columns={'Order ID':'order_id'}, inplace=True)
df.head(2)
```

### df 기본기

**직접 해본 단계**: 구현 코드

df 기본기 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python
# query() 인덱싱
df.query('Category=="Furniture" and Sales > 500')
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250814_코드실습5_7.DF 마스터하기.md`
- Source formats: `ipynb`, `md`
- Companion files: `250814_코드실습5_7.DF 마스터하기.ipynb`, `250814_코드실습5_7.DF 마스터하기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `0.유튜브`
- External references: `www.kaggle.com`, `localhost`

## 원문 미리보기

> Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)
> 1. 개요
