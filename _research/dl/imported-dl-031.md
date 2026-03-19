---
title: "VGGNet - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "5-4_VGGNet - 공유"
source_path: "12_Deep_Learning/Code_Snippets/5-4_VGGNet - 공유.md"
excerpt: "- 파이토치 : https://pytorch.org/vision/main/models.html#table-of-all-available-classification-weights - VGG-16 with ImageNet & BN : https://pytorch.or..."
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
| Code Blocks | 14 |
| Execution Cells | 11 |
| Libraries | `torch`, `torchinfo`, `os`, `torchvision`, `matplotlib`, `tqdm`, `collections`, `random` |
| Source Note | `5-4_VGGNet - 공유` |

## What I Worked On

- 사전 훈련된 모델 활용
- GPU 사용 가능 여부 확인
- model = torchvision.models.vgg16_bn(pretrained=True)
- 실습
- 라벨 해석 함수: 0 -> Cat, 1 -> Dog

## Implementation Flow

1. 사전 훈련된 모델 활용
2. GPU 사용 가능 여부 확인
3. model = torchvision.models.vgg16_bn(pretrained=True)
4. 실습
5. 라벨 해석 함수: 0 -> Cat, 1 -> Dog
6. 카테고리별로 n개의 샘플 이미지를 수집하여 시각화하는 함수

## Code Highlights

### class VGG(nn.Module)

```python
class VGG(nn.Module):

    def __init__(self, cfg, batch_norm, num_classes=1000, init_weights=True):
        super(VGG, self).__init__()
        self.features = self.make_layers(cfg, batch_norm)
        self.avgpool = nn.AdaptiveAvgPool2d((7, 7)) # 7x7 avg poolng (flatten 노드 개수 통일을 위해 adaptive pooling 사용)
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, num_classes),
        )
        if init_weights:
            self._initialize_weights()

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
# ... trimmed ...
```

### 실습

```python
import torch.nn as nn
from torchvision.models import vgg16, VGG16_Weights
from tqdm.auto import tqdm
import matplotlib.pyplot as plt

device = "cuda" if torch.cuda.is_available() else "cpu"

model = vgg16(weights=VGG16_Weights.IMAGENET1K_V1)  # 사전학습 가중치 로드 [oai_citation:6‡docs.pytorch.org](https://docs.pytorch.org/vision/main/models/generated/torchvision.models.vgg16.html?utm_source=chatgpt.com)
model.classifier[6] = nn.Linear(4096, 2)            # 1000→2 클래스로 교체
model = model.to(device)

crit = nn.CrossEntropyLoss()
optim = torch.optim.AdamW(model.parameters(), lr=3e-4, weight_decay=1e-4)  # AdamW: decoupled WD [oai_citation:7‡docs.pytorch.org](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html?utm_source=chatgpt.com)
sched = torch.optim.lr_scheduler.StepLR(optim, step_size=5, gamma=0.1) # 학습률 스케줄러: 5 epoch마다 lr를 1/10로 감소
                                                                       # → 초반에는 빠르게 학습하고, 일정 단계 이후에는 작은 lr로 미세 조정

train_acc_hist, val_acc_hist = [], []
EPOCHS = 10
for epoch in range(EPOCHS):
    # ---- Train ----
    model.train()
    corr = tot = 0
    for x,y in tqdm(train_loader, desc=f"E{epoch+1}/{EPOCHS}"):
        x,y = x.to(device), y.to(device)
        optim.zero_grad()
        out = model(x)
        loss = crit(out, y)
        loss.backward()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/5-4_VGGNet - 공유.md`
- Source formats: `md`
- Companion files: `5-4_VGGNet - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `stackoverflow.com`, `docs.pytorch.org`, `localhost`, `pytorch.org`, `www.microsoft.com`

## Note Preview

> --
> - 파이토치 : https://pytorch.org/vision/main/models.html#table-of-all-available-classification-weights - VGG-16 with ImageNet & BN : https://pytorch.org/vision/main/models/generated/torchvision.models.vgg16_bn.html#torchvision.models.VGG16_BN_Weights
