from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_google(query):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")        # run headless
    options.add_argument("--no-sandbox")          # container safe
    options.add_argument("--disable-dev-shm-usage") # avoid /dev/shm issues
    options.add_argument("--disable-gpu")         # disable GPU
    options.add_argument("--remote-debugging-port=9222") # fixes DevToolsActivePort
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-software-rasterizer")

    # Use Chromium in Codespaces
    options.binary_location = "/usr/bin/chromium-browser"

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://www.google.com")
        print("Page title:", driver.title)

        search = driver.find_element(By.NAME, "q")
        search.send_keys(query)
        search.send_keys(Keys.RETURN)

        time.sleep(2)

        results = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf > a")
        for r in results[:10]:
            print(r.text)
            print(r.get_attribute("href"))
            print()

    finally:
        driver.quit()

if __name__ == "__main__":
    search_google("python selenium tutorial")
