---
title: "4 Portuguese Bank Data Marketing - AI 5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md"
excerpt: "결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고..."
research_summary: "결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를... 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기. `ipynb/md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다."
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

결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를... 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기. `ipynb/md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다.

**빠르게 볼 수 있는 포인트**: 결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페..., 🏦 미션 설명, 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2.....

**남겨둔 자료**: `ipynb/md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다.

**주요 스택**: `urllib`, `helper_c0z0c_dev`, `time`, `pandas`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 88 |
| Execution Cells | 45 |
| Libraries | `urllib`, `helper_c0z0c_dev`, `time`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn` |
| Source Note | `[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안` |

## What I Studied

### 🏦 미션 설명

결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를 바탕으로 비즈니스 전략을 제시하는 것

### 데이터 설명

2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기

### 📌 강사 Tip

데이터 설명을 읽었을 때, 해당 데이터는 크게 3가지가 독특함

### 참고 - 코랩(쥬피터 노트북) matplotlib 한글 오류 해결법

김명환님 제공 git: https://github.com/c0z0c/jupyter_hangul

## What I Tried in Code

1. 데이터 불러오기: CSV 데이터 불러오기
2. 전처리: LabelEncoder 전처리
3. 피처 가공: 데이터 시각화 후 추가 파생변수 생성
4. 모델 구성: XGBoost / RandomForest 모델 구성
5. 학습: 모델 학습 루프
6. 평가: 분류 성능 평가

## Code Evidence

### CSV 데이터 불러오기

**직접 해본 단계**: 데이터 불러오기

`CSV 데이터 불러오기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
df = pd.read_csv("/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/bank-additional-full.csv", sep=';')
df.head()
```

### LabelEncoder 전처리

**직접 해본 단계**: 전처리

`LabelEncoder 전처리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다. 코드에는 unknown을 제외하고 라벨 인코딩 후 unknown은..., unknown 제외하고 각각 컬럼 라벨 인코딩 같은 처리 포인트도 함께 남아 있습니다.

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

`데이터 시각화 후 추가 파생변수 생성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다. 코드에는 나이 관련, 직업 관련 같은 처리 포인트도 함께 남아 있습니다.

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

`XGBoost / RandomForest 모델 구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. XGBoost / RandomForest 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다. 코드에는 모델 정의 같은 처리 포인트도 함께 남아 있습니다.

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

`모델 학습 루프`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 훈련 데이터를 기준으로 모델을 실제로 fitting 하며 성능을 끌어올리는 학습 단계입니다. 코드에는 모델 평가 같은 처리 포인트도 함께 남아 있습니다.

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

`분류 성능 평가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다. 코드에는 결과 정리 같은 처리 포인트도 함께 남아 있습니다.

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

## Why These Steps Matter

### 데이터 입력부터 다시 보기

- 왜 필요한가: 실습을 다시 따라가려면 어떤 데이터 파일에서 출발했는지부터 분명해야 전체 흐름이 재현됩니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `CSV 데이터 불러오기` 코드를 앞쪽에 배치해 train/test 또는 원본 테이블이 어디서 올라오는지 바로 확인할 수 있게 했습니다.
- 원리: 표 형태 원본을 DataFrame으로 읽어와야 전처리, 피처 가공, 모델 학습이 같은 입력 기준 위에서 이어집니다.

### 전처리 코드를 남기는 이유

- 왜 필요한가: 머신러닝에선 모델보다 먼저 입력 데이터의 결측치, 범주형 값, 스케일을 어떻게 다뤘는지가 성능을 크게 바꿉니다.
- 왜 이 방식을 쓰는가: 그래서 `LabelEncoder 전처리` 같은 코드를 통해 실제로 어떤 정제 규칙을 적용했는지 문장보다 코드로 먼저 보여주도록 정리했습니다.
- 원리: 원본 데이터를 모델이 다루기 쉬운 수치 형태로 바꾸면 같은 알고리즘이어도 학습 안정성과 해석 가능성이 함께 올라갑니다.

### 파생 변수를 직접 만든 부분

- 왜 필요한가: 원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `데이터 시각화 후 추가 파생변수 생성` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.
- 원리: 좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.

### 모델을 바꿔가며 비교한 이유

- 왜 필요한가: 한 가지 모델만 보면 데이터에 맞는 편향과 분산 특성을 놓치기 쉬워서 여러 알고리즘을 비교해 보는 과정이 중요합니다.
- 왜 이 방식을 쓰는가: 그래서 `XGBoost / RandomForest 모델 구성`처럼 실제로 올려본 모델 코드를 남겨 어떤 후보를 실험했는지 바로 확인할 수 있게 했습니다.
- 원리: 모델마다 가정과 표현력이 달라 같은 데이터라도 잡아내는 패턴이 다르기 때문에 비교 실험이 필수입니다.

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
