---
title: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md"
excerpt: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다"
research_summary: "코딩실습9 9.기본 지도학습 알고리즘들 (K-fold & 그리드서치)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 회귀 문제, 피처 엔지니어링, 평가 지표 해석 순서로 큰 장을 먼저 훑고, 1990년 캘리포니아 주택 데이터, from sklearn.datasets... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, numpy입니다."
research_artifacts: "ipynb/md · 코드 7개 · 실행 6개"
code_block_count: 7
execution_block_count: 6
research_focus:
  - "https"
  - "1990년 캘리포니아 주택 데이터"
  - "데이터 로드"
research_stack:
  - "sklearn"
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

## 글 한눈에 보기

| 항목 | 내용 |
|------|------|
| 문제 설정 | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html 데이터 피쳐 설명 |
| 원본 구조 | 1990년 캘리포니아 주택 데이터 |
| 데이터 맥락 | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html 데이터 피쳐 설명 |
| 핵심 주제 | 회귀 문제 · 피처 엔지니어링 · 평가 지표 해석 |
| 구현 흐름 | 1990년 캘리포니아 주택 데이터 -> from sklearn.datasets import fetch_california_hou... |
| 자료 | ipynb / md · 코드 7 · 실행 6 |
| 주요 스택 | sklearn, numpy |

## 원본 노트 흐름

### 1990년 캘리포니아 주택 데이터

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html 데이터 피쳐 설명

- 읽을 포인트: 데이터 구조와 주의할 변수부터 읽고 실험 방향을 정리하는 구간입니다.

## 구현 흐름

### 1. 1990년 캘리포니아 주택 데이터

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: -
- 코드 포인트: 데이터 로드

### 2. from sklearn.datasets import fetch_california_housing

- 단계: 환경 준비
- 구현 의도: 지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다.
- 핵심 API: `GridSearchCV`, `RMSE`
- 코드 포인트: -

## 코드로 확인한 내용

### 1990년 캘리포니아 주택 데이터

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 데이터 로드
X, y = fetch_california_housing(return_X_y=True)
```

### from sklearn.datasets import fetch_california_housing

**직접 해본 단계**: 환경 준비

**핵심 API**: `GridSearchCV`, `RMSE`

지표를 계산해 성능을 비교하고 결과를 해석하는 평가 단계입니다.

```python
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import numpy as np
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md`
- Source formats: `ipynb`, `md`
- Companion files: `250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).ipynb`, `250822_코딩실습9_9.기본 지도학습 알고리즘들 (K-fold & 그리드서치).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## 원문 미리보기

> https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html
> 데이터 피쳐 설명
