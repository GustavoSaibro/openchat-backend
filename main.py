from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from chat import completion_prompt,completion_prompt2

class Prompt(BaseModel):
    prompt: str

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message":"Hello World!!"}

@app.post("/complete")
async def completion(prompt: Prompt) -> dict:
    # completion = await completion_prompt2(prompt.prompt)
    completion = await completion_prompt(prompt.prompt)
    print()
    return {"message": completion}

@app.post("/complete2")
async def completion(prompt: Prompt):
    # completion = await completion_prompt(prompt)
    return {"message": "test"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)