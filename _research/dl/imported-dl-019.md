---
title: "Autoencoder CNN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "10-1_Autoencoder_CNN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/10-1_Autoencoder_CNN - 공유.md"
excerpt: "Latent Vactor에 noise 추가, 라이브러리 임포트 및 MNIST 데이터셋 로드, 오토인코더 모델 생성 중심으로 구현 과정을 정리한 Autoencoder CNN - 공유 기록입니다"
research_summary: "Latent Vactor에 noise 추가, 라이브러리 임포트 및 MNIST 데이터셋 로드, 오토인코더 모델 생성 중심으로 구현 과정을 정리한 Autoencoder CNN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다."
research_artifacts: "md · 코드 7개 · 실행 6개"
code_block_count: 7
execution_block_count: 6
research_focus:
  - "Latent Vactor에 noise 추가"
  - "라이브러리 임포트 및 MNIST 데이터셋 로드"
  - "오토인코더 모델 생성"
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

Latent Vactor에 noise 추가, 라이브러리 임포트 및 MNIST 데이터셋 로드, 오토인코더 모델 생성 중심으로 구현 과정을 정리한 Autoencoder CNN - 공유 기록입니다. 페이지 상단에서 문제 정의, 구현 범위, 코드 하이라이트를 먼저 확인하고 바로 원본 실습 맥락으로 내려갈 수 있게 구성했습니다. `md` 원본과 7개 코드 블록, 6개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 torch, torchvision, matplotlib, numpy입니다.

**빠르게 볼 수 있는 포인트**: Latent Vactor에 noise 추가, 라이브러리 임포트 및 MNIST 데이터셋 로드, 오토인코더 모델 생성.

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

- Latent Vactor에 noise 추가
- 라이브러리 임포트 및 MNIST 데이터셋 로드
- 오토인코더 모델 생성
- CNN 코드
- 모델 학습

## Implementation Flow

1. Key Step: 라이브러리 임포트 및 MNIST 데이터셋 로드
2. Key Step: Evaluation and Intermediate Result Visualization
3. Key Step: Latent Vactor에 noise 추가
4. Key Step: Function to generate a new image from a random latent vector

## Code Highlights

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
