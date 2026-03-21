---
title: "코딩실습16 11.차원축소(PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습16_11.차원축소(PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md"
excerpt: "코딩실습16 11.차원축소(PCA)를 중심으로 차원 축소, 전처리와 입력 정리 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다"
research_summary: "코딩실습16 11.차원축소(PCA)를 중심으로 차원 축소, 전처리와 입력 정리 개념과 구현 흐름을 함께 정리한 ML 실습 기록입니다. 본문에서는 데이터 설명, StandardScaler 스케일링 같은 코드를 따라가며 실제 실습 과정을 확인할 수 있습니다. `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다."
research_artifacts: "ipynb/md · 코드 11개 · 실행 10개"
code_block_count: 11
execution_block_count: 10
research_focus:
  - "사이킷런"
  - "데이터 설명"
  - "데이터 불러오기"
research_stack:
  - "sklearn"
  - "matplotlib"
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
      <td>사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html</td>
    </tr>
    <tr>
      <th scope="row">데이터 맥락</th>
      <td>사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html</td>
    </tr>
    <tr>
      <th scope="row">핵심 개념</th>
      <td>차원 축소 · 전처리와 입력 정리</td>
    </tr>
    <tr>
      <th scope="row">구현 흐름</th>
      <td>데이터 설명 -&gt; StandardScaler 스케일링 -&gt; 데이터 분포 시각화</td>
    </tr>
    <tr>
      <th scope="row">자료</th>
      <td>ipynb / md · 코드 11 · 실행 10</td>
    </tr>
    <tr>
      <th scope="row">주요 스택</th>
      <td>sklearn, matplotlib</td>
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
      <th scope="row">차원 축소</th>
      <td>차원 축소는 많은 변수의 정보를 더 적은 축으로 압축해 시각화, 노이즈 감소, 계산 효율 개선에 활용하는 기법입니다.</td>
      <td>이 글에서는 PCA처럼 분산을 최대한 보존하는 축을 찾아 데이터를 다시 표현하는 실습과 이어집니다.</td>
    </tr>
    <tr>
      <th scope="row">전처리와 입력 정리</th>
      <td>머신러닝 모델은 입력 형식에 민감하기 때문에 결측치 처리, 인코딩, 스케일링 같은 전처리 단계가 성능을 크게 좌우합니다.</td>
      <td>이 글에서는 범주형 값을 숫자로 바꾸거나 학습/검증을 분리하는 코드가 이 개념에 해당합니다.</td>
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
        <strong class="research-compact-table__main">데이터 설명</strong>
        <span class="research-compact-table__sub">실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.</span>
      </td>
      <td><span class="research-compact-table__muted">-</span></td>
      <td>데이터 불러오기</td>
    </tr>
    <tr>
      <th scope="row">Step 2 · 전처리</th>
      <td>
        <strong class="research-compact-table__main">StandardScaler 스케일링</strong>
        <span class="research-compact-table__sub">결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.</span>
      </td>
      <td><code>StandardScaler</code></td>
      <td>데이터 표준화</td>
    </tr>
    <tr>
      <th scope="row">Step 3 · 시각화</th>
      <td>
        <strong class="research-compact-table__main">데이터 분포 시각화</strong>
        <span class="research-compact-table__sub">데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.</span>
      </td>
      <td><code>matplotlib</code></td>
      <td>스크리플롯</td>
    </tr>
    </tbody>
  </table>
</div>

## Code Evidence

### 데이터 설명

**직접 해본 단계**: 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

```python
# 데이터 불러오기
X, y = load_digits(return_X_y=True)
```

### StandardScaler 스케일링

**직접 해본 단계**: 전처리

**핵심 API**: `StandardScaler`

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

```python
# 데이터 표준화

X_scaled = StandardScaler().fit_transform(X)
```

### 데이터 분포 시각화

**직접 해본 단계**: 시각화

**핵심 API**: `matplotlib`

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

```python
# 스크리플롯

plt.figure(figsize=(12,4))
plt.plot(
        range(1, len(pca.explained_variance_ratio_)+1),        # X축
        pca.explained_variance_,                               # Y축
        marker='o', linestyle='--'
        )
plt.title("Scree plot")
plt.grid(True)
plt.show()
```

## Source Bundle

- Source path: `11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md`
- Source formats: `ipynb`, `md`
- Companion files: `250901_코딩실습16_11.차원축소(PCA).ipynb`, `250901_코딩실습16_11.차원축소(PCA).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## Note Preview

> 64차원의 손글씨 데이터
> 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
