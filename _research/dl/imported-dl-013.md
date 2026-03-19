---
title: "Segmentation 데이터다루기"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Segmentation_데이터다루기"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Segmentation_데이터다루기.md"
excerpt: "- **하나의 JSON 파일** - 모든 이미지 메타데이터, 객체 Annotation, 카테고리, 라이선스 정보가 하나의 JSON 파일(예: instances_train2017.json 또는 instances_val2017.json)에 저장됨"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

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

## What I Worked On

- 1. 데이터 구조 이해
- 2. Annotation의 유형
- 3. 데이터셋 분할 및 버전
- 4. COCO API 활용
- 5. 실습 시 유의사항

## Implementation Flow

1. 1. 데이터 구조 이해
2. 2. Annotation의 유형
3. 3. 데이터셋 분할 및 버전
4. 4. COCO API 활용
5. 5. 실습 시 유의사항
6. !wget http://images.cocodataset.org/zips/train2017.zip

## Code Highlights

### 5. 실습 시 유의사항

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
