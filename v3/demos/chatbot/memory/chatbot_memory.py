from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
memory = []  # simple in-memory conversation log

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    memory.append({"user": message.text})

    # simple context logic
    if "my name is" in message.text.lower():
        name = message.text.split("is")[-1].strip()
        memory.append({"bot": f"Nice to meet you, {name}!"})
        return {"response": f"Nice to meet you, {name}!"}

    if "who am i" in message.text.lower():
        for m in reversed(memory):
            if "my name is" in m.get("user", "").lower():
                name = m["user"].split("is")[-1].strip()
                return {"response": f"You told me your name is {name}."}
        return {"response": "You haven't told me your name yet."}

    # fallback
    response = "I hear you. Tell me more."
    memory.append({"bot": response})
    return {"response": response}
