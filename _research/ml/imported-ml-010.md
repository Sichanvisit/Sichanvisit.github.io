---
title: "10.결정트리와 앙상블(DT)"
date: 2026-03-08
research_tab: "ML"
research_kind: "Archive Note"
source_title: "250827_코딩실습10_10.결정트리와 앙상블(DT)"
source_path: "11_Machine_Learning/Code_Snippets/250827_코딩실습10_10.결정트리와 앙상블(DT).md"
excerpt: "10.결정트리와 앙상블(DT)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 DT 회귀 실습, DT 분류 실습, 속성 중요도 실습 순서로 큰 장을 먼저 훑고, DecisionTree 모델 학습, DT 회귀 실습 같은 코드로 실제 구현을 이어서 확인할 수..."
research_summary: "10.결정트리와 앙상블(DT)의 원본 노트 흐름과 핵심 코드를 다시 따라갈 수 있게 정리한 ML 학습 기록입니다. 본문은 DT 회귀 실습, DT 분류 실습, 속성 중요도 실습 순서로 큰 장을 먼저 훑고, DecisionTree 모델 학습, DT 회귀 실습 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `ipynb/md` 원본과 26개 코드 블록, 25개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 matplotlib, warnings, sklearn, pandas입니다."
research_artifacts: "ipynb/md · 코드 26개 · 실행 25개"
code_block_count: 26
execution_block_count: 25
research_focus:
  - "_reg"
  - "DT 분류 실습"
  - "DT 회귀 실습"
research_stack:
  - "matplotlib"
  - "warnings"
  - "sklearn"
  - "pandas"
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
    <div class="research-overview__value">_reg: 회귀의 관례적 표현. _clf: 분류의 관례적 표현</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">원본 구조</div>
    <div class="research-overview__value">DT 회귀 실습 -&gt; DT 분류 실습 -&gt; 속성 중요도 실습 -&gt; 사전 가지치기 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">데이터 맥락</div>
    <div class="research-overview__value">특정 데이터셋 설명보다 DT 회귀 실습, DT 분류 실습, 속성 중요도 실습 같은 실습 흐름을 직접 익히는 데 초점을 둔 노트입니다.</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 장</div>
    <div class="research-overview__value">DT 회귀 실습 · DT 분류 실습 · 속성 중요도 실습 · 사전 가지치기 실습</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">구현 흐름</div>
    <div class="research-overview__value">Iris 데이터 불러오기 -&gt; DT 회귀 실습 -&gt; 학습/검증 데이터 분리</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">자료</div>
    <div class="research-overview__value">ipynb / md · 코드 26 · 실행 25</div>
  </div>
  <div class="research-overview__row">
    <div class="research-overview__label">주요 스택</div>
    <div class="research-overview__value">matplotlib, warnings, sklearn, pandas</div>
  </div>
</div>

```python
!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf

!apt-get update -qq
!apt-get install fonts-nanum* -qq

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings(action='ignore')

path = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf' # 나눔 고딕
font_name = fm.FontProperties(fname=path, size=10).get_name() # 기본 폰트 사이즈 : 10
plt.rc('font', family=font_name)

fm.fontManager.addfont(path)
```

# 1. DT 회귀 실습

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
```

```python
X_reg, y_reg = fetch_california_housing(return_X_y=True)
```

- _reg: 회귀의 관례적 표현
- _clf: 분류의 관례적 표현

```python
# 위 코드 판다스로 지정해 불러올 때

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)

X_reg = df.values
y_reg = data.target
```

```python
X_train, X_test, y_train, y_test = train_test_split(X_reg,y_reg, test_size=0.3, random_state=42)
```

```python
dt_reg = DecisionTreeRegressor()    # max_depth를 지정할 수 있음
dt_reg.fit(X_train, y_train)
```

```python
y_pred = dt_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("평균 제곱 오차(MSE): ", mse)
```

```python
df.head()
```

```python
from sklearn.tree import plot_tree

# 트리 시각화
plt.figure(figsize=(20, 10))
plot_tree(dt_reg,
          max_depth=3,
          filled=True,
          rounded=True,
          fontsize=10,
          feature_names=data.feature_names
          )
plt.title("결정 트리 시각화")
plt.show()
```

# DT 분류 실습

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import plot_tree
```

```python
iris = load_iris()
X_clf = iris.data
y_clf = iris.target
```

```python
df = pd.DataFrame(iris.data, columns=iris.feature_names)
```

```python
df.head()
```

```python
# 변수명 추출
feature_names_clf = iris.feature_names
class_names_clf = iris.target_names
```

```python
dt_clf = DecisionTreeClassifier(random_state=42)
dt_clf.fit(X_clf, y_clf)

plt.figure(figsize=(20,10))
plot_tree(
    dt_clf,
    feature_names=feature_names_clf,
    class_names=class_names_clf,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("결정 트리 분류")
plt.show()
```

```python
dt_clf.get_depth()
```

# 3. 속성 중요도 실습

```python
# 특성 이름 가져오기
feature_names = iris.feature_names
```

```python
# 각 특성의 중요도 값 가져오기
importances = dt_clf.feature_importances_
```

```python
importances
```

```python
importance_df = pd.DataFrame({
    'Feature' : feature_names,
    'Importance' : importances
    })
importance_df = importance_df.sort_values(by='Importance', ascending=False)
importance_df
```

# 4. 사전 가지치기 실습

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
```

```python
iris = load_iris()
X_clf = iris.data
y_clf = iris.target
```

```python
X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, test_size=0.3, random_state=42)
```

```python
# 하이퍼 파라미터 조합
dt_model_2 = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    max_features='sqrt'
)
dt_model_2.fit(X_train, y_train)
```

```python
plt.figure(figsize=(20,10))
plot_tree(
    dt_model_2,
    feature_names=feature_names_clf,
    class_names=class_names_clf,
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("결정 트리 분류 - 하이퍼 파라미터 지정")
plt.show()
```

```python

```
