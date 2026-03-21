---
title: "자연어사전학습모델"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)자연어사전학습모델"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)자연어사전학습모델.md"
excerpt: "https://huggingface.co/docs/transformers/en/model_doc/gpt2"
research_summary: "https://huggingface.co/docs/transformers/en/model_doc/gpt2. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 26개 코드 블록, 23개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, transformers, datasets, evaluate입니다."
research_artifacts: "md · 코드 26개 · 실행 23개"
code_block_count: 26
execution_block_count: 23
research_focus:
  - "패키지 설치"
  - "https"
  - "문장 생성(이어쓰기)"
research_stack:
  - "torch"
  - "transformers"
  - "datasets"
  - "evaluate"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

https://huggingface.co/docs/transformers/en/model_doc/gpt2. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 26개 코드 블록, 23개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, transformers, datasets, evaluate입니다.

**빠르게 볼 수 있는 포인트**: 패키지 설치, https, 문장 생성(이어쓰기).

**남겨둔 자료**: `md` 원본과 26개 코드 블록, 23개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, transformers, datasets, evaluate입니다.

**주요 스택**: `torch`, `transformers`, `datasets`, `evaluate`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 26 |
| Execution Cells | 23 |
| Libraries | `torch`, `transformers`, `datasets`, `evaluate`, `numpy`, `kagglehub`, `pandas` |
| Source Note | `3-3 (실습)자연어사전학습모델` |

## What This Note Covers

### 문장 생성(이어쓰기)

https://huggingface.co/docs/transformers/en/model_doc/gpt2

### Key Step

어떤 컬럼이 label인지 확인

### Key Step

토크나이저 준비 및 데이터 전처리

### Key Step

포맷 지정 및 label 컬럼 명시

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. 문장 생성(이어쓰기): https://huggingface.co/docs/transformers/en/model_doc/gpt2
2. Key Step: 어떤 컬럼이 label인지 확인
3. Key Step: 토크나이저 준비 및 데이터 전처리
4. Key Step: 포맷 지정 및 label 컬럼 명시

## Code Highlights

### 데이터셋 불러오기

`데이터셋 불러오기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Text 컬럼, Summary 컬럼 흐름이 주석과 함께 드러납니다.

```python
from transformers import AutoTokenizer
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")

# Text 컬럼
text_lengths = [
    len(tokenizer(text=t, add_special_tokens=False)["input_ids"])  # ← text=
    for t in dataset["train"]["Text"]
    if t                                                          # None/빈 문자열 방어
]

# Summary 컬럼
summary_lengths = [
    len(tokenizer(text=s, add_special_tokens=False)["input_ids"])  # ← text=
    for s in dataset["train"]["Summary"]
    if s
]

def print_stats(name, lengths):
    print(f"[{name}]")
    print(f"  평균 길이   : {np.mean(lengths):.1f}")
    print(f"  90% 이하 길이: {np.percentile(lengths, 90):.0f}")
    print(f"  최대 길이   : {np.max(lengths)}\n")

print_stats("Text", text_lengths)
print_stats("Summary", summary_lengths)
```

### 토크나이저 준비 및 데이터 전처리

`토크나이저 준비 및 데이터 전처리`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 None · 숫자 · NaN 등을 깨끗한 문자열로 변환 흐름이 주석과 함께 드러납니다.

```python
def preprocess_function(examples):
    # None · 숫자 · NaN 등을 깨끗한 문자열로 변환
    texts     = [str(t) if t is not None else "" for t in examples["Text"]]
    summaries = [str(s) if s is not None else "" for s in examples["Summary"]]

    inputs = tokenizer(
        text=texts,
        max_length=max_input_length,
        truncation=True,
        padding="max_length",
    )
    targets = tokenizer(
        text=summaries,
        max_length=max_target_length,
        truncation=True,
        padding="max_length",
    )
    inputs["labels"] = targets["input_ids"]
    return inputs

tokenized_datasets = dataset.map(
    preprocess_function,
    batched=True,
    remove_columns=dataset["train"].column_names,   # 필요 없으면 지워도 됨
)

tokenized_datasets.set_format(
    type="torch",
# ... trimmed ...
```

### Trainer 설정 및 학습

`Trainer 설정 및 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 GPU 장치 설정, test 셋 선택, 요약 결과 저장용 리스트 흐름이 주석과 함께 드러납니다.

```python
import torch

# 1. GPU 장치 설정
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# 2. test 셋 선택
test_texts = dataset["test"]["Text"][:10]  # 예시로 10개만 추론

# 3. 요약 결과 저장용 리스트
summaries = []

# 4. 문장 하나씩 요약
for text in test_texts:
    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=256,
        truncation=True,
        padding="max_length"
    ).to(device)  # 입력도 GPU로 이동

    summary_ids = model.generate(
        **inputs,
        max_length=48,
        num_beams=4,
        early_stopping=True
    )
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-3 (실습)자연어사전학습모델.md`
- Source formats: `md`
- Companion files: `3-3 (실습)자연어사전학습모델.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `Text'', ''Summary`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `huggingface.co`

## Note Preview

> - https://huggingface.co/docs/transformers/en/model_doc/gpt2
