
from langchain_groq import ChatGroq
from sql_agent import sql_agent_from_query
import os

# Initialize LLM
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.0,
    max_tokens=256,
    groq_api_key=os.getenv("GROQ_API_KEY")
)


# Tool 1 — Order Query Tool
def order_query_tool(user_query):

    order_id, raw_data = sql_agent_from_query(user_query)

    return order_id, raw_data


# Tool 2 — Answer Generation Tool
def answer_tool(user_query, raw_data):

    prompt = f'''
    You are a polite and professional customer support assistant for FoodHub.

    User Query:
    {user_query}

    Order Details:
    {raw_data}

    Instructions:
    - Give short responses
    - Be professional
    - Be customer friendly
    - Do not hallucinate
    - Use only provided order details

    Generate final response.
    '''

    response = llm.invoke(prompt)

    return response.content
