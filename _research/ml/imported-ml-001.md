---
title: "2.객체와 클래스"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250807-08_코드실습2_2.객체와 클래스"
source_path: "11_Machine_Learning/Code_Snippets/250807-08_코드실습2_2.객체와 클래스.md"
excerpt: "2.객체와 클래스의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 클래스 코드 연습, 은행 클래스, 다양한 메소드 순서로 큰 장을 먼저 훑고, 클래스 코드 연습, 은행 클래스 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과..."
research_summary: "2.객체와 클래스의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 클래스 코드 연습, 은행 클래스, 다양한 메소드 순서로 큰 장을 먼저 훑고, 클래스 코드 연습, 은행 클래스 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 28개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다."
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
    <div class="research-overview__value">클래스 코드 연습 -&gt; 은행 클래스 -&gt; 다양한 메소드</div>
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

# 1. 클래스 코드 연습

```python
# Person 클래스 연습

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello {self.name}')
```

```python
human1 = Person('Jonh', 25)
```

```python
human1.greet()
```

```python
# 두 명 추가하기
p1 = Person('Alice', 30)
p2 = Person('Bob', 40)
```

```python
p1.greet()
p2.greet()
```

# 2. 은행 클래스

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

```python
a1 = BankAccount('홍길동')
print(a1.deposit(10000))
```

```python
a1.withdraw(3000)
```

```python
a2 = BankAccount('이순신')
print(a2.deposit(5000))
```

```python
a2.withdraw(30000)
```

```python
a1.transfer(a2, 3000)
```

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

```python
a1 = BankAccount('홍길동', 10000)
print(a1.deposit(10000))
```

```python
a1 = BankAccount()
a1.owner = "장보고"
a1.balance = 10000

a2 = BankAccount()
a2.owner = "이순신"
a2.balance = 5000
```

```python
a1.deposit(3000)
```

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

```python
x = Product('사과', 800)
y = Product('바나나', 2000)
```

```python
y.restock(20)
```

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

```python
p1 = Person('Alice', 1000)
```

```python
p2 = Person('Bob', 50)
print(p2.greet())
```

# 3. 다양한 메소드

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

```python
book1 = Book("노인과 바다", "헤밍웨이", "1952")
book2 = Book("소년이 온다", "한강", "2014")
```

```python
print(repr(book1))
print(str(book2))
```

```python
print(book1)
print(book2)
```

```python
book1
```

```python
book2
```

```python

```
