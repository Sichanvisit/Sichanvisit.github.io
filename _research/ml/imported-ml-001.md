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

<!-- #region id="OxonTeN0q4QC" -->
# 1. 클래스 코드 연습
<!-- #endregion -->

```python id="UdH_yuIFqxAF"
# Person 클래스 연습

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello {self.name}')
```

```python id="eNggF_tjrjKC"
human1 = Person('Jonh', 25)
```

```python colab={"base_uri": "https://localhost:8080/"} id="bvx2fZsfrrVZ" executionInfo={"status": "ok", "timestamp": 1754555942633, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3f393cb3-b9ff-4abf-97dc-0763c5c747bb"
human1.greet()
```

```python id="WddATN2Jru-y"
# 두 명 추가하기
p1 = Person('Alice', 30)
p2 = Person('Bob', 40)
```

```python colab={"base_uri": "https://localhost:8080/"} id="f8Krby3osSrq" executionInfo={"status": "ok", "timestamp": 1754556097618, "user_tz": -540, "elapsed": 75, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2f95fe06-ac9d-4f4a-a6db-1fd43e5bfb7a"
p1.greet()
p2.greet()
```

<!-- #region id="pNDBiPazsaOy" -->
# 2. 은행 클래스
<!-- #endregion -->

```python id="oTDsq6EfsWL8"
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

```python colab={"base_uri": "https://localhost:8080/"} id="ecJq5jQlyGIq" executionInfo={"status": "ok", "timestamp": 1754557795668, "user_tz": -540, "elapsed": 26, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2fc13536-6c22-4754-ac20-4a51a1b3afb7"
a1 = BankAccount('홍길동')
print(a1.deposit(10000))
```

```python colab={"base_uri": "https://localhost:8080/", "height": 35} id="zr2jZ-YdyQMc" executionInfo={"status": "ok", "timestamp": 1754557796645, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e916569e-5dc9-438a-ff1b-4d702148f83c"
a1.withdraw(3000)
```

```python colab={"base_uri": "https://localhost:8080/"} id="p_tKOGu3yW3R" executionInfo={"status": "ok", "timestamp": 1754557798089, "user_tz": -540, "elapsed": 25, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a09d28eb-68ee-4755-f704-a7ff34e45bb9"
a2 = BankAccount('이순신')
print(a2.deposit(5000))
```

```python colab={"base_uri": "https://localhost:8080/", "height": 35} id="o6O7xbLhygsh" executionInfo={"status": "ok", "timestamp": 1754557799646, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ac759f01-b334-4d40-b76d-0112edbd2733"
a2.withdraw(30000)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 35} id="_SJO6Vdeyj4O" executionInfo={"status": "ok", "timestamp": 1754557800411, "user_tz": -540, "elapsed": 26, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a6898bdd-ffc6-47f6-e652-2bc7deb2f12b"
a1.transfer(a2, 3000)
```

```python id="qB_nsm74yvfH"
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

```python colab={"base_uri": "https://localhost:8080/", "height": 163} id="8wRFisimzGMV" executionInfo={"status": "error", "timestamp": 1754557887951, "user_tz": -540, "elapsed": 127, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="897cf9a8-837d-4cf2-b9d4-c4c8f5a59805"
a1 = BankAccount('홍길동', 10000)
print(a1.deposit(10000))
```

```python id="8WN21LeizVO_"
a1 = BankAccount()
a1.owner = "장보고"
a1.balance = 10000

a2 = BankAccount()
a2.owner = "이순신"
a2.balance = 5000
```

```python colab={"base_uri": "https://localhost:8080/", "height": 35} id="Qjl-4mK3zczm" executionInfo={"status": "ok", "timestamp": 1754557978758, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7b1f9474-2faa-43cb-882d-cf60fda72bbc"
a1.deposit(3000)
```

```python id="YKwxkinqzgdF"
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

```python id="SM0I5oCG2n_7"
x = Product('사과', 800)
y = Product('바나나', 2000)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 35} id="qBbuSZVT2wf-" executionInfo={"status": "ok", "timestamp": 1754558837905, "user_tz": -540, "elapsed": 28, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="22754e6a-a17d-46fe-8617-28c0e3fd8f92"
y.restock(20)
```

```python id="Kk904hNu2zMw"
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

```python colab={"base_uri": "https://localhost:8080/", "height": 270} id="R8YAaP1_6Kvg" executionInfo={"status": "error", "timestamp": 1754559824206, "user_tz": -540, "elapsed": 33, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="59ea5195-ffab-48e5-90be-39468fb06d45"
p1 = Person('Alice', 1000)
```

```python colab={"base_uri": "https://localhost:8080/"} id="2DUxnONl6Qq1" executionInfo={"status": "ok", "timestamp": 1754559825226, "user_tz": -540, "elapsed": 43, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5ba95d20-ebd5-41ce-aac3-109b6695311f"
p2 = Person('Bob', 50)
print(p2.greet())
```

<!-- #region id="h7CUb6GmCX7s" -->
# 3. 다양한 메소드
<!-- #endregion -->

```python id="igPgxHpp6cCz" executionInfo={"status": "ok", "timestamp": 1754612498270, "user_tz": -540, "elapsed": 25, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
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

```python id="l1bLwBM7Df3n" executionInfo={"status": "ok", "timestamp": 1754612544472, "user_tz": -540, "elapsed": 6, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
book1 = Book("노인과 바다", "헤밍웨이", "1952")
book2 = Book("소년이 온다", "한강", "2014")
```

```python colab={"base_uri": "https://localhost:8080/"} id="oRvNqtk3DrKw" executionInfo={"status": "ok", "timestamp": 1754612567839, "user_tz": -540, "elapsed": 45, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bef447a7-6294-4971-cac3-32dbd534d6be"
print(repr(book1))
print(str(book2))
```

```python colab={"base_uri": "https://localhost:8080/"} id="ED0VFiAbDw31" executionInfo={"status": "ok", "timestamp": 1754612583757, "user_tz": -540, "elapsed": 174, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bfa8d046-625d-44ff-dd5a-042676a10b8d"
print(book1)
print(book2)
```

```python colab={"base_uri": "https://localhost:8080/"} id="DJXDKAo2D0sy" executionInfo={"status": "ok", "timestamp": 1754612601484, "user_tz": -540, "elapsed": 48, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="13ca3a28-0cf7-4e9c-81dd-71ec9bd06209"
book1
```

```python id="a2wgIntCD5Er" executionInfo={"status": "ok", "timestamp": 1754612608516, "user_tz": -540, "elapsed": 16, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="1f153e10-7029-415d-e401-e4141c57c5eb" colab={"base_uri": "https://localhost:8080/"}
book2
```

```python id="f9wH3bwPD6zd"

```
