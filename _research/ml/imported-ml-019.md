---
title: "1 Python 연습(문제)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "[스프린트미션]1_Python_연습(문제) - AI5 강사 답안"
source_path: "11_Machine_Learning/Code_Snippets/[스프린트미션]1_Python_연습(문제) - AI5 강사 답안.md"
excerpt: "Python 연습(문제)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 파이썬 연습, 객체와 클래스, 심화 문제 순서로 큰 장을 먼저 훑고, 문제2. 주소록 클래스, 문제1. 투표 시스템 클래스 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ip..."
research_summary: "Python 연습(문제)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 파이썬 연습, 객체와 클래스, 심화 문제 순서로 큰 장을 먼저 훑고, 문제2. 주소록 클래스, 문제1. 투표 시스템 클래스 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 114개 코드 블록, 61개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 itertools, time, datetime, csv입니다."
research_artifacts: "ipynb/md · 코드 114개 · 실행 61개"
code_block_count: 114
execution_block_count: 61
research_focus:
  - "간단한 투표 시스템을 위한 VoteSystem 클래스를 구현하는 프로젝트를 시작합니다. 이 시스템은 후..."
  - "문제1. 투표 시스템 클래스"
  - "주소록 관리 시스템을 위한 Contact 클래스를 구현하는 프로젝트를 시작합니다. 이 클래스는 개인의..."
research_stack:
  - "itertools"
  - "time"
  - "datetime"
  - "csv"
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
    <div class="research-overview__value">간단한 투표 시스템을 위한 VoteSystem 클래스를 구현하는 프로젝트를 시작합니다. 이 시스템은 후보자 목록을 관리하고, 각 후보자에 대한 투표를 집계하는 기능을 제공합니다</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">파이썬 연습 -&gt; 객체와 클래스 -&gt; 심화 문제</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">이 프로그램은 사용자가 제한된 시간 내에 최대한 많은 일을 수행할 수 있도록 돕습니다. 할 일과 각각의 소요 시간이 CSV 파일에 저장되어 있으며, 사용자는 이 데이터와 자신에게 남은 시간을 입력하여 이용할 수 있습니다....</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">파이썬 연습 · 객체와 클래스 · 심화 문제</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">문제2. 주소록 클래스 -&gt; 문제1. 투표 시스템 클래스 -&gt; 문제2. 은행 계좌 클래스</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 114 · 실행 61</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">itertools, time, datetime, csv</div>
  </div>
</div>

<!-- #region id="PbVgH0G4_mer" -->
# **파이썬 연습**
<!-- #endregion -->

<!-- #region id="Q4Wm3gxu_xHr" -->
## 기초(7문제)
<!-- #endregion -->

<!-- #region id="Juz-6LWkAItk" -->
### 문제1. 3의 배수 출력
<!-- #endregion -->

<!-- #region id="AiHzC_5X_7u2" -->
- **문제 설명**  
1부터 n까지의 숫자 중에서 3의 배수만 출력하는 함수를 작성하세요.

- **함수 설명**  
`print_multiples_of_three(n: int) -> int`:  
  - n: 3의 배수를 구하고자 하는 범위의 최대값입니다.

- **입출력 예시**   

    - 입력1:

    ```
    7
    ```

    - 출력1:

    ```
    3
    6
    ```

    - 입력2:
    
    ```
    30
    ```

    - 출력2:

    ```
    3
    6
    9
    12
    15
    18
    21
    24
    27
    30
    ```
<!-- #endregion -->

```python id="m1BC9Ez0_iuS" executionInfo={"status": "ok", "timestamp": 1754887529581, "user_tz": -540, "elapsed": 26, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
def print_multiples_of_three(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            print(i)
```

```python id="StCVnx4-cpaI" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887529599, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="40b4d2e8-442e-40a4-98d7-242941e68c75"
# 프로그램 실행
print_multiples_of_three(30)
```

```python colab={"base_uri": "https://localhost:8080/"} id="zVYYk-50_vh6" executionInfo={"status": "ok", "timestamp": 1754887529613, "user_tz": -540, "elapsed": 13, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="baf74875-9a4e-45c9-cb3e-44789e467826"
# for 문 한 줄 실행 답안
def print_multiples_of_three(n):
    [print(i) for i in range(1, n + 1) if i % 3 == 0]

# 예시 실행
print_multiples_of_three(7)
```

<!-- #region id="370RMQCNAyq_" -->
### 문제2. 모음 제거하기
<!-- #endregion -->

<!-- #region id="NPqtMNfXBjEH" -->
- **문제 설명**  
문자열에서 모음(a, e, i, o, u)을 제거한 문자열을 반환하는 함수를 작성하세요.

- **함수 설명**  
`remove_vowels(s: string) -> string`:  
  - s: 영어 소문자 알파벳으로 이루어진 문자열입니다.

- **입출력 예시**   

    - 입력1:

    ```
    "codeit"
    ```

    - 출력1:

    ```
    "cdt"
    ```

    - 입력2:
    
    ```
    "python programming"
    ```

    - 출력2:

    ```
    "pythn prgrmmng"
    ```


<!-- #endregion -->

```python id="ySFIF63AA5p2" executionInfo={"status": "ok", "timestamp": 1754887529619, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
def remove_vowels(s):
    answer = ''
    for char in s:
        if char not in ['a', 'e', 'i', 'o', 'u']:  #"aeiou"
            answer += char
    return answer
```

```python id="e571RozHD0aU" executionInfo={"status": "ok", "timestamp": 1754889022116, "user_tz": -540, "elapsed": 10, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 응용 답안
def remove_vowels(s):
    return ''.join([char for char in s if char not in 'aeiou'])
```

```python id="whdVJ850crtz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754889023674, "user_tz": -540, "elapsed": 61, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a0ea762a-8bdb-4685-f004-682f69c6a7e6"
# 프로그램 실행
print(remove_vowels("codeit"))
```

<!-- #region id="3fmZxhvUA84G" -->
### 문제3. 수 크기 비교하기
<!-- #endregion -->

<!-- #region id="neh_z-dxB246" -->
- **문제 설명**  
두 개의 숫자를 입력받아, 큰 숫자와 작은 숫자를 각각 반환하는 함수를 작성하세요.
(단, 동일한 숫자를 2회 입력하는 경우에는 순서 없이 한 번만 출력되도록 해 주세요.)

- **함수 설명**

  `compare_numbers(num1, num2)`:  
  - num1, num2 : 정수형

- **입출력 예시**

  - 입력:
    ```
    10, 20
    ```

  - 출력:
    ```
    20
    ```
<!-- #endregion -->

```python id="ZJZKN6c7HCB2" executionInfo={"status": "ok", "timestamp": 1754887529643, "user_tz": -540, "elapsed": 3, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안 - 문제 설명과 동일 ver
def compare_numbers(num1, num2):
    if num1 == num2:
        return num1
    else:
        return max(num1, num2), min(num1, num2)
```

```python colab={"base_uri": "https://localhost:8080/"} id="Z52jsjRvKlx8" executionInfo={"status": "ok", "timestamp": 1754887529659, "user_tz": -540, "elapsed": 13, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="84dc2fc5-17e5-4d27-f0d8-3f3be4cfcca3"
# 프로그램 실행
print(compare_numbers(30, 700))
```

```python id="uy7jlZ5HA84I" executionInfo={"status": "ok", "timestamp": 1754887529668, "user_tz": -540, "elapsed": 6, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안 - 출력값과 동일 ver
def compare_numbers(num1, num2):
    if num1 == num2:
        return num1
    else:
        return max(num1, num2)
```

```python id="TaCXp5wPcteR" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887529747, "user_tz": -540, "elapsed": 76, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="54227b23-31b9-4c14-e5be-c6302e0f4adc"
# 프로그램 실행
print(compare_numbers(10, 20))
```

<!-- #region id="y676kwTvA9JC" -->
### 문제4. 문자열 길이 반환하기
<!-- #endregion -->

<!-- #region id="ZYsb67Q_CAEB" -->
- **문제 설명**  
문자열의 길이를 반환하되, 문자열이 빈 문자열이면 “문자열이 비어 있습니다.“를 반환하는 함수를 작성하세요.

- **함수 설명**
`check_string_length(string)`:  
  - string : 영어 알파벳 및 공백이 포함된 문자열입니다.

- **입출력 예시**   

    - 입력1:

    ```
    "Python"
    ```

    - 출력1:

    ```
    6
    ```

    - 입력2:
    
    ```
    ""
    ```

    - 출력2:

    ```
    "문자열이 비어 있습니다."
    ```
<!-- #endregion -->

```python id="yY4uoyTbCLaY" executionInfo={"status": "ok", "timestamp": 1754887529753, "user_tz": -540, "elapsed": 24, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
def check_string_length(string):
    if string == '':
        return "문자열이 비어 있습니다."
    else:
        return len(string)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"status": "ok", "timestamp": 1754887529769, "user_tz": -540, "elapsed": 11, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="825a9814-5678-4d5f-8c65-69e9bc06cbcb" id="ja5-0OVDWScG"
# 프로그램 실행
check_string_length("")
```

```python colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887529815, "user_tz": -540, "elapsed": 40, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="06ecaa79-76e3-4d2e-bfd5-9f5e298c7165" id="xbSfybuAWScH"
# 프로그램 실행
check_string_length("Python")
```

```python id="89LWLmLRLRMT" executionInfo={"status": "ok", "timestamp": 1754887529820, "user_tz": -540, "elapsed": 2, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 한줄로 줄인 코드
def check_string_length(string):
    return len(string) if string else "문자열이 비어 있습니다."
```

```python id="IqEvBf2QcwN1" colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"status": "ok", "timestamp": 1754887529903, "user_tz": -540, "elapsed": 77, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="a619ca2b-ccbe-41ea-dee0-57873325d9c4"
# 프로그램 실행
check_string_length("")
```

```python colab={"base_uri": "https://localhost:8080/"} id="SUkED8JOK8xw" executionInfo={"status": "ok", "timestamp": 1754887529921, "user_tz": -540, "elapsed": 17, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="64fb3aca-eaf6-4dc5-da3c-293cccd4ea9b"
# 프로그램 실행
check_string_length("Python")
```

<!-- #region id="RT_7aSKZBNWd" -->
### 문제5. 총 합계 구하기
<!-- #endregion -->

<!-- #region id="Xc9D8bHFCRJG" -->
- **문제 설명**  
0부터 사용자가 입력한 숫자 n까지의 합을 구하는 함수를 작성하세요.

- **함수 설명**  
`sum_up_to_n(n)`:  
  - n: 0보다 큰 정수

- **입출력 예시**   

    - 입력1:

    ```
    3
    ```

    - 출력1:

    ```
    6
    ```

    - 입력2:
    
    ```
    10
    ```

    - 출력2:

    ```
    55
    ```


<!-- #endregion -->

```python id="HC4sgDFdBNWk" executionInfo={"status": "ok", "timestamp": 1754887529927, "user_tz": -540, "elapsed": 3, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
def sum_up_to_n(n):
    answer = 0
    for i in range(1, n+1):
        answer += i
    return answer
```

```python id="jWlALiuGTh__" executionInfo={"status": "ok", "timestamp": 1754887529931, "user_tz": -540, "elapsed": 2, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 내장함수 이용한 버전
def sum_up_to_n(n):
    return sum(range(n + 1))
```

```python id="0hulzYZ3TpQH" executionInfo={"status": "ok", "timestamp": 1754887529936, "user_tz": -540, "elapsed": 2, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 수학 공식 활용 - 가우스 방식
def sum_up_to_n(n):
    return n*(n+1)//2
```

```python id="pdWV5lntcx9h" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887529961, "user_tz": -540, "elapsed": 20, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d761b1b8-b8fa-4017-fe9b-717af1d0dd0b"
# 프로그램 실행
print(sum_up_to_n(10))
```

<!-- #region id="Cvtyy64dBNig" -->
### 문제6. 짝수 합 구하기
<!-- #endregion -->

<!-- #region id="jMWwAW7xDGtv" -->
- **문제 설명**

  사용자가 입력한 숫자 n까지의 짝수 합을 구하는 함수를 작성하되, 0을 입력하면 프로그램을 종료하는 함수를 작성하세요. (단, 음수는 입력하지 않는다고 가정합니다.)

- **함수 설명**

  `sum_even_numbers(n: int)`

  - 사용자에게 숫자 입력값을 받아, 1부터 n까지의 짝수 합은 ___ 입니다." 가 출력됩니다.
  - 0 입력시 종료됨을 안내합니다.

- **입출력 예시**

    - 입력1:

    ```
    9
    ```

    - 출력1:

    ```
    "1부터 9까지의 짝수 합은 20입니다."
    ```

    - 입력2:
    
    ```
    0
    ```

    - 출력2:

    ```
    종료
    ```
<!-- #endregion -->

```python id="1_sLXOtKBNih" executionInfo={"status": "ok", "timestamp": 1754889750489, "user_tz": -540, "elapsed": 13, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
def sum_even_numbers(n):
    if n == 0:
        return "종료"
    else:
        answer = 0
        for i in range(1,n):
            if i % 2 == 0:
                answer += i
        return f"1부터 {n}까지의 짝수 합은  {answer}입니다."
```

```python id="B8P6CW-ec0sn" colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"status": "ok", "timestamp": 1754889751679, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2c3edcc1-78b0-48d8-c4bd-98bc25be01e9"
# 프로그램 실행
sum_even_numbers(9)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 36} id="BYmD05EnQkl6" executionInfo={"status": "ok", "timestamp": 1754887529991, "user_tz": -540, "elapsed": 13, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="1eadce8d-0e0b-42aa-c302-bb7532392a3b"
# 프로그램 실행
sum_even_numbers(0)
```

<!-- #region id="xtmzptFYBNqV" -->
### 문제7. 두 숫자 나누기
<!-- #endregion -->

<!-- #region id="BUfPiCg9Defz" -->
- **문제 설명**
사용자가 입력한 두 숫자를 나누는 프로그램을 작성하세요. 예외가 발생하면 "잘못된 입력입니다."를 반환하는 함수를 작성하세요.

- **함수 설명**

  `divide_numbers(a, b)`
  - 사용자에게 두개의 숫자를 차례대로 입력 받습니다.
  - 첫번째 숫자를 두번째 숫자로 나눕니다.
  - 결과값을 반환합니다. 단, 예외가 발생하면 "잘못된 입력입니다."를 반환합니다.
  - `try-except` 구문을 활용하여 함수를 작성해보세요. 이 문법에 대해서 구글링을 해도 좋습니다.

- **입출력 예시**

- 입력1:
    ```
    42, 7
    ```

- 출력1:
    ```
    6
    ```

- 입력2:
    ```
    135, 0
    ```

- 출력2:
    ```
    "잘못된 입력입니다."
    ```
<!-- #endregion -->

```python id="AoZgw6aRBNqa" executionInfo={"status": "ok", "timestamp": 1754887530064, "user_tz": -540, "elapsed": 72, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
def divide_numbers():
    print('두 개의 숫자를 순서대로 입력하세요')
    try:
        num1 = float(input('첫 번째 숫자: '))
        num2 = float(input('두 번째 숫자: '))
        return num1 / num2
    except:
        return '잘못된 입력입니다.'
```

```python id="RZUAXWopc2sp" colab={"base_uri": "https://localhost:8080/", "height": 73} executionInfo={"status": "ok", "timestamp": 1754887535042, "user_tz": -540, "elapsed": 5048, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="66e4e253-2701-46d5-dce6-632467960ef3"
# 프로그램 실행
divide_numbers()
```

```python colab={"base_uri": "https://localhost:8080/"} id="CSpB-zU2UE-D" executionInfo={"status": "ok", "timestamp": 1754887539736, "user_tz": -540, "elapsed": 4698, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="75ffbb26-4748-4845-e26c-c8fdbdfaf736"
# 프로그램 실행
divide_numbers()
```

<!-- #region id="mZDwWOfcFWlb" -->
## 응용(3문제)
<!-- #endregion -->

<!-- #region id="Tuj2xplNFgCq" -->
### 문제1. 문자열 압축 게임


<!-- #endregion -->

<!-- #region id="txOKh3aEFiw5" -->
- **문제 설명**

  주어진 문자열에서 연속해서 같은 문자가 반복되는 경우, 그 문자와 반복 횟수를 이용해 새로운 형태로 문자열을 압축합니다. 예를 들어, "aabcccccaaa" 문자열은 "a2b1c5a3"로 압축될 수 있습니다.

- **함수 설명**  
`compress_string(s: str) -> str`:  
  - s: 압축하고자 하는 문자열입니다.

- **입출력 예시**

    - 입력1:

    ```
    "aaabbaaa"
    ```

    - 출력1:

    ```
    "a3b2a3"
    ```

    - 입력2:
    
    ```
    "aabcccccaaa"
    ```

    - 출력2:

    ```
    "a2b1c5a3"
    ```
<!-- #endregion -->

```python id="Ft7h8CGrFi7j" executionInfo={"status": "ok", "timestamp": 1754887539743, "user_tz": -540, "elapsed": 6, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
def compress_string(s):
    if not s:                            # 문자열이 비었을 때 빈 값을 출력하는 로직 먼저 만듦
        return ''

    result = ''
    count = 1
    prev = s[0]                          # 첫 문자 지정

    for char in s[1:]:
        if char == prev:
            count += 1
        else:
            result += prev + str(count)
            prev = char
            count = 1

    result += prev + str(count)           # 마지막 문자 추가

    return result
```

```python id="PP2SR2Fyc4k_" colab={"base_uri": "https://localhost:8080/", "height": 36} executionInfo={"status": "ok", "timestamp": 1754887539757, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ef623adb-7e2f-43a1-c773-a74def459385"
# 프로그램 실행
compress_string("aaabbaaa")
```

```python colab={"base_uri": "https://localhost:8080/", "height": 36} id="FZHvAP2Kq8ul" executionInfo={"status": "ok", "timestamp": 1754887539771, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d069e5cb-1b87-4267-c582-d00760a4dc67"
# 프로그램 실행
compress_string("11111122222")
```

```python id="oGoY0F8sqsyU" executionInfo={"status": "ok", "timestamp": 1754887539903, "user_tz": -540, "elapsed": 127, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# groupby 사용와 itertools 사용
# itertools.groupby(): 연속된 동일 요소를 묶어주는 도구
from itertools import groupby

def compress_string(s):
    return ''.join([char + str(len(list(group))) for char, group in groupby(s)])
```

<!-- #region id="y4kJ_x6eFnmp" -->
### 문제2. 덧셈 프로그램


<!-- #endregion -->

<!-- #region id="nT-U2IVsFnmr" -->
- **문제 설명**
이 프로그램은 두 개의 숫자를 입력받아 그 합을 계산합니다. 입력받은 값이 숫자 형식이 아니면, 사용자에게 숫자 형식의 입력을 요청합니다. 숫자 입력이 완료되면 두 숫자의 합을 출력합니다.

- **함수 설명**

  `add_numbers()`
  - 이 함수는 `input()`을 사용하여 사용자로부터 두 개의 숫자를 입력받습니다.
  - 입력된 값이 숫자가 아닐 경우, "올바른 숫자를 입력하세요."라는 메시지를 출력하고 다시 입력을 요청합니다.
  - 두 숫자의 합을 계산하고 결과를 출력합니다.

- **입출력 예시**

    - 입력:
        ```
        첫 번째 숫자를 입력하세요: 10
        첫 번째 숫자를 입력하세요: twenty
        첫 번째 숫자를 입력하세요: 10
        두 번째 숫자를 입력하세요: 20
        ```

    - 출력:
        ```
        올바른 숫자를 입력하세요.
        10 + 20 = 30
        ```
<!-- #endregion -->

```python id="Np5jxyB8Fnms" executionInfo={"status": "ok", "timestamp": 1754887539948, "user_tz": -540, "elapsed": 46, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
def add_numbers():
    while True:
        try:
            num1 = int(input("첫 번째 숫자를 입력하세요: "))
            break                                                  # 숫자 입력이 성공하면 반복 종료
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    while True:
        try:
            num2 = int(input("두 번째 숫자를 입력하세요: "))
            break                                                  # 숫자 입력이 성공하면 반복 종료
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    print(f"{num1} + {num2} = {num1 + num2}")
```

```python id="aV-p2L9NWv9d" executionInfo={"status": "ok", "timestamp": 1754887539952, "user_tz": -540, "elapsed": 1, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 간단하게 정리된 버전
def get_valid_number(num):
    while True:
        try:
            return int(input(num))                               # return에 바로 input()값을 넣는 형태이므로, 함수 정의부분에 변수가 없다면 오류
        except ValueError:
            print("올바른 숫자를 입력하세요.")

def add_numbers():
    num1 = get_valid_number("첫 번째 숫자를 입력하세요: ")
    num2 = get_valid_number("두 번째 숫자를 입력하세요: ")
    print(f"{num1} + {num2} = {num1 + num2}")
```

```python id="TA_0uSezYJsK" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754890339047, "user_tz": -540, "elapsed": 27077, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6efe4be9-5dbf-4fe7-80de-bb3ab39040f5"
# 프로그램 실행
add_numbers()
```

<!-- #region id="AOeljAinFnxF" -->
### 문제3. 카운트다운 타이머
<!-- #endregion -->

<!-- #region id="cvg3_x06FnxG" -->
- **문제 설명**  
  사용자로부터 시간(초)을 입력받아 해당 시간만큼 카운트 다운을 진행한 후, "타이머 종료!"를 출력하고 프로그램이 종료됩니다. 매 초마다 남은 시간을 화면에 출력합니다.

- **함수 설명**     
  
  `count_down(seconds: int)`:  
  - seconds: 카운트 다운할 시간(초)입니다.
  - 입력받은 초만큼 카운트 다운을 진행하며, 매 초마다 남은 시간을 출력합니다.
  - 시간이 종료되면 "타이머 종료!"를 출력하고 프로그램을 종료합니다.

- **입출력 예시**

  - 입력:
    ```
    타이머를 시작할 시간(초)을 입력하세요: 5
    ```

  - 출력:
    ```
    타이머 시작!
    5
    4
    3
    2
    1
    타이머 종료!
    ```
<!-- #endregion -->

```python id="5PkfT7ZTFnxG" executionInfo={"status": "ok", "timestamp": 1754890425829, "user_tz": -540, "elapsed": 26, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
import time

def countdown_timer(seconds):
    print("타이머 시작!")
    for i in range(seconds, 0, -1):  # seconds부터 1까지 거꾸로 반복
        print(i)
        time.sleep(1)  # 1초 대기
    print("타이머 종료!")
```

```python id="Uqb2vhP4YLoy" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754890429658, "user_tz": -540, "elapsed": 3041, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d745f874-6cca-4501-ce46-bd422d4ae8b6"
# 프로그램 실행
countdown_timer(3)
```

<!-- #region id="HQMkKObNAr4s" -->
# **객체와 클래스**
<!-- #endregion -->

<!-- #region id="ko02FG9WGubi" -->
## 기초(2문제)
<!-- #endregion -->

<!-- #region id="DuBZXjwCGwvs" -->
### 문제1. 시간 추적 클래스(TimeTracker)
<!-- #endregion -->

<!-- #region id="C6_k548JGygZ" -->
- **실습 설명**

  시간을 관리하고 추적하는 `TimeTracker` 클래스를 구현하는 프로젝트를 시작합니다. 시간 관리 기능은 특히 프로젝트 작업, 운동, 공부 시간 등 다양한 활동의 지속 시간을 측정하는 데 유용합니다.

  `TimeTracker` 클래스는 다음 기능을 제공해야 합니다:

  1. **시작 시간 설정**: 사용자가 활동을 시작할 때의 시간을 기록합니다.
  2. **종료 시간 설정**: 사용자가 활동을 종료할 때의 시간을 기록합니다.
  3. **경과 시간 계산**: 활동의 시작과 종료 사이의 시간 차이를 계산합니다.

  이 클래스의 인스턴스를 사용하여 각각의 활동에 대해 별도의 시간 추적을 할 수 있어야 합니다.

- **구현해야 할 메소드**

  - `start`: 현재 시간을 시작 시간으로 설정합니다.
  - `stop`: 현재 시간을 종료 시간으로 설정하고 경과 시간을 계산합니다.
  - `get_elapsed_time`: 마지막으로 기록된 시작 시간과 종료 시간 사이의 경과 시간을 분 단위로 반환합니다.

- **실습 결과 예시**

  다음과 같은 코드를 실행했을 때의 출력 예시입니다:

  ```python
  study_session = TimeTracker()
  study_session.start()
  # 1시간 30분 경과(가정)
  study_session.stop()

  print("활동 시간:", study_session.get_elapsed_time(), "분")
  ```

  예상 출력:

  ```
  공부한 시간: 90 분
  ```

- **요구 사항**

  1. 실제 시간을 추적하려면 Python의 `datetime` 모듈을 사용하여 현재 시간을 `datetime.now()`로 가져올 수 있습니다.
  2. 경과 시간은 분 단위로 반환해야 합니다.
<!-- #endregion -->

```python id="h7RXJAbAAvUZ" executionInfo={"status": "ok", "timestamp": 1754887555584, "user_tz": -540, "elapsed": 2, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
from datetime import datetime

# 문제
class TimeTracker:
    def __init__(self):
        self.start_time = None                             # 시작 시간 초기화
        self.end_time = None                               # 종료 시간 초기화

    def start(self):
        self.start_time = datetime.now()                   # 현재 시간을 시작 시간으로 설정

    def stop(self):
        self.end_time = datetime.now()                     # 현재 시간을 종료 시간으로 설정

    def get_elapsed_time(self):
        if self.start_time and self.end_time:
            elapsed = self.end_time - self.start_time      # 시간 차이 계산 (timedelta 객체)
            return round(elapsed.total_seconds() / 60)     # 분 단위로 반환
        else:
            return "시간이 충분히 기록되지 않았습니다."
```

```python id="AsvTxp19Xyuo" executionInfo={"status": "ok", "timestamp": 1754890634642, "user_tz": -540, "elapsed": 32, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 사용 예시
# 활동 시작
study_session = TimeTracker()
study_session.start()
```

```python id="2eSYFcojj476" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754890893990, "user_tz": -540, "elapsed": 24, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="42525eee-d07a-469b-f3e4-55a45ad4b4ae"
# 활동 종료
study_session.stop()
print("공부한 시간:", study_session.get_elapsed_time(), "분")
```

<!-- #region id="aS6kmb2nHQ8J" -->
### 문제2. 주소록 클래스
<!-- #endregion -->

<!-- #region id="HUmjzWzpHS3Z" -->


- **실습 설명**

  주소록 관리 시스템을 위한 `Contact` 클래스를 구현하는 프로젝트를 시작합니다. 이 클래스는 개인의 기본 연락처 정보를 저장하고 관리하는 데 사용됩니다.

  `Contact` 클래스는 다음 정보를 저장할 수 있어야 합니다:

  - 이름(name)
  - 전화번호(phone number)
  - 이메일 주소(email address)

  클래스는 이 정보를 효율적으로 관리할 수 있는 기능을 제공해야 합니다.


- **구현해야 할 메소드**

  - `__init__`: 객체를 생성할 때 이름, 전화번호, 이메일 주소를 초기화합니다.
  - `__str__`: 연락처의 정보를 예쁘게 출력할 수 있는 문자열로 반환합니다. 이 문자열은 연락처 정보를 한눈에 알아볼 수 있도록 포맷팅됩니다.


                                       

- **실습 결과 예시**

  다음과 같은 코드를 실행했을 때의 출력 예시입니다:

  ```python
  friend = Contact("Jane Doe", "010-1234-5678", "jane@example.com")
  print(friend)
  ```

  예상 출력:

  ```
  이름: Jane Doe
  전화번호: 010-1234-5678
  이메일: jane@example.com
  ```

- **요구 사항**

  - 모든 입력 데이터는 문자열로 처리해야 합니다.
  - 연락처 정보를 적절하게 포맷팅하여 출력할 수 있어야 합니다.
<!-- #endregion -->

```python id="YGmtWN0_HGxo" executionInfo={"status": "ok", "timestamp": 1754887555764, "user_tz": -540, "elapsed": 50, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"이름: {self.name}\n전화번호: {self.phone_number}\n이메일: {self.email}"
```

```python id="_YsspEH3ZPHN" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887555768, "user_tz": -540, "elapsed": 51, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="42af8e7b-71c9-4cb5-8930-337a5a58c373"
# 사용 예시
friend = Contact("Jane Doe", "010-1234-5678", "jane@example.com")
print(friend)
```

<!-- #region id="wehB6bRNH4cD" -->
## 응용(4문제)
<!-- #endregion -->

<!-- #region id="OVzp80MqHkf1" -->
### 문제1. 투표 시스템 클래스
<!-- #endregion -->

<!-- #region id="HL5-6uKyHksh" -->
- **실습 설명**

  간단한 투표 시스템을 위한 `VoteSystem` 클래스를 구현하는 프로젝트를 시작합니다. 이 시스템은 후보자 목록을 관리하고, 각 후보자에 대한 투표를 집계하는 기능을 제공합니다.

  `VoteSystem` 클래스는 다음 기능을 제공해야 합니다:

  - 후보자 등록
  - 투표 기능
  - 투표 결과 조회

- **구현해야 할 메소드**

  - `add_candidate`: 후보자를 등록합니다. 후보자의 이름을 입력받아 목록에 추가합니다.
  - `vote`: 특정 후보자에게 투표합니다. 투표하려는 후보자의 이름을 입력받습니다.
  - `get_results`: 각 후보자의 투표 수를 출력합니다.

- **실습 결과 예시**

  - 다음과 같은 코드를 실행했을 때의 출력 예시입니다:

    ```python
    voting_system = VoteSystem()
    voting_system.add_candidate("Alice")
    voting_system.add_candidate("Bob")
    voting_system.add_candidate("Charlie")

    voting_system.vote("Alice")
    voting_system.vote("Alice")
    voting_system.vote("Bob")

    voting_system.get_results()
    ```

  - 예상 출력:

    ```
    Alice 후보가 성공적으로 등록되었습니다.
    Bob 후보가 성공적으로 등록되었습니다.
    Charlie 후보가 성공적으로 등록되었습니다.
    Alice에게 투표하였습니다.
    Alice에게 투표하였습니다.
    Bob에게 투표하였습니다.
    투표 결과:
    Alice: 2 votes
    Bob: 1 vote
    Charlie: 0 votes
    ```

- **요구 사항**

  - 후보자는 중복 등록될 수 없습니다.
  - 등록되지 않은 후보자에게 투표할 수 없습니다.
  - 각 후보자의 이름과 투표 수는 사전(dictionary)을 사용하여 관리합니다.
<!-- #endregion -->

```python id="hNWovpBKHmjW" colab={"base_uri": "https://localhost:8080/", "height": 54} executionInfo={"status": "ok", "timestamp": 1754887555770, "user_tz": -540, "elapsed": 38, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="84d8fa7c-03c2-4e56-e57b-951a037c75b5"
# 기본 답안
class VoteSystem:
    def __init__(self):
        self.candidates = {}                                    # 후보자 이름을 키, 투표 수를 값으로 저장하기 위한 딕셔너리

    def add_candidate(self, name):
        if name in self.candidates:
            print(f"{name} 후보는 이미 등록되어 있습니다.")
        else:
            self.candidates[name] = 0
            print(f"{name} 후보가 성공적으로 등록되었습니다.")

    def vote(self, name):
        if name in self.candidates:
            self.candidates[name] += 1
            print(f"{name}에게 투표하였습니다.")
        else:
            print(f"{name} 후보는 등록되어 있지 않습니다.")

    def get_results(self):
        print("투표 결과:")
        for name, count in self.candidates.items():
            if count != 1:
                print(f"{name}: {count} votes")
            else:
                print(f"{name}: {count} vote")

"""
위의 get_result 간단하게 바꾼 버전
    def get_results(self):
        print("투표 결과:")
        for name, count in self.candidates.items():
            print(f"{name}: {count} vote{'s' if count != 1 else ''}")
"""
```

```python id="c6aW0c4tZc8W" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887555771, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e81719c1-350a-4d8d-c755-772b508bccbd"
# 사용 예시
voting_system = VoteSystem()
voting_system.add_candidate("Alice")
voting_system.add_candidate("Bob")
voting_system.add_candidate("Charlie")

voting_system.vote("Alice")
voting_system.vote("Alice")
voting_system.vote("Bob")

voting_system.get_results()
```

<!-- #region id="jAlpA07gH7B2" -->
### 문제2. 은행 계좌 클래스
<!-- #endregion -->

<!-- #region id="AiGBIJWpH7B4" -->
- **실습 설명**

  간단한 은행 계좌 관리 시스템을 위한 `BankAccount` 클래스를 구현하는 프로젝트를 시작합니다. 이 클래스는 개인의 은행 계좌 정보를 관리하고 기본적인 은행 거래 기능을 제공합니다.

  `BankAccount` 클래스는 다음 정보와 기능을 제공해야 합니다:

  - 계좌 번호(account number)
  - 소유자 이름(account holder)
  - 현재 잔액(balance)

- **구현해야 할 메소드**

  - `__init__`: 객체 생성 시 계좌 번호, 소유자 이름, 초기 잔액을 설정합니다.
  - `deposit`: 계좌에 금액을 입금합니다. 입금할 금액을 인자로 받고, 잔액을 업데이트합니다.
  - `withdraw`: 계좌에서 금액을 출금합니다. 출금할 금액을 인자로 받고, 잔액이 충분할 경우에만 출금을 허용하고 잔액을 업데이트합니다.
  - `get_balance`: 현재 계좌 잔액을 반환합니다.

- **실습 결과 예시**

  - 다음과 같은 코드를 실행했을 때의 출력 예시입니다:

    ```python
    my_account = BankAccount("123-456-789", "김철수", 100000)
    my_account.deposit(50000)
    my_account.withdraw(20000)
    print(f"현재 잔액: {my_account.get_balance()}원")
    ```

  - 예상 출력:

    ```
    김철수님의 계좌 123-456-789가 개설되었습니다. 초기 잔액: 100000원
    50000원이 입금되었습니다. 현재 잔액: 150000원
    20000원이 출금되었습니다. 현재 잔액: 130000원
    현재 잔액: 130000원
    ```


- **요구 사항**

  - 계좌에서 출금 시도 시 잔액보다 많은 금액을 출금하려고 하면, 출금을 거부하고 경고 메시지를 출력해야 합니다.
  - 모든 금액은 정수 또는 실수로 처리될 수 있어야 하며, 화폐 단위로만 입력받습니다.
  - 계좌 생성, 입금, 출금 및 잔액 조회 기능을 모두 구현해야 합니다.
<!-- #endregion -->

```python id="fnpMUQf7H7B5" executionInfo={"status": "ok", "timestamp": 1754887555772, "user_tz": -540, "elapsed": 16, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"{self.account_holder}님의 계좌 {self.account_number}가 개설되었습니다. 초기 잔액: {self.balance:.0f}원")

    def deposit(self, amount: float):
        self.balance += amount
        print(f"{amount:.0f}원이 입금되었습니다. 현재 잔액: {self.balance:.0f}원")

    def withdraw(self, amount: float):
        if self.balance < amount:
            print("잔액이 부족하여 출금할 수 없습니다.")
        else:
            self.balance -= amount
            print(f"{amount:.0f}원이 출금되었습니다. 현재 잔액: {self.balance:.0f}원")

    def get_balance(self):
        return self.balance
```

```python id="vugx-M0TZt_G" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887555790, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e84b32cf-a830-451b-d364-a28f0b06814f"
# 사용 예시
my_account = BankAccount("123-456-789", "김철수", 100000)
my_account.deposit(50000)
my_account.withdraw(20000)
print(f"현재 잔액: {my_account.get_balance()}원")
```

<!-- #region id="gLGgyxNbH7JN" -->
### 문제3. 직원 관리 클래스
<!-- #endregion -->

<!-- #region id="E4YmPRZ6H7JS" -->
- **실습 설명**

  당신은 회사의 HR 부서에서 일하며, 회사 내 모든 직원의 급여 정보를 관리하는 시스템을 개발할 임무를 맡았습니다. 이 시스템은 직원들의 정보를 저장하고, 전체 직원의 평균 급여를 계산하는 기능을 제공해야 합니다.

  `EmployeeManager` 클래스는 다음 기능을 제공해야 합니다:

  - **직원 추가**: 새로운 직원의 정보를 시스템에 추가합니다. 직원의 이름과 급여 정보를 저장합니다.
  - **급여 평균 계산**: 클래스 메서드를 사용하여 모든 직원의 급여 평균을 계산합니다. 이 메서드는 저장된 모든 직원의 급여 정보를 집계하여 평균 급여를 계산하고 출력합니다.

- **구현해야 할 메소드**

  - `__init__`: 직원의 이름과 급여를 초기화하고, 직원 정보를 클래스 변수에 저장합니다.
  - `calculate_average_salary`: 클래스 메서드로 구현되며, `EmployeeManager`에 저장된 모든 직원의 급여 평균을 계산합니다.

- **실습 결과 예시**

  - 다음과 같은 코드를 실행했을 때의 출력 예시입니다:

    ```python
    emp1 = EmployeeManager("홍길동", 50000)
    emp2 = EmployeeManager("김철수", 60000)

    EmployeeManager.calculate_average_salary()
    ```

  - 예상 출력:

    ```
    홍길동 님이 추가되었습니다. 급여: 50000원
    김철수 님이 추가되었습니다. 급여: 60000원
    전체 직원의 평균 급여: 55000원
    ```

- **요구 사항**

  - 직원 정보는 클래스 변수 `employees`에 저장되어 전체 `EmployeeManager` 인스턴스에서 접근 가능해야 합니다.
  - `calculate_average_salary` 메서드는 저장된 모든 직원의 급여를 합산하여 평균을 출력하고, 직원이 없는 경우 0을 반환해야 합니다.
<!-- #endregion -->

```python id="vRuY2rAXImzi" executionInfo={"status": "ok", "timestamp": 1754887555838, "user_tz": -540, "elapsed": 3, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안

class EmployeeManager:
    employees = []                                                          # 클래스 변수: 모든 직원 정보를 리스트로 저장

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        EmployeeManager.employees.append(self)                              # 생성 시 자동으로 클래스 변수 employees에 추가됨
        print(f"{self.name} 님이 추가되었습니다. 급여: {self.salary}원")

    @classmethod
    def calculate_average_salary(cls):
        if not cls.employees:
            print("등록된 직원이 없습니다. 평균 급여: 0원")
            return 0

        total_salary = sum(emp.salary for emp in cls.employees)
        average = total_salary / len(cls.employees)
        print(f"전체 직원의 평균 급여: {average}원")
        return average
```

```python id="_Q8vSlR8Z0Y7" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887555850, "user_tz": -540, "elapsed": 10, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="4783b728-82b8-409f-a322-9ab6cae596e5"
# 사용 예시
emp1 = EmployeeManager("홍길동", 50000)
emp2 = EmployeeManager("김철수", 60000)

EmployeeManager.calculate_average_salary()
```

<!-- #region id="vbeAqh9rIjFc" -->
### 문제4. 프랜차이즈 레스토랑 관리 클래스
<!-- #endregion -->

<!-- #region id="LzZjOpGlIlYk" -->

- **실습 설명**

  당신은 여러 지점을 가진 레스토랑 체인의 IT 팀에서 일하며, 각 지점의 예약을 관리하고 중앙에서 예약 현황을 파악할 수 있는 시스템을 개발할 임무를 맡았습니다. 이 시스템은 각 지점의 예약 상황을 관리하고, 고객의 예약 요청을 효과적으로 처리할 수 있는 기능을 제공해야 합니다.

  `ReservationSystem` 클래스는 각 레스토랑 지점의 예약을 관리하며, 다음 기능을 제공해야 합니다:

  - **예약 추가**: 고객이 특정 지점, 예약 일시, 인원 수에 대한 예약을 요청하면 시스템에 추가합니다.
  - **예약 취소**: 고객이 예약을 취소할 수 있으며, 해당 예약을 시스템에서 제거합니다.
  - **예약 조회**: 특정 지점의 모든 예약 상황을 확인할 수 있습니다.
  - **예약 집계**: 모든 지점의 예약 수를 합산합니다. 이 메서드는 모든 `ReservationSystem` 인스턴스의 예약 수를 합산하여 보여줍니다.

- **구현해야 할 메소드**

  - `__init__`: 레스토랑 지점의 이름을 초기화하고 예약 리스트를 관리합니다.
  - `add_reservation`: 새로운 예약을 추가합니다. 이 메서드는 예약자 이름, 예약 일시, 인원 수를 받아 저장합니다.
  - `list_reservations`: 현재 지점의 모든 예약 상태를 출력합니다.
  - `sum_reservations`: 주어진 `ReservationSystem` 인스턴스 리스트에서 모든 예약 수를 합산합니다.

- **실습 결과 예시**
  
  - 다음과 같은 코드를 실행했을 때의 출력 예시입니다:

    ```python
    restaurant1 = ReservationSystem("강남점")
    restaurant2 = ReservationSystem("홍대점")

    restaurant1.add_reservation("홍길동", "2024-05-20", 4)
    restaurant2.add_reservation("김철수", "2024-05-21", 2)

    restaurant1.list_reservations()
    restaurant2.list_reservations()

    total_reservations = ReservationSystem.sum_reservations([restaurant1, restaurant2])
    print(f"전체 레스토랑 예약 수: {total_reservations}")
    ```

  - 예상 출력:

    ```
    강남점 예약 목록:
    - 홍길동, 2024-05-20, 4명
    홍대점 예약 목록:
    - 김철수, 2024-05-21, 2명
    전체 레스토랑 예약 수: 2
    ```

- **요구 사항**

  - 모든 출력 메시지는 한국어로 제공되어야 합니다.
  - 각 메서드는 적절한 입력 검증과 예외 처리를 포함해야 합니다.
  - `sum_reservations` 클래스 메서드는 모든 지점에서의 예약 수를 효과적으로 합산하여 전체 예약 상태를 중앙에서 확인할 수 있게 합니다.
<!-- #endregion -->

```python id="u92svE7xv3ln" executionInfo={"status": "ok", "timestamp": 1754887555886, "user_tz": -540, "elapsed": 35, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안
class ReservationSystem:
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.reservations = []                                    # 각 지점의 예약 목록을 담는 리스트 - 지점별 초기화 가능

    def add_reservation(self, customer_name, date, num_people):
        if not customer_name or not date or num_people <= 0:
            print("잘못된 예약 정보입니다.")
            return
        self.reservations.append({
            "name": customer_name,
            "date": date,
            "num_people": num_people
        })

    def list_reservations(self):
        print(f"{self.branch_name} 예약 목록:")
        if not self.reservations:
            print("현재 예약이 없습니다.")
        else:
            for r in self.reservations:
                print(f"- {r['name']}, {r['date']}, {r['num_people']}명")

    @classmethod
    def sum_reservations(cls, branches):
        total = 0
        for branch in branches:
            total += len(branch.reservations)
        return total


    """
    클래스 메소드 간단 버전
    def sum_reservations(cls, branches):
        total = sum(len(branch.reservations) for branch in branches)
        return total
    """
```

```python id="B5OAo28nZ4_z" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887555892, "user_tz": -540, "elapsed": 39, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="ce12c9eb-c153-41df-c02f-f30ce3ae7e62"
# 사용 예시
restaurant1 = ReservationSystem("강남점")
restaurant2 = ReservationSystem("홍대점")

restaurant1.add_reservation("홍길동", "2024-05-20", 4)
restaurant2.add_reservation("김철수", "2024-05-21", 2)

restaurant1.list_reservations()
restaurant2.list_reservations()

total_reservations = ReservationSystem.sum_reservations([restaurant1, restaurant2])
print(f"전체 레스토랑 예약 수: {total_reservations}")
```

```python id="3SEG3Jh-JBha" executionInfo={"status": "ok", "timestamp": 1754887555893, "user_tz": -540, "elapsed": 12, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 응용 버전 1 - cancel_reservation 추가
class ReservationSystem:
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.reservations = []

    def add_reservation(self, customer_name, date, num_people):
        if not customer_name or not date or num_people <= 0:
            print("잘못된 예약 정보입니다.")
            return
        self.reservations.append({
            "name": customer_name,
            "date": date,
            "num_people": num_people
        })

    def list_reservations(self):
        print(f"{self.branch_name} 예약 목록:")
        if not self.reservations:
            print("현재 예약이 없습니다.")
        else:
            for r in self.reservations:
                print(f"- {r['name']}, {r['date']}, {r['num_people']}명")

    # 고객 이름과 예약 일시를 기준으로 해당 예약을 찾아 삭제하는 함수 정의
    def cancel_reservation(self, customer_name, date):
        original_count = len(self.reservations)
        self.reservations = [
            r for r in self.reservations
            if not (r["name"] == customer_name and r["date"] == date)
        ]
        if len(self.reservations) < original_count:
            print(f"{customer_name}님의 예약이 취소되었습니다.")
        else:
            print("해당 예약을 찾을 수 없습니다.")

    @classmethod
    def sum_reservations(cls, branches: list):
        total = 0
        for branch in branches:
            total += len(branch.reservations)
        return total
```

```python colab={"base_uri": "https://localhost:8080/"} id="_BoBCR8twFrH" executionInfo={"status": "ok", "timestamp": 1754887555916, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c8dce192-8c56-47cc-addb-42f80f81216c"
# 사용 예시
restaurant1 = ReservationSystem("강남점")
restaurant2 = ReservationSystem("홍대점")

restaurant1.add_reservation("홍길동", "2024-05-20", 4)
restaurant2.add_reservation("김철수", "2024-05-21", 2)

restaurant1.cancel_reservation("홍길동", "2024-05-20")

restaurant1.list_reservations()
restaurant2.list_reservations()

total_reservations = ReservationSystem.sum_reservations([restaurant1, restaurant2])
print(f"전체 레스토랑 예약 수: {total_reservations}")
```

```python id="w1eRpdnOwa9u" executionInfo={"status": "ok", "timestamp": 1754887555924, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 응용 버전 2 - classmethod 사용 대신 staticmethod 사용
# sum_reservations은 인스턴스를 인자로 받기 때문에 클래스 변수에 접근하지 않음 — 사실 staticmethod로도 충분
class ReservationSystem:
    def __init__(self, branch_name):
        self.branch_name = branch_name
        self.reservations = []

    def add_reservation(self, customer_name, date, num_people):
        if not customer_name or not date or num_people <= 0:
            print("잘못된 예약 정보입니다.")
            return
        self.reservations.append({
            "name": customer_name,
            "date": date,
            "num_people": num_people
        })

    def list_reservations(self):
        print(f"{self.branch_name} 예약 목록:")
        if not self.reservations:
            print("현재 예약이 없습니다.")
        else:
            for r in self.reservations:
                print(f"- {r['name']}, {r['date']}, {r['num_people']}명")

    def cancel_reservation(self, customer_name, date):
        original_count = len(self.reservations)
        self.reservations = [
            r for r in self.reservations
            if not (r["name"] == customer_name and r["date"] == date)
        ]
        if len(self.reservations) < original_count:
            print(f"{customer_name}님의 예약이 취소되었습니다.")
        else:
            print("해당 예약을 찾을 수 없습니다.")

    @staticmethod
    def sum_reservations(branches: list):
        return sum(len(branch.reservations) for branch in branches)
```

<!-- #region id="bkd6-iPqJb5w" -->
# **심화 문제**

심화 문제는 채점에 포함되지 않습니다. 편한 마음으로 도전해 보세요.
<!-- #endregion -->

<!-- #region id="mzIDKWPjWZqc" -->
## 심화(4문제)
<!-- #endregion -->

<!-- #region id="sSy0kCSEJjIa" -->
### 문제1. 시간 관리 프로그램
<!-- #endregion -->

<!-- #region id="4iGvFHpgJ5b4" -->
- **실습 설명**

  이 프로그램은 사용자가 제한된 시간 내에 최대한 많은 일을 수행할 수 있도록 돕습니다. 할 일과 각각의 소요 시간이 CSV 파일에 저장되어 있으며, 사용자는 이 데이터와 자신에게 남은 시간을 입력하여 이용할 수 있습니다. 프로그램은 사용자가 입력한 시간 내에서 가능한 최대한 많은 할 일을 선택하고, 선택된 할 일을 소요 시간이 짧은 순으로 정렬하여 출력합니다. 이를 통해 사용자는 가장 시간을 최적화하여 일정을 관리할 수 있습니다.

- **기능 설명**
  - 데이터 읽기: 사용자로부터 CSV 파일 경로를 입력받아 파일을 읽습니다. 파일은 각 할 일과 그에 소요되는 시간을 포함합니다.
  - 할 일 선택: 사용자에게 남은 시간을 입력받습니다. 이 시간을 기준으로 할 수 있는 최대한의 할 일을 선택합니다.
  - 결과 출력: 선택된 할 일을 소요 시간이 짧은 순으로 정렬하여 출력합니다. 출력 형식은 목록 형태로 할 일과 예상 소요 시간을 포함합니다.

- **입출력 예시**

    - 할 일 및 소요 시간 CSV 파일 예시 (`tasks.csv`):
        ```
        할일,소요시간
        공부하기,120
        운동하기,60
        가계부정리,30
        영화보기,150
        ```

    - 입력:
        ```
        남은 시간(분): 210
        ```

    - 출력:
        ```
        선택된 할 일 목록:
        1. 가계부정리 - 예상 소요 시간: 30분
        2. 운동하기 - 예상 소요 시간: 60분
        3. 공부하기 - 예상 소요 시간: 120분
        ```
<!-- #endregion -->

```python id="cSylWzAlJdDQ" executionInfo={"status": "ok", "timestamp": 1754887555929, "user_tz": -540, "elapsed": 3, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
### 문제를 위한 파일 생성코드입니다. 문제를 풀기 전 이 코드를 반드시 실행해주세요.

import csv
# (시뮬레이션을 위한) 예시 파일 작성코드
def write_tasks_to_csv(filename, tasks):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['할일', '소요시간']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task, time in tasks:
            writer.writerow({'할일': task, '소요시간': time})

# 할 일과 소요 시간 데이터
tasks = [
    ('공부하기', 120),
    ('운동하기', 60),
    ('가계부정리', 30),
    ('영화보기', 150)
]

# CSV 파일로 저장
write_tasks_to_csv('tasks.csv', tasks)
```

```python id="mQWxIuB3Jd46" executionInfo={"status": "ok", "timestamp": 1754887556003, "user_tz": -540, "elapsed": 76, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안

import csv

# CSV 파일에서 할 일을 불러오는 함수
def load_tasks(filename):
    tasks = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            task_name = row['할일']
            duration = int(row['소요시간'])
            tasks.append((task_name, duration))
    return tasks

# 남은 시간 내에서 가능한 할 일을 추천하는 함수
def suggest_tasks(tasks, remaining_time):
    # 소요 시간이 짧은 순으로 정렬
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    selected = []
    total_time = 0

    for task, time in sorted_tasks:
        if total_time + time <= remaining_time:
            selected.append((task, time))
            total_time += time
        else:
            break

    return selected

# 프로그램 실행 함수
def main():
    filename = input("할 일 CSV 파일 경로를 입력하세요: ")
    tasks = load_tasks(filename)

    remaining_time = int(input("남은 시간(분): "))

    suggested = suggest_tasks(tasks, remaining_time)

    print("\n선택된 할 일 목록:")
    for idx, (task, time) in enumerate(suggested, start=1):
        print(f"{idx}. {task} - 예상 소요 시간: {time}분")
```

```python id="GCGyO3vSaDX-" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887572085, "user_tz": -540, "elapsed": 16080, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="eaa0b58f-7a49-4f66-86d6-7f83130c88bf"
# 프로그램 실행
if __name__ == "__main__":
    main()
```

<!-- #region id="qInOiISZLw36" -->

이 문제에서는 남은 시간을 최적으로 활용하는 방법을 고려하고 있습니다. 할 일을 선택하는 과정에서 간혹 같은 총 소요 시간 내에서 여러 조합의 할 일 목록을 선택할 수 있는 상황이 발생할 수 있습니다. 이러한 경우, 어떤 기준을 적용하여 할 일의 조합을 결정할까요?      
                  
       

다음과 같은 기준들을 고려해볼 수 있습니다:   
- 가장 많은 할 일을 포함하는 조합: 가능한 많은 다양한 활동을 하고자 할 때 선택할 수 있는 방법입니다.
- 가장 적은 시간이 남는 조합: 가용 시간을 거의 다 쓰는 조합을 선택하여 시간을 최대한 활용하고자 할 때 선택할 수 있는 방법입니다.
- 특정 할 일을 우선하는 조합: 개인의 선호도나 긴급도에 따라 특정 할 일을 우선적으로 포함시키는 조합을 선택할 수 있습니다.
- 가장 많은 시간을 소모하는 할 일을 포함하는 조합: 가장 긴 시간이 필요한 할 일을 포함시켜, 일상에서 잘 못하던 일을 이번 기회에 해결하고자 할 때 선택할 수 있는 방법입니다.

이러한 선택지 중에서 어떤 기준이 당신의 상황에 가장 적합한지 고민해보고, 이를 코드로 반영해보세요.
<!-- #endregion -->

```python id="FsqYOUG0yJm8" executionInfo={"status": "ok", "timestamp": 1754887572147, "user_tz": -540, "elapsed": 60, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
##  "가장 많은 할 일을 포함하는 조합" 기준으로 구현

import csv
import itertools   # 조합, 순열등을 생성하는 함수 제공 기본 라이브러리

# 작업 불러오기
def load_tasks(filename):
    tasks = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tasks.append((row['할일'], int(row['소요시간'])))
    return tasks

# 최적 조합 선택 (가장 많은 작업 개수 우선)
def suggest_max_tasks(tasks, remaining_time):
    best_combination = []
    max_task_count = 0

    # 가능한 모든 작업 조합을 확인 => 코드 로직: 모든 조합을 생성해 최적의 작업 목록 선택
    for i in range(1, len(tasks) + 1):
        for combo in itertools.combinations(tasks, i):    # tasks 리스트에서 i개씩 묶은 모든 조합 생성 => 가장 많은 작업 개수의 조합 찾을 수 있음
            total_time = sum(task[1] for task in combo)
            if total_time <= remaining_time:
                if len(combo) > max_task_count:
                    best_combination = combo
                    max_task_count = len(combo)
                elif len(combo) == max_task_count:
                    # 추가 기준: 남은 시간이 더 적게 남는 쪽 선택
                    if sum(t[1] for t in combo) > sum(t[1] for t in best_combination):
                        best_combination = combo
    return sorted(best_combination, key=lambda x: x[1])

def main():
    filename = input("할 일 CSV 파일 경로를 입력하세요: ")
    tasks = load_tasks(filename)

    remaining_time = int(input("남은 시간(분): "))

    suggested = suggest_max_tasks(tasks, remaining_time)

    print("\n선택된 할 일 목록:")
    for idx, (task, time) in enumerate(suggested, start=1):
        print(f"{idx}. {task} - 예상 소요 시간: {time}분")
```

```python colab={"base_uri": "https://localhost:8080/"} id="kYwDi6O3yNEt" executionInfo={"status": "ok", "timestamp": 1754887580072, "user_tz": -540, "elapsed": 7920, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2479f16d-7e93-4389-9a53-32bd29a8c698"
# 프로그램 실행
if __name__ == "__main__":
    main()
```

<!-- #region id="ZL_5Je5tLoEK" -->
### 문제2. 수학 퍼즐: 소수의 합
<!-- #endregion -->

<!-- #region id="1fJY0HQEL8Qv" -->
- **실습 설명**  
  이 프로그램은 사용자로부터 어떤 수 이하의 소수의 합을 구할 것인지 입력 받아, 해당 수까지의 모든 소수의 합을 계산하여 출력합니다. 소수(prime number)는 1과 자기 자신만을 약수로 가지는 자연수를 말합니다. 소수를 찾는 방법은 자유롭게 선택할 수 있지만, 효율적인 방법을 고려하여 구현해야 합니다.

- **기능 설명**
  - 소수 판별: 주어진 수까지의 모든 자연수에 대해 소수 여부를 판별합니다. (힌트 : 에라토스테네스의 체)
  - 소수 합 계산: 판별된 소수들의 합을 계산합니다.
  - 결과 출력: 계산된 소수의 합을 출력합니다. 출력 형식은 사용자가 입력한 수까지의 소수 합과 그 값을 포함합니다.

- **입출력 예시**

  - 입력:

  ```
  어떤 수까지의 소수의 합을 구하시겠습니까?: 10
  ```
  - 출력:

  ```
  10 이하 소수의 합은 17입니다.
  ```
<!-- #endregion -->

```python id="txK2vvrNLmdq" executionInfo={"status": "ok", "timestamp": 1754887580076, "user_tz": -540, "elapsed": 2, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안

# 소수인지 판별 => 보통 루트값만 확인
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # √num 까지만 확인
        if num % i == 0:
            return False
    return True

# 2부터 n까지 반복하면서 소수만 리스트 추가 -> 합산
def sum_of_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return sum(primes)

# 사용자 입력받고 결과 출력
def main():
    n = int(input("어떤 수까지의 소수의 합을 구하시겠습니까?: "))
    total = sum_of_primes(n)
    print(f"{n} 이하 소수의 합은 {total}입니다.")
```

```python id="pWsXH8UUyfjf" executionInfo={"status": "ok", "timestamp": 1754887580107, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 에라토스테네스의 체로 구현한 버전

# 소수인지 판별 => 보통 루트값만 확인
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # √num 까지만 확인
        if num % i == 0:
            return False
    return True

# 에라토스테네스 구현
def sum_of_primes(n):
    if n < 2:
        return 0

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return sum(i for i, prime in enumerate(is_prime) if prime)

# 사용자 입력받고 결과 출력
def main():
    n = int(input("어떤 수까지의 소수의 합을 구하시겠습니까?: "))
    total = sum_of_primes(n)
    print(f"{n} 이하 소수의 합은 {total}입니다.")
```

```python id="Rs_Kz0wwaPc3" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887582929, "user_tz": -540, "elapsed": 2820, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e2866a34-1c11-4e56-f845-907c10e9f1bf"
# 프로그램 실행
if __name__ == "__main__":
    main()
```

<!-- #region id="pJ30RiGXSRIi" -->
### 문제3. 도서관 관리 시스템
<!-- #endregion -->

<!-- #region id="rVE7padZSTqv" -->

- **실습 설명**

  당신은 지역 도서관에서 시스템 개발자로 일하고 있으며, 도서관의 도서, 회원, 대여 정보를 효과적으로 관리하는 시스템을 개발할 임무를 맡았습니다. `LibraryManagement` 클래스와 여러 하위 클래스를 구현하여, 도서의 추가, 삭제, 검색, 대여 및 반납 기능을 포괄적으로 다루어야 합니다.

- **시스템 구성 요소**

  - **도서(Books)**: 도서 정보를 저장합니다. 각 도서는 제목, 저자, 출판년도, ISBN 등의 정보를 포함해야 합니다.
  - **회원(Members)**: 회원 정보를 관리합니다. 각 회원은 이름, 회원번호, 대여 중인 도서 목록 등의 정보를 갖습니다.
  - **대여 관리(Rentals)**: 도서 대여 및 반납 정보를 처리합니다. 대여 시 회원 ID와 도서 ISBN을 연결하고, 대여일 및 반납일을 기록합니다.

- **구현해야 할 메소드 및 클래스**

  1. **Book Class**:
    - 도서 정보(제목, 저자, 출판년도, ISBN)를 저장하는 클래스입니다.
    - 각 도서 객체는 고유 정보를 관리합니다.

  2. **Member Class**:
    - 회원 정보(이름, 회원번호, 대여 중인 도서 목록)를 저장하는 클래스입니다.
    - 회원별 대여 기록을 관리합니다.

  3. **Rental Class**:
    - 대여 정보(회원 ID, 도서 ISBN, 대여일, 반납일)를 저장하는 클래스입니다.
    - 대여 및 반납 프로세스를 처리합니다.

  4. **LibraryManagement**:
    - 도서, 회원, 대여 정보를 관리하는 메소드와 데이터 구조를 포함합니다.
    - 도서 추가, 삭제, 검색 메소드를 구현합니다.
    - 회원 등록, 정보 조회 메소드를 구현합니다.
    - 대여 및 반납 프로세스를 관리하는 메소드를 구현합니다.

- **예시**
  
  - 다음과 같은 코드를 실행했을 때의 출력 예시입니다:

      ```python
      # 도서관 관리 시스템 초기화
      library_system = LibraryManagement()

      # 도서 추가
      library_system.add_book("1984", "조지 오웰", 1949, "978-0451524935")
      library_system.add_book("앵무새 죽이기", "하퍼 리", 1960, "978-0446310789")
      print()

      # 회원 등록
      library_system.add_member("홍길동")
      print()

      # 도서 대여
      library_system.rent_book("978-0451524935", "홍길동")
      print()

      # 도서 정보 출력
      library_system.print_books()
      print()

      # 회원 정보 출력
      library_system.print_members()

      # 도서 반납
      library_system.return_book("978-0451524935", "홍길동")
      print()

      # 회원 정보 출력
      library_system.print_members()
      ```
  
  - 출력 예시:
    
    ```
    '1984' (저자: 조지 오웰, 출판년도: 1949) 도서가 추가되었습니다.
    '앵무새 죽이기' (저자: 하퍼 리, 출판년도: 1960) 도서가 추가되었습니다.
    회원 '홍길동'님이 등록되었습니다.
    '홍길동' 회원님이 '1984' 도서를 대여하였습니다.
    도서 목록:
    - 1984 (저자: 조지 오웰, 출판년도: 1949)
    - 앵무새 죽이기 (저자: 하퍼 리, 출판년도: 1960)
    회원 목록:
    - 홍길동 (대여 중인 도서: 1984)
    '홍길동' 회원님이 '1984' 도서를 반납하였습니다.   
    회원 목록:
    - 홍길동 (대여 중인 도서: 없음)
    ```

- **요구 사항**

  - 모든 클래스 및 메소드는 적절한 입력 검증과 예외 처리를 포함해야 합니다.
  - 시스템은 사용자의 행동에 따라 적절한 피드백을 제공해야 합니다. (예: 도서가 없을 때, 회원 정보가 없을 때)

<!-- #endregion -->

```python id="WjiD18H0SS9e" executionInfo={"status": "ok", "timestamp": 1754887670660, "user_tz": -540, "elapsed": 20, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 기본 답안

# Book 클래스: 도서 정보 저장
class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

# Member 클래스: 회원 정보 및 대여 기록 저장
class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []                           # 대여 중인 도서 제목 리스트

# Rental 클래스: 대여 내역 기록
class Rental:
    def __init__(self, member_name, isbn):
        self.member_name = member_name
        self.isbn = isbn

# LibraryManagement 클래스: 도서관 전체 관리 시스템
class LibraryManagement:
    def __init__(self):
        self.books = {}                                    # ISBN -> Book 객체
        self.members = {}                                  # 이름 -> Member 객체

    # 도서 추가 메서드
    def add_book(self, title, author, year, isbn):
        if isbn in self.books:
            print("이미 등록된 ISBN입니다.")
        else:
            self.books[isbn] = Book(title, author, year, isbn)
            print(f"'{title}' (저자: {author}, 출판년도: {year}) 도서가 추가되었습니다.")

    # 회원 등록 메서드
    def add_member(self, name):
        if name in self.members:
            print("이미 등록된 회원입니다.")
        else:
            self.members[name] = Member(name)
            print(f"회원 '{name}'님이 등록되었습니다.")

    # 도서 대여 메서드
    def rent_book(self, isbn, member_name):
        if isbn not in self.books:
            return False, "해당 ISBN의 도서가 존재하지 않습니다."

        if member_name not in self.members:
            print("해당 회원이 존재하지 않습니다.")
            return
        book = self.books[isbn]
        member = self.members[member_name]

        if book.title in member.borrowed_books:
            print(f"이미 '{book.title}' 도서를 대여 중입니다.")
        else:
            member.borrowed_books.append(book.title)
            print(f"'{member_name}' 회원님이 '{book.title}' 도서를 대여하였습니다.")

    # 도서 반납 메서드
    def return_book(self, isbn, member_name):
        if isbn not in self.books or member_name not in self.members:
            print("도서 또는 회원 정보가 잘못되었습니다.")
            return
        book = self.books[isbn]
        member = self.members[member_name]

        if book.title in member.borrowed_books:
            member.borrowed_books.remove(book.title)
            print(f"'{member_name}' 회원님이 '{book.title}' 도서를 반납하였습니다.")
        else:
            print(f"'{book.title}' 도서는 현재 대여 중이 아닙니다.")

    # 전체 도서 목록 출력
    def print_books(self):
        print("도서 목록:")
        for book in self.books.values():
            print(f"- {book.title} (저자: {book.author}, 출판년도: {book.year})")

    # 전체 회원 목록 및 대여 현황 출력
    def print_members(self):
        print("회원 목록:")
        for member in self.members.values():
            books = ', '.join(member.borrowed_books) if member.borrowed_books else "없음"
            print(f"- {member.name} (대여 중인 도서: {books})")
```

```python id="cvO4Q2-UTRiz" colab={"base_uri": "https://localhost:8080/"} executionInfo={"status": "ok", "timestamp": 1754887671354, "user_tz": -540, "elapsed": 45, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="1b09fc10-d47f-4dce-d2bc-54d0539ef3e2"
# 사용 예시
library = LibraryManagement()
library.add_book("1984", "조지 오웰", 1949, "978-0451524935")
library.add_book("앵무새 죽이기", "하퍼 리", 1960, "978-0446310789")
library.add_member("홍길동")

library.rent_book("978-0451524935", "홍길동")
library.print_books()
library.print_members()
library.return_book("978-0451524935", "홍길동")
library.print_members()
```

<!-- #region id="cM8h84fQUi_t" -->
심화문제를 풀고 싶으나 어디서부터 시작해야 할지 막막하다면, 이래의 단계별 개발 가이드를 참고해보세요.


- **1단계: 기본 클래스 정의**
  - **목표**: 도서, 회원, 대여 정보를 저장할 기본 클래스를 생성합니다.

  - **주요 작업**
    1. `Book` 클래스 생성: `__init__` 메소드에는 `title`, `author`, `publication_year`, `isbn` 파라미터를 포함시킵니다.
    2. `Member` 클래스 생성: `__init__` 메소드에는 `name` 파라미터를 포함시키고, 대여 중인 도서 목록을 관리할 리스트를 초기화합니다.
    3. `Rental` 클래스 생성: `__init__` 메소드에는 `book`, `member`, `rental_date`, `return_date` 파라미터를 포함시킵니다.

- **2단계: 관리 시스템 클래스 구현**
  - **목표**: 도서, 회원, 대여 정보를 관리하는 메소드를 포함하는 `LibraryManagement` 클래스를 구현합니다.

  - **주요 작업**
    1. `LibraryManagement` 클래스에 필요한 인스턴스 변수 초기화: 도서 목록, 회원 목록, 대여 목록.
    2. 도서 추가 메소드(`add_book`) 구현.
    3. 회원 추가 메소드(`add_member`) 구현.
    4. 도서 대여 메소드(`rent_book`) 구현.
    5. 도서 반납 메소드(`return_book`) 구현.

- **3단계: 도서 및 회원 정보 조회 기능 추가**
  - **목표**: 도서 및 회원 정보를 조회하고 출력하는 기능을 구현합니다.

  - **주요 작업**
    1. 도서 목록 출력 메소드(`print_books`) 구현.
    2. 회원 목록 출력 메소드(`print_members`) 구현.

- **4단계: 테스트 및 디버깅**
  - **목표**: 관리 시스템의 테스트하여 오류를 찾고 수정합니다.

  - **주요 작업**
    1. 각 단계에서 구현한 기능을 개별적으로 테스트합니다.
    2. 예상하지 못한 에러가 발생하면 원인을 분석하고 수정합니다.
    3. 오류 메시지 외에 처리 과정을 확인하고 필요에 따라 수정합니다.

<!-- #endregion -->
