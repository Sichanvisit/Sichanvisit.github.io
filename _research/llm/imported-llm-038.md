---
title: "미션14 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션14_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션14_1팀_박시찬.md"
excerpt: "1. 미션 소개 **LLM이 외부 문서의 정보를 참고하여 답변할 수 있도록 RAG(Retrieval-Augmented Generation)를 구현하는 프로젝트입니다.** LangChain 프레임워크를 사용하여, **2024년 국세청 연말정산 안내 문서**를 기반으..."
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
| Code Blocks | 19 |
| Execution Cells | 13 |
| Libraries | `google`, `langchain_community`, `os`, `random`, `numpy`, `torch`, `transformers`, `langchain` |
| Source Note | `미션14_1팀_박시찬` |

## What I Worked On

- [미션] 2024년 연말정산 가이드 RAG 시스템 구축
- 구글 드라이브 마운트
- - langchain 계열: RAG 체인 구성
- - faiss-cpu/gpu: 벡터 검색 엔진
- - bitsandbytes, accelerate: LLM 경량화(4bit) 및 가속

## Implementation Flow

1. [미션] 2024년 연말정산 가이드 RAG 시스템 구축
2. 구글 드라이브 마운트
3. - langchain 계열: RAG 체인 구성
4. - faiss-cpu/gpu: 벡터 검색 엔진
5. - bitsandbytes, accelerate: LLM 경량화(4bit) 및 가속
6. - pypdf: PDF 문서 로딩

## Code Highlights

### 구글 드라이브 마운트

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
