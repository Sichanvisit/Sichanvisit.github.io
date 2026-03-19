---
title: "허깅페이스"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-3 (실습)허깅페이스"
source_path: "13_LLM_GenAI/Code_Snippets/3-3 (실습)허깅페이스.md"
excerpt: "허깅페이스(Hugging Face)는 자연어 처리(NLP) 분야에서 매우 널리 사용되는 오픈소스 라이브러리와 커뮤니티를 제공하는 플랫폼으로, 모델 공유 HUB, 데이터셋 공유 HUB, 라이브러리(Transformers, Datasets 등)를 통해 손쉽게 NLP..."
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
| Code Blocks | 33 |
| Execution Cells | 14 |
| Libraries | `huggingface_hub`, `transformers`, `torch` |
| Source Note | `3-3 (실습)허깅페이스` |

## What I Worked On

- 허깅페이스를 활용한 BERT/GPT 모델 사용
- 허깅페이스 살펴보기
- 허깅페이스 토큰 생성
- 주피터 환경에서 허깅페이스 인증하기
- 허깅페이스의 모델 객체

## Implementation Flow

1. 허깅페이스를 활용한 BERT/GPT 모델 사용
2. 허깅페이스 살펴보기
3. 허깅페이스 토큰 생성
4. 주피터 환경에서 허깅페이스 인증하기
5. 허깅페이스의 모델 객체
6. Transformer 형식 모델

## Code Highlights

### 텍스트 생성하기

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
