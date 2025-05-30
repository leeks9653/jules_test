# jules_test

This is a test repository for Jules.

## South Korean National Anthem Lyrics

동해 물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.

남산 위에 저 소나무, 철갑을 두른 듯
바람 서리 불변함은 우리 기상일세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.

가을 하늘 공활한데 높고 구름 없이
밝은 달은 우리 가슴 일편단심일세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.

이 기상과 이 맘으로 충성을 다하여
괴로우나 즐거우나 나라 사랑하세.
무궁화 삼천리 화려 강산
대한 사람, 대한으로 길이 보전하세.

## Running the FastAPI Application

To run the FastAPI application, follow these steps:

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the application:**
    ```bash
    uvicorn main:app --reload
    ```

    The application will be available at `http://127.0.0.1:8000`.

### Login Endpoint

The application includes a login endpoint at `/login`. It accepts POST requests with a JSON body containing `username` and `password`.

Example credentials:
-   Username: `testuser`
-   Password: `testpassword`
