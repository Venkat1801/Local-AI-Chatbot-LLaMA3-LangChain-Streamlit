import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "TRUE"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

##prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful; assistant.Please respond to the question asked"), #assigning roles train how to behave 
        ("user","Question:{question}")
    ]
)


#stremlit framework
st.title("Langchain demo with LLAMA2")
input_text=st.text_input("what question you have in mind?")


#ollama Llama model
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({"question":input_text}))