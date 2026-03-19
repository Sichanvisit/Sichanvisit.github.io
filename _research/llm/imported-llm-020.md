---
title: "3 Gemma QLoRA"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-4 (실습)3_Gemma_QLoRA"
source_path: "13_LLM_GenAI/Code_Snippets/3-4 (실습)3_Gemma_QLoRA.md"
excerpt: "LLM과 같은 대규모 모델에서 더욱 효율 적인 미세조정 즉, PEFT(Parameter-Efficient Fine-Tuning)을 하기위한 가장 대표적인 방식이 바로 Lora 방식 입니다."
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
| Code Blocks | 20 |
| Execution Cells | 16 |
| Libraries | `huggingface_hub`, `transformers`, `torch`, `datasets`, `peft`, `trl`, `shutil`, `google` |
| Source Note | `3-4 (실습)3_Gemma_QLoRA` |

## What I Worked On

- Lora 기법을 활용한 PEFT
- 초기화 과정
- 라이브러리 설치
- 1. Gemma 모델 PEFT
- 양자화 하여 모델 로드

## Implementation Flow

1. Lora 기법을 활용한 PEFT
2. 초기화 과정
3. 라이브러리 설치
4. 1. Gemma 모델 PEFT
5. 양자화 하여 모델 로드
6. 4비트 양자화: https://huggingface.co/docs/transformers/ko/quantization/bitsandbytes#normal-float-4-(nf4)

## Code Highlights

### 양자화 하여 모델 로드

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

### PEFT 학습 진행

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
