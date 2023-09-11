# 차량 번호판 인식 AI 모델 개발, 차량 출입 관리 웹 서비스 개발하기

## 1. 프로젝트 소개 
- 개요: AI 모델을 통해 출입하는 차량의 번호판을 판별하고, 그 기록을 관리하는 웹서비스
- 활용 데이터 : 현장 CCTV 사진, 번호판 사진
- 기간: 2023. 08.21 ~

## 2. 목차
1. [프로젝트 소개](#1-프로젝트-소개)
2. [목차](#2-목차)
3. [팀원](#3-팀원)  
4. [기술 스택](#4-활용-스택)  
5. [주요 기능](#5-주요-기능)    
6. [서비스 아키텍처](#6-서비스-아키텍처)   
7. [데이터 라벨링](#7-데이터-라벨링)   
8. [YOLOv5 학습 진행](#8-YOLOv5-학습-진행)  
9. [YOLOv5 모델 결과](#9-YOLOv5-모델-결과)  
10. [이미지 분류 데이터 전처리](#10-이미지-분류-데이터-전처리)
11. [이미지 모델 분류 (사용 안함)](#11-이미지-모델-분류)
12. [최종 모델 ESRGAN, YOLOv5](#12-최종-모델)
13. [Flask 제작](#13-Flask-제작)
  
## 3. 팀원 
|<img width="200" alt="image" src="https://avatars.githubusercontent.com/u/129818813?v=4">|<img width="200" alt="image" src="https://avatars.githubusercontent.com/u/98063854?v=4">|<img width="200" alt="image" src="https://avatars.githubusercontent.com/u/70638717?v=4">|<img width="200" alt="image" src="https://avatars.githubusercontent.com/u/86204430?v=4">|
| :---------------------------------: | :-----------------------------------:| :---------------------------------: | :-----------------------------------:|
|                FrontEnd           |           Backend                       |              AI 모델 개발         |           AI 모델 개발                |       
|             김은진            |          김재민            |                          김민범                  |          최호진                      |      
|[GitHub](https://github.com/EUNJIN6131)|[GitHub](https://github.com/JaeMin1130)|[GitHub](https://github.com/sou05091/)|[GitHub](https://github.com/Gansaw/)|

## 4. 활용 스택 
<h3>Environment</h3>

- <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
- <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=black"/>
- <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/> <img width="23" src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Notion-logo.svg">
- <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&logo=Google Colab&logoColor=white"/>

- Machine Learning:  TensorFlow, PyTorch

## 5. 주요 기능 
- [ ] YOLOv5 활용 차량 번호판 객체 인식
- [ ] 출입 차량 번호판 이미지 추출
- [ ] 차량 번호판 이미지 분류
- [ ] 새로운 차량에 대해서 이미지 저장 후 학습 진행

## 6. 서비스 아키텍처
![image](https://file.notion.so/f/s/b1f81bed-4a33-426d-8f3c-85a73c8aa7f9/Untitled.png?id=3b1e2af4-ea4b-4f7a-ba89-b32098c778d0&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693324800000&signature=XY71KiivZQHGlN8Muvvvrn_yvKrbZ7PYf68mO5zJyf8&downloadName=Untitled.png)

## 7. 데이터 라벨링
### YOLOv5 라벨링 RoboFlow 사용 (최호진 라벨링 진행)
![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/yolo/RoboFlow%20%EC%82%AC%EC%9A%A9.png)
### txt파일 Export
![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/yolo/Export.png)

## 8. YOLOv5 학습 진행
### Colab에서 모델 학습 진행 (라벨링 데이터 1000장 사용)
![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/yolo/model%20%ED%95%99%EC%8A%B5.png)

## 9. YOLOv5 모델 결과
### 전체 이미지 객체 인식
![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/yolo/result.png)
### 번호판 객체 이미지 저장
![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/yolo/result1.jpg)

## 10. 이미지 분류 데이터 전처리
### 데이터 전처리
- 이미지 분류 진행 (7월달에 출입한 모든 차량, 64개 class사용)
- class간 데이터 불균형 발생 (이미지 수가 작은 class에 대해 데이터 증강 적용)
- 분류된 이미지 번호판 판단
- 이미지 화질 판단 수작업

![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/classfication/folder.png)

## 11. 이미지 모델 분류
### 모델 제작 (모델 사용 안함)
- VGG16 사용
- 상세 코드는 GitHub 참조
### 모델 결과
![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/classfication/result.png)

![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/classfication/result1.png)

#### 모델 사용 안하는 이유
- 새로운 차량이 있을시 새롭게 학습해야함
- 이미지 수가 적어 Overfiting의 경향이 보임

## 12. 최종 모델
- YOLOv5x FineTuning
- ESRGAN을 활용하여 이미지 화질 개선
- YOLOv5로 번호판의 번호예측
- EasyOCR, RoboflowOCR 기능을 추가적으로 구현
- 3가지 모델을 앙상블기법으로 결과 추론

<a href="https://sou05091.github.io/MinBeom/pdf/pdf.html">모델 결과 보고서 보러가기

## 13. Flask 제작
### AI모델 정리
- 총 5가지 모델 사용 (YOLOv5, ESRGAN, YOLOv5, EasyOCR, RoboFlowOCR)
- 3가지 모델(YOLOv5, EasyOCR, RoboFlowOCR) return값 반환 (Json 형식)

### 모델 작업 순서
- YOLOv5 번호판 객체인식 및 저장
- ESRGAN 이미지 선명도 조절 및 흑백사진으로 변환
- EasyOCR, RoboFlowOCR, YOLOv5로 번호 예측

![image](https://github.com/sou05091/MainProject_LicensePlate/blob/main/img/yolo/Flask%20%EC%82%AC%EC%9A%A9.png)
## 개발 일지 
<a href="https://shrub-snap-550.notion.site/CRUD-566be659b7bf4693a6515f408cf2f1d9?pvs=4">개발 일지 보러 가기  <img width="23" src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Notion-logo.svg"> </a>****
