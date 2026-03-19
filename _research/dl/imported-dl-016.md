---
title: "VGGNet"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)VGGNet"
source_path: "12_Deep_Learning/Code_Snippets/(실습)VGGNet.md"
excerpt: "데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법"
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
| Code Blocks | 25 |
| Execution Cells | 25 |
| Libraries | `torch`, `torchinfo`, `os`, `torchvision`, `matplotlib`, `tqdm`, `collections`, `random` |
| Source Note | `(실습)VGGNet` |

## What I Worked On

- VGG Network
- 사전 훈련 모델 활용
- 모델
- '''D'': [64, 64, ''M'', 128, 128, ''M'', 256, 256, 256, ''M'', 512, 512, 512, ''M'',

## Implementation Flow

1. VGG Network
2. 사전 훈련 모델 활용
3. 모델
4. '''D'': [64, 64, ''M'', 128, 128, ''M'', 256, 256, 256, ''M'', 512, 512, 512, ''M'',

## Code Highlights

### VGG Network

```python
class VGG(nn.Module):
    def __init__(self, cfg, batch_norm, num_classes=1000, init_weights=True):
        super().__init__()
        self.features = self.make_layers(cfg, batch_norm)
        self.avgpool = nn.AdaptiveAvgPool2d((7,7))
        self.classifier = nn.Sequential(
            nn.Linear(512*7*7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, num_classes)
        )
        if init_weights:
            self._initialize_weigths()

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x,1)
        x = self.classifier(x)
        return x

    def _initialize_weigths(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
# ... trimmed ...
```

### 모델 활용

```python
train_acc_hist, val_acc_hist = [], []
EPOCHS = 10
for epoch in range(EPOCHS):
    # train
    model.train()
    corr = 0
    tot = 0  # correct =0, total =0
    for x,y in tqdm(train_loader, desc=f"E{epoch+1}/{EPOCHS}"):
        x,y = x.to(device), y.to(device)
        opt.zero_grad()
        out = model(x)
        loss = loss_fn(out, y)
        loss.backward()
        opt.step()

        corr += (out.argmax(1) == y).sum().item()
        tot += y.size(0)
    train_acc_hist.append(corr/tot)

    #val
    model.eval()
    corr = 0
    tot = 0
    with torch.no_grad():
        for x, y in val_loader:
            x,y = x.to(device), y.to(device)
            out = model(x)
            corr += (out.argmax(1)==y).sum().item()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)VGGNet.md`
- Source formats: `md`
- Companion files: `(실습)VGGNet.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> 데이터 전처리 - 이미지 변환은 이미지 데이터의 크기를 256으로 키웠다가 224로 중앙 자르기 수행 - 탐지하려는 객체가 중앙에 위치할 확률이 높으므로 불필요한 지역특징을 제거하기 위한 전처리 방법
> - 입력 이미지 크기를 224로 바로 리사이즈 할 수도 있지만, 그러면 검출하려는 객체의 크기가 더 작아질 수 있음
