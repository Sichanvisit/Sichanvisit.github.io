---
title: "08 코드실습2 2.객체와 클래스"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807-08_코드실습2_2.객체와 클래스"
source_path: "11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md"
excerpt: "클래스 코드 연습, 은행 클래스, 다양한 메소드 중심으로 구현 과정을 정리한 08 코드실습2 2.객체와 클래스 기록입니다"
research_summary: "클래스 코드 연습, 은행 클래스, 다양한 메소드 중심으로 구현 과정을 정리한 08 코드실습2 2.객체와 클래스 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다."
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

클래스 코드 연습, 은행 클래스, 다양한 메소드 중심으로 구현 과정을 정리한 08 코드실습2 2.객체와 클래스 기록입니다. 이 글은 개념 요약보다 전처리, 피처 가공, 모델링, 평가 코드를 직접 다시 볼 수 있게 구성한 ML 실습 기록입니다. `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다.

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

## What I Studied

- 클래스 코드 연습
- 은행 클래스
- 다양한 메소드
- Person 클래스 연습
- 두 명 추가하기

## What I Tried in Code

1. 클래스 설계: 은행 클래스
2. 구현 코드: 은행 클래스
3. 클래스 설계: 다양한 메소드

## Code Evidence

### 은행 클래스

**직접 해본 단계**: 클래스 설계

`은행 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 입금 기능 구현, 출금 기능 구현 같은 처리 포인트도 함께 남아 있습니다.

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

### 은행 클래스

**직접 해본 단계**: 구현 코드

`은행 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
a1 = BankAccount()
a1.owner = "장보고"
a1.balance = 10000

a2 = BankAccount()
a2.owner = "이순신"
a2.balance = 5000
```

### 은행 클래스

**직접 해본 단계**: 클래스 설계

`은행 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 위의 은행 클래스 init없이 구현, 입금 기능 구현 같은 처리 포인트도 함께 남아 있습니다.

```python
# 위의 은행 클래스 init없이 구현
class BankAccount:

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

### 은행 클래스

**직접 해본 단계**: 클래스 설계

`은행 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 실습문제1 상품 클래스 구현하기 문제 같은 처리 포인트도 함께 남아 있습니다.

```python
# 실습문제1 상품 클래스 구현하기 문제
class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, amount):
        self.stock += amount
        return f'{amount}개가 추가 되었습니다. 현재 재고: {self.stock}개'

    def info(self):
        return f'{self.name} | 가격: {self.price}원 | 재고: {self.stock}개'

    def sell(self, quantity):
        if quantity > self.stock:
            return '재고 부족'
        self.stock -= quantity
        return f'{quantity}개 판매되었습니다. 남은 재고: {self.stock}'
```

### 다양한 메소드

**직접 해본 단계**: 클래스 설계

`다양한 메소드`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 str메소드 같은 처리 포인트도 함께 남아 있습니다.

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

### 은행 클래스

**직접 해본 단계**: 클래스 설계

`은행 클래스`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다. 코드에는 실습2 문제 - 인스턴스 변수 초기화 예외 처리 같은 처리 포인트도 함께 남아 있습니다.

```python
# 실습2 문제 - 인스턴스 변수 초기화 예외 처리
class Person:
    def __init__(self, name, age, email=None):
        if not (0<= age <= 120):
            raise ValueError("유효한 나이를 입력하세요")
        self.name=name
        self.age=age
        self.email=email or 'unknown@email.com'

    def greet(self):
        print(f"{self.name} ({self.age}세) - {self.email} 님, 안녕하세요!")
```

## Why These Steps Matter

### 클래스로 문제를 쪼개 본 이유

- 왜 필요한가: 상태와 동작이 함께 움직이는 문제는 함수만 나열하기보다 객체 단위로 묶어야 구조가 더 선명해집니다.
- 왜 이 방식을 쓰는가: 이 글에서는 `은행 클래스` 코드를 통해 생성자와 메서드를 어떻게 나눠 문제를 모델링했는지 바로 보이게 했습니다.
- 원리: 클래스는 관련 데이터와 동작을 한 단위로 캡슐화해 재사용성과 확장성을 높여 줍니다.

### 구현 흐름을 코드로 남긴 이유

- 왜 필요한가: 설명만으로는 내가 실제로 어디까지 손댔는지 전달되기 어려워 핵심 구현 코드를 직접 보여줄 필요가 있습니다.
- 왜 이 방식을 쓰는가: 그래서 `은행 클래스` 블록을 포함해 문제를 풀 때 건드린 핵심 로직이 그대로 보이도록 정리했습니다.
- 원리: 코드는 학습한 내용을 실행 가능한 형태로 옮긴 결과물이기 때문에, 가장 직접적인 실습 증거가 됩니다.

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
