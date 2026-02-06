from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer, util

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

class Message(BaseModel):
    text: str

knowledge = {
    "hours": "We're open Monday–Friday, 9am–5pm.",
    "location": "We're located in North Carolina.",
    "services": "We offer automation, chatbots, and workflow optimization."
}

keys = list(knowledge.keys())
key_embeddings = model.encode(keys, convert_to_tensor=True)

@app.post("/chat")
def chat(message: Message):
    user_embedding = model.encode(message.text, convert_to_tensor=True)
    scores = util.cos_sim(user_embedding, key_embeddings)[0]
    best_idx = int(scores.argmax())

    if float(scores[best_idx]) > 0.4:
        return {"response": knowledge[keys[best_idx]]}

    return {"response": "I'm not sure yet, but I'm learning more every day."}
