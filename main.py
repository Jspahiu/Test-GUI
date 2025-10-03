import requests
from bs4 import BeautifulSoup

def google_search(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for a in soup.find_all("a"):
        href = a.get("href")
        if href and href.startswith("https://") and "google.com" not in href:
            title = a.get_text()
            if title.strip():  # ignore empty titles
                results.append((title, href))

    # print top 10 results
    for i, (title, link) in enumerate(results[:10], 1):
        print(f"{i}. {title}\n{link}\n")

if __name__ == "__main__":
    google_search("python selenium tutorial")
