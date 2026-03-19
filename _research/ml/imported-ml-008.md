---
title: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md"
excerpt: "legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스..."
research_summary: "legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - l... 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "Iris 데이터로 이진 분류"
  - "Iris 데이터로 다중 분류"
  - "Softmax 이용한 다중 분류"
research_stack:
  - "sklearn"
  - "matplotlib"
  - "numpy"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - l... 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: Iris 데이터로 이진 분류, Iris 데이터로 다중 분류, Softmax 이용한 다중 분류.

**남겨둔 자료**: `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다.

**주요 스택**: `sklearn`, `matplotlib`, `numpy`

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

## What This Note Covers

### handles, _ = scatter.legend_elements() 코드 설명

legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - label: 0, 1, 2처럼 자동 생성된 클래스 이름...

### Key Step

Softmax 이용한 다중 분류

## Implementation Flow

1. handles, _ = scatter.legend_elements() 코드 설명: legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_...
2. Key Step: Softmax 이용한 다중 분류

## Code Highlights

### Iris 데이터로 이진 분류

`Iris 데이터로 이진 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
```

### Iris 데이터로 다중 분류

`Iris 데이터로 다중 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델링 & 시각화 흐름이 주석과 함께 드러납니다.

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
