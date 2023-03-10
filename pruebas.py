import openai

openai.api_key = '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'
from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import os

  
def ask_ai(question):
 # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 300
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600 

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
 
    documents = SimpleDirectoryReader('data').load_data()
    
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )


    while True: 
        query = question
        response = index.query(query, response_mode="compact")
        return response.response
  
os.environ["OPENAI_API_KEY"] = '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'








