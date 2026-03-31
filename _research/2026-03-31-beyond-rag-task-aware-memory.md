---
title: "Beyond RAG에서 본 다음 단계"
date: 2026-03-31
research_tab: "RAG"
research_kind: "Research Note"
research_summary: "RAG를 더 잘 검색하는 문제를 넘어서, 태스크 단위 메모리와 압축 KV 캐시 관점으로 확장되는 흐름을 정리한 글입니다. 검색 중심 구조의 한계와 언제 이런 관점이 더 유효한지, 제 RAG 설계 관점에 어떤 영향을 줬는지 함께 담았습니다."
research_artifacts: "Beyond RAG · Task-aware Memory · KV Cache"
excerpt: "매 질의마다 문서를 다시 찾는 구조를 넘어서, 태스크 단위 메모리를 미리 준비하는 관점에서 Beyond RAG를 정리했습니다."
tags:
  - rag
  - llm
  - retrieval
  - memory
  - kv-cache
header:
  teaser: /assets/images/research/beyond-rag.svg
---

## Research Snapshot

| Item | Summary |
|------|---------|
| Topic | Beyond RAG, task-aware memory, query-agnostic compressed KV cache |
| Why I Read It | RAG를 더 튜닝하는 방향만으로는 한계가 있다고 느껴, 검색 이후의 구조를 이해하고 싶었습니다. |
| Core Question | 매 질의마다 검색하는 구조 대신, 태스크 단위 메모리를 미리 준비해두는 방식은 언제 더 유리한가? |
| Portfolio Angle | Obsidian RAG를 설계할 때 검색 품질뿐 아니라 “반복 질의에 강한 구조”를 함께 고민하게 만든 메모입니다. |

## Why This Paper Caught My Attention

제가 RAG를 계속 보면서 느낀 가장 큰 한계는 `검색 정확도`만의 문제가 아니었습니다.  
문서가 넓게 흩어져 있거나, 비슷한 질문이 여러 번 반복되거나, 한 번에 조합해야 할 근거가 많아질수록 RAG는 매번 같은 일을 다시 하게 됩니다.

이 글에서 다룬 Beyond RAG는 그런 상황에서 관점을 바꿉니다.

- 질문이 들어올 때마다 문서를 다시 찾는 대신
- 태스크 단위로 미리 압축된 메모리를 준비해두고
- 그 메모리를 바탕으로 여러 질문을 처리하는 방식입니다.

이 지점이 흥미로웠던 이유는, 단순히 “더 잘 검색하는 법”이 아니라 “아예 다른 비용 구조를 만드는 법”으로 읽혔기 때문입니다.

## What I Took Away

### 1. RAG의 병목은 검색 정확도만이 아니다

RAG는 필요한 근거를 잘 찾는 것이 중요하지만, 반복 사용 시에는 검색과 재조립 자체가 비용이 됩니다.

- 같은 문서군에 대해 비슷한 질문이 여러 번 들어오면 같은 retrieval 과정이 반복됩니다.
- 멀티홉 질문에서는 부분적으로 맞는 chunk가 섞여 들어오며 품질이 흔들릴 수 있습니다.
- 답에 필요한 정보가 코퍼스 전체에 넓게 퍼져 있으면 top-k 검색만으로는 회수 자체가 불안정해집니다.

이 글은 RAG를 부정하기보다, `언제 RAG가 구조적으로 불리해지는가`를 더 선명하게 보여줬습니다.

### 2. “문서 검색”이 아니라 “태스크 메모리”로 보는 관점이 필요하다

Beyond RAG에서 인상적이었던 핵심은 query-aware가 아니라 task-aware라는 점이었습니다.

- 질문마다 증거를 새로 찾는 대신
- 태스크 설명과 코퍼스 전체를 바탕으로
- 압축된 KV 캐시를 먼저 만들고
- 이후 질문은 그 캐시를 참조하며 처리합니다.

비유하자면 시험 문제를 받을 때마다 교과서를 다시 뒤지는 것이 아니라, 과목 전체 요약 노트를 먼저 만든 뒤 그 노트로 여러 문제를 푸는 방식에 가깝습니다.

### 3. 결국 중요한 건 “언제 어떤 구조를 택할지”다

이 글을 읽고 난 뒤에는 RAG와 메모리형 구조를 경쟁 관계보다 선택지로 보게 됐습니다.

- 문서가 자주 바뀌고 질문이 산발적이면 여전히 RAG가 유리합니다.
- 같은 태스크 위에서 반복 질의가 많고, 넓게 퍼진 지식을 종합해야 한다면 메모리형 구조가 더 설득력 있습니다.
- 실제 서비스에서는 두 방식을 섞어, 최신성은 retrieval로 보완하고 반복성은 memory/cache로 흡수하는 하이브리드 설계가 현실적입니다.

## How It Changed My Design Thinking

이 글은 제 RAG 프로젝트를 당장 완전히 바꾼 것은 아니지만, 설계 기준을 분명히 바꿨습니다.

이전에는 주로 이런 질문을 했습니다.

- 검색 품질을 어떻게 높일까?
- chunking과 reranking을 어떻게 조정할까?
- query rewriting을 어디에 둘까?

이 글 이후에는 이런 질문도 같이 보기 시작했습니다.

- 같은 코퍼스에 대한 반복 질의를 어떻게 더 싸게 처리할까?
- retrieval과 memory를 어떤 기준으로 나눌까?
- 매번 문서를 다시 읽는 흐름이 정말 최선일까?

즉, 검색 파이프라인만 보는 시선에서 `지식 접근 구조 전체`를 보는 쪽으로 이동했습니다.

## Where I Would Apply This

제가 만든 Obsidian RAG 같은 구조에 바로 적용한다면, 우선 이런 식으로 연결해볼 수 있다고 생각합니다.

- 자주 반복되는 주제별 질의군을 추적해 세션/태스크 단위 요약 메모리로 별도 관리
- raw note 검색과 summary memory를 분리해 서로 다른 역할을 맡기기
- 장기적으로는 검색 결과를 매번 재조합하는 대신, 누적된 작업 맥락을 memory layer로 다루기

아직 직접 구현까지 이어진 것은 아니지만, 단순한 paper review가 아니라 다음 실험 방향을 정해준 글에 가깝습니다.

## Why This Note Belongs in My Portfolio

이 글을 포트폴리오에 남기는 이유는 “최신 논문을 읽었다”를 보여주기 위해서가 아닙니다.

- RAG를 고정된 정답처럼 보지 않고 한계를 구분해서 바라본 점
- retrieval, memory, cost structure를 함께 보는 시각
- 프로젝트 바깥에서도 설계 기준을 계속 업데이트하고 있다는 점

이 세 가지가 제가 지향하는 AI 엔지니어링 방식과 더 맞닿아 있다고 생각했습니다.

## Next Step

다음 단계에서는 이 관점을 실제 구조 실험으로 연결해보고 싶습니다.

- 반복 질의 패턴을 수집해 task-aware memory가 유효한 구간 찾기
- retrieval layer와 memory layer를 분리한 작은 프로토타입 만들기
- “정답률”만이 아니라 latency, token cost, 반복 질의 안정성까지 함께 비교하기
