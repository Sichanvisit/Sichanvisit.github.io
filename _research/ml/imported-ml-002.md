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

<!-- #region id="IDuwt4OJ62k4" -->
## 1. 모듈 기본 3가지
<!-- #endregion -->

<!-- #region id="mTcWSWei664W" -->
#### (1) time
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="lGMtBTq86rst" executionInfo={"status": "ok", "timestamp": 1754543309478, "user_tz": -540, "elapsed": 40, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4b5766bf-7cfd-42e4-883a-4aae8be12f47"
import time
print(time.time())
```

```python colab={"base_uri": "https://localhost:8080/"} id="VylInxOv7i21" executionInfo={"status": "ok", "timestamp": 1754543475381, "user_tz": -540, "elapsed": 504, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6682aa3f-2183-4489-f780-58ede2b250ad"
print("시작:        ", time.time())
time.sleep(0.5)
print("3초 후 출력: ", time.time())
```

```python colab={"base_uri": "https://localhost:8080/"} id="TogVd8tf77rR" executionInfo={"status": "ok", "timestamp": 1754543459070, "user_tz": -540, "elapsed": 47, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6082fbc4-7429-4ef5-d31e-734770fc182a"
t = time.localtime()
print(t.tm_year, "년", t.tm_mon, "월", t.tm_mday, "일")
```

```python colab={"base_uri": "https://localhost:8080/"} id="LY0jG8HS8Jc1" executionInfo={"status": "ok", "timestamp": 1754543623855, "user_tz": -540, "elapsed": 35, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ddd7c394-6451-4589-c51e-8d0d79ad495f"
# strftime() 응용

timestamp = time.time()
local_time = time.localtime(timestamp)
formatted = time.strftime('%Y-%m-%d %H:%M:%S', local_time)

print(formatted)
```

```python colab={"base_uri": "https://localhost:8080/"} id="CSmUdyPy8w13" executionInfo={"status": "ok", "timestamp": 1754543705630, "user_tz": -540, "elapsed": 47, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="33649e94-2fa9-44a0-fbff-003b5ca17b60"
# 현재 시간 바로 출력
print(time.strftime('%Y-%m-%d %H:%M:%S'))
```

```python colab={"base_uri": "https://localhost:8080/", "height": 163} id="MEOSj8gi9Ezh" executionInfo={"status": "error", "timestamp": 1754543752106, "user_tz": -540, "elapsed": 79, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="cd7639ba-be70-49f0-8db7-2816ac8551f0"
# 현재 시간에서 좀전에 정의한 formatted를 빼주기 (시간끼리 연산 확인)
print(time.strftime('%Y-%m-%d %H:%M:%S') - formatted)
```

<!-- #region id="3-2ttbA_9a7N" -->
#### (2) datetime
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="pPRDFW4n9QJE" executionInfo={"status": "ok", "timestamp": 1754543818883, "user_tz": -540, "elapsed": 37, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="3a6d0e48-8dc5-4f67-87da-f64629d8c1b3"
import datetime
print(datetime.datetime.now())
```

```python colab={"base_uri": "https://localhost:8080/"} id="QODDe0QT9gdJ" executionInfo={"status": "ok", "timestamp": 1754543881116, "user_tz": -540, "elapsed": 53, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a3876ad4-19e9-410b-f4dc-ab83dad186a1"
# 초의 소숫점 빼기
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
```

```python colab={"base_uri": "https://localhost:8080/"} id="4yYyc9pS9zYv" executionInfo={"status": "ok", "timestamp": 1754543917855, "user_tz": -540, "elapsed": 53, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="050bb1a4-29f8-4b69-b946-de9ad8ac278e"
# 오늘 날짜만 보기

print(datetime.date.today())
```

```python colab={"base_uri": "https://localhost:8080/"} id="UvejMvLp94nS" executionInfo={"status": "ok", "timestamp": 1754544126067, "user_tz": -540, "elapsed": 47, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c76b1f6a-93a8-4701-843f-0f9c472b13dc"
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

```python colab={"base_uri": "https://localhost:8080/"} id="vlXecjTa-rcX" executionInfo={"status": "ok", "timestamp": 1754544270869, "user_tz": -540, "elapsed": 38, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5c8620ae-d8ef-414e-faba-74bfd40a691e"
# 실제 시간 연산방법

past_time = datetime.strptime(formatted, '%Y-%m-%d %H:%M:%S')
now = datetime.now()

print(now - past_time)
```

<!-- #region id="mUsfVxBl_RuC" -->
#### (3) random
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="AED-jWmB_NZw" executionInfo={"status": "ok", "timestamp": 1754544451425, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="07597329-069e-439c-ebcd-19aa8e8b4511"
import random
random.random()
```

```python colab={"base_uri": "https://localhost:8080/"} id="SCA9qCvR_6H8" executionInfo={"status": "ok", "timestamp": 1754544540816, "user_tz": -540, "elapsed": 50, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="1ef0259b-7d49-432e-d413-749966690b8f"
# randint(a, b): a~b 사이 정수

print(random.randint(1,6))
```

```python colab={"base_uri": "https://localhost:8080/"} id="08RfI01oAQCz" executionInfo={"status": "ok", "timestamp": 1754544597670, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c57c5630-275d-4410-f9ab-e1bbcd6b5525"
# choice(): 무작위 선택

questions = ['Q1', 'Q2', 'Q3']
print(random.choice(questions))
```

```python colab={"base_uri": "https://localhost:8080/"} id="Nryb2qMWAieI" executionInfo={"status": "ok", "timestamp": 1754544688742, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="96c248c3-ab37-4669-9adb-c665bd5a1674"
# shuffle(): 섞기

deck = ['A♠', 'K♣', 'Q♦']
random.shuffle(deck)
print(deck)
```

```python colab={"base_uri": "https://localhost:8080/"} id="qpGcFAnVA0zV" executionInfo={"status": "ok", "timestamp": 1754544725162, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2d31f3c2-82f5-407d-af8d-9acd4253ed0a"
deck = ['S', 'A', 'T', 'Q', 'W', 'E']
random.shuffle(deck)
print(deck)
```

```python colab={"base_uri": "https://localhost:8080/"} id="HOVG-ryVA9th" executionInfo={"status": "ok", "timestamp": 1754544791777, "user_tz": -540, "elapsed": 27, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="37aa5c3c-c3c5-4478-b0e0-677c2b9e2d06"
# uniform(a, b): a~b사이 임의 실수 생성
value = random.uniform(1.0, 5.0)
print(value)
```

<!-- #region id="4_8BT74IcGuo" -->
# 2. 파일 입력과 문자 수정
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/", "height": 77} id="MZGi1k6TBN9_" executionInfo={"status": "ok", "timestamp": 1754552010756, "user_tz": -540, "elapsed": 10208, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="28ebf308-4812-4729-c8e2-d1acae4893a2"
# 파일 업로드해서 불러오기 - 코랩용

from google.colab import files
uploaded = files.upload()
```

```python colab={"base_uri": "https://localhost:8080/"} id="qkAVcFYScYs4" executionInfo={"status": "ok", "timestamp": 1754552097369, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="44b72492-af92-4f16-e8c0-48a70ed1a75b"
# 업로드한 파일 읽기

with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

<!-- #region id="NBq04DsedPt-" -->
기타 인코딩 방식
=> EUC-KR, CP949
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="8LkgS_qJdFkj" executionInfo={"status": "ok", "timestamp": 1754552399843, "user_tz": -540, "elapsed": 41, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="0cbc9cfa-12a7-431e-a9d3-f4a0460f8b64"
with open('sample_fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        cleaned = line.strip()                           # 맨 윗줄과 아랫줄 공백 제거
        fruits = cleaned.split(',')                      # 쉼표 기준 나누기
        fruits = [fruit.strip() for fruit in fruits]    # 각 과일명 공백 제거
        print(fruits)
```

```python id="svH0ljxoeKae" executionInfo={"status": "ok", "timestamp": 1754552463324, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 파일 쓰기

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("코랩에서 저장한 텍스트입니다.")
```

```python colab={"base_uri": "https://localhost:8080/", "height": 17} id="3jV-4CHmee6w" executionInfo={"status": "ok", "timestamp": 1754552486708, "user_tz": -540, "elapsed": 25, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ef458f7c-5b71-419f-f725-36f85c57d67c"
# 파일 다운로드
files.download('test.txt')
```

```python id="NqaJAnmCet74" executionInfo={"status": "ok", "timestamp": 1754552599035, "user_tz": -540, "elapsed": 27, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# fruit파일에 내용 추가하기

new_line = "  papaya , pear ,  plum  \n"

with open('sample_fruits.txt', 'a', encoding='utf-8') as f:
    f.write(new_line)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 17} id="XCH8iCt0fAmd" executionInfo={"status": "ok", "timestamp": 1754552633583, "user_tz": -540, "elapsed": 86, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d680250a-25b1-45bd-8511-fac7943ee787"
# 파일 다운로드
files.download('sample_fruits.txt')
```

<!-- #region id="XV-qIVKWfRp4" -->
#### 구글 드라이브에서 직접 불러오기
<!-- #endregion -->

```python colab={"base_uri": "https://localhost:8080/"} id="Cpsb4GY-fUvx" executionInfo={"status": "ok", "timestamp": 1754552844664, "user_tz": -540, "elapsed": 214, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6c20f07c-22e1-4d54-be96-de9e02e67ba0"
path = '/content/drive/MyDrive/코드잇/AI 엔지니어 5기/공유폴더/Data/sample_fruits.txt'

with open(path, 'r') as f:
    print(f.read())
```

```python id="eiRKyGPFf78o"

```
