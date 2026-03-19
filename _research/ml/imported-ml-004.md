---
title: "코드실습4 5. 기초 통계와 데이터 시각화"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250813_코드실습4_5. 기초 통계와 데이터 시각화"
source_path: "11_Machine_Learning/Code_Snippets/250813_코드실습4_5. 기초 통계와 데이터 시각화.md"
excerpt: "ML Practice: Seaborn 실습, 씨본 스타일, 상관관계"
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
| Code Blocks | 37 |
| Execution Cells | 35 |
| Libraries | `matplotlib`, `warnings`, `numpy`, `seaborn`, `google`, `pandas` |
| Source Note | `250813_코드실습4_5. 기초 통계와 데이터 시각화` |

## What I Worked On

- 박스 프롯 - 이상치 확인
- 박스 프롯 - 커스터마이징 (1)
- 박스 프롯 - 커스터마이징 (2)
- 히스토그램 실습 (1)
- 히스토그램 실습 (2)

## Implementation Flow

1. 박스 프롯 - 이상치 확인
2. 박스 프롯 - 커스터마이징 (1)
3. 박스 프롯 - 커스터마이징 (2)
4. 히스토그램 실습 (1)
5. 히스토그램 실습 (2)
6. 히스토그램 실습 (3)

## Code Highlights

### 박스 프롯 - 커스터마이징 (2)

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

### 실습1 - 키와 몸무게 이상치 박스플롯 그리기

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
