---
title: "Advanced Project"
date: 2026-02-28
excerpt: "제품 이미지와 텍스트 입력으로 광고 크리에이티브를 자동 생성하는 End-to-End AI 파이프라인"
header:
  teaser: /assets/images/profile.png
github_url: "https://github.com/codeitTeam5/SMB_GenMarketingContents"
project_dir: "C:/Users/bhs33/Desktop/project/Advanced_Project"
tech_stack:
  - Python
  - Computer Vision
  - LLM
  - Prompt Engineering
---

## 1) 문제 배경
광고 소재 제작은 기획, 카피 작성, 시각 합성 단계에서 반복 작업이 많고 작업자별 품질 편차가 컸습니다. 이 문제를 줄이기 위해 입력부터 결과물 생성까지 이어지는 자동화 파이프라인이 필요했습니다.

## 2) 목표
- 이미지/텍스트 입력 기반 광고 시안 자동 생성
- 품질 편차를 줄이고 재현 가능한 제작 프로세스 확보
- 팀 협업에 맞는 API 중심 실행 구조 구축

## 3) 핵심 구현
- 입력 전처리, 배경 생성, 카피 생성, 합성 단계를 모듈화한 파이프라인 구성
- 단계별 실패 로그를 수집해 재시도/보정이 가능한 품질 개선 루프 설계
- 서비스 연동을 고려한 API 호출 흐름으로 구성해 확장성 확보

## 4) 트러블슈팅
- 문제: 입력 이미지 품질과 프롬프트 표현 방식에 따라 결과 일관성이 흔들림
- 대응: 전처리 규칙과 프롬프트 템플릿을 표준화하고, 실패 케이스를 기준으로 보정 규칙을 추가
- 효과: 동일 유형 입력에서 결과 안정성이 개선되고 재작업 빈도가 감소

## 5) 성과
- 반복 제작 작업 시간을 단축
- 동일 조건에서 결과를 재생성할 수 있는 기반 확보
- 운영 단계에서 개선 포인트를 추적 가능한 구조 마련

## 6) 링크
- GitHub: [codeitTeam5/SMB_GenMarketingContents](https://github.com/codeitTeam5/SMB_GenMarketingContents)
