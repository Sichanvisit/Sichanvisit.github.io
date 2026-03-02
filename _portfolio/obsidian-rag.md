---
title: "Obsidian RAG"
date: 2026-02-28
priority: 3
excerpt: "Obsidian 노트를 Summary+Raw 2계층 RAG와 하이브리드 검색으로 연결해, 질문-근거-답변 흐름을 만든 개인 지식 검색 프로젝트"
header:
  teaser: /assets/images/profile.png
github_url: "https://github.com/Sichanvisit/Obsidian_RAG"
project_dir: "C:/Users/bhs33/Desktop/project/Obsidian_RAG"
tech_stack:
  - Python
  - FastAPI
  - Streamlit
  - ChromaDB
  - RAG
  - BM25
---

## TL;DR
- Obsidian에 쌓인 노트를 키워드 검색이 아니라 질문 기반으로 찾고, 근거와 함께 답변하도록 만든 RAG 시스템입니다.
- Summary DB + Raw DB를 함께 쓰는 2계층 검색 구조로, 빠른 탐색과 원문 근거 확인을 동시에 노렸습니다.
- FastAPI 스트리밍 백엔드와 Streamlit UI를 연결해 실제 사용 가능한 형태로 구현했습니다.

## 1) 문제와 목표
### 문제
- 노트 수가 많아지면서 키워드 검색만으로는 필요한 정보를 빠르게 찾기 어려웠습니다.
- 답변이 나와도 어떤 노트에서 근거를 가져왔는지 확인하기 번거로웠습니다.

### 목표
- 자연어 질문으로 검색하고, 근거 문서와 함께 답변하기
- 속도와 정확도 사이 균형을 위해 검색 단계를 분리하기
- 로컬 환경에서 가볍게 실행 가능한 워크플로우 유지하기

## 2) 해결 방식 (Pipeline)
1. 노트 수집/인덱싱: Obsidian Markdown을 수집해 벡터 DB를 구성
2. 검색 1차: 임베딩 검색 + BM25를 결합한 하이브리드 검색
3. 검색 2차: RRF(Reciprocal Rank Fusion)로 결과를 합성/정렬
4. 근거 보강: Summary 문서의 링크를 따라 Raw 문서를 추가 수집
5. 답변 생성: 근거 문맥 기반으로 답변을 생성하고 스트리밍 전송
6. 검증/종료: 중복/품질 점검 + 사용자 중단 신호 처리

## 3) 구현 포인트
- **2계층 검색 구조**: Summary로 빠르게 후보를 찾고 Raw로 근거를 보강
- **하이브리드 검색**: 임베딩 검색이 실패해도 BM25로 fallback 가능
- **프로젝트 힌트 필터링**: 질문/프로젝트명 기반으로 관련 문서 우선 검색
- **실사용 UX**: `/api/chat/stream` 스트리밍 응답, `/api/chat/stop` 중단 API 제공

## 4) 트러블슈팅
- 인코딩 혼선: `utf-8 / utf-8-sig / cp949 / euc-kr` 순서로 안전 읽기 처리
- 임베딩 모델 로딩 실패: 임베딩 비활성화 후 텍스트 기반 검색 fallback
- 장문 생성 반복: 중복 감지 및 후처리 루틴으로 반복 응답 완화

## 5) 결과
- 정성적 성과:
  - 노트 탐색 시간을 줄이고, 질문-근거-답변 흐름을 일관되게 구성
  - 단순 검색 도구가 아니라 "근거 중심 응답기" 형태로 개선
- 정량 지표:
  - 현재 개인 사용 기준으로 검증 중이며, 응답시간/정확도 지표를 추가 정리 예정

## 6) 회고와 다음 단계
- 현재 한계: 개인 Vault 구조에 최적화된 룰이 일부 포함되어 범용성이 낮음
- 다음 개선:
  - 평가셋 기반 검색 품질 지표화
  - 프로젝트별 인덱스 분리 전략 고도화
  - UI에서 근거 문서 하이라이트/비교 뷰 제공

## Links
- GitHub: [Sichanvisit/Obsidian_RAG](https://github.com/Sichanvisit/Obsidian_RAG)
