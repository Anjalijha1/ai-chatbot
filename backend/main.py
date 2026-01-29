from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="YOUR_API_KEY_HERE")  # replace with your key

# For GET request
@app.get("/")  # <-- no colon here
def home():
    return {"message": "Backend working"}

# POST request for chat
class Chat(BaseModel):
    message: str

@app.post("/chat")
def chat(data: Chat):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": data.message}
        ]
    )
    return {"reply": response.choices[0].message.content}
