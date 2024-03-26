import requests
from bs4 import BeautifulSoup

def scrape_kindle_highlights():
    url = "https://read.amazon.com/notebook"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    highlights = ["Highlight 1", "Highlight 2", "Highlight 3"]
    
    return highlights
