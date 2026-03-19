---
title: "FCN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "FCN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/FCN - 공유.md"
excerpt: "실습, Step 1, Step 2 중심으로 구현 과정을 정리한 FCN - 공유 기록입니다"
research_summary: "실습, Step 1, Step 2 중심으로 구현 과정을 정리한 FCN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다."
research_artifacts: "md · 코드 11개 · 실행 8개"
code_block_count: 11
execution_block_count: 8
research_focus:
  - "실습"
  - "Step 1"
  - "Step 2"
research_stack:
  - "os"
  - "json"
  - "torch"
  - "numpy"
  - "PIL"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

실습, Step 1, Step 2 중심으로 구현 과정을 정리한 FCN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**빠르게 볼 수 있는 포인트**: 실습, Step 1, Step 2.

**남겨둔 자료**: `md` 원본과 11개 코드 블록, 8개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, json, torch, numpy입니다.

**주요 스택**: `os`, `json`, `torch`, `numpy`, `PIL`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 11 |
| Execution Cells | 8 |
| Libraries | `os`, `json`, `torch`, `numpy`, `PIL`, `torchvision`, `matplotlib`, `tqdm` |
| Source Note | `FCN - 공유` |

## What This Note Covers

- 실습
- Step 1
- Step 2
- 이미지 변환
- PIL 이미지를 tensor로 변환

## Implementation Flow

1. Key Step: Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기
2. Key Step: Step 2: 이미지와 마스크에 적용할 전처리(Transform) 정의하기
3. Key Step: PIL 이미지를 tensor로 변환
4. Key Step: tensor의 데이터 타입을 float로 변경

## Code Highlights

### import os

`import os`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기, train이면 'train', 아니면 'val' 이미지를 선택합니다., torchvision의 VOCSegmentation 클래스를 사용하여 VOC 데이터셋을... 흐름이 주석과 함께 드러납니다.

```python
import os
import json
import torch
import numpy as np
from PIL import Image
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, datasets
import matplotlib.pyplot as plt

###############################################
# Step 1: VOCSegmentation 데이터셋 로드 및 클래스 정보 설정하기
###############################################
class SegmentationDataset(Dataset):
    def __init__(self, root, train=True, transform=None, target_transform=None, download=False):
        """
        VOCSegmentation 데이터셋을 로드하고, 이미지와 pixel-level segmentation mask를 반환하는 Dataset 클래스입니다.

        Args:
            root (str): 데이터셋이 저장될 루트 경로
            train (bool): True이면 training 데이터를, False이면 validation 데이터를 사용
            transform: 입력 이미지에 적용할 변환(예: 크기 조정, tensor 변환 등)
            target_transform: segmentation mask에 적용할 변환(보통 크기 조정 등, 클래스 값 보존을 위해 nearest interpolation 사용)
            download (bool): 데이터가 없으면 자동으로 다운로드할지 여부
        """
        # train이면 'train', 아니면 'val' 이미지를 선택합니다.
        image_set = 'train' if train else 'val'

        # torchvision의 VOCSegmentation 클래스를 사용하여 VOC 데이터셋을 불러옵니다.
# ... trimmed ...
```

### 실습

`실습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
!wget https://www.cis.upenn.edu/~jshi/ped_html/PennFudanPed.zip -P data
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/FCN - 공유.md`
- Source formats: `md`
- Companion files: `FCN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`

## Note Preview

> -
