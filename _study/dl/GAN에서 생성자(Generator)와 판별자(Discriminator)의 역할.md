---
title: "인공지능의 창의성을 깨우다: GAN(Generative Adversarial Network) 심층 분석"
date: 2025-10-20
study_tab: "DL"
tags:
  - DL
  - GAN
  - Generative-Model
  - Adversarial-Training
  - Generator
  - Discriminator
  - Computer-Vision
excerpt: "GAN의 핵심 구조(생성자·판별자), 미니맥스 목표, 적대적 학습 루프를 수식/표와 함께 정리한 심화 노트."
header:
  teaser: /assets/images/profile.png
---

GAN(Generative Adversarial Network)은 생성자(Generator)와 판별자(Discriminator)가 경쟁적으로 학습하는 구조를 통해, 실제와 유사한 데이터를 생성하는 대표적인 생성 모델입니다.

## 1. GAN의 핵심 아이디어

GAN의 학습은 게임 이론의 미니맥스(minimax) 관점으로 해석할 수 있습니다.

\[
\min_G \max_D V(D, G)
\]

- 판별자 \(D\): 진짜/가짜를 최대한 정확히 구분
- 생성자 \(G\): 판별자를 속일 수 있는 샘플 생성

두 네트워크의 경쟁이 반복되며 생성 품질이 향상됩니다.

## 2. 생성자(Generator, G)

생성자는 잠재 벡터 \(z\)를 입력받아 가짜 데이터 \(G(z)\)를 만듭니다.

| 역할/목표 | 설명 |
|---|---|
| 데이터 생성 | 랜덤 노이즈 \(z\) -> 의미 있는 데이터 샘플 생성 |
| 판별자 속이기 | \(G(z)\)가 실제 데이터처럼 보이게 학습 |
| 손실 관점 | \(D(G(z))\)를 높이는 방향으로 학습 |
| 최종 목표 | 실제 분포 \(P_{data}\)에 가까운 샘플 생성 |

## 3. 판별자(Discriminator, D)

판별자는 입력이 진짜인지 가짜인지 구분하는 이진 분류기입니다.

| 역할/목표 | 설명 |
|---|---|
| 진위 판별 | 실제 \(x\)와 가짜 \(G(z)\)를 구분 |
| 확률 출력 | \(D(\cdot)\in[0,1]\), 1에 가까울수록 진짜 |
| 손실 관점 | \(D(x)\uparrow,\ D(G(z))\downarrow\) 되도록 학습 |
| 최종 목표 | 생성자가 고도화되어도 구분 성능 유지 |

## 4. 적대적 학습(Adversarial Training) 루프

| 단계 | 학습 대상 | 목표 | 결과 |
|---|---|---|---|
| Step 1 | 생성자 G | 잠재 벡터로 가짜 샘플 생성 | 판별자 입력 준비 |
| Step 2 | 판별자 D | 진짜는 1, 가짜는 0으로 분류 | 판별 능력 향상 |
| Step 3 | 생성자 G | \(D(G(z))\approx 1\) 되도록 갱신 | 생성 품질 향상 |

이 과정을 반복하면, 생성자는 점점 더 실제 같은 샘플을 만들고 판별자는 더 정교하게 구분하게 됩니다.

## 5. 수렴 관점

이상적으로는 두 네트워크가 균형(Nash Equilibrium)에 가까워지며, 생성 샘플이 실제 데이터와 구별 어려운 수준에 도달합니다.

실무에서는 다음 이슈를 함께 다룹니다.
- 학습 불안정성
- 모드 붕괴(Mode Collapse)
- 생성/판별 균형 붕괴

이를 완화하기 위해 WGAN, Gradient Penalty, Spectral Norm 등 다양한 개선 기법이 제안되었습니다.

## 6. 응용 분야

- 이미지 생성/복원
- 스타일 변환(Style Transfer)
- 데이터 증강(Data Augmentation)
- 초해상도(Super-Resolution)
- 도메인 변환(Domain Translation)

## 정리

GAN은 “이해”를 넘어 “생성”을 가능하게 한 딥러닝의 핵심 패러다임입니다.  
생성자와 판별자의 경쟁 학습은 단순하지만 강력하며, 현대 생성형 AI 발전의 중요한 출발점이 되었습니다.

