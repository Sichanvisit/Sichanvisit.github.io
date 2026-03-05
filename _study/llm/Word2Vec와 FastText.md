---
title: "Word2Vec을 넘어: FastText가 단어 임베딩의 판도를 바꾼 이유"
date: 2025-11-17
study_tab: "LLM"
tags:
  - LLM
  - NLP
  - Word-Embedding
  - Word2Vec
  - FastText
  - Subword
  - OOV
excerpt: "Word2Vec과 FastText의 핵심 차이(학습 단위), OOV 처리, 형태 정보 학습 능력, 실무 선택 기준을 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

단어 임베딩에서 Word2Vec은 큰 전환점이었지만, OOV와 형태 정보 처리에서 한계가 있었습니다.  
FastText는 subword 기반 접근으로 이 문제를 실용적으로 해결했습니다.

## 1. 핵심 차이: 단어를 보는 관점

- **Word2Vec**: 단어를 쪼갤 수 없는 단위로 학습
- **FastText**: 단어를 문자 n-gram(subword) 집합으로 분해해 학습

예: `apple` (n=3)
- `<ap`, `app`, `ppl`, `ple`, `le>` 같은 subword 조합

FastText의 단어 벡터는 보통 단어 자체 + subword 벡터 조합으로 표현됩니다.

## 2. 비교 요약

| 구분 | Word2Vec | FastText |
|---|---|---|
| 학습 단위 | 단어 단위 | subword(문자 n-gram) 단위 |
| OOV 처리 | 사실상 불가 | subword 조합으로 추론 가능 |
| 오타 강건성 | 낮음 | 상대적으로 높음 |
| 형태 정보 반영 | 제한적 | 강함 |
| 언어 적합성 | 정제된 대규모 코퍼스에 강함 | 형태 변화 많은 언어/UGC에 강함 |

## 3. FastText의 실전 장점

### 1) OOV 문제 완화

처음 보는 단어도 내부 subword를 통해 벡터를 만들 수 있어, 신조어·희귀어에 강합니다.

### 2) 오타/변형에 대한 강인성

철자가 조금 달라도 공통 subword를 공유하면 유사 벡터를 형성할 수 있습니다.

### 3) 형태적 유사성 학습

`run`, `running`, `runner`처럼 어근 공유 단어를 더 자연스럽게 가깝게 배치합니다.

## 4. 어떤 모델을 선택할까?

### Word2Vec이 유리한 경우

- 매우 정제된 대규모 코퍼스
- OOV 발생이 적은 환경
- 간단한 베이스라인이 필요한 경우

### FastText가 유리한 경우

- 신조어/오타/희귀어가 많은 데이터
- 형태 변화가 큰 언어(예: 한국어)
- 사용자 생성 텍스트(SNS/리뷰) 중심 태스크

## 결론

FastText는 Word2Vec의 철학을 계승하면서 subword를 도입해 실무 문제(OOV, 형태 정보, 노이즈 텍스트)를 효과적으로 해결한 모델입니다.  
또한 subword 기반 사고는 이후 BPE 토크나이저와 현대 LLM 전처리 철학으로 이어지는 중요한 연결고리입니다.

