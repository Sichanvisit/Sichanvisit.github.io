---
title: "08 코드실습2 2.객체와 클래스"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807-08_코드실습2_2.객체와 클래스"
source_path: "11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md"
excerpt: "코드실습2 2.객체와 클래스를 중심으로 객체지향 설계, 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코드실습2 2.객체와 클래스를 중심으로 객체지향 설계, 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 은행 클래스, 은행 클래스 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다."
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

<div class="research-doc-hero">
  <div class="research-doc-hero__meta">
<div class="research-doc-hero__meta-item">
  <span>Source</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Artifacts</span>
  <strong>코드 28 · 실행 18</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>Not detected</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">코드실습2 2.객체와 클래스를 중심으로 학습한 내용을 정리한 ML 실습입니다.</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">객체지향 설계 · 함수 분해와 로직 구성</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">클래스 설계 -&gt; 구현 코드 -&gt; 클래스 설계</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">객체지향 설계</p>
  <p class="research-note-card__body">객체지향은 관련 데이터와 동작을 하나의 객체로 묶어 문제를 구조적으로 표현하는 방식입니다.</p>
  <p class="research-note-card__meta">이 글에서는 클래스, 메서드, 상태 관리 같은 코드가 핵심 학습 포인트로 드러납니다.</p>
</div>
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
  <p class="research-step-card__title">은행 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 입금 기능 구현 · 출금 기능 구현</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 구현 코드</p>
  <p class="research-step-card__title">은행 클래스</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 클래스 설계</p>
  <p class="research-step-card__title">은행 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 위의 은행 클래스 init없이 구현 · 입금 기능 구현</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 클래스 설계</p>
  <p class="research-step-card__title">은행 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 실습문제1 상품 클래스 구현하기 문제</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 클래스 설계</p>
  <p class="research-step-card__title">다양한 메소드</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> str메소드</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 클래스 설계</p>
  <p class="research-step-card__title">은행 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 실습2 문제 - 인스턴스 변수 초기화 예외 처리</p>
</div>
</div>

## Code Evidence

### 은행 클래스

**직접 해본 단계**: 클래스 설계

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

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

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

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
