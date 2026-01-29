from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# For testing simple GET request
@app.get("/")
def home():
    return {"message": "Backend working"}

# Example POST for chat
class Chat(BaseModel):
    message: str

@app.post("/chat")
def chat(data: Chat):
    user_msg = data.message
    return {"reply": f"You said: {user_msg}"}
