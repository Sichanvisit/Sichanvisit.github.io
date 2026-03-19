---
title: "10 텍스트임베딩 예"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1_10_텍스트임베딩_예"
source_path: "13_LLM_GenAI/Code_Snippets/3-1_10_텍스트임베딩_예.md"
excerpt: "--- tags: [\"LLM\", \"Code\"] ---"
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
| Code Blocks | 45 |
| Execution Cells | 45 |
| Libraries | `os`, `random`, `re`, `sys`, `urllib`, `warnings`, `zipfile`, `numpy` |
| Source Note | `3-1_10_텍스트임베딩_예` |

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
import os
import random
import re
import sys
import urllib.request
import warnings
import zipfile

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from tqdm import tqdm

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight

from gensim.models import FastText, Word2Vec

import torch
import torch.nn as nn
# ... trimmed ...
```

### **LSTM 모델 정의**

```python
class LSTMClassifier(nn.Module):
    def __init__(self, embedding_matrix, hidden_dim, output_dim, num_layers, dropout):
        super(LSTMClassifier, self).__init__()

        vocab_size, embedding_dim = embedding_matrix.shape

        # 1. 임베딩 레이어
        self.embedding = nn.Embedding.from_pretrained(
            torch.tensor(embedding_matrix, dtype=torch.float).to(device),
            freeze=False
        )

        # 2. LSTM
        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            dropout=dropout if num_layers > 1 else 0,
            batch_first=True,
            bidirectional=True
        )

        # 3. FC 레이어
        self.fc = nn.Linear(hidden_dim * 2, output_dim)

    def forward(self, x):
        x = self.embedding(x)
        _, (hidden, _) = self.lstm(x)
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-1_10_텍스트임베딩_예.md`
- Source formats: `md`
- Companion files: `3-1_10_텍스트임베딩_예.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `nlp.stanford.edu`

## Note Preview

> --- tags: ["LLM", "Code"] ---
> ---
