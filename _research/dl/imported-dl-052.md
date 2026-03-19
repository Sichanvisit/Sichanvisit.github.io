---
title: "MNIST samplecode"
date: 2026-03-08
research_tab: "DL"
research_kind: "Sample Code"
source_title: "MNIST_samplecode"
source_path: "12_Deep_Learning/Code_Snippets/MNIST_samplecode.md"
excerpt: "DL Sample Code: 데이터 로더, model = MLP(input_size, hidden_size, num_cls).to(device), input_ch, hidden_size, num_cls"
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
| Code Blocks | 11 |
| Execution Cells | 11 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy` |
| Source Note | `MNIST_samplecode` |

## What I Worked On

- 데이터 로더
- model = MLP(input_size, hidden_size, num_cls).to(device)
- input_ch, hidden_size, num_cls
- 테스트 셋에서 20개 샘플 추출
- 모델 예측

## Implementation Flow

1. 데이터 로더
2. model = MLP(input_size, hidden_size, num_cls).to(device)
3. input_ch, hidden_size, num_cls
4. 테스트 셋에서 20개 샘플 추출
5. 모델 예측
6. 결과 시각화

## Code Highlights

### class CNN(nn.Module)

```python
class CNN(nn.Module):
    def __init__(self, input_ch, hidden_size, num_cls):
        super(CNN, self).__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(input_ch, hidden_size, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(hidden_size, hidden_size, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.block3 = nn.Sequential(
            nn.Conv2d(hidden_size, input_ch, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.flatten = nn.Flatten()
        self.output = nn.Linear(784, num_cls)

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)

        x = self.flatten(x)
        out = self.output(x)

        return out
```

### input_size = 784

```python
input_size = 784
hidden_size = 500
num_cls = 10
epochs = 3

# model = MLP(input_size, hidden_size, num_cls).to(device)

# input_ch, hidden_size, num_cls
model = CNN(1, 16, 10).to(device)

loss_fn = nn.CrossEntropyLoss()
optim = opt.Adam(model.parameters(), lr=0.001)

for epoch in range(epochs):
    for i, (images, labels) in enumerate(train_loader):
        # 데이터를 디바이스로 이동
        # images = images.reshape(-1,input_size)
        images = images.to(device)
        labels = labels.to(device)

        # 모델을 실행
        outputs = model(images).squeeze()
        loss = loss_fn(outputs,labels)

        # 역전파 & 옵티마이저
        optim.zero_grad()
        loss.backward()
        optim.step()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/MNIST_samplecode.md`
- Source formats: `md`
- Companion files: `MNIST_samplecode.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> -
