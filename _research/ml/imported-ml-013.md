---
title: "코딩실습13 10.결정트리와 앙상블(XGBoost)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습13_10.결정트리와 앙상블(XGBoost)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습13_10.결정트리와 앙상블(XGBoost).md"
excerpt: "코딩실습13 10.결정트리와 앙상블(XGBoost)를 중심으로 분류 문제, 회귀 문제 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습13 10.결정트리와 앙상블(XGBoost)를 중심으로 분류 문제, 회귀 문제 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 XGBoost 회귀, XGBoost 분류 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 12개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, xgboost, numpy입니다."
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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>코딩실습13 10.결정트리와 앙상블(XGBoost)를 중심으로 학습한 내용을 정리한 ML 실습입니다.</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>원본 노트에서 데이터를 설명한 부분을 기준으로 실습 맥락을 정리했습니다.</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>분류 문제 · 회귀 문제 · 결정 트리와 앙상블</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>XGBoost 회귀 -&gt; XGBoost 분류</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 12 · 실행 11</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>sklearn, xgboost, numpy</td>
    </tr>
    </tbody>
  </table>
</div>

## What I Studied

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--notes">
    <thead>
      <tr>
        <th>개념</th>
        <th>핵심 설명</th>
        <th>코드에서 확인한 것</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">분류 문제</th>
      <td>분류는 입력 특성으로 클래스나 반응 여부를 예측하는 문제입니다. 모델은 각 샘플이 어떤 범주에 속하는지 확률 또는 라벨로 출력합니다.</td>
      <td>이 글에서는 가입 여부, 품종, 레이블 예측처럼 범주형 타깃을 다루는 실습 맥락으로 연결됩니다.</td>
    </tr>
    <tr>
      <th scope="row">회귀 문제</th>
      <td>회귀는 연속적인 수치를 예측하는 문제입니다. 예측값과 실제값의 차이를 오차로 계산해 모델 성능을 판단합니다.</td>
      <td>이 글에서는 수요량, 가격, 점수처럼 숫자 타깃을 예측하는 실습과 이어집니다.</td>
    </tr>
    <tr>
      <th scope="row">결정 트리와 앙상블</th>
      <td>결정 트리는 조건 분기로 예측 규칙을 만들고, 앙상블은 여러 모델의 예측을 묶어 편향과 분산을 함께 줄이는 접근입니다.</td>
      <td>이 글에서는 Decision Tree, RandomForest, XGBoost, Voting, Stacking 코드를 통해 여러 모델을 비교해 볼 수 있습니다.</td>
    </tr>
    <tr>
      <th scope="row">전처리와 입력 정리</th>
      <td>머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.</td>
      <td>이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.</td>
    </tr>
    </tbody>
  </table>
</div>

## How I Implemented It

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--steps">
    <thead>
      <tr>
        <th>단계</th>
        <th>구현 내용</th>
        <th>핵심 API</th>
        <th>코드 포인트</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">Step 1 · 데이터 불러오기</th>
      <td>
        <strong class="research-compact-table__main">XGBoost 회귀</strong>
        <span class="research-compact-table__sub">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 모델 구성</th>
      <td>
        <strong class="research-compact-table__main">XGBoost 분류</strong>
        <span class="research-compact-table__sub">XGBoost 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</span>
      </td>
      <td><code>XGBoost</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

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
