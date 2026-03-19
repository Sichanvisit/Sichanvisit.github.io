---
title: "미션14 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션14_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션14_1팀_박시찬.md"
excerpt: "미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다"
research_summary: "미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반으로 사용자의 질문에 정확하게 답변하는 시스템을 구축합니다. 작성자: [팀명/성함] 프로젝트 기간: 202X.XX.XX ~ 202X.XX.XX 환경: Google Colab (T4 GPU), LangChain, HuggingFace. `ipynb/md` 원본과 19개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, langchain_community, os, random입니다."
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

미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반으로 사용자의 질문에 정확하게 답변하는 시스템을 구축합니다. 작성자: [팀명/성함] 프로젝트 기간: 202X.XX.XX ~ 202X.XX.XX 환경: Google Colab (T4 GPU), LangChain, HuggingFace. `ipynb/md` 원본과 19개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, langchain_community, os, random입니다.

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

미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반으로 사용자의 질문에 정확하게 답변하는 시스템을 구축합니다.

### [Final Report] 2024년 연말정산 지능형 QA 시스템 구축 결과 보고서

작성자: [팀명/성함] 프로젝트 기간: 202X.XX.XX ~ 202X.XX.XX 환경: Google Colab (T4 GPU), LangChain, HuggingFace

### Key Step

langchain 계열: RAG 체인 구성

### Key Step

faiss-cpu/gpu: 벡터 검색 엔진

## Implementation Flow

1. [미션] 2024년 연말정산 가이드 RAG 시스템 구축: 미션 소개 LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다. LangChain 프레임워크를 사용하여, 2024년 국세청 연말정산 안내 문서를 기반...
2. [Final Report] 2024년 연말정산 지능형 QA 시스템 구축 결과 보고서: 작성자: [팀명/성함] 프로젝트 기간: 202X.XX.XX ~ 202X.XX.XX 환경: Google Colab (T4 GPU), LangChain, HuggingFace
3. Key Step: langchain 계열: RAG 체인 구성
4. Key Step: faiss-cpu/gpu: 벡터 검색 엔진

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
> ---
