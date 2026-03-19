---
title: "미션13 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션13_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션13_1팀_박시찬.md"
excerpt: "쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다"
research_summary: "쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다. 초기 진단 (Initial Diagnosis) 데이터 로드 직후 수행한 1차 정밀 진단 결과입니다. `ipynb/md` 원본과 27개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 peft, google, os, re입니다."
research_artifacts: "ipynb/md · 코드 27개 · 실행 25개"
code_block_count: 27
execution_block_count: 25
research_focus:
  - "쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full..."
  - "쇼핑몰 리뷰 감성 분석 미션"
  - "데이터셋"
research_stack:
  - "peft"
  - "google"
  - "os"
  - "re"
  - "torch"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - mission
---

쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다. 초기 진단 (Initial Diagnosis) 데이터 로드 직후 수행한 1차 정밀 진단 결과입니다. `ipynb/md` 원본과 27개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 peft, google, os, re입니다.

**빠르게 볼 수 있는 포인트**: 쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analys..., 쇼핑몰 리뷰 감성 분석 미션, 데이터셋.

**남겨둔 자료**: `ipynb/md` 원본과 27개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 peft, google, os, re입니다.

**주요 스택**: `peft`, `google`, `os`, `re`, `torch`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Mission |
| Source Files | `ipynb`, `md` |
| Code Blocks | 27 |
| Execution Cells | 25 |
| Libraries | `peft`, `google`, `os`, `re`, `torch`, `numpy`, `pandas`, `nltk` |
| Source Note | `미션13_1팀_박시찬` |

## What This Note Covers

### 쇼핑몰 리뷰 감성 분석 미션

쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다.

### 데이터 전처리 및 라벨 복원 보고서

초기 진단 (Initial Diagnosis) 데이터 로드 직후 수행한 1차 정밀 진단 결과입니다.

### 정량적 검증 및 심층 분석 보고서

Full Fine-Tuning vs PEFT (LoRA) 비교 평가

### 성능 및 효율성 종합 비교 (Global Comparison)

/ 항목 / Full Fine-Tuning / PEFT (LoRA) / 차이 (Diff) / 비고 / /---------------------/------------------------/-----------------------/---------------------/-----------------------------------/ / Accuracy / 91.02% / 90.32%...

## Implementation Flow

1. 쇼핑몰 리뷰 감성 분석 미션: 쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다.
2. 데이터 전처리 및 라벨 복원 보고서: 초기 진단 (Initial Diagnosis) 데이터 로드 직후 수행한 1차 정밀 진단 결과입니다.
3. 정량적 검증 및 심층 분석 보고서: Full Fine-Tuning vs PEFT (LoRA) 비교 평가
4. 성능 및 효율성 종합 비교 (Global Comparison): / 항목 / Full Fine-Tuning / PEFT (LoRA) / 차이 (Diff) / 비고 / /---------------------/------------------------/-----------------------/--...

## Code Highlights

### 데이터 전처리 및 라벨 복원 보고서

`데이터 전처리 및 라벨 복원 보고서`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 & 토크나이저 로드, 설정값, 전처리 함수 정의 흐름이 주석과 함께 드러납니다.

```python
from transformers import AutoTokenizer

# 1. 모델 & 토크나이저 로드
MODEL_ID = "klue/bert-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

# 2. 설정값
MAX_LEN = 180

# 3. 전처리 함수 정의
def preprocess_function(examples):
    # 텍스트 토크나이징
    tokenized = tokenizer(
        examples['text'],
        truncation=True,
        max_length=MAX_LEN,
        padding=False
    )

    # 라벨 매핑 (확실하게!)
    label_map = {-1: 0, 0: 1, 1: 2}
    tokenized['labels'] = [label_map[l] for l in examples['label']]

    return tokenized

print(f"🚀 [Step 2-2] 토크나이징 및 컬럼 정리")

# 4. 전체 데이터 변환 (병렬 처리)
# ... trimmed ...
```

### 학습 실험

`학습 실험`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Data Collator 생성, 동적 패딩 검증 함수 (수정됨), ★ 중요: 학습에 불필요한 컬럼 제거 (Aspects 등이 있으면 에러남) 흐름이 주석과 함께 드러납니다.

```python
from transformers import DataCollatorWithPadding
import torch

# 1. Data Collator 생성
data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# 2. 동적 패딩 검증 함수 (수정됨)
def verify_dynamic_padding(dataset, collator, batch_size=32):
    print("🚀 [Step 3-1] 동적 패딩 효율성 검증")

    # ★ 중요: 학습에 불필요한 컬럼 제거 (Aspects 등이 있으면 에러남)
    # 필요한 컬럼만 남김: input_ids, token_type_ids, attention_mask, labels
    cols_to_keep = ['input_ids', 'token_type_ids', 'attention_mask', 'labels']
    # 실제 데이터셋에 있는 컬럼만 keep 리스트에 포함
    cols_to_keep = [c for c in cols_to_keep if c in dataset.column_names]

    # 임시로 필요한 컬럼만 가진 데이터셋 생성 (메모리 효율 위해 select 후 remove)
    # (전체 데이터셋을 건드리지 않고, 샘플링한 것만 처리)

    # 1. 랜덤 샘플링 (인덱스)
    import random
    indices = random.sample(range(len(dataset)), batch_size)

    # 2. 샘플 데이터 추출 (리스트 of 딕셔너리 형태)
    samples = []
    for idx in indices:
        item = dataset[idx]
        # 불필요한 키 제거 (Aspects 등)
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/미션13_1팀_박시찬.md`
- Source formats: `ipynb`, `md`
- Companion files: `미션13_1팀_박시찬.ipynb`, `미션13_1팀_박시찬.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `text'', ''label`, `text'', ''label'', ''Aspects`, `Accuracy", "Macro F1`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `test.com`

## Note Preview

> 쇼핑몰 리뷰 데이터를 대상으로 **감성 분석(Sentiment Analysis)** 모델을 학습하고, **Full Fine-Tuning** 방식과 **PEFT** 방식의 성능·효율성을 비교하는 미션입니다.
> ---
