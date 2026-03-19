---
title: "4 Portuguese Bank Data Marketing - AI 5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]4_Portuguese Bank Data Marketing - AI 5 강사 답안.md"
excerpt: "- 결정 트리와 앙상블 기법을 사용하여 분류 모델을 구축 - 🎯마케팅 캠페인의 효율성을 높이는 전략을 도출 - 데이터를 이용해 고객이 정기 예금을 가입할 가능성을 예측 - 마케팅 캠페인의 효율성을 높이는 것 - **최종 목표** : 가장 정확한 분류 모델을 개발하..."
tags:
  - research-archive
  - imported-note
  - ml
  - archive-note
---

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

## What I Worked On

- 🏦 미션 설명
- **데이터 설명**
- **📌 강사 Tip**
- 참고 - 코랩(쥬피터 노트북) matplotlib 한글 오류 해결법
- 한줄 설치

## Implementation Flow

1. 🏦 미션 설명
2. **데이터 설명**
3. **📌 강사 Tip**
4. 참고 - 코랩(쥬피터 노트북) matplotlib 한글 오류 해결법
5. 한줄 설치
6. 1. 데이터 확인

## Code Highlights

### 4. 모델링

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

### **🚨 SMOTE 적용시 주의사항**

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
