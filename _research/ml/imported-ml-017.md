---
title: "코딩실습16 11.차원축소(PCA)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Practice"
source_title: "250901_코딩실습16_11.차원축소(PCA)"
source_path: "11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md"
excerpt: "코딩실습16 11.차원축소(PCA)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 설명 순서로 큰 장을 먼저 훑고, 데이터 설명, StandardScaler 스케일링 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과..."
research_summary: "코딩실습16 11.차원축소(PCA)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 데이터 설명 순서로 큰 장을 먼저 훑고, 데이터 설명, StandardScaler 스케일링 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 11개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib입니다."
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

## 글 한눈에 보기

| 항목 | 내용 |
|------|------|
| 문제 설정 | 코딩실습16 11.차원축소(PCA)에서 데이터 설명 흐름을 직접 따라가며 구현했습니다. |
| 원본 구조 | 데이터 설명 |
| 데이터 맥락 | 64차원의 손글씨 데이터 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html |
| 주요 장 | 데이터 설명 |
| 구현 흐름 | 데이터 설명 -> StandardScaler 스케일링 -> 데이터 분포 시각화 |
| 자료 | ipynb / md · 코드 11 · 실행 10 |
| 주요 스택 | sklearn, matplotlib |

## 원본 노트 흐름

### 데이터 설명

64차원의 손글씨 데이터 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html

- 읽을 포인트: 세부 흐름: 데이터 불러오기, 데이터 표준화, PCA전 시각화

#### 데이터 불러오기

실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.

#### 데이터 표준화

결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.

#### PCA전 시각화

데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.

## 구현 흐름

### 1. 데이터 설명

- 단계: 데이터 불러오기
- 구현 의도: 실습에 사용한 원본 데이터를 불러와 이후 전처리, 피처 가공, 모델 실험이 어디서 시작되는지 보여주는 코드입니다.
- 핵심 API: -
- 코드 포인트: 데이터 불러오기

### 2. StandardScaler 스케일링

- 단계: 전처리
- 구현 의도: 결측치 처리, 인코딩, 스케일링처럼 모델이 바로 사용할 수 있도록 입력 형태를 다듬는 단계입니다.
- 핵심 API: `StandardScaler`
- 코드 포인트: 데이터 표준화

### 3. 데이터 분포 시각화

- 단계: 시각화
- 구현 의도: 데이터 분포나 결과를 눈으로 확인해 가설을 세우고 다음 피처 엔지니어링으로 이어가기 위한 시각화 코드입니다.
- 핵심 API: `matplotlib`
- 코드 포인트: 스크리플롯

## 코드로 확인한 내용

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

## 참고 자료

- Source path: `11_Machine_Learning/Code_Snippets/250901_코딩실습16_11.차원축소(PCA).md`
- Source formats: `ipynb`, `md`
- Companion files: `250901_코딩실습16_11.차원축소(PCA).ipynb`, `250901_코딩실습16_11.차원축소(PCA).md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `11_Machine_Learning_Code_Summary.md`
- External references: `scikit-learn.org`, `localhost`

## 원문 미리보기

> 64차원의 손글씨 데이터
> 사이킷런: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html
