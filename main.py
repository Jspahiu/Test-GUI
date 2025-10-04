import requests
from bs4 import BeautifulSoup

def bing_search(query):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.bing.com/search?q={query.replace(' ', '+')}"
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    results = []
    for h2 in soup.find_all("h2"):
        a = h2.find("a")
        if a and a.get("href"):
            results.append((a.get_text(), a["href"]))
    for i, (title, link) in enumerate(results[:10], 1):
        print(f"{i}. {title}\n{link}\n")

if __name__ == "__main__":
    bing_search("python selenium tutorial")
