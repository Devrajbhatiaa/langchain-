import os 
from  dotenv import  load_dotenv

from langchain_ollama import OllamaLLM

import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


prompt = ChatPromptTemplate.from_messages(
  [
    ("system","you are a helpful assistant "),
    ("user", "Question:{question}")

  ]
)


st.title("langchain demo with ollama ")
input_text =st.text_input("what question")


#ollama 
llm= OllamaLLM(model="gemma:2b")
output_parser=StrOutputParser()
chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))