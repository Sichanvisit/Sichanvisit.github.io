---
title: "Faster R-CNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Faster R-CNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Faster R-CNN.md"
excerpt: "- COCO API : https://github.com/cocodataset/cocoapi"
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
| Code Blocks | 18 |
| Execution Cells | 17 |
| Libraries | `kagglehub`, `os`, `shutil`, `__future__`, `json`, `torch`, `PIL`, `torchvision` |
| Source Note | `(실습)Faster R-CNN` |

## What I Worked On

- COCO Data
- 데이터셋
- "area": 174816.81699840003,
- "iscrowd": 0,
- "image_id": 1,

## Implementation Flow

1. COCO Data
2. 데이터셋
3. "area": 174816.81699840003,
4. "iscrowd": 0,
5. "image_id": 1,
6. "bbox": [

## Code Highlights

### 데이터셋

```python
from __future__ import annotations
#@title CustomCOCO
import os
import json
import torch
from PIL import Image
from torch.utils.data import Dataset

# "area": 174816.81699840003,
# "iscrowd": 0,
# "image_id": 1,
# "bbox": [
#     1.0799999999999272,
#     187.69008000000002,
#     611.5897600000001,
#     285.84000000000003
# ],
# "category_id": 19,
# "id": 1
# },
class CustomCOCO:
    # Json 파일을 읽어서 data에 입력
    def __init__(self, annotation_file):
        with open(annotation_file, 'r') as f:
            self.data = json.load(f)

        # 이미지 정보를 'id'를 키로 하는 딕셔너리로 저장
        self.images = {img["id"]: img for img in self.data.get('images',[])} # 없으면 빈 리스트
# ... trimmed ...
```

### 데이터셋

```python
#@title COCODataset class

class COCODataset(Dataset):
    def __init__(self, root, train, transform=None):
        super().__init__()
        directory = "train" if train else "val"

        annotations_file = os.path.join(root, 'annotations', f"{directory}_annotations.json")

        # customCOCO를 이용해 annotation 파일 정보 수지
        self.coco = CustomCOCO(annotations_file)
        # 이미지 파일 경로 설정
        self.image_path = os.path.join(root, directory)
        self.transform = transform

        # COCO 데이터셋의 카테고리 정보를 저장 -->0번은 배경
        self.categories = {0:'backgroud'}
        for cat_id, cat in self.coco.cats.items():
            self.categories[cat_id] = cat['name']

        self.data = self._load_data()

    def _load_data(self):
        data = []
        for _id, img_info in self.coco.images.items():
            file_name = img_info["file_name"]
            image_path = os.path.join(self.image_path, file_name)
            image = Image.open(image_path).convert("RGB")
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)Faster R-CNN.md`
- Source formats: `md`
- Companion files: `(실습)Faster R-CNN.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `50,50,200,200`, `12_Deep_Learning_Code_Summary.md`
- External references: `github.com`, `localhost`

## Note Preview

> - COCO API : https://github.com/cocodataset/cocoapi
> MS COCO 데이터셋은 약 328000장의 이미지와 80개의 클래스로 이루어져있으나, 워낙 대규모이기 때문에 개와 고양이 클래스를 소규모로 샘플링해 실습을 진행합니다.
