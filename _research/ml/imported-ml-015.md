---
title: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN)"
source_path: "11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md"
excerpt: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 분류 문제, 전처리와 입력 정리, 평가 지표 해석 순서로 큰 장을 먼저 훑고, wine = load_wine(), StandardScaler 스케일링 같은 코..."
research_summary: "코딩실습15 9.기본 지도학습 알고리즘들(KNN)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 분류 문제, 전처리와 입력 정리, 평가 지표 해석 순서로 큰 장을 먼저 훑고, wine = load_wine(), StandardScaler 스케일링 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 13개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn입니다."
research_artifacts: "ipynb/md · 코드 13개 · 실행 13개"
code_block_count: 13
execution_block_count: 13
research_focus:
  - "사이킷런 링크"
  - "표준화"
  - "최적의 K값으로 학습 및 평가"
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

## 글 한눈에 보기

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <colgroup>
      <col class="research-compact-table__col research-compact-table__col--label">
      <col class="research-compact-table__col research-compact-table__col--value">
    </colgroup>
    <thead>
      <tr>
        <th>항목</th>
        <th>내용</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">문제 설정</th>
        <td>사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html 클래스 수: 3개. 샘플 수: 총 178개 (class_0...</td>
      </tr>
      <tr>
        <th scope="row">원본 구조</th>
        <td>원본 마크다운의 큰 섹션 흐름을 기준으로 이 실습을 다시 읽을 수 있게 정리했습니다.</td>
      </tr>
      <tr>
        <th scope="row">데이터 맥락</th>
        <td>사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html 클래스 수: 3개 - 샘플 수: 총 178개 (class_...</td>
      </tr>
      <tr>
        <th scope="row">주요 장</th>
        <td>분류 문제 · 전처리와 입력 정리 · 평가 지표 해석</td>
      </tr>
      <tr>
        <th scope="row">구현 흐름</th>
        <td>wine = load_wine() -&gt; StandardScaler 스케일링 -&gt; KNN 모델 구성</td>
      </tr>
      <tr>
        <th scope="row">자료</th>
        <td>ipynb / md · 코드 13 · 실행 13</td>
      </tr>
      <tr>
        <th scope="row">주요 스택</th>
        <td>sklearn</td>
      </tr>
    </tbody>
  </table>
</div>

## 원본 노트 흐름

### 분류 문제

분류는 입력 특성으로 클래스나 반응 여부를 예측하는 문제입니다. 모델은 각 샘플이 어떤 범주에 속하는지 확률 또는 라벨로 출력합니다.

- 읽을 포인트: 이 글에서는 가입 여부, 품종, 레이블 예측처럼 범주형 타깃을 다루는 실습 맥락으로 연결됩니다.

### 전처리와 입력 정리

머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.

- 읽을 포인트: 이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.

### 평가 지표 해석

평가 지표는 예측 결과를 수치화해 모델의 강점과 약점을 읽게 해주는 기준입니다. 문제 유형에 맞는 지표를 골라야 실험 비교가 가능합니다.

- 읽을 포인트: 이 글에서는 F1, Recall, Accuracy, RMSLE 같은 지표를 실제 코드에서 계산하는 흐름으로 연결됩니다.

## 구현 흐름

### 1. wine = load_wine()

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: -
- 코드 포인트: -

### 2. StandardScaler 스케일링

- 단계: 전처리
- 구현 의도: 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.
- 핵심 API: `StandardScaler`
- 코드 포인트: 표준화

### 3. KNN 모델 구성

- 단계: 모델 구성
- 구현 의도: KNN 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: -
- 코드 포인트: -

### 4. 예측 결과 점검

- 단계: 평가
- 구현 의도: 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.
- 핵심 API: -
- 코드 포인트: 최적의 K값으로 학습 및 평가

### 5. from sklearn.datasets import load_wine

- 단계: 환경 준비
- 구현 의도: 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.
- 핵심 API: `train_test_split`, `StandardScaler`, `accuracy_score`
- 코드 포인트: -

### 6. best_k = grid.best_params_['n_neighbors']

- 단계: 구현 코드
- 구현 의도: best_k = grid.best_params_['n_nei... 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: -

## 코드로 확인한 내용

### wine = load_wine()

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
wine = load_wine()
X, y = wine.data, wine.target
target_names = wine.target_names
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

**핵심 API**: `StandardScaler`

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

```python
# 표준화

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)
```

### KNN 모델 구성

**직접 해본 단계**: 모델 구성

KNN 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
```

### 예측 결과 점검

**직접 해본 단계**: 평가

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

```python
# 최적의 K값으로 학습 및 평가
best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test_scaled)
```

### from sklearn.datasets import load_wine

**직접 해본 단계**: 환경 준비

**핵심 API**: `train_test_split`, `StandardScaler`, `accuracy_score`

전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
```

### best_k = grid.best_params_['n_neighbors']

**직접 해본 단계**: 구현 코드

best_k = grid.best_params_['n_nei... 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python
best_k = grid.best_params_['n_neighbors']
best_k
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md`
- Source formats: `ipynb`, `md`
- Companion files: `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).ipynb`, `250828_코딩실습15_9.기본 지도학습 알고리즘들(KNN).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## 원문 미리보기

> 사이킷런 링크: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html
> - 클래스 수: 3개 - 샘플 수: 총 178개 (class_0: 59, class_1: 71, class_2: 48) - 피처 수: 13개 (연속형, 모두 양수) - 출처: UCI 머신러닝 저장소의 Wine 데이터셋 (값 일부 포맷화됨)
