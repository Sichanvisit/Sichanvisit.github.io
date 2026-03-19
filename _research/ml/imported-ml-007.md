---
title: "코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md"
excerpt: "ML Practice: 데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할"
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
| Code Blocks | 19 |
| Execution Cells | 18 |
| Libraries | `sklearn` |
| Source Note | `250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge)` |

## What I Worked On

- 데이터 불러오기
- 위와 같은 코드
- 테스트 데이터 트레이닝 데이터 분할
- 모델링
- 릿지 회귀 모델링

## Implementation Flow

1. 데이터 불러오기
2. 위와 같은 코드
3. 테스트 데이터 트레이닝 데이터 분할
4. 모델링
5. 릿지 회귀 모델링

## Code Highlights

### 테스트 데이터 트레이닝 데이터 분할

```python
# 테스트 데이터 트레이닝 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)
```

### 모델링

```python
# 모델링
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md`
- Source formats: `ipynb`, `md`
- Companion files: `250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).ipynb`, `250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
