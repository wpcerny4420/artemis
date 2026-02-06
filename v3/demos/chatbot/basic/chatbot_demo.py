# chatbot_demo.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    user_input = message.text.lower()

    # Simple rule-based responses (easy to expand)
    if "hours" in user_input:
        return {"response": "We're open Monday–Friday, 9am–5pm."}
    if "hello" in user_input or "hi" in user_input:
        return {"response": "Hello! How can I help you today?"}
    if "location" in user_input:
        return {"response": "We're located in North Carolina."}

    # Default fallback
    return {"response": "I'm not sure about that yet, but I can learn!"}
