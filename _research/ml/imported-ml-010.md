---
title: "코딩실습10 10.결정트리와 앙상블(DT)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습10_10.결정트리와 앙상블(DT)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md"
excerpt: "_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현"
research_summary: "_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다."
research_artifacts: "ipynb/md · 코드 26개 · 실행 25개"
code_block_count: 26
execution_block_count: 25
research_focus:
  - "_reg"
  - "DT 회귀 실습"
  - "DT 분류 실습"
research_stack:
  - "matplotlib"
  - "warnings"
  - "sklearn"
  - "pandas"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다.

**빠르게 볼 수 있는 포인트**: _reg, DT 회귀 실습, DT 분류 실습.

**남겨둔 자료**: `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다.

**주요 스택**: `matplotlib`, `warnings`, `sklearn`, `pandas`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 26 |
| Execution Cells | 25 |
| Libraries | `matplotlib`, `warnings`, `sklearn`, `pandas` |
| Source Note | `250827_코딩실습10_10.결정트리와 앙상블(DT)` |

## What This Note Covers

### DT 회귀 실습

_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현

### Key Step

위 코드 판다스로 지정해 불러올 때

### Key Step

각 특성의 중요도 값 가져오기

## Implementation Flow

1. DT 회귀 실습: _reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현
2. Key Step: 위 코드 판다스로 지정해 불러올 때
3. Key Step: 각 특성의 중요도 값 가져오기

## Code Highlights

### DT 회귀 실습

`DT 회귀 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 트리 시각화 흐름이 주석과 함께 드러납니다.

```python
from sklearn.tree import plot_tree

# 트리 시각화
plt.figure(figsize=(20, 10))
plot_tree(dt_reg,
          max_depth=3,
          filled=True,
          rounded=True,
          fontsize=10,
          feature_names=data.feature_names
          )
plt.title("결정 트리 시각화")
plt.show()
```

### DT 분류 실습

`DT 분류 실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
dt_clf = DecisionTreeClassifier(random_state=42)
dt_clf.fit(X_clf, y_clf)

plt.figure(figsize=(20,10))
plot_tree(
    dt_clf,
    feature_names=feature_names_clf,
    class_names=class_names_clf,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("결정 트리 분류")
plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습10_10.결정트리와 앙상블(DT).ipynb`, `250827_코딩실습10_10.결정트리와 앙상블(DT).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - _reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현
