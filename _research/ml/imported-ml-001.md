---
title: "08 코드실습2 2.객체와 클래스"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807-08_코드실습2_2.객체와 클래스"
source_path: "11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md"
excerpt: "코드실습2 2.객체와 클래스를 중심으로 객체지향 설계, 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코드실습2 2.객체와 클래스를 중심으로 객체지향 설계, 함수 분해와 로직 구성 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 은행 클래스, 다양한 메소드 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다."
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
  <div class="research-doc-summary">
    <p class="research-doc-summary__label">문제 설정</p>
    <p class="research-doc-summary__body">코드실습2 2.객체와 클래스를 중심으로 학습한 내용을 정리한 ML 실습입니다.</p>
  </div>
  <div class="research-doc-meta">
<div class="research-doc-card">
  <p class="research-doc-card__label">핵심 개념</p>
  <p class="research-doc-card__value">객체지향 설계 · 함수 분해와 로직 구성</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">구현 포인트</p>
  <p class="research-doc-card__value">은행 클래스 · 다양한 메소드 · 클래스 코드 연습</p>
</div>
  </div>
  <div class="research-doc-stats">
<div class="research-doc-stat">
  <span>소스</span>
  <strong>ipynb / md</strong>
</div>
<div class="research-doc-stat">
  <span>자료</span>
  <strong>코드 28 · 실행 18</strong>
</div>
<div class="research-doc-stat">
  <span>주요 스택</span>
  <strong>Not detected</strong>
</div>
  </div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">객체지향 설계</p>
  <p class="research-note-card__body">객체지향은 관련 데이터와 동작을 하나의 객체로 묶어 문제를 구조적으로 표현하는 방식입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 클래스, 메서드, 상태 관리 같은 코드가 핵심 학습 포인트로 드러납니다.</p>
</div>
<div class="research-note-card">
  <p class="research-note-card__label">함수 분해와 로직 구성</p>
  <p class="research-note-card__body">함수는 입력, 처리, 반환을 분리해 로직을 재사용하기 쉽게 만들고, 문제를 작은 단위로 나누는 기본 도구입니다.</p>
  <p class="research-note-card__meta"><span>코드에서 확인한 것</span>이 글에서는 문제 풀이를 함수 단위로 쪼개고 입출력을 나눠 보는 실습과 연결됩니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-list">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 클래스 설계</p>
  <p class="research-step-card__title">은행 클래스</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 입금 기능 구현 · 출금 기능 구현</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 클래스 설계</p>
  <p class="research-step-card__title">다양한 메소드</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> str메소드</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 클래스 설계</p>
  <p class="research-step-card__title">클래스 코드 연습</p>
  <p class="research-step-card__body">문제를 객체 단위로 나눠 상태와 동작을 함께 묶어보는 클래스 설계 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> Person 클래스 연습</p>
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
