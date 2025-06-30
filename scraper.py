import requests
from bs4 import BeautifulSoup

def scrape_image(keyword):
    query = keyword.replace(' ', '+')
    url = f"https://duckduckgo.com/?q={query}&iax=images&ia=images"
    headers = {'User-Agent': 'Mozilla/5.0'}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    imgs = soup.find_all("img")
    for img in imgs:
        src = img.get("src") or img.get("data-src")
        if src and "http" in src:
            return src
    return None
