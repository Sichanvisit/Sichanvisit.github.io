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

## What This Note Covers

### 요즘 배우는 것

파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링

### 나의 목표

마크다운으로 매일 학습 기록을 남기는 습관 만들기!

### matplotlib 실습

/ 포맷 문자열 / 설명 / 예시 출력 / / --------- / -------- / -------- / / %1.0f%% / 정수로 표시 / 25% / / %1.1f%% / 소수점 한 자리 / 25.0% / / %1.2f%% / 소수점 두 자리 / 25.00% /

### Key Step

np.array(): 넘파이 배열로 바꿔주는 함수

## Implementation Flow

1. 요즘 배우는 것: 파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링
2. 나의 목표: 마크다운으로 매일 학습 기록을 남기는 습관 만들기!
3. matplotlib 실습: / 포맷 문자열 / 설명 / 예시 출력 / / --------- / -------- / -------- / / %1.0f%% / 정수로 표시 / 25% / / %1.1f%% / 소수점 한 자리 / 25.0% / / %1.2f%% / 소수점 두 자리 / 25.00% /
4. Key Step: np.array(): 넘파이 배열로 바꿔주는 함수

## Code Highlights

### 기본 함수들

`기본 함수들`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 실습 과제1 - 상품 매출액 계산 답안 흐름이 주석과 함께 드러납니다.

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

`matplotlib 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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
