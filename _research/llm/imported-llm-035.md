---
title: "미션11 1팀 박시찬"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Mission"
source_title: "미션11_1팀_박시찬"
source_path: "13_LLM_GenAI/Code_Snippets/미션11_1팀_박시찬.md"
excerpt: "Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교"
research_summary: "Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교. 무엇을 봤나 - 빈 문장: 0% (OK) - 완전 중복 페어: 4.64% - 한-다/다-한 중복: KO 6.75%, EN 8.96% - 예시에 ‘>네.’, ‘>Yes.’ 같은 ‘>’ 표식 다수 - 왜 중요하나 - 완전 중복은 모델이 일부 문장에 과적합하고, 평가가 과대평가될 수 있음. - ‘>’ 표식은 의미 없는 토큰을 늘려 어휘와... `ipynb/md` 원본과 43개 코드 블록, 0개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, random, re입니다."
research_artifacts: "ipynb/md · 코드 43개 · 실행 0개"
code_block_count: 43
execution_block_count: 0
research_focus:
  - "Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교"
  - "🧩 미션 11"
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

Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교. 무엇을 봤나 - 빈 문장: 0% (OK) - 완전 중복 페어: 4.64% - 한-다/다-한 중복: KO 6.75%, EN 8.96% - 예시에 ‘>네.’, ‘>Yes.’ 같은 ‘>’ 표식 다수 - 왜 중요하나 - 완전 중복은 모델이 일부 문장에 과적합하고, 평가가 과대평가될 수 있음. - ‘>’ 표식은 의미 없는 토큰을 늘려 어휘와... `ipynb/md` 원본과 43개 코드 블록, 0개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, random, re입니다.

**빠르게 볼 수 있는 포인트**: Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교, 🧩 미션 11, 데이터 로드.

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

### 🧩 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트

Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교

### 무결성/중복

무엇을 봤나 - 빈 문장: 0% (OK) - 완전 중복 페어: 4.64% - 한-다/다-한 중복: KO 6.75%, EN 8.96% - 예시에 ‘>네.’, ‘>Yes.’ 같은 ‘>’ 표식 다수 - 왜 중요하나 - 완전 중복은 모델이 일부 문장에 과적합하고, 평가가 과대평가될 수 있음. - ‘>’ 표식은 의미 없는 토큰을 늘려 어휘와 길이 통계를 왜곡. - 액션 - 정규화에서 ‘>’ 제거...

### 길이 분포와 길이비

무엇을 봤나 - KO 토큰 중앙값 6, 95p 14, 99p 18 - EN 토큰 중앙값 11, 95p 23, 99p 30 - 길이비 EN/KO 중앙값 1.85, 95p 3.5, 99p 5.0 - 그래프에서도 EN이 KO보다 일관되게 길다 - 왜 중요하나 - 너무 긴 꼬리 샘플은 메모리/속도 문제 유발. - 길이비가 너무 크거나 작으면 잘못 매칭된 페어일 수 있어 학습을 불안정하게 함....

### 특수 패턴(숫자/퍼센트/화폐/URL/이메일)

무엇을 봤나 - 숫자: KO 1.76%, EN 6.04% - 나머지는 극소수 - 왜 중요하나 - 숫자/화폐/날짜는 번역 오류가 잦지만, 비율이 낮아 현재는 큰 위험 아님. - 액션 - 기본은 치환 없이 진행. - 숫자/단위가 중요한 도메인이라면 / 같은 치환 실험을 “추가 실험”으로.

## Implementation Flow

1. 🧩 미션 11: 한국어→영어 기계 번역 모델 구축 프로젝트: Seq2Seq · Attention 기반 NMT 모델 구현 & 성능 비교
2. 무결성/중복: 무엇을 봤나 - 빈 문장: 0% (OK) - 완전 중복 페어: 4.64% - 한-다/다-한 중복: KO 6.75%, EN 8.96% - 예시에 ‘>네.’, ‘>Yes.’ 같은 ‘>’ 표식 다수 - 왜 중요하나 - 완전 중복은 모델이 일부 문장에 과적합하고, 평가가 과대평가될 수 있음....
3. 길이 분포와 길이비: 무엇을 봤나 - KO 토큰 중앙값 6, 95p 14, 99p 18 - EN 토큰 중앙값 11, 95p 23, 99p 30 - 길이비 EN/KO 중앙값 1.85, 95p 3.5, 99p 5.0 - 그래프에서도 EN이 KO보다 일관되게 길다 - 왜 중요하나 - 너무 긴 꼬리 샘플은...
4. 특수 패턴(숫자/퍼센트/화폐/URL/이메일): 무엇을 봤나 - 숫자: KO 1.76%, EN 6.04% - 나머지는 극소수 - 왜 중요하나 - 숫자/화폐/날짜는 번역 오류가 잦지만, 비율이 낮아 현재는 큰 위험 아님. - 액션 - 기본은 치환 없이 진행. - 숫자/단위가 중요한 도메인이라면 / 같은...

## Code Highlights

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

`Seq2Seq + Attention`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 여기 tie_weights=False 로 변경, sanity overfit(선택), full train 흐름이 주석과 함께 드러납니다.

```python
src_vocab = sp_ko.vocab_size()
tgt_vocab = sp_en.vocab_size()

enc2 = EncoderAttn(src_vocab, emb=512, hid=512, bi=True, drop=0.2)
enc_out_dim = 512 * 2
# 여기 tie_weights=False 로 변경
dec2 = DecoderAttn(tgt_vocab, enc_dim=enc_out_dim, hid=512, emb=512, drop=0.2, attn_dim=256, tie_weights=False)
model_attn = Seq2SeqAttn(enc2, dec2).to(device)

opt2 = torch.optim.Adam(model_attn.parameters(), lr=3e-4)
scaler2 = amp.GradScaler('cuda' if device.type == 'cuda' else 'cpu')

# sanity overfit(선택)
tiny_idx = torch.randperm(len(train_ds))[:1000].tolist()
tiny_loader = DataLoader(torch.utils.data.Subset(train_ds, tiny_idx),
                         batch_size=128, shuffle=True, collate_fn=collate_sp)
for e in range(2):
    loss = train_epoch_attn(model_attn, tiny_loader, opt2, scaler2, tf_ratio=0.7)
    print(f"[tiny-attn] epoch {e + 1} | loss {loss:.3f}")

# full train
EPOCHS = 20
tf_start, tf_end = 0.7, 0.3
best_bleu, best_state = -1, None

for epoch in range(1, EPOCHS + 1):
    tf_ratio = tf_end + (tf_start - tf_end) * max(0, (EPOCHS - epoch) / (EPOCHS - 1))
    t0 = time.time()
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
