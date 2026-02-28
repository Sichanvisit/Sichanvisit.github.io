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
Obsidian에 축적한 노트 양이 늘어나면서 키워드 검색만으로는 필요한 정보를 빠르게 찾기 어려웠습니다.

## 2) 목표
- 자연어 질문 기반 검색 정확도 향상
- 답변과 근거 문맥을 함께 제시
- 로컬 환경에서 가볍게 운영 가능한 구조 유지

## 3) 핵심 구현
- Markdown 노트 수집/정제
- 청크 분할 + 임베딩 + 벡터 검색
- 검색 문맥을 활용한 RAG 답변 생성

## 4) 성과
- 노트 재검색 시간 단축
- 근거 기반 답변으로 활용성 향상

## 5) 링크
- GitHub: [Sichanvisit/Obsidian_RAG](https://github.com/Sichanvisit/Obsidian_RAG)