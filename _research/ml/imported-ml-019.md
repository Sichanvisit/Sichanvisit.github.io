---
title: "1 Python 연습(문제) - AI5 강사 답안"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]1_Python_연습(문제) - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md"
excerpt: "Python 연습(문제)를 중심으로 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "Python 연습(문제)를 중심으로 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 문제1. 투표 시스템 클래스, 문제1. 시간 관리 프로그램 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다."
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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>원본 노트에서 데이터를 설명한 부분을 기준으로 실습 맥락을 정리했습니다.</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>함수 분해와 로직 구성</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>문제1. 투표 시스템 클래스 -&gt; 문제1. 시간 관리 프로그램 -&gt; 문제3. 도서관 관리 시스템</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 114 · 실행 61</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>itertools, time, datetime, csv</td>
    </tr>
    </tbody>
  </table>
</div>

## What I Studied

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--notes">
    <thead>
      <tr>
        <th>개념</th>
        <th>핵심 설명</th>
        <th>코드에서 확인한 것</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">함수 분해와 로직 구성</th>
      <td>함수는 입력, 처리, 반환을 분리해 로직을 재사용하기 쉽게 만들고, 문제를 작은 단위로 나누는 기본 도구입니다.</td>
      <td>이 글에서는 문제 풀이를 함수 단위로 쪼개고 입출력을 나눠 보는 실습과 연결됩니다.</td>
    </tr>
    </tbody>
  </table>
</div>

## How I Implemented It

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--steps">
    <thead>
      <tr>
        <th>단계</th>
        <th>구현 내용</th>
        <th>핵심 API</th>
        <th>코드 포인트</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">Step 1 · 클래스 설계</th>
      <td>
        <strong class="research-compact-table__main">문제1. 투표 시스템 클래스</strong>
        <span class="research-compact-table__sub">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>기본 답안</td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 함수 실습</th>
      <td>
        <strong class="research-compact-table__main">문제1. 시간 관리 프로그램</strong>
        <span class="research-compact-table__sub">입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>기본 답안 · CSV 파일에서 할 일을 불러오는 함수</td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 구현 코드</th>
      <td>
        <strong class="research-compact-table__main">문제3. 도서관 관리 시스템</strong>
        <span class="research-compact-table__sub">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>도서관 관리 시스템 초기화 · 도서 추가</td>
    </tr>
    <tr>
      <th scope="row">Step 4 · 클래스 설계</th>
      <td>
        <strong class="research-compact-table__main">문제4. 프랜차이즈 레스토랑 관리 클래스</strong>
        <span class="research-compact-table__sub">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>기본 답안</td>
    </tr>
    <tr>
      <th scope="row">Step 5 · 함수 실습</th>
      <td>
        <strong class="research-compact-table__main">문제2. 수학 퍼즐: 소수의 합</strong>
        <span class="research-compact-table__sub">입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>에라토스테네스의 체로 구현한 버전 · 소수인지 판별 =&gt; 보통 루트값만 확인</td>
    </tr>
    <tr>
      <th scope="row">Step 6 · 클래스 설계</th>
      <td>
        <strong class="research-compact-table__main">문제2. 은행 계좌 클래스</strong>
        <span class="research-compact-table__sub">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>기본 답안</td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

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
