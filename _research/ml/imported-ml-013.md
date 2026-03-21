---
title: "10.결정트리와 앙상블(XGBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습13_10.결정트리와 앙상블(XGBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md"
excerpt: "코딩실습13 10.결정트리와 앙상블(XGBoost)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 XGBoost 회귀, XGBoost 분류 순서로 큰 장을 먼저 훑고, XGBoost 회귀, XGBoost 분류 같은 코드로 실제 구현을 이어서 확인할 수 있..."
research_summary: "코딩실습13 10.결정트리와 앙상블(XGBoost)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 XGBoost 회귀, XGBoost 분류 순서로 큰 장을 먼저 훑고, XGBoost 회귀, XGBoost 분류 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다."
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

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">코딩실습13 10.결정트리와 앙상블(XGBoost)에서 XGBoost 회귀, XGBoost 분류 흐름을 직접 따라가며 구현했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">XGBoost 회귀 -&gt; XGBoost 분류</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">특정 데이터셋 설명보다 XGBoost 회귀, XGBoost 분류 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">XGBoost 회귀 · XGBoost 분류</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">XGBoost 회귀 -&gt; XGBoost 분류</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 12 · 실행 11</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn, xgboost, numpy</div>
  </div>
</div>

## 원본 노트 흐름

### XGBoost 회귀

XGBoost 회귀와 관련된 핵심 흐름을 원본 노트 기준으로 다시 읽을 수 있게 정리했습니다.

- 읽을 포인트: 이 장의 설명을 먼저 읽고 아래 코드 섹션으로 내려가면 흐름이 더 자연스럽습니다.

### XGBoost 분류

XGBoost 분류와 관련된 핵심 흐름을 원본 노트 기준으로 다시 읽을 수 있게 정리했습니다.

- 읽을 포인트: 이 장의 설명을 먼저 읽고 아래 코드 섹션으로 내려가면 흐름이 더 자연스럽습니다.

## 구현 흐름

### 1. XGBoost 회귀

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: -
- 코드 포인트: -

### 2. XGBoost 분류

- 단계: 모델 구성
- 구현 의도: XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: `XGBoost`
- 코드 포인트: -

## 코드로 확인한 내용

### XGBoost 회귀

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
data = fetch_california_housing()
X = data.data
y = data.target
```

### XGBoost 분류

**직접 해본 단계**: 모델 구성

**핵심 API**: `XGBoost`

XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
model = xgb.XGBClassifier(
    objective='multi:softmax',                  # 다중 클래스 분류
    num_class=3                                 # objective='multi:softmax'와 num_class는 같이 써야함
)
model.fit(X_train, y_train)
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).ipynb`, `250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## 원문 미리보기

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
