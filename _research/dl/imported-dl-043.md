---
title: "AutoEncoder samplecode"
date: 2026-03-08
research_tab: "DL"
research_kind: "Sample Code"
source_title: "AutoEncoder_samplecode"
source_path: "12_Deep_Learning/Code_Snippets/AutoEncoder_samplecode.md"
excerpt: "DL Sample Code: Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32), Decoder : Dense(32 -> 64), Dense(64 -> 128), Dense(128 -> 784), mod..."
tags:
  - research-archive
  - imported-note
  - dl
  - sample-code
---

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Sample Code |
| Source Files | `md` |
| Code Blocks | 10 |
| Execution Cells | 10 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy` |
| Source Note | `AutoEncoder_samplecode` |

## What I Worked On

- Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)
- Decoder : Dense(32 -> 64), Dense(64 -> 128), Dense(128 -> 784)
- model = AE()
- Training
- images_flat = images.view(images.size(0), -1)

## Implementation Flow

1. Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)
2. Decoder : Dense(32 -> 64), Dense(64 -> 128), Dense(128 -> 784)
3. model = AE()
4. Training
5. images_flat = images.view(images.size(0), -1)
6. recon_images_flat, encoded = model(images.to(device))

## Code Highlights

### Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)

```python
# Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)
# Decoder : Dense(32 -> 64), Dense(64 -> 128), Dense(128 -> 784)

class AE(nn.Module):
    def __init__(self):
        super(AE, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(784, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32)
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 784)
        )
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)

        return decoded, encoded
```

### class CNNAE(nn.Module)

```python
class CNNAE(nn.Module):
    def __init__(self):
        super(CNNAE, self).__init__()
        #Encoder
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        #Decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(32, 16, kernel_size=2, stride=2),
            nn.ReLU(),
            nn.ConvTranspose2d(16, 1, kernel_size=2, stride=2),
            nn.Sigmoid()
        )
    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded, encoded
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/AutoEncoder_samplecode.md`
- Source formats: `md`
- Companion files: `AutoEncoder_samplecode.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> -
