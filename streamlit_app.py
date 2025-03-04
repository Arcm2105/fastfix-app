import streamlit as st
import pandas as pd
from langchain_groq import ChatGroq
from langchain_experimental.agents.agent_toolkits import create_csv_agent

st.title("Customer Support Ticket Analysis")

csv_file_path = 'customer_support_tickets_updated.csv'
df_csv = pd.read_csv(csv_file_path)

st.write("Preview of Data:", df_csv.head())

groq_api_key = "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"  
llm = ChatGroq(temperature=0, model="llama3-70b-8192", api_key=groq_api_key)
agent = create_csv_agent(llm, csv_file_path, verbose=True, allow_dangerous_code=True)

user_query = st.text_input("Ask a question about the data:")

def query_data(query):
    response = agent.invoke(query)
    return response

if st.button("Get Answer"):
    if user_query:
        response = query_data(user_query)
        st.write("Answer:", response)
    else:
        st.warning("Please enter a question.")

