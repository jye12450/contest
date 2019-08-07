import requests
from urllib.parse import quote

def crwal(url):
    result = requests.get(url)
    return result.content
