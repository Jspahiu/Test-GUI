from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time

def search_google(query):
    # Configure Firefox options
    options = webdriver.FirefoxOptions()
    options.binary_location = "/opt/firefox/firefox"  # Path to the Firefox binary you extracted
    options.add_argument("--headless")                # Run without GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Start Firefox with GeckoDriver
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://www.google.com")
        print("Page title:", driver.title)

        # Find the search box
        search = driver.find_element(By.NAME, "q")
        search.send_keys(query)
        search.send_keys(Keys.RETURN)

        time.sleep(2)  # wait for results

        # Grab top 10 results
        results = driver.find_elements(By.CSS_SELECTOR, "div.yuRUbf > a")
        for r in results[:10]:
            title = r.text
            link = r.get_attribute("href")
            print(f"{title}\n{link}\n")

    finally:
        driver.quit()

if __name__ == "__main__":
    search_google("python selenium tutorial")
