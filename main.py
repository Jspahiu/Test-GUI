from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def search_google(query):
    chrome_options = Options()
    # Point Selenium to Chromium explicitly
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    # Codespaces / noVNC friendly flags
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")

    # Path to chromedriver
    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.google.com")

    # Try to accept cookies (if popup appears)
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(.,'Accept')]").click()
    except:
        pass

    # Perform search
    box = driver.find_element(By.NAME, "q")
    box.send_keys(query)
    box.submit()

    time.sleep(3)

    # Print first results
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    for i, r in enumerate(results[:10], 1):
        print(f"{i}. {r.text}")

    input("✅ Press ENTER to quit...")
    driver.quit()

if __name__ == "__main__":
    search_google("python selenium tutorial")
