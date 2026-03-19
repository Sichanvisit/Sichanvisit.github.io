---
title: "7 Object Detection"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "[스프린트_미션]7_Object_Detection"
source_path: "12_Deep_Learning/Code_Snippets/[스프린트_미션]7_Object_Detection.md"
excerpt: "DL Archive Note: 데이터 탐색 및 불러오기, Object Detection 시각화, 데이터셋 준비"
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
| Code Blocks | 27 |
| Execution Cells | 17 |
| Libraries | `kagglehub`, `torch`, `pandas`, `os`, `cv2`, `matplotlib`, `xml`, `torchvision` |
| Source Note | `[스프린트_미션]7_Object_Detection` |

## What I Worked On

- 데이터 탐색 및 불러오기
- Download latest version
- GPU 설정
- 파일 경로 설정
- 이미지, Annotation 경로 설정

## Implementation Flow

1. 데이터 탐색 및 불러오기
2. Download latest version
3. GPU 설정
4. 파일 경로 설정
5. 이미지, Annotation 경로 설정
6. Train/Validation 파일 읽기

## Code Highlights

### 데이터셋 준비

```python
from PIL import Image
from torch.utils.data import Dataset

class VOCDataset(Dataset):
    def __init__(self, image_dir, annotation_dir, classes, image_list, transforms=None):
        self.image_dir = image_dir
        self.annotation_dir = annotation_dir
        self.classes = classes
        self.transforms = transforms
        self.image_files = image_list # 미리 필터링된 유효한 이미지 파일 리스트

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        # 이미지 및 XML 파일 경로 설정
        image_file = self.image_files[idx] + ".jpg"
        annotation_file = self.image_files[idx] + ".xml"
        image_path = os.path.join(self.image_dir, image_file)
        annotation_path = os.path.join(self.annotation_dir, annotation_file)

        # 이미지 로드
        image = Image.open(image_path).convert("RGB")

        # 어노테이션 로드
        boxes = []
        labels = []
        tree = ET.parse(annotation_path)
# ... trimmed ...
```

### 모델 학습 및 평가

```python
from tqdm import tqdm # 진행 상황 시각화
import torch

# Training + Validation Loop
num_epochs = 5

for epoch in range(num_epochs):
    print(f"Epoch {epoch + 1}/{num_epochs} 시작")

    # Training Phase
    model.train()
    total_train_loss = 0

    for images, targets in tqdm(train_loader, desc="Training"):
        images = [img.to(device) for img in images]
        targets = [{k: v.to(device) for k, v in t.items()} for t in targets]

        # Forward pass
        loss_dict = model(images, targets)
        losses = sum(loss for loss in loss_dict.values())
        total_train_loss += losses.item()

        # Backward pass and optimization
        optimizer.zero_grad()
        losses.backward()
        optimizer.step()

    avg_train_loss = total_train_loss / len(train_loader)
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/[스프린트_미션]7_Object_Detection.md`
- Source formats: `md`
- Companion files: `[스프린트_미션]7_Object_Detection.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `x_min, y_min, x_max, y_max`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
