---
title: "미션13 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션13_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션13_1팀_박시찬.md"
excerpt: "쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다. 데이터 다운로드: 약 40MB (AI Hub - 속성기반 감정분석 데이터) - 형식: JSON 파일 (하나의 파일에..."
research_summary: "쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다. 데이터 다운로드: 약 40MB (AI Hub - 속성기반 감정분석 데이터) - 형식: JSON 파일 (하나의 파일에 다수의 리뷰 포함) - 주요 필드... 초기 진단 (Initial Diagnosis) 데이터 로드 직후 수행한 1차 정밀 진단 결과입니다. 총 데이터 수: 201,616건 - 결측치 (Missing Values): - text: 0건 (양호) - label: 17,091건 (전체의 약 8.5% 누락). `ipynb/md` 원본과 27개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 peft, google, os, re입니다."
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

쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다. 데이터 다운로드: 약 40MB (AI Hub - 속성기반 감정분석 데이터) - 형식: JSON 파일 (하나의 파일에 다수의 리뷰 포함) - 주요 필드... 초기 진단 (Initial Diagnosis) 데이터 로드 직후 수행한 1차 정밀 진단 결과입니다. 총 데이터 수: 201,616건 - 결측치 (Missing Values): - text: 0건 (양호) - label: 17,091건 (전체의 약 8.5% 누락). `ipynb/md` 원본과 27개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 peft, google, os, re입니다.

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

쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다. 데이터 다운로드: 약 40MB (AI Hub - 속성기반 감정분석 데이터) - 형식: JSON 파일 (하나의 파일에 다수의 리뷰 포함) - 주요 필드 - RawText: 리뷰 원문 텍스트 - General...

### 데이터 전처리 및 라벨 복원 보고서

초기 진단 (Initial Diagnosis) 데이터 로드 직후 수행한 1차 정밀 진단 결과입니다. 총 데이터 수: 201,616건 - 결측치 (Missing Values): - text: 0건 (양호) - label: 17,091건 (전체의 약 8.5% 누락)

### 정량적 검증 및 심층 분석 보고서

Full Fine-Tuning vs PEFT (LoRA) 비교 평가 본 프로젝트에서는 동일한 데이터셋과 학습 조건 하에 Full Fine-Tuning (Full FT) 방식과 PEFT-LoRA 방식을 각각 적용하여 모델을 학습하였으며, 성능·효율성·품질 측면에서 체계적인 비교 분석을 수행하였습니다.

### 성능 및 효율성 종합 비교 (Global Comparison) > 핵심 인사이트

성능 보존 우수 LoRA는 전체 파라미터의 약 0.05%만 업데이트했음에도 Full FT 대비 정확도 손실 0.7% p 수준으로 방어 → 실서비스 적용 가능 수준 2. 용량 혁명 423 MB → 2.1 MB (약 1/200) → 동일 스토리지에 200개 이상의 특화 모델 동시 보관·서빙 가능 (MLOps 관점에서 압도적 이점)

## Why This Matters

### 파라미터 효율 미세조정

- 왜 필요한가: 대형 언어모델 전체를 다시 학습하는 비용이 크기 때문에, 적은 자원으로도 실험 가능한 미세조정 방식이 필요합니다.
- 왜 이 방식을 쓰는가: LoRA/QLoRA는 전체 가중치를 모두 바꾸지 않고 작은 적응 파라미터만 학습해 메모리와 시간을 크게 줄일 수 있습니다.
- 원리: 기존 가중치는 고정하고 저차원 행렬 업데이트만 추가로 학습해, 적은 파라미터로도 모델 행동을 조정합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

## Implementation Flow

1. 쇼핑몰 리뷰 감성 분석 미션: 쇼핑몰 리뷰 데이터를 대상으로 감성 분석(Sentiment Analysis) 모델을 학습하고, Full Fine-Tuning 방식과 PEFT 방식의 성능·효율성을 비교하는 미션입니다. 데이터 다운로드: 약 40MB (AI Hub - 속성기반 감정분석 데이터) - 형식:...
2. 데이터 전처리 및 라벨 복원 보고서: 초기 진단 (Initial Diagnosis) 데이터 로드 직후 수행한 1차 정밀 진단 결과입니다. 총 데이터 수: 201,616건 - 결측치 (Missing Values): - text: 0건 (양호) - label: 17,091건 (전체의 약 8.5% 누락)
3. 정량적 검증 및 심층 분석 보고서: Full Fine-Tuning vs PEFT (LoRA) 비교 평가 본 프로젝트에서는 동일한 데이터셋과 학습 조건 하에 Full Fine-Tuning (Full FT) 방식과 PEFT-LoRA 방식을 각각 적용하여 모델을 학습하였으며, 성능·효율성·품질 측면에서...
4. 성능 및 효율성 종합 비교 (Global Comparison) > 핵심 인사이트: 성능 보존 우수 LoRA는 전체 파라미터의 약 0.05%만 업데이트했음에도 Full FT 대비 정확도 손실 0.7% p 수준으로 방어 → 실서비스 적용 가능 수준 2. 용량 혁명 423 MB → 2.1 MB (약 1/...

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

### 효율적 데이터 파이프라인 구축

`효율적 데이터 파이프라인 구축`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 HF Dataset 변환, 전처리 함수 (토크나이징 + 라벨 매핑), 텍스트 토크나이징 흐름이 주석과 함께 드러납니다.

```python
from datasets import Dataset, DatasetDict

# 1. HF Dataset 변환
datasets = DatasetDict({
    "train": Dataset.from_pandas(train_df),
    "test": Dataset.from_pandas(test_df)
})

# 2. 전처리 함수 (토크나이징 + 라벨 매핑)
def preprocess_function(examples):
    # 텍스트 토크나이징
    tokenized = tokenizer(
        examples['text'],
        truncation=True,
        max_length=180,   # 1-4에서 분석한 값
        padding=False     # ★ Dynamic Padding을 위해 여기서는 패딩 안 함
    )

    # 라벨 매핑: {-1, 0, 1} -> {0, 1, 2}
    label_map = {-1: 0, 0: 1, 1: 2}
    # examples['label']는 리스트(batch) 형태이므로 list comprehension 사용
    tokenized['labels'] = [label_map[int(l)] for l in examples['label']]

    return tokenized

# 3. 변환 실행 (병렬 처리)
print("🚀 토크나이징 & 라벨 매핑 진행 중...")
encoded_datasets = datasets.map(
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
> 사용 데이터셋
