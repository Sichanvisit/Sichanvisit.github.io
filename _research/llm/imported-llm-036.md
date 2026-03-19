---
title: "미션12 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션12_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션12_1팀_박시찬.md"
excerpt: "미션 소개 Hugging Face transformers 라이브러리를 사용하여 **실제 한국어 문서 요약 모델**을 처음부터 끝까지 구축하는 미션입니다. 데이터 로드 → 전처리 → 모델 Fine-tuning → 요약 생성 → 평가까지 **전체 파이프라인**을 직접..."
tags:
  - research-archive
  - imported-note
  - llm
  - mission
---

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Mission |
| Source Files | `ipynb`, `md` |
| Code Blocks | 22 |
| Execution Cells | 19 |
| Libraries | `google`, `torch`, `os`, `json`, `pandas`, `re`, `html`, `numpy` |
| Source Note | `미션12_1팀_박시찬` |

## What I Worked On

- 미션: Hugging Face Transformers를 활용한 문서 요약 모델 구현
- 1. CUDA 사용 가능 여부 체크 및 장치 설정
- 2. 실제 사용 예시 (데이터/모델을 장치로 이동)
- 이후 모델 정의 시에도 아래처럼 사용합니다
- model = MyModel().to(device)

## Implementation Flow

1. 미션: Hugging Face Transformers를 활용한 문서 요약 모델 구현
2. 1. CUDA 사용 가능 여부 체크 및 장치 설정
3. 2. 실제 사용 예시 (데이터/모델을 장치로 이동)
4. 이후 모델 정의 시에도 아래처럼 사용합니다
5. model = MyModel().to(device)
6. 기본 경로 설정

## Code Highlights

### 토크나이저 정렬 분석

```python
import pandas as pd
from datasets import Dataset, DatasetDict
from transformers import AutoTokenizer
import os

# =========================================================
BASE_PATH =  r"C:\Users\bhs33\PyCharmMiscProject\summarization\summarization"
INPUT_TRAIN = "step5_density_controlled_train.csv"
INPUT_VALID = "step5_density_controlled_valid.csv"
OUTPUT_DIR = "final_processed_dataset"
MODEL_NAME = "gogamza/kobart-base-v2"

# 여기서 정의한 값을 함수로 넘겨줄 겁니다
MY_MAX_INPUT = 700
MY_MAX_TARGET = 128
# =========================================================

# 인자에 max_input_len, max_target_len 추가
def preprocess_function(examples, tokenizer=None, max_input_len=None, max_target_len=None):
    # 텍스트가 숫자로 들어오는 경우 대비 문자열 변환
    inputs = [str(t) for t in examples["text"]]
    targets = [str(s) for s in examples["summary"]]

    # 인자로 받은 max_input_len 사용
    model_inputs = tokenizer(
        inputs,
        max_length=max_input_len,
        truncation=True,
# ... trimmed ...
```

### 모델 파이프라인

```python
import os
import torch
import gc
import numpy as np
import evaluate
from datasets import load_from_disk
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainingArguments,
    Seq2SeqTrainer,
    EarlyStoppingCallback
)

# =========================================================
# [사용자 설정]
# =========================================================
BASE_PATH = r"C:\Users\bhs33\PyCharmMiscProject\summarization\summarization"
DATASET_DIR = "final_processed_dataset"
OUTPUT_DIR = "bart_summary_model_final"
MODEL_NAME = "gogamza/kobart-base-v2"

# [1660 Ti 최적화 파라미터]
BATCH_SIZE = 2           # 6GB VRAM 안전값
GRAD_ACCUM_STEPS = 16    # 실질적 배치 32
LEARNING_RATE = 3e-5
NUM_EPOCHS = 5           # Early Stopping이 있으므로 넉넉하게 설정
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/미션12_1팀_박시찬.md`
- Source formats: `ipynb`, `md`
- Companion files: `미션12_1팀_박시찬.ipynb`, `미션12_1팀_박시찬.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `text'', ''summary`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `aihub.or.kr`, `localhost`, `pypi.python.org`

## Note Preview

> 미션 소개 Hugging Face transformers 라이브러리를 사용하여 **실제 한국어 문서 요약 모델**을 처음부터 끝까지 구축하는 미션입니다. 데이터 로드 → 전처리 → 모델 Fine-tuning → 요약 생성 → 평가까지 **전체 파이프라인**을 직접 구현해 봅니다.
> ---
