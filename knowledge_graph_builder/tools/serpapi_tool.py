import os
from dotenv import load_dotenv
import requests

def search_google(query):
    """
    Search Google using SerpAPI and return the results.
    """
    load_dotenv()
    api_key = os.getenv("SERP_API_KEY")
    if not api_key:
        raise ValueError("Please set the SERP_API_KEY environment variable.")
    
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": api_key
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")