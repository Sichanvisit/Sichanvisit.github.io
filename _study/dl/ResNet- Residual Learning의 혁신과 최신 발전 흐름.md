---
title: "ResNet 계열 네트워크의 진화: ResNet부터 ConvNeXt까지"
date: 2025-09-28
study_tab: "DL"
tags:
  - DL
  - ResNet
  - Residual-Learning
  - ResNeXt
  - Wide-ResNet
  - Res2Net
  - ResNeSt
  - ConvNeXt
  - Computer-Vision
excerpt: "Residual Learning의 핵심 원리와 ResNet 계열(Pre-ResNet, WRN, ResNeXt, Res2Net, ResNeSt, ConvNeXt)의 발전 흐름을 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

ResNet은 단순한 CNN 모델이 아니라, 딥러닝 아키텍처 설계 패러다임을 바꾼 전환점입니다.  
핵심 아이디어인 Residual Learning은 이후 다양한 계열 모델로 확장되며 현대 비전 모델의 기반이 되었습니다.

## 1. ResNet의 혁신: 깊이의 한계를 넘다

2015년 ResNet은 “네트워크를 깊게 쌓을수록 성능이 악화되는 문제(Degradation)”를 해결했습니다.

핵심 수식:

- 목표 매핑: \(H(x)\)
- 잔차 학습: \(F(x) = H(x) - x\)
- 출력: \(y = F(x) + x\)

입력을 skip connection으로 직접 전달해, 최적화 난이도와 그래디언트 흐름 문제를 크게 완화했습니다.

## 2. ResNet 기본 블록 구조

### BasicBlock (ResNet-18/34)

- `3x3 Conv -> BN -> ReLU -> 3x3 Conv -> BN`
- skip 연결 후 `y = F(x) + x`
- 상대적으로 얕은 네트워크에 적합

### Bottleneck Block (ResNet-50/101/152)

- `1x1 Conv(축소) -> 3x3 Conv -> 1x1 Conv(복원)`
- 연산 효율을 유지하며 깊은 네트워크 구성 가능

## 3. ResNet 이후의 주요 확장

### (1) Pre-activation ResNet (ResNet v2, 2016)

- `BN -> ReLU -> Conv` 순서
- 깊은 네트워크에서 학습 안정성 및 수렴 개선

### (2) Wide ResNet (WRN, 2016)

- 깊이만 늘리는 대신 채널 폭(width) 확대
- 학습 안정성과 성능의 균형 확보

### (3) ResNeXt (2017)

- Group Convolution + Cardinality 도입
- Split-Transform-Merge 구조로 효율적 성능 향상

### (4) Res2Net (2019)

- 채널 그룹을 계층적으로 연결해 멀티스케일 표현 강화
- 탐지/분할 등 다양한 비전 과제에서 강점

### (5) ResNeSt (2020)

- Split Attention 결합
- 채널 그룹별 중요도 학습으로 표현력 향상

### (6) ConvNeXt (2022)

- ResNet을 현대적으로 재설계
- Transformer 설계 인사이트(큰 커널, LayerNorm, Depthwise Conv 등) 반영
- CNN 계열의 경쟁력 재입증

## 4. 진화 요약 표

| 모델 | 핵심 아이디어 | 특징 |
|---|---|---|
| ResNet (2015) | Residual Block + Skip | 초심층 학습 가능 |
| Pre-ResNet (2016) | Pre-activation | 그래디언트 흐름 개선 |
| Wide ResNet (2016) | 깊이보다 너비 확대 | 학습 안정성/성능 균형 |
| ResNeXt (2017) | Group Conv + Cardinality | 효율적 성능 향상 |
| Res2Net (2019) | 멀티스케일 residual | 탐지/분할에 강점 |
| ResNeSt (2020) | Split Attention | 채널 중요도 학습 강화 |
| ConvNeXt (2022) | 현대화된 CNN 설계 | ViT급 성능 경쟁 |

## 5. ResNet 계열의 전략적 가치

- 전이학습 백본 표준: ResNet-50/101은 탐지·분할 파이프라인에서 여전히 강력
- 확장성: skip connection 철학은 CNN을 넘어 다른 아키텍처에도 영향
- CNN-Transformer 연결: ConvNeXt가 두 패러다임의 경계를 좁힘

## 6. 결론

ResNet은 딥러닝의 깊이 한계를 돌파한 출발점이었고, 이후 계열 모델들은 효율성·표현력·안정성을 확장해 왔습니다.  
현재도 Residual 철학은 비전 모델 설계의 핵심 축으로 남아 있으며, 앞으로의 CNN/하이브리드 모델 진화에서도 중요한 기반이 될 것입니다.

