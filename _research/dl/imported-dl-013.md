---
title: "Segmentation 데이터다루기"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Segmentation_데이터다루기"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Segmentation_데이터다루기.md"
excerpt: "하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구성 - images: 각 이미지의 파일명, 고유 ID,..."
research_summary: "하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구성 - images: 각 이미지의 파일명, 고유 ID, 해상도 등의 메타데이터 - annot... 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공. `md` 원본과 47개 코드 블록, 41개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pycocotools, numpy, os, json입니다."
research_artifacts: "md · 코드 47개 · 실행 41개"
code_block_count: 47
execution_block_count: 41
research_focus:
  - "하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가..."
  - "데이터 구조 이해"
  - "바운딩 박스 (Bounding Box)"
research_stack:
  - "pycocotools"
  - "numpy"
  - "os"
  - "json"
  - "urllib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구성 - images: 각 이미지의 파일명, 고유 ID, 해상도 등의 메타데이터 - annot... 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공. `md` 원본과 47개 코드 블록, 41개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pycocotools, numpy, os, json입니다.

**빠르게 볼 수 있는 포인트**: 하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotati..., 데이터 구조 이해, 바운딩 박스 (Bounding Box).

**남겨둔 자료**: `md` 원본과 47개 코드 블록, 41개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pycocotools, numpy, os, json입니다.

**주요 스택**: `pycocotools`, `numpy`, `os`, `json`, `urllib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Archive Note |
| Source Files | `md` |
| Code Blocks | 47 |
| Execution Cells | 41 |
| Libraries | `pycocotools`, `numpy`, `os`, `json`, `urllib`, `cv2`, `matplotlib`, `pylab` |
| Source Note | `(실습)Segmentation_데이터다루기` |

## What This Note Covers

### 데이터 구조 이해

하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구성 - images: 각 이미지의 파일명, 고유 ID, 해상도 등의 메타데이터 - annotations: 각 이미지에 포함된 객체의 Annotat...

### Annotation의 유형

바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공

### 데이터셋 분할 및 버전

분할 (Train/Val/Test): - 학습, 검증, 평가 용도로 분리되어 있으며, 실습 시 데이터 분할에 따라 적절한 셋을 사용 버전 차이: - 2014, 2017 등 여러 버전이 있으며, 각 버전마다 이미지 및 Annotation 수가 다를 수 있음

### COCO API 활용

pycocotools 라이브러리: - COCO 데이터를 쉽게 로드하고 탐색, 시각화할 수 있도록 도와주는 API 제공 - 설치 시 pip보다 conda 또는 GitHub 소스코드를 이용하는 방법 추천 주요 기능 - COCO() 생성자를 통해 JSON 파일을 로드 - getCatIds(), loadCats(): 카테고리 관련 정보 확인 - getImgIds(), loadImgs(): 이미...

## Why This Matters

### 객체 탐지와 영역 단위 이해

- 왜 필요한가: 이미지 안에서 무엇이 있는지만이 아니라 어디에 있는지까지 알아야 할 때는 박스 또는 마스크 단위 예측이 필요합니다.
- 왜 이 방식을 쓰는가: Detection 계열 모델은 분류보다 한 단계 더 나아가 위치 정보를 함께 학습하므로 실제 비전 문제에 더 직접적으로 연결됩니다.
- 원리: 모델은 후보 영역을 만들고, 각 영역의 클래스와 좌표 또는 마스크를 동시에 예측해 장면을 해석합니다.

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 픽셀 단위 분할

- 왜 필요한가: 객체의 경계를 세밀하게 다뤄야 할 때는 이미지 전체를 한 번에 분류하는 방식만으로는 부족합니다.
- 왜 이 방식을 쓰는가: Segmentation은 픽셀마다 클래스를 붙여주기 때문에 의료영상, 장면 이해, 배경 제거처럼 경계가 중요한 문제에 잘 맞습니다.
- 원리: 이미지 특징을 추출한 뒤 해상도를 복원하면서 각 픽셀 위치에 대한 클래스 확률을 예측합니다.

## Implementation Flow

1. 데이터 구조 이해: 하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구성 - images: 각 이미지의 파...
2. Annotation의 유형: 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공
3. 데이터셋 분할 및 버전: 분할 (Train/Val/Test): - 학습, 검증, 평가 용도로 분리되어 있으며, 실습 시 데이터 분할에 따라 적절한 셋을 사용 버전 차이: - 2014, 2017 등 여러 버전이 있으며, 각 버전마다 이미지 및 Annotation 수가 다를 수 있음
4. COCO API 활용: pycocotools 라이브러리: - COCO 데이터를 쉽게 로드하고 탐색, 시각화할 수 있도록 도와주는 API 제공 - 설치 시 pip보다 conda 또는 GitHub 소스코드를 이용하는 방법 추천 주요 기능 - COCO() 생성자를 통해 JSON 파일을 로드 - getCa...

## Code Highlights

### 실습 시 유의사항

`실습 시 유의사항`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Json 파일 확인하기, 파일 정보 확인, json 파일을 사람이 읽기 편한 형태로 저장 흐름이 주석과 함께 드러납니다.

```python
#@title Json 파일 확인하기

import os
import json

# 파일 정보 확인
file_path = '/content/data/annotations/instances_val2017.json'
try:
    stat_info = os.stat(file_path)
    print("파일 크기(바이트) ", stat_info.st_size)
    print("수정 시간 : ", stat_info.st_mtime)
    print('생성 시산 : ', stat_info.st_ctime)
    print('Inode 번호', stat_info.st_ino)

except FileNotFoundError:
    print("파일이 존재하지 않습니다. ", file_path)

# json 파일을 사람이 읽기 편한 형태로 저장
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
print(type(data))

with open('output2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

### polylines- open cv

`polylines- open cv`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 설명: - cv2.polylines 함수는 이미지에 다각형의 외곽선을 그리는 OpenCV 함수입니다. - 인자 설명: - 첫 번째 인자 draw_img: 외곽선을 그릴 대상 이미지입니다. - 두 번째 인자 [polygon_xy]: 다각형의 좌표 배열을 리스트 형태로 전달합니다. (여러 개의 다각형을 동시에 그릴 수 있음) - 세 번째 인자 True: 다각형을 닫힌(closed) 형태로 그릴지 여부를 지정합니다. True이면 마지막 점과 첫 번째 점이 자동으로 연결되어 닫힌 도형이 됩니다. - 네 번째 인자 (0, 255, 0): 외곽선의 색상(BGR 포맷)입니다. 여기서는 녹색으로 지정되어 있습니다. - 이 함수 호출로 draw_img에 다각형 외곽선이 그려진 결과를 저장합니다.

```python
import numpy as np

g_color = (0,255,0)

draw_img = image_array.copy()
polygon_xy = np.array(polygon_xy, np.int32)

draw_img = cv2.polylines(draw_img, [polygon_xy], True, g_color)

plt.figure(figsize=(10,12))
plt.imshow(draw_img)
plt.axis('off')
```

### OpenCV의 fillPoly

`OpenCV의 fillPoly`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 마스크 블렌딩 흐름이 주석과 함께 드러납니다.

```python
#@title 마스크 블렌딩
def apply_mask_01(image, mask, color, alpha=0.6):
    for c in range(3):
        image[:,:,c] = np.where(mask==1,
                                (1-alpha) * image[:,:,c] + alpha * color[c] * 255,
                                image[:,:,c])
    return image
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)Segmentation_데이터다루기.md`
- Source formats: `md`
- Companion files: `(실습)Segmentation_데이터다루기.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `images.cocodataset.org`

## Note Preview

> - **하나의 JSON 파일** - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨
> - **주요 키 구성** - **images:** 각 이미지의 파일명, 고유 ID, 해상도 등의 메타데이터 - **annotations:** 각 이미지에 포함된 객체의 Annotation 정보(바운딩 박스, segmentation, keypoint 등) - **categories:** 사용되는 객체 카테고리의 이름, ID, 상위 카테고리 정보 - **licenses:** 이미지 사용에 관련된 라이선스 정보
