---
title: "Mission 5 강사공유"
date: 2026-03-08
research_tab: "DL"
research_kind: "Mission"
source_title: "Mission_5_강사공유"
source_path: "12_Deep_Learning/Code_Snippets/Mission_5_강사공유.md"
excerpt: "학습 손실 시각화, 모델 생성 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 학습 손실 시각화, 모델 생성, model.load_state_di... 순서로 핵심 장면을 먼저 훑고, Image Size check 함수, Transf..."
research_summary: "학습 손실 시각화, 모델 생성 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 학습 손실 시각화, 모델 생성, model.load_state_di... 순서로 핵심 장면을 먼저 훑고, Image Size check 함수, Transform 설정, DataSet Class 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 44개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, numpy, cv2입니다."
research_artifacts: "md · 코드 44개 · 실행 12개"
code_block_count: 44
execution_block_count: 12
research_focus:
  - "학습 손실 시각화"
  - "모델 생성"
  - "model.load_state_dict(torch.load(os.path.join(main_folder,\"model_unet.pth\")))"
research_stack:
  - "os"
  - "torch"
  - "numpy"
  - "cv2"
  - "matplotlib"
source_formats:
  - "md"
tags:
  - research-archive
  - imported-note
  - dl
  - mission
---

학습 손실 시각화, 모델 생성 중심의 DL 실험에서 직접 따라간 구현 흐름과 코드 증거를 다시 볼 수 있게 정리한 DL 학습 기록입니다. 본문은 학습 손실 시각화, 모델 생성, model.load_state_di... 순서로 핵심 장면을 먼저 훑고, Image Size check 함수, Transform 설정, DataSet Class 같은 코드로 실제 구현을 이어서 확인할 수 있습니다. `md` 원본과 44개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, numpy, cv2입니다.

**빠르게 볼 수 있는 포인트**: 학습 손실 시각화, 모델 생성, model.load_state_dict(torch.load(os.pat....

**남겨둔 자료**: `md` 원본과 44개 코드 블록, 12개 실행 셀을 함께 남겨 구현 흐름을 다시 따라갈 수 있게 정리했습니다. 주요 스택은 os, torch, numpy, cv2입니다.

**주요 스택**: `os`, `torch`, `numpy`, `cv2`, `matplotlib`

## Snapshot

| Item | Value |
|------|-------|
| Track | DL |
| Type | Mission |
| Source Files | `md` |
| Code Blocks | 44 |
| Execution Cells | 12 |
| Libraries | `os`, `torch`, `numpy`, `cv2`, `matplotlib`, `math`, `torchvision`, `PIL` |
| Source Note | `Mission_5_강사공유` |

## What This Note Covers

### 학습 손실 시각화

plt.figure(figsize=(6,3)) plt.plot(train_losses, label="Train Loss", marker="o") plt.xlabel("Epochs") plt.ylabel("Loss") plt.title("Training Loss") plt.legend() plt.show() def model_test(...

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### 모델 생성

model = Autoencoder().to(device) summary(model, input_size=(1, 1, 420, 540))

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### model.load_state_dict(torch.load(os.path.join(main_folder,"model_unet.pth")))

train_losses = train(20, model_unet, loss_fn, opt, train_loader, device) preds, yy= model_test(model_unet, loss_fn, val_loader, device)

- 읽을 포인트: 비전 모델이 객체나 픽셀 단위를 어떻게 예측하는지 구현으로 따라가는 구간입니다.

### RMSE 와 PSNR 계산

def calculate_rmse(original, restored): return torch.sqrt(F.mse_loss(original, restored)).item() def calculate_psnr(original, restored, max_pixel=1.0): mse = F.mse_loss(original, restored...

- 읽을 포인트: RMSE 와 PSNR 계산 아래 코드와 함께 읽으면 구현 포인트가 더 또렷해지는 구간입니다.

### 모델 학습

train_losses = train(10, model, loss_fn, opt, train_loader, device)

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

### 기존의 학습을 이어서 하기 위해 필요시 모델 load

model.load_state_dict(torch.load(os.path.join(main_folder,"model.pth"))) train_losses = train(40, model, loss_fn, opt, train_loader, device)

- 읽을 포인트: 모델 정의, 손실, 최적화 흐름을 코드로 연결해 보는 구간입니다.

## Why This Matters

### 데이터 파이프라인

- 왜 필요한가: 모델 성능 이전에 입력이 일정한 형식으로 잘 들어가야 학습과 평가가 안정적으로 반복됩니다.
- 왜 이 방식을 쓰는가: Dataset/DataLoader 구조는 데이터 읽기, 변환, 배치 처리를 분리해 코드 재사용성과 실험 반복성을 높여줍니다.
- 원리: 각 샘플을 Dataset이 제공하고, DataLoader가 이를 배치로 묶어 셔플·병렬 로딩·collate를 담당합니다.

## Implementation Flow

1. 학습 손실 시각화: plt.figure(figsize=(6,3)) plt.plot(train_losses, label="Train Loss", marker="o") plt.xlabel("Epochs") plt.ylabel("Loss") plt.title("Trai...
2. 모델 생성: model = Autoencoder().to(device) summary(model, input_size=(1, 1, 420, 540))
3. model.load_state_dict(torch.load(os.path.join(main_folder,"model_unet.pth"))): train_losses = train(20, model_unet, loss_fn, opt, train_loader, dev...
4. RMSE 와 PSNR 계산: def calculate_rmse(original, restored): return torch.sqrt(F.mse_loss(original, restored)).item() def calculate_psnr(original, resto...
5. 모델 학습: train_losses = train(10, model, loss_fn, opt, train_loader, device)
6. 기존의 학습을 이어서 하기 위해 필요시 모델 load: model.load_state_dict(torch.load(os.path.join(main_folder,"model.pth"))) train_losses = train(40, model, loss_fn, op...

## Code Highlights

### Image Size check 함수

`Image Size check 함수`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. 코드 안에서는 그레이스케일 변환, Return a tuple if multiple images were passed, ot... 흐름이 주석과 함께 드러납니다.

```python
class Grayscale:
    def __call__(self, *imgs):
        outputs = []
        for img in imgs:
            # 그레이스케일 변환
            grayscale_img = TF.rgb_to_grayscale(img)  # RGB -> Grayscale
            outputs.append(grayscale_img)
        # Return a tuple if multiple images were passed, otherwise return the single image
        if len(outputs) == 1:
            return outputs[0]
        else:
            return tuple(outputs)
```

### Transform 설정

`Transform 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. * PadToSize class를 적용할 수 있음.

```python
transform_train = v2.Compose(
    [
        v2.ToImage(),
        v2.ToDtype(torch.float32, scale=True),
        v2.Normalize(mean=[0], std=[1.0]),
        v2.RandomRotation(10),
        v2.RandomHorizontalFlip(),
        v2.RandomVerticalFlip(),
        Grayscale(),
        PadToSize(target_size=set_size),
    ]
)
transform_test = v2.Compose(
    [
        v2.ToImage(),
        v2.ToDtype(torch.float32, scale=True),
        v2.Normalize(mean=[0], std=[1.0]),
        Grayscale(),
        PadToSize(target_size=set_size),

    ]
)
```

### DataSet Class

`DataSet Class`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. * Train 이미지와 Train_cleaned 데이터를 pair로 묶어 데이터 셋 설정 * 입력으로 이미지 파일 리스트와 transform 추가 * pad to size 함수를 입력으로 받아와 처리.

```python
class Dataset(Dataset):
  def __init__(self, files, transform=None):
    self.files = files
    self.transform = transform

  def __len__(self):
    return len(self.files)

  def __getitem__(self, idx):
    data_path = os.path.join(self.files[idx])
    img = Image.open(data_path)
    clean_path = data_path.replace("train", "train_cleaned")
    clean_img = Image.open(clean_path)

    if self.transform:
        img, clean_img = self.transform(img, clean_img)

    return img.to(device), clean_img.to(device)
```

### Dataset 및 Dataloader 설정

`Dataset 및 Dataloader 설정`는 이 노트에서 핵심 구현을 보여주는 코드 블록입니다. * random_split을 이용해 데이터 분할 * 학습 batch_size : 32.

```python
train_file, val_file = random_split(datafiles, [train_size, val_size])
train_dataset = Dataset(train_file, transform=transform_train)
val_dataset = Dataset(val_file, transform=transform_test)
test_dataset = TestDataset(testfiles, transform=transform_test)

print(f"Train dataset length: {len(train_dataset)}, Test dataset length: {len(val_dataset)}")
```

## Source Bundle

- Source path: `12_Deep_Learning/Code_Snippets/Mission_5_강사공유.md`
- Source formats: `md`
- Companion files: `Mission_5_강사공유.md`
- Note type: `code-note`
- Last updated in the source vault: `2026-03-08T03:33:14`
- Related notes: `axes`, `12_Deep_Learning_Code_Summary.md`
- External references: `localhost`

## Note Preview

> - 파일 위치 주소 관련 : os - torch : torch, torch.nn, torch.optim. torch.nn.functional - torch.utils.data : Dataset, DataLoader, random_split - torchvision : torchvision.transform, v2
> * CUDA gpu가 있는 경우 cuda로 디바이스 설정 * mac - Apple 실리콘의 gpu 사용을 위해 mps 설정추가
