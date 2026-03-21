---
title: "코드실습1 1. 파이썬 응용하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807_코드실습1_1. 파이썬 응용하기"
source_path: "11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md"
excerpt: "기타 인코딩 방식 => EUC-KR, CP949"
research_summary: "기타 인코딩 방식 => EUC-KR, CP949. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 time, datetime, random, google입니다."
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

기타 인코딩 방식 => EUC-KR, CP949. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 time, datetime, random, google입니다.

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

## What I Studied

### 파일 입력과 문자 수정

기타 인코딩 방식 => EUC-KR, CP949

### Key Step

현재 시간에서 좀전에 정의한 formatted를 빼주기 (시간끼리 연산 확인)

### Key Step

3시간 45분 전의 시간 계산

## What I Tried in Code

1. 피처 가공: (2) datetime
2. 구현 코드: 파일 입력과 문자 수정
3. 구현 코드: (1) time
4. 구현 코드: (2) datetime
5. 구현 코드: (3) random

## Code Evidence

### (2) datetime

**직접 해본 단계**: 피처 가공

`(2) datetime`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다. 코드에는 timedelta 활용, 현재 시간 같은 처리 포인트도 함께 남아 있습니다.

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

**직접 해본 단계**: 구현 코드

`파일 입력과 문자 수정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cleaned = line.strip()                           # 맨 윗줄과 아랫줄 공백 제거
        fruits = cleaned.split(',')                      # 쉼표 기준 나누기
        fruits = [fruit.strip() for fruit in fruits]    # 각 과일명 공백 제거
        print(fruits)
```

### (1) time

**직접 해본 단계**: 구현 코드

`(1) time`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 strftime() 응용 같은 처리 포인트도 함께 남아 있습니다.

```python
# strftime() 응용

timestamp = time.time()
local_time = time.localtime(timestamp)
formatted = time.strftime('%Y-%m-%d %H:%M:%S', local_time)

print(formatted)
```

### (2) datetime

**직접 해본 단계**: 구현 코드

`(2) datetime`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 실제 시간 연산방법 같은 처리 포인트도 함께 남아 있습니다.

```python
# 실제 시간 연산방법

past_time = datetime.strptime(formatted, '%Y-%m-%d %H:%M:%S')
now = datetime.now()

print(now - past_time)
```

### (3) random

**직접 해본 단계**: 구현 코드

`(3) random`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 shuffle() 같은 처리 포인트도 함께 남아 있습니다.

```python
# shuffle(): 섞기

deck = ['A♠', 'K♣', 'Q♦']
random.shuffle(deck)
print(deck)
```

### 파일 입력과 문자 수정

**직접 해본 단계**: 구현 코드

`파일 입력과 문자 수정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 업로드한 파일 읽기 같은 처리 포인트도 함께 남아 있습니다.

```python
# 업로드한 파일 읽기

with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

## Why These Steps Matter

### 파생 변수를 직접 만든 부분

- 왜 필요한가: 원본 컬럼만으로는 숨겨진 패턴이 잘 드러나지 않아 도메인 정보를 반영한 새 특징이 필요할 때가 많습니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `(2) datetime` 코드를 통해 시간, 범주, 조건식을 어떻게 새로운 feature로 바꿨는지 바로 볼 수 있게 했습니다.
- 원리: 좋은 feature engineering은 데이터 분포를 다시 표현해 모델이 더 유용한 경계나 관계를 학습하도록 돕습니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `파일 입력과 문자 수정` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

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
