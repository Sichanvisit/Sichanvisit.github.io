---
title: "RAGAS 완벽 가이드: RAG 성능 평가의 표준"
date: 2026-03-05
study_tab: "LLM"
tags:
  - LLM
  - RAG
  - RAGAS
  - Evaluation
  - LLM-as-a-Judge
  - Faithfulness
excerpt: "RAGAS의 핵심 지표와 작동 원리, Python 구현 예시, 운영 단계 활용 전략을 정리합니다."
header:
  teaser: /assets/images/profile.png
---

RAG 시스템에서 가장 어려운 문제는 \"만들기\"보다 \"운영 환경에서 안전한지 검증하기\"입니다.  
RAGAS는 이 검증을 정량화하기 위해 등장한 대표 평가 프레임워크입니다.

## 1. RAGAS란 무엇인가?

RAGAS(RAG Assessment)는 RAG 파이프라인의 검색·생성 품질을 데이터 기반으로 측정하는 평가 프레임워크입니다.

기존 BLEU/ROUGE는 단어 겹침 중심이라,
- 의미는 맞지만 표현이 다르면 저평가
- 표현은 그럴듯하지만 사실과 다르면 고평가
문제가 발생합니다.

RAGAS는 **LLM-as-a-Judge** 접근으로,  
질문·컨텍스트·답변의 논리적 정합성과 근거 기반성을 평가합니다.

## 2. 핵심 지표 4가지

## 2.1 Faithfulness
- 비교 축: 답변 vs 컨텍스트
- 목적: 답변이 검색 근거 안에서만 생성됐는지 확인
- 의미: 할루시네이션 방어 핵심 지표

## 2.2 Answer Relevance
- 비교 축: 답변 vs 질문
- 목적: 답변이 질문 의도를 정확히 충족하는지 평가

## 2.3 Context Precision
- 비교 축: 질문 vs 검색 컨텍스트
- 목적: 검색 결과 상위권에 핵심 문서가 잘 배치되었는지 측정

## 2.4 Context Recall
- 비교 축: 컨텍스트 vs 정답(Ground Truth)
- 목적: 정답에 필요한 정보가 검색 단계에서 누락되지 않았는지 측정

## 3. 내부 작동 방식

RAGAS는 일반적으로 다음 순서로 점수를 산출합니다.

1. 입력 구성: `Q(질문), C(컨텍스트), A(답변), GT(선택)`
2. 평가 프롬프트: 평가용 LLM에 판단 과제 전달
3. 세부 판정 결과를 0~1 스코어로 집계

즉, 단순 문자열 비교가 아니라 \"판단 후 점수화\" 방식입니다.

## 4. Python 구현 예시

```bash
pip install ragas datasets langchain openai
```

```python
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevance, context_precision, context_recall
from datasets import Dataset

data_samples = {
    "question": ["삼성전자의 2023년 영업이익은 얼마인가요?"],
    "answer": ["2023년 영업이익은 약 6조 5,700억 원입니다."],
    "contexts": [[
        "삼성전자는 2023년 연결 기준 영업이익 6조 5670억 원을 기록했다고 발표했다."
    ]],
    "ground_truth": ["6조 5,670억 원"],
}

dataset = Dataset.from_dict(data_samples)

result = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevance, context_precision, context_recall],
)

print(result.to_pandas())
```

## 5. 실무 활용 팁

### 5.1 정답이 없는 운영 환경
Ground Truth가 없어도 `faithfulness`, `answer_relevance`만으로  
서비스 건강도를 지속 모니터링할 수 있습니다.

### 5.2 평가셋 자동 생성
초기 데이터 부족 시 문서 기반 synthetic QA 세트를 생성해  
회귀 테스트 기반을 빠르게 만들 수 있습니다.

### 5.3 비용 최적화
평가도 LLM 호출 비용이 드므로,
- 핵심 샘플 세트(예: 50~100) 고정
- 주기적 배치 평가
- 경량 평가 모델 활용
전략이 필요합니다.

## 6. 운영 관점 결론

RAGAS를 파이프라인에 넣으면 다음이 가능해집니다.

- 모델/리트리버 교체의 객관적 A/B 비교
- 청크 전략·임베딩 변경 영향의 수치 검증
- 할루시네이션 리스크의 조기 탐지

한 줄 요약: **RAGAS는 고품질 RAG 운영을 위한 선택이 아니라 필수 계측 장치입니다.**
