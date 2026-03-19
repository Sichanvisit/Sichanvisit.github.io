---
title: "GPT 사전학습"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)GPT_사전학습"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)GPT_사전학습.md"
excerpt: "GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다."
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
| Code Blocks | 13 |
| Execution Cells | 13 |
| Libraries | `google`, `torch`, `sentencepiece`, `pandas`, `numpy`, `os`, `math`, `matplotlib` |
| Source Note | `3-3 (실습)GPT_사전학습` |

## What I Worked On

- GPT
- GPT 학습을 위한 데이터세트 구성
- Autoregressive 학습을 위한 데이터세트
- BPE :바이트 페어 인코딩(Byte Pair Encoding, BPE)
- 추가 쓰기모드로 텍스트 파일 열기

## Implementation Flow

1. GPT
2. GPT 학습을 위한 데이터세트 구성
3. Autoregressive 학습을 위한 데이터세트
4. BPE :바이트 페어 인코딩(Byte Pair Encoding, BPE)
5. 추가 쓰기모드로 텍스트 파일 열기
6. 저장 경로 생성

## Code Highlights

### Autoregressive 학습을 위한 데이터세트

```python
class SPDataSet(Dataset):
    def __init__(self, sp, max_len):
        self.max_len = max_len
        self.df = pd.read_csv(f'./train.csv')[['HS01','SS01']]
        self.sp = sp

    def zero_pad(self, tok):
        if len(tok) >= self.max_len:
            return tok[:self.max_len]
        else:
            padding = np.zeros(self.max_len)
            padding[:len(tok)] = tok
            return padding

    def __len__(self):
        return (len(self.df))

    def __getitem__(self, i):
        sent = self.df.iloc[i]
        sent1 = self.sp.encode_as_ids(sent['HS01'])
        sent2 = self.sp.encode_as_ids(sent['SS01'])

        # 문장 구분을 위해 bos 토큰과 eos 토큰 추가
        inp = sent1 + [self.sp.bos_id()] + sent2 + [self.sp.eos_id()]

        # 문장이 끝나면 제로 패딩
        input_ids = self.zero_pad(inp)

# ... trimmed ...
```

### 모델 학습하기

```python
# 손실 계산시 형상 변환
def loss_function(tar, pred, pad_token=0):
    # pred shape: (batch_size, seq_len, vocab_size)
    # tar shape: (batch_size, seq_len)
    # pred shape to (batch_size * seq_len, vocab_size)
    pred_reshaped = pred.view(-1, pred.size(-1))
    tar_reshaped = tar.reshape(-1)
    return loss_fn(pred_reshaped, tar_reshaped)

train_loss = []
val_loss = []
for epoch in range(num_epochs):
    model.train()
    total_loss = 0.0
    for step, (input_ids, tar_ids, mask) in enumerate(train_loader):
        input_ids = input_ids.long().to(device)
        tar_ids = tar_ids.long().to(device)
        key_padding_mask = mask.to(device)

        outputs = model(input_ids, key_padding_mask=key_padding_mask)

        loss = loss_function(tar_ids, outputs)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-3 (실습)GPT_사전학습.md`
- Source formats: `md`
- Companion files: `3-3 (실습)GPT_사전학습.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `HS01'',''SS01`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `www.aihub.or.kr`, `localhost`, `drive.google.com`

## Note Preview

> GPT 모델 또한 일반적으로 사전학습과 미세조정 두가지의 학습 단계가 존재합니다.
> - **사전 학습** * 웹 텍스트나 책, 논문, 뉴스 등 다양한 출처의 방대한 텍스트 데이터를 활용하여 사전학습을 진행 * 특수한 라벨이나 태그가 달려 있지 않으며, 자연어 형태(대체로 가공되지 않은(unlabeled) 텍스트 형태)로 학습 * 욕설・중복 등 품질이 매우 낮은 텍스트를 걸러내는 등의 기본적인 전처리(cleaning) 작업만 진행
