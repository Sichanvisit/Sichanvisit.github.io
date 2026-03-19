---
title: "Attention 1"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 (실습)Attention_1"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 (실습)Attention_1.md"
excerpt: "Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가"
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
| Code Blocks | 14 |
| Execution Cells | 12 |
| Libraries | `torch`, `google`, `pandas`, `numpy`, `sentencepiece`, `os`, `math` |
| Source Note | `3-2 (실습)Attention_1` |

## What I Worked On

- 1. 감정 분류을 위한 Attention 순환 신경망: BiLSTM + Attention
- 단계:
- 모델링
- 모델 생성
- 모델 학습

## Implementation Flow

1. 1. 감정 분류을 위한 Attention 순환 신경망: BiLSTM + Attention
2. 단계:
3. 모델링
4. 모델 생성
5. 모델 학습
6. 파일 업로드 창 열기

## Code Highlights

### 모델 학습(train) + 평가(validation) 단계

```python
criterion = nn.CrossEntropyLoss() # 다중 클래스 분류
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

history = {'train_loss': [],
           'val_loss': [],
           'val_acc': []
           }

for epoch in range(num_epochs):
  model.train() # 모델을 학습모드로 설정
  total_loss = 0.0

  for input, labels in train_loader:
    # 입력데이터 준비
    input_ids = input.long().to(device) # [batch_size, seq_len]
    labels = labels.to(device)
    # 순전파
    outputs = model(input_ids)          # [batch_size, num_calsses]
    loss = criterion(outputs, labels)   # 손실 계산

    # 역전파 및 옵티마아지 업데이트
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    total_loss += loss.item()

  avg_loss = total_loss / len(train_loader)
# ... trimmed ...
```

### 디코더 구성

```python
from torch.utils.data import Dataset, DataLoader, random_split
import sentencepiece as spm
import numpy as np

class SPDataSet(Dataset):
    def __init__(self, sp, max_len):
        self.max_len = max_len
        self.df = pd.read_csv(f'train.csv')[['HS01','SS01']]
        self.sp = sp

    # 제로 패딩
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

        # 질의는 단어 토큰만 활용
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-2 (실습)Attention_1.md`
- Source formats: `md`
- Companion files: `3-2 (실습)Attention_1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `label'',''HS01`, `HS01'', ''SS01`, `HS01'',''SS01`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `www.aihub.or.kr`, `drive.google.com`, `localhost`

## Note Preview

> Attention
> Embedding + BiLSTM 모델과 추가로 Seq2seq을 구성하여 Attention 층을 추가
