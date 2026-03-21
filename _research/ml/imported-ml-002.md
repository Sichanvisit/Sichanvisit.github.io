---
title: "코드실습1 1. 파이썬 응용하기"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250807_코드실습1_1. 파이썬 응용하기"
source_path: "11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md"
excerpt: "코드실습1 1"
research_summary: "코드실습1 1. 파이썬 응용하기를 중심으로 구현 중심 학습 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 (2) datetime, 파일 입력과 문자 수정 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 time, datetime, random, google입니다."
research_artifacts: "ipynb/md · 코드 26개 · 실행 25개"
code_block_count: 26
execution_block_count: 25
research_focus:
  - "모듈 기본 3가지"
  - "(1) time"
  - "(2) datetime"
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
  <strong>코드 26 · 실행 25</strong>
</div>
<div class="research-doc-hero__meta-item">
  <span>Libraries</span>
  <strong>time, datetime, random, google</strong>
</div>
  </div>
</div>
<div class="research-doc-grid">
<div class="research-doc-card">
  <p class="research-doc-card__label">Study Topic</p>
  <p class="research-doc-card__value">기타 인코딩 방식 =&gt; EUC-KR, CP949</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Data Context</p>
  <p class="research-doc-card__value">기타 인코딩 방식 =&gt; EUC-KR, CP949</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Core Concepts</p>
  <p class="research-doc-card__value">구현 중심 학습</p>
</div>
<div class="research-doc-card">
  <p class="research-doc-card__label">Implementation Focus</p>
  <p class="research-doc-card__value">피처 가공 -&gt; 구현 코드 -&gt; 구현 코드</p>
</div>
</div>

## What I Studied

<div class="research-note-grid">
<div class="research-note-card">
  <p class="research-note-card__label">구현 중심 학습</p>
  <p class="research-note-card__body">이 글은 개념 설명과 함께 실제 코드를 통해 학습 흐름을 다시 따라가도록 정리된 ML 실습 기록입니다.</p>
  <p class="research-note-card__meta">데이터 입력, 처리, 모델링, 평가 가운데 실제로 손댄 단계를 중심으로 읽을 수 있습니다.</p>
</div>
</div>

## How I Implemented It

<div class="research-step-grid">
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 1 · 피처 가공</p>
  <p class="research-step-card__title">(2) datetime</p>
  <p class="research-step-card__body">원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> timedelta 활용 · 현재 시간</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 2 · 구현 코드</p>
  <p class="research-step-card__title">파일 입력과 문자 수정</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>


</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 3 · 구현 코드</p>
  <p class="research-step-card__title">(1) time</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> strftime() 응용</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 4 · 구현 코드</p>
  <p class="research-step-card__title">(2) datetime</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 실제 시간 연산방법</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 5 · 구현 코드</p>
  <p class="research-step-card__title">(3) random</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> shuffle()</p>
</div>
<div class="research-step-card">
  <p class="research-step-card__kicker">Step 6 · 구현 코드</p>
  <p class="research-step-card__title">파일 입력과 문자 수정</p>
  <p class="research-step-card__body">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</p>

  <p class="research-step-card__meta"><span>코드 포인트</span> 업로드한 파일 읽기</p>
</div>
</div>

## Code Evidence

### (2) datetime

**직접 해본 단계**: 피처 가공

원본 컬럼을 그대로 쓰지 않고 시간 정보나 도메인 규칙을 반영한 파생 변수를 만드는 실습 코드입니다.

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

### 파일 입력과 문자 수정

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cleaned = line.strip()                           # 맨 윗줄과 아랫줄 공백 제거
        fruits = cleaned.split(',')                      # 쉼표 기준 나누기
        fruits = [fruit.strip() for fruit in fruits]    # 각 과일명 공백 제거
        print(fruits)
```

### (1) time

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# strftime() 응용

timestamp = time.time()
local_time = time.localtime(timestamp)
formatted = time.strftime('%Y-%m-%d %H:%M:%S', local_time)

print(formatted)
```

### (2) datetime

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# 실제 시간 연산방법

past_time = datetime.strptime(formatted, '%Y-%m-%d %H:%M:%S')
now = datetime.now()

print(now - past_time)
```

### (3) random

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# shuffle(): 섞기

deck = ['A♠', 'K♣', 'Q♦']
random.shuffle(deck)
print(deck)
```

### 파일 입력과 문자 수정

**직접 해본 단계**: 구현 코드

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
# 업로드한 파일 읽기

with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250807_코드실습1_1. 파이썬 응용하기.md`
- Source formats: `ipynb`, `md`
- Companion files: `250807_코드실습1_1. 파이썬 응용하기.ipynb`, `250807_코드실습1_1. 파이썬 응용하기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 기타 인코딩 방식 => EUC-KR, CP949
