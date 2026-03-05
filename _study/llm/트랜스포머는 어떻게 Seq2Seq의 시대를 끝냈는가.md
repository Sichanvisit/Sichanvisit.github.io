---
title: "트랜스포머는 어떻게 Seq2Seq의 시대를 끝냈는가"
date: 2025-11-17
study_tab: "LLM"
tags:
  - LLM
  - NLP
  - Transformer
  - Seq2Seq
  - Self-Attention
  - Positional-Encoding
  - BERT
  - GPT
excerpt: "RNN 기반 Seq2Seq와 Transformer의 구조·연산·문맥 처리 차이를 비교하고, 트랜스포머가 표준이 된 이유를 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

트랜스포머는 단순한 성능 개선 모델이 아니라, NLP 아키텍처의 규칙 자체를 바꾼 전환점입니다.  
핵심은 RNN 기반 순차 처리에서 Self-Attention 기반 병렬 처리로의 이동입니다.

## 1. 구조적 단절: RNN과의 결별

| 구분 | Seq2Seq (+ Attention) | Transformer |
|---|---|---|
| 핵심 엔진 | RNN/LSTM/GRU 중심 | Self-Attention 중심 |
| 처리 방식 | 순차적(이전 시점 의존) | 병렬적(전체 토큰 동시 관계 계산) |
| 장기 의존성 | 완화되지만 한계 존재 | 전역 의존성 직접 학습 |

Seq2Seq는 어텐션을 “보조 장치”로 붙인 구조인 반면, 트랜스포머는 어텐션 자체를 주 엔진으로 삼았습니다.

## 2. 계산 방식 혁명: 순차 -> 병렬

### Seq2Seq 한계

- 시간축 의존 계산
- 긴 시퀀스일수록 학습/추론 지연
- GPU 병렬 효율 제한

### Transformer 장점

- 행렬 연산 기반 대규모 병렬화
- 긴 시퀀스 학습 효율 향상
- 대규모 사전학습(LLM) 가능성 확대

이 차이가 BERT/GPT 같은 대형 모델의 현실적 학습을 가능하게 했습니다.

## 3. 문맥 처리: 압축에서 상호 참조로

Seq2Seq는 입력 정보를 압축해 전달하는 경향이 강해 길이가 길어질수록 정보 손실 위험이 있습니다.  
Transformer는 각 토큰이 모든 토큰을 직접 참조(Self-Attention)해 전역 문맥을 동적으로 조합합니다.

즉, 문맥 처리의 중심이 “단일 벡터 압축”에서 “전역 관계 계산”으로 바뀐 것입니다.

## 4. 순서 정보 문제와 위치 인코딩

Self-Attention은 기본적으로 순서 정보를 알지 못하므로, Transformer는 **Positional Encoding**을 도입합니다.

- 토큰 임베딩 + 위치 벡터 결합
- 절대/상대 위치 신호를 모델에 주입
- 단어 순서가 의미에 미치는 영향을 보존

## 결론

트랜스포머는 다음을 동시에 달성했습니다.

- RNN 의존 제거
- 장기 의존성 학습 강화
- 대규모 병렬 학습 가능
- 전역 문맥 이해 향상

결과적으로 NLP의 표준 아키텍처가 되었고, 현대 LLM의 기반으로 자리잡았습니다.

