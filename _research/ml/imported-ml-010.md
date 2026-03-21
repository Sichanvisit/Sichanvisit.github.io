---
title: "코딩실습10 10.결정트리와 앙상블(DT)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250827_코딩실습10_10.결정트리와 앙상블(DT)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md"
excerpt: "코딩실습10 10.결정트리와 앙상블(DT)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 DT 회귀 실습, DT 분류 실습, 속성 중요도 실습 순서로 큰 장을 먼저 훑고, DT 회귀 실습, DT 분류 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니..."
research_summary: "코딩실습10 10.결정트리와 앙상블(DT)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 DT 회귀 실습, DT 분류 실습, 속성 중요도 실습 순서로 큰 장을 먼저 훑고, DT 회귀 실습, DT 분류 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다."
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

## 글 한눈에 보기

| 항목 | 내용 |
|------|------|
| 문제 설정 | 코딩실습10 10.결정트리와 앙상블(DT)에서 DT 회귀 실습, DT 분류 실습, 속성 중요도 실습 흐름을 직접 따라가며 구현했습니다. |
| 원본 구조 | DT 회귀 실습 -> DT 분류 실습 -> 속성 중요도 실습 -> 사전 가지치기 실습 |
| 데이터 맥락 | 특정 데이터셋 설명보다 DT 회귀 실습, DT 분류 실습, 속성 중요도 실습 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다. |
| 주요 장 | DT 회귀 실습 · DT 분류 실습 · 속성 중요도 실습 · 사전 가지치기 실습 |
| 구현 흐름 | DT 회귀 실습 -> DT 분류 실습 -> 데이터 분포 시각화 |
| 자료 | ipynb / md · 코드 26 · 실행 25 |
| 주요 스택 | matplotlib, warnings, sklearn, pandas |

## 원본 노트 흐름

### DT 회귀 실습

_reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현

- 읽을 포인트: 세부 흐름: 위 코드 판다스로 지정해 불러올 때, 트리 시각화

#### 위 코드 판다스로 지정해 불러올 때

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

#### 트리 시각화

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

### DT 분류 실습

변수명 추출 같은 코드를 직접 따라가며 DT 분류 실습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 변수명 추출

#### 변수명 추출

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

### 속성 중요도 실습

특성 이름 가져오기, 각 특성의 중요도 값 가져오기 같은 코드를 직접 따라가며 속성 중요도 실습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 특성 이름 가져오기, 각 특성의 중요도 값 가져오기

#### 특성 이름 가져오기

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

#### 각 특성의 중요도 값 가져오기

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

### 사전 가지치기 실습

하이퍼 파라미터 조합 같은 코드를 직접 따라가며 사전 가지치기 실습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 하이퍼 파라미터 조합

#### 하이퍼 파라미터 조합

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

## 구현 흐름

### 1. DT 회귀 실습

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: -
- 코드 포인트: 위 코드 판다스로 지정해 불러올 때

### 2. DT 분류 실습

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: `DecisionTree`, `matplotlib`
- 코드 포인트: -

### 3. 데이터 분포 시각화

- 단계: 시각화
- 구현 의도: 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.
- 핵심 API: `matplotlib`
- 코드 포인트: -

### 4. 사전 가지치기 실습

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: `DecisionTree`
- 코드 포인트: 하이퍼 파라미터 조합

### 5. 속성 중요도 실습

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: -

## 코드로 확인한 내용

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

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md`
- Source formats: `ipynb`, `md`
- Companion files: `250827_코딩실습10_10.결정트리와 앙상블(DT).ipynb`, `250827_코딩실습10_10.결정트리와 앙상블(DT).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## 원문 미리보기

> - _reg: 회귀의 관례적 표현 - _clf: 분류의 관례적 표현
