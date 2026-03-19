---
title: "UNet"
date: 2026-03-08
research_tab: "DL"
research_kind: "Archive Note"
source_title: "(실습)UNet"
source_path: "12_Deep_Learning/Code_Snippets/(실습)UNet.md"
excerpt: "DL Archive Note note with implementation details and archived source context."
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
| Code Blocks | 11 |
| Execution Cells | 8 |
| Libraries | `os`, `numpy`, `PIL`, `torch`, `torchvision`, `matplotlib`, `pdb` |
| Source Note | `(실습)UNet` |

## What I Worked On

- This archived note is categorized as `Archive Note` under `DL`.

## Implementation Flow

1. Review the archived source note.
2. Inspect the main implementation blocks.
3. Reuse the extracted approach in a full project page if needed.

## Code Highlights

### from pdb import run

```python
from pdb import run
#@title 학습/평가 함수
def train(model, dataloader, optimizer, criterion, device):
    model.train()
    running_loss = 0.0
    for imgs, masks in dataloader:
        imgs = imgs.to(device)
        masks = masks.to(device)

        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, masks)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * imgs.size(0)
    epoch_loss = running_loss / len(dataloader.dataset)
    return epoch_loss

def evaluate(model, dataloader, criterion, device):
    model.eval()
    running_loss = 0.0
    with torch.no_grad():
        for imgs, masks in dataloader:
            imgs.to(device)
            masks.to(device)
            outputs = model(imgs)
            loss = criterion(outputs, masks)
# ... trimmed ...
```

### @title 학습 루프

```python
#@title 학습 루프
num_epochs = 2
batch_size = 4
lr = 1e-4

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

dataset = PennFudanDataset(root="/content/data/PennFudanPed", transform=joint_transform)

train_size = int(0.8* len(dataset))
val_size = len(dataset)-train_size
train_dataset, val_dataset = torch.utils.data.random_split(dataset, [train_size, val_size])

train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_dataloader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

model = UNet(n_ch=3, n_classes=2).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

best_val_loss = float('inf')
for epoch in range(num_epochs):
    train_loss = train(model, train_dataloader, optimizer, criterion, device)
    val_loss = evaluate(model, val_dataloader, criterion, device)
    print(f"Epoch {epoch+1}/{num_epochs} , Train Loss : {train_loss:.4f}, Val Loss : {val_loss:.4f}")
    if val_loss < best_val_loss:
        best_val_loss = val_loss
        torch.save(model.state_dict(), 'best_unet.pt')
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/(실습)UNet.md`
- Source formats: `md`
- Companion files: `(실습)UNet.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `2025.10.1,2,13,14.md`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`, `www.cis.upenn.edu`

## Note Preview

> No prose preview was available in the source note.
