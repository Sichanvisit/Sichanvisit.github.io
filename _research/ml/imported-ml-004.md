---
title: "코드실습4 5. 기초 통계와 데이터 시각화"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250813_코드실습4_5. 기초 통계와 데이터 시각화"
source_path: "11_Machine_Learning/Code_Snippets/250813_코드실습4_5. 기초 통계와 데이터 시각화.md"
excerpt: "코드실습4 5"
research_summary: "코드실습4 5. 기초 통계와 데이터 시각화를 중심으로 구현 중심 학습 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 CSV 데이터 불러오기, 씨본 스타일 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 37개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, seaborn입니다."
research_artifacts: "ipynb/md · 코드 37개 · 실행 35개"
code_block_count: 37
execution_block_count: 35
research_focus:
  - "Seaborn 실습"
  - "씨본 스타일"
  - "상관관계"
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
  - practice
---

<div class="research-doc-hero">
  <div class="research-doc-summary">
    <p class="research-doc-summary__label">문제 설정</p>
    <p class="research-doc-summary__body">박스 프롯. 커스터마이징 (1)</p>
  </div>
  <div class="research-doc-meta">
<div class="research-doc-card">
  <p class="research-doc-card__label">핵심 개념</p>
  <p class="research-doc-card__value">구현 중심 학습</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">구현 포인트</p>
  <p class="research-doc-card__value">CSV 데이터 불러오기 · 씨본 스타일 · import numpy as np</p>
</div>
  </div>
  <div class="research-doc-stats">
<div class="research-doc-stat">
  <span>소스</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-stat">
  <span>자료</span>
  <strong>코드 37 · 실행 35</strong>
</div>
<div class="research-doc-stat">
  <span>주요 스택</span>
  <strong>matplotlib, warnings, numpy, seaborn 외 1</strong>
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
  <p class="research-step-card__title">CSV 데이터 불러오기</p>
  <p class="research-step-card__body">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>pd.read_csv</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 시각화</p>
  <p class="research-step-card__title">씨본 스타일</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code> <code>seaborn</code></p>

</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 구현 코드</p>
  <p class="research-step-card__title">import numpy as np</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 시각화</p>
  <p class="research-step-card__title">데이터 분포 시각화</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> 박스 프롯 - 커스터마이징 (2)</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 구현 코드</p>
  <p class="research-step-card__title">x = [-100, 5, 7, 8, 9, 10, 12, 13, 14, 20, 79]</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 시각화</p>
  <p class="research-step-card__title">Seaborn 실습</p>
  <p class="research-step-card__body">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</p>
  <p class="research-step-card__meta"><span>핵심 API</span> <code>matplotlib</code> <code>seaborn</code></p>
  <p class="research-step-card__meta"><span>코드 포인트</span> barplot</p>
</div>
</div>

## Code Evidence

### CSV 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/body.csv')
df
```

### 씨본 스타일

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`, `seaborn`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
plt.figure(figsize=(4,3))
sns.set_palette(sns.color_palette("pastel")) # pastel, deep, muted....
sns.barplot(data=titanic_data, x='age', y='class', errorbar=None)
plt.show()
```

### import numpy as np

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

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

### x = [-100, 5, 7, 8, 9, 10, 12, 13, 14, 20, 79]

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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

### Seaborn 실습

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`, `seaborn`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
# barplot

plt.figure(figsize=(6,3))
sns.barplot(data=df, x='height_bin', y='weight', errorbar=None)
plt.title("키와 몸무게 평균 비교")
plt.xticks(rotation=45)
plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250813_코드실습4_5. 기초 통계와 데이터 시각화.md`
- Source formats: `ipynb`, `md`
- Companion files: `250813_코드실습4_5. 기초 통계와 데이터 시각화.ipynb`, `250813_코드실습4_5. 기초 통계와 데이터 시각화.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 팔레트
