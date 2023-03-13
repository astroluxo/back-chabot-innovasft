from langchain import OpenAI
import os
from fastapi import FastAPI
from pruebas import ask_ai 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app= FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
    promt: str
    token: str


@app.post("/promts")
async def root(data:Data):
    return ask_ai(data.promt,data.token)
