---
title: "Faster R-CNN에서 YOLO로: 헤드·넥·출력 구조의 진화"
date: 2025-10-12
study_tab: "DL"
tags:
  - DL
  - Object-Detection
  - Faster-RCNN
  - YOLO
  - Backbone
  - Neck
  - Head
  - NMS
excerpt: "Faster R-CNN의 2단계 구조가 YOLO 계열에서 어떻게 흡수·단순화되었는지, 헤드/넥/출력 관점으로 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

## 1. Faster R-CNN의 기준점 역할

Faster R-CNN은 객체 검출의 2-stage 표준을 확립한 모델입니다.

핵심 특징:
- RPN(Region Proposal Network) 내장으로 end-to-end 학습 가능
- 공유 feature map 기반으로 proposal + 분류/박스회귀 수행
- RoI 단위 head에서 정밀한 분류/보정
- 작은 객체/복잡 배경에서 강한 정밀도

구조 관점:
- **Backbone**: 특징 추출
- **Neck (선택적)**: FPN 등 멀티스케일 통합
- **Head (RoI head)**: classification + localization
- **Tail/Output**: 클래스 점수 + 박스 오프셋 + objectness

## 2. YOLO가 흡수·탈피한 방식

YOLO는 Faster R-CNN의 장점을 일부 흡수하면서도, 후보 기반 2단계 흐름을 단일 회귀 구조로 단순화했습니다.

### 기본 대비

- Faster R-CNN: 후보 생성 -> 후보별 정밀 분류/회귀
- YOLO: 단일 forward에서 dense prediction

이 차이가 헤드/넥 설계 철학을 갈라놓습니다.

### Backbone 진화

- YOLO v2: Darknet-19
- YOLO v3: Darknet-53 (Residual)
- 이후: CSP 기반/경량 블록/재파라미터라이제이션 등

### Neck 진화

- 초기 YOLO: Neck 약함
- v3: 다중 스케일 feature 활용
- v4/v5+: FPN/PAN/SPP 계열 융합
- 최근: attention/fusion 효율화, large-neck small-head 경향

### Head/Output 진화

- v1: grid 기반 직접 예측
- v2: anchor 도입
- v3: 클래스별 독립 로지스틱 예측
- 최근: head 경량화, assignment 개선, NMS-free 시도

## 3. 시간축 요약 (YOLO 계열)

| 버전 구간 | Backbone | Neck | Head/Output 포인트 |
|---|---|---|---|
| v1 | 초기 CNN | 거의 없음 | grid 직접 회귀 |
| v2 | Darknet-19 | 단순 보강 | anchor + objectness |
| v3 | Darknet-53 | 멀티스케일 | 독립 로지스틱 분류 |
| v4/v5 | CSP 계열 | FPN+PAN+SPP | 개선된 loss/assignment |
| v6~v8 | 경량 최적화 | 효율 fusion | 경량 head, 실시간 최적화 |
| v10/최신 | 효율 backbone | reparam + attention | NMS-free/dual assignment 시도 |

## 4. 설계 철학 비교: 얻고 잃은 것

| 항목 | Faster R-CNN 계열 | YOLO 계열 |
|---|---|---|
| 정확도(특히 작은 객체) | 강점 | 초기 약점, 최근 개선 |
| 속도/실시간성 | 상대적으로 느림 | 강점 |
| 파이프라인 복잡도 | 높음 | 낮음 |
| 모듈 독립 최적화 | 용이 | 통합 튜닝 필요 |
| 후처리 | 후보 기반 필터링 | NMS 중심, 최근 NMS-free 시도 |

요약하면, YOLO는 Faster R-CNN의 정밀도 중심 철학을 “통합·경량·실시간” 방향으로 재설계한 계열입니다.

## 5. 결론

객체 검출의 큰 흐름은 2-stage의 정밀함과 1-stage의 실시간성 사이 균형을 찾는 과정이었습니다.  
Faster R-CNN은 구조적 기준점을 제공했고, YOLO는 이를 단순화·가속화하며 실전 배포 친화적 방향으로 진화했습니다.

최근 추세는 **head 경량화 + neck 강화 + assignment 고도화 + 후처리 단순화**로 요약할 수 있습니다.

## 다음 탐구 질문

- Q1. YOLO 버전 중 어떤 계열(v5/v8/v10/DAMO-YOLO)이 가장 궁금한가?
- Q2. Head/Neck/Output 중 어디를 가장 깊게 보고 싶은가?
- Q3. 실무 타깃(모바일/드론/CCTV) 기준으로 속도·메모리 제약은 어느 정도인가?

