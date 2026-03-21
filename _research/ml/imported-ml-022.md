---
title: "4 Portuguese Bank Data Marketing - AI 5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md"
excerpt: "Portuguese Bank Data Marketing를 중심으로 분류 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "Portuguese Bank Data Marketing를 중심으로 분류 문제, 결정 트리와 앙상블 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 CSV 데이터 불러오기, LabelEncoder 전처리 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다."
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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축. 마케팅 캠페인의 효율성을 높이는 전략을 도출</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>분류 문제 · 결정 트리와 앙상블 · 전처리와 입력 정리</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>CSV 데이터 불러오기 -&gt; LabelEncoder 전처리 -&gt; 데이터 시각화 후 추가 파생변수 생성</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 88 · 실행 45</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>urllib, helper_c0z0c_dev, time, pandas 외 1</td>
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
        <strong class="research-compact-table__main">CSV 데이터 불러오기</strong>
        <span class="research-compact-table__sub">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</span>
      </td>
      <td><code>pd.read_csv</code></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 전처리</th>
      <td>
        <strong class="research-compact-table__main">LabelEncoder 전처리</strong>
        <span class="research-compact-table__sub">결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.</span>
      </td>
      <td><code>LabelEncoder</code></td>
      <td>unknown을 제외하고 라벨 인코딩 후 unknown은... · unknown 제외하고 각각 컬럼 라벨 인코딩</td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 피처 가공</th>
      <td>
        <strong class="research-compact-table__main">데이터 시각화 후 추가 파생변수 생성</strong>
        <span class="research-compact-table__sub">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>나이 관련 · 직업 관련</td>
    </tr>
    <tr>
      <th scope="row">Step 4 · 모델 구성</th>
      <td>
        <strong class="research-compact-table__main">XGBoost / RandomForest 모델 구성</strong>
        <span class="research-compact-table__sub">XGBoost / RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</span>
      </td>
      <td><code>DecisionTree</code> <code>RandomForest</code> <code>XGBoost</code> <code>AdaBoost</code></td>
      <td>모델 정의</td>
    </tr>
    <tr>
      <th scope="row">Step 5 · 학습</th>
      <td>
        <strong class="research-compact-table__main">모델 학습 루프</strong>
        <span class="research-compact-table__sub">훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다.</span>
      </td>
      <td><code>accuracy_score</code> <code>precision_score</code> <code>recall_score</code> <code>f1_score</code></td>
      <td>모델 평가</td>
    </tr>
    <tr>
      <th scope="row">Step 6 · 평가</th>
      <td>
        <strong class="research-compact-table__main">분류 성능 평가</strong>
        <span class="research-compact-table__sub">예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.</span>
      </td>
      <td><code>accuracy_score</code> <code>precision_score</code> <code>recall_score</code> <code>f1_score</code></td>
      <td>결과 정리</td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

### CSV 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

**핵심 API**: `pd.read_csv`

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
df = pd.read_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bank-additional-full.csv", sep=';')
df.head()
```

### LabelEncoder 전처리

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

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md`
- Source formats: `ipynb`, `md`
- Companion files: `[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.ipynb`, `[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- External references: `github.com`, `localhost`, `raw.githubusercontent.com`, `en.wikipedia.org`, `kbthink.com`

## Note Preview

> - 결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - **최종 목표** : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를 바탕으로 비즈니스 전략을 제시하는 것
> 1. 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기
