---
title: "CNN 아키텍처의 진화와 딥러닝 응용 전략: 컴퓨터 비전의 큰 흐름 속에서"
date: 2025-09-28
study_tab: "DL"
tags:
  - DL
  - CNN
  - Computer-Vision
  - LeNet
  - AlexNet
  - VGG
  - GoogLeNet
  - ResNet
  - Transfer-Learning
excerpt: "LeNet-5부터 ResNet까지 CNN 아키텍처의 진화 흐름과 전이 학습 기반 실무 응용 전략을 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

컴퓨터 비전의 발전은 CNN 아키텍처의 진화와 함께 진행됐습니다.  
LeNet-5에서 시작해 AlexNet, VGG, GoogLeNet, ResNet으로 이어진 흐름은 이미지 인식/탐지 성능을 크게 끌어올렸고, 오늘날 전이 학습 기반 실무 응용의 토대가 되었습니다.

## 전통적 방식의 한계와 CNN의 등장

과거 FCN/MLP 기반 이미지 처리에는 한계가 있었습니다.

- 공간 구조 손실: Flatten 과정에서 위치 정보 소실
- 파라미터 폭증: 입력 해상도 증가 시 연결 수 급격히 증가

CNN은 합성곱 연산과 가중치 공유로 이 문제를 해결하며, 지역 특징을 계층적으로 학습하는 구조를 제시했습니다.

## CNN의 기본 구성 요소

### 1) 합성곱 층 (Convolutional Layer)

- 필터(커널)를 슬라이딩하며 특징 추출
- 가중치 공유로 파라미터 절감
- 선/텍스처/패턴 감지에 강함

### 2) 활성화 함수 (Activation Function)

- ReLU로 비선형성 확보
- 학습 속도 개선, 기울기 소실 완화

### 3) 풀링 층 (Pooling Layer)

- 공간 차원 축소로 계산 효율 향상
- 위치 변화에 대한 불변성 강화

### 4) 완전 연결 층 (Fully Connected Layer)

- 고차원 특징 통합 후 최종 분류/회귀 수행

이 구조를 통해 CNN은 저수준 특징 -> 고수준 의미로 이어지는 계층적 특징 학습을 수행합니다.

## 주요 CNN 아키텍처 발전 흐름

### 1. LeNet-5 (1998)

- 실용적인 초기 CNN 구조 제시
- 손글씨 숫자 인식에서 성능 입증

### 2. AlexNet (2012)

- ILSVRC 우승으로 딥러닝 대중화 촉발
- ReLU, Dropout, GPU 병렬 학습 적극 활용

### 3. VGGNet (2014)

- 깊이 증가의 효과를 명확히 보여줌
- 3x3 필터 반복의 단순하고 강력한 설계

### 4. GoogLeNet / Inception (2014)

- 인셉션 모듈로 멀티스케일 병렬 추출
- 1x1 병목 합성곱으로 연산량 최적화

### 5. ResNet (2015)

- Skip Connection(Residual Learning) 도입
- 초심층 네트워크 학습 안정화
- 기울기 소실 문제를 실용적으로 해결

## 딥러닝 응용 전략: 전이 학습 (Transfer Learning)

실무에서는 ImageNet 사전학습 모델을 재사용하는 전이 학습이 핵심입니다.

### 특징 추출 (Feature Extraction)

- 백본(합성곱 층) 고정
- 분류기 헤드만 교체·학습
- 데이터가 적을 때 효과적

### 미세 조정 (Fine-tuning)

- 사전학습 가중치를 초기값으로 사용
- 상위층 또는 전체를 재학습
- 도메인 차이가 크거나 데이터가 충분할 때 유리

## 결론

- LeNet-5는 기본 틀을 만들고,
- AlexNet은 딥러닝 전환점을 만들었으며,
- VGG/GoogLeNet/ResNet은 깊이·효율·학습 안정성 문제를 단계적으로 해결했습니다.

현재 CNN은 전이 학습과 결합되어 의료 영상, 자율주행, 제조 품질 검사 등 다양한 산업 문제를 해결하는 핵심 기반으로 활용됩니다.

