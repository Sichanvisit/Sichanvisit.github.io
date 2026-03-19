---
title: "자연어사전학습모델"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)자연어사전학습모델"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)자연어사전학습모델.md"
excerpt: "- https://huggingface.co/docs/transformers/en/model_doc/gpt2"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

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

## What I Worked On

- 패키지 설치
- 1. 문장 생성(이어쓰기)
- 2. 리뷰 감성 분석
- 데이터셋 불러오기
- 어떤 컬럼이 label인지 확인

## Implementation Flow

1. 패키지 설치
2. 1. 문장 생성(이어쓰기)
3. 2. 리뷰 감성 분석
4. 데이터셋 불러오기
5. 어떤 컬럼이 label인지 확인
6. 토크나이저 준비 및 데이터 전처리

## Code Highlights

### 데이터셋 불러오기

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
