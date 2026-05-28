# 회의에서 살아남기

> 하고 싶은 말을 회의에서 말해도 되는 표현으로 바꿔드립니다.

---

## 서비스 소개

직장인이라면 누구나 회의 중 속으로만 하는 말이 있습니다.  
**"왜 제가 해야 하죠?"**, **"그건 불가능한데요"**, **"그거 이미 말씀드렸잖아요"**

**회의에서 살아남기**는 그 속마음을 입력하면, Gemini AI가 회의에서 실제로 쓸 수 있는 정중한 비즈니스 표현 3가지로 변환해줍니다.

---

## 주요 기능

**말투 4종 선택**
- 부드럽게 — 갈등 없이 배려 있게
- 단호하게 — 프로답고 논리적으로
- 상사 앞 버전 — 예의 바르고 능력 있어 보이도록
- 회의록에 남겨도 되는 버전 — 격식 있고 중립적으로

**변환 결과 3개 제공 + 복사 버튼**

**재미 지표 표시**
- 속마음 보존율
- 사회생활 안전도
- 회의 생존 가능성

---

## 스크린샷

<img width="933" height="832" alt="image" src="https://github.com/user-attachments/assets/1a44d0db-1784-4156-96cb-5fcd9c48035b" />
<img width="1418" height="410" alt="image" src="https://github.com/user-attachments/assets/3d402e68-a4af-4943-abdf-7e7739cbc6de" />
<img width="1376" height="1298" alt="image" src="https://github.com/user-attachments/assets/fe6a175a-7028-4dcf-af32-94af9f4cade1" />
<img width="1452" height="468" alt="image" src="https://github.com/user-attachments/assets/edb455b9-128e-43c0-b542-664868a78ebc" />





---

## 기술 스택

| 항목 | 내용 |
|------|------|
| Backend | Django 4.2 |
| AI | Google Gemini 2.5 Flash |
| 배포 | Render |

---

## 로컬 실행 방법

### 1. 패키지 설치
```bash
pip install -r requirements.txt
```

### 2. 환경변수 설정
프로젝트 루트에 `.env` 파일 생성:
```
GEMINI_API_KEY=발급받은_Gemini_API_키
SECRET_KEY=랜덤_문자열
DEBUG=True
```

### 3. 데이터베이스 초기화
```bash
python manage.py migrate
```

### 4. 서버 실행
```bash
python manage.py runserver
```

브라우저에서 http://127.0.0.1:8000 접속

---

## 배포 (Render)

1. Render에서 New Web Service 생성
2. 이 저장소 연결
3. 아래 설정 입력:

| 항목 | 값 |
|------|----|
| Build Command | `./build.sh` |
| Start Command | `gunicorn survive_meeting.wsgi` |

4. Environment Variables 추가:

| KEY | VALUE |
|-----|-------|
| `GEMINI_API_KEY` | Gemini API 키 |
| `SECRET_KEY` | 랜덤 문자열 |
| `DEBUG` | `False` |
