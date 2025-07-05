# English to PostgreSQL using LCEL + Groq in Streamlit with environment loading

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# Load environment variables (ensure .env file has GROQ_API_KEY)
load_dotenv()

st.title("🦙 English ➔ PostgreSQL Generator (LCEL + Environment)")

llm = ChatGroq(model="llama3-70b-8192")

prompt = ChatPromptTemplate.from_template(
    """
You are a PostgreSQL expert. Convert the following English instruction to an accurate PostgreSQL SQL query:
Instruction: {instruction}
SQL:
"""
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

instruction = st.text_area("Enter your instruction in English:")
if st.button("Generate SQL"):
    with st.spinner("Generating SQL..."):
        sql_query = chain.invoke({"instruction": instruction})
    st.code(sql_query, language="sql")

st.caption("Powered by Shafin")
