import os
import requests
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI
from rich import print
load_dotenv()
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
tool = TavilySearch(max_results=5, apikey = "TAVILY_API_KEY")

def web_search(query: str) -> str:
    """
    Perform a web search using the Tavily API and return the results.

    Args:
        query (str): The search query.

    Returns:
        str: The search results.
    """
    try:
        results = tool.run(query)
        return print(results)
    except Exception as e:
        return f"An error occurred while performing the web search: {e}"