---
title: "2.객체와 클래스"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250807-08_코드실습2_2.객체와 클래스"
source_path: "11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md"
excerpt: "2.객체와 클래스의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 클래스 코드 연습, 은행 클래스, 다양한 메소드 순서로 큰 장을 먼저 훑고, 은행 클래스, 클래스 코드 연습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과..."
research_summary: "2.객체와 클래스의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 클래스 코드 연습, 은행 클래스, 다양한 메소드 순서로 큰 장을 먼저 훑고, 은행 클래스, 클래스 코드 연습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다."
research_artifacts: "ipynb/md · 코드 28개 · 실행 18개"
code_block_count: 28
execution_block_count: 18
research_focus:
  - "은행 클래스"
  - "클래스 코드 연습"
  - "다양한 메소드"
research_stack: []
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

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">2.객체와 클래스에서 클래스 코드 연습, 은행 클래스, 다양한 메소드 흐름을 직접 따라가며 구현했습니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">클래스 코드 연습 -&gt; 은행 클래스 -&gt; 다양한 메소드</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">특정 데이터셋 설명보다 클래스 코드 연습, 은행 클래스, 다양한 메소드 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">클래스 코드 연습 · 은행 클래스 · 다양한 메소드</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">은행 클래스 -&gt; 클래스 코드 연습 -&gt; 다양한 메소드</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 28 · 실행 18</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">미확인</div>
  </div>
</div>

## 원본 노트 흐름

### 클래스 코드 연습

Person 클래스 연습, 두 명 추가하기 같은 코드를 직접 따라가며 클래스 코드 연습 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: Person 클래스 연습, 두 명 추가하기

#### Person 클래스 연습

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

#### 두 명 추가하기

클래스 코드 연습 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

### 은행 클래스

입금 기능 구현, 위의 은행 클래스 init없이 구현, 실습문제1 상품 클래스 구현하기 문제 같은 코드를 직접 따라가며 은행 클래스 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 입금 기능 구현, 위의 은행 클래스 init없이 구현, 실습문제1 상품 클래스 구현하기 문제

#### 입금 기능 구현

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

#### 위의 은행 클래스 init없이 구현

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

#### 실습문제1 상품 클래스 구현하기 문제

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

### 다양한 메소드

str메소드 같은 코드를 직접 따라가며 다양한 메소드 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: str메소드

#### str메소드

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

## 구현 흐름

### 1. 은행 클래스

- 단계: 클래스 설계
- 구현 의도: 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: 입금 기능 구현 · 출금 기능 구현

### 2. 클래스 코드 연습

- 단계: 클래스 설계
- 구현 의도: 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: Person 클래스 연습

### 3. 다양한 메소드

- 단계: 클래스 설계
- 구현 의도: 문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.
- 핵심 API: -
- 코드 포인트: str메소드

## 코드로 확인한 내용

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

### 클래스 코드 연습

**직접 해본 단계**: 클래스 설계

문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.

```python
# Person 클래스 연습

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello {self.name}')
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

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md`
- Source formats: `ipynb`, `md`
- Companion files: `250807-08_코드실습2_2.객체와 클래스.ipynb`, `250807-08_코드실습2_2.객체와 클래스.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## 원문 미리보기

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
