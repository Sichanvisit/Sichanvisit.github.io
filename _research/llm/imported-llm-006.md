---
title: "10 텍스트임베딩 예"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1_10_텍스트임베딩_예"
source_path: "13_LLM_GenAI/Code_Snippets/3-1_10_텍스트임베딩_예.md"
excerpt: "✔ 요약, ✔ 6. 결론 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 ✔ 요약, ✔ 6. 결론, ✔ 데이터 설명 순서로 핵심 장면을 먼저 훑고, 데이터셋 클래스 정의, LSTM 모델 정의, LSTM 모델 학습 같은 코드로 실제..."
research_summary: "✔ 요약, ✔ 6. 결론 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 ✔ 요약, ✔ 6. 결론, ✔ 데이터 설명 순서로 핵심 장면을 먼저 훑고, 데이터셋 클래스 정의, LSTM 모델 정의, LSTM 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 45개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, random, re, sys입니다."
research_artifacts: "md · 코드 45개 · 실행 45개"
code_block_count: 45
execution_block_count: 45
research_focus:
  - "✔ 요약"
  - "✔ 6. 결론"
  - "✔ 데이터 설명"
research_stack:
  - "os"
  - "random"
  - "re"
  - "sys"
  - "urllib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

✔ 요약, ✔ 6. 결론 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 ✔ 요약, ✔ 6. 결론, ✔ 데이터 설명 순서로 핵심 장면을 먼저 훑고, 데이터셋 클래스 정의, LSTM 모델 정의, LSTM 모델 학습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 45개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, random, re, sys입니다.

**빠르게 볼 수 있는 포인트**: ✔ 요약, ✔ 6. 결론, ✔ 데이터 설명.

**남겨둔 자료**: `md` 원본과 45개 코드 블록, 45개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, random, re, sys입니다.

**주요 스택**: `os`, `random`, `re`, `sys`, `urllib`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 45 |
| Execution Cells | 45 |
| Libraries | `os`, `random`, `re`, `sys`, `urllib`, `warnings`, `zipfile`, `numpy` |
| Source Note | `3-1_10_텍스트임베딩_예` |

## What This Note Covers

### ✔ 요약

본 실습에서는 20개의 뉴스 카테고리로 구성된 텍스트 분류 문제를 해결하기 위해, LSTM 기반 분류 모델을 구현하고 성능을 비교하였다. 텍스트는 소문자화, 특수문자 제거, 불용어 제거를 통해 학습에 적합한 형태로 정제했다. 단어 임베딩 방식으로는 Word2Vec, FastText, GloVe를 사용으며, 이후에는 동일한 구조의 Bi...

- 읽을 포인트: ✔ 요약에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### ✔ 6. 결론

본 프로젝트에서는 Word2Vec, FastText, GloVe 세 가지 임베딩 방식을 활용하여 뉴스 카테고리 분류 모델을 구현하고 성능을 비교하였다. 모든 실험에서 동일한 BiLSTM 모델 구조와 전처리 방식을 적용하였으며, 클래스 불균형 문제를 고려해 클래스 가중치를 반영한 손실 함수를 사용하였다. 실험 결과, GloVe 임베딩을...

- 읽을 포인트: ✔ 6. 결론에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### ✔ 데이터 설명

목적 본 실습의 목적은 18,846개의 뉴스 문서를 20개의 주제 카테고리로 분류하는 딥러닝 모델을 구현하는 것이다. 텍스트 데이터를 입력으로 받아 뉴스의 카테고리를 예측하며, 다양한 임베딩 기법을 적용해 분류 성능을 비교한다. 데이터셋 사용한 데이터는 총 18,846개의 뉴스 문서로 구성된 20 Newsgroups 데이터셋으로, 각...

- 읽을 포인트: ✔ 데이터 설명에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### ✔ 사전 세팅

✔️ 사전 세팅는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

- 읽을 포인트: 세부 흐름: ✔️ 사전 세팅

#### ✔️ 사전 세팅

✔️ 사전 세팅는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 전처리와 학습/검증 분리를 담당해 전체 파이프라인의 출발점을 정리하는 코드입니다.

### ✔ 4. FastText

Word2vec와 코드 구성이 유사해서 구체적인 설명은 생략한다.

- 읽을 포인트: 세부 흐름: LSTM 모델 정의, LSTM 모델 학습, LSTM 모델 평가

#### LSTM 모델 정의

임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다.

#### LSTM 모델 학습

임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다.

#### LSTM 모델 평가

FastText의 전체 정확도는 65%로, Word2Vec와 동일하다. 클래스별 F1-Score를 보면 FastText가 recall에서 약간 높거나 비슷한 수준이다. FastText는 이론적으로 희귀 단어 처리에 강점이 있지만, 뉴스 데이터셋에 등장하는 단어들이 대부분 친숙한 단...

### ✔ 5. GloVe

GloVe 실험에서는 사전학습된 GloVe 벡터(glove.6B.200d)를 사용하였다. 앞선 Word2vec나 FastText와 마찬가지로, 코드 구성이 유사해서 구체적인 설명은 생략한다.

- 읽을 포인트: 세부 흐름: LSTM 모델 정의, LSTM 모델 학습, LSTM 모델 평가

#### LSTM 모델 정의

임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다.

#### LSTM 모델 학습

임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다.

#### LSTM 모델 평가

Word2Vec, FastText와 비교했을 때, GloVe의 전체 정확도는 68%로 가장 좋은 성능을 보인다. 특히 class 10, 13, 7 등 일부 주요 클래스에서 precision/recall 모두 향상되었다. class 19처럼 희귀 클래스에선 여전히 낮은 점수를 보이지...

## Why This Matters

### 임베딩과 표현 학습

- 왜 필요한가: 텍스트나 토큰을 그대로는 모델이 다룰 수 없기 때문에, 의미를 담은 수치 벡터 표현으로 바꾸는 단계가 필요합니다.
- 왜 이 방식을 쓰는가: Word2Vec, FastText, GloVe 같은 방식은 같은 단어라도 주변 문맥이나 서브워드 정보를 반영해 비교 가능한 표현 공간을 만듭니다.
- 원리: 자주 함께 등장하는 단어는 가까운 벡터가 되도록 학습해, 의미적으로 비슷한 표현이 공간에서도 가까워지게 합니다.

### 순차 데이터 모델링

- 왜 필요한가: 문장, 시계열처럼 순서가 중요한 데이터는 현재 입력만이 아니라 앞선 맥락까지 함께 봐야 합니다.
- 왜 이 방식을 쓰는가: LSTM/GRU는 기본 RNN보다 긴 문맥을 더 안정적으로 다룰 수 있어 텍스트 분류나 시계열 예측 실습에 자주 쓰입니다.
- 원리: 이전 시점의 은닉 상태를 다음 입력과 함께 업데이트하며, 게이트 구조로 필요한 정보는 남기고 불필요한 정보는 줄입니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. ✔ 요약: 본 실습에서는 20개의 뉴스 카테고리로 구성된 텍스트 분류 문제를 해결하기 위해, LSTM 기반 분류 모델을 구현하고 성능을 비교하였다. 텍스트는 소문자화, 특수문자 제거, 불용어 제거를 통해 학습에 적합한 형태로 정제했다. 단어 임베딩 방식으로는 Wo...
2. ✔ 6. 결론: 본 프로젝트에서는 Word2Vec, FastText, GloVe 세 가지 임베딩 방식을 활용하여 뉴스 카테고리 분류 모델을 구현하고 성능을 비교하였다. 모든 실험에서 동일한 BiLSTM 모델 구조와 전처리 방식을 적용하였으며, 클래스 불균형 문제를...
3. ✔ 데이터 설명: 목적 본 실습의 목적은 18,846개의 뉴스 문서를 20개의 주제 카테고리로 분류하는 딥러닝 모델을 구현하는 것이다. 텍스트 데이터를 입력으로 받아 뉴스의 카테고리를 예측하며, 다양한 임베딩 기법을 적용해 분류 성능을 비교한다. 데이터셋 사용한...
4. ✔ 사전 세팅: ✔️ 사전 세팅
5. ✔ 4. FastText: LSTM 모델 정의, LSTM 모델 학습
6. ✔ 5. GloVe: LSTM 모델 정의, LSTM 모델 학습

## Code Highlights

### 데이터셋 클래스 정의

`데이터셋 클래스 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 데이터를 모델이 바로 받을 수 있는 샘플 구조로 바꾸기 위해 커스텀 Dataset을 정의하는 부분입니다.

```python
class TextEmbeddingDataset(Dataset):
    def __init__(self, texts, labels, word2idx, max_len):
        self.texts = texts
        self.labels = labels
        self.word2idx = word2idx
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        tokens = self.texts[idx]
        encoded = [self.word2idx.get(word, self.word2idx["<UNK>"]) for word in tokens]

        if len(encoded) < self.max_len:
            encoded += [self.word2idx["<PAD>"]] * (self.max_len - len(encoded))
        else:
            encoded = encoded[:self.max_len]

        return torch.tensor(encoded, dtype=torch.long), torch.tensor(self.labels[idx], dtype=torch.long)
```

### LSTM 모델 정의

`LSTM 모델 정의`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 임베딩 레이어, LSTM, FC 레이어 흐름이 주석과 함께 드러납니다.

```python
class LSTMClassifier(nn.Module):
    def __init__(self, embedding_matrix, hidden_dim, output_dim, num_layers, dropout):
        super(LSTMClassifier, self).__init__()

        vocab_size, embedding_dim = embedding_matrix.shape

        # 1. 임베딩 레이어
        self.embedding = nn.Embedding.from_pretrained(
            torch.tensor(embedding_matrix, dtype=torch.float).to(device),
            freeze=False
        )

        # 2. LSTM
        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            dropout=dropout if num_layers > 1 else 0,
            batch_first=True,
            bidirectional=True
        )

        # 3. FC 레이어
        self.fc = nn.Linear(hidden_dim * 2, output_dim)

    def forward(self, x):
        x = self.embedding(x)
        _, (hidden, _) = self.lstm(x)
# ... trimmed ...
```

### LSTM 모델 학습

`LSTM 모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 손실 계산, 역전파, optimizer 또는 scheduler 업데이트가 이어지는 학습 루프입니다.

```python
EPOCHS = 20

for epoch in range(EPOCHS):
    model.train()
    total_loss = 0

    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"[Epoch {epoch+1}] Loss: {avg_loss:.4f}")
```

### LSTM 모델 평가

`LSTM 모델 평가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 성능 평가 흐름이 주석과 함께 드러납니다.

```python
model.eval()
all_preds = []
all_labels = []

with torch.no_grad():
    for inputs, labels in test_loader:
        inputs = inputs.to(device)
        outputs = model(inputs)
        preds = torch.argmax(outputs, dim=1).cpu().numpy()
        all_preds.extend(preds)
        all_labels.extend(labels.numpy())

# 성능 평가
print(classification_report(all_labels, all_preds))
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-1_10_텍스트임베딩_예.md`
- Source formats: `md`
- Companion files: `3-1_10_텍스트임베딩_예.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `nlp.stanford.edu`

## Note Preview

> tags: ["LLM", "Code"]
> 본 실습에서는 **20개의 뉴스 카테고리**로 구성된 텍스트 분류 문제를 해결하기 위해, **LSTM 기반 분류 모델**을 구현하고 성능을 비교하였다. 텍스트는 **소문자화**, **특수문자 제거**, **불용어 제거**를 통해 학습에 적합한 형태로 정제했다.
