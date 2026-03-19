---
title: "미션12 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션12_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션12_1팀_박시찬.md"
excerpt: "미션 소개 Hugging Face transformers 라이브러리를 사용하여 실제 한국어 문서 요약 모델을 처음부터 끝까지 구축하는 미션입니다"
research_summary: "미션 소개 Hugging Face transformers 라이브러리를 사용하여 실제 한국어 문서 요약 모델을 처음부터 끝까지 구축하는 미션입니다. 데이터 로드 → 전처리 → 모델 Fine-tuning → 요약 생성 → 평가까지 전체 파이프라인을 직접 구현해 봅니다. 원문 (Text): 95%가 678 토큰 이내. 요약 (Summary): 95%가 74 토큰 이내. 이 숫자가 황금 비율입니다. 보통 BART 기본 설정이 1024인데, 굳이 1024까지 쓸 필요 없이 700~800 정도만 써도 충분하다는 뜻입니다. 이러면 학습 속도도 빨라지고 메모리도 아낄 수 있습니다. `ipynb/md` 원본과 22개 코드 블록, 19개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, os, json입니다."
research_artifacts: "ipynb/md · 코드 22개 · 실행 19개"
code_block_count: 22
execution_block_count: 19
research_focus:
  - "미션 소개 Hugging Face transformers 라이브러리를 사용하여 실제 한국어 문서 요약..."
  - "미션"
  - "원문 (Text)"
research_stack:
  - "google"
  - "torch"
  - "os"
  - "json"
  - "pandas"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - mission
---

미션 소개 Hugging Face transformers 라이브러리를 사용하여 실제 한국어 문서 요약 모델을 처음부터 끝까지 구축하는 미션입니다. 데이터 로드 → 전처리 → 모델 Fine-tuning → 요약 생성 → 평가까지 전체 파이프라인을 직접 구현해 봅니다. 원문 (Text): 95%가 678 토큰 이내. 요약 (Summary): 95%가 74 토큰 이내. 이 숫자가 황금 비율입니다. 보통 BART 기본 설정이 1024인데, 굳이 1024까지 쓸 필요 없이 700~800 정도만 써도 충분하다는 뜻입니다. 이러면 학습 속도도 빨라지고 메모리도 아낄 수 있습니다. `ipynb/md` 원본과 22개 코드 블록, 19개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, os, json입니다.

**빠르게 볼 수 있는 포인트**: 미션 소개 Hugging Face transformers 라이브러리를..., 미션, 원문 (Text).

**남겨둔 자료**: `ipynb/md` 원본과 22개 코드 블록, 19개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, os, json입니다.

**주요 스택**: `google`, `torch`, `os`, `json`, `pandas`

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

## What This Note Covers

### 미션: Hugging Face Transformers를 활용한 문서 요약 모델 구현

미션 소개 Hugging Face transformers 라이브러리를 사용하여 실제 한국어 문서 요약 모델을 처음부터 끝까지 구축하는 미션입니다. 데이터 로드 → 전처리 → 모델 Fine-tuning → 요약 생성 → 평가까지 전체 파이프라인을 직접 구현해 봅니다.

### EDA 및 데이터 정제 실험

원문 (Text): 95%가 678 토큰 이내. 요약 (Summary): 95%가 74 토큰 이내. 이 숫자가 황금 비율입니다. 보통 BART 기본 설정이 1024인데, 굳이 1024까지 쓸 필요 없이 700~800 정도만 써도 충분하다는 뜻입니다. 이러면 학습 속도도 빨라지고 메모리도 아낄 수 있습니다.

### 토크나이저 정렬 분석

UNK 비율 확인: 모델이 모르는 단어가 1% 미만이어야 안전합니다. - 파편화율 확인: 단어가 너무 잘게 쪼개지면 학습이 어렵습니다. (0.3 ~ 0.6 사이면 양호)

### Key Step

CUDA 사용 가능 여부 체크 및 장치 설정

## Implementation Flow

1. 미션: Hugging Face Transformers를 활용한 문서 요약 모델 구현: 미션 소개 Hugging Face transformers 라이브러리를 사용하여 실제 한국어 문서 요약 모델을 처음부터 끝까지 구축하는 미션입니다. 데이터 로드 → 전처리 → 모델 Fine-tuning → 요약 생성...
2. EDA 및 데이터 정제 실험: 원문 (Text): 95%가 678 토큰 이내. 요약 (Summary): 95%가 74 토큰 이내. 이 숫자가 황금 비율입니다. 보통 BART 기본 설정이 1024인데, 굳이 1024까지 쓸 필요 없이 700~800 정도만 써도 충분하다는 뜻입니다. 이러면 학습 속도도...
3. 토크나이저 정렬 분석: UNK 비율 확인: 모델이 모르는 단어가 1% 미만이어야 안전합니다. - 파편화율 확인: 단어가 너무 잘게 쪼개지면 학습이 어렵습니다. (0.3 ~ 0.6 사이면 양호)
4. Key Step: CUDA 사용 가능 여부 체크 및 장치 설정

## Code Highlights

### 토크나이저 정렬 분석

`토크나이저 정렬 분석`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 =================================================..., 여기서 정의한 값을 함수로 넘겨줄 겁니다 흐름이 주석과 함께 드러납니다.

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

`모델 파이프라인`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 =================================================..., [사용자 설정] 흐름이 주석과 함께 드러납니다.

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
