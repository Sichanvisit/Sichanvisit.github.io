---
title: "파이썬 응용하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250807_코드실습1_1. 파이썬 응용하기"
source_path: "11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md"
excerpt: "파이썬 응용하기의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 모듈 기본 3가지, 파일 입력과 문자 수정 순서로 큰 장을 먼저 훑고, (1) time, (2) datetime 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과..."
research_summary: "파이썬 응용하기의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 모듈 기본 3가지, 파일 입력과 문자 수정 순서로 큰 장을 먼저 훑고, (1) time, (2) datetime 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 time, datetime, random, google입니다."
research_artifacts: "ipynb/md · 코드 26개 · 실행 25개"
code_block_count: 26
execution_block_count: 25
research_focus:
  - "(2) datetime"
  - "모듈 기본 3가지"
  - "(1) time"
research_stack:
  - "time"
  - "datetime"
  - "random"
  - "google"
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
    <div class="research-overview__value">기타 인코딩 방식 =&gt; EUC-KR, CP949</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">모듈 기본 3가지 -&gt; 파일 입력과 문자 수정</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">특정 데이터셋 설명보다 모듈 기본 3가지, 파일 입력과 문자 수정 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">모듈 기본 3가지 · 파일 입력과 문자 수정</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">(1) time -&gt; (2) datetime -&gt; (3) random</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 26 · 실행 25</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">time, datetime, random, google</div>
  </div>
</div>

## 1. 모듈 기본 3가지

#### 1) time

```python
import time
print(time.time())
```

```python
print("시작:        ", time.time())
time.sleep(0.5)
print("3초 후 출력: ", time.time())
```

```python
t = time.localtime()
print(t.tm_year, "년", t.tm_mon, "월", t.tm_mday, "일")
```

```python
# strftime() 응용

timestamp = time.time()
local_time = time.localtime(timestamp)
formatted = time.strftime('%Y-%m-%d %H:%M:%S', local_time)

print(formatted)
```

```python
# 현재 시간 바로 출력
print(time.strftime('%Y-%m-%d %H:%M:%S'))
```

```python
# 현재 시간에서 좀전에 정의한 formatted를 빼주기 (시간끼리 연산 확인)
print(time.strftime('%Y-%m-%d %H:%M:%S') - formatted)
```

#### 2) datetime

```python
import datetime
print(datetime.datetime.now())
```

```python
# 초의 소숫점 빼기
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
```

```python
# 오늘 날짜만 보기

print(datetime.date.today())
```

```python
# timedelta 활용

from datetime import datetime, timedelta

# 현재 시간
now = datetime.now()
print("현재:          ", now)

# 2일 뒤의 날짜 계산
after_two_days = now +timedelta(days=2)
print("2일 후:        ", after_two_days)

# 3시간 45분 전의 시간 계산
before_time = now - timedelta(hours=3, minutes=45)
print("3시간 45분 전: ", before_time)
```

```python
# 실제 시간 연산방법

past_time = datetime.strptime(formatted, '%Y-%m-%d %H:%M:%S')
now = datetime.now()

print(now - past_time)
```

#### 3) random

```python
import random
random.random()
```

```python
# randint(a, b): a~b 사이 정수

print(random.randint(1,6))
```

```python
# choice(): 무작위 선택

questions = ['Q1', 'Q2', 'Q3']
print(random.choice(questions))
```

```python
# shuffle(): 섞기

deck = ['A♠', 'K♣', 'Q♦']
random.shuffle(deck)
print(deck)
```

```python
deck = ['S', 'A', 'T', 'Q', 'W', 'E']
random.shuffle(deck)
print(deck)
```

```python
# uniform(a, b): a~b사이 임의 실수 생성
value = random.uniform(1.0, 5.0)
print(value)
```

# 2. 파일 입력과 문자 수정

```python
# 파일 업로드해서 불러오기 - 코랩용

from google.colab import files
uploaded = files.upload()
```

```python
# 업로드한 파일 읽기

with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

기타 인코딩 방식
=> EUC-KR, CP949

```python
with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cleaned = line.strip()                           # 맨 윗줄과 아랫줄 공백 제거
        fruits = cleaned.split(',')                      # 쉼표 기준 나누기
        fruits = [fruit.strip() for fruit in fruits]    # 각 과일명 공백 제거
        print(fruits)
```

```python
# 파일 쓰기

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("코랩에서 저장한 텍스트입니다.")
```

```python
# 파일 다운로드
files.download('test.txt')
```

```python
# fruit파일에 내용 추가하기

new_line = "  papaya , pear ,  plum  \n"

with open('sample_fruits.txt', 'a', encoding='utf-8') as f:
    f.write(new_line)
```

```python
# 파일 다운로드
files.download('sample_fruits.txt')
```

#### 구글 드라이브에서 직접 불러오기

```python
path = '/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/sample_fruits.txt'

with open(path, 'r') as f:
    print(f.read())
```

```python

```
