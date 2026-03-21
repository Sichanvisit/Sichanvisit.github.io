---
title: "코드실습4 5. 기초 통계와 데이터 시각화"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250813_코드실습4_5. 기초 통계와 데이터 시각화"
source_path: "11_Machine_Learning/Code_Snippets/250813_코드실습4_5. 기초 통계와 데이터 시각화.md"
excerpt: "Seaborn 실습, 씨본 스타일, 상관관계 중심으로 구현 과정을 정리한 코드실습4 5"
research_summary: "Seaborn 실습, 씨본 스타일, 상관관계 중심으로 구현 과정을 정리한 코드실습4 5. 기초 통계와 데이터 시각화 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 37개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, seaborn입니다."
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

Seaborn 실습, 씨본 스타일, 상관관계 중심으로 구현 과정을 정리한 코드실습4 5. 기초 통계와 데이터 시각화 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 37개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, seaborn입니다.

**빠르게 볼 수 있는 포인트**: Seaborn 실습, 씨본 스타일, 상관관계.

**남겨둔 자료**: `ipynb/md` 원본과 37개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, seaborn입니다.

**주요 스택**: `matplotlib`, `warnings`, `numpy`, `seaborn`, `google`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 37 |
| Execution Cells | 35 |
| Libraries | `matplotlib`, `warnings`, `numpy`, `seaborn`, `google`, `pandas` |
| Source Note | `250813_코드실습4_5. 기초 통계와 데이터 시각화` |

## What I Studied

- Seaborn 실습
- 씨본 스타일
- 상관관계
- 박스 프롯 - 이상치 확인
- 박스 프롯 - 커스터마이징 (1)

## What I Tried in Code

1. 데이터 불러오기: CSV 데이터 불러오기
2. 시각화: 씨본 스타일
3. 구현 코드: import numpy as np
4. 시각화: 데이터 분포 시각화

## Code Evidence

### CSV 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

`CSV 데이터 불러오기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/body.csv')
df
```

### 씨본 스타일

**직접 해본 단계**: 시각화

`씨본 스타일`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
plt.figure(figsize=(4,3))
sns.set_palette(sns.color_palette("pastel")) # pastel, deep, muted....
sns.barplot(data=titanic_data, x='age', y='class', errorbar=None)
plt.show()
```

### import numpy as np

**직접 해본 단계**: 구현 코드

`import numpy as np`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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

`데이터 분포 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 박스 프롯 - 커스터마이징 (2) 같은 처리 포인트도 함께 남아 있습니다.

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

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

`데이터 분포 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 실습1 - 키와 몸무게 이상치 박스플롯 그리기, 모범답안 기본 - height 같은 처리 포인트도 함께 남아 있습니다.

```python
## 실습1 - 키와 몸무게 이상치 박스플롯 그리기
import numpy as np

# 모범답안 기본 - height
q1 = np.percentile(df['height'], 25)
q2 = np.percentile(df['height'], 50)
q3 = np.percentile(df['height'], 75)
iqr = q3 - q1

print("Q1:", q1)
print("Q2 (중앙값):", q2)
print("Q3:", q3)
print("IQR:", iqr)

plt.figure(figsize=(4,3))
plt.boxplot(df['height'], vert=False)
plt.title("height IQR")
plt.xlabel("값")
plt.show()
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

`데이터 분포 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다. 코드에는 박스 프롯 - 커스터마이징 (1) 같은 처리 포인트도 함께 남아 있습니다.

```python
# 박스 프롯 - 커스터마이징 (1)

plt.figure(figsize=(7,3))
plt.boxplot(
    x,
    vert = False,
    patch_artist=True,                                        # 박스 색을 채워라
    boxprops=dict(facecolor = 'skyblue', color = 'blue'),     # 박스 스타일
    medianprops=dict(color = 'red', linewidth = 3),           # 중앙값 선 스타일
    whiskerprops=dict(color = 'gray', linestyle = '--'),      # 수염 스타일
    flierprops=dict(marker='*', markersize=8)                 # 이상치 스타일
    )
plt.title("사분위수 시각화", fontsize=15, fontweight='bold')
plt.grid(axis = 'x', linestyle = '--', alpha=0.4)
plt.yticks([1], ['Group A'])
plt.show()
```

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `CSV 데이터 불러오기` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 시각화를 같이 남긴 이유

- 왜 필요한가: 숫자만 보면 놓치기 쉬운 분포와 이상치를 그래프로 확인해야 다음 전처리나 feature engineering 방향이 또렷해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `씨본 스타일` 코드를 통해 어떤 그래프를 보고 판단했는지 실습 흔적을 남겼습니다.
- 원리: 시각화는 데이터 분포를 직관적으로 드러내 모델 선택과 변수 설계의 근거를 만들어 줍니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `import numpy as np` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

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
