---
title: "코딩실습11 10.결정트리와 앙상블(RF)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습11_10.결정트리와 앙상블(RF)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md"
excerpt: "ML Practice: 1. 단일 디시전 트리 실습, 2. 랜덤 포레스트 실습"
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
| Code Blocks | 16 |
| Execution Cells | 16 |
| Libraries | `numpy`, `matplotlib`, `sklearn`, `graphviz` |
| Source Note | `250827_코딩실습11_10.결정트리와 앙상블(RF)` |

## What I Worked On

- 1. 단일 디시전 트리 실습
- make_moons 데이터 불러오기 - 암기 X
- 데이터셋 시각화 (어떻게 생겼는지 눈으로 확인)
- 정확도 계산
- 추가 - 보기 좋은 시각화

## Implementation Flow

1. 1. 단일 디시전 트리 실습
2. make_moons 데이터 불러오기 - 암기 X
3. 데이터셋 시각화 (어떻게 생겼는지 눈으로 확인)
4. 정확도 계산
5. 추가 - 보기 좋은 시각화
6. 산점도 시각화할 함수 정의

## Code Highlights

### 1. 단일 디시전 트리 실습

```python
# 추가 - 보기 좋은 시각화

from sklearn.tree import export_graphviz
import graphviz

dot_data = export_graphviz(
    dt_clf,
    feature_names=['Feature1', 'Feature2'],
    class_names=['Class0', 'Class1'],
    filled=True,
    rounded=True
)

graph = graphviz.Source(dot_data)

graph
```

### 1. 단일 디시전 트리 실습

```python
# 산점도 시각화할 함수 정의

def plot_decision_boundary(model, X, y, title="Decision Boundary"):
    # 컬러맵 정의
    cmap_light = ListedColormap(['#FFAAAA', '#AAAAFF'])  # 배경 색
    cmap_bold = ListedColormap(['#FF0000', '#0000FF'])   # 점 색

    # 그리드 영역 설정
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    # 모델로 예측한 결정 경계
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # 시각화
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, cmap=cmap_light)  # 결정 경계 색
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=30)
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.grid(True)
    plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습11_10.결정트리와 앙상블(RF).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습11_10.결정트리와 앙상블(RF).ipynb`, `250827_코딩실습11_10.결정트리와 앙상블(RF).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
