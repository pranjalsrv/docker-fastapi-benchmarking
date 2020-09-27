from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Message(BaseModel):
    message: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/post", status_code=200)
async def post(message: Message):
    return {"Message Recieved": message.message}
