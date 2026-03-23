---
title: "9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀)"
source_path: "11_Machine_Learning/Code_Snippets/250822_코딩실습8_9.기본 지도학습 알고리즘들 (로지스틱 회귀).md"
excerpt: "9.기본 지도학습 알고리즘들 (로지스틱 회귀)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 Iris 데이터로 이진 분류, Iris 데이터로 다중 분류, Softmax 이용한 다중 분류 순서로 큰 장을 먼저 훑고, LogisticRegression 모델..."
research_summary: "9.기본 지도학습 알고리즘들 (로지스틱 회귀)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 Iris 데이터로 이진 분류, Iris 데이터로 다중 분류, Softmax 이용한 다중 분류 순서로 큰 장을 먼저 훑고, LogisticRegression 모델 학습, Iris 데이터로 이진 분류 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 19개 코드 블록, 18개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 sklearn, matplotlib, numpy입니다."
research_artifacts: "ipynb/md · 코드 19개 · 실행 18개"
code_block_count: 19
execution_block_count: 18
research_focus:
  - "Iris 데이터로 다중 분류"
  - "Iris 데이터로 이진 분류"
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
  - archive-note
---

## 글 한눈에 보기

<div class="research-overview research-overview--intro">
  <div class="research-overview__row">
    <div class="research-overview__label">문제 설정</div>
    <div class="research-overview__value">legend_elements(). (handles, label) 두 값을 반환</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">Iris 데이터로 이진 분류 -&gt; Iris 데이터로 다중 분류 -&gt; Softmax 이용한 다중 분류</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">Iris 데이터로 다중 분류</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">Iris 데이터로 이진 분류 · Iris 데이터로 다중 분류 · Softmax 이용한 다중 분류</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">Iris 데이터 불러오기 -&gt; Iris 데이터로 이진 분류 -&gt; 데이터 분포 시각화</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 19 · 실행 18</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">sklearn, matplotlib, numpy</div>
  </div>
</div>

<!-- #region id="HRFDpeqzbYuB" -->
# 1. Iris 데이터로 이진 분류
<!-- #endregion -->

```python id="qz4Eo0MmWZg5" executionInfo={"status": "ok", "timestamp": 1755825749129, "user_tz": -540, "elapsed": 3528, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
```

```python id="JzNnCA7CXp0e" executionInfo={"status": "ok", "timestamp": 1755825774064, "user_tz": -540, "elapsed": 22, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 데이터 로드
iris = load_iris()
```

```python id="FOk94Oe7Xx1p" executionInfo={"status": "ok", "timestamp": 1755825954692, "user_tz": -540, "elapsed": 3, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X = iris.data[:, :2]                   # 앞의 2 피쳐만 사용 (시각화 위해!)
y = (iris.target==0).astype(int)       # 붓꽃 품종 1개 vs 나머지
```

```python colab={"base_uri": "https://localhost:8080/", "height": 79} id="2ZOTxHUWYd73" executionInfo={"status": "ok", "timestamp": 1755826063347, "user_tz": -540, "elapsed": 60, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6fb38cd0-018b-4c84-a6ff-a82ff80a663f"
# 모델 학습
model = LogisticRegression()
model.fit(X, y)
```

```python id="m0jwBGsUY4cn" executionInfo={"status": "ok", "timestamp": 1755826124206, "user_tz": -540, "elapsed": 5, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 시각화용 격자 생성 코드

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5          # x축
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5          # y축
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))           # 200X200 격자 생성
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])               # 모델이 예측한 클래스 라벨 계산
Z = Z.reshape(xx.shape)                                        # Z를 격자 형태로 변형 -> 2D
```

```python colab={"base_uri": "https://localhost:8080/", "height": 333} id="yKtPqJ6oZH6L" executionInfo={"status": "ok", "timestamp": 1755826617961, "user_tz": -540, "elapsed": 278, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="2202871e-43ea-4ec5-95ef-cbbcf5187899"
# 시각화
plt.figure(figsize=(4,3))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='bwr')
plt.scatter(X[:,0], X[:,1], c=y, cmap='bwr', edgecolors='black')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title("Logistic Regression - (Setosa vs Others)")
plt.grid(True)
plt.show()
```

<!-- #region id="1wnHYFa1bd23" -->
# 2. Iris 데이터로 다중 분류
<!-- #endregion -->

```python id="pT987METZH3Z" executionInfo={"status": "ok", "timestamp": 1755826762476, "user_tz": -540, "elapsed": 16, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
```

```python id="X3oha2esZH0o" executionInfo={"status": "ok", "timestamp": 1755826777664, "user_tz": -540, "elapsed": 18, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 데이터 로드
iris = load_iris()
```

```python id="8KZ6nBZMbm20" executionInfo={"status": "ok", "timestamp": 1755826873319, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X = iris.data[:, :2]                  # 앞 2개만 사용(시각화 위해!)
y = iris.target
class_names = iris.target_names       # Iris데이터의 각 클래스 이름을 가져옴
```

```python id="iBMB4EOabyf4" executionInfo={"status": "ok", "timestamp": 1755827350770, "user_tz": -540, "elapsed": 17, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 시각화용 격자 생성 코드

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5          # x축
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5          # y축
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))           # 200X200 격자 생성
grid = np.c_[xx.ravel(), yy.ravel()]
```

```python colab={"base_uri": "https://localhost:8080/", "height": 303} id="B8nSwbypcGAU" executionInfo={"status": "ok", "timestamp": 1755827353789, "user_tz": -540, "elapsed": 538, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="c3419b96-9a22-4dfe-8448-9681041dbf5a"
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

<!-- #region id="sar-YRjBeBjN" -->
# 3. Softmax 이용한 다중 분류
<!-- #endregion -->

```python executionInfo={"status": "ok", "timestamp": 1755828137080, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} id="k-6yRGfbgwTi"
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
```

```python executionInfo={"status": "ok", "timestamp": 1755828138286, "user_tz": -540, "elapsed": 29, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} id="R3iMW9MJgwTk"
# 데이터 로드
iris = load_iris()
```

```python executionInfo={"status": "ok", "timestamp": 1755828139158, "user_tz": -540, "elapsed": 9, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} id="REqrwmCcgwTk"
X = iris.data[:, :2]                  # 앞 2개만 사용(시각화 위해!)
y = iris.target
class_names = iris.target_names       # Iris데이터의 각 클래스 이름을 가져옴
```

```python colab={"base_uri": "https://localhost:8080/", "height": 135} id="Woht6OCKgzuZ" executionInfo={"status": "ok", "timestamp": 1755828254965, "user_tz": -540, "elapsed": 68, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bbc3a758-fc8e-4021-c410-58ded94b181c"
# Softmax 회귀 모델링
model = LogisticRegression(multi_class='multinomial', solver='lbfgs')   # multi_class='multinomial' + solver='lbfgs : 소프트 맥스
model.fit(X, y)
```

```python id="DnILDrWXgzrl" executionInfo={"status": "ok", "timestamp": 1755828289744, "user_tz": -540, "elapsed": 14, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 시각화용 격자 생성 코드

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5          # x축
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5          # y축
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                     np.linspace(y_min, y_max, 200))           # 200X200 격자 생성
grid = np.c_[xx.ravel(), yy.ravel()]
```

```python id="LAJatwOQgzpK" executionInfo={"status": "ok", "timestamp": 1755828348910, "user_tz": -540, "elapsed": 23, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 예측값
Z = model.predict(grid)
Z = Z.reshape(xx.shape)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 314} id="vUbNm_i5gzmi" executionInfo={"status": "ok", "timestamp": 1755831212520, "user_tz": -540, "elapsed": 354, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="47a0222f-3fdb-42b2-e627-b742a9d67e45"
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

<!-- #region id="aF-tDVmdstWA" -->
#### **handles, _ = scatter.legend_elements() 코드 설명**

- **legend_elements()**
    - (handles, label) 두 값을 반환
        - https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html
        - scatter plot이 튜플 반환
    - handles: 스캐터 플롯에 표현되는 작은 점
    - label: 0, 1, 2처럼 자동 생성된 클래스 이름 문자열
- scatter.legend_elements()는 handles, label을 반환하지만, 클래스 이름을 실제 label로 사용해 보여주고자 함
- handles, _ = scatter.legend_elements()로 변수를 두 개 지정할 때, handles는 가져오고 labels는 무시한다는 의미로 **아래 밑줄**을 사용
    - 아래 밑줄: 파이썬의 관례적인 표현
        1. 사용하지 않는 값 무시
        2. 표현식의 마지막 결과값 저장
        3. 내부 문서 의미
<!-- #endregion -->

```python id="0gQtOabLiY2D"

```
