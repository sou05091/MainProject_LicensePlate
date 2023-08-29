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
<div>
  <img src="https://img.shields.io/badge/vscode 1.18.1-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
</div>
<h3>Communication</h3>
<div>
  <a href="https://shrub-snap-550.notion.site/6e3827cac0a846c393106e0dfec6ac6e?v=c805bf85a004454695cc77a7968262b5&pvs=4"><img src="https://img.shields.io/badge/notion-000000?style=for-the-badge&logo=notion&logoColor=white"> </a>
    <a href="https://github.com/EUNJIN6131/MiniProject_LicensePlate"><img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"></a>
</div>

## 4. 주요 기능 
- [ ] YOLOv5 활용 차량 번호판 객체 인식
- [ ] 출입 차량 번호판 이미지 추출
- [ ] 차량 번호판 이미지 분류
- [ ] 새로운 차량에 대해서 이미지 저장 후 학습 진행

## 5. 서비스 아키텍처
![image](https://file.notion.so/f/s/b1f81bed-4a33-426d-8f3c-85a73c8aa7f9/Untitled.png?id=3b1e2af4-ea4b-4f7a-ba89-b32098c778d0&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693324800000&signature=XY71KiivZQHGlN8Muvvvrn_yvKrbZ7PYf68mO5zJyf8&downloadName=Untitled.png)

## 6. 데이터 라벨링
- [YOLOv5] RoboFlow 웹사이트 이용
![image](https://www.notion.so/RoboFlow-YOLOv5-f4babf5a57d041d9a426e28ed86ecc5d?pvs=4#595984bfba4145d182b4a89dc1971708)
## 7. REST API 명세 
### Spring Boot
| ID | Method | URI | Params | Return | Description |
| --- | --- | --- | --- | --- | --- |
| 1 | POST  | /user/signup | UserDto userDto | Boolean | 회원가입 |
| 2 | POST | /user/signin | UserDto userDto | UserDto | 로그인 |
| 3 | POST | /main/record | MultipartFile file | List<LogDto> | 로그 기록 |
| 4 | GET | /main/search/date | Date start, Date end | List<LogDto> | 날짜별 조회 |
| 5 | GET | /main/search/plate | String plate | List<LogDto> | 차량번호별 조회 |
| 6 | GET | /main/history |  | List<HistoryDto> | 수정/삭제 기록 조회 |
| 7 | PUT | /main/update | List<LogDto> list | Boolean | 로그 수정(admin) |
| 8 | DELETE              | /main/delete | List<LogDto> list | Boolean | 로그 삭제(admin) |
### Flask
| ID | Method | URI | Params | Return | Description |
| --- | --- | --- | --- | --- | --- |
| 3 | POST | /main/record | MultipartFile file | LogDto | 로그 기록 |

## 8. DB 설계(ERD)
![image](https://file.notion.so/f/s/e271867a-0cd4-49ef-be39-63172df6294c/ERD.drawio.png?id=61525a4a-4485-4740-a298-4363ba287a90&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693324800000&signature=4J4ElumGHr7EwvYpICvitrmIB4XqsBi34XuyeayQ8a8&downloadName=ERD.drawio.png)

## 9. UML(Class Diagram)
![image](https://file.notion.so/f/s/43427bf7-09e1-4d3f-b619-cda48425081a/UML.drawio.png?id=e973859d-96bf-4923-940f-9ea25125f100&table=block&spaceId=305e395a-5955-44d6-bb5f-c488ffd0100f&expirationTimestamp=1693324800000&signature=jpO8mIdR9OoJ9W8IJIwM6Lumy7_ygjSoBLvHTa-t67g&downloadName=UML.drawio.png)
## 10. 개발 일지 
<a href="https://shrub-snap-550.notion.site/CRUD-566be659b7bf4693a6515f408cf2f1d9?pvs=4">개발 일지 보러 가기  <img width="23" src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Notion-logo.svg"> </a>****
