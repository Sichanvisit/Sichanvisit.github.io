---
title: "CSPNet과 YOLO 백본 진화: CSPDarknet에서 NAS 기반 구조까지"
date: 2025-10-12
study_tab: "DL"
tags:
  - DL
  - CSPNet
  - YOLO
  - Backbone
  - CSPDarknet
  - C3
  - SPPF
  - NAS
  - DAMO-YOLO
excerpt: "CSP의 핵심 아이디어와 YOLO v4 이후 백본 구조 변화, v5 C3/SPPF, 최신 NAS 기반 CSP-like 설계 흐름을 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

## 1. CSP(Cross-Stage Partial Network) 기본 개념

CSPNet은 깊은 네트워크에서 발생하는 계산/그래디언트 중복을 줄이기 위해 제안된 구조입니다.

핵심 아이디어:
- 입력 feature map을 두 경로로 분할
- 한 경로는 블록 연산(Residual/CSP block) 수행
- 다른 경로는 상대적으로 짧은 bypass 경로 유지
- 후단에서 두 경로를 다시 결합

효과:
- 중복 경로 완화
- 연산량/메모리 감소
- 표현력 유지 또는 개선

YOLO 계열에서는 v4 이후 CSP 개념이 백본/넥 설계에 본격 반영됩니다.

## 2. YOLO 계열 백본 진화 흐름

| 버전 구간 | 백본 구조 | CSP 도입 여부 | 핵심 포인트 |
|---|---|---|---|
| YOLO v1/v2 | Darknet 계열 (Darknet-19 등) | 없음 | Conv-BN-Activation 중심 |
| YOLO v3 | Darknet-53 (Residual) | 없음 | 깊은 residual backbone |
| YOLO v4 | CSPDarknet 계열 | 본격 도입 | CSP + residual 결합 |
| YOLO v5 | CSPDarknet 기반 표준화 | 유지/확장 | Focus, Conv, C3, SPPF |
| YOLO v6/v7 | CSP + 경량 최적화 블록 혼합 | 유지 | Rep 계열 최적화 블록 |
| 최신 계열 / DAMO-YOLO | NAS 기반 CSP-like 혼합 구조 | 변형/자동 탐색 | latency 제약 하 구조 최적화 |

## 2.1 YOLO v5 백본 구조 요약

YOLO v5 백본은 CSPDarknet 계열이며, 대표 모듈은 다음과 같습니다.

- Focus / Stem Conv: 초기 정보 재배치 및 효율적 다운샘플링
- Conv + C3: CSP residual 블록 반복
- SPPF: 다중 receptive field 확보

구조적으로는 여러 단계 feature map(P3/P4/P5 등)을 출력해 Neck(PAN/FPN)과 연결합니다.

## 2.2 최신 흐름: NAS 기반 CSP-like 구조

최신 흐름은 고정 백본을 수작업 설계하기보다 NAS(Neural Architecture Search)로 탐색하는 방향입니다.

DAMO-YOLO 예시:
- MAE-NAS 기반으로 CSP 스타일 블록과 Res 스타일 블록을 혼합 탐색
- 지연(latency) 제약 하에서 성능/효율 균형 최적화
- “large neck, small head” 철학으로 neck 쪽 표현력을 강화

즉, CSP 철학은 유지하되, 블록 배치와 비율은 모델 스케일/하드웨어에 맞춰 자동 최적화되는 방향으로 발전하고 있습니다.

## 3. 구조도 수준 요약

```text
Input
 -> Focus/Stem Conv
 -> [Conv downsample + CSP(C3/Res) blocks]  # Backbone
 -> SPP/SPPF (optional)
 -> Multi-scale features (P3, P4, P5)
 -> Neck (FPN/PAN/RepFPN 등)
 -> Detection Heads (class + box + objectness)
 -> Post-process (NMS / NMS-free)
```

CSP의 본질은 백본 내부에서 “경로 분할 -> 부분 연산 -> 재결합”을 통해 효율과 표현력을 동시에 가져가는 데 있습니다.

## 정리

- CSP는 YOLO의 경량화/고성능 균형에 핵심 기여
- YOLO v4부터 CSPDarknet 계열이 주류
- v5에서 C3/SPPF로 구조 표준화
- 최신은 NAS 기반으로 CSP-like 철학을 하드웨어 친화적으로 재설계

