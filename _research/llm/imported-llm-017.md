---
title: "허깅페이스"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)허깅페이스"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)허깅페이스.md"
excerpt: "허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매우 널리 사용되는 오픈소스 라이브러리와 커뮤니티를 제공하는 플랫폼으로, 모델 공유 HUB, 데이터셋 공유 HUB, 라이브러리(Transformers, Datasets 등)를 통해 손쉽게 NLP 모델들을 학습, 배포하고 활용할 수..."
research_summary: "허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매우 널리 사용되는 오픈소스 라이브러리와 커뮤니티를 제공하는 플랫폼으로, 모델 공유 HUB, 데이터셋 공유 HUB, 라이브러리(Transformers, Datasets 등)를 통해 손쉽게 NLP 모델들을 학습, 배포하고 활용할 수 있도록 돕습니다. 허깅페이스 라이브러리. 허깅페이스 사이트에는 허브에 업로드된 Model, Dataset 등을 확인 할수 있으며, 활용을 위한 문서와 각종 커뮤니티가 공유되어 있습니다. `md` 원본과 33개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, torch입니다."
research_artifacts: "md · 코드 33개 · 실행 14개"
code_block_count: 33
execution_block_count: 14
research_focus:
  - "허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매우 널리 사용되는 오픈소스 라이브..."
  - "허깅페이스를 활용한 BERT/GPT 모델 사용"
  - "허깅페이스 사이트에는 허브에 업로드된 Model, Dataset 등을 확인 할수 있으며, 활용을 위한..."
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

허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매우 널리 사용되는 오픈소스 라이브러리와 커뮤니티를 제공하는 플랫폼으로, 모델 공유 HUB, 데이터셋 공유 HUB, 라이브러리(Transformers, Datasets 등)를 통해 손쉽게 NLP 모델들을 학습, 배포하고 활용할 수 있도록 돕습니다. 허깅페이스 라이브러리. 허깅페이스 사이트에는 허브에 업로드된 Model, Dataset 등을 확인 할수 있으며, 활용을 위한 문서와 각종 커뮤니티가 공유되어 있습니다. `md` 원본과 33개 코드 블록, 14개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 huggingface_hub, transformers, torch입니다.

**빠르게 볼 수 있는 포인트**: 허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매..., 허깅페이스를 활용한 BERT/GPT 모델 사용, 허깅페이스 사이트에는 허브에 업로드된 Model, Dataset 등을....

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

### 허깅페이스를 활용한 BERT/GPT 모델 사용 > 허깅페이스 살펴보기

허깅페이스 사이트에는 허브에 업로드된 Model, Dataset 등을 확인 할수 있으며, 활용을 위한 문서와 각종 커뮤니티가 공유되어 있습니다.

### 허깅페이스 살펴보기 > 허깅페이스 토큰 생성

허깅페이스의 특정 모델은 라이센스로인해 인증 과정이 필요할 수 있습니다. 따라서 먼저 허깅페이스에 회원가입을 하고 프로필 정보에서 Access Tokens 메뉴에 접속하여 새로운 토큰을 생성합니다.

### 허깅페이스 살펴보기 > 허깅페이스의 모델 객체

허깅페이스는 모델의 아키텍처에 따라 통일된 모델 객체를 만들어 놓고 허브에 올라온 모델 이름을 통해 쉽게 학습된 모델을 가져 올 수 있습니다. AutoModel: 주로 BERT 계열처럼 마스킹 기반 모델(Encoder)을 불러올 때 사용하는 객체

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

1. 허깅페이스를 활용한 BERT/GPT 모델 사용: 허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매우 널리 사용되는 오픈소스 라이브러리와 커뮤니티를 제공하는 플랫폼으로, 모델 공유 HUB, 데이터셋 공유 HUB, 라이브러리(Transformers, Datasets 등)를 통해 손...
2. 허깅페이스를 활용한 BERT/GPT 모델 사용 > 허깅페이스 살펴보기: 허깅페이스 사이트에는 허브에 업로드된 Model, Dataset 등을 확인 할수 있으며, 활용을 위한 문서와 각종 커뮤니티가 공유되어 있습니다.
3. 허깅페이스 살펴보기 > 허깅페이스 토큰 생성: 허깅페이스의 특정 모델은 라이센스로인해 인증 과정이 필요할 수 있습니다. 따라서 먼저 허깅페이스에 회원가입을 하고 프로필 정보에서 Access Tokens 메뉴에 접속하여 새로운 토큰을 생성합니다.
4. 허깅페이스 살펴보기 > 허깅페이스의 모델 객체: 허깅페이스는 모델의 아키텍처에 따라 통일된 모델 객체를 만들어 놓고 허브에 올라온 모델 이름을 통해 쉽게 학습된 모델을 가져 올 수 있습니다. AutoModel: 주로 BERT 계열처럼 마스킹 기반 모델(Encoder)을 불러올 때 사용하는 객체

## Code Highlights

### 기계번역 해보기

`기계번역 해보기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 타겟 언어 설정, 모델 입력 및 출력: 번역 결과 생성하기, input_ids: 번역할 문장의 토큰 ID 흐름이 주석과 함께 드러납니다.

```python
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 타겟 언어 설정
tar_lang = tokenizer.convert_tokens_to_ids("eng_Latn")
print(tar_lang)

# 모델 입력 및 출력: 번역 결과 생성하기
# - input_ids: 번역할 문장의 토큰 ID
# - forced_bos_token_id: 출력 언어 지정(여기서는 영어: "eng_Latn")
# - early_stopping=True: 문장의 끝(EOS)이 나오면 즉시 생성 중단
generated_tokens = model.generate(input_ids.to(device),
                                  forced_bos_token_id=tar_lang,     # 영어로 번역
                                  early_stopping=True               # 끝토큰(eos)이 나오면 중단
                                  )
print(f'출력 토큰: {generated_tokens}')

generated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=False)
print(f'생성 텍스트: {generated_text}')
```

### 텍스트 생성하기

`텍스트 생성하기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 텍스트 생성, 입력 토큰과 어텐션 마스크를 나누어 입력, 생성된 토큰을 사람이 읽을 수 있는 문장으로 디코딩 흐름이 주석과 함께 드러납니다.

```python
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

input_tensor = tokens['input_ids'].to(device)
attention_mask = tokens['attention_mask'].to(device)

# 텍스트 생성
with torch.no_grad():                   # 생성 단계에서는 그래디언트 계산 비활성화 (속도 ↑, 메모리 ↓)
    # 입력 토큰과 어텐션 마스크를 나누어 입력
    outputs = model.generate(
        input_tensor,                   # 입력 토큰
        attention_mask=attention_mask,  # 어텐션 마스크: 패딩 토큰은 무시하도록 하는 마스
        max_length=128,                 # 생성할 최대 토큰(단어) 길이 제한
        no_repeat_ngram_size=2,         # 2단어 연속 중복 생성을 억제
        early_stopping=True             # 문장 끝(EOS) 토큰 나오면 즉시 멈추기
    )

# 생성된 토큰을 사람이 읽을 수 있는 문장으로 디코딩
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
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
