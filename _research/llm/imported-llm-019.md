---
title: "2 BERT LoRA"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-4 (실습)2_BERT_LoRA"
source_path: "13_LLM_GenAI/Code_Snippets/3-4 (실습)2_BERT_LoRA.md"
excerpt: "BERT 모델을 사용하여 PEFT(LoRA) 사용"
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
| Code Blocks | 9 |
| Execution Cells | 9 |
| Libraries | `huggingface_hub`, `transformers`, `datasets`, `peft`, `evaluate`, `torch` |
| Source Note | `3-4 (실습)2_BERT_LoRA` |

## What I Worked On

- 1. LoRA - BERT 모델을 사용한 PEFT
- 허깅페이스 계정에 로그인
- hugging face login
- BERT 모델 로드
- BERT 로드

## Implementation Flow

1. 1. LoRA - BERT 모델을 사용한 PEFT
2. 허깅페이스 계정에 로그인
3. hugging face login
4. BERT 모델 로드
5. BERT 로드
6. 데이터세트 로드

## Code Highlights

### 토크나이저 설정

```python
# 토크나이저
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def preprocess(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )

tokenized = dataset.map(preprocess, batched=True)
tokenized = tokenized.rename_column("label", "labels")
tokenized.set_format(type="torch", columns=["input_ids", "attention_mask", "labels"])
train_ds = tokenized["train"]
eval_ds  = tokenized["validation"]

train_ds[0]
```

### PEFT - Lora 설정과 학습

```python
from peft import LoraConfig, get_peft_model
import evaluate

# LoRA 구성
lora_config = LoraConfig(
    task_type="SEQ_CLS",  # 시퀀스 분류
    r=8,
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["query", "key", "value", "output.dense"],
)

# LoRA 적용
model = get_peft_model(base_model, lora_config)

# Trainer 구성
training_args = TrainingArguments(
    output_dir="./lora_bert_mrpc",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    eval_strategy="steps",
    logging_steps=20,
    save_steps=200,
    save_total_limit=2,
    learning_rate=2e-5,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-4 (실습)2_BERT_LoRA.md`
- Source formats: `md`
- Companion files: `3-4 (실습)2_BERT_LoRA.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> BERT 모델을 사용하여 PEFT(LoRA) 사용
> LoRA는 모델 전체가 아니라 학습된 '어댑터(Adapter)' 부분만 저장하면 됩니다. 용량이 매우 작아서 효율적입니다.
