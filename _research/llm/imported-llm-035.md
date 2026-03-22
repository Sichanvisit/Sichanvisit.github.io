---
title: "미션11 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션11_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션11_1팀_박시찬.md"
excerpt: "미션 11: 한국어→영어 기계 번역..., 분석/시각화 세트 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 미션 11: 한국어→영어 기계 번역..., 분석/시각화 세트, 데이터 로드 순서로 핵심 장면을 먼저 훑고, 정제후 OOV..."
research_summary: "미션 11: 한국어→영어 기계 번역..., 분석/시각화 세트 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 미션 11: 한국어→영어 기계 번역..., 분석/시각화 세트, 데이터 로드 순서로 핵심 장면을 먼저 훑고, 정제후 OOV, Seq2Seq, Seq2Seq + Attention 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 43개 코드 블록, 0개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, random, re입니다."
research_artifacts: "ipynb/md · 코드 43개 · 실행 0개"
code_block_count: 43
execution_block_count: 0
research_focus:
  - "미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트"
  - "분석/시각화 세트"
  - "데이터 로드"
research_stack:
  - "os"
  - "json"
  - "random"
  - "re"
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

미션 11: 한국어→영어 기계 번역..., 분석/시각화 세트 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 미션 11: 한국어→영어 기계 번역..., 분석/시각화 세트, 데이터 로드 순서로 핵심 장면을 먼저 훑고, 정제후 OOV, Seq2Seq, Seq2Seq + Attention 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 43개 코드 블록, 0개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, random, re입니다.

**빠르게 볼 수 있는 포인트**: 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트, 분석/시각화 세트, 데이터 로드.

**남겨둔 자료**: `ipynb/md` 원본과 43개 코드 블록, 0개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, random, re입니다.

**주요 스택**: `os`, `json`, `random`, `re`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Mission |
| Source Files | `ipynb`, `md` |
| Code Blocks | 43 |
| Execution Cells | 0 |
| Libraries | `os`, `json`, `random`, `re`, `numpy`, `torch`, `pandas`, `matplotlib` |
| Source Note | `미션11_1팀_박시찬` |

## What This Note Covers

### 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트

Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교 이번 미션에서는 한국어 문장을 영어로 번역하는 기계 번역 모델을 직접 구축하고 학습합니다. 다음 두 가지 모델을 구현하고 성능을 비교∙분석합니다.

- 읽을 포인트: 세부 흐름: 🧩 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트

#### 🧩 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트

🧩 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. * 데이터는 JSON 파일 형식이며, 각 항목은 다음 구조로 구성됨.

### 분석/시각화 세트

[Overall] BLEU=1.71 / chrF=12.91 / n=2136 BLEU chrF n [0,8) 1.892464 12.902399 566.0 [8,12) 2.385305 14.320471 658.0 [12,16) 1.160073 12.931954 494.0 [16,20) 1.041161 11.871017 281.0 [20,...

- 읽을 포인트: 분석/시각화 세트 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 데이터 로드

데이터 로드 코드를 직접 따라가며 데이터 로드 흐름을 확인했습니다.

- 읽을 포인트: 데이터 로드 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### EDA적용

(지금까지 결과 기반), 정제후 길이, 서브워드 같은 코드를 직접 따라가며 EDA적용 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: (지금까지 결과 기반), 정제후 길이, 서브워드

#### (지금까지 결과 기반)

정규화/클린 - ‘>’ 제거, 완전 중복 제거(ko_norm+en_norm 기준). - 길이 정책 - MAX_LEN: KO 16, EN 27(98p). - 길이비 컷: r ∈ [0.6, 4.0]로 시작, 정리 후 [0.8, 3.5]로 좁히는 것도 가능(95p에 맞춤). - 토크나이...

#### 정제후 길이

데이터 상태를 점검한 뒤 다음 전처리와 학습 단계로 넘어가기 위한 구간입니다.

#### 서브워드

데이터 상태를 점검한 뒤 다음 전처리와 학습 단계로 넘어가기 위한 구간입니다.

### Seq2Seq

Seq2Seq 코드를 직접 따라가며 Seq2Seq 흐름을 확인했습니다.

- 읽을 포인트: Seq2Seq 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

## Why This Matters

### 순차 데이터 모델링

- 왜 필요한가: 문장, 시계열처럼 순서가 중요한 데이터는 현재 입력만이 아니라 앞선 맥락까지 함께 봐야 합니다.
- 왜 이 방식을 쓰는가: LSTM/GRU는 기본 RNN보다 긴 문맥을 더 안정적으로 다룰 수 있어 텍스트 분류나 시계열 예측 실습에 자주 쓰입니다.
- 원리: 이전 시점의 은닉 상태를 다음 입력과 함께 업데이트하며, 게이트 구조로 필요한 정보는 남기고 불필요한 정보는 줄입니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

## Implementation Flow

1. 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트: 🧩 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트
2. 분석/시각화 세트: [Overall] BLEU=1.71 / chrF=12.91 / n=2136 BLEU chrF n [0,8) 1.892464 12.902399 566.0 [8,12) 2.385305 14.320471 658.0 [12,16) 1.160073 12...
3. 데이터 로드: 데이터 로드 코드를 직접 따라가며 데이터 로드 흐름을 확인했습니다.
4. EDA적용: (지금까지 결과 기반), 정제후 길이
5. Seq2Seq: Seq2Seq 코드를 직접 따라가며 Seq2Seq 흐름을 확인했습니다.

## Code Highlights

### 정제후 OOV

`정제후 OOV`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 토큰화 흐름이 주석과 함께 드러납니다.

```python
SPECIALS = ["<PAD>", "<SOS>", "<EOS>", "<UNK>"]


def build_vocab(tokens_list, min_freq=2):
    cnt = Counter(w for sent in tokens_list for w in sent)
    itos = SPECIALS + [w for w, c in cnt.items() if c >= min_freq]
    stoi = {w: i for i, w in enumerate(itos)}
    return stoi, itos, cnt


def oov_rate(tokens_list, stoi):
    tot = 0
    oov = 0
    for sent in tokens_list:
        for w in sent:
            tot += 1
            if w not in stoi:
                oov += 1
    return oov / tot if tot else 0.0


# 토큰화
train_ko_ws = [s.split() for s in df_clean["ko_norm"]]
valid_ko_ws = [s.split() for s in df_valid["ko_norm"]]
train_en = [tokenize_en(s) for s in df_clean["en_norm"]]
valid_en = [tokenize_en(s) for s in df_valid["en_norm"]]

if USE_OKT and (okt is not None):
# ... trimmed ...
```

### Seq2Seq

`Seq2Seq`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 성능/안정: Windows/노트북에선 num_workers=0 권장(앞서 병목 이슈 대비) 흐름이 주석과 함께 드러납니다.

```python
import torch
from torch.utils.data import Dataset, DataLoader
from torch.nn.utils.rnn import pad_sequence

PAD_ID, SOS_ID, EOS_ID, UNK_ID = 0, 1, 2, 3


def sp_encode_ids(sp, text, add_specials=True, max_len=None):
    ids = sp.encode(text, out_type=int)
    if add_specials:
        ids = [SOS_ID] + ids + [EOS_ID]
    if max_len is not None:
        ids = ids[:max_len]
    return torch.tensor(ids, dtype=torch.long)


class MTDatasetSP(Dataset):
    def __init__(self, df, sp_src, sp_tgt, max_src=None, max_tgt=None):
        self.src = df["ko_norm"].tolist()
        self.tgt = df["en_norm"].tolist()
        self.sp_src = sp_src;
        self.sp_tgt = sp_tgt
        self.max_src = max_src;
        self.max_tgt = max_tgt

    def __len__(self): return len(self.src)

    def __getitem__(self, i):
# ... trimmed ...
```

### Seq2Seq + Attention

`Seq2Seq + Attention`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 enc_out: [B,S,Eenc] (fp16일 수 있음), dec_h: [B,Hdec], autocast OFF: 이 블록은 항상 fp32로 계산, fp16에서도 안전한 마스크 값 사용(−1e4 권장) 흐름이 주석과 함께 드러납니다.

```python
import torch
import torch.nn as nn

PAD_ID, SOS_ID, EOS_ID, UNK_ID = 0, 1, 2, 3
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class EncoderAttn(nn.Module):
    def __init__(self, vocab_size, emb=512, hid=512, layers=1, bi=True, drop=0.2):
        super().__init__()
        self.emb = nn.Embedding(vocab_size, emb, padding_idx=PAD_ID)
        self.rnn = nn.GRU(emb, hid, num_layers=layers, batch_first=True,
                          bidirectional=bi, dropout=(drop if layers > 1 else 0.0))
        self.bi = bi
        self.bridge = nn.Linear(hid * (2 if bi else 1), hid)

    def forward(self, src, src_mask):
        x = self.emb(src)  # [B,S,E]
        out, h = self.rnn(x)  # out:[B,S,H*dir], h:[L*dir,B,H]
        if self.bi:
            h0 = torch.cat([h[-2], h[-1]], dim=-1)  # [B,2H]
        else:
            h0 = h[-1]
        h0 = torch.tanh(self.bridge(h0)).unsqueeze(0)  # [1,B,H]
        return out, h0  # enc_out for attention


class BahdanauAttention(nn.Module):
# ... trimmed ...
```

### 분석/시각화 세트

`분석/시각화 세트`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 분석할 모델 선택, seq2seq(베이스라인)을 보고 싶으면: model_to_eval = model, attn 모델이면: model_to_eval = model_attn 흐름이 주석과 함께 드러납니다.

```python
import re, numpy as np, pandas as pd
from sacrebleu import corpus_bleu
from sacrebleu.metrics import CHRF

# 분석할 모델 선택
# - seq2seq(베이스라인)을 보고 싶으면: model_to_eval = model
# - attn 모델이면: model_to_eval = model_attn
model_to_eval = model_attn  # 혹은 model

IS_ATTN = isinstance(model_to_eval.dec, (DecoderAttn,))  # 대략적인 판별
chrf = CHRF(word_order=2)  # chrF++


def decode_batch_any(model, src, src_mask, max_len):
    if IS_ATTN:
        return greedy_decode_any(model, src, src_mask, max_len)
    else:
        return greedy_decode(model, src, src_mask, max_len)


def collect_predictions(model, loader, sp_src, sp_tgt):
    hyps, refs, src_txts, ref_txts, src_lens = [], [], [], [], []
    for i in range(len(loader.dataset)):
        src_ids, tgt_ids = loader.dataset[i]
        src_text = sp_src.decode([x for x in src_ids.tolist() if x not in (PAD_ID, SOS_ID, EOS_ID)])
        ref_text = sp_tgt.decode([x for x in tgt_ids.tolist() if x not in (PAD_ID, SOS_ID, EOS_ID)])
        # 한 샘플 배치로 디코딩
        batch = collate_sp([(src_ids, tgt_ids)])
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/미션11_1팀_박시찬.md`
- Source formats: `ipynb`, `md`
- Companion files: `미션11_1팀_박시찬.ipynb`, `미션11_1팀_박시찬.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `ko_len_tok", "en_len_tok", "len_ratio_en_per_ko`, `ko_len_tok", "en_len_tok`, `ko_len_tok", "en_len_tok", "len_ratio`, `ko_sp_len", "en_sp_len", "sp_ratio`, `13_LLM_code_Roadmap.md`

## Note Preview

> Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교
> 📌 프로젝트 개요
