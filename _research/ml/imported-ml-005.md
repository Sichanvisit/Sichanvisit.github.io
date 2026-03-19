---
title: "코드실습5 7.DF 마스터하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250814_코드실습5_7.DF 마스터하기"
source_path: "11_Machine_Learning/Code_Snippets/250814_코드실습5_7.DF 마스터하기.md"
excerpt: "Sample Superstore 데이터 설명 (교육·실습용으로 자주 쓰이는 판매 주문 데이터셋)"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

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

## What I Worked On

- 1. 데이터 확인
- 드라이브 마운트 코드
- 데이터의 컬럼별 정보 확인
- 행과 열의 갯수 정보
- 기술 통계 요약

## Implementation Flow

1. 1. 데이터 확인
2. 드라이브 마운트 코드
3. 데이터의 컬럼별 정보 확인
4. 행과 열의 갯수 정보
5. 기술 통계 요약
6. 컬럼명 확인

## Code Highlights

### 데이터 전처리

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

### 데이터 전처리

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
