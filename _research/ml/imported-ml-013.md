---
title: "코딩실습13 10.결정트리와 앙상블(XGBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습13_10.결정트리와 앙상블(XGBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md"
excerpt: "XGBoost 회귀, XGBoost 분류 중심으로 구현 과정을 정리한 코딩실습13 10.결정트리와 앙상블(XGBoost) 기록입니다"
research_summary: "XGBoost 회귀, XGBoost 분류 중심으로 구현 과정을 정리한 코딩실습13 10.결정트리와 앙상블(XGBoost) 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다."
research_artifacts: "ipynb/md · 코드 12개 · 실행 11개"
code_block_count: 12
execution_block_count: 11
research_focus:
  - "XGBoost 회귀"
  - "XGBoost 분류"
research_stack:
  - "sklearn"
  - "xgboost"
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

XGBoost 회귀, XGBoost 분류 중심으로 구현 과정을 정리한 코딩실습13 10.결정트리와 앙상블(XGBoost) 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다.

**빠르게 볼 수 있는 포인트**: XGBoost 회귀, XGBoost 분류.

**남겨둔 자료**: `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다.

**주요 스택**: `sklearn`, `xgboost`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 12 |
| Execution Cells | 11 |
| Libraries | `sklearn`, `xgboost`, `numpy` |
| Source Note | `250827_코딩실습13_10.결정트리와 앙상블(XGBoost)` |

## What This Note Covers

- XGBoost 회귀
- XGBoost 분류

## Implementation Flow

1. XGBoost 회귀
2. XGBoost 분류

## Code Highlights

### XGBoost 회귀

`XGBoost 회귀`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4
)
model.fit(X_train, y_train)
```

### XGBoost 분류

`XGBoost 분류`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
model = xgb.XGBClassifier(
    objective='multi:softmax',                  # 다중 클래스 분류
    num_class=3                                 # objective='multi:softmax'와 num_class는 같이 써야함
)
model.fit(X_train, y_train)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).ipynb`, `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
