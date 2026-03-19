---
title: "AI Engineering Research Map"
date: 2026-03-18
research_tab: "Overview"
research_kind: "Research Map"
research_summary: "Machine Learning, Deep Learning, LLM/GenAI로 흩어져 있던 실습과 미션을 하나의 research map으로 다시 엮은 개요 글입니다. 어떤 트랙에서 무엇을 구현했고, 대표 작업물이 무엇인지 빠르게 훑을 수 있게 구성했습니다."
research_artifacts: "ML 22 · DL 55 · LLM 38"
excerpt: "ML, DL, LLM 실습 노트를 포트폴리오형 리서치 지도로 다시 정리한 개요 글"
tags:
  - research-archive
  - portfolio
  - machine-learning
  - deep-learning
  - llm
header:
  teaser: /assets/images/research/research-map.svg
---

## Archive Snapshot

| Track | Source Notes | Main Focus | Representative Artifacts |
|------|-------------:|------------|--------------------------|
| Machine Learning | 22 | Python, pandas, statistics, classical ML, feature engineering | `Hotel Booking Demand`, `Bike Rental System`, `Portuguese Bank Data Marketing` |
| Deep Learning | 55 | PyTorch fundamentals, CNN/RNN, detection, segmentation, generation | `Mission_7_강사공유`, `Mission_8_강사공유`, `Mission 9_이미지 생성` |
| LLM / GenAI | 38 | Embedding, RAG, fine-tuning, LangGraph agents, evaluation | `한국어_FAQ_챗봇_LangSmith`, `Gemma_QLoRA`, `미션13`, `미션14` |

## Why I Reorganized These Notes

원본 노트에는 수업 실습, 스프린트 미션, 강사 공유 코드, 혼자 확장한 실험이 한꺼번에 섞여 있었습니다.  
이 섹션에서는 그 재료를 그대로 나열하지 않고, 아래 기준으로 다시 묶었습니다.

- 실습 파일을 "무엇을 만들었는가"보다 "어떤 문제를 어떻게 풀었는가" 중심으로 재정리했습니다.
- 강의용 예제도 그대로 복붙한 기록이 아니라, 실제로 익힌 엔지니어링 포인트가 드러나도록 선별했습니다.
- 모델 이름만 적는 대신 데이터 전처리, 평가 지표, 실패 지점, 다음 실험 방향까지 남겼습니다.

## Track Guide

### 1. Machine Learning

기초 Python 실습에서 시작해 pandas, 통계, 시각화, scikit-learn 기반 회귀/분류, 앙상블, 차원 축소까지 이어지는 흐름입니다.  
특히 스프린트 미션에서는 단순히 모델을 돌리는 수준을 넘어서, 지표에 맞는 전처리와 피처 엔지니어링을 어떻게 고르는지에 집중했습니다.

### 2. Deep Learning

PyTorch 텐서와 데이터 로더부터 모델링, CNN, RNN, 사전학습 모델, Object Detection, Segmentation, GAN/VAE까지 시야를 확장한 트랙입니다.  
정확도만 보는 분류 실습에서 끝나지 않고, IoU, AP, mAP, Dice loss 같은 비전 태스크의 평가 관점으로 넘어간 흔적을 담고 있습니다.

### 3. LLM / GenAI

텍스트 벡터화와 Transformer 기초부터 BERT/GPT 계열 사전학습, LoRA/QLoRA, RAG, LangChain, LangGraph까지 연결되는 실험 기록입니다.  
이 영역은 특히 "모델 호출"이 아니라, 검색, 추적, 평가, 도구 호출, 파이프라인 설계까지 시스템으로 다뤘다는 점을 강조하고 싶었습니다.

## What Makes This Section Portfolio-Worthy

- 수업 내용을 단순히 따라간 흔적이 아니라, 문제를 구조화하는 방식이 보입니다.
- 회귀에서는 `RMSLE`, 분류에서는 `Precision/Recall/F1/ROC-AUC`, 비전에서는 `IoU/AP/mAP`, LLM에서는 `Grounded RAG`와 `PEFT 효율`처럼 태스크에 맞는 기준이 남아 있습니다.
- 같은 기술을 여러 번 반복한 노트라도, 이번에는 "학습 경로"가 아니라 "실제 역량"으로 읽히도록 재배치했습니다.

## Recommended Reading Order

1. 예측 문제와 전통 ML 감각을 먼저 보고 싶다면 `Machine Learning Sprint Archive`
2. 컴퓨터 비전과 PyTorch 확장을 보고 싶다면 `Deep Learning Vision Track`
3. 최근 관심사인 RAG, LoRA, Agent 흐름을 보고 싶다면 `LLM / GenAI Experiment Log`

## Next Step

이 Research 섹션은 강의 노트를 보관하는 장소라기보다, 앞으로 프로젝트로 확장할 주제를 고르는 실험실에 가깝습니다.  
이후에는 여기서 검증한 흐름 중 재사용 가치가 큰 것들을 별도 `portfolio` 프로젝트로 승격시킬 계획입니다.
