---
title: "딥러닝 기반 이미지 이해의 핵심: Semantic Segmentation 완벽 분석"
date: 2026-03-05
study_tab: "DL"
tags:
  - DL
  - Semantic-Segmentation
  - Computer-Vision
  - FCN
  - U-Net
  - DeepLab
  - Instance-Segmentation
excerpt: "Semantic Segmentation의 정의, 분류/탐지와의 차이, 인코더-디코더 구조, Skip Connection, Instance Segmentation 확장을 심화 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

Semantic Segmentation은 이미지의 모든 픽셀에 의미적 클래스 라벨을 부여해, 장면을 정밀하게 해석하는 컴퓨터 비전 핵심 기술입니다.

## 1. 정의와 역할

### 핵심 개념

- **Pixel-wise Classification**: 픽셀 단위 클래스 예측
- **Class-level Partition**: 같은 클래스 픽셀은 동일 레이블
- **고해상도 출력 필요**: 입력과 같은 해상도의 마스크 생성

중요 포인트:
- Semantic Segmentation은 동일 클래스 내 개별 인스턴스(사람1, 사람2)를 구분하지 않습니다.

### 주요 응용

- 자율주행: 도로/차선/보행자 분할
- 의료영상: 종양/장기 경계 추출
- 로보틱스: 환경 이해 및 조작

## 2. 분류·탐지·세그멘테이션 비교

| 구분 | 이미지 분류 | 객체 탐지 | Semantic Segmentation |
|---|---|---|---|
| 질문 | 이미지에 무엇이 있나? | 어디에 무엇이 있나? | 모든 픽셀이 무엇인가? |
| 출력 | 단일 클래스 | 박스 + 클래스 | 픽셀 단위 마스크 |
| 공간 정보 | 많이 압축됨 | 박스 수준 위치 | 픽셀 경계까지 유지 |
| 인스턴스 구분 | 없음 | 가능(박스 단위) | 없음(동일 클래스 통합) |

요약:
- 분류는 이미지 레벨 인식
- 세그멘테이션은 픽셀 레벨 이해

## 3. 네트워크 구조: FCN과 인코더-디코더

### A. 인코더 (Encoder)

- CNN(ResNet, VGG 등) 기반 특징 추출
- 다운샘플링으로 고수준 의미 특징 확보
- 공간 해상도는 감소

### B. 디코더 (Decoder)

- 업샘플링(Transposed Conv, Interpolation 등)으로 해상도 복원
- 픽셀별 클래스 확률 맵 생성

### C. Skip Connection의 중요성

- 인코더의 저수준 공간 정보를 디코더로 직접 전달
- 경계/윤곽 복원 품질 향상
- FCN, U-Net 계열에서 성능 핵심 요소

## 4. Semantic vs Instance Segmentation

| 구분 | Semantic Segmentation | Instance Segmentation |
|---|---|---|
| 목표 | 클래스만 분할 | 클래스 + 개별 인스턴스 분할 |
| 결과 | 같은 클래스는 같은 라벨 | 같은 클래스라도 객체별 라벨 분리 |
| 대상 | Stuff 중심(하늘/도로 등) | Things 중심(사람/차량 등) |
| 대표 모델 | FCN, U-Net, DeepLab | Mask R-CNN, YOLACT |

예시:
- 자동차 2대가 있을 때
  - Semantic: 둘 다 `car`
  - Instance: `car#1`, `car#2`로 분리

## 정리

Semantic Segmentation은 “무엇이 어디에 있는가”를 픽셀 단위로 해석하는 기술이며, 정밀한 공간 정보 복원이 핵심입니다.  
FCN/Encoder-Decoder/Skip Connection 구조를 이해하면, 자율주행·의료영상·산업 비전 등 고정밀 AI 문제를 체계적으로 설계할 수 있습니다.

