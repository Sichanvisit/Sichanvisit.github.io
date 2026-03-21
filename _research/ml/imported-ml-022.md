---
title: "4 Portuguese Bank Data Marketing"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md"
excerpt: "Portuguese Bank Data Marketing의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 미션 설명, 데이터 확인, 데이터 전처리 순서로 큰 장을 먼저 훑고, CSV 데이터 불러오기, (7) 범주형 변수 처리 같은 코드로 실제 구현을 이어서..."
research_summary: "Portuguese Bank Data Marketing의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 미션 설명, 데이터 확인, 데이터 전처리 순서로 큰 장을 먼저 훑고, CSV 데이터 불러오기, (7) 범주형 변수 처리 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다."
research_artifacts: "ipynb/md · 코드 88개 · 실행 45개"
code_block_count: 88
execution_block_count: 45
research_focus:
  - "결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출..."
  - "🏦 미션 설명"
  - "2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, d..."
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
    <div class="research-overview__value">미션 설명 · 데이터 확인 · 데이터 전처리 · 데이터 시각화</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">CSV 데이터 불러오기 -&gt; (7) 범주형 변수 처리 -&gt; 데이터 시각화 후 추가 파생변수 생성</div>
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

## 원본 노트 흐름

### 미션 설명

결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를...

- 읽을 포인트: 세부 흐름: 데이터 설명, 강사 Tip

#### 데이터 설명

2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기

#### 강사 Tip

데이터 설명을 읽었을 때, 해당 데이터는 크게 3가지가 독특함 결측치를 unknown으로 처리한 것 2. 999라는 수치가 실제로는 無의 상태인 것 3. duration이 종속변수를 대변하는 피쳐인 점

### 데이터 확인

종속변수 y의 이진화 필요 확인할 컬럼들 - campaign 75%까지의 값은 문제없어 보이나 최대값이 극도로 큰 느낌 - pdays와 previous 전반적으로 값 동일 -> 특이 - pdays 설명: 999 means client was not previously contacted - previous: 이전에 연락을 받지 못한 고...

- 읽을 포인트: 세부 흐름: 1차 데이터 확인, 특정 컬럼 데이터 확인

#### 1차 데이터 확인

종속변수 y의 이진화 필요 확인할 컬럼들 - campaign 75%까지의 값은 문제없어 보이나 최대값이 극도로 큰 느낌 - pdays와 previous 전반적으로 값 동일 -> 특이 - pdays 설명: 999 means client was not previously contact...

#### 특정 컬럼 데이터 확인

Duration 전화를 받고 정기예금을 가입한 사람의 여부를 따지는 것이 이번 분석의 종속변수

### 데이터 전처리

최소 17, 최대 98 - 최대와 최소는 극단적인 값이나 완전히 비현실적인 수치는 아님 - 두 값이 불가능하다는 완벽한 증거는 없음 => 이상치라고 판단하지 않음

- 읽을 포인트: 세부 흐름: (3) 이상치 처리, (7) 범주형 변수 처리, (8) unknown 및 pdays=999 추가 처리

#### (3) 이상치 처리

최소 17, 최대 98 - 최대와 최소는 극단적인 값이나 완전히 비현실적인 수치는 아님 - 두 값이 불가능하다는 완벽한 증거는 없음 => 이상치라고 판단하지 않음

#### (7) 범주형 변수 처리

범주형 변수 라벨 전에 인코딩 전에 unknown값은 라벨 인코딩에서 제외하고 나머지 값으로 라벨 인코딩을 한 뒤,

#### (8) unknown 및 pdays=999 추가 처리

일반 트리모델(결정 트리)와 일반 앙상블(랜덤 포레스트 & 그레디언트 부스팅)은 결측치 자체를 모델링 할 수 없음 그러나 XGBoost는 missing 파라미터로 자동 처리 가능한 반면, LightGBM과 Catboost는 NaN을 자동 처리해주는 기능이 존재

### 데이터 시각화

데이터를 분위수 기준으로 구간화하는 함수 데이터를 같은 개수의 그룹으로 나누는 것

- 읽을 포인트: 세부 흐름: 그래프 결과 해석, 그래프 결과 해석 > 고객 특성 관련 변수, 데이터 시각화 후 추가 파생변수 생성

#### 그래프 결과 해석

데이터 구조와 주의할 변수부터 읽고 실험 방향을 정리하는 구간입니다.

#### 그래프 결과 해석 > 고객 특성 관련 변수

age - 중년층(30~40대)과 고연령층(60대 이상)에서 Yes 비율이 다소 높음 job - 학생, 은퇴자, 블루칼라보다는 관리직, 기술직, 자영업, 실업자 집단에서 가입률 차이가 존재. 특히 학생의 Yes 비율이 상당히 높음

#### 데이터 시각화 후 추가 파생변수 생성

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

### 모델링

예금 가입이 높은 구간대를 따로 구별한 파생변수를 추가하여 모델링 XGBoost는 scale_pos_weight 파라미터 사용

- 읽을 포인트: 세부 흐름: (3) 3차 모델링, (5) 5차 모델링, (6) 6차 모델링

#### (3) 3차 모델링

예금 가입이 높은 구간대를 따로 구별한 파생변수를 추가하여 모델링 XGBoost는 scale_pos_weight 파라미터 사용

#### (5) 5차 모델링

독립변수 분할하여 모델링 위 모델링 과정에서 시간이 오래 걸려 데이터 넘파이로 변환하며 모델링 진행

#### (6) 6차 모델링

결측치 지정한 컬럼들로 XGBoost, LGBM, Catboost 사용 => LightGBM은 모델링할 때 내부적으로 어떤 일이 벌어지고 있는지 메세지를 줌

### 결론

범주형 변수 라벨링 적용한 LightGBM의 Recall이 0.65로 가장 높음 => 결측치를 결측치 자체로 봤을때 점수가 가장 높음

- 읽을 포인트: 결론 아래에 이어질 세부 설명과 코드를 읽기 전 흐름을 잡는 구간입니다.

## 구현 흐름

### 1. CSV 데이터 불러오기

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: `pd.read_csv`
- 코드 포인트: -

### 2. (7) 범주형 변수 처리

- 단계: 전처리
- 구현 의도: 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.
- 핵심 API: `LabelEncoder`
- 코드 포인트: unknown을 제외하고 라벨 인코딩 후 unknown은... · unknown 제외하고 각각 컬럼 라벨 인코딩

### 3. 데이터 시각화 후 추가 파생변수 생성

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 나이 관련 · 직업 관련

### 4. XGBoost / RandomForest 모델 구성

- 단계: 모델 구성
- 구현 의도: XGBoost / RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: `DecisionTree`, `RandomForest`, `XGBoost`, `AdaBoost`
- 코드 포인트: 모델 정의

### 5. 모델 학습 루프

- 단계: 학습
- 구현 의도: 훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.
- 핵심 API: `accuracy_score`, `precision_score`, `recall_score`, `f1_score`
- 코드 포인트: 모델 평가

### 6. 분류 성능 평가

- 단계: 평가
- 구현 의도: 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.
- 핵심 API: `accuracy_score`, `precision_score`, `recall_score`, `f1_score`
- 코드 포인트: 결과 정리

## 코드로 확인한 내용

### CSV 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
df = pd.read_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bank-additional-full.csv", sep=';')
df.head()
```

### (7) 범주형 변수 처리

**직접 해본 단계**: 전처리

**핵심 API**: `LabelEncoder`

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

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

### 데이터 시각화 후 추가 파생변수 생성

**직접 해본 단계**: 피처 가공

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

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

### XGBoost / RandomForest 모델 구성

**직접 해본 단계**: 모델 구성

**핵심 API**: `DecisionTree`, `RandomForest`, `XGBoost`, `AdaBoost`

XGBoost / RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

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

### 모델 학습 루프

**직접 해본 단계**: 학습

**핵심 API**: `accuracy_score`, `precision_score`, `recall_score`, `f1_score`

훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.

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

### 분류 성능 평가

**직접 해본 단계**: 평가

**핵심 API**: `accuracy_score`, `precision_score`, `recall_score`, `f1_score`

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

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

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md`
- Source formats: `ipynb`, `md`
- Companion files: `[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.ipynb`, `[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- External references: `github.com`, `localhost`, `raw.githubusercontent.com`, `en.wikipedia.org`, `kbthink.com`

## 원문 미리보기

> - 결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - **최종 목표** : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를 바탕으로 비즈니스 전략을 제시하는 것
> 1. 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기
