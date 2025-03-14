import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Define Web Agent
web_agent = Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="qwen-2.5-32b"),
    tools=[DuckDuckGoTools()],
    instructions="Always include the sources",
    show_tool_calls=True,
    markdown=True,
)

# Define Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

# Create Agent Team
agent_team = Agent(
    team=[web_agent, finance_agent],
    model=Groq(id="qwen-2.5-32b"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Streamlit UI
st.title("Stock Analysis App")
st.write("Analyze companies and get long-term investment suggestions.")

# User input
stocks = st.text_input("Enter stock symbols (comma-separated, e.g., TSLA, NVDA, AAPL)", "TSLA, NVDA, AAPL")

if st.button("Analyze"):
    with st.spinner("Fetching data and analyzing..."):
        response = agent_team.get_response(f"Analyze companies like {stocks} and suggest which to buy for long term")
        st.markdown(response)
