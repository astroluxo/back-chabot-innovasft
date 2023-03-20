import openai


from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import os

  
def ask_ai(promt,token):

    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    query='Responde en markdown. /markdown \n'+ promt
    response = index.query(query,response_mode="default",mode="embedding")
    return response.response
  
   








