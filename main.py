import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"  # chromium path
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def search_google(query, headless=False):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get("https://www.google.com")
        # accept cookies if needed (site dependent) - optional
        search = driver.find_element(By.NAME, "q")
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        time.sleep(2)  # wait for results
        results = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf > a")
        for r in results[:10]:
            href = r.get_attribute("href")
            title = r.text
            print(title)
            print(href)
            print()
    finally:
        driver.quit()

if __name__ == "__main__":
    search_google("python selenium tutorial", headless=False)
