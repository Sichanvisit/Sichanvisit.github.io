---
title: "코드실습4 5. 기초 통계와 데이터 시각화"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250813_코드실습4_5. 기초 통계와 데이터 시각화"
source_path: "11_Machine_Learning/Code_Snippets/250813_코드실습4_5. 기초 통계와 데이터 시각화.md"
excerpt: "Seaborn 실습, 씨본 스타일, 상관관계 중심으로 구현 과정을 정리한 코드실습4 5"
research_summary: "Seaborn 실습, 씨본 스타일, 상관관계 중심으로 구현 과정을 정리한 코드실습4 5. 기초 통계와 데이터 시각화 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 37개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, seaborn입니다."
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

Seaborn 실습, 씨본 스타일, 상관관계 중심으로 구현 과정을 정리한 코드실습4 5. 기초 통계와 데이터 시각화 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 37개 코드 블록, 35개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, numpy, seaborn입니다.

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

## What This Note Covers

- Seaborn 실습
- 씨본 스타일
- 상관관계
- 박스 프롯 - 이상치 확인
- 박스 프롯 - 커스터마이징 (1)

## Implementation Flow

1. Key Step: 박스 프롯 - 커스터마이징 (1)
2. Key Step: 박스 프롯 - 커스터마이징 (2)
3. Key Step: 실습1 - 키와 몸무게 이상치 박스플롯 그리기
4. Key Step: 모범답안 기본 - height

## Code Highlights

### 박스 프롯 - 커스터마이징 (2)

`박스 프롯 - 커스터마이징 (2)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 박스 프롯 - 커스터마이징 (2) 흐름이 주석과 함께 드러납니다.

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

### 씨본 스타일

`씨본 스타일`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
plt.figure(figsize=(4,3))
sns.set_palette(sns.color_palette("pastel")) # pastel, deep, muted....
sns.barplot(data=titanic_data, x='age', y='class', errorbar=None)
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
