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

```python colab={"base_uri": "https://localhost:8080/"} id="r7mpkmJHL5NR" executionInfo={"status": "ok", "timestamp": 1756268562103, "user_tz": -540, "elapsed": 21238, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d3ccd5ea-886b-4b40-9797-961fae44769b"
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

<!-- #region id="ELm-DKIhMl3k" -->
# 1. DT 회귀 실습
<!-- #endregion -->

```python id="Lxs3RvTTMRUx" executionInfo={"status": "ok", "timestamp": 1756268563727, "user_tz": -540, "elapsed": 1618, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
```

```python id="Pvd4mw3AMoLy" executionInfo={"status": "ok", "timestamp": 1756268563763, "user_tz": -540, "elapsed": 30, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X_reg, y_reg = fetch_california_housing(return_X_y=True)
```

<!-- #region id="kHBSm05iNES_" -->
- _reg: 회귀의 관례적 표현
- _clf: 분류의 관례적 표현
<!-- #endregion -->

```python id="4Na81UJDNCqz" executionInfo={"status": "ok", "timestamp": 1756268563813, "user_tz": -540, "elapsed": 24, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 위 코드 판다스로 지정해 불러올 때

data = fetch_california_housing()

df = pd.DataFrame(data.data, columns=data.feature_names)

X_reg = df.values
y_reg = data.target
```

```python id="217ROncdNbXW" executionInfo={"status": "ok", "timestamp": 1756268563836, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X_train, X_test, y_train, y_test = train_test_split(X_reg,y_reg, test_size=0.3, random_state=42)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 79} id="9EFQXSrsNfCj" executionInfo={"status": "ok", "timestamp": 1756268564133, "user_tz": -540, "elapsed": 295, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="d2076ff1-8542-4b77-e88a-37d1391e84e6"
dt_reg = DecisionTreeRegressor()    # max_depth를 지정할 수 있음
dt_reg.fit(X_train, y_train)
```

```python colab={"base_uri": "https://localhost:8080/"} id="Z_PX3IQrQgyK" executionInfo={"status": "ok", "timestamp": 1756268564134, "user_tz": -540, "elapsed": 19, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="be9bde55-ca10-4cad-d1cc-82bd9777cf9c"
y_pred = dt_reg.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("평균 제곱 오차(MSE): ", mse)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 206} id="IYO_9qVTSURa" executionInfo={"status": "ok", "timestamp": 1756268564163, "user_tz": -540, "elapsed": 35, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="1a98487a-b8aa-4491-e951-a6642576fbdb"
df.head()
```

```python colab={"base_uri": "https://localhost:8080/", "height": 520} id="H0Vpvz-vQ0LQ" executionInfo={"status": "ok", "timestamp": 1756268564996, "user_tz": -540, "elapsed": 836, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="49e2d8e8-c95d-471c-e487-af8a86a36921"
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

<!-- #region id="wbpZeHm5TwQH" -->
# DT 분류 실습
<!-- #endregion -->

```python id="3GLQvl1kSMe7" executionInfo={"status": "ok", "timestamp": 1756268565005, "user_tz": -540, "elapsed": 4, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import plot_tree
```

```python id="rQ7GItzAUEjH" executionInfo={"status": "ok", "timestamp": 1756268565021, "user_tz": -540, "elapsed": 10, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
iris = load_iris()
X_clf = iris.data
y_clf = iris.target
```

```python id="qIgsbGbZUS8_" executionInfo={"status": "ok", "timestamp": 1756268565031, "user_tz": -540, "elapsed": 2, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
df = pd.DataFrame(iris.data, columns=iris.feature_names)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 206} id="ZuAIeVZlUeTo" executionInfo={"status": "ok", "timestamp": 1756268565048, "user_tz": -540, "elapsed": 16, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="e28b883c-3d45-4a39-bb2a-cd67255ee71a"
df.head()
```

```python id="zvdKK0qtUtVA" executionInfo={"status": "ok", "timestamp": 1756268565052, "user_tz": -540, "elapsed": 2, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 변수명 추출
feature_names_clf = iris.feature_names
class_names_clf = iris.target_names
```

```python colab={"base_uri": "https://localhost:8080/", "height": 520} id="gLTaM8XAVC3M" executionInfo={"status": "ok", "timestamp": 1756268565519, "user_tz": -540, "elapsed": 465, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="6ffd8fa4-833d-4629-ff31-0bf999039162"
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

```python colab={"base_uri": "https://localhost:8080/"} id="u0P1uiULVorP" executionInfo={"status": "ok", "timestamp": 1756268565531, "user_tz": -540, "elapsed": 8, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="5122f5ca-3205-4dcd-ff81-3e819a83b7d1"
dt_clf.get_depth()
```

<!-- #region id="HRpjd-qfaDnV" -->
# 3. 속성 중요도 실습
<!-- #endregion -->

```python id="YPXWGV4xW2j_" executionInfo={"status": "ok", "timestamp": 1756268565535, "user_tz": -540, "elapsed": 3, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 특성 이름 가져오기
feature_names = iris.feature_names
```

```python id="_7cAv-PTaQuq" executionInfo={"status": "ok", "timestamp": 1756268565543, "user_tz": -540, "elapsed": 5, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
# 각 특성의 중요도 값 가져오기
importances = dt_clf.feature_importances_
```

```python colab={"base_uri": "https://localhost:8080/"} id="p0Kx8XrcafsV" executionInfo={"status": "ok", "timestamp": 1756268565566, "user_tz": -540, "elapsed": 18, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="fc8eae5a-f93c-4f41-e529-019e1fdc7e48"
importances
```

```python colab={"base_uri": "https://localhost:8080/", "height": 174} id="QJoqFXKBajzw" executionInfo={"status": "ok", "timestamp": 1756268565642, "user_tz": -540, "elapsed": 18, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="bc637436-5975-4d25-ed76-f9b63ca017f2"
importance_df = pd.DataFrame({
    'Feature' : feature_names,
    'Importance' : importances
    })
importance_df = importance_df.sort_values(by='Importance', ascending=False)
importance_df
```

<!-- #region id="rjEA3je1xY2O" -->
# 4. 사전 가지치기 실습
<!-- #endregion -->

```python id="25BRDTgCbIWn" executionInfo={"status": "ok", "timestamp": 1756268778245, "user_tz": -540, "elapsed": 26, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
```

```python id="0wkKO8E5yklD" executionInfo={"status": "ok", "timestamp": 1756269008179, "user_tz": -540, "elapsed": 64, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
iris = load_iris()
X_clf = iris.data
y_clf = iris.target
```

```python id="dutAnMCgyloO" executionInfo={"status": "ok", "timestamp": 1756269065194, "user_tz": -540, "elapsed": 11, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}}
X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, test_size=0.3, random_state=42)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 97} id="-GRwp1nTxqEI" executionInfo={"status": "ok", "timestamp": 1756269066450, "user_tz": -540, "elapsed": 34, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="62f4c8b3-3a07-445f-f87d-937e22e08498"
# 하이퍼 파라미터 조합
dt_model_2 = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    max_features='sqrt'
)
dt_model_2.fit(X_train, y_train)
```

```python colab={"base_uri": "https://localhost:8080/", "height": 520} id="-mmegbmLyX_D" executionInfo={"status": "ok", "timestamp": 1756269110257, "user_tz": -540, "elapsed": 675, "user": {"displayName": "Hana Cho", "userId": "08103705611627615689"}} outputId="7bf79d1e-2989-4512-fde8-3d201e94c96d"
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

```python id="TvqQikJGy-Bq"

```
