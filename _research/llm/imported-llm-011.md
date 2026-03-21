---
title: "11 Seq2Seq 예시1"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 11_Seq2Seq_예시1"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 11_Seq2Seq_예시1.md"
excerpt: "목적 본 실습의 목적은 한국어 문장을 영어로 번역하는 기계번역 모델을 구현하고 성능을 비교하는 것이다. 이를 위해 전통적인 Seq2Seq 모델, Attention 기법을 적용한 모델을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을 정량적(BLEU 점수) 및 정성적으로(번역 분석) 평가..."
research_summary: "목적 본 실습의 목적은 한국어 문장을 영어로 번역하는 기계번역 모델을 구현하고 성능을 비교하는 것이다. 이를 위해 전통적인 Seq2Seq 모델, Attention 기법을 적용한 모델을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을 정량적(BLEU 점수) 및 정성적으로(번역 분석) 평가할 것이다. 데이터셋 사용한 데이터는... 본 실습에서는 한영 말뭉치 데이터셋을 기반으로 Sequence-to-Sequence 모델을 구축하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄링 등을 적용하였지만, 문장 예측 품질(BLEU)은 0.1217로 낮았다. 이에... `md` 원본과 36개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 json, os, random, re입니다."
research_artifacts: "md · 코드 36개 · 실행 13개"
code_block_count: 36
execution_block_count: 13
research_focus:
  - "✔️ 사전 세팅"
  - "본 실습에서는 한영 말뭉치 데이터셋을 기반으로 Sequence-to-Sequence 모델을 구축하였다...."
  - "✔️ 요약"
research_stack:
  - "json"
  - "os"
  - "random"
  - "re"
  - "sys"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

목적 본 실습의 목적은 한국어 문장을 영어로 번역하는 기계번역 모델을 구현하고 성능을 비교하는 것이다. 이를 위해 전통적인 Seq2Seq 모델, Attention 기법을 적용한 모델을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을 정량적(BLEU 점수) 및 정성적으로(번역 분석) 평가할 것이다. 데이터셋 사용한 데이터는... 본 실습에서는 한영 말뭉치 데이터셋을 기반으로 Sequence-to-Sequence 모델을 구축하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄링 등을 적용하였지만, 문장 예측 품질(BLEU)은 0.1217로 낮았다. 이에... `md` 원본과 36개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 json, os, random, re입니다.

**빠르게 볼 수 있는 포인트**: ✔️ 사전 세팅, 본 실습에서는 한영 말뭉치 데이터셋을 기반으로 Sequence-to-S..., ✔️ 요약.

**남겨둔 자료**: `md` 원본과 36개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 json, os, random, re입니다.

**주요 스택**: `json`, `os`, `random`, `re`, `sys`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 36 |
| Execution Cells | 13 |
| Libraries | `json`, `os`, `random`, `re`, `sys`, `urllib`, `warnings`, `zipfile` |
| Source Note | `3-2 11_Seq2Seq_예시1` |

## What This Note Covers

### ✔ 요약

본 실습에서는 한영 말뭉치 데이터셋을 기반으로 Sequence-to-Sequence 모델을 구축하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄링 등을 적용하였지만, 문장 예측 품질(BLEU)은 0.1217로 낮았다. 이에 따라 Bahdanau Attention을 추가한 모델...

### ✔ 데이터 설명

목적 본 실습의 목적은 한국어 문장을 영어로 번역하는 기계번역 모델을 구현하고 성능을 비교하는 것이다. 이를 위해 전통적인 Seq2Seq 모델, Attention 기법을 적용한 모델을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을 정량적(BLEU 점수) 및 정성적으로(번역 분석) 평가할 것이다. 데이터셋 사용한 데이터는 AI Hub에서 공개한 「일상생활 및 구어체 한-영...

### ✔ 1. 데이터 분석 > 데이터 재구성

일상생활및구어체_한영_train_set.json의 데이터 개수는 1,200,000개이고, 일상생활및구어체_한영_valid_set.json의 데이터 개수는 150,000개였다. 이번 미션에서 사용하기에는 데이터 개수가 너무 많기 때문에, train_set.json에서 60000, valid_set.json에서 3000개만을 사용하기로 결정했다. 또한, train_set.json의 6000...

### ✔ 1. 데이터 분석 > 불필요한 기호 제거

데이터에 포함된 불필요한 기호는 제거하였다.

## Why This Matters

### 순차 데이터 모델링

- 왜 필요한가: 문장, 시계열처럼 순서가 중요한 데이터는 현재 입력만이 아니라 앞선 맥락까지 함께 봐야 합니다.
- 왜 이 방식을 쓰는가: LSTM/GRU는 기본 RNN보다 긴 문맥을 더 안정적으로 다룰 수 있어 텍스트 분류나 시계열 예측 실습에 자주 쓰입니다.
- 원리: 이전 시점의 은닉 상태를 다음 입력과 함께 업데이트하며, 게이트 구조로 필요한 정보는 남기고 불필요한 정보는 줄입니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

## Implementation Flow

1. ✔ 요약: 본 실습에서는 한영 말뭉치 데이터셋을 기반으로 Sequence-to-Sequence 모델을 구축하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄링 등을 적용하였지만, 문장 예측...
2. ✔ 데이터 설명: 목적 본 실습의 목적은 한국어 문장을 영어로 번역하는 기계번역 모델을 구현하고 성능을 비교하는 것이다. 이를 위해 전통적인 Seq2Seq 모델, Attention 기법을 적용한 모델을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을 정량적(BLEU 점수) 및 정성적으로...
3. ✔ 1. 데이터 분석 > 데이터 재구성: 일상생활및구어체_한영_train_set.json의 데이터 개수는 1,200,000개이고, 일상생활및구어체_한영_valid_set.json의 데이터 개수는 150,000개였다. 이번 미션에서 사용하기에는 데이터 개수가 너무 많기 때문에, train_set.js...
4. ✔ 1. 데이터 분석 > 불필요한 기호 제거: 데이터에 포함된 불필요한 기호는 제거하였다.

## Code Highlights

### ✔️ 사전 세팅

`✔️ 사전 세팅`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

```python
import json
import os
import random
import re
import sys
import urllib.request
import warnings
import zipfile

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from tqdm import tqdm

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction

from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight

import sentencepiece as spm

# ... trimmed ...
```

### 데이터 재구성

`데이터 재구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기존 데이터에서 일부만 사용, train_set.json을 train/val로 나누기, 새로운 파일로 저장 흐름이 주석과 함께 드러납니다.

```python
train_path = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/일상생활및구어체_한영_train_set.json"
valid_path = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/일상생활및구어체_한영_valid_set.json"
out_dir = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/"

with open(train_path, 'r', encoding='utf-8') as f:
    train_data = json.load(f)['data']

with open(valid_path, 'r', encoding='utf-8') as f:
    valid_data = json.load(f)['data']

# 기존 데이터에서 일부만 사용
random.seed(42)
train_sample = random.sample(train_data, 60000)
test_sample = random.sample(valid_data, 3000)

# train_set.json을 train/val로 나누기
val_ratio = 0.1
split_idx = int(len(train_sample) * (1 - val_ratio))
train_split = train_sample[:split_idx]
val_split = train_sample[split_idx:]

# 새로운 파일로 저장
with open(out_dir + "mini_train.json", "w", encoding="utf-8") as f:
    json.dump({"data": train_split}, f, ensure_ascii=False, indent=2)

with open(out_dir + "mini_val.json", "w", encoding="utf-8") as f:
    json.dump({"data": val_split}, f, ensure_ascii=False, indent=2)

# ... trimmed ...
```

### SentencePiece

`SentencePiece`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 옵션 (한국어용, 영어용 따로) 흐름이 주석과 함께 드러납니다.

```python
# 학습 옵션 (한국어용, 영어용 따로)
spm.SentencePieceTrainer.train(
    input=spm_dir + "ko_corpus.txt",
    model_prefix=spm_dir + "spm_ko",
    vocab_size=8000,
    model_type="unigram",
    character_coverage=0.999,
    bos_id=1,
    eos_id=2,
    pad_id=0,
    unk_id=3
)

spm.SentencePieceTrainer.train(
    input=spm_dir + "en_corpus.txt",
    model_prefix=spm_dir + "spm_en",
    vocab_size=8000,
    model_type="unigram",
    character_coverage=1.0,
    bos_id=1,
    eos_id=2,
    pad_id=0,
    unk_id=3
)
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-2 11_Seq2Seq_예시1.md`
- Source formats: `md`
- Companion files: `3-2 11_Seq2Seq_예시1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `SOS_ID`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 본 실습에서는 한영 말뭉치 데이터셋을 기반으로 **Sequence-to-Sequence 모델을 구축**하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄링 등을 적용하였지만, **문장 예측 품질(BLEU)은 0.1217**로 낮았다. 이에 따라 **Bahdanau Attention을 추가**한 모델을 설계하였고, 문맥 정보를 효과적으로 반영하여 번역 품질이 향상되었다. **BLEU 점수도 0.1217 → 0.2381**으로 개선되었다. 이번 실습을 통해 Attention 메커니즘의 중요성을 확인할 수 있었다. 다만 시간 제약으로 인해 Transformer 모델까지 실험하지 못한 점은 아쉬움으로 남는다. 향후에는 Transformer 기반 구조를 적용하여 보다 높은 번역 품질을 달성해보고자 한다.
> **1) 목적** 본 실습의 목적은 한국어 문장을 영어로 번역하는 **기계번역 모델을 구현**하고 성능을 비교하는 것이다. 이를 위해 **전통적인 Seq2Seq 모델**, **Attention 기법을 적용한 모델**을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을 **정량적(BLEU 점수)** 및 **정성적으로(번역 분석) 평가**할 것이다.
