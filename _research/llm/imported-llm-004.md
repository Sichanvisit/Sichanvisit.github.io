---
title: "임베딩 스팸메시지분류"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)임베딩_스팸메시지분류"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)임베딩_스팸메시지분류.md"
excerpt: "https://wikidocs.net/50739"
research_summary: "https://wikidocs.net/50739. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 27개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pandas, numpy, matplotlib, torch입니다."
research_artifacts: "md · 코드 27개 · 실행 13개"
code_block_count: 27
execution_block_count: 13
research_focus:
  - "데이터 불러오기"
  - "데이터 분할"
  - "https"
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

https://wikidocs.net/50739. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 27개 코드 블록, 13개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pandas, numpy, matplotlib, torch입니다.

**빠르게 볼 수 있는 포인트**: 데이터 불러오기, 데이터 분할, https.

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

### Key Step

SMS Spam 데이터 다운로드 및 로드

### Key Step

Series를 list로 변환하여 레이블 인덱스 문제를 제거합니다

### Key Step

Word2Vec 모델 학습 및 단어-인덱스 매핑 생성

## Implementation Flow

1. Word2Vec: https://wikidocs.net/50739
2. Key Step: SMS Spam 데이터 다운로드 및 로드
3. Key Step: Series를 list로 변환하여 레이블 인덱스 문제를 제거합니다
4. Key Step: Word2Vec 모델 학습 및 단어-인덱스 매핑 생성

## Code Highlights

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

> ---
> https://wikidocs.net/50739
