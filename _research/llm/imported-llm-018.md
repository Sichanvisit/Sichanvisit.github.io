---
title: "1 미세조정 Freezing"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-4 (실습)1_미세조정_Freezing"
source_path: "13_LLM_GenAI/Code_Snippets/3-4 (실습)1_미세조정_Freezing.md"
excerpt: "허깅페이스의 사전학습만 진행된 다국어 BERT 모델(bert-base-multilingual-cased)을 활용하여 감성분류를 위한 미세조정 테스크를 만들어 봅니다."
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
| Code Blocks | 11 |
| Execution Cells | 11 |
| Libraries | `google`, `torch`, `sentencepiece`, `pandas`, `numpy`, `transformers`, `evaluate` |
| Source Note | `3-4 (실습)1_미세조정_Freezing` |

## What I Worked On

- 감성 분류를 위한 BERT 미세조정
- 데이터세트 구성
- 토크나이져 로드
- 토크나이저 로드
- Dataset 만들기

## Implementation Flow

1. 감성 분류를 위한 BERT 미세조정
2. 데이터세트 구성
3. 토크나이져 로드
4. 토크나이저 로드
5. Dataset 만들기
6. 전체 파인튜닝을 통한 분류 학습

## Code Highlights

### Dataset 만들기

```python
class SPDataSet(Dataset):
    def __init__(self, df, tokenizer, max_len):
        self.max_len = max_len
        self.df = df
        self.tokenizer = tokenizer
        self.class_name = {'E1':0, 'E6':1, 'E3':2, 'E5':3, 'E2':4, 'E4':5}

    def __getitem__(self, i):
        inp = str(self.df.iloc[i]['text'])
        tar = self.df.iloc[i]['label']
        # 라벨 인코딩
        tar = self.class_name[tar]

        # AutoTokenizer를 활용하여 입력 id, 패딩 마스크 생성
        encoding = self.tokenizer(
            inp,
            truncation=True,          # max_length 보다 길면 자르기
            padding="max_length",     # max_length 만큼 패딩
            max_length=self.max_len,  # max_length 설정
            return_tensors="pt"
        )

        item = {
            "input_ids": encoding["input_ids"].squeeze(),           # 입력 토큰
            "attention_mask": encoding["attention_mask"].squeeze(), # 어텐션 토큰
            "labels": torch.tensor(tar, dtype=torch.long)           # 분류 라벨
        }
        return item
# ... trimmed ...
```

### 프리징된 모델 학습

```python
from transformers import Trainer, TrainingArguments
import evaluate

# 학습 파라미터 설정
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="steps",
    eval_steps=200,
    num_train_epochs=20,
    optim="adamw_torch",
    learning_rate=2e-5,
    weight_decay=1e-5,
    per_device_train_batch_size=64,
    per_device_eval_batch_size=64,
    logging_steps=200,
    save_steps=1000,
    save_total_limit=2,
    load_best_model_at_end=True,
    push_to_hub=False,
    report_to="none"
)

dataset = SPDataSet(sent_df, tokenizer, 60)
generator1 = torch.Generator().manual_seed(42)
test_dataset, train_dataset = random_split(dataset, [0.2, 0.8], generator=generator1)

metric = evaluate.load("accuracy")
def compute_metrics(eval_pred):
# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-4 (실습)1_미세조정_Freezing.md`
- Source formats: `md`
- Companion files: `3-4 (실습)1_미세조정_Freezing.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `label'',''HS01`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `www.aihub.or.kr`, `aiota.notion.site`, `localhost`

## Note Preview

> 허깅페이스의 사전학습만 진행된 다국어 BERT 모델(bert-base-multilingual-cased)을 활용하여 감성분류를 위한 미세조정 테스크를 만들어 봅니다.
> 먼저 감정분류를 위한 데이터세트를 구성합니다. 미세조정도 사전학습과 동일하게 토큰화가 진행되어야 하고, 테스크에 맞게 입력과 라벨을 구성하여 만들어 줍니다.
