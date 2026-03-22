---
title: "1 미세조정 Freezing"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-4 (실습)1_미세조정_Freezing"
source_path: "13_LLM_GenAI/Code_Snippets/3-4 (실습)1_미세조정_Freezing.md"
excerpt: "1 미세조정 Freezing에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 감성 분류를 위한 BERT 미세조정, LLM 파인튜닝 방법 선택 기준 요약표 순서로 핵심 장면을 먼저 훑고, 토크나이져 로드, Dataset 만들기, TrainingArgu..."
research_summary: "1 미세조정 Freezing에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 감성 분류를 위한 BERT 미세조정, LLM 파인튜닝 방법 선택 기준 요약표 순서로 핵심 장면을 먼저 훑고, 토크나이져 로드, Dataset 만들기, TrainingArguments 하이퍼... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 11개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, sentencepiece, pandas입니다."
research_artifacts: "md · 코드 11개 · 실행 11개"
code_block_count: 11
execution_block_count: 11
research_focus:
  - "감성 분류를 위한 BERT 미세조정"
  - "LLM 파인튜닝 방법 선택 기준 요약표"
research_stack:
  - "google"
  - "torch"
  - "sentencepiece"
  - "pandas"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

1 미세조정 Freezing에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 감성 분류를 위한 BERT 미세조정, LLM 파인튜닝 방법 선택 기준 요약표 순서로 핵심 장면을 먼저 훑고, 토크나이져 로드, Dataset 만들기, TrainingArguments 하이퍼... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 11개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, sentencepiece, pandas입니다.

**빠르게 볼 수 있는 포인트**: 감성 분류를 위한 BERT 미세조정, LLM 파인튜닝 방법 선택 기준 요약표.

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 11개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 google, torch, sentencepiece, pandas입니다.

**주요 스택**: `google`, `torch`, `sentencepiece`, `pandas`, `numpy`

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

## What This Note Covers

### 감성 분류를 위한 BERT 미세조정

허깅페이스의 사전학습만 진행된 다국어 BERT 모델(bert-base-multilingual-cased)을 활용하여 감성분류를 위한 미세조정 테스크를 만들어 봅니다.

- 읽을 포인트: 세부 흐름: 데이터세트 구성 > 토크나이져 로드, 전체 파인튜닝을 통한 분류 학습 > Trainer 모델 학습, 프리징 하여 미세조정 > 프리징된 모델 학습

#### 데이터세트 구성 > 토크나이져 로드

허깅페이스를 활용하여 bert-base-multilingual-cased 모델을 로드할것 이므로 이에 맞는 토크나이져를 AutoTokenizer 객체를 통해 로드해 줍니다.

#### 전체 파인튜닝을 통한 분류 학습 > Trainer 모델 학습

허깅페이스는 학습 로직을 직접 구현할 필요없이 TrainingArguments로 만든 하이퍼파라미터를 적용한 학습을 수행하는 Trainer 객체를 제공합니다. 간단하게 Trainer 생성자에 모델과, TrainingArguments, 데이터세트를 입력하여 인스턴스를 만들고 trai...

#### 프리징 하여 미세조정 > 프리징된 모델 학습

학습은 동일하게 Trainer, TrainingArguments를 통해 학습 가능합니다. 총 학습 시간이 BERT를 전체 미세조정한것에 비해 적게 걸린것을 확인할 수 있습니다.

### LLM 파인튜닝 방법 선택 기준 요약표

요약 - 데이터가 많고, 성능이 최우선 → Full Fine-tuning - 성능·속도·안정성 골고루 → Partial Freeze Fine-tuning - 적은 GPU로 고성능 확보 → LoRA - 진짜 저렴하게 하고 싶다 → QLoRA

- 읽을 포인트: LLM 파인튜닝 방법 선택 기준 요약표에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

## Implementation Flow

1. 감성 분류를 위한 BERT 미세조정: 데이터세트 구성 > 토크나이져 로드, 전체 파인튜닝을 통한 분류 학습 > Trainer 모델 학습
2. LLM 파인튜닝 방법 선택 기준 요약표: 요약 - 데이터가 많고, 성능이 최우선 → Full Fine-tuning - 성능·속도·안정성 골고루 → Partial Freeze Fine-tuning - 적은 GPU로 고성능 확보 → LoRA - 진짜 저렴하게 하고 싶...

## Code Highlights

### 토크나이져 로드

`토크나이져 로드`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 토크나이저 로드 흐름이 주석과 함께 드러납니다.

```python
from transformers import AutoTokenizer

model_name = "google-bert/bert-base-multilingual-cased"

# 토크나이저 로드
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer('점심 시간이 30분이 남았습니다')
```

### Dataset 만들기

`Dataset 만들기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 라벨 인코딩, AutoTokenizer를 활용하여 입력 id, 패딩 마스크 생성 흐름이 주석과 함께 드러납니다.

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

### TrainingArguments 하이퍼파라미터 설정

`TrainingArguments 하이퍼파라미터 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 파라미터 설정 흐름이 주석과 함께 드러납니다.

```python
from transformers import TrainingArguments


# 학습 파라미터 설정
training_args = TrainingArguments(
    output_dir="./results",                 # 모델 저장 경로
    eval_strategy="steps",                  # 평가 전략 ("no", "steps", "epoch")
    eval_steps=200,                         # steps 평가 간격 (에포크인 경우는 1에폭마다 평가)
    num_train_epochs=5,                     # 에포크 수
    optim="adamw_torch",                    # 옵티마이져
    learning_rate=2e-5,                     # 학습률
    weight_decay=2e-5,                      # 가중치 감쇠
    per_device_train_batch_size=64,         # 학습 배치 크기
    per_device_eval_batch_size=64,          # 평가 배치 크기
    logging_steps=200,                      # 로그 출력 간격
    save_strategy = "steps",                # 모델 저장 전략 ("no", "steps", "epoch", "best")
    save_steps=1000,                        # 저장 간격
    save_total_limit=2,                     # 최대 저장수 (가장 좋은 모델만 남김)
    load_best_model_at_end=True,            # 학습 후 가장 평가가 좋은 모델 로드
    push_to_hub=False,                      # 모델을 허깅페이스 허브에 푸시 X
    report_to="none",                       # wandb 사용 X
)

dataset = SPDataSet(sent_df, tokenizer, 60)
generator1 = torch.Generator().manual_seed(42)
test_dataset, train_dataset = random_split(dataset, [0.2, 0.8], generator=generator1)
print(len(test_dataset), len(train_dataset))
```

### 프리징된 모델 학습

`프리징된 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 학습 파라미터 설정, 학습 시작 흐름이 주석과 함께 드러납니다.

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
