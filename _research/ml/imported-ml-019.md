---
title: "1 Python 연습(문제) - AI5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]1_Python_연습(문제) - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md"
excerpt: "문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요"
research_summary: "문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요. 문제 설명 문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 함수를 작성하세요. `ipynb/md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다."
research_artifacts: "ipynb/md · 코드 114개 · 실행 61개"
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
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - archive-note
---

문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요. 문제 설명 문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 함수를 작성하세요. `ipynb/md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다.

**빠르게 볼 수 있는 포인트**: 파이썬 연습, 기초(7문제), 문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작....

**남겨둔 자료**: `ipynb/md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다.

**주요 스택**: `itertools`, `time`, `datetime`, `csv`

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Archive Note |
| Source Files | `ipynb`, `md` |
| Code Blocks | 114 |
| Execution Cells | 61 |
| Libraries | `itertools`, `time`, `datetime`, `csv` |
| Source Note | `[스프린트미션]1_Python_연습(문제) - AI5 강사 답안` |

## What I Studied

### 문제1. 3의 배수 출력

문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.

### 문제2. 모음 제거하기

문제 설명 문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 함수를 작성하세요.

### 문제3. 수 크기 비교하기

문제 설명 두 개의 숫자를 입력받아, 큰 숫자와 작은 숫자를 각각 반환하는 함수를 작성하세요. (단, 동일한 숫자를 2회 입력하는 경우에는 순서 없이 한 번만 출력되도록 해 주세요.)

### 문제4. 문자열 길이 반환하기

문제 설명 문자열의 길이를 반환하되, 문자열이 빈 문자열이면 “문자열이 비어 있습니다.“를 반환하는 함수를 작성하세요.

## What I Tried in Code

1. 클래스 설계: 문제1. 투표 시스템 클래스
2. 함수 실습: 문제1. 시간 관리 프로그램
3. 구현 코드: 문제3. 도서관 관리 시스템
4. 클래스 설계: 문제4. 프랜차이즈 레스토랑 관리 클래스

## Code Evidence

### 문제1. 투표 시스템 클래스

**직접 해본 단계**: 클래스 설계

`문제1. 투표 시스템 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 기본 답안 같은 처리 포인트도 함께 남아 있습니다.

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
위의 get_result 간단하게 바꾼 버전
    def get_results(self):
        print("투표 결과:")
        for name, count in self.candidates.items():
            print(f"{name}: {count} vote{'s' if count != 1 else ''}")
"""
```

### 문제1. 시간 관리 프로그램

**직접 해본 단계**: 함수 실습

`문제1. 시간 관리 프로그램`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다. 코드에는 기본 답안, CSV 파일에서 할 일을 불러오는 함수 같은 처리 포인트도 함께 남아 있습니다.

```python
# 기본 답안

import csv

# CSV 파일에서 할 일을 불러오는 함수
def load_tasks(filename):
    tasks = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task_name = row['할일']
            duration = int(row['소요시간'])
            tasks.append((task_name, duration))
    return tasks

# 남은 시간 내에서 가능한 할 일을 추천하는 함수
def suggest_tasks(tasks, remaining_time):
    # 소요 시간이 짧은 순으로 정렬
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    selected = []
    total_time = 0

    for task, time in sorted_tasks:
        if total_time + time <= remaining_time:
            selected.append((task, time))
            total_time += time
        else:
            break

    return selected

# 프로그램 실행 함수
def main():
    filename = input("할 일 CSV 파일 경로를 입력하세요: ")
    tasks = load_tasks(filename)

# ... trimmed ...
```

### 문제3. 도서관 관리 시스템

**직접 해본 단계**: 구현 코드

`문제3. 도서관 관리 시스템`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다. 코드에는 도서관 관리 시스템 초기화, 도서 추가 같은 처리 포인트도 함께 남아 있습니다.

```python
      # 도서관 관리 시스템 초기화
      library_system = LibraryManagement()

      # 도서 추가
      library_system.add_book("1984", "조지 오웰", 1949, "978-0451524935")
      library_system.add_book("앵무새 죽이기", "하퍼 리", 1960, "978-0446310789")
      print()

      # 회원 등록
      library_system.add_member("홍길동")
      print()

      # 도서 대여
      library_system.rent_book("978-0451524935", "홍길동")
      print()

      # 도서 정보 출력
      library_system.print_books()
      print()

      # 회원 정보 출력
      library_system.print_members()

      # 도서 반납
      library_system.return_book("978-0451524935", "홍길동")
      print()

      # 회원 정보 출력
      library_system.print_members()
```

### 문제4. 프랜차이즈 레스토랑 관리 클래스

**직접 해본 단계**: 클래스 설계

`문제4. 프랜차이즈 레스토랑 관리 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 기본 답안 같은 처리 포인트도 함께 남아 있습니다.

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
            total += len(branch.reservations)
        return total


    """
    클래스 메소드 간단 버전
    def sum_reservations(cls, branches):
        total = sum(len(branch.reservations) for branch in branches)
# ... trimmed ...
```

### 문제4. 프랜차이즈 레스토랑 관리 클래스

**직접 해본 단계**: 클래스 설계

`문제4. 프랜차이즈 레스토랑 관리 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 응용 버전 1 - cancel_reservation 추가, 고객 이름과 예약 일시를 기준으로 해당 예약을 찾아 삭제... 같은 처리 포인트도 함께 남아 있습니다.

```python
# 응용 버전 1 - cancel_reservation 추가
class ReservationSystem:
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.reservations = []

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

    # 고객 이름과 예약 일시를 기준으로 해당 예약을 찾아 삭제하는 함수 정의
    def cancel_reservation(self, customer_name, date):
        original_count = len(self.reservations)
        self.reservations = [
            r for r in self.reservations
            if not (r["name"] == customer_name and r["date"] == date)
        ]
        if len(self.reservations) < original_count:
            print(f"{customer_name}님의 예약이 취소되었습니다.")
        else:
            print("해당 예약을 찾을 수 없습니다.")

# ... trimmed ...
```

### 문제4. 프랜차이즈 레스토랑 관리 클래스

**직접 해본 단계**: 클래스 설계

`문제4. 프랜차이즈 레스토랑 관리 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 응용 버전 2 - classmethod 사용 대신 sta..., sum_reservations은 인스턴스를 인자로 받기... 같은 처리 포인트도 함께 남아 있습니다.

```python
# 응용 버전 2 - classmethod 사용 대신 staticmethod 사용
# sum_reservations은 인스턴스를 인자로 받기 때문에 클래스 변수에 접근하지 않음 — 사실 staticmethod로도 충분
class ReservationSystem:
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.reservations = []

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

    def cancel_reservation(self, customer_name, date):
        original_count = len(self.reservations)
        self.reservations = [
            r for r in self.reservations
            if not (r["name"] == customer_name and r["date"] == date)
        ]
        if len(self.reservations) < original_count:
            print(f"{customer_name}님의 예약이 취소되었습니다.")
        else:
            print("해당 예약을 찾을 수 없습니다.")

# ... trimmed ...
```

## Why These Steps Matter

### 클래스로 문제를 쪼개 본 이유

- 왜 필요한가: 상태와 동작이 함께 움직이는 문제는 함수만 나열하기보다 객체 단위로 묶어야 구조가 더 선명해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `문제1. 투표 시스템 클래스` 코드를 통해 생성자와 메서드를 어떻게 나눠 문제를 모델링했는지 바로 보이게 했습니다.
- 원리: 클래스는 관련 데이터와 동작을 한 단위로 캡슐화해 재사용성과 확장성을 높여 줍니다.

### 함수 단위로 연습한 이유

- 왜 필요한가: 기초 문제 풀이도 입력, 처리, 반환을 함수로 분리해 봐야 로직을 재사용하고 테스트하기 쉬워집니다.
- 왜 이 방식을 쓰는가: 그래서 `문제1. 시간 관리 프로그램` 같은 코드를 앞쪽에 두고, 문제 해결 흐름이 함수 단위로 어떻게 정리됐는지 보여주도록 만들었습니다.
- 원리: 함수는 반복되는 로직을 한 번 정의해 여러 입력에 적용할 수 있게 하며, 문제를 작은 단위로 나누는 기본 도구입니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `문제3. 도서관 관리 시스템` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md`
- Source formats: `ipynb`, `md`
- Companion files: `[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.ipynb`, `[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- External references: `localhost`

## Note Preview

> - **문제 설명** 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.
> - **함수 설명** print_multiples_of_three(n: int) -> int: - n: 3의 배수를 구하고자 하는 범위의 최대값입니다.
