---
title: "코딩실습10 10.결정트리와 앙상블(DT)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습10_10.결정트리와 앙상블(DT)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md"
excerpt: "코딩실습10 10.결정트리와 앙상블(DT)를 중심으로 회귀 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습10 10.결정트리와 앙상블(DT)를 중심으로 회귀 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 DT 회귀 실습, DT 분류 실습 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다."
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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>_reg: 회귀의 관례적 표현. _clf: 분류의 관례적 표현</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>원본 노트에서 데이터를 설명한 부분을 기준으로 실습 맥락을 정리했습니다.</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>회귀 문제 · 결정 트리와 앙상블 · 전처리와 입력 정리</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>DT 회귀 실습 -&gt; DT 분류 실습 -&gt; 데이터 분포 시각화</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 26 · 실행 25</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>matplotlib, warnings, sklearn, pandas</td>
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
    <tr>
      <th scope="row">피처 엔지니어링</th>
      <td>피처 엔지니어링은 원본 컬럼을 그대로 쓰지 않고 문제에 맞는 새 특징을 설계해 모델이 더 유용한 패턴을 학습하도록 돕는 과정입니다.</td>
      <td>이 글에서는 시간 파생 변수, 조건식 기반 플래그, 도메인 규칙을 반영한 새 컬럼 생성 코드가 여기에 해당합니다.</td>
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
        <strong class="research-compact-table__main">DT 회귀 실습</strong>
        <span class="research-compact-table__sub">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>위 코드 판다스로 지정해 불러올 때</td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 피처 가공</th>
      <td>
        <strong class="research-compact-table__main">DT 분류 실습</strong>
        <span class="research-compact-table__sub">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</span>
      </td>
      <td><code>DecisionTree</code> <code>matplotlib</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 시각화</th>
      <td>
        <strong class="research-compact-table__main">데이터 분포 시각화</strong>
        <span class="research-compact-table__sub">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</span>
      </td>
      <td><code>matplotlib</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 4 · 피처 가공</th>
      <td>
        <strong class="research-compact-table__main">사전 가지치기 실습</strong>
        <span class="research-compact-table__sub">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</span>
      </td>
      <td><code>DecisionTree</code></td>
      <td>하이퍼 파라미터 조합</td>
    </tr>
    <tr>
      <th scope="row">Step 5 · 피처 가공</th>
      <td>
        <strong class="research-compact-table__main">속성 중요도 실습</strong>
        <span class="research-compact-table__sub">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

### DT 회귀 실습

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 위 코드 판다스로 지정해 불러올 때

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)

X_reg = df.values
y_reg = data.target
```

### DT 분류 실습

**직접 해본 단계**: 피처 가공

**핵심 API**: `DecisionTree`, `matplotlib`

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

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

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

!apt-get update -qq
!apt-get install fonts-nanum* -qq

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings(action='ignore')

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf' # 나눔 고딕
font_name = fm.FontProperties(fname=path, size=10).get_name() # 기본 폰트 사이즈 : 10
plt.rc('font', family=font_name)

fm.fontManager.addfont(path)
```

### 사전 가지치기 실습

**직접 해본 단계**: 피처 가공

**핵심 API**: `DecisionTree`

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
# 하이퍼 파라미터 조합
dt_model_2 = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    max_features='sqrt'
)
dt_model_2.fit(X_train, y_train)
```

### 속성 중요도 실습

**직접 해본 단계**: 피처 가공

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

```python
importance_df = pd.DataFrame({
    'Feature' : feature_names,
    'Importance' : importances
    })
importance_df = importance_df.sort_values(by='Importance', ascending=False)
importance_df
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
