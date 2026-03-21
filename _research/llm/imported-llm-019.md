---
title: "2 BERT LoRA"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-4 (실습)2_BERT_LoRA"
source_path: "13_LLM_GenAI/Code_Snippets/3-4 (실습)2_BERT_LoRA.md"
excerpt: "BERT 모델을 사용하여 PEFT(LoRA) 사용. LoRA는 모델 전체가 아니라 학습된 '어댑터(Adapter)' 부분만 저장하면 됩니다. 용량이 매우 작아서 효율적입니다. `md` 원본과 9개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 h..."
research_summary: "BERT 모델을 사용하여 PEFT(LoRA) 사용. LoRA는 모델 전체가 아니라 학습된 '어댑터(Adapter)' 부분만 저장하면 됩니다. 용량이 매우 작아서 효율적입니다. `md` 원본과 9개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, datasets, peft입니다."
research_artifacts: "md · 코드 9개 · 실행 9개"
code_block_count: 9
execution_block_count: 9
research_focus:
  - "BERT 모델을 사용하여 PEFT(LoRA) 사용"
  - "LoRA - BERT 모델을 사용한 PEFT"
  - "허깅페이스 계정에 로그인"
research_stack:
  - "huggingface_hub"
  - "transformers"
  - "datasets"
  - "peft"
  - "evaluate"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

BERT 모델을 사용하여 PEFT(LoRA) 사용. LoRA는 모델 전체가 아니라 학습된 '어댑터(Adapter)' 부분만 저장하면 됩니다. 용량이 매우 작아서 효율적입니다. `md` 원본과 9개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, datasets, peft입니다.

**빠르게 볼 수 있는 포인트**: BERT 모델을 사용하여 PEFT(LoRA) 사용, LoRA - BERT 모델을 사용한 PEFT, 허깅페이스 계정에 로그인.

**남겨둔 자료**: `md` 원본과 9개 코드 블록, 9개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, datasets, peft입니다.

**주요 스택**: `huggingface_hub`, `transformers`, `datasets`, `peft`, `evaluate`

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

## What This Note Covers

### LoRA - BERT 모델을 사용한 PEFT

BERT 모델을 사용하여 PEFT(LoRA) 사용

### LoRA - BERT 모델을 사용한 PEFT > 모델 저장 (Save)

LoRA는 모델 전체가 아니라 학습된 '어댑터(Adapter)' 부분만 저장하면 됩니다. 용량이 매우 작아서 효율적입니다.

### LoRA - BERT 모델을 사용한 PEFT > 실제 테스트 (Inference)

저장된 모델이 새로운 문장을 보고 감정을 잘 맞추는지 직접 테스트해 봅니다.

### Key Step

PEFT - Lora 설정과 학습

## Why This Matters

### 파라미터 효율 미세조정

- 왜 필요한가: 대형 언어모델 전체를 다시 학습하는 비용이 크기 때문에, 적은 자원으로도 실험 가능한 미세조정 방식이 필요합니다.
- 왜 이 방식을 쓰는가: LoRA/QLoRA는 전체 가중치를 모두 바꾸지 않고 작은 적응 파라미터만 학습해 메모리와 시간을 크게 줄일 수 있습니다.
- 원리: 기존 가중치는 고정하고 저차원 행렬 업데이트만 추가로 학습해, 적은 파라미터로도 모델 행동을 조정합니다.

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. LoRA - BERT 모델을 사용한 PEFT: BERT 모델을 사용하여 PEFT(LoRA) 사용
2. LoRA - BERT 모델을 사용한 PEFT > 모델 저장 (Save): LoRA는 모델 전체가 아니라 학습된 '어댑터(Adapter)' 부분만 저장하면 됩니다. 용량이 매우 작아서 효율적입니다.
3. LoRA - BERT 모델을 사용한 PEFT > 실제 테스트 (Inference): 저장된 모델이 새로운 문장을 보고 감정을 잘 맞추는지 직접 테스트해 봅니다.
4. Key Step: PEFT - Lora 설정과 학습

## Code Highlights

### 토크나이저 설정

`토크나이저 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 토크나이저 흐름이 주석과 함께 드러납니다.

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

`PEFT - Lora 설정과 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 LoRA 구성, LoRA 적용, Trainer 구성 흐름이 주석과 함께 드러납니다.

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

### 실제 테스트 (Inference)

`실제 테스트 (Inference)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 테스트: 문장을 넣어 감정 예측해보기, 테스트할 문장, 입력 변환 흐름이 주석과 함께 드러납니다.

```python
# 테스트: 문장을 넣어 감정 예측해보기
import torch

# 테스트할 문장
text = "I feel so happy and excited today!"

# 입력 변환
inputs = tokenizer(text, return_tensors="pt").to(model.device)

# 예측
with torch.no_grad():
    logits = model(**inputs).logits
    predicted_class_id = logits.argmax().item()

# 결과 출력 (Emotion 데이터셋 라벨 매핑)
# 0: sadness, 1: joy, 2: love, 3: anger, 4: fear, 5: surprise
labels = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']
print(f"입력 문장: {text}")
print(f"예측 감정: {labels[predicted_class_id]}")
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
