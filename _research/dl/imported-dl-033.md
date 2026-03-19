---
title: "ResNet - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-6_ResNet - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-6_ResNet - 공유.md"
excerpt: "DL Shared Note: BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록, Bottleneck: ResNet-50, ResNet-101, ResNet-152에서 사용하는 블록, ResNet 모델 클래스"
tags:
  - research-archive
  - imported-note
  - dl
  - shared-note
---

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

## What I Worked On

- BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록
- Bottleneck: ResNet-50, ResNet-101, ResNet-152에서 사용하는 블록
- ResNet 모델 클래스

## Implementation Flow

1. BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록
2. Bottleneck: ResNet-50, ResNet-101, ResNet-152에서 사용하는 블록
3. ResNet 모델 클래스

## Code Highlights

### BasicBlock: ResNet-18, ResNet-34에서 사용하는 기본 블록

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

> No prose preview was available in the source note.
