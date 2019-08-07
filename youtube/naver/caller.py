import requests
from urllib.parse import quote

def crawl(url):
    result = requests.get(url)
    return result.content
