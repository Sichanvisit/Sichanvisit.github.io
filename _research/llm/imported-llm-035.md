---
title: "미션11 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션11_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션11_1팀_박시찬.md"
excerpt: "Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교"
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
| Code Blocks | 43 |
| Execution Cells | 0 |
| Libraries | `os`, `json`, `random`, `re`, `numpy`, `torch`, `pandas`, `matplotlib` |
| Source Note | `미션11_1팀_박시찬` |

## What I Worked On

- 🧩 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트
- 데이터 로드
- 1. 환경 준비 ─────────────────────────────────────────────────────────────
- 영어 토크나이저
- 한국어 토크나이저 (옵션)

## Implementation Flow

1. 🧩 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트
2. 데이터 로드
3. 1. 환경 준비 ─────────────────────────────────────────────────────────────
4. 영어 토크나이저
5. 한국어 토크나이저 (옵션)
6. 재현성

## Code Highlights

### Seq2Seq

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

### Seq2Seq

```python
import os, torch

src_vocab = sp_ko.vocab_size()
tgt_vocab = sp_en.vocab_size()

enc = Encoder(src_vocab, emb=512, hid=512, bi=True, drop=0.2)
dec = Decoder(tgt_vocab, emb=512, hid=512, drop=0.2, tie_weights=True)
model = Seq2Seq(enc, dec).to(device)

opt = torch.optim.Adam(model.parameters(), lr=3e-4)
use_cuda = torch.cuda.is_available()
scaler = amp.GradScaler('cuda' if use_cuda else 'cpu')

# 1) sanity overfit(선택): 1k 샘플에 1~2 epoch로 loss 급락 확인
tiny_idx = torch.randperm(len(train_ds))[:1000].tolist()
tiny_loader = DataLoader(torch.utils.data.Subset(train_ds, tiny_idx),
                         batch_size=128, shuffle=True, collate_fn=collate_sp)
for e in range(2):
    loss = train_epoch(model, tiny_loader, opt, scaler, tf_ratio=0.7)
    print(f"[tiny-seq2seq] epoch {e + 1} | loss {loss:.3f}")

# 2) full train
EPOCHS = 20
tf_start, tf_end = 0.6, 0.2
best_bleu, best_state = -1, None

for epoch in range(1, EPOCHS + 1):
    tf_ratio = tf_end + (tf_start - tf_end) * max(0, (EPOCHS - epoch) / (EPOCHS - 1))
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

> ---
> Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교
