---
title: "미션14 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션14_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션14_1팀_박시찬.md"
excerpt: "미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반으로 사용자의 질문에 정확하게 답변하는 시스템을 구축합니다..."
research_summary: "미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반으로 사용자의 질문에 정확하게 답변하는 시스템을 구축합니다. 사용 데이터셋 * 데이터: 국세청... 작성자: [팀명/성함] 프로젝트 기간: 202X.XX.XX ~ 202X.XX.XX 환경: Google Colab (T4 GPU), LangChain, HuggingFace 프로젝트 개요 (Executive Summary). `ipynb/md` 원본과 19개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, langchain_community, os, random입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 13개"
code_block_count: 19
execution_block_count: 13
research_focus:
  - "미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmen..."
  - "[미션] 2024년 연말정산 가이드 RAG 시스템 구축"
  - "구글 드라이브 마운트"
research_stack:
  - "google"
  - "langchain_community"
  - "os"
  - "random"
  - "numpy"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - mission
---

미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반으로 사용자의 질문에 정확하게 답변하는 시스템을 구축합니다. 사용 데이터셋 * 데이터: 국세청... 작성자: [팀명/성함] 프로젝트 기간: 202X.XX.XX ~ 202X.XX.XX 환경: Google Colab (T4 GPU), LangChain, HuggingFace 프로젝트 개요 (Executive Summary). `ipynb/md` 원본과 19개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, langchain_community, os, random입니다.

**빠르게 볼 수 있는 포인트**: 미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RA..., [미션] 2024년 연말정산 가이드 RAG 시스템 구축, 구글 드라이브 마운트.

**남겨둔 자료**: `ipynb/md` 원본과 19개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, langchain_community, os, random입니다.

**주요 스택**: `google`, `langchain_community`, `os`, `random`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Mission |
| Source Files | `ipynb`, `md` |
| Code Blocks | 19 |
| Execution Cells | 13 |
| Libraries | `google`, `langchain_community`, `os`, `random`, `numpy`, `torch`, `transformers`, `langchain` |
| Source Note | `미션14_1팀_박시찬` |

## What This Note Covers

### [미션] 2024년 연말정산 가이드 RAG 시스템 구축

미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반으로 사용자의 질문에 정확하게 답변하는 시스템을 구축합니다. 사용 데이터셋 * 데이터: 국세청 발간 [2024년 연말정산 신고 안내] * 내용: 연...

### [Final Report] 2024년 연말정산 지능형 QA 시스템 구축 결과 보고서

작성자: [팀명/성함] 프로젝트 기간: 202X.XX.XX ~ 202X.XX.XX 환경: Google Colab (T4 GPU), LangChain, HuggingFace 프로젝트 개요 (Executive Summary)

### 가이드코드

문서 파일 불러오기 Vector DB에 저장

### Key Step

langchain 계열: RAG 체인 구성

## Why This Matters

### RAG 검색 파이프라인

- 왜 필요한가: LLM이 외부 지식을 안정적으로 참조하게 하려면, 생성 전에 관련 문서를 정확히 찾아오는 검색 단계가 먼저 필요합니다.
- 왜 이 방식을 쓰는가: 이 방식은 모델 파라미터만 믿지 않고 최신 문서나 도메인 지식을 붙일 수 있어서 실제 서비스형 QA에 적합합니다.
- 원리: 문서를 청크로 나누고 임베딩한 뒤, 질문과 가까운 벡터를 검색해 프롬프트에 함께 넣는 구조로 동작합니다.

### 에이전트 상태 흐름

- 왜 필요한가: 단일 호출만으로 해결되지 않는 작업은 추론, 도구 호출, 중간 상태 관리가 이어지는 흐름 제어가 필요합니다.
- 왜 이 방식을 쓰는가: 상태 그래프 기반 접근은 단계별 분기와 재시도를 명시적으로 관리할 수 있어 에이전트 실험을 설명하기 좋습니다.
- 원리: 현재 상태를 노드 간에 전달하면서, 조건에 따라 다음 노드나 도구 호출을 결정하는 방식으로 실행 흐름이 이어집니다.

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

## Implementation Flow

1. [미션] 2024년 연말정산 가이드 RAG 시스템 구축: 미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반...
2. [Final Report] 2024년 연말정산 지능형 QA 시스템 구축 결과 보고서: 작성자: [팀명/성함] 프로젝트 기간: 202X.XX.XX ~ 202X.XX.XX 환경: Google Colab (T4 GPU), LangChain, HuggingFace 프로젝트 개요 (Executive Summ...
3. 가이드코드: 문서 파일 불러오기 Vector DB에 저장
4. Key Step: langchain 계열: RAG 체인 구성

## Code Highlights

### 구글 드라이브 마운트

`구글 드라이브 마운트`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ==========================================, PHASE 0. 실험 설계 및 환경 제어 (Implementation) 흐름이 주석과 함께 드러납니다.

```python
# ==========================================
# PHASE 0. 실험 설계 및 환경 제어 (Implementation)
# ==========================================

import os
import random
import numpy as np
import torch
import transformers
import langchain

# ------------------------------------------
# 0-1. 통제 변수 설정 (Random Seed Fixation)
# ------------------------------------------
def set_seed(seed=42):
    """
    실험의 재현성(Reproducibility)을 위해 모든 난수 생성기의 시드를 고정합니다.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # Multi-GPU 사용 시

    # CuDNN 결정론적 옵션 (속도는 약간 느려질 수 있으나 재현성 확보됨)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

# ... trimmed ...
```

### 구글 드라이브 마운트

`구글 드라이브 마운트`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 ==========================================, PHASE 2. 생성 모델 엔지니어링 (Implementation) 흐름이 주석과 함께 드러납니다.

```python
# ==========================================
# PHASE 2. 생성 모델 엔지니어링 (Implementation)
# ==========================================

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import gc

# ------------------------------------------
# [중요] 메모리 청소 (VRAM 확보)
# ------------------------------------------
# PHASE 1에서 임베딩 모델이 GPU 메모리를 먹고 있으므로,
# LLM 로드 전에 최대한 비워줘야 합니다.
gc.collect()
torch.cuda.empty_cache()
print(f"🧹 Memory Cleared. Current Allocated: {torch.cuda.memory_allocated(0) / 1e9:.2f} GB")


# ------------------------------------------
# 2-1. LLM 경량화 및 로드 (4-bit Quantization)
# ------------------------------------------
print("\n🔄 [2-1] Loading LLM with 4-bit Quantization...")

# [모델 선택 전략: VRAM 6GB 대응]
# KULLM3(10B+) -> 불가능 (OOM)
# Llama-3-Ko-8B -> 매우 위험 (OOM 가능성 높음)
# Recommendation: Llama-3.2-Korean-Bllossom-AICA-5B (안전하고 성능 좋음)
# ... trimmed ...
```

### 가이드코드

`가이드코드`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 language_model_name = "Bllossom/llama-3.2-Korean-... 흐름이 주석과 함께 드러납니다.

```python
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
import torch


language_model_name = "nlpai-lab/KULLM3"
# language_model_name = "Bllossom/llama-3.2-Korean-Bllossom-AICA-5B"

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    llm_int8_enable_fp32_cpu_offload=True,
)
model = AutoModelForCausalLM.from_pretrained(
    language_model_name,
    quantization_config=bnb_config,
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(language_model_name)
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/미션14_1팀_박시찬.md`
- Source formats: `ipynb`, `md`
- Companion files: `미션14_1팀_박시찬.ipynb`, `미션14_1팀_박시찬.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `www.nts.go.kr`, `localhost`

## Note Preview

> 1. 미션 소개 **LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다.** LangChain 프레임워크를 사용하여, **2024년 국세청 연말정산 안내 문서**를 기반으로 사용자의 질문에 정확하게 답변하는 시스템을 구축합니다.
> 2. 사용 데이터셋 * **데이터:** 국세청 발간 [2024년 연말정산 신고 안내] * **내용:** 연말정산 절차, 공제 항목, 유의사항, **2024년 개정 세법** 등 * **목표:** 텍스트에 포함된 세법 정보와 절차를 LLM이 이해하고 참조할 수 있도록 처리
