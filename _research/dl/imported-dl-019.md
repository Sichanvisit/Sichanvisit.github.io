---
title: "Autoencoder CNN - 공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Shared Note"
source_title: "10-1_Autoencoder_CNN - 공유"
source_path: "12_Deep_Learning/Code_Snippets/10-1_Autoencoder_CNN - 공유.md"
excerpt: "DL Shared Note: Latent Vactor에 noise 추가"
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
| Code Blocks | 7 |
| Execution Cells | 6 |
| Libraries | `torch`, `torchvision`, `matplotlib`, `numpy` |
| Source Note | `10-1_Autoencoder_CNN - 공유` |

## What I Worked On

- 1. 라이브러리 임포트 및 MNIST 데이터셋 로드
- 2. 오토인코더 모델 생성
- CNN 코드
- 모델 학습
- Training loop

## Implementation Flow

1. 1. 라이브러리 임포트 및 MNIST 데이터셋 로드
2. 2. 오토인코더 모델 생성
3. CNN 코드
4. 모델 학습
5. Training loop
6. Evaluation and Intermediate Result Visualization

## Code Highlights

### 모델 학습

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
