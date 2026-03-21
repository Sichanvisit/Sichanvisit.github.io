---
title: "3 Gemma QLoRA"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-4 (실습)3_Gemma_QLoRA"
source_path: "13_LLM_GenAI/Code_Snippets/3-4 (실습)3_Gemma_QLoRA.md"
excerpt: "LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(Parameter-Efficient Fine-Tuning)을 하기위한 가장 대표적인 방식이 바로 Lora 방식 입니다"
research_summary: "LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(Parameter-Efficient Fine-Tuning)을 하기위한 가장 대표적인 방식이 바로 Lora 방식 입니다. transformers > 4.50.1 : gemma3 가 포함된 최신 transformers 버전 2. bitsandbytes : 양자화를 위한 라이브러리 3. trl : SFTTrainer를 활용하여 학습하기 위한 라이브러리 4. datasets : Hugging Face Hub에 저장된 데이터세트를 불러오기 위한 라이브러리. `md` 원본과 20개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, torch, datasets입니다."
research_artifacts: "md · 코드 20개 · 실행 16개"
code_block_count: 20
execution_block_count: 16
research_focus:
  - "LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(Parameter-Efficien..."
  - "Lora 기법을 활용한 PEFT"
  - "초기화 과정"
research_stack:
  - "huggingface_hub"
  - "transformers"
  - "torch"
  - "datasets"
  - "peft"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(Parameter-Efficient Fine-Tuning)을 하기위한 가장 대표적인 방식이 바로 Lora 방식 입니다. transformers > 4.50.1 : gemma3 가 포함된 최신 transformers 버전 2. bitsandbytes : 양자화를 위한 라이브러리 3. trl : SFTTrainer를 활용하여 학습하기 위한 라이브러리 4. datasets : Hugging Face Hub에 저장된 데이터세트를 불러오기 위한 라이브러리. `md` 원본과 20개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, torch, datasets입니다.

**빠르게 볼 수 있는 포인트**: LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(..., Lora 기법을 활용한 PEFT, 초기화 과정.

**남겨둔 자료**: `md` 원본과 20개 코드 블록, 16개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, torch, datasets입니다.

**주요 스택**: `huggingface_hub`, `transformers`, `torch`, `datasets`, `peft`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 20 |
| Execution Cells | 16 |
| Libraries | `huggingface_hub`, `transformers`, `torch`, `datasets`, `peft`, `trl`, `shutil`, `google` |
| Source Note | `3-4 (실습)3_Gemma_QLoRA` |

## What This Note Covers

### Lora 기법을 활용한 PEFT

LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(Parameter-Efficient Fine-Tuning)을 하기위한 가장 대표적인 방식이 바로 Lora 방식 입니다.

### 라이브러리 설치

transformers > 4.50.1 : gemma3 가 포함된 최신 transformers 버전 2. bitsandbytes : 양자화를 위한 라이브러리 3. trl : SFTTrainer를 활용하여 학습하기 위한 라이브러리 4. datasets : Hugging Face Hub에 저장된 데이터세트를 불러오기 위한 라이브러리

### Gemma 모델 PEFT

Gemma3 모델은 구글에서 Gemini 모델을 만드는 데 사용된 것과 동일한 연구 및 기술로 구축한 GPT 기반의 최신 텍스트 생성 모델입니다.

### 양자화 하여 모델 로드

LLM 모델을 더욱 특정 테스크에 최적화하여 더욱 효율 적으로 사용하기 위해 모델의 크기를 줄이는 경량화 작업을 진행할 수 있습니다.

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

1. Lora 기법을 활용한 PEFT: LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(Parameter-Efficient Fine-Tuning)을 하기위한 가장 대표적인 방식이 바로 Lora 방식 입니다.
2. 라이브러리 설치: transformers > 4.50.1 : gemma3 가 포함된 최신 transformers 버전 2. bitsandbytes : 양자화를 위한 라이브러리 3. trl : SFTTrainer를 활용하여 학습하기 위한 라이브러리 4. datasets : Hugging Face Hu...
3. Gemma 모델 PEFT: Gemma3 모델은 구글에서 Gemini 모델을 만드는 데 사용된 것과 동일한 연구 및 기술로 구축한 GPT 기반의 최신 텍스트 생성 모델입니다.
4. 양자화 하여 모델 로드: LLM 모델을 더욱 특정 테스크에 최적화하여 더욱 효율 적으로 사용하기 위해 모델의 크기를 줄이는 경량화 작업을 진행할 수 있습니다.

## Code Highlights

### 양자화 하여 모델 로드

`양자화 하여 모델 로드`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 4비트 양자화: https://huggingface.co/docs/transformers..., 양자화를 적용하여 모델 로드: https://huggingface.co/docs/tran... 흐름이 주석과 함께 드러납니다.

```python
from transformers import AutoTokenizer, BitsAndBytesConfig, AutoModelForCausalLM
import torch

model_id = "google/gemma-3-1b-it"

# 4비트 양자화: https://huggingface.co/docs/transformers/ko/quantization/bitsandbytes#normal-float-4-(nf4)
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,                        # 가중치를 4-bit 양자화
    bnb_4bit_compute_dtype=torch.float16,     # 연산 텐서는 float16 사용
    bnb_4bit_quant_type="nf4",                # NormalFloat4 양자화 타입 (분포를 유연하게)
    bnb_4bit_use_double_quant=True            # 더블 양자화 (양자화 노이즈를 보다 잘 보정하려는 목적)
)

# 양자화를 적용하여 모델 로드: https://huggingface.co/docs/transformers/en/main_classes/model
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=quantization_config,    # 양자화 적용
    attn_implementation="eager"                 # 안정적인 eager 어텐션 사용
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_id)

print(model)
```

### 텍스트 생성해보기

`텍스트 생성해보기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. AutoTokenizer로 토크나이져를 생성한 후 apply_chat_template() 함수를 통해 역할이 지정된 프롬프트 텍스트를 토큰화 하고 모델 입력에 맞게 구성해 줍니다.

```python
tokenizer = AutoTokenizer.from_pretrained(model_id)

messages = [
    [
        {
            "role": "system",
            "content": "마크다운 표기 없이 일반 텍스트 형식으로 답변 작성"
        },
        {
            "role": "user",
            "content": "LLM과 허깅페이스에 대한 간략한 설명"
        },
    ],
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device).to(torch.bfloat16)

inputs
```

### PEFT 학습 진행

`PEFT 학습 진행`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 === 기본 설정 ===, === 배치 처리 ===, === 메모리 관리 === 흐름이 주석과 함께 드러납니다.

```python
from trl import SFTConfig

save_model = "gemma-text-to-sum4"

args = SFTConfig(
    # === 기본 설정 ===
    output_dir=save_model,                  # 학습된 모델을 저장할 폴더 이름
    num_train_epochs=1,                     # 전체 데이터를 몇 번 반복 학습할지 (1번만)
    eval_strategy="no",                     # 평가 전략을 'epoch'으로 설정하여 save_strategy와 일치시킴
    do_eval=False,                          # 평가 활성화

    # === 배치 처리 ===
    per_device_train_batch_size=2,          # GPU가 한 번에 처리할 샘플 개수 (2개씩)
    gradient_accumulation_steps=4,          # 4번 모아서 한 번에 업데이트 (실제로는 2×4=8개)

    # === 메모리 관리 ===
    gradient_checkpointing=False,           # 메모리 절약 기능 끄기 (속도 우선)
    fp16=True,                              # 16비트 사용 (32비트의 절반, 메모리↓ 속도↑)

    # === 학습 속도 ===
    learning_rate=2e-4,                     # 학습 보폭 (0.0002, 한 번에 얼마나 크게 변화)
    optim="adamw_torch_fused",              # 옵티마이저 종류 (학습 방법, 빠른 버전)
    lr_scheduler_type="constant",           # 학습률 고정 (처음부터 끝까지 동일)
    warmup_ratio=0.03,                      # 처음 3%는 천천히 시작 (급발진 방지)

    # === 안정성 ===
    max_grad_norm=0.3,                      # 그래디언트 폭주 방지 (최대 0.3까지만)
    weight_decay=2e-4,                      # 과적합 방지 (가중치 조금씩 줄이기)
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-4 (실습)3_Gemma_QLoRA.md`
- Source formats: `md`
- Companion files: `3-4 (실습)3_Gemma_QLoRA.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `developers.googleblog.com`, `huggingface.co`, `localhost`, `drive.google.com`, `www.youtube.com`

## Note Preview

> LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(Parameter-Efficient Fine-Tuning)을 하기위한 가장 대표적인 방식이 바로 Lora 방식 입니다.
> 해당 예시에서는 허깅페이스로 모델을 불러온뒤 LoraConfig를 활용하여 구글의 gemma3 모델을 한국어 뉴스 요약 테스크로 PEFT 진행하는 과정을 살펴봅니다.
