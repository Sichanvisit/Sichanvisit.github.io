---
title: "08 코드실습2 2.객체와 클래스"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807-08_코드실습2_2.객체와 클래스"
source_path: "11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md"
excerpt: "클래스 코드 연습, 은행 클래스, 다양한 메소드 중심으로 구현 과정을 정리한 08 코드실습2 2.객체와 클래스 기록입니다"
research_summary: "클래스 코드 연습, 은행 클래스, 다양한 메소드 중심으로 구현 과정을 정리한 08 코드실습2 2.객체와 클래스 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다."
research_artifacts: "ipynb/md · 코드 28개 · 실행 18개"
code_block_count: 28
execution_block_count: 18
research_focus:
  - "클래스 코드 연습"
  - "은행 클래스"
  - "다양한 메소드"
research_stack: []
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

클래스 코드 연습, 은행 클래스, 다양한 메소드 중심으로 구현 과정을 정리한 08 코드실습2 2.객체와 클래스 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다.

**빠르게 볼 수 있는 포인트**: 클래스 코드 연습, 은행 클래스, 다양한 메소드.

**남겨둔 자료**: `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다.

## Snapshot

| Item | Value |
|------|-------|
| Track | ML |
| Type | Practice |
| Source Files | `ipynb`, `md` |
| Code Blocks | 28 |
| Execution Cells | 18 |
| Libraries | Not detected |
| Source Note | `250807-08_코드실습2_2.객체와 클래스` |

## What This Note Covers

- 클래스 코드 연습
- 은행 클래스
- 다양한 메소드
- Person 클래스 연습
- 두 명 추가하기

## Why This Matters

### 클래스와 객체 모델링

- 왜 필요한가: 코드를 기능별로 나누고 상태를 함께 관리하려면 변수와 함수를 흩어두기보다 객체 단위로 묶는 연습이 필요합니다.
- 왜 이 방식을 쓰는가: 클래스 기반 구조는 같은 패턴의 동작을 여러 인스턴스에 반복 적용하기 쉬워 기초 문법을 실제 코드 구조로 연결하기 좋습니다.
- 원리: 클래스는 속성과 메서드를 묶는 설계도이고, 인스턴스는 그 설계도를 바탕으로 생성된 실제 객체입니다.

## Implementation Flow

1. Key Step: 위의 은행 클래스 init없이 구현
2. Key Step: 실습문제1 상품 클래스 구현하기 문제
3. Key Step: 실습2 문제 - 인스턴스 변수 초기화 예외 처리

## Code Highlights

### 클래스 코드 연습

`클래스 코드 연습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Person 클래스 연습 흐름이 주석과 함께 드러납니다.

```python
# Person 클래스 연습

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello {self.name}')
```

### 은행 클래스

`은행 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 입금 기능 구현, 출금 기능 구현, 이체 기능 구현 흐름이 주석과 함께 드러납니다.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # 입금 기능 구현
    def deposit(self, amount):
        self.balance += amount
        return f'{amount}원이 입금됨. 현재 잔액: {self.balance}원.'

    # 출금 기능 구현
    def withdraw(self, amount):
        if amount > self.balance:
            return '잔액이 부족.'
        self.balance -= amount
        return f'{amount}원이 출금됨. 현재 잔액: {self.balance}원.'

    # 이체 기능 구현
    def transfer(self, target_amount, amount):
        if amount > self.balance:
            return '이체 실패 - 잔액 부족'
        self.balance -= amount
        target_amount.balance += amount
        return (f'{amount}원 {target_amount.owner}님께 이체 완료\n'
                f'내 잔액: {self.balance}원')
```

### 다양한 메소드

`다양한 메소드`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 str메소드 흐름이 주석과 함께 드러납니다.

```python
# __str__메소드

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'Book(title={self.title}, author={self.author}, year={self.year})'

    def __str__(self):
        return f'{self.title} by {self.author} ({self.year})'
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md`
- Source formats: `ipynb`, `md`
- Companion files: `250807-08_코드실습2_2.객체와 클래스.ipynb`, `250807-08_코드실습2_2.객체와 클래스.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
