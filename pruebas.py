import openai


from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import os



def construct_index(direct,token):
    os.environ["OPENAI_API_KEY"] = token
    # set maximum input size
    max_input_size = 5096
    # set number of output tokens
    num_outputs = 2600
    # set maximum chunk overlap
    max_chunk_overlap = 40
    # set chunk size limit
    chunk_size_limit = 1600 

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.1, model_name="gpt-3.5-turbo", max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
 
    documents = SimpleDirectoryReader(direct).load_data()
    
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper
    )

    index.save_to_disk('index.json')

    return index
  
def ask_ai(promt,token):
    os.environ["OPENAI_API_KEY"] = token
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    query='Responde en markdown. \n'+ promt
    response = index.query(query,response_mode="default",mode="embedding")
    return response.response
  
  

   








