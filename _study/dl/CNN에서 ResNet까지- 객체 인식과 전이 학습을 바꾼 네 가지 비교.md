---
title: "CNN에서 ResNet까지: 객체 인식과 전이 학습을 바꾼 네 가지 혁신"
date: 2025-09-30
study_tab: "DL"
tags:
  - DL
  - CNN
  - AlexNet
  - VGG
  - ResNet
  - Object-Detection
  - Segmentation
  - YOLO
  - SSD
  - U-Net
  - Transfer-Learning
excerpt: "CNN→AlexNet→VGG→ResNet 발전 흐름과 YOLO/SSD vs U-Net의 구조적 관계를 실무 관점으로 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

컴퓨터 비전의 핵심 흐름은 CNN 아키텍처의 진화와 함께 발전해 왔습니다.  
이 문서는 CNN, AlexNet, VGG, ResNet의 혁신 포인트와 객체 인식/전이 학습에 준 영향을 정리하고, YOLO·SSD와 U-Net의 관계를 비교합니다.

## 1. CNN: 모든 혁신의 기반

CNN은 개별 모델이 아니라 이미지 처리용 아키텍처 패밀리의 뿌리입니다.

핵심 기여:
- 가중치 공유/부분 연결로 파라미터 폭발 완화
- 계층적 특징 학습(저수준 -> 고수준)
- 현대 검출기의 백본(backbone) 기반 제공

전이 학습 관점:
- 초기 레이어의 범용 시각 특징(에지/텍스처)은 다양한 과제에 재사용 가능

## 2. AlexNet (2012): 딥러닝 대중화의 출발점

주요 혁신:
- ReLU 본격 도입
- Dropout 적용
- GPU 병렬 학습 확산

영향:
- ImageNet 성능 도약
- R-CNN 계열의 특징 추출기로 활용되며 탐지 성능 급상승
- 사전학습 모델 재사용 문화(전이 학습) 확산

## 3. VGGNet (2014): 깊이와 단순성의 표준화

주요 혁신:
- 작은 3x3 필터 반복으로 깊은 네트워크 구성
- 단순하고 일관된 구조

영향:
- 한동안 검출기 백본 표준으로 널리 사용(VGG-16)
- 전이 학습 베이스 모델로 높은 실무 채택

## 4. ResNet (2015): 깊이의 한계 돌파

주요 혁신:
- Residual Learning + Skip Connection
- 초심층 학습 안정화
- Bottleneck으로 연산 효율 확보

영향:
- 검출/분할 백본의 사실상 표준(ResNet-50/101)
- 현대 비전 파이프라인 전반의 기본 골격 제공

## 5. U-Net은 어디에 속하나?

U-Net은 분류/검출 백본 계열과 목적이 다릅니다.

- 목적: 픽셀 단위 분류(세그멘테이션)
- 구조: Encoder-Decoder + Skip Connection
- 출력: 박스가 아닌 픽셀 마스크

즉, YOLO/SSD와 직접 계보라기보다 “다른 문제를 푸는 특화 아키텍처”에 가깝습니다.

## 6. YOLO·SSD vs ResNet·VGG vs U-Net

### Detection 계열 (YOLO/SSD/Faster R-CNN)

- 목표: 클래스 + 박스 좌표 동시 예측
- 일반 구조: `Backbone CNN + Detection Head`
- 백본으로 ResNet/VGG/MobileNet/Darknet 등 사용

### Segmentation 계열 (U-Net/DeepLab)

- 목표: 픽셀 단위 클래스 예측
- 일반 구조: `Encoder-Decoder + Skip`

## 한눈 비교

| 문제 유형 | 질문 | 대표 모델 | 구조 특징 | Backbone 연결성 |
|---|---|---|---|---|
| Classification | 이 이미지에 무엇이 있나? | AlexNet, VGG, ResNet | 단방향 feature extractor | 모델 자체 |
| Detection | 어디에 무엇이 있나? | YOLO, SSD, Faster R-CNN | Backbone + Detection Head | ResNet/VGG 계열과 밀접 |
| Segmentation | 각 픽셀은 무엇인가? | U-Net, DeepLab | Encoder-Decoder + Skip | 세그멘테이션 특화 |

## 종합 정리

- CNN: 이미지 딥러닝의 구조적 기반
- AlexNet: 실용 딥러닝 시대 개막
- VGG: 단순·깊은 구조의 표준화
- ResNet: 초심층 학습을 가능하게 한 전환점
- YOLO/SSD: CNN 백본 위 검출기로 발전
- U-Net: 픽셀 단위 예측 중심의 별도 축

이 흐름을 이해하면 새 모델이 나와도 “분류/검출/분할 중 어디에 속하고, 어떤 백본 철학을 계승했는지”를 빠르게 판단할 수 있습니다.

