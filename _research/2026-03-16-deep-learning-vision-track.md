---
title: "Deep Learning Vision Track"
date: 2026-03-16
research_tab: "DL"
research_kind: "Track Overview"
excerpt: "PyTorch 기초에서 Object Detection, Segmentation, Image Generation까지 확장한 딥러닝 비전 실습 아카이브입니다."
tags:
  - deep-learning
  - pytorch
  - computer-vision
  - object-detection
  - gan
header:
  teaser: /assets/images/research/dl-vision.svg
classes: wide
---

## Research Snapshot

| Item | Summary |
|------|---------|
| Scope | PyTorch 기초, CNN/RNN, 사전학습 모델, Detection, Segmentation, Generation |
| Main Stack | PyTorch, torchvision, matplotlib, NumPy |
| Core Question | 분류를 넘어 위치와 형태, 생성까지 딥러닝 모델을 어떻게 확장할 것인가 |
| Portfolio Angle | 모델 이름 암기보다 태스크별 평가와 데이터 처리 흐름을 이해한 기록 |

## Core Progression

- `PyTorch_텐서_살펴보기`, `PyTorch_데이터`, `PyTorch_모델`로 기초 문법과 데이터 파이프라인을 정리했습니다.
- `PyTorch_DNN기초`, `CNN_이미지 분류`, `RNN` 실습으로 기본 신경망 구조를 직접 구현했습니다.
- `AlexNet`, `VGGNet`, `사전훈련모델`, `YOLOv1`, `Faster R-CNN`, `FCN`, `UNet`, `VAE`, `GAN` 노트로 대표 아키텍처를 폭넓게 복습했습니다.
- 이후 스프린트 미션에서는 분류에서 끝나지 않고 탐지, 분할, 생성으로 문제 유형을 확장했습니다.

## Highlighted Artifacts

| Artifact | Focus | Why It Matters |
|----------|-------|----------------|
| `Mission_7_강사공유` / `[스프린트_미션]7_Object_Detection` | SSD 기반 개/고양이 얼굴 탐지, `IoU`, `AP`, `mAP` 계산 | 컴퓨터 비전 평가 지표를 직접 구현하고 이해한 흔적입니다. |
| `Mission_8_강사공유` | 축구 장면 semantic segmentation, `U-Net`, `Dice loss`, `IoU` 관점 | 픽셀 단위 예측으로 문제 난이도가 한 단계 올라간 사례입니다. |
| `Mission 9_이미지 생성` | FashionMNIST 조건부 생성, `cGAN`, BCE loss, 생성 샘플 확인 | 생성형 모델 학습 안정화와 조건부 생성 흐름을 경험했습니다. |
| 아키텍처 실습 묶음 | AlexNet, VGG, YOLO, Faster R-CNN, FCN, VAE, GAN | 대표 모델을 태스크 맥락 속에서 연결해 볼 수 있습니다. |

## What Changed in My Practice

### From Accuracy to Task-Specific Metrics

기초 분류 실습에서는 정확도 중심으로 모델을 봤지만, 비전 미션으로 넘어오면서 기준이 완전히 달라졌습니다.  
탐지에서는 박스를 얼마나 잘 맞추는지가 중요했고, 분할에서는 픽셀 단위 겹침 정도가 중요했으며, 생성에서는 샘플 품질과 학습 안정성이 핵심이었습니다.

### From Model Study to Pipeline Thinking

PyTorch 비전 실습을 하면서 모델 정의 자체보다도 데이터셋 구성, 시각화, 전처리, 배치 단위 추론, 결과 확인 루프가 훨씬 중요하다는 점을 배웠습니다.  
특히 Detection과 Segmentation 미션은 "모델 한 줄 호출"이 아니라, 예측 결과를 해석하고 평가하는 보조 코드까지 포함되어야 제대로 끝나는 작업이었습니다.

## Portfolio Reading

이 트랙은 "딥러닝 모델을 안다"보다 "문제에 따라 다른 출력 형식과 평가 방식을 다룰 수 있다"는 점을 보여줍니다.

- 분류: 이미지 클래스 예측
- 탐지: 객체 위치와 클래스 동시 예측
- 분할: 픽셀 단위 마스크 예측
- 생성: 조건에 맞는 샘플 생성

한 트랙 안에서 이 흐름을 밟았다는 점이, 이후 멀티모달 프로젝트나 생성형 비전 프로젝트로 확장하기 좋은 기반이라고 생각합니다.

## Next Experiments

- Detection 미션을 `Faster R-CNN` 또는 `YOLO` 계열로 다시 비교하기
- Segmentation 미션에 augmentation과 class imbalance 대응을 더해보기
- GAN/VAE 실습을 실제 프로젝트용 이미지 생성 파이프라인으로 연결하기
