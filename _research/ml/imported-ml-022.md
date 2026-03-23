---
title: "4 Portuguese Bank Data Marketing"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md"
excerpt: "Portuguese Bank Data Marketing의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 전처리, 모델링, 데이터 시각화 순서로 큰 장을 먼저 훑고, XGBoost 모델 학습, XGBoost / RandomFores... 같은 코드로..."
research_summary: "Portuguese Bank Data Marketing의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 전처리, 모델링, 데이터 시각화 순서로 큰 장을 먼저 훑고, XGBoost 모델 학습, XGBoost / RandomFores... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다."
research_artifacts: "ipynb/md · 코드 88개 · 실행 45개"
code_block_count: 88
execution_block_count: 45
research_focus:
  - "🚨 SMOTE 적용시 주의사항"
  - "=> 반드시 훈련 데이터에만 적용할 것!"
  - "예금 가입이 높은 구간대를 따로 구별한 파생변수를 추가하여 모델링"
research_stack:
  - "urllib"
  - "helper_c0z0c_dev"
  - "time"
  - "pandas"
  - "numpy"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - archive-note
---

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축. 마케팅 캠페인의 효율성을 높이는 전략을 도출</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">미션 설명 -&gt; 데이터 확인 -&gt; 데이터 전처리 -&gt; 데이터 시각화 -&gt; 모델링</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">데이터 전처리 · 모델링 · 데이터 시각화 · 데이터 확인</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">CSV 데이터 불러오기 -&gt; XGBoost / RandomForest 모델 구성 -&gt; 학습/검증 데이터 분리</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 88 · 실행 45</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">urllib, helper_c0z0c_dev, time, pandas 외 1</div>
  </div>
</div>

# 미션 설명

- 결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축
- 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출
    - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측
    - 마케팅 캠페인의 효율성을 높이는 것
- **최종 목표** : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를 바탕으로 비즈니스 전략을 제시하는 것

### 데이터 설명

1. 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터
2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터
3. 결측치는 unknown으로 표기

| 컬럼명              | 설명                              |
| ---------------- | ------------------------------- |
| `age`            | 나이 (숫자)                         |
| `job`            | 직업 (범주형)                        |
| `marital`        | 결혼 여부 (범주형)                     |
| `education`      | 교육 수준 (범주형)                     |
| `default`        | 신용 불량 여부 (범주형)                  |
| `housing`        | 주택 대출 여부 (범주형)                  |
| `loan`           | 개인 대출 여부 (범주형)                  |
| `contact`        | 연락 유형 (범주형)                     |
| `month`          | 마지막 연락 월 (범주형)                  |
| `day_of_week`    | 마지막 연락 요일 (범주형)                 |
| `duration`       | 마지막 연락 지속 시간, 초 단위 (숫자)         |
| `campaign`       | 캠페인 동안 연락 횟수 (숫자)               |
| `pdays`          | 이전 캠페인 후 지난 일수 (숫자)             |
| `previous`       | 이전 캠페인 동안 연락 횟수 (숫자)            |
| `poutcome`       | 이전 캠페인의 결과 (범주형)                |
| `emp.var.rate`   | 고용 변동률 (숫자)                     |
| `cons.price.idx` | 소비자 물가지수 (숫자)                   |
| `cons.conf.idx`  | 소비자 신뢰지수 (숫자)                   |
| `euribor3m`      | 3개월 유리보 금리 (숫자)                 |
| `nr.employed`    | 고용자 수 (숫자)                      |
| `y`              | 정기 예금 가입 여부 (`'yes'` 또는 `'no'`) |

### 강사 Tip

> 데이터 설명을 읽었을 때, 해당 데이터는 크게 3가지가 독특함

1. 결측치를 unknown으로 처리한 것
2. 999라는 수치가 실제로는 無의 상태인 것
3. duration이 종속변수를 대변하는 피쳐인 점

> 특히 분류문제는 어떤 값을 평가의 기준으로 할 것인가에 따라 모델의 성능을 향상시키는 방법론이 달라질 수 있음

**<고민해 볼 문제>**
1. 위양성 (False Positive)를 줄인다 => Precision
2. False Negative를 줄인다 -> 진짜 Positive를 놓치지 않는다 => Recall

비즈니스 상황에 따라 어떤 점수를 높일 것인지 달라짐.
해당 데이터의 경우,

1. 콜센터, 마케팅 자원이 제한적이다

    => **Precision**을 높이는 게 중요

 괜히 "가입할 거야!"라고 예측된 수십만 명에게 연락했는데, 실제 가입자는 몇 명 안 되면 인건비 낭비가 큼

 2. 모든 잠재 고객을 놓치지 않고 잡고 싶다

    => **Recall**을 높이자

 고객을 많이 확보하는 게 중요하고, 인건비보다 고객 전환율이 더 중요할 경우

---

## 참고 - 코랩(쥬피터 노트북) matplotlib 한글 오류 해결법

김명환님 제공
git: https://github.com/c0z0c/jupyter_hangul

```python
# 한줄 설치
from urllib.request import urlretrieve; urlretrieve("https://raw.githubusercontent.com/c0z0c/jupyter_hangul/refs/heads/beta/helper_c0z0c_dev.py", "helper_c0z0c_dev.py")
import helper_c0z0c_dev as helper
```

```python
!pip install catboost
```

# 1. 데이터 확인

```python
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, BaggingClassifier, AdaBoostClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
import lightgbm as lgb
from imblearn.over_sampling  import SMOTE
#from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
#from sklearn.model_selection import GridSearchCV
```

```python
df = pd.read_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bank-additional-full.csv", sep=';')
df.head()
```

```python
df.info()
```

```python
df.shape
```

```python
df.describe()
```

### 1차 데이터 확인

1. 종속변수 y의 이진화 필요

2. 확인할 컬럼들
    - campaign 75%까지의 값은 문제없어 보이나 최대값이 극도로 큰 느낌
    - pdays와 previous 전반적으로 값 동일 -> 특이
        - pdays 설명: 999 means client was not previously contacted
        - previous: 이전에 연락을 받지 못한 고객이 많은 데이터

3. 범주형 변수 라벨 인코딩으로 모두 변환
    - 모델링 위해
    - 트리 모델의 경우 범주의 순서 영향성이 낮은 모델이라 라벨 인코딩을 해줘도 문제 없을 것으로 예상

4. 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed'와 같은 경제지표들 단위가 다름
    - 정규화/표준화로 조정하여 실험
        => 트리 모델의 장점은 데이터 스케일링에 큰 영향을 받지 않는다는 것! 단, 기본 학습기로 로지스틱 회귀 등도 사용할 예정이므로 정규화/표준화 진행 필요

5. 결측치
    - 데이터 설명: Missing Attribute Values: There are several missing values in some categorical attributes, all coded with the "unknown" label.
    - 결측치 전체적으로 확인 필요

6. 데이터는 전체적으로 세 분류로 나눠짐
    - 고객 정보, 캠페인 정보, 경제지표

### 특정 컬럼 데이터 확인

**1. Duration**

전화를 받고 정기예금을 가입한 사람의 여부를 따지는 것이 이번 분석의 종속변수

즉, 마지막 통화시간인 duration은 종속변수에 큰 영향을 줄 것으로 판단함

- 데이터설명된 txt 파일에서 명시가 된 부분
- 컬럼 자체를 삭제하고 모델링 진행

**2. pdays**

이전 캠페인 이후 지난 날짜

- 999의 데이터가 많다면, 이전 날짜에 연락을 받은 적이 없는 고객이 많다는 뜻
- 해당 데이터를 어떻게 처리할 것인지 고민 필요

**3. previous**

이전 캠페인 동안 연락 횟수

- 은행 마케팅 캠페인에 연락을 자주 받는게 흔할까?
- 이전 캠페인 연락받아서 가입하고 또 가입할 수 있을까?

```python
# 종속변수 y값 비율 확인
df['y'].value_counts(normalize=True)
```

=> 정기 예금 가입 결과 비율이 낮은 데이터

- 현실적으로 마케팅을 통해 가입하는 것의 비율이 낮을 것으로 판단
- 단, 모델이 학습하는데 데이터 불균형이 좋지 않음
    - 비율에 대해 추후 고민해 볼 필요있음

```python
# campaign - 이상치 확인

plt.figure(figsize=(4,4))
plt.boxplot(df['campaign'])
plt.title('campaign 이상치 확인 - 박스플롯')
plt.grid(True, alpha=0.4)
plt.show()
```

```python
# campaign - 막대그래프

plt.figure(figsize=(8,3))
plt.hist(df['campaign'], bins=50, edgecolor='black')
plt.title('campaign 컬럼 확인')
plt.xlabel('campaign')
plt.ylabel('count')
plt.grid(True, alpha=0.4)
plt.show()
```

- 대부분의 고객은 1~3회 내외의 연락만 받음
    - right-skewed(오른쪽으로 치우친) 분포
- 로그 변환 없이 보면 값이 너무 안 나와서 로그로 바꾸고 확인 필요
- 이상치 존재

```python
# campaign

plt.figure(figsize=(8,3))
plt.hist(df['campaign'], bins=50, edgecolor='black')
plt.title('campaign 컬럼 확인 - 로그 변환')
plt.xlabel('campaign')
plt.ylabel('count')
plt.yscale('log')                                                        # 로그 변환
plt.grid(True, alpha=0.4)
plt.show()
```

```python
# pdays 딥다이브

np.sort(df['pdays'].unique())
```

```python
# pdays==999 비율 확인

len(df[df['pdays']==999])/len(df) * 100
```

pdays의 값 중 999는 고객이 이전에 연락을 한번도 받지 않았을 때

- 이 값은 모델링에 굉장히 중요한 영향을 미칠 것으로 판단됨
- 이전에 연락을 받은 것과 안 받은 것을 구분하는 독립변수 필요

**고민**
1. 파생변수 추가해 모델링 할까
    - 변수 실험 필요
2. XGboost나 LightGBM같은 Nan처리 기능있는 모델을 쓸 것인가

```python
# previous 딥다이브

np.sort(df['previous'].unique())
```

```python
# previous 시각화

plt.figure(figsize=(5,3))
plt.hist(df['previous'], edgecolor='black')
plt.title('previous 컬럼 확인')
plt.xlabel('previous')
plt.ylabel('count')
plt.grid(True)
plt.show()
```

대부분의 고객이 거의 연락을 받은 적이 없음

=> 연락 유무에 대한 파생변수 필요

---

경제 지표 관련 변수들은 그래프를 그려봤으나 딱히 의미가 있진 않아 모두 삭제

```python
# 전체 컬럼 unknown 카운트 정리

unknown_summary = {}

for col in df.select_dtypes(include='object').columns:
    unknown_count = (df[col] == 'unknown').sum()
    if unknown_count > 0:
        unknown_summary[col] = {
            'count' : unknown_count,
            'ratio' : round(unknown_count / len(df) * 100, 2)
            }

unknown_df = pd.DataFrame(unknown_summary).T
unknown_df = unknown_df.sort_values(by='ratio', ascending=False)
unknown_df
```

```python
# poutcome (이전 캠페인 결과) 시각화

plt.figure(figsize=(6,4))

sns.countplot(data=df, x='poutcome', hue = 'y')
plt.title('이전 캠페인 결과')
plt.xlabel('이전 캠페인 성공 유무')
plt.ylabel('count')
plt.show()
```

```python
# poutcome 비율 확인

df.groupby(by='poutcome')['y'].value_counts(normalize=True)*100
```

=> 이전에 성공한 마케팅 캠페인은 이번 정기 예금 가입 전환이 높음. 이전에 성공한 마케팅의 요인을 상세하게 분석하여 추후 적절한 마케팅 방안을 제안하는 방식도 중요할 것으로 판단.

# 2. 데이터 전처리

### 1) 중복값 처리

```python
# 중복행 확인

df.duplicated().sum()
```

```python
# 중복행 제거

df = df.drop_duplicates()
```

### 2) 결측치 처리

데이터 설명대로라면 결측치가 없어야 하나, 확인차 코딩해봄

```python
# 결측치 확인

df.isnull().sum()
```

=> 진짜 없는 것 확인

- unknown 처리 중요

### 3) 이상치 처리

```python
# 이상치 확인 - age

plt.figure(figsize=(3, 3))
plt.boxplot(df['age'])
plt.title('age 이상치')
plt.xlabel('age')
plt.show()
```

```python
# 나이 비율보고 싶어서 바이올린 플롯으로 다시 그림

plt.figure(figsize=(3, 3))
sns.violinplot(df['age'])
plt.title('age 이상치')
plt.xlabel('age')
plt.show()
```

**age**

- 최소 17, 최대 98
- 최대와 최소는 극단적인 값이나 완전히 비현실적인 수치는 아님
    - 두 값이 불가능하다는 완벽한 증거는 없음

=> 이상치라고 판단하지 않음

```python
# campaign - 이상치 확인 (데이터 확인 파트와 동일)

plt.figure(figsize=(4,4))
plt.boxplot(df['campaign'])
plt.title('campaign 이상치 확인 - 박스플롯')
plt.grid(True, alpha=0.4)
plt.show()
```

```python
# 비율보고 싶어서 바이올린 플롯으로 다시 그림

plt.figure(figsize=(4, 4))
sns.violinplot(df['campaign'])
plt.title('campaign 이상치')
plt.xlabel('campaign')
plt.show()
```

```python
# campaign 비율 확인
len(df[df['campaign']>16])/len(df) * 100
```

**campaign**

- campaign값이 작은 것은 현실적으로 충분히 납득되는 상황
    - 대부분의 고객이 마케팅 캠페인 전화를 자주 받지 않았을 것임
- IQR방식으로 이상치 제거할 경우 Q1 - Q1*IQR쪽 제거는 데이터의 현실성을 반영하지 못할 것으로 판단
- 특정 수치(16)의 근거는 없지만, 대체로 전체 데이터 중 1~2% 값의 변경은 경험적으로 안정적 수치 (강사 Tip)
- campaign이 16이상인 값은 이상치로 간주하고 윈저라이징 사용
    - **Winsorizing**
        - 위키피디아: https://en.wikipedia.org/wiki/Winsorizing
        - 극단적인 값을 다른 값으로 대체하는 것

```python
# campaign 이상치 제거 - 윈저라이징
df['campaign'] = df['campaign'].clip(upper=15)
```

그 외 여러 컬럼에 대해 이상치 제거가 필요한지 고민하였으나, 최종적으로 진행하지 않기도 판단

**이유**

머신러닝 모델링은 결국 많은 데이터를 컴퓨터가 스스로 학습하게 하는 방식.

특별하게 잘못 입력되었거나, 명백한 자료에 기반한 오류를 발견한 상황이 아니기 때문에 다른 컬럼의 이상치 제거는 하지 않음.

### 4) duration 컬럼

```python
# duration 컬럼 삭제

df.drop(columns = ['duration'], inplace=True)
```

### 5) 종속변수 이진 변환

```python
# 종속변수 y 이진 변환

df['y'] = df['y'].map({'yes': 1, 'no': 0})
```

### 6) 파생변수 추가

```python
# pdays - 이전에 연락받은 적 있는지 여부
df['was_contacted_before'] = (df['pdays'] != 999).astype(int)
```

```python
df.head(3)
```

### 7) 범주형 변수 처리

범주형 변수 라벨 전에 인코딩 전에 unknown값은 라벨 인코딩에서 제외하고

나머지 값으로 라벨 인코딩을 한 뒤,

unknown은 각각 컬럼의 최대 라벨값 +1로 지정

```python
# unknown을 제외하고 라벨 인코딩 후 unknown은 max+1 값 부여하는 함수 생성

def custom_label_encode(df, column):

    # unknown 제외하고 각각 컬럼 라벨 인코딩
    known_values = df[column][df[column] != 'unknown']
    le = LabelEncoder()
    le.fit(known_values)

    # 인코딩 적용
    max_label = len(le.classes_)
    encoded_col = df[column].apply(lambda x: le.transform([x])[0] if x != 'unknown' else max_label)

    return encoded_col, le, max_label
```

```python
# 라벨 인코딩위한 변수 설정
categorical_cols = df.select_dtypes(include='object').columns
```

```python
# 범주형 변수 라벨 인코딩 진행 => 시간 걸림

for col in categorical_cols:
    encoded_col, le, max_label = custom_label_encode(df, col)
    df[col + '_encoded'] = encoded_col
```

```python
df.columns
```

### 8) unknown 및 pdays=999 추가 처리

- 일반 트리모델(결정 트리)와 일반 앙상블(랜덤 포레스트 & 그레디언트 부스팅)은 결측치 자체를 모델링 할 수 없음

- 그러나 XGBoost는 missing 파라미터로 자동 처리 가능한 반면, LightGBM과 Catboost는 NaN을 자동 처리해주는 기능이 존재

> XGBoost 계열 모델링을 위해 unknown과 pdays의 999를 결측치로 자동 지정할 컬럼 생성

```python
# object 타입 중 'unknown'을 포함한 컬럼만 선택
target_cols = [col for col in df.select_dtypes(include='object').columns if 'unknown' in df[col].unique()]
```

```python
# unknown을 결측치로 처리하고, 그 뒤 나머지 값 라벨 인코딩하여 파생변수 지정
for col in target_cols:
    new_col = f"{col}_na"
    df[new_col] = df[col].replace('unknown', np.nan)
    le = LabelEncoder()
    notna_mask = df[new_col].notna()
    df.loc[notna_mask, new_col] = le.fit_transform(df.loc[notna_mask, new_col])
    df[new_col] = pd.to_numeric(df[new_col], errors='coerce')
```

```python
# pdays==999 값 NaN으로 변환하며 파생 변수 생성
df['pdays_na'] = df['pdays'].replace(999, np.nan)
```

```python
df.columns
```

# 3. 데이터 시각화

```python
# 수치형, 범주형 구분
num_cols = df.select_dtypes(include=[np.number]).drop(columns=['y']).columns
cat_cols = df.select_dtypes(exclude=[np.number]).columns
```

```python
# 수치형 변수 5구간으로 나누기
df_binned = df.copy()
for col in num_cols:
    df_binned[col] = pd.qcut(df_binned[col], q=5, duplicates='drop')
```

**qcut함수**

데이터를 분위수 기준으로 구간화하는 함수

- 데이터를 같은 개수의 그룹으로 나누는 것

- cut함수와 비교
    - cut은 단순히 값의 범위로 나눌때, qcut은 예를 들어 최상위 25%, 상위 25%, 중간 25%, 하위 25%로 나눌때 사용

```python
# 시각화
ncols = 3
nrows = int(np.ceil((len(num_cols) + len(cat_cols)) / ncols))       # ceil(): 위쪽 정수로 올림하는 함수

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(18, 4*nrows))
axes = axes.flatten()

all_cols = list(num_cols) + list(cat_cols)

for i, col in enumerate(all_cols):
    ax = axes[i]
    tmp = df_binned.groupby(col)['y'].mean().reset_index()
    sns.barplot(x=col, y='y', data=tmp, ax=ax)
    ax.set_title(f"{col} vs Yes 비")
    ax.set_ylabel("가입한 비율")
    ax.set_xlabel(col)
    ax.tick_params(axis='x', rotation=45)

for j in range(i+1, len(axes)):
    axes[j].set_visible(False)

plt.tight_layout()
plt.show()
```

- 수치형 변수의 경우 5분할을 했지만, 고유값이 적은 emp.var.rate같은 컬럼은 두 구간을 합쳐 총 4구간 생성
- 그 외 다른 수치형 변수 역시 데이터가 특정 값에 몰려있거나 고유값이 적을때는 5분할 되지 않음

- 범주형은 범주에 따른 비율로 표현

### 그래프 결과 해석

#### 고객 특성 관련 변수

- age
    - 중년층(30~40대)과 고연령층(60대 이상)에서 Yes 비율이 다소 높음

- job
    - 학생, 은퇴자, 블루칼라보다는 관리직, 기술직, 자영업, 실업자 집단에서 가입률 차이가 존재. 특히 학생의 Yes 비율이 상당히 높음

- education
    - 고등교육(대학 학위, 전문과정) 집단에서 Yes 비율이 더 높음

👉 즉, 학생·고학력자·특정 직업군이 금융상품 가입에 긍정적으로 반응

---

#### 이전 캠페인 관련 변수

- campaign
    - 연락 횟수가 적을수록 Yes 비율이 높음 => 과도한 반복 접촉은 효과 낮음

- previous / pdays / poutcome

    - 이전에 **연락한 적 없던 고객(previous=0)** 은 가입률이 낮음

    - 하지만, 이전 캠페인에서 **성공 경험이 있는 고객(poutcome=success)** 은 이번에도 Yes 비율이 매우 높음(약 60%)

- month
    - 특정 달(may, aug, oct, dec)의 가입률이 높음

👉 반복 접촉보다, 이전 캠페인 성과가 있었던 고객이 가장 중요한 타깃이며, 특정 월에 캠페인이 집중적으로 진행된 것이라 예상

---
#### 경제/거시 지표 관련 변수

- euribor3m (3개월 대출 금리)
    - Euribo: 유럽은행협회(EBF : 브뤼셀 소재)와 국제딜러협회(ACI : 파리 소재)가 지정한 57개 은행들의 대출금리를 집계, 발표하는 유러화 금리
        - 참조 사이트: 국민은행 https://kbthink.com/dictionary/view.html?dictId=KED-00002890
    - 금리가 낮을수록 Yes 비율이 확연히 높음

- emp.var.rate (고용변동률)
    - 값이 낮거나 음수일 때 Yes 비율이 높음 -> 경제가 불안정 혹은 변동이 마이너스일수록 캠페인 반응률이 상대적으로 좋음

- cons.conf.idx (소비자 신뢰지수)
    - 지수가 낮을수록 Yes 비율이 높음 -> 소비 심리가 위축될 때 금융상품에 가입하는 경향
    - 미래 대비의 목적으로 신뢰지수가 낮을때 예금이 증가한다는 경향성이 있음
        - 참조 사이트: 기획재정부 시사경제 용어사전
        https://www.moef.go.kr/sisa/dictionary/detail?idx=1501#:~:text=%EC%86%8C%EB%B9%84%EC%9E%90%EA%B0%80%20%EC%B2%B4%EA%B0%90%ED%95%98%EB%8A%94%20%EA%B2%BD%EC%A0%9C,%EC%A0%80%EC%B6%95%ED%95%98%EA%B3%A0%20%EC%A0%81%EA%B2%8C%20%EC%86%8C%EB%B9%84%ED%95%9C%EB%8B%A4.

👉 종합하면, 경기 침체 상황일수록 고객이 상품에 더 많이 가입하는 경향이 뚜렷함

### 데이터 시각화 후 추가 파생변수 생성

```python
# 나이 관련
df["is_target_age"] = ((df["age"].between(30, 45)) | (df["age"] >= 60)).astype(int)

# 직업 관련
df["is_student_or_retired"] = df["job"].isin(["student", "retired"]).astype(int)

# 학력 관련
df["is_high_edu"] = df["education"].isin(["university.degree", "professional.course"]).astype(int)

# 이전 캠페인 성공 경험
df["had_prev_success"] = (df["poutcome"] == "success").astype(int)

# 연락 방식이 휴대폰인지 아닌지
df["is_cellular"] = (df["contact"] == "cellular").astype(int)

# 성과가 높았던 월인지
df["is_target_month"] = df["month"].isin(["may", "aug", "oct", "dec"]).astype(int)

# 경제 지표 관련
df["low_euribor3m"] = (df["euribor3m"] < df["euribor3m"].median()).astype(int)
df["neg_emp_var_rate"] = (df["emp.var.rate"] < 0).astype(int)
df["low_cons_conf"] = (df["cons.conf.idx"] < df["cons.conf.idx"].median()).astype(int)

# 연락 횟수
df["few_contacts"] = (df["campaign"] <= 2).astype(int)
```

# 4. 모델링

### 1) 1차 모델링

범주형 변수 인코딩 한 값 + was_contacted_before로 가장 기본 모델링 진행

- 적용 모델: 결정 트리, 보팅, 배깅, 랜덤 포레스트, Adaboost, XGBoost, 스택킹

```python
feature_names =['age', 'job_encoded', 'marital_encoded', 'education_encoded', 'default_encoded',
                'housing_encoded', 'loan_encoded', 'contact_encoded', 'month_encoded', 'pdays',
                'day_of_week_encoded','campaign', 'was_contacted_before', 'previous', 'poutcome_encoded',
                'emp.var.rate', 'cons.price.idx', 'cons.conf.idx','euribor3m', 'nr.employed']
```

```python
target_name = 'y'
```

```python
# 데이터 분할
X = df[feature_names]
y = df[target_name]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```python
# 모델 정의
dt = DecisionTreeClassifier()
rf = RandomForestClassifier()
bag = BaggingClassifier()
ada = AdaBoostClassifier()
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
voting = VotingClassifier(estimators=[('dt', dt), ('rf', rf), ('xgb', xgb)])
stacking = StackingClassifier(estimators=[('rf', rf), ('xgb', xgb)], final_estimator=LogisticRegression())
```

```python
# 모델 평가
models = {
    'Decision Tree': dt,
    'Random Forest': rf,
    'Bagging': bag,
    'AdaBoost': ada,
    'XGBoost': xgb,
    'Voting': voting,
    'Stacking': stacking
}

results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds)
    rec = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    results.append({
        'Model': name,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1 Score': f1
    })
```

```python
# 결과 확인
results_df = pd.DataFrame(results)
results_df
```

```python
# classification report 확인 위해 추가

for name, model in models.items():
    preds = model.predict(X_test)
    print(f"--------- {name}  classification report ---------")
    print(classification_report(y_test, preds))
```

- Adaboost의 Precision 점수는 좋은편
- 데이터의 불균형이 매우 심각함
- 이 경우 accuracy점수 자체는 의미가 없음
    - 대다수 클래스(0)를 모두 '0'으로만 예측해도 90%의 정확도를 얻을 수 있기 때문
- 알고리즘별 accuracy나 precision 점수는 높으나 1일때 예측도는 굉장히 낮음

    => 이는 결국 가입할 고객을 잘 찾지 못하는 것!

> ### **👉 class가 1일 때 점수가 높은 방향으로 모델링!**

**방법론**

1. 알고리즘 레벨에서의 불균형 처리
    - 클래스 가중치 (Class Weights) - XGBoost의  class_weight 또는 scale_pos_weight 파라미터
        - https://xgboost.readthedocs.io/en/stable/parameter.html
2. 오버샘플링 - 소수 클래스 증가
     - SMOTE
2. 언더샘플링 - 다수 클래스 감소
    - Random Under-sampling

---

### 2) 2차 모델링

XGBoost의 scale_pos_weight 파라미터 사용

**<scale_pos_weight>**
- 클래스의 중요도를 조정하는 파라미터
    - Neg, Pos 모두 가능
- 특히 **0/1 불균형이 심한 이진 분류(binary classification)** 에서 사용
- 현재 데이터에는 양성 클래스가 굉장히 적으므로 Yes에 가중치를 줄 수 있도록 조정

=> 결과적으로 이 방식을 쓴다면 **Recall** 의 점수 향상

**<공식>**

scale_pos_weight = (Negative 클래스 개수) / (Positive 클래스 개수)
- scale_pos_weight = 88 / 12 ≈ 7.33

=> XGBoost가 Yes(Positive 클래스)를 학습할 때, 가중치를 약 7배 더 줘서 불균형 문제를 완화시켜 준다는 의미

```python
# 클래스 비율 계산
neg, pos = y_train.value_counts()
scale = neg / pos
```

```python
# 모델 정의 및 학습 - XGBoost
xgb = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss',
    scale_pos_weight=scale,
    random_state=42
)
xgb.fit(X_train, y_train)
```

```python
# 모델 평가
preds = xgb.predict(X_test)
probs = xgb.predict_proba(X_test)[:, 1]                        # ROC-AUC 스코어를 위해 준비. [:, 1]: y=1일 확률만 가져오겠다는 뜻

acc = accuracy_score(y_test, preds)
prec = precision_score(y_test, preds, zero_division=0)         # zero_division=0: 분모=0일 때 결과값을 0으로 대체 (예측한 게 없으니 성능은 0점으로 처리)
rec = recall_score(y_test, preds)
f1 = f1_score(y_test, preds, zero_division=0)
roc_auc = roc_auc_score(y_test, probs)

results = []
results = [{
    'Model': 'XGBoost',
    'Accuracy': acc,
    'Precision': prec,
    'Recall': rec,
    'F1 Score': f1,
    'ROC-AUC': roc_auc
}]
```

```python
# 결과 확인
results_df = pd.DataFrame(results)
results_df
```

```python
# classification report 확인 위해 추가

print("--------- XGBoost  classification report ---------")
print(classification_report(y_test, preds))
```

=> XGBoost 모델과 이 모델을 베이스로 쓰는 경우 Recall과  F1 score가 일부 상승하는 결과를 얻었으나, 아직 점수가 괜찮은 것은 아님. 불균형 데이터 자체를 바꿔주는게 필요함

## 3) 3차 모델링

예금 가입이 높은 구간대를 따로 구별한 파생변수를 추가하여 모델링

- XGBoost는 scale_pos_weight 파라미터 사용

```python
feature_names =['age', 'job_encoded', 'marital_encoded', 'education_encoded', 'default_encoded',
                'housing_encoded', 'loan_encoded', 'contact_encoded', 'month_encoded', 'pdays',
                'day_of_week_encoded','campaign', 'was_contacted_before', 'previous', 'poutcome_encoded',
                'emp.var.rate', 'cons.price.idx', 'cons.conf.idx','euribor3m', 'nr.employed',
                'is_student_or_retired', 'is_high_edu', 'had_prev_success','is_cellular', 'is_target_month',
                'low_euribor3m', 'neg_emp_var_rate','low_cons_conf', 'few_contacts', 'is_target_age']
```

```python
target_name = 'y'
```

```python
# 데이터 분할
X = df[feature_names]
y = df[target_name]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

```python
# 모델 정의
dt = DecisionTreeClassifier()
rf = RandomForestClassifier()
bag = BaggingClassifier()
ada = AdaBoostClassifier()
xgb = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss',
    scale_pos_weight=scale,
    random_state=42
)
voting = VotingClassifier(estimators=[('dt', dt), ('rf', rf), ('xgb', xgb)])
stacking = StackingClassifier(estimators=[('rf', rf), ('xgb', xgb)], final_estimator=LogisticRegression())
```

```python
# 모델 평가
models = {
    'Decision Tree': dt,
    'Random Forest': rf,
    'Bagging': bag,
    'AdaBoost': ada,
    'XGBoost': xgb,
    'Voting': voting,
    'Stacking': stacking
}

results = []
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds)
    rec = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    results.append({
        'Model': name,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1 Score': f1
    })
```

```python
# 결과 확인
results_df = pd.DataFrame(results)
results_df
```

=> 모델별 점수의 등락은 있으나, 모든 모델의 Recall점수가 상승했고, F1 score가 처음으로 0.4대 점수가 나옴

```python
# classification report 확인 위해 추가

for name, model in models.items():
    preds = model.predict(X_test)
    print(f"--------- {name}  classification report ---------")
    print(classification_report(y_test, preds))
```

## 4) 4차 모델링

SMOTE사용

```python
feature_names =['age', 'job_encoded', 'marital_encoded', 'education_encoded', 'default_encoded',
                'housing_encoded', 'loan_encoded', 'contact_encoded', 'month_encoded', 'pdays',
                'day_of_week_encoded','campaign', 'was_contacted_before', 'previous', 'poutcome_encoded',
                'emp.var.rate', 'cons.price.idx', 'cons.conf.idx','euribor3m', 'nr.employed',
                'is_student_or_retired', 'is_high_edu', 'had_prev_success','is_cellular', 'is_target_month',
                'low_euribor3m', 'neg_emp_var_rate','low_cons_conf', 'few_contacts', 'is_target_age']
```

```python
# 데이터 분할 및 SMOTE 적용
X = df[feature_names]
y = df[target_name]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
```

##### SMOTE 적용시 주의사항

=> 반드시 훈련 데이터에만 적용할 것!

전체 데이터를 통해 나온 결과는 데이터 누수(정보 교환)이 일어난 뒤 결과이기 때문에 점수가 높을 수 밖에 없음

```python
# SMOTE 적용후 데이터 비율 확인
len(y_resampled[y_resampled==0])/len(y_resampled)
```

```python
# 모델 정의
dt = DecisionTreeClassifier()
rf = RandomForestClassifier()
bag = BaggingClassifier()
ada = AdaBoostClassifier()
xgb = XGBClassifier(
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42
)
voting = VotingClassifier(estimators=[('dt', dt), ('rf', rf), ('xgb', xgb)], voting='soft')
stacking = StackingClassifier(estimators=[('rf', rf), ('xgb', xgb)], final_estimator=LogisticRegression(), passthrough=True)
```

```python
# 모델 평가 - 시간이 오래 걸려 시간 테스트

start_time = time.time()

models = {
    'Decision Tree': dt,
    'Random Forest': rf,
    'Bagging': bag,
    'AdaBoost': ada,
    'XGBoost': xgb,
    'Voting': voting,
    'Stacking': stacking
}

results = []
for name, model in models.items():
    model.fit(X_resampled, y_resampled)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds)
    rec = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    results.append({
        'Model': name,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1 Score': f1
    })

end_time = time.time()

print(f"-------- total processing -------- \n {end_time-start_time} seconds")
```

```python
results_df = pd.DataFrame(results)
results_df
```

-  3차 모델링 대비 Precision의 점수는 대부분의 모델에서 떨어졌지만 XGBoost에선 상승

- Recall점수는 Stacking과 XGBoost 제외 다른 모델에선 큰 폭으로 상승하는 경향

=> F1 score가 전체적으로 안정적이 되며 최고점 0.45기록

```python
# classification report 확인 위해 추가

for name, model in models.items():
    preds = model.predict(X_test)
    print(f"--------- {name}  classification report ---------")
    print(classification_report(y_test, preds))
```

**모델링 결과 정리**

1. SMOTE 적용 뒤, 점수는 좋으나 처리에 시간이 걸림
    - SMOTE는 KNN을 기반(디폴트 k_neighbors = 5)

2. AdaBoost 모델의 Recall 점수가 눈에 띄게 상승
    - 현재 데이터 기준 베이스라인이 10% 내외인것에 비해서는 의미있는 성과

## 5) 5차 모델링

독립변수 분할하여 모델링

```python
# 독립변수를 고객정보 feature_customer와 경제지표 feature_economic로 나누어 모델링

feature_customer = ['age', 'job_encoded', 'marital_encoded', 'education_encoded',
                    'default_encoded', 'housing_encoded', 'loan_encoded', 'contact_encoded',
                    'month_encoded', 'day_of_week_encoded', 'campaign', 'was_contacted_before', 'previous',
                    'poutcome_encoded','is_student_or_retired', 'is_high_edu', 'had_prev_success','is_cellular',
                    'is_target_month', 'is_target_age']
feature_economic = ['emp.var.rate', 'cons.price.idx', 'cons.conf.idx',
                    'euribor3m', 'nr.employed','low_euribor3m', 'neg_emp_var_rate']
```

위 모델링 과정에서 시간이 오래 걸려 데이터 넘파이로 변환하며 모델링 진행

```python
# 종속변수 넘파이 변환
y = df[target_name].values
```

```python
# 고객 정보 독립변수 넘파이 변환 및 데이터 나누기
X_customer = df[feature_customer].values.astype("float32")                      # 메모리 절약 위해 float32 지정

Xc_train, Xc_test, yc_train, yc_test = train_test_split(X_customer, y, test_size=0.3, stratify=y, random_state=42)

smote = SMOTE(random_state=42)
Xc_resampled, yc_resampled = smote.fit_resample(Xc_train, yc_train)
```

```python
# 경제 지표 독립변수 넘파이 변환 및 데이터 나누기
X_economic = df[feature_economic].values.astype("float32")                      # 메모리 절약 위해 float32 지정
Xe_train, Xe_test, ye_train, ye_test = train_test_split(X_economic, y, test_size=0.3, stratify=y, random_state=42)

Xe_resampled, ye_resampled = smote.fit_resample(Xe_train, ye_train)
```

##### stratify=y의미

불균형 데이터에서 종속변수를 나누면, 운이 안 좋을경우 테스트셋에 positive 클래스가 거의 없을 수 있음

이를 방지하기 위해 y(정답 레이블)의 클래스 비율을 기준으로 나누라는 문법

```python
# 모델 정의
dt_customer = DecisionTreeClassifier()
rf_economic = RandomForestClassifier()

# 모델 개별 학습
dt_customer.fit(Xc_resampled, yc_resampled)
rf_economic.fit(Xe_resampled, ye_resampled)
```

```python
# 개별 예측

dt_preds = dt_customer.predict_proba(Xc_test)[:, 1]
rf_preds = rf_economic.predict_proba(Xe_test)[:, 1]
```

```python
# 보팅 (두 함수 평균)
voting_probs = (dt_preds + rf_preds) / 2
voting_labels = (voting_probs >= 0.5).astype(int)

# 스태킹
stacking_X = np.vstack((dt_preds, rf_preds)).T
meta_model = LogisticRegression()
meta_model.fit(stacking_X, yc_test)
stacking_preds = meta_model.predict(stacking_X)
```

```python
# 결과 정리
def evaluate_model(name, y_true, y_pred):
    return {
        'Model': name,
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, average='binary', zero_division=0),
        'Recall': recall_score(y_true, y_pred, average='binary', zero_division=0),
        'F1 Score': f1_score(y_true, y_pred, average='binary', zero_division=0)
    }
```

```python
# 평가 결과를 DataFrame으로 정리
results = []
results.append(evaluate_model("Voting (Soft Avg)", yc_test, voting_labels))
results.append(evaluate_model("Stacking (LogReg)", yc_test, stacking_preds))
```

```python
# 결과 확인
results_df = pd.DataFrame(results)
results_df
```

```python
# classification report 확인 위해 추가

print(classification_report(y_test, voting_labels))
print(classification_report(y_test, stacking_preds))
```

**모델링 결과 정리**

전체적으로 성능 하락의 결과

## 6) 6차 모델링

결측치 지정한 컬럼들로 XGBoost, LGBM, Catboost 사용

```python
feature_2 = ['age', 'job_na', 'marital_na', 'education_na', 'default_na', 'housing_na',
             'loan_na','contact_encoded', 'month_encoded','day_of_week_encoded', 'campaign',
             'pdays_na', 'previous','poutcome_encoded', 'emp.var.rate', 'cons.price.idx',
             'cons.conf.idx','euribor3m', 'nr.employed','is_student_or_retired', 'is_high_edu',
             'had_prev_success','is_cellular','is_target_month', 'is_target_age','low_euribor3m',
             'neg_emp_var_rate', 'low_cons_conf', 'few_contacts', 'was_contacted_before']
target_2 = 'y'
```

```python
# 데이터 분할

X_2 = df[feature_2]
y_2 = df[target_2]

X2_train, X2_test, y2_train, y2_test = train_test_split(X_2, y_2, test_size=0.3, stratify=y_2, random_state=42)
```

```python
# 불균형 비율
pos_ratio = (y2_train == 0).sum() / (y2_train == 1).sum()
```

```python
# 모델 정의

xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42, scale_pos_weight=pos_ratio)
lgbm = LGBMClassifier(random_state=42, class_weight='balanced')
cat = CatBoostClassifier(verbose=0, random_state=42, auto_class_weights='Balanced')

models = {
    'XGBoost': xgb,
    'LightGBM': lgbm,
    'CatBoost': cat
}
```

```python
# 모델 평가

results = []
for name, model in models.items():
    model.fit(X2_train, y2_train)
    preds = model.predict(X2_test)

    acc = accuracy_score(y2_test, preds)
    prec = precision_score(y2_test, preds, pos_label=1)
    rec = recall_score(y2_test, preds)
    f1 = f1_score(y2_test, preds, pos_label=1)

    results.append({
        'Model': name,
        'Accuracy': acc,
        'Precision': prec,
        'Recall': rec,
        'F1 Score': f1
    })
```

=> LightGBM은 모델링할 때 내부적으로 어떤 일이 벌어지고 있는지 메세지를 줌

```python
# 결과 확인
results_df = pd.DataFrame(results)
results_df
```

```python
# classification report 확인 위해 추가

for name, model in models.items():
    preds = model.predict(X2_test)
    print(f"--------- {name}  classification report ---------")
    print(classification_report(y2_test, preds))
```

# 4. 결론

범주형 변수 라벨링 적용한 LightGBM의 Recall이 0.65로 가장 높음

=> 결측치를 결측치 자체로 봤을때 점수가 가장 높음

**<추가 방안>**

1. 트리 개수나 학습률, 트리 깊이 등 하이퍼 파라미터 탐색을 진행한 뒤 모델링하면 성능 향상될 듯

2. 교차검증을 추가하면 모델링 성능 늘어날 것으로 판단
 - 특히, 데이터의 클래스 불균형을 고려한 StratifiedKFold를 사용하면 성능 향상 가능성 높음

---

# 5. 추가할 사항
현업에선 어떤 가설을 설정하고 그에 맞춰 '비즈니스 지표 (KPI)'를 생성함

**[예시]**

**1. 비용 절감에 대한 KPI**
- 이와 같은 캠페인엔 <전화 비용 + 상담원 시간>이 필요
- 두 지표를 이용한 KPI를 만들 수 있음
    [예시]
    - Contact Reduction Rate: 모델을 쓰면서 전체 고객 중 몇 %만 연락했는지
    - Cost per Subscription: 모델이 추천한 고객에게만 연락했을 때, 실제 1건의 가입을 얻는 데 드는 평균 비용

**2. 매출 기여에 대한 KPI**
- 예금 가입 1건당 기대 수익을 가정했을때,
    - Expected Revenue Lift: 모델 적용 전후로 기대 수익 차이

    - KPI 수식 예: (모델 기반 추천군 가입자 수 × 1인당 평균 수익) – (전체 캠페인 시 평균 수익)

**3. 캠페인 효율성에 대한 KPI**
- 모델이 추천한 상위 N% 고객에게만 연락했을 때, 실제 “가입(yes)” 비율이 전체 평균 대비 얼마나 높은지를 나타냄
    - KPI 수식 예: 상위 20% 예측 고객군에서의 가입률 ÷ 전체 평균 가입률

=> 이렇게 지정한 뒤 매핑하여 회사 내부에서 사용할 수 있으며, 그에 따른 인사이트 전략 도출가능

```python

```
