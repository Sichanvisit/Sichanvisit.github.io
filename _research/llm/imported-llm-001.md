---
title: "10 4팀 손성경"
date: 2026-03-08
research_tab: "LLM"
research_kind: "Archive Note"
source_title: "10_4팀_손성경"
source_path: "13_LLM_GenAI/Code_Snippets/10_4팀_손성경.md"
excerpt: "전처리 비교 실험, 3종 임베딩 실험 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 전처리 비교 실험, 3종 임베딩 실험, 학습준비 순서로 핵심 장면을 먼저 훑고, 학습준비, 전처리 비교 실험, 3종 임베딩 실험 같은 코드로 실..."
research_summary: "전처리 비교 실험, 3종 임베딩 실험 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 전처리 비교 실험, 3종 임베딩 실험, 학습준비 순서로 핵심 장면을 먼저 훑고, 학습준비, 전처리 비교 실험, 3종 임베딩 실험 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 84개 코드 블록, 64개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 gensim, os, re, torch입니다."
research_artifacts: "ipynb/md · 코드 84개 · 실행 64개"
code_block_count: 84
execution_block_count: 64
research_focus:
  - "전처리 비교 실험"
  - "3종 임베딩 실험"
  - "학습준비"
research_stack:
  - "gensim"
  - "os"
  - "re"
  - "torch"
  - "numpy"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - llm
  - archive-note
---

전처리 비교 실험, 3종 임베딩 실험 중심의 LLM 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 LLM 학습 기록입니다. 본문은 전처리 비교 실험, 3종 임베딩 실험, 학습준비 순서로 핵심 장면을 먼저 훑고, 학습준비, 전처리 비교 실험, 3종 임베딩 실험 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 84개 코드 블록, 64개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 gensim, os, re, torch입니다.

**빠르게 볼 수 있는 포인트**: 전처리 비교 실험, 3종 임베딩 실험, 학습준비.

**남겨둔 자료**: `ipynb/md` 원본과 84개 코드 블록, 64개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 gensim, os, re, torch입니다.

**주요 스택**: `gensim`, `os`, `re`, `torch`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | LLM |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 84 |
| Execution Cells | 64 |
| Libraries | `gensim`, `os`, `re`, `torch`, `numpy`, `pandas`, `nltk`, `sklearn` |
| Source Note | `10_4팀_손성경` |

## What This Note Covers

### 전처리 비교 실험

먼저 다양한 전처리 방식(original, v1, v2, v2_1, v3)이 모델 성능에 어떤 영향을 미치는지 확인하기 위해 FastText 기반으로 전처리 비교 실험을 진행하였다. FastText를 기준 임베딩으로 선택한 이유는, - subword 기반이라 전처리 방법이 달라져도 단어 표현이 크게 무너지지 않고, - Word2Vec...

- 읽을 포인트: 텍스트 정제와 토큰 구성을 바꾸며 입력 품질을 비교하는 구간입니다.

### 3종 임베딩 실험

3종 임베딩 실험은 전처리(v2_1, v3_1)와 임베딩 방식(Word2Vec, FastText, GloVe)을 반복 실행하는 구조로 구성해보았다다. 전처리 → 임베딩 생성 → LSTM 학습 → 성능 평가의 순서로 자동화 루프를 만들고, 각 조합의 결과를 리스트와 DataFrame에 저장해 전처리–임베딩별 성능을 한눈에 비교할 수 있...

- 읽을 포인트: 임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다.

### 학습준비

LSTM 기반 모델 구조에서 사전 학습된 임베딩만 바꿨을 때 성능 차이를 비교하고자 한다. 임베딩 3종 1. Word2Vec: 단어 단위 임베딩 생성 방식 2. FastText: 서브워드 기반이라 희귀 단어에 조금 더 강함 3. GloVe: 스탠포드에서 공개한 전역 동시발생 통계 기반 임베딩으로 LSTM과 궁합이 좋음 - 대규모 코퍼...

- 읽을 포인트: 임베딩, 모델 구조, 학습 루프를 실제 코드로 연결하는 구간입니다.

### 추가 실험

전처리 과정에서 긴 텍스트 검토 누락을 확인하여 추가로 점검함. 2. 임베딩 실험에서 토큰화를 실수로 t.split()(단순 공백 기준)로 처리했던 문제를 발견함. 추가 실험에서는 보다 표준적이고 범용적인 토큰화 방식인 NLTK word_tokenize()를 적용하여 토큰화 방식 변화가 성능에 미치는 영향을 관찰하였다. 3. GloV...

- 읽을 포인트: 실험 조건을 바꾸고 지표를 비교하며 어떤 설정이 맞는지 확인하는 구간입니다.

### 실험 결과 요약

런타임이 중단되어 현재까지 나온 결과를 기준으로 분석했다.

- 읽을 포인트: 세부 흐름: 전처리 영향, Epoch 증가 효과, 임베딩에 따른 클래스별 성능 차이 분석

#### 전처리 영향

임베딩 3종 실험에서 v2_1과 v3_1의 성능 차이는 0.3~0.7% 수준으로 거의 없었음. - 즉, 이 데이터셋에서 stopword 제거 효과는 거의 없음

#### Epoch 증가 효과

학습 loss는 epoch 증가에 따라 크게 감소했으나, - Accuracy/F1은 5epoch 대비 10epoch에서 매우 미미한 개선만 발생함. → 이미 5epoch 부근에서 수렴 상태에 도달했던 것으로 보이며, 추가 epoch가 성능 향상에 크게 기여하지 않음

#### 임베딩에 따른 클래스별 성능 차이 분석

각 임베딩 특성에 따라 강한 클래스가 다르게 나타났다. FastText가 강한 클래스: - 기술/하드웨어/컴퓨터 관련 토픽 - 제품명, 코드 조각, 오타·변형 표현 등 subword 단서가 많은 경우 유리 - FastText의 특성상 형태소 변형과 희귀 단어를 잘 처리하기 때문에...

### 추가 실험 결과 요약표 정리

3종 임베딩 실험 (원본 GloVe / 이상치 포함 / split 기반 / 10 epoch) 추가실험 1 (GloVe vocab 수정 / 이상치 삭제 / tokenizer 기반 / 5 epoch)

- 읽을 포인트: 실험 조건을 바꾸고 지표를 비교하며 어떤 설정이 맞는지 확인하는 구간입니다.

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

1. 전처리 비교 실험: 먼저 다양한 전처리 방식(original, v1, v2, v2_1, v3)이 모델 성능에 어떤 영향을 미치는지 확인하기 위해 FastText 기반으로 전처리 비교 실험을 진행하였다. FastText를 기준 임베딩으로 선택한 이유는, - subw...
2. 3종 임베딩 실험: 3종 임베딩 실험은 전처리(v2_1, v3_1)와 임베딩 방식(Word2Vec, FastText, GloVe)을 반복 실행하는 구조로 구성해보았다다. 전처리 → 임베딩 생성 → LSTM 학습 → 성능 평가의 순서로 자동화 루프를 만들고, 각 조...
3. 학습준비: LSTM 기반 모델 구조에서 사전 학습된 임베딩만 바꿨을 때 성능 차이를 비교하고자 한다. 임베딩 3종 1. Word2Vec: 단어 단위 임베딩 생성 방식 2. FastText: 서브워드 기반이라 희귀 단어에 조금 더 강함 3. GloVe: 스탠포드에서...
4. 추가 실험: 전처리 과정에서 긴 텍스트 검토 누락을 확인하여 추가로 점검함. 2. 임베딩 실험에서 토큰화를 실수로 t.split()(단순 공백 기준)로 처리했던 문제를 발견함. 추가 실험에서는 보다 표준적이고 범용적인 토큰화 방식인 NLTK word_tokeniz...
5. 실험 결과 요약: 전처리 영향, Epoch 증가 효과
6. 추가 실험 결과 요약표 정리: 3종 임베딩 실험 (원본 GloVe / 이상치 포함 / split 기반 / 10 epoch) 추가실험 1 (GloVe vocab 수정 / 이상치 삭제 / tokenizer 기반 / 5 epoch)

## Code Highlights

### 학습준비

`학습준비`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 데이터셋 정의, padding 또는 truncate 흐름이 주석과 함께 드러납니다.

```python
# @title 데이터셋 정의
class TextEmbeddingDataset(Dataset):
    """
    텍스트를 모델에 넣기 위해 토큰화된 리스트를
    -> word2idx 기반 정수 인덱스 리스트로 변환하고
    -> max_len 기준으로 padding/truncation 하는 Dataset 클래스 구현

    (텍스트 → 정수 인덱스 시퀀스 → max_len 길이로 padding)
    """
    def __init__(self, token_list, labels, word2idx, max_len):
        self.token_list = token_list
        self.labels = labels
        self.word2idx = word2idx
        self.max_len = max_len

    def __len__(self):
        return len(self.token_list)

    def __getitem__(self, idx):
        tokens = self.token_list[idx]
        encoded = [self.word2idx.get(word, 0) for word in tokens]

        # padding 또는 truncate
        if len(encoded) < self.max_len:
            encoded += [0] * (self.max_len - len(encoded))
        else:
            encoded = encoded[:self.max_len]

# ... trimmed ...
```

### 전처리 비교 실험

`전처리 비교 실험`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 전처리 v1 학습, ======== 전처리 버전 선택 =========, ================================== 흐름이 주석과 함께 드러납니다.

```python
# @title 전처리 v1 학습
'''
clean_fns = {
    "v1_minimal": clean_text_v1,
    "v2_special_removed": clean_text_v2,
    "v2_1_patterns_preserved": clean_text_v2_1,
    "v3_stopword_removed": clean_text_v3
}
'''
# ======== 전처리 버전 선택 =========
clean_fn = clean_fns["v1_minimal"]   # ← 여기만 바꿔서 실험
print("사용 중인 전처리 버전:", clean_fn.__name__)
# ==================================

# 1) 텍스트 전처리
train_clean = [clean_fn(t) for t in X_train]
test_clean  = [clean_fn(t) for t in X_test]

# 2) 토큰화
train_tokens = [t.split() for t in train_clean]
test_tokens  = [t.split() for t in test_clean]

# 3) FastText 학습
ft = FastText(
    sentences=train_tokens,
    vector_size=vector_size,
    window=5,
    min_count=1,
# ... trimmed ...
```

### 3종 임베딩 실험

`3종 임베딩 실험`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 실험 자동화 파이프라인, ==========================================, 실험할 전처리 버전 2개 선택 흐름이 주석과 함께 드러납니다.

```python
# @title 실험 자동화 파이프라인

# ==========================================
# 0) 실험할 전처리 버전 2개 선택
# ==========================================
target_preprocesses = [
    "v2_1_patterns_preserved",
    "v3_1_stopword_removed_patterns_preserved"
]

target_embeddings = ["word2vec", "fasttext", "glove"]

results_embed = []   # 결과 저장


# ==========================================
# 1) 실험 시작
# ==========================================
for prep_name in target_preprocesses:

    clean_fn = clean_fns[prep_name]
    print(f"\n==============================")
    print("전처리 버전:", prep_name)
    print("==============================")

    # 전처리 → 토큰화
    train_clean = [clean_fn(t) for t in X_train]
    test_clean  = [clean_fn(t) for t in X_test]
# ... trimmed ...
```

### 추가 실험

`추가 실험`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 추가실험 1, ====== 임베딩 생성 ======, 수정: vocab = train_tokens 기반으로 생성해야 되는데 아까는 전체 Glo... 흐름이 주석과 함께 드러납니다.

```python
# @title 추가실험 1
'''
전처리 v2_1, class_weight 적용, glove 코드 수정, 5epoch
'''
target_preprocess = "v2_1_patterns_preserved"
target_embeddings = ["word2vec", "fasttext", "glove"]

results_embed = []

for emb_type in target_embeddings:

    print(f"\n>>> 실험: Preprocess={target_preprocess}, Embedding={emb_type}")

    # ====== 임베딩 생성 ======
    if emb_type == "word2vec":
        model_emb = Word2Vec(train_tokens, vector_size=vector_size, min_count=1, window=5, sg=1)
        word2idx = {w: i+1 for i, w in enumerate(model_emb.wv.index_to_key)}
        embedding_matrix = np.zeros((len(word2idx)+1, vector_size))
        for w, i in word2idx.items():
            embedding_matrix[i] = model_emb.wv[w]

    elif emb_type == "fasttext":
        model_emb = FastText(train_tokens, vector_size=vector_size, min_count=1, window=5, sg=1)
        word2idx = {w: i+1 for i, w in enumerate(model_emb.wv.index_to_key)}
        embedding_matrix = np.zeros((len(word2idx)+1, vector_size))
        for w, i in word2idx.items():
            embedding_matrix[i] = model_emb.wv[w]

# ... trimmed ...
```

## Source Bundle

- Source path: `13_LLM_GenAI/Code_Snippets/10_4팀_손성경.md`
- Source formats: `ipynb`, `md`
- Companion files: `10_4팀_손성경.ipynb`, `10_4팀_손성경.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `13_LLM_code_Roadmap.md`, `13_LLM_GenAI_Code_Summary.md`
- External references: `localhost`, `nlp.stanford.edu`

## Note Preview

> 텍스트 데이터를 입력으로 받아 뉴스 그룹 게시글의 카테고리를 예측하는 딥 러닝 모델 구현
> 18,846개의 뉴스 문서를 20개의 카테고리로 분류한 News Group 20 데이터 (뉴스 기사가 아니라 인터넷 포럼 글 모음집)
