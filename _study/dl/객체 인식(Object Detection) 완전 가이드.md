---
title: "객체 인식(Object Detection) 완전 가이드"
date: 2026-03-05
study_tab: "DL"
tags:
  - DL
  - Object-Detection
  - Computer-Vision
  - YOLO
  - SSD
  - Faster-RCNN
  - mAP
  - IoU
excerpt: "객체 인식 프로젝트를 데이터 준비부터 모델 설계, 학습, 추론/후처리, 평가까지 5단계 로드맵으로 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

객체 인식(Object Detection)은 “무엇(What)”과 “어디(Where)”를 동시에 해결하는 문제입니다.  
즉, 클래스 분류와 위치 추정(Bounding Box)을 함께 수행해야 합니다.

## 1단계: 데이터 준비 (Data Preparation)

### 데이터셋 구성

- 이미지 파일 (JPG/PNG 등)
- 어노테이션 (Pascal VOC XML, COCO JSON 등)

### 전처리

- 입력 크기 통일 (예: 300x300, 512x512)
- 정규화 (픽셀값 스케일링)
- 박스 좌표 정규화(상대 좌표)

### 데이터 증강

- Random Crop, Flip, Rotation, Color Jitter
- 객체 탐지에서는 BBox 동기 변환이 핵심
- Albumentations가 실무에서 자주 사용됨

### DataLoader 구성

- 이미지마다 객체 개수가 다르므로 커스텀 `collate_fn` 필요

## 2단계: 모델 구조 설계 (Model Architecture)

객체 탐지 모델은 보통 3개 블록으로 구성됩니다.

### Backbone

- 이미지 특징 추출기
- 예: ResNet, VGG, MobileNet, EfficientNet

### Neck

- 멀티스케일 특징 통합
- 예: FPN, PANet

### Head

- 분류 Head: 클래스 확률 예측
- 회귀 Head: 박스 좌표 보정

## 3단계: 모델 학습 (Model Training)

### 학습 흐름

- Forward: 입력 -> Backbone/Neck/Head -> 예측
- Loss 계산
  - 분류 손실: Cross Entropy/Focal 계열
  - 위치 손실: Smooth L1, IoU/GIoU/CIoU 계열
- Backward + Optimizer Step

### 최적화 전략

- Optimizer: SGD(momentum), Adam, AdamW
- LR Scheduler: Warm-up, Cosine Annealing
- 관리: Early Stopping, Checkpoint, TensorBoard/WandB

## 4단계: 추론 및 후처리 (Inference & Post-processing)

모델 출력은 바로 사용하지 않고 정제합니다.

- Confidence Thresholding: 낮은 점수 박스 제거
- NMS(Non-Maximum Suppression): 중복 박스 제거
- 변형: Soft-NMS, Weighted-NMS

## 5단계: 성능 평가 (Evaluation)

### IoU

- 예측 박스와 GT 박스의 겹침 비율

### Precision / Recall

- Precision: 검출한 것 중 정답 비율
- Recall: 실제 객체 중 검출한 비율

### AP / mAP

- AP: PR Curve 면적
- mAP: 클래스별 AP 평균
- COCO 기준: `mAP@[.5:.95]` 사용

## 보너스: 탐지기 2가지 큰 계열

### 2-Stage Detector

- Region Proposal 후 분류/회귀
- 예: Faster R-CNN
- 장점: 정확도 높음
- 단점: 상대적으로 느림

### 1-Stage Detector

- End-to-End 직접 예측
- 예: YOLO, SSD, RetinaNet
- 장점: 빠름(실시간 유리)

## 정리

객체 인식의 본질 파이프라인은 다음 5단계로 요약됩니다.

`데이터 준비 -> 모델 구조 설계 -> 학습 -> 추론/후처리 -> 성능 평가`

모델 이름이 달라도(SSD, YOLO, Faster R-CNN) 이 기본 흐름은 공통입니다.

