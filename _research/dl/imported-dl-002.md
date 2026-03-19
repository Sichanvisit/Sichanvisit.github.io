---
title: "AutoEncoder"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)AutoEncoder"
source_path: "12_Deep_Learning/Code_Snippets/(실습)AutoEncoder.md"
excerpt: "DL Archive Note: 오토인코더 구현 (MNIST), 기본 전처리 + 데이터 로드, 모델 생성 및 학습"
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
| Code Blocks | 22 |
| Execution Cells | 21 |
| Libraries | `numpy`, `matplotlib`, `torch`, `torchvision`, `plotly` |
| Source Note | `(실습)AutoEncoder` |

## What I Worked On

- 오토인코더 구현 (MNIST)
- 기본 전처리 + 데이터 로드
- 모델 생성 및 학습
- 모델 생성
- Basic Auto Encoder

## Implementation Flow

1. 오토인코더 구현 (MNIST)
2. 기본 전처리 + 데이터 로드
3. 모델 생성 및 학습
4. 모델 생성
5. Basic Auto Encoder
6. BasicAutoEncoder

## Code Highlights

### 3D view

```python
# BasicAutoEncoder 2
class BasicAutoEncoder2(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(28*28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 3),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(3, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 28*28),
            nn.Sigmoid()
        )
    def forward(self, x):
        latent = self.encoder(x)
        x = self.decoder(latent)
        return x
```

### CNN Auto Encoder

```python
# 모델 학습
model = CNNAutoEncoder().to(device)
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 학습 루프
epochs = 10
num_ch = 5

plt.figure(figsize=(20,10))

for epoch in range(epochs):
    model.train()
    running_loss = 0.
    for data in train_loader:
        inputs = data[0].to(device)
        outputs, encoded = model(inputs)

        loss = loss_fn(outputs,inputs)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        running_loss += loss.item()

    for c in range(num_ch):
        ax = plt.subplot(num_ch, epochs, epoch + c * epochs+1)
        encoded_img_channel = encoded[epoch, c, :,:].detach().cpu().numpy()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)AutoEncoder.md`
- Source formats: `md`
- Companion files: `(실습)AutoEncoder.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2025.10.1,2,13,14.md`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> No prose preview was available in the source note.
