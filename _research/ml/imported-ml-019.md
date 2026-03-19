---
title: "1 Python 연습(문제) - AI5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]1_Python_연습(문제) - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md"
excerpt: "문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요"
research_summary: "문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요. 문제 설명 문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 함수를 작성하세요. `md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다."
research_artifacts: "md · 코드 114개 · 실행 61개"
code_block_count: 114
execution_block_count: 61
research_focus:
  - "파이썬 연습"
  - "기초(7문제)"
  - "문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요."
research_stack:
  - "itertools"
  - "time"
  - "datetime"
  - "csv"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - archive-note
---

문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요. 문제 설명 문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 함수를 작성하세요. `md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다.

**빠르게 볼 수 있는 포인트**: 파이썬 연습, 기초(7문제), 문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작....

**남겨둔 자료**: `md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다.

**주요 스택**: `itertools`, `time`, `datetime`, `csv`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 114 |
| Execution Cells | 61 |
| Libraries | `itertools`, `time`, `datetime`, `csv` |
| Source Note | `[스프린트미션]1_Python_연습(문제) - AI5 강사 답안` |

## What This Note Covers

### 문제1. 3의 배수 출력

문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.

### 문제2. 모음 제거하기

문제 설명 문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 함수를 작성하세요.

### 문제3. 수 크기 비교하기

문제 설명 두 개의 숫자를 입력받아, 큰 숫자와 작은 숫자를 각각 반환하는 함수를 작성하세요. (단, 동일한 숫자를 2회 입력하는 경우에는 순서 없이 한 번만 출력되도록 해 주세요.)

### 문제4. 문자열 길이 반환하기

문제 설명 문자열의 길이를 반환하되, 문자열이 빈 문자열이면 “문자열이 비어 있습니다.“를 반환하는 함수를 작성하세요.

## Implementation Flow

1. 문제1. 3의 배수 출력: 문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.
2. 문제2. 모음 제거하기: 문제 설명 문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 함수를 작성하세요.
3. 문제3. 수 크기 비교하기: 문제 설명 두 개의 숫자를 입력받아, 큰 숫자와 작은 숫자를 각각 반환하는 함수를 작성하세요. (단, 동일한 숫자를 2회 입력하는 경우에는 순서 없이 한 번만 출력되도록 해 주세요.)
4. 문제4. 문자열 길이 반환하기: 문제 설명 문자열의 길이를 반환하되, 문자열이 빈 문자열이면 “문자열이 비어 있습니다.“를 반환하는 함수를 작성하세요.

## Code Highlights

### 문제1. 투표 시스템 클래스

`문제1. 투표 시스템 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기본 답안 흐름이 주석과 함께 드러납니다.

```python
# 기본 답안
class VoteSystem:
    def __init__(self):
        self.candidates = {}                                    # 후보자 이름을 키, 투표 수를 값으로 저장하기 위한 딕셔너리

    def add_candidate(self, name):
        if name in self.candidates:
            print(f"{name} 후보는 이미 등록되어 있습니다.")
        else:
            self.candidates[name] = 0
            print(f"{name} 후보가 성공적으로 등록되었습니다.")

    def vote(self, name):
        if name in self.candidates:
            self.candidates[name] += 1
            print(f"{name}에게 투표하였습니다.")
        else:
            print(f"{name} 후보는 등록되어 있지 않습니다.")

    def get_results(self):
        print("투표 결과:")
        for name, count in self.candidates.items():
            if count != 1:
                print(f"{name}: {count} votes")
            else:
                print(f"{name}: {count} vote")

"""
# ... trimmed ...
```

### 문제4. 프랜차이즈 레스토랑 관리 클래스

`문제4. 프랜차이즈 레스토랑 관리 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기본 답안 흐름이 주석과 함께 드러납니다.

```python
# 기본 답안
class ReservationSystem:
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.reservations = []                                    # 각 지점의 예약 목록을 담는 리스트 - 지점별 초기화 가능

    def add_reservation(self, customer_name, date, num_people):
        if not customer_name or not date or num_people <= 0:
            print("잘못된 예약 정보입니다.")
            return
        self.reservations.append({
            "name": customer_name,
            "date": date,
            "num_people": num_people
        })

    def list_reservations(self):
        print(f"{self.branch_name} 예약 목록:")
        if not self.reservations:
            print("현재 예약이 없습니다.")
        else:
            for r in self.reservations:
                print(f"- {r['name']}, {r['date']}, {r['num_people']}명")

    @classmethod
    def sum_reservations(cls, branches):
        total = 0
        for branch in branches:
# ... trimmed ...
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md`
- Source formats: `md`
- Companion files: `[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- External references: `localhost`

## Note Preview

> - **문제 설명** 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.
> - **함수 설명** print_multiples_of_three(n: int) -> int: - n: 3의 배수를 구하고자 하는 범위의 최대값입니다.
