---
title: "코드실습5 7.DF 마스터하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250814_코드실습5_7.DF 마스터하기"
source_path: "11_Machine_Learning/Code_Snippets/250814_코드실습5_7.DF 마스터하기.md"
excerpt: "Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)"
research_summary: "Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋). loc: 레이블기반 데이터 선택 - df.loc[행 레이블, 열 레이블]. `ipynb/md` 원본과 83개 코드 블록, 69개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, seaborn, matplotlib입니다."
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

Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋). loc: 레이블기반 데이터 선택 - df.loc[행 레이블, 열 레이블]. `ipynb/md` 원본과 83개 코드 블록, 69개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, seaborn, matplotlib입니다.

**빠르게 볼 수 있는 포인트**: Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰..., 데이터 확인, df 기본기.

**남겨둔 자료**: `ipynb/md` 원본과 83개 코드 블록, 69개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, pandas, seaborn, matplotlib입니다.

**주요 스택**: `google`, `pandas`, `seaborn`, `matplotlib`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 83 |
| Execution Cells | 69 |
| Libraries | `google`, `pandas`, `seaborn`, `matplotlib`, `numpy`, `sklearn` |
| Source Note | `250814_코드실습5_7.DF 마스터하기` |

## What This Note Covers

### 데이터 확인

Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)

### loc/iloc

loc: 레이블기반 데이터 선택 - df.loc[행 레이블, 열 레이블]

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. 데이터 확인: Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)
2. loc/iloc: loc: 레이블기반 데이터 선택 - df.loc[행 레이블, 열 레이블]

## Code Highlights

### 데이터 전처리

`데이터 전처리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 이상치 - IQR 단일 변수 흐름이 주석과 함께 드러납니다.

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

### 추가 - 컬럼명 변경

`추가 - 컬럼명 변경`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 위와 같은 코드 - 딕셔너리 따로 지정 흐름이 주석과 함께 드러납니다.

```python
# 위와 같은 코드 - 딕셔너리 따로 지정
rename_dict = {
    'Order Date': 'order_date',
    'Ship Date': 'ship_date'
    }
df = df.rename(columns = rename_dict)
df.head(2)
```

### 정규화/표준화

`정규화/표준화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 위와 같은 코드 흐름이 주석과 함께 드러납니다.

```python
# 위와 같은 코드
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['sales_norm'] = scaler.fit_transform(df[['sales']])
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
