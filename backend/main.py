from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key="YOUR_API_KEY_HERE")  # Put your OpenAI key

class Chat(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Backend working"}

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
