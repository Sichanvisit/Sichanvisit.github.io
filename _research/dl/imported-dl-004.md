---
title: "Faster R-CNN"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)Faster R-CNN"
source_path: "12_Deep_Learning/Code_Snippets/(실습)Faster R-CNN.md"
excerpt: "COCO API : https://github.com/cocodataset/cocoapi"
research_summary: "COCO API : https://github.com/cocodataset/cocoapi. COCO 데이터는 \"ID\"를 기준으로 파싱을 해야 합니다. images. `md` 원본과 18개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, future입니다."
research_artifacts: "md · 코드 18개 · 실행 17개"
code_block_count: 18
execution_block_count: 17
research_focus:
  - "COCO API"
  - "COCO Data"
  - "COCO 데이터는 \"ID\"를 기준으로 파싱을 해야 합니다. images"
research_stack:
  - "kagglehub"
  - "os"
  - "shutil"
  - "future"
  - "json"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

COCO API : https://github.com/cocodataset/cocoapi. COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images. `md` 원본과 18개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, future입니다.

**빠르게 볼 수 있는 포인트**: COCO API, COCO Data, COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images.

**남겨둔 자료**: `md` 원본과 18개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, os, shutil, future입니다.

**주요 스택**: `kagglehub`, `os`, `shutil`, `__future__`, `json`

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

## What This Note Covers

### COCO Data

COCO API : https://github.com/cocodataset/cocoapi

### 데이터셋

COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images

### Custom Collator가 필요한 이유

아래에 기본 collate 함수의 출력과 custom collate를 적용한 최종 출력 형태를 요약했습니다.

### Key Step

"area": 174816.81699840003,

## Implementation Flow

1. COCO Data: COCO API : https://github.com/cocodataset/cocoapi
2. 데이터셋: COCO 데이터는 "ID"를 기준으로 파싱을 해야 합니다. images
3. Custom Collator가 필요한 이유: 아래에 기본 collate 함수의 출력과 custom collate를 적용한 최종 출력 형태를 요약했습니다.
4. Key Step: "area": 174816.81699840003,

## Code Highlights

### 데이터셋

`데이터셋`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 COCODataset class, customCOCO를 이용해 annotation 파일 정보 수지, 이미지 파일 경로 설정 흐름이 주석과 함께 드러납니다.

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

### Custom Collator가 필요한 이유

`Custom Collator가 필요한 이유`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 기본 collator, > (image1, image2), (target1, target2), custom collator 흐름이 주석과 함께 드러납니다.

```python
import torch
from torch.utils.data import DataLoader

image1 = torch.randn(3,300,300)
target1 ={
    'boxes' : torch.tensor([[50,50,200,200]], dtype=torch.float32),
    'labels' : torch.tensor([1])
}

image2 = torch.randn(3,400,300)
target2 ={
    'boxes' : torch.tensor([[100,100,350,350], [20,20,100,100]], dtype=torch.float32),
    'labels' : torch.tensor([2,3])
}

sample_data = [(image1,target1), (image2, target2)]

#기본 collator
loader_wo_collator = DataLoader(sample_data, batch_size=2)
# --> (image1, image2), (target1, target2)

try:
    for batch in loader_wo_collator:
        images, targets = batch
        print("Batch images shape", images.shape)
except Exception as e:
    print("기본 collator함수 사용시 에러 ", e)

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
