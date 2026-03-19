---
title: "코드실습1 1. 파이썬 응용하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807_코드실습1_1. 파이썬 응용하기"
source_path: "11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md"
excerpt: "기타 인코딩 방식 => EUC-KR, CP949"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

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

## What I Worked On

- 1. 모듈 기본 3가지
- (1) time
- strftime() 응용
- 현재 시간 바로 출력
- 현재 시간에서 좀전에 정의한 formatted를 빼주기 (시간끼리 연산 확인)

## Implementation Flow

1. 1. 모듈 기본 3가지
2. (1) time
3. strftime() 응용
4. 현재 시간 바로 출력
5. 현재 시간에서 좀전에 정의한 formatted를 빼주기 (시간끼리 연산 확인)
6. (2) datetime

## Code Highlights

### (2) datetime

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

### 2. 파일 입력과 문자 수정

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
