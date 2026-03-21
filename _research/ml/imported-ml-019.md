---
title: "1 Python 연습(문제) - AI5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]1_Python_연습(문제) - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md"
excerpt: "Python 연습(문제)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다"
research_summary: "Python 연습(문제)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 함수 분해와 로직 구성 순서로 큰 장을 먼저 훑고, 문제1. 투표 시스템 클래스, 문제1. 시간 관리 프로그램 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다."
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

## 글 한눈에 보기

| 항목 | 내용 |
|------|------|
| 문제 설정 | 심화 문제는 채점에 포함되지 않습니다. 편한 마음으로 도전해 보세요. |
| 원본 구조 | 파이썬 연습 -> 객체와 클래스 -> 심화 문제 |
| 데이터 맥락 | 원본 노트에서 데이터를 설명한 부분을 기준으로 실습 맥락을 정리했습니다. |
| 핵심 주제 | 함수 분해와 로직 구성 |
| 구현 흐름 | 문제1. 투표 시스템 클래스 -> 문제1. 시간 관리 프로그램 -> 문제3. 도서관 관리 시스템 |
| 자료 | ipynb / md · 코드 114 · 실행 61 |
| 주요 스택 | itertools, time, datetime, csv |

## 원본 노트 흐름

### 파이썬 연습

문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요. 함수 설명 print_multiples_of_three(n: int) -> int: - n: 3의 배수를 구하고자 하는 범위의 최대값입니다.

- 읽을 포인트: 하위 구간: 기초(7문제), 기초(7문제) > 문제1. 3의 배수 출력, 기초(7문제) > 문제2. 모음 제거하기

### 객체와 클래스

당신은 여러 지점을 가진 레스토랑 체인의 IT 팀에서 일하며, 각 지점의 예약을 관리하고 중앙에서 예약 현황을 파악할 수 있는 시스템을 개발할 임무를 맡았습니다. 이 시스템은 각 지점의 예약 상황을 관리하고, 고객의 예약 요청을 효과적으로 처리할 수 있는 기능을 제공해야 합니다. ReservationSystem 클래스는 각 레스토랑...

- 읽을 포인트: 하위 구간: 기초(2문제), 기초(2문제) > 문제1. 시간 추적 클래스(TimeTracker), 기초(2문제) > 문제2. 주소록 클래스

### 심화 문제

심화 문제는 채점에 포함되지 않습니다. 편한 마음으로 도전해 보세요.

- 읽을 포인트: 하위 구간: 심화(4문제), 심화(4문제) > 문제1. 시간 관리 프로그램, 심화(4문제) > 문제2. 수학 퍼즐: 소수의 합

## 구현 흐름

### 1. 문제1. 투표 시스템 클래스

- 단계: 클래스 설계
- 구현 의도: 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 기본 답안

### 2. 문제1. 시간 관리 프로그램

- 단계: 함수 실습
- 구현 의도: 입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 기본 답안 · CSV 파일에서 할 일을 불러오는 함수

### 3. 문제3. 도서관 관리 시스템

- 단계: 구현 코드
- 구현 의도: 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.
- 핵심 API: -
- 코드 포인트: 도서관 관리 시스템 초기화 · 도서 추가

### 4. 문제4. 프랜차이즈 레스토랑 관리 클래스

- 단계: 클래스 설계
- 구현 의도: 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 기본 답안

### 5. 문제2. 수학 퍼즐: 소수의 합

- 단계: 함수 실습
- 구현 의도: 입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 에라토스테네스의 체로 구현한 버전 · 소수인지 판별 => 보통 루트값만 확인

### 6. 문제2. 은행 계좌 클래스

- 단계: 클래스 설계
- 구현 의도: 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 기본 답안

## 코드로 확인한 내용

### 문제1. 투표 시스템 클래스

**직접 해본 단계**: 클래스 설계

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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

입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.

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

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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

### 문제2. 수학 퍼즐: 소수의 합

**직접 해본 단계**: 함수 실습

입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.

```python
# 에라토스테네스의 체로 구현한 버전

# 소수인지 판별 => 보통 루트값만 확인
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # √num 까지만 확인
        if num % i == 0:
            return False
    return True

# 에라토스테네스 구현
def sum_of_primes(n):
    if n < 2:
        return 0

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return sum(i for i, prime in enumerate(is_prime) if prime)

# 사용자 입력받고 결과 출력
def main():
    n = int(input("어떤 수까지의 소수의 합을 구하시겠습니까?: "))
    total = sum_of_primes(n)
    print(f"{n} 이하 소수의 합은 {total}입니다.")
```

### 문제2. 은행 계좌 클래스

**직접 해본 단계**: 클래스 설계

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

```python
# 기본 답안
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"{self.account_holder}님의 계좌 {self.account_number}가 개설되었습니다. 초기 잔액: {self.balance:.0f}원")

    def deposit(self, amount: float):
        self.balance += amount
        print(f"{amount:.0f}원이 입금되었습니다. 현재 잔액: {self.balance:.0f}원")

    def withdraw(self, amount: float):
        if self.balance < amount:
            print("잔액이 부족하여 출금할 수 없습니다.")
        else:
            self.balance -= amount
            print(f"{amount:.0f}원이 출금되었습니다. 현재 잔액: {self.balance:.0f}원")

    def get_balance(self):
        return self.balance
```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md`
- Source formats: `ipynb`, `md`
- Companion files: `[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.ipynb`, `[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- External references: `localhost`

## 원문 미리보기

> - **문제 설명** 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.
> - **함수 설명** print_multiples_of_three(n: int) -> int: - n: 3의 배수를 구하고자 하는 범위의 최대값입니다.
