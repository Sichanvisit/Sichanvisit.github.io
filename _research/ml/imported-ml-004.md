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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>박스 프롯. 커스터마이징 (1)</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>원본 노트에서 데이터를 설명한 부분을 기준으로 실습 맥락을 정리했습니다.</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>구현 중심 학습</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>CSV 데이터 불러오기 -&gt; 씨본 스타일 -&gt; import numpy as np</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 37 · 실행 35</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>matplotlib, warnings, numpy, seaborn 외 1</td>
    </tr>
    </tbody>
  </table>
</div>

## What I Studied

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--notes">
    <thead>
      <tr>
        <th>개념</th>
        <th>핵심 설명</th>
        <th>코드에서 확인한 것</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">구현 중심 학습</th>
      <td>이 글은 개념 설명과 함께 실제 코드를 통해 학습 흐름을 다시 따라가도록 정리된 ML 실습 기록입니다.</td>
      <td>데이터 입력, 처리, 모델링, 평가 가운데 실제로 손댄 단계를 중심으로 읽을 수 있습니다.</td>
    </tr>
    </tbody>
  </table>
</div>

## How I Implemented It

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--steps">
    <thead>
      <tr>
        <th>단계</th>
        <th>구현 내용</th>
        <th>핵심 API</th>
        <th>코드 포인트</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">Step 1 · 데이터 불러오기</th>
      <td>
        <strong class="research-compact-table__main">CSV 데이터 불러오기</strong>
        <span class="research-compact-table__sub">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</span>
      </td>
      <td><code>pd.read_csv</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 시각화</th>
      <td>
        <strong class="research-compact-table__main">씨본 스타일</strong>
        <span class="research-compact-table__sub">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</span>
      </td>
      <td><code>matplotlib</code> <code>seaborn</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 구현 코드</th>
      <td>
        <strong class="research-compact-table__main">import numpy as np</strong>
        <span class="research-compact-table__sub">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 4 · 시각화</th>
      <td>
        <strong class="research-compact-table__main">데이터 분포 시각화</strong>
        <span class="research-compact-table__sub">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</span>
      </td>
      <td><code>matplotlib</code></td>
      <td>박스 프롯 - 커스터마이징 (2)</td>
    </tr>
    <tr>
      <th scope="row">Step 5 · 구현 코드</th>
      <td>
        <strong class="research-compact-table__main">x = [-100, 5, 7, 8, 9, 10, 12, 13, 14, 20, 79]</strong>
        <span class="research-compact-table__sub">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 6 · 시각화</th>
      <td>
        <strong class="research-compact-table__main">Seaborn 실습</strong>
        <span class="research-compact-table__sub">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</span>
      </td>
      <td><code>matplotlib</code> <code>seaborn</code></td>
      <td>barplot</td>
    </tr>
    </tbody>
  </table>
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
