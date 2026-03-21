---
title: "7 Object Detection"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "[스프린트_미션]7_Object_Detection"
source_path: "12_Deep_Learning/Code_Snippets/[스프린트_미션]7_Object_Detection.md"
excerpt: "데이터 탐색 및 불러오기, Object Detection 시각화, 데이터셋 준비 중심으로 구현 과정을 정리한 7 Object Detection 기록입니다"
research_summary: "데이터 탐색 및 불러오기, Object Detection 시각화, 데이터셋 준비 중심으로 구현 과정을 정리한 7 Object Detection 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 27개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, torch, pandas, os입니다."
research_artifacts: "md · 코드 27개 · 실행 17개"
code_block_count: 27
execution_block_count: 17
research_focus:
  - "데이터 탐색 및 불러오기"
  - "Object Detection 시각화"
  - "데이터셋 준비"
research_stack:
  - "kagglehub"
  - "torch"
  - "pandas"
  - "os"
  - "cv2"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - archive-note
---

데이터 탐색 및 불러오기, Object Detection 시각화, 데이터셋 준비 중심으로 구현 과정을 정리한 7 Object Detection 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 27개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, torch, pandas, os입니다.

**빠르게 볼 수 있는 포인트**: 데이터 탐색 및 불러오기, Object Detection 시각화, 데이터셋 준비.

**남겨둔 자료**: `md` 원본과 27개 코드 블록, 17개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 kagglehub, torch, pandas, os입니다.

**주요 스택**: `kagglehub`, `torch`, `pandas`, `os`, `cv2`

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

## What This Note Covers

- 데이터 탐색 및 불러오기
- Object Detection 시각화
- 데이터셋 준비
- SSD 모델 준비
- 모델 학습 및 평가

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. Key Step: 이미지, Annotation 경로 설정
2. Key Step: Train과 Validation에 사용될 이미지 파일 이름 리스트 생성
3. Key Step: Test에 사용될 이미지 파일 이름 리스트 생성
4. Key Step: Train 데이터에서 예제 이미지 불러오기

## Code Highlights

### 데이터셋 준비

`데이터셋 준비`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 이미지 및 XML 파일 경로 설정, 이미지 로드, 어노테이션 로드 흐름이 주석과 함께 드러납니다.

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

`모델 학습 및 평가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Training + Validation Loop, Training Phase, Forward pass 흐름이 주석과 함께 드러납니다.

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

### 모델 추론 및 시각화

`모델 추론 및 시각화`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Tensor 이미지를 (H, W, C) 형식으로 변환, Matplotlib을 사용한 이미지 시각화, Bounding Box와 클래스 이름 시각화 흐름이 주석과 함께 드러납니다.

```python
import matplotlib.patches as patches

def visualize_prediction(image, prediction, classes):
    """
    image (torch.Tensor): 추론에 사용된 이미지 (C, H, W 형식).
    prediction (dict): 모델의 예측 결과 (boxes, labels, scores 포함).
    classes (list): 클래스 이름 리스트.
    """
    # Tensor 이미지를 (H, W, C) 형식으로 변환
    image = image.permute(1, 2, 0).numpy()

    # Matplotlib을 사용한 이미지 시각화
    fig, ax = plt.subplots(1, figsize=(8, 8))
    ax.imshow(image)

    # Bounding Box와 클래스 이름 시각화
    for box, label, score in zip(prediction["boxes"], prediction["labels"], prediction["scores"]):
        if score > 0.5:  # Confidence Score 임계값
            x_min, y_min, x_max, y_max = box.tolist()
            width, height = x_max - x_min, y_max - y_min

            # Bounding Box 추가
            rect = patches.Rectangle(
                (x_min, y_min), width, height, linewidth=2, edgecolor="red", facecolor="none"
            )
            ax.add_patch(rect)

            # 클래스 이름과 Confidence Score 추가
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

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
