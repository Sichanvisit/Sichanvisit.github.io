---
title: "Segmentation 데이터다루기"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Segmentation_데이터다루기"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Segmentation_데이터다루기.md"
excerpt: "하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨"
research_summary: "하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨. 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보. `md` 원본과 47개 코드 블록, 41개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pycocotools, numpy, os, json입니다."
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

하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨. 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보. `md` 원본과 47개 코드 블록, 41개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 pycocotools, numpy, os, json입니다.

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

하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨

### Annotation의 유형

바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보

### 데이터셋 분할 및 버전

분할 (Train/Val/Test): - 학습, 검증, 평가 용도로 분리되어 있으며, 실습 시 데이터 분할에 따라 적절한 셋을 사용

### COCO API 활용

pycocotools 라이브러리: - COCO 데이터를 쉽게 로드하고 탐색, 시각화할 수 있도록 도와주는 API 제공 - 설치 시 pip보다 conda 또는 GitHub 소스코드를 이용하는 방법 추천

## Implementation Flow

1. 데이터 구조 이해: 하나의 JSON 파일 - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨
2. Annotation의 유형: 바운딩 박스 (Bounding Box): - 객체의 위치와 크기를 나타내는 사각형 정보
3. 데이터셋 분할 및 버전: 분할 (Train/Val/Test): - 학습, 검증, 평가 용도로 분리되어 있으며, 실습 시 데이터 분할에 따라 적절한 셋을 사용
4. COCO API 활용: pycocotools 라이브러리: - COCO 데이터를 쉽게 로드하고 탐색, 시각화할 수 있도록 도와주는 API 제공 - 설치 시 pip보다 conda 또는 GitHub 소스코드를 이용하는 방법 추천

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
