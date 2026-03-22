---
title: "Segmentation 데이터다루기"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Segmentation_데이터다루기"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Segmentation_데이터다루기.md"
excerpt: "Segmentation 데이터다루기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Instance Segmentati..., 실습 시 유의사항, Annotation의 유형 순서로 핵심 장면을 먼저 훑고, 실습 시 유의사항, Instance Segme..."
research_summary: "Segmentation 데이터다루기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Instance Segmentati..., 실습 시 유의사항, Annotation의 유형 순서로 핵심 장면을 먼저 훑고, 실습 시 유의사항, Instance Segmentation..., polylines- open cv 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 47개 코드 블록, 41개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pycocotools, numpy, os, json입니다."
research_artifacts: "md · 코드 47개 · 실행 41개"
code_block_count: 47
execution_block_count: 41
research_focus:
  - "Instance Segmentation 시각화 - COCO API 활용한 시각화"
  - "실습 시 유의사항"
  - "Annotation의 유형"
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

Segmentation 데이터다루기에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Instance Segmentati..., 실습 시 유의사항, Annotation의 유형 순서로 핵심 장면을 먼저 훑고, 실습 시 유의사항, Instance Segmentation..., polylines- open cv 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 47개 코드 블록, 41개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pycocotools, numpy, os, json입니다.

**빠르게 볼 수 있는 포인트**: Instance Segmentation 시각화 - COCO API 활용..., 실습 시 유의사항, Annotation의 유형.

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

### Instance Segmentation 시각화 - COCO API 활용한 시각화

getAnnIds()로 특정 image에 해당하는 annotation id를 가져온 후에 이 id를 loadAnns()로 입력하여 해당 이미지의 모든 annotation 정보를 가져옴. - segmentation 정보는 polygon 형태로 되어 있음. - annotation 정보를 coco.showAnns(anns)에 입력하여 in...

- 읽을 포인트: 비전 모델이 객체나 픽셀 단위를 어떻게 예측하는지 구현으로 따라가는 구간입니다.

### 실습 시 유의사항

데이터 불균형: - 일부 카테고리는 데이터 수가 적을 수 있으므로, 모델 학습 시 주의가 필요함 Annotation 품질: - Annotation은 수작업으로 생성된 경우도 있으므로, 일부 부정확할 수 있음

- 읽을 포인트: 실습 시 유의사항 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### Annotation의 유형

바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공

- 읽을 포인트: Annotation의 유형에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### 데이터셋 분할 및 버전

분할 (Train/Val/Test): - 학습, 검증, 평가 용도로 분리되어 있으며, 실습 시 데이터 분할에 따라 적절한 셋을 사용 버전 차이: - 2014, 2017 등 여러 버전이 있으며, 각 버전마다 이미지 및 Annotation 수가 다를 수 있음

- 읽을 포인트: 데이터셋 분할 및 버전에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### 데이터 구조 이해

하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구성 - images: 각 이미지의 파일명, 고유 ID, 해상도 등의 메타데이터 - annot...

- 읽을 포인트: 데이터 구조 이해에서 다룬 핵심 개념과 구현 흐름을 다시 읽을 수 있게 정리한 구간입니다.

### OpenCV의 fillPoly

다각형 내부 영역 채우기 설명: - cv2.fillPoly 함수는 지정된 다각형 내부를 특정 색상으로 채워줍니다. - 매개변수 설명: - 첫 번째 인자 draw_img: 채우기를 적용할 대상 이미지입니다. - 두 번째 인자 [polygon_xy]: 다각형 좌표 배열을 리스트 형태로 전달합니다. - 여러 개의 다각형을 동시에 채울 수...

- 읽을 포인트: OpenCV의 fillPoly 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

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

1. Instance Segmentation 시각화 - COCO API 활용한 시각화: getAnnIds()로 특정 image에 해당하는 annotation id를 가져온 후에 이 id를 loadAnns()로 입력하여 해당 이미지의 모든 annotation 정보를 가져...
2. 실습 시 유의사항: 데이터 불균형: - 일부 카테고리는 데이터 수가 적을 수 있으므로, 모델 학습 시 주의가 필요함 Annotation 품질: - Annotation은 수작업으로 생성된 경우도 있으므로, 일부 부정확할 수 있음
3. Annotation의 유형: 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보 Instance Segmentation: - 객체의 경계를 보다 세밀하게 표현하기 위해 polygon(다각형) 또는 마스크 형태의 정보 제공
4. 데이터셋 분할 및 버전: 분할 (Train/Val/Test): - 학습, 검증, 평가 용도로 분리되어 있으며, 실습 시 데이터 분할에 따라 적절한 셋을 사용 버전 차이: - 2014, 2017 등 여러 버전이 있으며, 각 버전마다 이미지 및 Annotation 수...
5. 데이터 구조 이해: 하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨 주요 키 구...
6. OpenCV의 fillPoly: 다각형 내부 영역 채우기 설명: - cv2.fillPoly 함수는 지정된 다각형 내부를 특정 색상으로 채워줍니다. - 매개변수 설명: - 첫 번째 인자 draw_img: 채우기를 적용할 대상 이미지입니다. - 두 번째 인자 [pol...

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

### Instance Segmentation 시각화 - COCO API 활용한 시각화

`Instance Segmentation 시각화 - COCO API 활용한 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 showAnns( )는 annotation 정보들을 입력 받아서 Visualization... 흐름이 주석과 함께 드러납니다.

```python
# showAnns( )는 annotation 정보들을 입력 받아서 Visualization 시켜줌. 단 먼저 matplotlib 객체로 원본 이미지가 먼저 로드되어 있어야 함.
plt.figure(figsize=(10,12))
plt.imshow(image_array)
plt.axis("off")

coco.showAnns(anns)
```

### polylines- open cv

`polylines- open cv`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
   draw_img = cv2.polylines(draw_img, [polygon_xy], True, (0, 255, 0))
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
