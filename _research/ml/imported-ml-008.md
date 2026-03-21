---
title: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md"
excerpt: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)를 중심으로 구현 중심 학습 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습8 9.기본 지도학습 알고리즘들 (로지스틱 회귀)를 중심으로 구현 중심 학습 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 Iris 데이터로 이진 분류, Iris 데이터로 다중 분류 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
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

<div class="research-compact-wrap research-compact-wrap--intro">
  <table class="research-compact-table research-compact-table--intro">
    <tbody>
    <tr>
      <th scope="row">문제 설정</th>
      <td>legend_elements(). (handles, label) 두 값을 반환</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>Iris 데이터로 이진 분류</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>구현 중심 학습</td>
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

## What I Studied

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--notes">
    <thead>
      <tr>
        <th>개념</th>
        <th>핵심 설명</th>
        <th>코드에서 확인한 것</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">구현 중심 학습</th>
      <td>이 글은 개념 설명과 함께 실제 코드를 통해 학습 흐름을 다시 따라가도록 정리된 ML 실습 기록입니다.</td>
      <td>데이터 입력, 처리, 모델링, 평가 가운데 실제로 손댄 단계를 중심으로 읽을 수 있습니다.</td>
    </tr>
    </tbody>
  </table>
</div>

## How I Implemented It

<div class="research-compact-wrap">
  <table class="research-compact-table research-compact-table--steps">
    <thead>
      <tr>
        <th>단계</th>
        <th>구현 내용</th>
        <th>핵심 API</th>
        <th>코드 포인트</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <th scope="row">Step 1 · 데이터 불러오기</th>
      <td>
        <strong class="research-compact-table__main">Iris 데이터로 이진 분류</strong>
        <span class="research-compact-table__sub">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>데이터 로드</td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 모델 구성</th>
      <td>
        <strong class="research-compact-table__main">Iris 데이터로 다중 분류</strong>
        <span class="research-compact-table__sub">LogisticRegression 같은 모델을 올려 두고 어떤 알고리즘이 문제에 더 잘 맞는지 비교해 보는 구간입니다.</span>
      </td>
      <td><code>LogisticRegression</code> <code>matplotlib</code></td>
      <td>모델링 &amp; 시각화</td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 시각화</th>
      <td>
        <strong class="research-compact-table__main">Softmax 이용한 다중 분류</strong>
        <span class="research-compact-table__sub">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</span>
      </td>
      <td><code>matplotlib</code></td>
      <td>시각화 · legend 지정 위한 코드</td>
    </tr>
    <tr>
      <th scope="row">Step 4 · 구현 코드</th>
      <td>
        <strong class="research-compact-table__main">handles, _ = scatter.legend_elements() 코드 설명</strong>
        <span class="research-compact-table__sub">원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td><span class="research-compact-table__muted">-</span></td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

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

원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python

```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Source formats: `ipynb`, `md`
- Companion files: `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).ipynb`, `250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `localhost`, `matplotlib.org`

## Note Preview

> - **legend_elements()** - (handles, label) 두 값을 반환 - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html - scatter plot이 튜플 반환 - handles: 스캐터 플롯에 표현되는 작은 점 - label: 0, 1, 2처럼 자동 생성된 클래스 이름 문자열 - scatter.legend_elements()는 handles, label을 반환하지만, 클래스 이름을 실제 label로 사용해 보여주고자 함 - handles, _ = scatter.legend_elements()로 변수를 두 개 지정할 때, handles는 가져오고 labels는 무시한다는 의미로 **아래 밑줄**을 사용 - 아래 밑줄: 파이썬의 관례적인 표현 1. 사용하지 않는 값 무시 2. 표현식의 마지막 결과값 저장 3. 내부 문서 의미
