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

<div class="research-doc-hero">
  <div class="research-doc-hero__meta">
<div class="research-doc-hero__meta-item">
  <span>Source</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Artifacts</span>
  <strong>코드 114 · 실행 61</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>itertools, time, datetime, csv</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">문제 설명 1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">함수 분해와 로직 구성</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">클래스 설계 -&gt; 함수 실습 -&gt; 구현 코드</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">함수 분해와 로직 구성</p>
  <p class="research-note-card__body">함수는 입력, 처리, 반환을 분리해 로직을 재사용하기 쉽게 만들고, 문제를 작은 단위로 나누는 기본 도구입니다.</p>
  <p class="research-note-card__meta">이 글에서는 문제 풀이를 함수 단위로 쪼개고 입출력을 나눠 보는 실습과 연결됩니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-grid">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 클래스 설계</p>
  <p class="research-step-card__title">문제1. 투표 시스템 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 기본 답안</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 함수 실습</p>
  <p class="research-step-card__title">문제1. 시간 관리 프로그램</p>
  <p class="research-step-card__body">입력과 반환값을 분리해 문제 해결 과정을 함수로 정리하는 기초 구현 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 기본 답안 · CSV 파일에서 할 일을 불러오는 함수</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 구현 코드</p>
  <p class="research-step-card__title">문제3. 도서관 관리 시스템</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 도서관 관리 시스템 초기화 · 도서 추가</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 클래스 설계</p>
  <p class="research-step-card__title">문제4. 프랜차이즈 레스토랑 관리 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 기본 답안</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 클래스 설계</p>
  <p class="research-step-card__title">문제4. 프랜차이즈 레스토랑 관리 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 응용 버전 1 - cancel_reservation 추가 · 고객 이름과 예약 일시를 기준으로 해당 예약을 찾아 삭제...</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 클래스 설계</p>
  <p class="research-step-card__title">문제4. 프랜차이즈 레스토랑 관리 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 응용 버전 2 - classmethod 사용 대신 sta... · sum_reservations은 인스턴스를 인자로 받기...</p>
</div>
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

### 문제4. 프랜차이즈 레스토랑 관리 클래스

**직접 해본 단계**: 클래스 설계

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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
