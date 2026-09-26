from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from langserve import add_routes
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

model = OllamaLLM(model="gemma:2b")

system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

chain = prompt_template | model | StrOutputParser()

app = FastAPI(
    title="LangChain API",
    version="1.0",
    description="A simple LangChain API"
)

add_routes(app, chain)