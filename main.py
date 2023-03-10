from langchain import OpenAI
import os
from fastapi import FastAPI
from pruebas import ask_ai 
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/query")
def root(query):
    return ask_ai('La siguiente es una conversación con un asistente de la mesa de ayuda a la aplicación de Class Limitless. El asistente es útil, creativo, inteligente y muy amigable.\n\n'+'USERROMEO: '+query+'\nAVAINNOVASOFT:')