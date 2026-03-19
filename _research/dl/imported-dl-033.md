---
title: "ResNet - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-6_ResNet - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-6_ResNet - 공유.md"
excerpt: "BasicBlock, Bottleneck, ResNet 모델 클래스 중심으로 구현 과정을 정리한 ResNet - 공유 기록입니다"
research_summary: "BasicBlock, Bottleneck, ResNet 모델 클래스 중심으로 구현 과정을 정리한 ResNet - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 6개 코드 블록, 4개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, torchinfo입니다."
research_artifacts: "md · 코드 6개 · 실행 4개"
code_block_count: 6
execution_block_count: 4
research_focus:
  - "BasicBlock"
  - "Bottleneck"
  - "ResNet 모델 클래스"
research_stack:
  - "torch"
  - "torchvision"
  - "torchinfo"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

BasicBlock, Bottleneck, ResNet 모델 클래스 중심으로 구현 과정을 정리한 ResNet - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 6개 코드 블록, 4개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, torchinfo입니다.

**빠르게 볼 수 있는 포인트**: BasicBlock, Bottleneck, ResNet 모델 클래스.

**남겨둔 자료**: `md` 원본과 6개 코드 블록, 4개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, torchinfo입니다.

**주요 스택**: `torch`, `torchvision`, `torchinfo`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 6 |
| Execution Cells | 4 |
| Libraries | `torch`, `torchvision`, `torchinfo` |
| Source Note | `5-6_ResNet - 공유` |

## What This Note Covers

- BasicBlock
- Bottleneck
- ResNet 모델 클래스

## Implementation Flow

1. Key Step: BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록
2. Key Step: Bottleneck: ResNet-50, ResNet-101, ResNet-152에서 사용하는 블록

## Code Highlights

### BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록

`BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록, Bottleneck: ResNet-50, ResNet-101, ResNet-152에서 사..., ResNet 모델 클래스 흐름이 주석과 함께 드러납니다.

```python
# BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록
class BasicBlock(nn.Module):
    expansion = 1  # 출력 채널 확장 비율

    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super(BasicBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3,
                               stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3,
                               stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)
# ... trimmed ...
```

### from torchvision import models

`from torchvision import models`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 원본 노트에서 구현 흐름을 가장 잘 보여주는 핵심 코드 중 하나입니다.

```python
from torchvision import models
from torchinfo import summary


resnet18 = ResNet(BasicBlock, [2, 2, 2, 2], 1000)
resnet34 = ResNet(BasicBlock, [3, 4, 6, 3], 1000)
resnet50 = ResNet(Bottleneck, [3, 4, 6, 3], 1000)
resnet101 = ResNet(Bottleneck, [3, 4, 23, 3], 1000)
resnet152 = ResNet(Bottleneck, [3, 8, 36, 3], 1000)
torch_model = models.resnet34(weights="ResNet34_Weights.IMAGENET1K_V1")

resnet34_info = summary(resnet34, (1, 3, 224, 224), verbose=0)
torch_model_info = summary(torch_model, (1, 3, 224, 224), verbose=0)

print(resnet34_info.total_params)
print(torch_model_info.total_params)
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/5-6_ResNet - 공유.md`
- Source formats: `md`
- Companion files: `5-6_ResNet - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 원본 노트에 별도 설명 문단이 많지 않아 코드 중심으로 보존했습니다.
