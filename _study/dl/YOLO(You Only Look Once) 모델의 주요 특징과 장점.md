---
title: "YOLO: 객체 검출을 단일 회귀 문제로 재정의한 혁신적 패러다임"
date: 2026-03-05
study_tab: "DL"
tags:
  - DL
  - YOLO
  - Object-Detection
  - Computer-Vision
  - Real-Time
  - One-Stage-Detector
excerpt: "YOLO가 객체 검출을 단일 회귀 문제로 바꾼 핵심 아이디어와 v1~v3 진화 포인트를 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

## 1. 서론: 객체 인식 패러다임 전환

객체 인식(Object Detection)은 “무엇(What)”과 “어디(Where)”를 동시에 해결하는 문제입니다.  
전통적으로는 R-CNN 계열의 2단계 방식(영역 제안 -> 분류)이 주류였지만, 파이프라인이 복잡하고 추론 속도가 느렸습니다.

YOLO(You Only Look Once)는 이를 **단일 단계(1-stage) 회귀 문제**로 재정의했습니다.

- 입력 이미지에서 바로 바운딩 박스 좌표 + 클래스 확률 동시 예측
- End-to-End 단일 네트워크로 실시간 검출 가능

## 2. YOLO 핵심 개념

### (1) Single Regression Problem

객체 검출을 `(x, y, w, h, class_prob)` 예측 문제로 일체화해 속도/효율을 크게 높였습니다.

### (2) End-to-End 단일 네트워크

입력을 `SxS` 그리드로 나누고 각 셀이 객체 존재 여부와 박스를 예측합니다.  
영역 제안과 분류를 분리하지 않고 한 번에 처리합니다.

### (3) 전역 문맥(Global Context) 활용

이미지 전체를 한 번에 보므로 주변 문맥까지 반영되어 일반화에 유리합니다.

## 3. YOLO v1 -> v3 발전 흐름

| 버전 | 백본 네트워크 | 핵심 특징 | 주요 개선 |
|---|---|---|---|
| YOLO v1 (2016) | Custom CNN | 단일 스케일 회귀 예측 | 실시간 검출(약 45 FPS) 출발점 |
| YOLO v2 / YOLO9000 (2017) | Darknet-19 | Anchor Box, BN 도입 | mAP 향상, 클래스 확장 |
| YOLO v3 (2018) | Darknet-53 (Residual) | 다중 스케일 예측, 독립 로지스틱 분류 | 소형 객체 성능 및 정밀도 향상 |

## 4. 주요 기술 혁신 포인트

### (1) Batch Normalization (v2)

- 학습 안정화, 일반화 개선, 과적합 완화
- 성능(mAP) 향상에 직접 기여

### (2) Anchor Box + Dimension Clustering (v2)

- 다양한 종횡비 객체 대응력 강화
- 데이터 기반 템플릿(k-means)로 재현율 개선

### (3) Multi-Scale Training (v2)

- 학습 중 입력 해상도 변경
- 속도-정확도 트레이드오프 대응력 강화

### (4) Multi-Scale Prediction (v3)

- 여러 해상도 피처맵에서 동시 예측
- 작은 객체 검출 성능 개선

### (5) Independent Logistic Classifier (v3)

- 클래스별 독립 로지스틱 예측
- 멀티라벨 상황 대응 가능

## 5. YOLO 장점 요약

- 실시간 처리 성능 우수
- 구조 단순, End-to-End 학습/운영 용이
- 전역 문맥 반영
- 다양한 입력 해상도 대응
- 속도와 정확도의 균형

## 6. 결론

YOLO는 객체 검출을 “빠른 단일 회귀 문제”로 재해석해 실시간 비전의 표준을 만든 모델 계열입니다.  
v1의 단순한 출발에서 v2의 구조 개선, v3의 다중 스케일 정밀화로 발전했고, 이후 YOLO 계열 확장의 기반이 되었습니다.

---

### 정리 요약

- YOLO: 1-stage Detector, 단일 회귀 기반
- v2: BN + Anchor + Multi-scale Training
- v3: Darknet-53 + Multi-scale Prediction + Independent Logistic
- 결과: R-CNN 계열 대비 매우 빠른 실시간 추론과 실용적 정확도 달성

