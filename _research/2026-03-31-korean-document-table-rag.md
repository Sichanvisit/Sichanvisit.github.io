---
title: "문서형 RAG에서 표를 다루는 방법"
date: 2026-03-31
research_tab: "Document AI"
research_kind: "Practical Note"
research_summary: "한글 문서와 표 데이터를 RAG에 넣을 때 무엇이 실제로 검색 품질을 좌우하는지, 영상 자료와 LangChain 문서를 함께 보며 정리한 글입니다. HTML을 그대로 밀어 넣는 방식보다 구조를 보존한 변환이 왜 중요한지, 근거 출처를 본문 안에 섞는 방식으로 다시 정리했습니다."
research_artifacts: "HWP · Table Parsing · Markdown Preprocessing"
excerpt: "문서형 RAG에서 표는 작은 디테일이 아니라 검색과 답변 품질을 함께 흔드는 핵심 변수라고 봤습니다."
tags:
  - rag
  - document-ai
  - preprocessing
  - table
  - langchain
header:
  teaser: /assets/images/research/document-rag.svg
---

## 한눈에 보기

문서형 RAG에서 표는 자주 과소평가됩니다.  
하지만 실제로는 문서 로딩, 구조 보존, split 전략, retrieval-friendly representation이 전부 걸려 있는 핵심 요소입니다.

제가 이 글을 다시 쓴 이유는, 원래 정리해둔 영상 메모가 꽤 실무적인 포인트를 담고 있었고, 그 내용을 LangChain 문서와 함께 엮으면 더 설득력 있는 형태가 된다고 봤기 때문입니다.

- 원자료: [한글 문서와 데이터 테이블을 효과적으로 처리하는 기법](https://www.youtube.com/watch?v=AxOIbGo1BKQ)
- LangChain 문서 로더 개요: [Document loaders](https://docs.langchain.com/oss/python/integrations/document_loaders/)
- LangChain HTML 분할: [Split HTML](https://docs.langchain.com/oss/python/integrations/splitters/split_html)
- RAG 튜토리얼: [Build a RAG agent with LangChain](https://docs.langchain.com/oss/python/langchain/rag)
- 레이아웃/표 보존형 파싱 참고: [Docling loader](https://docs.langchain.com/oss/python/integrations/document_loaders/docling/)

## 1. 왜 이 주제가 생각보다 중요했는가

RAG를 다루다 보면 임베딩 모델이나 벡터 DB가 먼저 눈에 들어옵니다.  
그런데 문서형 AI를 실제로 만들수록, 결과를 더 크게 흔드는 건 앞단의 문서 표현 방식이라는 생각이 강해졌습니다.

특히 표가 들어가면 문제가 바로 드러납니다.

- 문단처럼 잘라버리면 행과 열 관계가 사라지고
- HTML을 그대로 넣으면 태그와 공백이 노이즈가 되고
- 지나치게 단순화하면 표의 구조 의미가 사라집니다

영상 메모에서도 바로 이 지점을 짚고 있었습니다.  
한글 문서 안의 표가 일반 텍스트처럼만 읽히면 검색과 답변 품질이 함께 흔들리기 때문에, 표 데이터를 별도의 전처리 대상으로 봐야 한다는 흐름이었습니다.

- 근거: [원자료 영상](https://www.youtube.com/watch?v=AxOIbGo1BKQ)

## 2. 영상 메모에서 가장 실무적으로 느껴진 포인트

원자료에서 제가 제일 중요하게 본 건 “문서 로딩 성공”이 아니라 “표를 RAG 친화적으로 바꾸는 과정”이었습니다.

영상 메모의 핵심은 대략 이렇습니다.

- HWP/HWPX 문서를 로더로 읽어온다
- 문서 내 일부 표는 HTML 구조로 추출된다
- 이 HTML을 그대로 쓰는 대신, 구조를 유지한 더 간결한 표현으로 바꾼다
- 그 결과 토큰 낭비를 줄이고 검색 및 답변 품질을 높인다

특히 `HTML → Markdown` 변환을 강조한 부분이 좋았습니다.  
그냥 예쁘게 보이게 바꾸는 게 아니라, 테이블 구조를 유지하면서도 LLM이 읽기 쉬운 형태로 만드는 방향이었기 때문입니다.

- 근거: [원자료 영상](https://www.youtube.com/watch?v=AxOIbGo1BKQ)

## 3. LangChain 문서와 함께 보니 더 분명해진 것

이 포인트가 단순 팁이 아니라 구조적 선택이라고 느낀 이유는 LangChain 문서와도 잘 맞아떨어졌기 때문입니다.

LangChain은 문서 로더를 `여러 소스의 데이터를 공통된 Document 형식으로 읽어오는 계층`으로 설명합니다.  
즉, 로더 단계는 단순한 파일 읽기가 아니라 이후 split, retrieval, generation의 출발점을 정하는 단계입니다.

- 근거: [LangChain Document loaders](https://docs.langchain.com/oss/python/integrations/document_loaders/)

또 HTML 분할 문서에서는, HTML을 나눌 때 단순 문자열 분할이 아니라 구조 보존이 중요하다고 말합니다.  
특히 `HTMLSemanticPreservingSplitter`는 테이블과 리스트 같은 의미 단위를 보존하는 것이 핵심이라고 설명합니다.

- 근거: [LangChain Split HTML](https://docs.langchain.com/oss/python/integrations/splitters/split_html)

이 두 문서를 같이 놓고 보면, 제가 영상 메모에서 중요하게 본 포인트가 더 선명해집니다.

- 문서 로딩은 시작점일 뿐이고
- 검색 친화적인 표현으로 바꾸는 과정이 필요하며
- 표와 리스트 같은 구조 요소는 별도 의미 단위로 봐야 합니다

## 4. 제가 실제 설계에 연결해서 보는 방식

이런 이유로 저는 문서형 RAG를 볼 때 `raw 그대로 넣기`보다 `표현층을 나누기`를 더 중요하게 봅니다.

예를 들어 문서형 AI를 설계한다면, 저는 대략 이런 순서를 먼저 볼 것 같습니다.

1. 원문 로딩 단계에서 문단, 표, 메타데이터를 분리합니다.
2. 표는 HTML 원본을 그대로 쓰기보다, retrieval-friendly representation으로 변환합니다.
3. 검색용 표현과 근거 제시용 원문을 분리해 저장합니다.
4. 질문 유형에 따라 표 중심 검색과 문단 중심 검색을 다르게 조합합니다.

이건 사실 제가 RAG에서 `Summary + Raw` 이중 저장소를 중요하게 보는 이유와도 연결됩니다.

- raw 원문은 evidence 보존에 강하고
- 정리된 표현은 retrieval 안정성에 유리하며
- 표나 비정형 구조가 많을수록 이 둘을 구분하는 편이 더 낫기 때문입니다

## 5. 왜 “HTML 그대로”보다 “의미를 보존한 단순화”가 낫다고 보는가

이 부분은 제 생각이지만, 영상 메모와 LangChain 문서를 같이 보고 나면 꽤 자연스럽게 이어집니다.

HTML 원본을 그대로 유지하면 좋은 점도 있습니다.  
원래 구조를 최대한 많이 남길 수 있기 때문입니다.

하지만 RAG 관점에서는 단점도 큽니다.

- 태그 자체가 토큰을 차지합니다
- 표의 본질보다 마크업 노이즈가 더 커질 수 있습니다
- 검색 시 유사도 계산이 구조보다 표면 문자열에 더 끌릴 수 있습니다

그래서 중요한 건 “원문을 버리자”가 아니라,  
`원문은 보존하되 검색용 표현은 따로 만들자`에 더 가깝습니다.

이게 문서형 AI에서 전처리를 부가 작업이 아니라 핵심 설계로 보는 이유입니다.

## 6. 왜 이 글을 포트폴리오에 남기는가

이 글은 “유튜브를 봤다”를 보여주기 위해 남기는 게 아닙니다.  
오히려 아래 세 가지를 보여주는 용도에 더 가깝습니다.

- 문서처리형 AI에서 모델보다 문서 표현 방식을 먼저 본다는 점
- 검색 품질 문제를 retrieval tuning만이 아니라 전처리 설계까지 포함해서 본다는 점
- 실무 문서의 어려움이 깔끔한 텍스트보다 표, 비정형 레이아웃, 파일 포맷에 있다는 점을 중요하게 본다는 점

Bytesize 같은 공고 기준으로 보면, 이 글은 제가 `문서처리형 AI`를 단순 키워드가 아니라 실제 구조 문제로 보고 있다는 걸 보여주는 쪽에 더 가깝습니다.

## 7. 다음에 더 실험해보고 싶은 것

이 주제는 메모로 끝내기보다 작게라도 실험해보고 싶은 영역입니다.

- HTML, Markdown, key-value flattening 방식 비교
- 표 전용 chunking 전략 비교
- 표가 많은 문서군에서 hybrid retrieval과 reranking 조합 검증

결국 문서형 RAG의 품질은 모델 선택 하나보다,  
문서를 얼마나 `읽을 수 있는 형태`로 바꾸느냐에서 많이 갈린다고 보고 있습니다.

## Sources

- [원자료 영상: 한글 문서와 데이터 테이블을 효과적으로 처리하는 기법](https://www.youtube.com/watch?v=AxOIbGo1BKQ)
- [LangChain Document loaders](https://docs.langchain.com/oss/python/integrations/document_loaders/)
- [LangChain Split HTML](https://docs.langchain.com/oss/python/integrations/splitters/split_html)
- [Build a RAG agent with LangChain](https://docs.langchain.com/oss/python/langchain/rag)
- [Docling loader](https://docs.langchain.com/oss/python/integrations/document_loaders/docling/)
