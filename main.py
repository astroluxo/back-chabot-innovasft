from fastapi import FastAPI
from pruebas import ask_ai 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pruebas import construct_index
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
        
class Load(BaseModel):
    direct: str
    token: str

@app.post("/promts")
def root(data:Data):
    return ask_ai(data.promt,data.token)


@app.post("/carga")
def load(load:Load):
    return construct_index(load.direct,load.token)
