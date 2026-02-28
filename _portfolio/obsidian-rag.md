---
title: "Obsidian RAG"
date: 2026-02-28
excerpt: "Obsidian 노트를 검색증강생성(RAG) 파이프라인으로 연결한 개인 지식 검색 프로젝트"
header:
  teaser: /assets/images/profile.png
github_url: "https://github.com/Sichanvisit/Obsidian_RAG"
project_dir: "C:/Users/bhs33/Desktop/project/Obsidian_RAG"
tech_stack:
  - Python
  - RAG
  - Vector Search
  - LLM
---

## 1) 문제 배경
Obsidian에 축적한 노트 양이 늘어나면서 키워드 검색만으로는 필요한 정보를 빠르게 찾기 어려웠습니다. 질문 의도를 반영해 관련 노트를 찾아 근거 기반으로 답변하는 검색 구조가 필요했습니다.

## 2) 목표
- 자연어 질문 기반 노트 검색 정확도 향상
- 답변과 함께 근거 문맥을 제시해 신뢰성 확보
- 로컬 환경에서 가볍게 운영 가능한 구조 유지

## 3) 핵심 구현
- Obsidian Markdown 노트를 수집하고 메타데이터를 포함해 정제
- 문서를 청크 단위로 분할하고 임베딩을 생성해 벡터 인덱스 구성
- 질의 시 유사도 검색으로 관련 문맥을 추출한 뒤 LLM에 전달하는 RAG 파이프라인 구현
- 프롬프트에 출처 문맥을 포함해 환각을 줄이고 답변 근거를 명확히 표시

## 4) 트러블슈팅
- 문제: 노트 형식 편차(헤더 구조, 코드블록, 링크 밀도) 때문에 청크 품질이 불안정
- 대응: 헤더/코드블록/링크 기준 분할 규칙을 고정하고, 청크 길이/겹침 파라미터를 조정
- 효과: 검색 일관성이 개선되고, 답변의 근거 연결성이 높아짐

## 5) 성과
- 노트 재검색 시간이 단축됨
- 질문-근거-답변 흐름이 명확해져 활용성이 향상됨
- 개인 지식베이스를 지속 확장할 수 있는 구조를 마련함

## 6) 링크
- GitHub: [Sichanvisit/Obsidian_RAG](https://github.com/Sichanvisit/Obsidian_RAG)
