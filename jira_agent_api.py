from fastapi import FastAPI
from pydantic import BaseModel
from jira_agent import run_agent

app = FastAPI()

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(req: ChatRequest):

    response = await run_agent(req.message)

    return {"response": response}