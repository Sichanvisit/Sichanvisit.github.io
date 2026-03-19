---
title: "코드실습1 1. 파이썬 응용하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807_코드실습1_1. 파이썬 응용하기"
source_path: "11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md"
excerpt: "기타 인코딩 방식 => EUC-KR, CP949"
research_summary: "기타 인코딩 방식 => EUC-KR, CP949. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 time, datetime, random, google입니다."
research_artifacts: "ipynb/md · 코드 26개 · 실행 25개"
code_block_count: 26
execution_block_count: 25
research_focus:
  - "모듈 기본 3가지"
  - "(1) time"
  - "(2) datetime"
research_stack:
  - "time"
  - "datetime"
  - "random"
  - "google"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

기타 인코딩 방식 => EUC-KR, CP949. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 time, datetime, random, google입니다.

**빠르게 볼 수 있는 포인트**: 모듈 기본 3가지, (1) time, (2) datetime.

**남겨둔 자료**: `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 time, datetime, random, google입니다.

**주요 스택**: `time`, `datetime`, `random`, `google`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 26 |
| Execution Cells | 25 |
| Libraries | `time`, `datetime`, `random`, `google` |
| Source Note | `250807_코드실습1_1. 파이썬 응용하기` |

## What This Note Covers

### 파일 입력과 문자 수정

기타 인코딩 방식 => EUC-KR, CP949

### Key Step

현재 시간에서 좀전에 정의한 formatted를 빼주기 (시간끼리 연산 확인)

### Key Step

3시간 45분 전의 시간 계산

## Implementation Flow

1. 파일 입력과 문자 수정: 기타 인코딩 방식 => EUC-KR, CP949
2. Key Step: 현재 시간에서 좀전에 정의한 formatted를 빼주기 (시간끼리 연산 확인)
3. Key Step: 3시간 45분 전의 시간 계산

## Code Highlights

### (2) datetime

`(2) datetime`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 timedelta 활용, 현재 시간, 2일 뒤의 날짜 계산 흐름이 주석과 함께 드러납니다.

```python
# timedelta 활용

from datetime import datetime, timedelta

# 현재 시간
now = datetime.now()
print("현재:          ", now)

# 2일 뒤의 날짜 계산
after_two_days = now +timedelta(days=2)
print("2일 후:        ", after_two_days)

# 3시간 45분 전의 시간 계산
before_time = now - timedelta(hours=3, minutes=45)
print("3시간 45분 전: ", before_time)
```

### 파일 입력과 문자 수정

`파일 입력과 문자 수정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 기타 인코딩 방식 => EUC-KR, CP949.

```python
with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cleaned = line.strip()                           # 맨 윗줄과 아랫줄 공백 제거
        fruits = cleaned.split(',')                      # 쉼표 기준 나누기
        fruits = [fruit.strip() for fruit in fruits]    # 각 과일명 공백 제거
        print(fruits)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md`
- Source formats: `ipynb`, `md`
- Companion files: `250807_코드실습1_1. 파이썬 응용하기.ipynb`, `250807_코드실습1_1. 파이썬 응용하기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 기타 인코딩 방식 => EUC-KR, CP949
