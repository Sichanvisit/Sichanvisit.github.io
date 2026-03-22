---
title: "AutoEncoder samplecode"
date: 2026-03-08
research_tab: "DL"
research_kind: "Sample Code"
source_title: "AutoEncoder_samplecode"
source_path: "12_Deep_Learning/Code_Snippets/AutoEncoder_samplecode.md"
excerpt: "AutoEncoder samplecode에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, trainset = torchvisio..., Encoder : Dense(784 -..., class CNNAE(nn.Module..."
research_summary: "AutoEncoder samplecode에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, trainset = torchvisio..., Encoder : Dense(784 -..., class CNNAE(nn.Module) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 10개 · 실행 10개"
code_block_count: 10
execution_block_count: 10
research_focus:
  - "Encoder"
  - "Decoder"
  - "model = AE()"
research_stack:
  - "torch"
  - "torchvision"
  - "matplotlib"
  - "numpy"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - sample-code
---

AutoEncoder samplecode에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 실험의 큰 흐름을 먼저 훑고, trainset = torchvisio..., Encoder : Dense(784 -..., class CNNAE(nn.Module) 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: Encoder, Decoder, model = AE().

**남겨둔 자료**: `md` 원본과 10개 코드 블록, 10개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `numpy`

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

## What This Note Covers

- Encoder
- Decoder
- model = AE()
- Training
- images_flat = images.view(images.size(0), -1)

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

### 학습 루프와 최적화

- 왜 필요한가: 모델을 한 번 정의했다고 바로 학습되는 것이 아니라, 손실을 계산하고 가중치를 반복적으로 갱신하는 루프가 필요합니다.
- 왜 이 방식을 쓰는가: optimizer와 scheduler를 명시적으로 두면 학습률 변화와 갱신 방식을 실험별로 비교하기 쉬워집니다.
- 원리: 예측값과 정답의 차이로 손실을 계산하고, 역전파로 기울기를 구한 뒤 optimizer가 가중치를 업데이트합니다.

### 합성곱 기반 특징 추출

- 왜 필요한가: 이미지는 인접 픽셀 관계와 지역 패턴이 중요해서, 완전연결층만으로는 공간 구조를 효율적으로 잡기 어렵습니다.
- 왜 이 방식을 쓰는가: CNN은 필터를 공유하며 지역 특징을 반복적으로 추출할 수 있어 이미지 실습의 기본 뼈대로 적합합니다.
- 원리: 작은 커널이 이미지 위를 이동하며 특징을 뽑고, 층이 깊어질수록 더 추상적인 패턴을 학습합니다.

## Implementation Flow

1. Key Step: Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)
2. Key Step: Decoder : Dense(32 -> 64), Dense(64 -> 128), Dense(128 -> 784)
3. Key Step: images_flat = images.view(images.size(0), -1)
4. Key Step: recon_images_flat, encoded = model(images.to(device))

## Code Highlights

### trainset = torchvision.datasets.MNIST(root='data',

`trainset = torchvision.datasets.MNIST(root='data',`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 학습과 평가가 배치 단위로 안정적으로 돌도록 DataLoader와 collate 구성을 잡는 부분입니다.

```python
trainset = torchvision.datasets.MNIST(root='data',
                                      train=True,
                                      transform=transforms.ToTensor(),
                                      download=True)

testset = torchvision.datasets.MNIST(root='data',
                                     train=False,
                                     transform=transforms.ToTensor(),
                                     download=True)

trainloader = torch.utils.data.DataLoader(trainset,batch_size=64, shuffle=True)
testloader = torch.utils.data.DataLoader(testset,batch_size=64, shuffle=False)
```

### Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)

`Encoder : Dense(784 -> 128), Dense(128 -> 64), Dense(64 -> 32)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Encoder : Dense(784 -> 128), Dense(128 -> 64), De..., Decoder : Dense(32 -> 64), Dense(64 -> 128), Dens..., Encoder 흐름이 주석과 함께 드러납니다.

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

`class CNNAE(nn.Module)`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Encoder, Decoder 흐름이 주석과 함께 드러납니다.

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

### loss_fn = nn.MSELoss()

`loss_fn = nn.MSELoss()`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Training, inputs = inputs.view(inputs.size(0), -1) 흐름이 주석과 함께 드러납니다.

```python
loss_fn = nn.MSELoss()
optim = opt.Adam(model.parameters(), lr=0.001)

# Training
epochs = 10

for epoch in range(epochs):
    for data in trainloader:
        inputs, _ = data
        inputs = inputs.to(device)
        # inputs = inputs.view(inputs.size(0), -1)

        optim.zero_grad()

        outputs, _ = model(inputs)
        loss = loss_fn(outputs, inputs)

        loss.backward()
        optim.step()

    print(f"epoch : {epoch}, loss : {loss}")
print("finish")
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
