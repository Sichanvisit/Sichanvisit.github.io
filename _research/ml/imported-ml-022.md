---
title: "4 Portuguese Bank Data Marketing - AI 5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md"
excerpt: "결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고..."
research_summary: "결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를... 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기. `md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다."
research_artifacts: "md · 코드 88개 · 실행 45개"
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
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - archive-note
---

결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를... 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기. `md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다.

**빠르게 볼 수 있는 포인트**: 결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페..., 🏦 미션 설명, 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2.....

**남겨둔 자료**: `md` 원본과 88개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 urllib, helper_c0z0c_dev, time, pandas입니다.

**주요 스택**: `urllib`, `helper_c0z0c_dev`, `time`, `pandas`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 88 |
| Execution Cells | 45 |
| Libraries | `urllib`, `helper_c0z0c_dev`, `time`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn` |
| Source Note | `[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안` |

## What This Note Covers

### 🏦 미션 설명

결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를 바탕으로 비즈니스 전략을 제시하는 것

### 데이터 설명

2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기

### 📌 강사 Tip

데이터 설명을 읽었을 때, 해당 데이터는 크게 3가지가 독특함

### 참고 - 코랩(쥬피터 노트북) matplotlib 한글 오류 해결법

김명환님 제공 git: https://github.com/c0z0c/jupyter_hangul

## Why This Matters

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

## Implementation Flow

1. 🏦 미션 설명: 결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - 최종 목표 : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지...
2. 데이터 설명: 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기
3. 📌 강사 Tip: 데이터 설명을 읽었을 때, 해당 데이터는 크게 3가지가 독특함
4. 참고 - 코랩(쥬피터 노트북) matplotlib 한글 오류 해결법: 김명환님 제공 git: https://github.com/c0z0c/jupyter_hangul

## Code Highlights

### 모델링

`모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 평가 흐름이 주석과 함께 드러납니다.

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

### (3) 3차 모델링

`(3) 3차 모델링`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 평가 흐름이 주석과 함께 드러납니다.

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

### 🚨 SMOTE 적용시 주의사항

`🚨 SMOTE 적용시 주의사항`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 평가 - 시간이 오래 걸려 시간 테스트 흐름이 주석과 함께 드러납니다.

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
# ... trimmed ...
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md`
- Source formats: `md`
- Companion files: `[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- External references: `github.com`, `localhost`, `raw.githubusercontent.com`, `en.wikipedia.org`, `kbthink.com`

## Note Preview

> - 결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - **최종 목표** : 가장 정확한 분류 모델을 개발하여 고객이 정기 예금을 가입할지 여부를 예측하고, 그 모델을 통해 도출한 인사이트를 바탕으로 비즈니스 전략을 제시하는 것
> 1. 2008년부터 2010년까지 포르투갈 은행 마케팅 캠페인 데이터 2. 데이터 설명 txt에 따르면, duration은 종속변수와 연관이 큰 데이터 3. 결측치는 unknown으로 표기
