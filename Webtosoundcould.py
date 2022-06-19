import requests
from bs4 import BeautifulSoup4

def load_page(url):
    result = request.get(url)
    doc= BeautifulSoup4(result.text, "html.parser")
    return doc