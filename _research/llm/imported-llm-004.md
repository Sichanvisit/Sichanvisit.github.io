---
title: "임베딩 스팸메시지분류"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "3-1(실습)임베딩_스팸메시지분류"
source_path: "13_LLM_GenAI/Code_Snippets/3-1(실습)임베딩_스팸메시지분류.md"
excerpt: "https://wikidocs.net/50739"
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
| Code Blocks | 27 |
| Execution Cells | 13 |
| Libraries | `pandas`, `numpy`, `matplotlib`, `torch`, `sklearn`, `nltk`, `gensim`, `os` |
| Source Note | `3-1(실습)임베딩_스팸메시지분류` |

## What I Worked On

- 데이터 불러오기
- SMS Spam 데이터 다운로드 및 로드
- 데이터 확인
- GPU 설정
- 데이터 분할

## Implementation Flow

1. 데이터 불러오기
2. SMS Spam 데이터 다운로드 및 로드
3. 데이터 확인
4. GPU 설정
5. 데이터 분할
6. 라벨 변환

## Code Highlights

### Word2Vec

```python
class WordSpamDataset(Dataset):
  """텍스트 문장을 토큰화, 정수 인코딩, 패딩/절단을 거쳐 지정된 길이(max_len)의 텐서로 변환하는 스팸 데이터셋"""
  def __init__(self, texts, labels, word2idx, max_len):
      self.texts = texts
      self.labels = labels
      self.word2idx = word2idx
      self.max_len = max_len

  def __len__(self):
      return len(self.texts)

  def __getitem__(self, idx):
      tokens = word_tokenize(self.texts[idx])
      encoded = [self.word2idx.get(word, 0) for word in tokens]  # OOV 단어는 0
      if len(encoded) < self.max_len:
          encoded += [0] * (self.max_len - len(encoded))
      else:
          encoded = encoded[:self.max_len]
      return torch.tensor(encoded, dtype=torch.long), torch.tensor(self.labels[idx], dtype=torch.float)
```

### Word2Vec

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
