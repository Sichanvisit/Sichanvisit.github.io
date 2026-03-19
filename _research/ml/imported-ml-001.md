---
title: "08 코드실습2 2.객체와 클래스"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807-08_코드실습2_2.객체와 클래스"
source_path: "11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md"
excerpt: "ML Practice: 1. 클래스 코드 연습, 2. 은행 클래스, 3. 다양한 메소드"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

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

## What I Worked On

- 1. 클래스 코드 연습
- Person 클래스 연습
- 두 명 추가하기
- 2. 은행 클래스
- 위의 은행 클래스 init없이 구현

## Implementation Flow

1. 1. 클래스 코드 연습
2. Person 클래스 연습
3. 두 명 추가하기
4. 2. 은행 클래스
5. 위의 은행 클래스 init없이 구현
6. 실습문제1 상품 클래스 구현하기 문제

## Code Highlights

### 2. 은행 클래스

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

### 2. 은행 클래스

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

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md`
- Source formats: `ipynb`, `md`
- Companion files: `250807-08_코드실습2_2.객체와 클래스.ipynb`, `250807-08_코드실습2_2.객체와 클래스.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
