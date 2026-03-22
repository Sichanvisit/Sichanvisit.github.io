---
title: "임베딩 스팸메시지분류"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)임베딩_스팸메시지분류"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)임베딩_스팸메시지분류.md"
excerpt: "임베딩 스팸메시지분류에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 Word2Vec, GloVe, 데이터 불러오기 순서로 핵심 장면을 먼저 훑고, 데이터 분할, Word2Vec, FastText 같은 코드로 실제 구현을 이어서 확인할 수 있습니다...."
research_summary: "임베딩 스팸메시지분류에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 Word2Vec, GloVe, 데이터 불러오기 순서로 핵심 장면을 먼저 훑고, 데이터 분할, Word2Vec, FastText 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 27개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pandas, numpy, matplotlib, torch입니다."
research_artifacts: "md · 코드 27개 · 실행 13개"
code_block_count: 27
execution_block_count: 13
research_focus:
  - "Word2Vec"
  - "GloVe"
  - "데이터 불러오기"
research_stack:
  - "pandas"
  - "numpy"
  - "matplotlib"
  - "torch"
  - "sklearn"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

임베딩 스팸메시지분류에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 Word2Vec, GloVe, 데이터 불러오기 순서로 핵심 장면을 먼저 훑고, 데이터 분할, Word2Vec, FastText 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 27개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pandas, numpy, matplotlib, torch입니다.

**빠르게 볼 수 있는 포인트**: Word2Vec, GloVe, 데이터 불러오기.

**남겨둔 자료**: `md` 원본과 27개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pandas, numpy, matplotlib, torch입니다.

**주요 스택**: `pandas`, `numpy`, `matplotlib`, `torch`, `sklearn`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 27 |
| Execution Cells | 13 |
| Libraries | `pandas`, `numpy`, `matplotlib`, `torch`, `sklearn`, `nltk`, `gensim`, `os` |
| Source Note | `3-1(실습)임베딩_스팸메시지분류` |

## What This Note Covers

### Word2Vec

https://wikidocs.net/50739

- 읽을 포인트: Word2Vec 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### GloVe

glove.6B.100d.txt 사용

- 읽을 포인트: GloVe 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 데이터 불러오기

데이터 불러오기 코드를 직접 따라가며 데이터 불러오기 흐름을 확인했습니다.

- 읽을 포인트: 데이터 불러오기 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 데이터 분할

데이터 분할 코드를 직접 따라가며 데이터 분할 흐름을 확인했습니다.

- 읽을 포인트: 데이터 분할 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### FastText

FastText 코드를 직접 따라가며 FastText 흐름을 확인했습니다.

- 읽을 포인트: FastText 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

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

1. Word2Vec: https://wikidocs.net/50739
2. GloVe: glove.6B.100d.txt 사용
3. 데이터 불러오기: 데이터 불러오기 코드를 직접 따라가며 데이터 불러오기 흐름을 확인했습니다.
4. 데이터 분할: 데이터 분할 코드를 직접 따라가며 데이터 분할 흐름을 확인했습니다.
5. FastText: FastText 코드를 직접 따라가며 FastText 흐름을 확인했습니다.

## Code Highlights

### 데이터 분할

`데이터 분할`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 라벨 변환, Series를 list로 변환하여 레이블 인덱스 문제를 제거합니다 흐름이 주석과 함께 드러납니다.

```python
# 라벨 변환
df['label'] = df['label'].map({'ham':0, 'spam': 1})
texts, labels = df['message'].tolist(), df['label'].tolist()
train_inputs, test_inputs, train_targets, test_targets = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Series를 list로 변환하여 레이블 인덱스 문제를 제거합니다
train_inputs_list = train_inputs.tolist()
train_targets_list = train_targets.tolist()
test_inputs_list = test_inputs.tolist()
test_targets_list = test_targets.tolist()

print(f"Number of documents: {len(texts)}")
print(f"Sample documents: \n{texts[0]}")
```

### Word2Vec

`Word2Vec`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 확률값(outputs)이 0.5 이상이면 1(스팸), 아니면 0(햄)으로 변환 흐름이 주석과 함께 드러납니다.

```python
def train(model, loader, criterion, optimizer):
  """모델을 1 epoch 동안 학습시키는 함수"""
  model.train()
  total_loss = 0
  for texts, labels in loader:
      texts, labels = texts.to(device), labels.to(device)
      labels = labels.unsqueeze(1)  # 라벨 크기를 (batch_size, 1)로 변환
      optimizer.zero_grad()
      outputs = model(texts)  # 모델 출력: (batch_size, 1)
      loss = criterion(outputs, labels)  # BCELoss 사용
      loss.backward()
      optimizer.step()
      total_loss += loss.item()
  return total_loss / len(loader)

def evaluate(model, loader):
  """모델의 성능(정확도)을 평가하는 함수"""
  model.eval()
  correct, total = 0, 0
  with torch.no_grad():
      for texts, labels in loader:
          texts, labels = texts.to(device), labels.to(device)
          labels = labels.unsqueeze(1).float()
          outputs = model(texts)
          # 확률값(outputs)이 0.5 이상이면 1(스팸), 아니면 0(햄)으로 변환
          predictions = (outputs >= 0.5).float()
          correct += (predictions == labels).sum().item()
          total += labels.size(0)
# ... trimmed ...
```

### FastText

`FastText`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습, 모델 평가 흐름이 주석과 함께 드러납니다.

```python
# 모델 학습
for epoch in range(10):
    loss = train(model_fasttext, train_loader_fasttext, loss_fn, optimizer)
    print(f"Epoch {epoch+1}, Loss: {loss:.4f}")

# 모델 평가
accuracy = evaluate(model_fasttext, test_loader_fasttext)
print(f"Test Accuracy: {accuracy:.4f}")
```

### GloVe

`GloVe`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습, 모델 평가 흐름이 주석과 함께 드러납니다.

```python
model_glove = EmbeddingLSTM(glove_matrix, hidden_dim, output_dim).to(device)
loss_fn = nn.BCELoss()
optimizer = torch.optim.Adam(model_glove.parameters(), lr=0.005)

# 모델 학습
for epoch in range(10):
    loss = train(model_glove, train_loader_glove, loss_fn, optimizer)
    print(f"Epoch {epoch+1}, Loss: {loss:.4f}")

# 모델 평가
accuracy = evaluate(model_glove, test_loader_glove)
print(f"Test Accuracy: {accuracy:.4f}")
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/3-1(실습)임베딩_스팸메시지분류.md`
- Source formats: `md`
- Companion files: `3-1(실습)임베딩_스팸메시지분류.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `raw.githubusercontent.com`, `wikidocs.net`, `nlp.stanford.edu`

## Note Preview

> https://wikidocs.net/50739
> - glove.6B.100d.txt 사용
