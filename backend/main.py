# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Test endpoint
@app.get("/")
def home():
    return {"message": "Backend working"}

# Chat endpoint (dummy for now)
class Chat(BaseModel):
    message: str

@app.post("/chat")
def chat(data: Chat):
    user_msg = data.message
    reply = f"You said: {user_msg}"  # temporary dummy reply
    return {"reply": reply}
