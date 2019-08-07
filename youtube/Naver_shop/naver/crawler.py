import requests
import urllib.parse import quote

def crawl(keyword, start):
    encText = quote(keyword)
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText +
            "&display=100"+"&start="+str(start)
    data = requests.get(url)
    return data.content
