---
title: "11 Seq2Seq 예시1"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 11_Seq2Seq_예시1"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 11_Seq2Seq_예시1.md"
excerpt: "본 실습에서는 한영 말뭉치 데이터셋을 기반으로 **Sequence-to-Sequence 모델을 구축**하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄..."
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
| Code Blocks | 36 |
| Execution Cells | 13 |
| Libraries | `json`, `os`, `random`, `re`, `sys`, `urllib`, `warnings`, `zipfile` |
| Source Note | `3-2 11_Seq2Seq_예시1` |

## What I Worked On

- ✔️ 사전 세팅
- Warnings 제거
- Pandas 보기 옵션
- GPU 설정
- ✔️ 요약

## Implementation Flow

1. ✔️ 사전 세팅
2. Warnings 제거
3. Pandas 보기 옵션
4. GPU 설정
5. ✔️ 요약
6. ✔️ **데이터 설명**

## Code Highlights

### ✔️ 사전 세팅

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

### **데이터 재구성**

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

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-2 11_Seq2Seq_예시1.md`
- Source formats: `md`
- Companion files: `3-2 11_Seq2Seq_예시1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `SOS_ID`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> ---
> 본 실습에서는 한영 말뭉치 데이터셋을 기반으로 **Sequence-to-Sequence 모델을 구축**하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄링 등을 적용하였지만, **문장 예측 품질(BLEU)은 0.1217**로 낮았다. 이에 따라 **Bahdanau Attention을 추가**한 모델을 설계하였고, 문맥 정보를 효과적으로 반영하여 번역 품질이 향상되었다. **BLEU 점수도 0.1217 → 0.2381**으로 개선되었다. 이번 실습을 통해 Attention 메커니즘의 중요성을 확인할 수 있었다. 다만 시간 제약으로 인해 Transformer 모델까지 실험하지 못한 점은 아쉬움으로 남는다. 향후에는 Transformer 기반 구조를 적용하여 보다 높은 번역 품질을 달성해보고자 한다.
