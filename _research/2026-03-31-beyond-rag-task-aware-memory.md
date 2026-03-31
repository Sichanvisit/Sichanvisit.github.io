---
title: "Beyond RAG에서 본 다음 단계"
date: 2026-03-31
research_tab: "RAG"
research_kind: "Research Note"
research_summary: "Beyond RAG 논문과 보조 해설을 함께 보며, 검색 중심 RAG가 언제 불리해지고 왜 task-aware memory 관점이 중요해지는지 정리한 글입니다. 주장만 적지 않고, 중간중간 근거 출처를 함께 배치해 제 해석이 어디에서 출발했는지 드러내는 방식으로 다시 썼습니다."
research_artifacts: "Beyond RAG · Task-aware Memory · KV Cache"
excerpt: "RAG의 한계를 말할 때 검색 품질만 볼 것이 아니라, 반복 질의와 넓게 흩어진 지식을 어떤 구조로 다룰지까지 함께 봐야 한다고 느꼈습니다."
tags:
  - rag
  - llm
  - retrieval
  - memory
  - kv-cache
header:
  teaser: /assets/images/research/beyond-rag.svg
---

## 한눈에 보기

제가 이 글을 남긴 이유는 단순히 “최신 논문을 읽었다”를 보여주기 위해서가 아닙니다.  
Obsidian RAG를 계속 다듬으면서, 검색 품질을 높이는 것만으로는 설명되지 않는 병목이 있다고 느꼈고, 그 지점을 `Beyond RAG`가 꽤 명확하게 짚어준다고 봤기 때문입니다.

- 논문 원문: [Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning](https://arxiv.org/abs/2503.04973)
- 빠르게 구조를 파악할 때 함께 본 자료: [Hugging Face Papers 페이지](https://huggingface.co/papers/2503.04973), [Moonlight 리뷰](https://www.themoonlight.io/en/review/beyond-rag-task-aware-kv-cache-compression-for-comprehensive-knowledge-reasoning)

## 1. 왜 이 논문이 눈에 들어왔는가

RAG를 실제로 다뤄보면, 문제는 늘 “검색 정확도” 한 줄로 끝나지 않습니다.

- 문서가 여러 군데 넓게 흩어져 있을 때는 top-k 검색만으로 필요한 근거를 다 회수하기 어렵고
- 같은 코퍼스에 대해 비슷한 질문이 반복되면 retrieval, filtering, prompt reconstruction이 계속 다시 일어나며
- 멀티홉 질문에서는 부분적으로 맞는 조각만 붙어서 답변 품질이 흔들리기 쉽습니다.

이 포인트는 논문 초록과 문제 정의에서 직접 확인할 수 있습니다.  
논문은 기존 방법의 trade-off를 `RAG는 top-ranked evidence 바깥의 정보를 놓칠 수 있고, long-context는 비싸다`는 식으로 정리합니다.

- 근거: [arXiv 초록](https://arxiv.org/abs/2503.04973)
- 보조 설명: [Moonlight 리뷰](https://www.themoonlight.io/en/review/beyond-rag-task-aware-kv-cache-compression-for-comprehensive-knowledge-reasoning)

제가 여기서 얻은 핵심은 이겁니다.  
`RAG를 더 잘 검색하게 만드는 것`과 `매번 다시 검색해야 하는 구조 자체를 다시 보는 것`은 다른 문제라는 점입니다.

## 2. 이 논문이 실제로 바꾸는 관점

이 논문이 흥미로운 이유는 “검색을 더 잘하는 법”보다 “태스크 단위로 메모리를 먼저 만들어두는 법”을 말한다는 데 있습니다.

논문이 제안하는 방향은 대략 이렇게 읽힙니다.

1. 질문마다 문서를 다시 찾지 않습니다.
2. 먼저 태스크 설명과 코퍼스 전체를 바탕으로 압축된 KV 캐시를 만듭니다.
3. 이후 질문은 그 압축된 캐시를 재사용하면서 처리합니다.

논문에서는 이걸 `task-aware`, `query-agnostic` KV cache compression이라고 부릅니다.  
즉, 특정 질문 하나에 맞춘 임시 요약이 아니라, 같은 태스크 안의 여러 질문을 커버할 수 있는 공통 메모리를 만드는 쪽에 가깝습니다.

- 근거: [arXiv 원문](https://arxiv.org/abs/2503.04973)
- 구조 요약 참고: [Hugging Face Papers](https://huggingface.co/papers/2503.04973)
- 메커니즘 해설 참고: [Moonlight 리뷰](https://www.themoonlight.io/en/review/beyond-rag-task-aware-kv-cache-compression-for-comprehensive-knowledge-reasoning)

이걸 제 식으로 다시 표현하면 이렇습니다.

- RAG는 시험 문제를 받을 때마다 교과서를 다시 뒤지는 방식
- Beyond RAG는 과목 전체 요약 노트를 먼저 만들고, 그 노트로 여러 문제를 푸는 방식

이 비유가 마음에 들었던 이유는, retrieval과 memory를 전혀 다른 층위의 선택지로 보게 해주기 때문입니다.

## 3. 숫자로 보면 왜 설득력이 있었는가

논문이 주장만 하고 끝났다면 저는 여기까지 관심을 두지 않았을 겁니다.  
그런데 초록에 실린 결과가 꽤 분명했습니다.

- LongBench v2에서 RAG 대비 정확도 최대 7 absolute points 향상
- 30x compression 조건에서 latency를 0.43s에서 0.16s로 감소

이 수치는 “조금 더 나아졌다”가 아니라,  
`반복 질의와 넓은 문맥을 다뤄야 하는 태스크라면 구조를 바꿀 이유가 있다`는 쪽에 가깝게 읽혔습니다.

- 근거: [arXiv 초록](https://arxiv.org/abs/2503.04973)
- 결과 요약 확인: [Hugging Face Papers](https://huggingface.co/papers/2503.04973)

물론 이걸 곧바로 “RAG는 끝났다”로 읽지는 않았습니다.  
오히려 논문은 어떤 상황에서 task-aware compression이 더 유리한지를 보여준다고 보는 게 맞습니다.

- sparse evidence만 잘 찾으면 되는 태스크는 RAG가 여전히 강할 수 있고
- 넓게 퍼진 지식을 반복적으로 활용해야 하는 태스크는 memory/cache 관점이 더 낫습니다.

이 구분선이 분명해진 것 자체가 제게는 큰 수확이었습니다.

## 4. 이 글이 제 프로젝트 설계에 준 영향

이 메모를 남긴 이유는 paper summary를 만들기 위해서가 아니라, 제 설계 기준이 어떻게 바뀌었는지 기록하기 위해서입니다.

예전에는 주로 이런 질문을 했습니다.

- chunking을 어떻게 조정할까
- reranking을 어디에 둘까
- query rewriting을 어떤 조건에서 쓸까

지금은 이런 질문도 같이 보게 됐습니다.

- 같은 코퍼스에 대한 반복 질의를 어떻게 더 싸게 처리할까
- retrieval layer와 memory layer를 어떤 기준으로 나눌까
- 매번 문서를 다시 읽는 흐름이 정말 최선일까

즉, 검색 파이프라인만 보는 시선에서 `지식 접근 구조 전체`를 보는 쪽으로 이동했습니다.

이건 특히 제가 Obsidian RAG에서 `Summary + Raw` 이중 저장소를 중요하게 보는 이유와도 연결됩니다.  
raw 원문을 그대로 두는 것과 별개로, 반복 질의를 버틸 수 있는 정리된 표현층이 필요하다는 생각이 점점 강해졌기 때문입니다.

## 5. 왜 이 글을 포트폴리오에 남기는가

이 글은 “논문 읽었습니다”가 아니라 아래 세 가지를 보여주는 용도로 남깁니다.

- RAG를 고정된 정답처럼 보지 않고 한계와 적용 구간을 구분해서 본다는 점
- retrieval, latency, token cost, 반복 질의 구조를 함께 본다는 점
- 프로젝트 밖에서도 설계 기준을 계속 업데이트하고 있다는 점

특히 Bytesize 같은 공고를 생각하면, 저는 이 부분이 더 중요하다고 봅니다.  
문서처리형 AI나 RAG 시스템을 만든다는 건 단순 구현보다 `어떤 구조가 언제 유리한가`를 판단하는 일에 더 가깝기 때문입니다.

## 6. 다음에 해보고 싶은 실험

이 관점은 메모로 끝내기보다 실제 구조 실험으로 연결하고 싶습니다.

- 반복 질의 패턴을 모아 task-aware memory가 유효한 구간 찾기
- retrieval layer와 memory layer를 분리한 작은 프로토타입 만들기
- 정답률뿐 아니라 latency, token cost, 반복 질의 안정성까지 함께 비교하기

이 글은 그래서 paper review라기보다, 다음 실험을 정하는 기준점에 더 가깝습니다.

## Sources

- [Beyond RAG: Task-Aware KV Cache Compression for Comprehensive Knowledge Reasoning, arXiv](https://arxiv.org/abs/2503.04973)
- [Hugging Face Papers: Beyond RAG](https://huggingface.co/papers/2503.04973)
- [Moonlight Review: Beyond RAG](https://www.themoonlight.io/en/review/beyond-rag-task-aware-kv-cache-compression-for-comprehensive-knowledge-reasoning)
