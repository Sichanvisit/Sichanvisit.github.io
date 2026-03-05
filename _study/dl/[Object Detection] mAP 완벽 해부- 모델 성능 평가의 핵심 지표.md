---
title: "[Object Detection] mAP 완벽 해부: 모델 성능 평가의 핵심 지표"
date: 2026-03-05
study_tab: "DL"
tags:
  - DL
  - Object-Detection
  - mAP
  - AP
  - IoU
  - Precision
  - Recall
  - COCO
  - Pascal-VOC
excerpt: "객체 인식 평가의 핵심 지표인 Precision/Recall/AP/mAP/IoU와 VOC·COCO 기준 차이를 실무 관점에서 정리한 노트."
header:
  teaser: /assets/images/profile.png
---

객체 인식 모델의 성능 평가는 단순 분류 정확도로 끝나지 않습니다.  
무엇을 맞췄는지뿐 아니라, **어디를 얼마나 정확히 찾았는지**까지 함께 봐야 하며, 이를 종합하는 대표 지표가 **mAP**입니다.

## 1. 기본기: Precision과 Recall

| 지표 | 정의 | 수식 |
|---|---|---|
| Precision | 모델이 정답이라 예측한 것 중 실제 정답 비율 | `TP / (TP + FP)` |
| Recall | 실제 정답 중 모델이 찾아낸 비율 | `TP / (TP + FN)` |

- TP: True Positive
- FP: False Positive (오탐)
- FN: False Negative (미탐)

두 지표는 임계값(confidence threshold)에 따라 트레이드오프 관계를 가집니다.

## 2. 단일 클래스 성능: AP

**AP (Average Precision)**는 한 클래스에 대한 Precision-Recall 곡선 아래 면적입니다.

- 임계값을 바꾸며 P-R 관계를 관찰
- 곡선 면적이 클수록 다양한 조건에서 성능이 안정적

즉, AP는 “단일 클래스 종합 성적표”입니다.

## 3. 전체 클래스 성능: mAP

**mAP (mean AP)**는 클래스별 AP 평균값입니다.

\[
\text{mAP} = \frac{1}{N}\sum_{i=1}^{N} AP_i
\]

예시:
- 사람 AP: 88
- 자동차 AP: 91
- 자전거 AP: 80
- mAP = 86.3

mAP는 모델이 특정 클래스에 편향되지 않고 전반적으로 잘 작동하는지 보여줍니다.

## 4. TP 판정 핵심: IoU

객체 인식에서는 클래스뿐 아니라 위치 정확도도 필요합니다.

\[
IoU = \frac{\text{예측 박스 ∩ 정답 박스}}{\text{예측 박스 ∪ 정답 박스}}
\]

TP로 인정되려면:
1. 클래스가 맞고
2. IoU가 기준값 이상이어야 합니다.

예: `IoU >= 0.5` 조건에서만 TP 처리.

## 5. 평가 기준 차이: VOC vs COCO

| 기준 | 설정 | 특징 |
|---|---|---|
| Pascal VOC | `mAP@0.5` (AP50) | 상대적으로 관대한 기준 |
| MS COCO | `mAP@[.5:.95]` | 여러 IoU 임계값 평균, 더 엄격 |

같은 모델이라도 COCO 기준 mAP가 더 낮게 나오는 경우가 일반적입니다.

## 결론

mAP는 객체 인식 모델의 “종합 성적표”입니다.

- 분류 정확성
- 위치 정밀도
- 클래스 전반 안정성

이 세 요소를 함께 반영합니다.  
YOLO, SSD, Faster R-CNN, DETR 등 어떤 탐지기든 mAP 해석 능력이 있어야 모델의 강점/약점을 정확히 진단할 수 있습니다.

