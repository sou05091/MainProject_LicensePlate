# 차량 번호판 인식 AI 모델 개발, 차량 출입 관리 웹 서비스 개발하기

## 1. 프로젝트 소개 
- 개요: AI 모델을 통해 출입하는 차량의 번호판을 판별하고, 그 기록을 관리하는 웹서비스
- 활용 데이터 : 현장 CCTV 사진, 번호판 사진
- 기간: 2023. 08.21 ~ 
- [Go to see our service](https://jaemin1130.github.io/MiniProject_MealNote/)

## 2. 팀원 
|<img width="200" alt="image" src="https://avatars.githubusercontent.com/u/129818813?v=4">|<img width="200" alt="image" src="https://avatars.githubusercontent.com/u/98063854?v=4">|<img width="200" alt="image" src="https://avatars.githubusercontent.com/u/70638717?v=4">|<img width="200" alt="image" src="https://avatars.githubusercontent.com/u/86204430?v=4">|
| :---------------------------------: | :-----------------------------------:| :---------------------------------: | :-----------------------------------:|
|                FrontEnd           |           Backend                       |              AI 모델 개발         |           AI 모델 개발                |       
|             김은진            |          김재민            |                          김민범                  |          최호진                      |      
|[GitHub](https://github.com/EUNJIN6131)|[GitHub](https://github.com/JaeMin1130)|[GitHub](https://github.com/sou05091/)|[GitHub](https://github.com/Gansaw/)|

## 3. 활용 스택 
<h3>Environment</h3>

- <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
- <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=black"/>
- <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white"/> <img width="23" src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Notion-logo.svg">
- <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&logo=Google Colab&logoColor=white"/>

- Machine Learning:  TensorFlow, PyTorch

## 4. 주요 기능 
- [ ] YOLOv5 활용 차량 번호판 객체 인식
- [ ] 출입 차량 번호판 이미지 추출
- [ ] 차량 번호판 이미지 분류
- [ ] 새로운 차량에 대해서 이미지 저장 후 학습 진행

## 5. 서비스 아키텍처
![image](https://file.notion.so/f/s/b1f81bed-4a33-426d-8f3c-85a73c8aa7f9/Untitled.png?id=3b1e2af4-ea4b-4f7a-ba89-b32098c778d0&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693324800000&signature=XY71KiivZQHGlN8Muvvvrn_yvKrbZ7PYf68mO5zJyf8&downloadName=Untitled.png)

## 6. 데이터 라벨링
### YOLOv5 라벨링 RoboFlow 사용 (최호진 라벨링 진행)
![image](https://file.notion.so/f/s/688803c3-1d08-4d3d-bfe5-efdc8f1dc474/Untitled.png?id=595984bf-ba41-45d1-82b4-a89dc1971708&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693368000000&signature=xlninWGcH0tZXGW0RYZxQhQO6W4kkkfFFX4XuQB6bbc&downloadName=Untitled.png)
### 라벨링 진행 (예시)
![image](https://file.notion.so/f/s/c4d410c2-f559-4766-a5be-a4255a37a570/Untitled.png?id=027fa699-5187-41f5-9c9d-c2a108f041cd&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693368000000&signature=70Kcv1dptcmknSm6t7LMiwOx8jv5hDRmMo5Qr1TnBLs&downloadName=Untitled.png)
### txt파일 Export
![image](https://file.notion.so/f/s/d2f1ae8d-d0eb-418e-88f0-fba8376828b2/Untitled.png?id=a235e696-a29e-4590-beab-002b2aa32b1b&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693368000000&signature=pjynem2on4YFZUG7wU9lUcdoAZTdSrqaJXV3hrfCOsU&downloadName=Untitled.png)

## 7. YOLOv5 학습 진행
### Colab에서 모델 학습 진행 (라벨링 데이터 1000장 사용)
![image](https://file.notion.so/f/s/a9341ecf-08fe-42cf-bf31-586a6d2b165a/Untitled.png?id=114dd6fd-3e1e-47e2-ab27-efbc4484d56c&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693368000000&signature=xuYyhdqo_lsTWbmSixpLqAm8NN_c4jxkxq4Ulezx0S4&downloadName=Untitled.png)

## 8. Test 웹 서비스
### Flask 사용
![image](https://file.notion.so/f/s/4c99d8d0-751e-4f8f-9e13-9d38886b0b6e/Untitled.png?id=10d2a120-7551-4b64-8c9c-8a31e10650c2&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693368000000&signature=WVEmbJ6XB7y0PLM3I5rKmxHDFDhGJkO6NBpfjs3ZNb8&downloadName=Untitled.png)
## 9. YOLOv5 모델 결과
### 전체 이미지 객체 인식
![image](https://file.notion.so/f/s/aba1a8a1-89cd-4f4a-9496-170dee735e40/2023-08-28_14-12-27-288193.png?id=76bdd566-fff5-46c7-90ca-2733cd40e49c&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693368000000&signature=xqh_kbKJektu63EnCZAfSYZR6kIoPuKX8fh4fcqSouE&downloadName=2023-08-28_14-12-27-288193.png)
### 번호판 객체 이미지 저장
![image](https://file.notion.so/f/s/018967e5-34c8-4521-912a-4fc5f2e75d35/2023-08-28_15-19-18-341637.jpg?id=3be1f49a-619a-4fb1-93e2-80cdb37d8371&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693368000000&signature=am1MqPQn92S2xa5B1wyCJgWHmQS317GXcrL8us7G7tk&downloadName=2023-08-28_15-19-18-341637.jpg)

## 10. 이미지 모델 분류 (진행중)
### 데이터 전처리
- 이미지 분류 진행 (14개 class사용, 100개 class 추가 예정)
- 데이터 분류 수작업

![image](https://file.notion.so/f/s/359cf42e-5dbe-420b-9972-b1e6070512a3/Untitled.png?id=0e731c39-8eae-4b3f-aae9-60f6db5be22c&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693389600000&signature=3BsDJ4SB6B0NtY03t5Zkw9ZX00cO9T5x3cHaK666qlM&downloadName=Untitled.png)
### 모델 제작
- VGG모델 사용 (다른 모델들도 사용 예정)
- 상세 코드는 GitHub 참조
### 모델 결과 (accuracy 더 올려야 함)
![image](https://file.notion.so/f/s/dd303162-fa56-4c99-9042-f7fbd40a1cbc/Untitled.png?id=d7ccd0d2-1b87-4882-80bc-3e4649a0d350&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693389600000&signature=bCjvAEU-oYlKEmG_v7u_Bd-KMP4quM5UCIvRfEFMaVc&downloadName=Untitled.png)

![image](https://file.notion.so/f/s/3e778283-1048-48ef-8d7d-f7351ef20b67/Untitled.png?id=08a4833e-846b-4019-ae6c-eabc8ef534bf&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693389600000&signature=sK4eaXzguECCKMxOSy6fM8usPv5-o0Uoyet13SyHAxI&downloadName=Untitled.png)

## 개발 일지 
<a href="https://shrub-snap-550.notion.site/CRUD-566be659b7bf4693a6515f408cf2f1d9?pvs=4">개발 일지 보러 가기  <img width="23" src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Notion-logo.svg"> </a>****
