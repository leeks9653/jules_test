from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login")
async def login(login_request: LoginRequest):
    # Hardcoded credentials
    hardcoded_username = "testuser"
    hardcoded_password = "testpassword"

    if login_request.username == hardcoded_username and login_request.password == hardcoded_password:
        return {"message": "Login successful", "token": "fake-jwt-token"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
