---
title: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md"
excerpt: "- **legend_elements()** - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatte..."
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
| Libraries | `sklearn`, `matplotlib`, `numpy` |
| Source Note | `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)` |

## What I Worked On

- 1. Iris 데이터로 이진 분류
- 데이터 로드
- 모델 학습
- 시각화용 격자 생성 코드
- 시각화

## Implementation Flow

1. 1. Iris 데이터로 이진 분류
2. 데이터 로드
3. 모델 학습
4. 시각화용 격자 생성 코드
5. 시각화
6. 2. Iris 데이터로 다중 분류

## Code Highlights

### 1. Iris 데이터로 이진 분류

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
```

### 2. Iris 데이터로 다중 분류

```python
# 모델링 & 시각화

plt.figure(figsize=(10,3))

for i in range(3):
    binary_y = (y==i).astype(int)                  # OvR -> 이진 라벨 생성
    model = LogisticRegression()
    model.fit(X, binary_y)

    Z = model.predict(grid)
    Z = Z.reshape(xx.shape)

    plt.subplot(1, 3, i+1)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
    plt.scatter(X[:,0], X[:,1], c=binary_y, cmap='bwr', edgecolors='black')
    plt.title(f'Class {i} : {class_names[i]} vs Rest')
    plt.grid(True)

plt.tight_layout()
plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Source formats: `ipynb`, `md`
- Companion files: `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).ipynb`, `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`, `matplotlib.org`

## Note Preview

> - **legend_elements()** - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - label: 0, 1, 2처럼 자동 생성된 클래스 이름 문자열 - scatter.legend_elements()는 handles, label을 반환하지만, 클래스 이름을 실제 label로 사용해 보여주고자 함 - handles, _ = scatter.legend_elements()로 변수를 두 개 지정할 때, handles는 가져오고 labels는 무시한다는 의미로 **아래 밑줄**을 사용 - 아래 밑줄: 파이썬의 관례적인 표현 1. 사용하지 않는 값 무시 2. 표현식의 마지막 결과값 저장 3. 내부 문서 의미
