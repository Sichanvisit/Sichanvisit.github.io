---
title: "코드실습3 4.데이터사이언스 Toolkit"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250812_코드실습3_4.데이터사이언스 Toolkit"
source_path: "11_Machine_Learning/Code_Snippets/250812_코드실습3_4.데이터사이언스 Toolkit.md"
excerpt: "- 파이썬 기초 문법 - 마크다운 정리법 - 데이터 시각화 - AI 엔지니어링"
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
| Code Blocks | 60 |
| Execution Cells | 59 |
| Libraries | `numpy`, `google`, `pandas`, `matplotlib`, `warnings` |
| Source Note | `250812_코드실습3_4.데이터사이언스 Toolkit` |

## What I Worked On

- 1. 마크다운 실습
- **자기소개 마크다운 미션**
- 이름
- 요즘 배우는 것
- 나의 목표

## Implementation Flow

1. 1. 마크다운 실습
2. **자기소개 마크다운 미션**
3. 이름
4. 요즘 배우는 것
5. 나의 목표
6. 2. Numpy 실습

## Code Highlights

### 4. matplotlib 실습

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

### 4. matplotlib 실습

```python
# 실습3 - 여러 그래프 시각화

plt.figure(figsize=(15, 4))

# 1. 키 분포
plt.subplot(1, 3, 1)
plt.hist(df['height'], bins=20)
plt.title("키 히스토그램")

# 2. 몸무게 분포
plt.subplot(1, 3, 2)
plt.hist(df['weight'], bins=20, color='gray')
plt.title("몸무게 히스토그램")

# 3. 산점도
plt.subplot(1, 3, 3)
plt.scatter(df['height'], df['weight'], alpha=0.6)
plt.title("키와 몸무게 산점도")

plt.tight_layout()
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
