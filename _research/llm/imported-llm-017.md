---
title: "허깅페이스"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)허깅페이스"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)허깅페이스.md"
excerpt: "허깅페이스를 활용한 BERT/GPT... 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 허깅페이스를 활용한 BERT/GPT... 순서로 핵심 장면을 먼저 훑고, AutoModel 모델 로드, 토큰화, 문장 임베딩 출력 같은 코드..."
research_summary: "허깅페이스를 활용한 BERT/GPT... 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 허깅페이스를 활용한 BERT/GPT... 순서로 핵심 장면을 먼저 훑고, AutoModel 모델 로드, 토큰화, 문장 임베딩 출력 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 33개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, torch입니다."
research_artifacts: "md · 코드 33개 · 실행 14개"
code_block_count: 33
execution_block_count: 14
research_focus:
  - "허깅페이스를 활용한 BERT/GPT 모델 사용"
research_stack:
  - "huggingface_hub"
  - "transformers"
  - "torch"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

허깅페이스를 활용한 BERT/GPT... 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 허깅페이스를 활용한 BERT/GPT... 순서로 핵심 장면을 먼저 훑고, AutoModel 모델 로드, 토큰화, 문장 임베딩 출력 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 33개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, torch입니다.

**빠르게 볼 수 있는 포인트**: 허깅페이스를 활용한 BERT/GPT 모델 사용.

**남겨둔 자료**: `md` 원본과 33개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, torch입니다.

**주요 스택**: `huggingface_hub`, `transformers`, `torch`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 33 |
| Execution Cells | 14 |
| Libraries | `huggingface_hub`, `transformers`, `torch` |
| Source Note | `3-3 (실습)허깅페이스` |

## What This Note Covers

### 허깅페이스를 활용한 BERT/GPT 모델 사용

허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매우 널리 사용되는 오픈소스 라이브러리와 커뮤니티를 제공하는 플랫폼으로, 모델 공유 HUB, 데이터셋 공유 HUB, 라이브러리(Transformers, Datasets 등)를 통해 손쉽게 NLP 모델들을 학습, 배포하고 활용할 수 있도록 돕습니다. 허깅페이스 라이브러리

- 읽을 포인트: 세부 흐름: GPT 형식 모델 > AutoModelForCausalLM 모델 로드, BERT 형식 모델 > AutoModel 모델 로드, BERT 형식 모델 > 감성 분류가 적용된 BERT

#### GPT 형식 모델 > AutoModelForCausalLM 모델 로드

디코더만 사용하여 캐주얼 마스크를 통해 자기회귀방식으로 텍스트를 생성하는 모델은 AutoModelForCausalLM 객체를 사용하여 로드해 줍니다. 위의 Llama 모델 요약 구조

#### BERT 형식 모델 > AutoModel 모델 로드

BERT 형식 모델은 AutoModel에서 from_pretrained() 함수에 모델 이름을 입력하여 쉽게 학습된 모델을 불러올 수 있습니다. BERT 모델을 허브에서 찾기 위해서 주로 Fill Mask테스크를 찾아봅니다.

#### BERT 형식 모델 > 감성 분류가 적용된 BERT

분류 작업이 추가된 BERT 모델은 AutoModelForSequenceClassification 객체를 활용하여 불러 올 수 있습니다. tabularisai/multilingual-sentiment-analysis

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

1. 허깅페이스를 활용한 BERT/GPT 모델 사용: GPT 형식 모델 > AutoModelForCausalLM 모델 로드, BERT 형식 모델 > AutoModel 모델 로드

## Code Highlights

### AutoModel 모델 로드

`AutoModel 모델 로드`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 예시에서는 다국어 지원이 되는 bert-base-multilingual-cased 모델을 활용하여 BERT 모델이 만든 임베딩값을 살펴봅니다.

```python
from transformers import AutoTokenizer, AutoModel
import torch

model_name = "google-bert/bert-base-multilingual-cased"

model = AutoModel.from_pretrained(model_name, device_map="auto")
print(model)
```

### 토큰화

`토큰화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 토크나이저, 토큰화 흐름이 주석과 함께 드러납니다.

```python
model_name = "google-bert/bert-base-multilingual-cased"

# 토크나이저
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 토큰화
sentence = "오늘 수업은 자연어 분석 수업인가?"
inputs = tokenizer(sentence, text_pair='아니 오늘 수업은 자연어 분석 수업이 아니다', return_tensors="pt")
inputs
```

### 문장 임베딩 출력

`문장 임베딩 출력`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 토크나이저 → 딕셔너리 3개, {'input_ids': ..., 'token_type_ids': ..., 'attent..., = 딕셔너리 펼치기 흐름이 주석과 함께 드러납니다.

```text
# 1. 토크나이저 → 딕셔너리 3개
inputs = tokenizer(text, return_tensors="pt")
# {'input_ids': ..., 'token_type_ids': ..., 'attention_mask': ...}

# 2. ** = 딕셔너리 펼치기
outputs = model(**inputs)

**inputs
= input_ids=..., token_type_ids=..., attention_mask=...
```

### 감성 분류가 적용된 BERT

`감성 분류가 적용된 BERT`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 위의 DistilBERT 모델 구조.

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def predition_sentiment(texts):
    inputs = tokenizer( texts,
                        return_tensors="pt",    # PyTorch 텐서로
                        truncation=True,        # 512자 넘으면 자르기
                        padding = True,         # 짧으면 패딩 추가
                        max_length=512          # 최대 512 토큰
                    )
    with torch.no_grad():                                               # 학습 안 함 (속도↑)
        outputs = model(**inputs.to(device))

    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1) # 가장 높은 인덱스
    sentiment_map = {0: "Very Negative",
                     1: "Negative",
                     2: "Neutral",
                     3: "Positive",
                     4: "Very Positive"
                     }
    return [sentiment_map[p] for p in torch.argmax(probabilities, dim=-1).tolist()]

texts =['하, 오늘 수업은 너무 어렵고 힘들었다.',
        '오, 오늘 수업은 너무 재미있고 유익했다!']

for text, sentiment in zip(texts, predition_sentiment(texts)):
    print(f"Text: {text}\nSentiment: {sentiment}\n")
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-3 (실습)허깅페이스.md`
- Source formats: `md`
- Companion files: `3-3 (실습)허깅페이스.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `huggingface.co`, `medium.com`, `localhost`, `miro.medium.com`, `drive.google.com`

## Note Preview

> 허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매우 널리 사용되는 오픈소스 라이브러리와 커뮤니티를 제공하는 플랫폼으로, 모델 공유 HUB, 데이터셋 공유 HUB, 라이브러리(Transformers, Datasets 등)를 통해 손쉽게 NLP 모델들을 학습, 배포하고 활용할 수 있도록 돕습니다.
> - **허깅페이스 라이브러리**
