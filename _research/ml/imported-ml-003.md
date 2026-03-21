---
title: "코드실습3 4.데이터사이언스 Toolkit"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250812_코드실습3_4.데이터사이언스 Toolkit"
source_path: "11_Machine_Learning/Code_Snippets/250812_코드실습3_4.데이터사이언스 Toolkit.md"
excerpt: "코드실습3 4.데이터사이언스 Toolkit를 중심으로 구현 중심 학습 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코드실습3 4.데이터사이언스 Toolkit를 중심으로 구현 중심 학습 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 csv파일 불러오는 실습, matplotlib 실습 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 60개 코드 블록, 59개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 numpy, google, pandas, matplotlib입니다."
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

<div class="research-doc-hero">
  <div class="research-doc-summary">
    <p class="research-doc-summary__label">문제 설정</p>
    <p class="research-doc-summary__body">파이썬 기초 문법. 마크다운 정리법</p>
  </div>
  <div class="research-doc-meta">
<div class="research-doc-card">
  <p class="research-doc-card__label">데이터 맥락</p>
  <p class="research-doc-card__value">파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">핵심 개념</p>
  <p class="research-doc-card__value">구현 중심 학습</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">구현 포인트</p>
  <p class="research-doc-card__value">csv파일 불러오는 실습 · matplotlib 실습 · 기본 함수들</p>
</div>
  </div>
  <div class="research-doc-stats">
<div class="research-doc-stat">
  <span>소스</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-stat">
  <span>자료</span>
  <strong>코드 60 · 실행 59</strong>
</div>
<div class="research-doc-stat">
  <span>주요 스택</span>
  <strong>numpy, google, pandas, matplotlib 외 1</strong>
</div>
  </div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">구현 중심 학습</p>
  <p class="research-note-card__body">이 글은 개념 설명과 함께 실제 코드를 통해 학습 흐름을 다시 따라가도록 정리된 ML 실습 기록입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>데이터 입력, 처리, 모델링, 평가 가운데 실제로 손댄 단계를 중심으로 읽을 수 있습니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-list">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 데이터 불러오기</p>
  <p class="research-step-card__title">csv파일 불러오는 실습</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>pd.read_csv</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> CSV 파일 불러오기 실습</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 시각화</p>
  <p class="research-step-card__title">matplotlib 실습</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 구현 코드</p>
  <p class="research-step-card__title">기본 함수들</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 실습 과제1 - 상품 매출액 계산 답안</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 구현 코드</p>
  <p class="research-step-card__title">나의 목표</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
</div>

## Code Evidence

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

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
import numpy as np

arr = np.array([[2, 3, 4,], [5, 6, 7]])

arr
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
