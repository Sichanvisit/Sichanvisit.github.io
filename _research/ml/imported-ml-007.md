---
title: "코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge)"
source_path: "11_Machine_Learning/Code_Snippets/250821_코딩실습7_9.기본 지도학습 알고리즘들 (Lasso, Ridge).md"
excerpt: "데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할 중심으로 구현 과정을 정리한 코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge) 기록입니다"
research_summary: "데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할 중심으로 구현 과정을 정리한 코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge) 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "데이터 불러오기"
  - "위와 같은 코드"
  - "테스트 데이터 트레이닝 데이터 분할"
research_stack:
  - "sklearn"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할 중심으로 구현 과정을 정리한 코딩실습7 9.기본 지도학습 알고리즘들 (Lasso, Ridge) 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다.

**빠르게 볼 수 있는 포인트**: 데이터 불러오기, 위와 같은 코드, 테스트 데이터 트레이닝 데이터 분할.

**남겨둔 자료**: `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다.

**주요 스택**: `sklearn`

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

## What This Note Covers

- 데이터 불러오기
- 위와 같은 코드
- 테스트 데이터 트레이닝 데이터 분할
- 모델링
- 릿지 회귀 모델링

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. Key Step: 테스트 데이터 트레이닝 데이터 분할

## Code Highlights

### 테스트 데이터 트레이닝 데이터 분할

`테스트 데이터 트레이닝 데이터 분할`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 테스트 데이터 트레이닝 데이터 분할 흐름이 주석과 함께 드러납니다.

```python
# 테스트 데이터 트레이닝 데이터 분할
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)
```

### 모델링

`모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델링 흐름이 주석과 함께 드러납니다.

```python
# 모델링
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
```

### 릿지 회귀 모델링

`릿지 회귀 모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 릿지 회귀 모델링 흐름이 주석과 함께 드러납니다.

```python
# 릿지 회귀 모델링
model_ridge = Ridge(alpha=0.9)
model_ridge.fit(X_train, y_train)
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

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
