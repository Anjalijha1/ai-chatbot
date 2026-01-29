from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

# Create FastAPI app
app = FastAPI()

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY_HERE")  # replace with your key

# GET request to test backend
@app.get("/")  # <-- NO colon here
def home():  # colon goes here only
    return {"message": "Backend working"}

# POST request for chat
class Chat(BaseModel):
    message: str

@app.post("/chat")  # <-- NO colon here
def chat(data: Chat):  # colon goes here only
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": data.message}
        ]
    )
    return {"reply": response.choices[0].message.content}
