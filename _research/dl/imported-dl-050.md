---
title: "Mission 7 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_7_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_7_강사공유.md"
excerpt: "이번 미션에서는 SSD 모델을 활용하여 개와 고양이의 얼굴(Face) 영역을 감지하는 Object Detection 작업을 수행해 봅시다. 데이터 링크 (The Oxford-IIIT Pet Dataset). * 1 = 고양이 * 2 = 개. `md` 원본과 41개 코드 블록, 40개 실행 셀을 함께..."
research_summary: "이번 미션에서는 SSD 모델을 활용하여 개와 고양이의 얼굴(Face) 영역을 감지하는 Object Detection 작업을 수행해 봅시다. 데이터 링크 (The Oxford-IIIT Pet Dataset). * 1 = 고양이 * 2 = 개. `md` 원본과 41개 코드 블록, 40개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torchinfo, os, sys, math입니다."
research_artifacts: "md · 코드 41개 · 실행 40개"
code_block_count: 41
execution_block_count: 40
research_focus:
  - "사전 설정"
  - "이번 미션에서는 SSD 모델을 활용하여 개와 고양이의 얼굴(Face) 영역을 감지하는 Object De..."
  - "과제 요약"
research_stack:
  - "torchinfo"
  - "os"
  - "sys"
  - "math"
  - "glob"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

이번 미션에서는 SSD 모델을 활용하여 개와 고양이의 얼굴(Face) 영역을 감지하는 Object Detection 작업을 수행해 봅시다. 데이터 링크 (The Oxford-IIIT Pet Dataset). * 1 = 고양이 * 2 = 개. `md` 원본과 41개 코드 블록, 40개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torchinfo, os, sys, math입니다.

**빠르게 볼 수 있는 포인트**: 사전 설정, 이번 미션에서는 SSD 모델을 활용하여 개와 고양이의 얼굴(Face)..., 과제 요약.

**남겨둔 자료**: `md` 원본과 41개 코드 블록, 40개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torchinfo, os, sys, math입니다.

**주요 스택**: `torchinfo`, `os`, `sys`, `math`, `glob`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Mission |
| Source Files | `md` |
| Code Blocks | 41 |
| Execution Cells | 40 |
| Libraries | `torchinfo`, `os`, `sys`, `math`, `glob`, `random`, `shutil`, `xml` |
| Source Note | `Mission_7_강사공유` |

## What This Note Covers

### 사전 설정 > 과제 요약

이번 미션에서는 SSD 모델을 활용하여 개와 고양이의 얼굴(Face) 영역을 감지하는 Object Detection 작업을 수행해 봅시다. 데이터 링크 (The Oxford-IIIT Pet Dataset)

### SSD 실험 > 데이터 확인

* 1 = 고양이 * 2 = 개

### 데이터 전처리 > 객체 Bounding Box 리스트화

모든 XML을 읽고, 이미지별 Bounding Box 정보를 하나의 리스트(annotations)에 저장했다. 지금까지 전처리가 잘 되었는지 예시 이미지를 시각화 해볼 것이다.

### Key Step

라이브러리 설치 및 import

## Why This Matters

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 평가 지표 해석

- 왜 필요한가: 정확도 하나만으로는 모델이 실제로 무엇을 잘하고 무엇을 놓치는지 충분히 설명할 수 없습니다.
- 왜 이 방식을 쓰는가: 문제 유형에 맞는 지표를 함께 보면 불균형 데이터, 오차 크기, 재현율 같은 중요한 관점을 놓치지 않을 수 있습니다.
- 원리: 예측 결과를 정답과 비교해 오차나 클래스별 성능을 수치화하고, 그 수치로 모델 선택과 개선 방향을 판단합니다.

## Implementation Flow

1. 사전 설정 > 과제 요약: 이번 미션에서는 SSD 모델을 활용하여 개와 고양이의 얼굴(Face) 영역을 감지하는 Object Detection 작업을 수행해 봅시다. 데이터 링크 (The Oxford-IIIT Pet Dataset)
2. SSD 실험 > 데이터 확인: * 1 = 고양이 * 2 = 개
3. 데이터 전처리 > 객체 Bounding Box 리스트화: 모든 XML을 읽고, 이미지별 Bounding Box 정보를 하나의 리스트(annotations)에 저장했다. 지금까지 전처리가 잘 되었는지 예시 이미지를 시각화 해볼 것이다.
4. Key Step: 라이브러리 설치 및 import

## Code Highlights

### 데이터셋으로 변환

`데이터셋으로 변환`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 경로 설정 및 파일 수량확인, xml-이미지 데이터 pair 확인 및 통합 list 생성, XML이 없는 이미지 목록 흐름이 주석과 함께 드러납니다.

```python
import torchvision.tv_tensors as tv_tensors

class CustomDataset(Dataset):
    def __init__(self, root, transforms=None):
        self.root = root
        self.transforms = transforms

        # 경로 설정 및 파일 수량확인
        self.img_path = os.path.join(root, "images", "images")
        self.xml_path = os.path.join(root, "annotations", "annotations", "xmls")

        self.xml_list, self.data_list = self._data_pair_check()
        self.annotations = self._xml_parser(self.xml_list)

    def _class_idx(self, cls_name):
        return ["background", "cat", "dog"].index(cls_name)

    # xml-이미지 데이터 pair 확인 및 통합 list 생성
    def _data_pair_check(self):
        xml_list = [os.path.splitext(file)[0] for file in os.listdir(self.xml_path) if file.endswith(".xml")]
        img_list = [os.path.splitext(file)[0] for file in os.listdir(self.img_path) if file.endswith(".jpg")]

        # XML이 없는 이미지 목록
        missing_xml = [image for image in img_list if image not in xml_list]
        # 이미지가 없는 XML 목록
        extra_xml = [xml for xml in xml_list if xml not in img_list]
        # 짝이 안 맞는 데이터는 drop
        trainval_list = [image for image in img_list if image in xml_list]
# ... trimmed ...
```

### Feature Extraction SSD 모델

`Feature Extraction SSD 모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습, only_header, 손실값 저장 흐름이 주석과 함께 드러납니다.

```python
# @title  모델 학습
# only_header
if only_header:
    model = model.to(device)

    # 손실값 저장
    train_losses = []
    old_loss = 10

    for epoch in range(num_epochs):
        print(f"Epoch {epoch + 1}/{num_epochs} 시작")

        model.train()
        total_train_loss = 0

        for images, targets in tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs} - Training"):
            images = [img.to(device) for img in images]
            targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

            loss_dict = model(images, targets)
            losses = sum(loss for loss in loss_dict.values())
            total_train_loss += losses.item()

            optimizer.zero_grad()
            losses.backward()
            optimizer.step()

        avg_train_loss = total_train_loss / len(train_loader)
# ... trimmed ...
```

### Fine Tuning SSD 모델

`Fine Tuning SSD 모델`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습, only_header, 손실값 저장 흐름이 주석과 함께 드러납니다.

```python
# @title  모델 학습
# only_header
if only_header:
    model = model.to(device)

    # 손실값 저장
    train_losses = []
    old_loss = 10

    for epoch in range(num_epochs):
        print(f"Epoch {epoch + 1}/{num_epochs} 시작")

        model.train()
        total_train_loss = 0

        for images, targets in tqdm(train_loader, desc=f"Epoch {epoch+1}/{num_epochs} - Training"):
            images = [img.to(device) for img in images]
            targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

            loss_dict = model(images, targets)
            losses = sum(loss for loss in loss_dict.values())
            total_train_loss += losses.item()

            optimizer.zero_grad()
            losses.backward()
            optimizer.step()

        avg_train_loss = total_train_loss / len(train_loader)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/Mission_7_강사공유.md`
- Source formats: `md`
- Companion files: `Mission_7_강사공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `www.kaggle.com`, `localhost`

## Note Preview

> 이번 미션에서는 SSD 모델을 활용하여 개와 고양이의 얼굴(Face) 영역을 감지하는 Object Detection 작업을 수행해 봅시다.
> - 데이터 링크 (The Oxford-IIIT Pet Dataset)
