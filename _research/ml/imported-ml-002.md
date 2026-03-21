---
title: "코드실습1 1. 파이썬 응용하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807_코드실습1_1. 파이썬 응용하기"
source_path: "11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md"
excerpt: "코드실습1 1"
research_summary: "코드실습1 1. 파이썬 응용하기의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 구현 중심 학습 순서로 큰 장을 먼저 훑고, (2) datetime, 파일 입력과 문자 수정 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 time, datetime, random, google입니다."
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

## 글 한눈에 보기

| 항목 | 내용 |
|------|------|
| 문제 설정 | 기타 인코딩 방식 => EUC-KR, CP949 |
| 원본 구조 | 파일 입력과 문자 수정 |
| 데이터 맥락 | 기타 인코딩 방식 => EUC-KR, CP949 |
| 핵심 주제 | 구현 중심 학습 |
| 구현 흐름 | (2) datetime -> 파일 입력과 문자 수정 -> (1) time |
| 자료 | ipynb / md · 코드 26 · 실행 25 |
| 주요 스택 | time, datetime, random, google |

## 원본 노트 흐름

### 파일 입력과 문자 수정

기타 인코딩 방식 => EUC-KR, CP949

- 읽을 포인트: 하위 구간: 구글 드라이브에서 직접 불러오기

## 구현 흐름

### 1. (2) datetime

- 단계: 피처 가공
- 구현 의도: 원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: timedelta 활용 · 현재 시간

### 2. 파일 입력과 문자 수정

- 단계: 구현 코드
- 구현 의도: 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.
- 핵심 API: -
- 코드 포인트: -

### 3. (1) time

- 단계: 구현 코드
- 구현 의도: 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.
- 핵심 API: -
- 코드 포인트: strftime() 응용

### 4. (3) random

- 단계: 구현 코드
- 구현 의도: 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.
- 핵심 API: -
- 코드 포인트: shuffle()

### 5. 구글 드라이브에서 직접 불러오기

- 단계: 구현 코드
- 구현 의도: 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.
- 핵심 API: -
- 코드 포인트: -

## 코드로 확인한 내용

### (2) datetime

**직접 해본 단계**: 피처 가공

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

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

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# strftime() 응용

timestamp = time.time()
local_time = time.localtime(timestamp)
formatted = time.strftime('%Y-%m-%d %H:%M:%S', local_time)

print(formatted)
```

### (3) random

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# shuffle(): 섞기

deck = ['A♠', 'K♣', 'Q♦']
random.shuffle(deck)
print(deck)
```

### 구글 드라이브에서 직접 불러오기

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
path = '/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/sample_fruits.txt'

with open(path, 'r') as f:
    print(f.read())
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md`
- Source formats: `ipynb`, `md`
- Companion files: `250807_코드실습1_1. 파이썬 응용하기.ipynb`, `250807_코드실습1_1. 파이썬 응용하기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## 원문 미리보기

> 기타 인코딩 방식 => EUC-KR, CP949
