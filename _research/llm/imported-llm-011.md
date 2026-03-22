---
title: "11 Seq2Seq 예시1"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-2 11_Seq2Seq_예시1"
source_path: "13_LLM_GenAI/Code_Snippets/3-2 11_Seq2Seq_예시1.md"
excerpt: "11 Seq2Seq 예시1에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 모델 로딩, ✔ 데이터 설명, 모델 구성 순서로 핵심 장면을 먼저 훑고, 데이터 재구성, 데이터 불러오기, SentencePiece 같은 코드로 실제 구현을 이어서 확인할 수..."
research_summary: "11 Seq2Seq 예시1에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 모델 로딩, ✔ 데이터 설명, 모델 구성 순서로 핵심 장면을 먼저 훑고, 데이터 재구성, 데이터 불러오기, SentencePiece 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 36개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 json, os, random, re입니다."
research_artifacts: "md · 코드 36개 · 실행 13개"
code_block_count: 36
execution_block_count: 13
research_focus:
  - "모델 로딩"
  - "✔ 데이터 설명"
  - "모델 구성"
research_stack:
  - "json"
  - "os"
  - "random"
  - "re"
  - "sys"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

11 Seq2Seq 예시1에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 모델 로딩, ✔ 데이터 설명, 모델 구성 순서로 핵심 장면을 먼저 훑고, 데이터 재구성, 데이터 불러오기, SentencePiece 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 36개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 json, os, random, re입니다.

**빠르게 볼 수 있는 포인트**: 모델 로딩, ✔ 데이터 설명, 모델 구성.

**남겨둔 자료**: `md` 원본과 36개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 json, os, random, re입니다.

**주요 스택**: `json`, `os`, `random`, `re`, `sys`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 36 |
| Execution Cells | 13 |
| Libraries | `json`, `os`, `random`, `re`, `sys`, `urllib`, `warnings`, `zipfile` |
| Source Note | `3-2 11_Seq2Seq_예시1` |

## What This Note Covers

### 모델 로딩

best_model_path = os.path.join(model_dir, "Seq2Seq_best_model.pt") model.load_state_dict(torch.load(best_model_path, map_location=device)) model.eval() print(f"모델 로드 완료: {best_model_path}...

- 읽을 포인트: 임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다.

### ✔ 데이터 설명

목적 본 실습의 목적은 한국어 문장을 영어로 번역하는 기계번역 모델을 구현하고 성능을 비교하는 것이다. 이를 위해 전통적인 Seq2Seq 모델, Attention 기법을 적용한 모델을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을 정량적(BLEU 점수) 및 정성적으로(번역 분석) 평가할 것이다. 데이터셋 사용한 데이터는...

- 읽을 포인트: ✔ 데이터 설명에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### 모델 구성

encoder = Encoder(input_vocab_size, embed_size, hidden_size, dropout_p).to(device) decoder = Decoder(output_vocab_size, embed_size, hidden_size, dropout_p).to(device) model = Seq2Seq(enco...

- 읽을 포인트: 임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다.

### ✔ 요약

본 실습에서는 한영 말뭉치 데이터셋을 기반으로 Sequence-to-Sequence 모델을 구축하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄링 등을 적용하였지만, 문장 예측 품질(BLEU)은 0.1217로 낮았다. 이에...

- 읽을 포인트: ✔ 요약에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### 모댈 저장 경로

model_dir = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/model" os.makedirs(model_dir, exist_ok=True)

- 읽을 포인트: 모댈 저장 경로에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### 저장 경로

model_dir = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/model" os.makedirs(model_dir, exist_ok=True)

- 읽을 포인트: 저장 경로에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

## Why This Matters

### 순차 데이터 모델링

- 왜 필요한가: 문장, 시계열처럼 순서가 중요한 데이터는 현재 입력만이 아니라 앞선 맥락까지 함께 봐야 합니다.
- 왜 이 방식을 쓰는가: LSTM/GRU는 기본 RNN보다 긴 문맥을 더 안정적으로 다룰 수 있어 텍스트 분류나 시계열 예측 실습에 자주 쓰입니다.
- 원리: 이전 시점의 은닉 상태를 다음 입력과 함께 업데이트하며, 게이트 구조로 필요한 정보는 남기고 불필요한 정보는 줄입니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 전처리와 입력 정리

- 왜 필요한가: 원본 데이터는 결측치, 스케일 차이, 불필요한 기호처럼 학습을 방해하는 요소가 많아 바로 넣기 어렵습니다.
- 왜 이 방식을 쓰는가: 전처리는 모델 종류와 데이터 특성에 맞는 입력 형식을 먼저 맞춰주기 때문에, 단순해 보여도 성능 차이를 크게 만듭니다.
- 원리: 불필요한 정보를 줄이고 유효한 패턴을 남기도록 데이터를 정규화·정제·인코딩해 모델이 학습하기 쉬운 분포로 바꿉니다.

## Implementation Flow

1. 모델 로딩: best_model_path = os.path.join(model_dir, "Seq2Seq_best_model.pt") model.load_state_dict(torch.load(best_model_path, map_location=device)) m...
2. ✔ 데이터 설명: 목적 본 실습의 목적은 한국어 문장을 영어로 번역하는 기계번역 모델을 구현하고 성능을 비교하는 것이다. 이를 위해 전통적인 Seq2Seq 모델, Attention 기법을 적용한 모델을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을...
3. 모델 구성: encoder = Encoder(input_vocab_size, embed_size, hidden_size, dropout_p).to(device) decoder = Decoder(output_vocab_size, embed_size, hidden_s...
4. ✔ 요약: 본 실습에서는 한영 말뭉치 데이터셋을 기반으로 Sequence-to-Sequence 모델을 구축하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스...
5. 모댈 저장 경로: model_dir = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/model" os.makedirs(model_dir, exist_ok=True)
6. 저장 경로: model_dir = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/model" os.makedirs(model_dir, exist_ok=True)

## Code Highlights

### 데이터 재구성

`데이터 재구성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기존 데이터에서 일부만 사용, train_set.json을 train/val로 나누기, 새로운 파일로 저장 흐름이 주석과 함께 드러납니다.

```python
train_path = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/일상생활및구어체_한영_train_set.json"
valid_path = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/일상생활및구어체_한영_valid_set.json"
out_dir = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/"

with open(train_path, 'r', encoding='utf-8') as f:
    train_data = json.load(f)['data']

with open(valid_path, 'r', encoding='utf-8') as f:
    valid_data = json.load(f)['data']

# 기존 데이터에서 일부만 사용
random.seed(42)
train_sample = random.sample(train_data, 60000)
test_sample = random.sample(valid_data, 3000)

# train_set.json을 train/val로 나누기
val_ratio = 0.1
split_idx = int(len(train_sample) * (1 - val_ratio))
train_split = train_sample[:split_idx]
val_split = train_sample[split_idx:]

# 새로운 파일로 저장
with open(out_dir + "mini_train.json", "w", encoding="utf-8") as f:
    json.dump({"data": train_split}, f, ensure_ascii=False, indent=2)

with open(out_dir + "mini_val.json", "w", encoding="utf-8") as f:
    json.dump({"data": val_split}, f, ensure_ascii=False, indent=2)

# ... trimmed ...
```

### 데이터 불러오기

`데이터 불러오기`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 개수 출력, 샘플 3개 출력 흐름이 주석과 함께 드러납니다.

```python
base_path = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/"
train_path = base_path + "mini_train.json"
val_path   = base_path + "mini_val.json"
test_path  = base_path + "mini_test.json"

with open(train_path, 'r', encoding='utf-8') as f:
    mini_train = json.load(f)['data']

with open(val_path, 'r', encoding='utf-8') as f:
    mini_val = json.load(f)['data']

with open(test_path, 'r', encoding='utf-8') as f:
    mini_test = json.load(f)['data']

# 개수 출력
print(f"mini_train 개수: {len(mini_train)}개")
print(f"mini_val 개수: {len(mini_val)}개")
print(f"mini_test 개수: {len(mini_test)}개\n")

# 샘플 3개 출력
for i in range(3):
    print(f"[{i}] ko: {mini_train[i]['ko']}")
    print(f"    en: {mini_train[i]['en']}\n")
```

### SentencePiece

`SentencePiece`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 학습용 데이터를 SentencePiece 토크나이저 학습에 사용할 수 있도록, 한국어와 영어 문장을 각각 텍스트 파일로 저장하였다.

```python
spm_dir = "/content/drive/MyDrive/코드잇/스프린트 미션/data/미션 11/spm/"
os.makedirs(spm_dir, exist_ok=True)

ko_path = os.path.join(spm_dir, "ko_corpus.txt")
en_path = os.path.join(spm_dir, "en_corpus.txt")

if not os.path.exists(ko_path) or not os.path.exists(en_path):
    with open(ko_path, "w", encoding="utf-8") as f_ko, \
         open(en_path, "w", encoding="utf-8") as f_en:
        for item in mini_train:
            f_ko.write(item['ko'].strip() + "\n")
            f_en.write(item['en'].strip() + "\n")
    print("학습용 텍스트 파일 생성 완료")
else:
    print("학습용 텍스트 파일이 이미 존재합니다.")
```

### 모델 로딩

`모델 로딩`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 결과 확인 흐름이 주석과 함께 드러납니다.

```text
<!-- #region id="LJ-pCHkwCPaW" -->
처음 Seq2Seq 모델을 학습시켰을 때는 **과적합이 발생**했다. <br>
Train Loss는 계속 감소하는데 비해 Val Loss는 그대로였다.
<br>

|               | Epoch 1                              | Epoch 20                             |
|---------------|---------------------------------------|---------------------------------------|
| 수정 전        | Train Loss: 5.1847 \| Val Loss: 5.7774 | Train Loss: 2.6143 \| Val Loss: 5.6510 |

<br>

<!-- #endregion -->

<!-- #region id="KkFeeh9AD2rX" -->
이에 따라 과적합을 방지하기 위해 아래와 같은 과정을 거쳐 전반적으로 코드를 수정했다. <br>

| 항목              | 수정 전                 | 수정 후                             |
|-------------------|--------------------------|--------------------------------------|
| GRU               | 단방향                   | 양방향                               |
| 손실 함수         | CrossEntropyLoss         | Label Smoothing                      |
| Dropout           | 0.1                      | 0.2                                  |
| 정규화            | 없음                     | L2 정규화      |
| Teacher Forcing   | 0.6으로 고정             | 에폭이 증가할수록 점진적으로 감소   |


<br>
<!-- #endregion -->

...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-2 11_Seq2Seq_예시1.md`
- Source formats: `md`
- Companion files: `3-2 11_Seq2Seq_예시1.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `SOS_ID`, `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 본 실습에서는 한영 말뭉치 데이터셋을 기반으로 **Sequence-to-Sequence 모델을 구축**하였다. 이 과정에서 과적합을 개선하기 위해 GRU 양방향 구조, Label Smoothing, Dropout, L2 정규화, Teacher Forcing 스케줄링 등을 적용하였지만, **문장 예측 품질(BLEU)은 0.1217**로 낮았다. 이에 따라 **Bahdanau Attention을 추가**한 모델을 설계하였고, 문맥 정보를 효과적으로 반영하여 번역 품질이 향상되었다. **BLEU 점수도 0.1217 → 0.2381**으로 개선되었다. 이번 실습을 통해 Attention 메커니즘의 중요성을 확인할 수 있었다. 다만 시간 제약으로 인해 Transformer 모델까지 실험하지 못한 점은 아쉬움으로 남는다. 향후에는 Transformer 기반 구조를 적용하여 보다 높은 번역 품질을 달성해보고자 한다.
> **1) 목적** 본 실습의 목적은 한국어 문장을 영어로 번역하는 **기계번역 모델을 구현**하고 성능을 비교하는 것이다. 이를 위해 **전통적인 Seq2Seq 모델**, **Attention 기법을 적용한 모델**을 각각 구현한 후, 동일한 데이터셋을 기반으로 학습시켜 성능을 **정량적(BLEU 점수)** 및 **정성적으로(번역 분석) 평가**할 것이다.
