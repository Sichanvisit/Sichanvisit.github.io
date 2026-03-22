---
title: "Autoencoder CNN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "10-1_Autoencoder_CNN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/10-1_Autoencoder_CNN - 공유.md"
excerpt: "Autoencoder CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Latent Vactor에 nois... 순서로 핵심 장면을 먼저 훑고, 오토인코더 모델 생성, 모델 학습, Evaluation and Interm... 같은 코드로..."
research_summary: "Autoencoder CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Latent Vactor에 nois... 순서로 핵심 장면을 먼저 훑고, 오토인코더 모델 생성, 모델 학습, Evaluation and Interm... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 7개 · 실행 6개"
code_block_count: 7
execution_block_count: 6
research_focus:
  - "Latent Vactor에 noise 추가"
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
  - shared-note
---

Autoencoder CNN - 공유에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 Latent Vactor에 nois... 순서로 핵심 장면을 먼저 훑고, 오토인코더 모델 생성, 모델 학습, Evaluation and Interm... 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: Latent Vactor에 noise 추가.

**남겨둔 자료**: `md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**주요 스택**: `torch`, `torchvision`, `matplotlib`, `numpy`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Shared Note |
| Source Files | `md` |
| Code Blocks | 7 |
| Execution Cells | 6 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy` |
| Source Note | `10-1_Autoencoder_CNN - 공유` |

## What This Note Covers

### Latent Vactor에 noise 추가

Latent Vactor에 noise 추가 코드를 직접 따라가며 Latent Vactor에 noise 추가 흐름을 확인했습니다.

- 읽을 포인트: Latent Vactor에 noise 추가 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

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

1. Latent Vactor에 noise 추가: Latent Vactor에 noise 추가 코드를 직접 따라가며 Latent Vactor에 noise 추가 흐름을 확인했습니다.

## Code Highlights

### 2. 오토인코더 모델 생성

`2. 오토인코더 모델 생성`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 오토인코더 모델 생성, CNN 코드, Encoder 흐름이 주석과 함께 드러납니다.

```python
# 2. 오토인코더 모델 생성
## CNN  코드
class CNNAutoencoder(nn.Module):
    def __init__(self):
        super(CNNAutoencoder, self).__init__()
        # Encoder
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, stride=1, padding=1),
            nn.ReLU(True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1),
            nn.ReLU(True),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )
        # Decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(32, 16, kernel_size=2, stride=2),
            nn.ReLU(True),
            nn.ConvTranspose2d(16, 1, kernel_size=2, stride=2),
            nn.Sigmoid()
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded, encoded # Return both decoded image and the encoded feature map
```

### 모델 학습

`모델 학습`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 모델 학습, Training loop, You can optionally save the trained model 흐름이 주석과 함께 드러납니다.

```python
# 모델 학습
model = CNNAutoencoder()
criterion = nn.MSELoss() # Mean Squared Error loss for autoencoders
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 3
num_channels_to_show = 5

plt.figure(figsize=(20, 10))

for epoch in range(num_epochs):
    model.train() # Set the model to training mode
    running_loss = 0.0
    for data in trainloader:
        inputs, _ = data # Autoencoder input is the image itself, ignore the label
        optimizer.zero_grad() # Zero the parameter gradients

        outputs, encoded_feat = model(inputs) # Forward pass

        loss = criterion(outputs, inputs) # Calculate the loss

        loss.backward() # Backward pass
        optimizer.step() # Optimize

        running_loss += loss.item()

    for c in range(num_channels_to_show):
# ... trimmed ...
```

### Evaluation and Intermediate Result Visualization

`Evaluation and Intermediate Result Visualization`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Evaluation and Intermediate Result Visualization, Get a batch of test data, Forward pass through the autoencoder 흐름이 주석과 함께 드러납니다.

```python
# Evaluation and Intermediate Result Visualization

model.eval() # Set the model to evaluation mode
with torch.no_grad(): # No need to calculate gradients
    # Get a batch of test data
    dataiter = iter(testloader)
    images, labels = next(dataiter)

    # Forward pass through the autoencoder
    decoded_images, encoded_features = model(images)

    # Compare original images, encoded representations, and decoded images
    n = 10  # Number of images to display
    num_channels_to_show = 6 # You can adjust this

    plt.figure(figsize=(20, 10))
    for i in range(n):
        # Original Images
        ax = plt.subplot(num_channels_to_show+2, n, i + 1)
        # Unnormalize the image for display (reverse the normalization done during preprocessing)
        img = images[i].cpu().numpy() * 0.5 + 0.5
        plt.imshow(np.transpose(img.squeeze(), (0, 1)), cmap='gray')
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        if i == 0:
            ax.set_title("Original")

        # Intermediate Encoded Feature Maps (Example of visualizing the output of the last encoder layer)
# ... trimmed ...
```

### Latent Vactor에 noise 추가

`Latent Vactor에 noise 추가`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 Function to generate a new image from a random la..., Create a random latent vector (matching the shape..., The shape of the encoded features is [batch_size,... 흐름이 주석과 함께 드러납니다.

```python
import matplotlib.pyplot as plt
# Function to generate a new image from a random latent vector
def generate_image(model):
    smple_num = 34
    model.eval()  # Set the model to evaluation mode
    with torch.no_grad():
        # Create a random latent vector (matching the shape of the encoded features)
        # The shape of the encoded features is [batch_size, 32, 7, 7] based on the model definition.
        # For a single generated image, the batch size is 1.
        # random_latent_vector = encoded_features[smple_num].unsqueeze(0) + torch.randn(1, 32, 7, 7)
        random_latent_vector = encoded_features[smple_num].unsqueeze(0) * 0.7 +0.9

        # Pass the random latent vector through the decoder part of the model
        # We need to access the decoder directly.
        generated_image = model.decoder(random_latent_vector)

        # Unnormalize and convert to numpy for plotting
        # Since the decoder output has Sigmoid, it's already in [0, 1].
        generated_img_np = generated_image.squeeze().cpu().numpy()

        plt.figure(figsize=(5, 5))
        plt.subplot(2,1,1)
        plt.imshow(images[smple_num].squeeze(), cmap='gray')
        plt.subplot(2,1,2)
        plt.imshow(generated_img_np, cmap='gray')
        plt.title("Generated Image")
        plt.axis('off')
        plt.show()
# ... trimmed ...
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/10-1_Autoencoder_CNN - 공유.md`
- Source formats: `md`
- Companion files: `10-1_Autoencoder_CNN - 공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> -
