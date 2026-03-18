---
title: "LLM / GenAI Experiment Log"
date: 2026-03-15
research_tab: "LLM"
research_kind: "Track Overview"
excerpt: "임베딩, RAG, LoRA, LangGraph 에이전트까지 이어지는 생성형 AI 실험 노트를 포트폴리오용으로 묶었습니다."
tags:
  - llm
  - genai
  - rag
  - lora
  - langgraph
header:
  teaser: /assets/images/research/llm-genai.svg
classes: wide
---

## Research Snapshot

| Item | Summary |
|------|---------|
| Scope | 텍스트 벡터화, Transformer 계열, 미세조정, RAG, LangChain, LangGraph |
| Main Stack | Hugging Face, LangChain, LangGraph, FAISS, bitsandbytes, PEFT |
| Core Question | LLM을 단순 호출이 아니라 검색, 추론, 평가, 도구 사용이 가능한 시스템으로 어떻게 다룰 것인가 |
| Portfolio Angle | 모델 사용법보다 파이프라인 구성과 효율 비교에 초점을 둔 트랙 |

## Core Themes

- 텍스트 전처리와 임베딩, 벡터화, 스팸 분류 실습으로 NLP 기초를 다졌습니다.
- Attention, Seq2Seq, Transformer, BERT, GPT, 허깅페이스 실습으로 LLM 이전 계보를 따라갔습니다.
- `Freezing`, `LoRA`, `QLoRA`, `Gemma` 실습으로 파인튜닝 비용을 줄이는 방식을 직접 다뤘습니다.
- `LangChain`, `RAG`, `하이브리드 검색`, `한국어 FAQ 챗봇`, `LangGraph`, `ReAct 에이전트`로 시스템 설계 관점까지 확장했습니다.

## Highlighted Artifacts

| Artifact | Focus | Why It Matters |
|----------|-------|----------------|
| `3-5 (실습)한국어_FAQ_챗봇_LangSmith` | 한국어 FAQ 기반 RAG, LangSmith 추적, 디버깅 | 단순 챗봇이 아니라 모니터링 가능한 체인 설계를 경험했습니다. |
| `3-4 (실습)3_Gemma_QLoRA` | `gemma-3-1b-it`, 4bit 양자화, `LoraConfig`, `SFTTrainer` | 제한된 자원에서도 미세조정 가능한 실전 감각을 얻었습니다. |
| `4-3 LangGraph_3_ReAct에이전트` | `create_react_agent`와 `StateGraph` 직접 구현 비교 | Tool calling과 에이전트 흐름을 코드 레벨에서 이해했습니다. |
| `미션13_1팀_박시찬` | 감성 분류에서 Full FT vs LoRA 비교 | 성능과 비용을 함께 비교한 실험으로 포트폴리오 가치가 큽니다. |
| `미션14_1팀_박시찬` | 연말정산 가이드 기반 RAG, `KoE5` 임베딩, `FAISS`, 근거 기반 응답 | 검색-생성 파이프라인을 하나의 시스템으로 묶은 대표 사례입니다. |

## Concrete Learning Points

### Gemma QLoRA

`Gemma` 실습에서는 4비트 양자화와 `LoRA`를 결합해, 제한된 자원에서도 생성형 모델을 미세조정하는 흐름을 따라갔습니다.  
`BitsAndBytesConfig`, `LoraConfig`, `SFTTrainer`, `merge_and_unload()`까지 한 번에 정리해두어서, 이후 다른 오픈 모델에도 재사용 가능한 템플릿이 되었습니다.

### LangGraph ReAct Agent

이 실습이 좋았던 이유는 라이브러리 사용법만 익힌 것이 아니라, `create_react_agent`의 내부 동작을 `StateGraph`로 다시 구현해봤기 때문입니다.  
도구 호출 여부를 결정하는 router, `tool_calls`를 순회하는 실행 노드, 다시 LLM으로 돌아가는 루프 구조를 이해하면서 에이전트 설계의 기본기를 잡을 수 있었습니다.

### Mission 13: Full Fine-Tuning vs LoRA

쇼핑몰 리뷰 감성 분석 미션에서는 같은 데이터셋으로 `Full Fine-Tuning`과 `LoRA`를 비교했습니다.

| Metric | Full FT | LoRA |
|--------|--------:|-----:|
| Accuracy | 91.02% | 90.32% |
| Macro F1 | 0.8795 | 0.8700 |
| Training Time | 4,916 sec | 3,110 sec |

실습 보고서에는 LoRA가 전체 파라미터의 약 `0.05%`만 업데이트하면서도 정확도 손실을 `0.7%p` 수준으로 방어했다고 정리되어 있습니다.  
즉, 자원 제약이 있는 환경에서 효율적인 선택지를 비교 가능한 숫자로 남겼다는 점이 중요했습니다.

### Mission 14: Grounded RAG

연말정산 가이드 RAG 미션에서는 PDF 문서를 쪼개고, `KoE5` 임베딩으로 벡터화한 뒤, `FAISS` 기반 retriever와 프롬프트 체인을 연결했습니다.  
이 흐름은 LLM이 외부 문서를 근거로 답하게 만드는 가장 기본적인 형태의 검색-생성 시스템이며, 소스 문서를 바탕으로 답변 신뢰성을 확보하려 한 점이 좋았습니다.

## What This Track Says About Me

- 최신 도구를 빠르게 써보는 데서 멈추지 않고, 내부 구조와 비용 구조까지 확인하려는 편입니다.
- LLM 성능 자체보다 검색 품질, 추적 가능성, 파인튜닝 효율, 근거 제시 같은 시스템 속성을 중요하게 봅니다.
- 실습 노트가 많아도 결국 남기고 싶은 것은 "이 기술을 어디에 어떻게 쓸 수 있나"라는 판단 기준입니다.

## Next Experiments

- RAG에 `reranking`과 `evaluation set`을 붙여 검색 품질을 수치화하기
- LangGraph 실습을 실제 워크플로우형 에이전트 프로젝트로 확장하기
- LoRA/QLoRA 비교를 다른 한국어 태스크로 재실험해 재현성 확인하기
