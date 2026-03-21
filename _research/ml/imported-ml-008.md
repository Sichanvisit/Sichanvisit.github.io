---
title: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md"
excerpt: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 Iris 데이터로 이진 분류, Iris 데이터로 다중 분류, Softmax 이용한 다중 분류 순서로 큰 장을 먼저 훑고, Iris 데이터로 이진 분류,..."
research_summary: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 Iris 데이터로 이진 분류, Iris 데이터로 다중 분류, Softmax 이용한 다중 분류 순서로 큰 장을 먼저 훑고, Iris 데이터로 이진 분류, Iris 데이터로 다중 분류 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "Iris 데이터로 이진 분류"
  - "Iris 데이터로 다중 분류"
  - "Softmax 이용한 다중 분류"
research_stack:
  - "sklearn"
  - "matplotlib"
  - "numpy"
source_formats:
  - "ipynb"
  - "md"
tags:
  - research-archive
  - imported-note
  - ml
  - practice
---

## 글 한눈에 보기

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <thead>
      <tr>
        <th>항목</th>
        <th>내용</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">문제 설정</th>
        <td>코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)에서 Iris 데이터로 이진 분류, Iris 데이터로 다중 분류, Softmax 이용한 다중 분류 흐름을 직접 따라가며 구현했습니다.</td>
      </tr>
      <tr>
        <th scope="row">원본 구조</th>
        <td>Iris 데이터로 이진 분류 -&gt; Iris 데이터로 다중 분류 -&gt; Softmax 이용한 다중 분류</td>
      </tr>
      <tr>
        <th scope="row">데이터 맥락</th>
        <td>Iris 데이터로 이진 분류</td>
      </tr>
      <tr>
        <th scope="row">주요 장</th>
        <td>Iris 데이터로 이진 분류 · Iris 데이터로 다중 분류 · Softmax 이용한 다중 분류</td>
      </tr>
      <tr>
        <th scope="row">구현 흐름</th>
        <td>Iris 데이터로 이진 분류 -&gt; Iris 데이터로 다중 분류 -&gt; Softmax 이용한 다중 분류</td>
      </tr>
      <tr>
        <th scope="row">자료</th>
        <td>ipynb / md · 코드 19 · 실행 18</td>
      </tr>
      <tr>
        <th scope="row">주요 스택</th>
        <td>sklearn, matplotlib, numpy</td>
      </tr>
    </tbody>
  </table>
</div>

## 원본 노트 흐름

### Iris 데이터로 이진 분류

데이터 로드, 모델 학습, 시각화용 격자 생성 코드 같은 코드를 직접 따라가며 Iris 데이터로 이진 분류 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 데이터 로드, 모델 학습, 시각화용 격자 생성 코드

#### 데이터 로드

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

#### 모델 학습

LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

#### 시각화용 격자 생성 코드

예측 결과를 지표로 계산해 어떤 모델과 전처리가 더 잘 맞았는지 확인하는 평가 코드입니다.

### Iris 데이터로 다중 분류

데이터 로드, 시각화용 격자 생성 코드, 모델링 & 시각화 같은 코드를 직접 따라가며 Iris 데이터로 다중 분류 흐름을 확인했습니다.

- 읽을 포인트: 세부 흐름: 데이터 로드, 시각화용 격자 생성 코드, 모델링 & 시각화

#### 데이터 로드

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

#### 시각화용 격자 생성 코드

Iris 데이터로 다중 분류 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

#### 모델링 & 시각화

LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

### Softmax 이용한 다중 분류

legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - l...

- 읽을 포인트: 세부 흐름: handles, _ = scatter.legend_elements() 코드 설명

#### handles, _ = scatter.legend_elements() 코드 설명

legend_elements() - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 -...

## 구현 흐름

### 1. Iris 데이터로 이진 분류

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: -
- 코드 포인트: 데이터 로드

### 2. Iris 데이터로 다중 분류

- 단계: 모델 구성
- 구현 의도: LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.
- 핵심 API: `LogisticRegression`, `matplotlib`
- 코드 포인트: 모델링 & 시각화

### 3. Softmax 이용한 다중 분류

- 단계: 시각화
- 구현 의도: 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.
- 핵심 API: `matplotlib`
- 코드 포인트: 시각화 · legend 지정 위한 코드

### 4. handles, _ = scatter.legend_elements() 코드 설명

- 단계: 구현 코드
- 구현 의도: handles, _ = scatter.legend_eleme... 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.
- 핵심 API: -
- 코드 포인트: -

## 코드로 확인한 내용

### Iris 데이터로 이진 분류

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 데이터 로드
iris = load_iris()
```

### Iris 데이터로 다중 분류

**직접 해본 단계**: 모델 구성

**핵심 API**: `LogisticRegression`, `matplotlib`

LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.

```python
# 모델링 & 시각화

plt.figure(figsize=(10,3))

for i in range(3):
    binary_y = (y==i).astype(int)                  # OvR -> 이진 라벨 생성
    model = LogisticRegression()
    model.fit(X, binary_y)

    Z = model.predict(grid)
    Z = Z.reshape(xx.shape)

    plt.subplot(1, 3, i+1)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
    plt.scatter(X[:,0], X[:,1], c=binary_y, cmap='bwr', edgecolors='black')
    plt.title(f'Class {i} : {class_names[i]} vs Rest')
    plt.grid(True)

plt.tight_layout()
plt.show()
```

### Softmax 이용한 다중 분류

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
# 시각화

plt.figure(figsize=(5,3))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='Set1')
scatter = plt.scatter(X[:,0], X[:,1], c=y, cmap='Set1', edgecolors='black')

# legend 지정 위한 코드
handles, _ = scatter.legend_elements()

plt.title('Softmax')
plt.legend(handles, class_names, title="Classes")
plt.grid(True)
plt.show()
```

### handles, _ = scatter.legend_elements() 코드 설명

**직접 해본 단계**: 구현 코드

handles, _ = scatter.legend_eleme... 코드를 직접 실행하며 이 장의 구현 흐름을 확인했습니다.

```python

```

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Source formats: `ipynb`, `md`
- Companion files: `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).ipynb`, `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`, `matplotlib.org`

## 원문 미리보기

> - **legend_elements()** - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - label: 0, 1, 2처럼 자동 생성된 클래스 이름 문자열 - scatter.legend_elements()는 handles, label을 반환하지만, 클래스 이름을 실제 label로 사용해 보여주고자 함 - handles, _ = scatter.legend_elements()로 변수를 두 개 지정할 때, handles는 가져오고 labels는 무시한다는 의미로 **아래 밑줄**을 사용 - 아래 밑줄: 파이썬의 관례적인 표현 1. 사용하지 않는 값 무시 2. 표현식의 마지막 결과값 저장 3. 내부 문서 의미
