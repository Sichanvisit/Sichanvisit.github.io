---
title: "코딩실습10 10.결정트리와 앙상블(DT)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습10_10.결정트리와 앙상블(DT)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md"
excerpt: "- _reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현"
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
| Code Blocks | 26 |
| Execution Cells | 25 |
| Libraries | `matplotlib`, `warnings`, `sklearn`, `pandas` |
| Source Note | `250827_코딩실습10_10.결정트리와 앙상블(DT)` |

## What I Worked On

- 1. DT 회귀 실습
- 위 코드 판다스로 지정해 불러올 때
- 트리 시각화
- DT 분류 실습
- 변수명 추출

## Implementation Flow

1. 1. DT 회귀 실습
2. 위 코드 판다스로 지정해 불러올 때
3. 트리 시각화
4. DT 분류 실습
5. 변수명 추출
6. 3. 속성 중요도 실습

## Code Highlights

### 1. DT 회귀 실습

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
