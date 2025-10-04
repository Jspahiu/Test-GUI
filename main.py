from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def search_google(query):
    chrome_options = Options()
    # Do NOT use headless since you're running noVNC
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")

    # Path to chromedriver (should already be in PATH if installed)
    service = Service("/usr/bin/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.google.com")

    # Accept cookies if popup shows up
    try:
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(.,'Accept')]").click()
    except:
        pass

    # Search
    box = driver.find_element(By.NAME, "q")
    box.send_keys(query)
    box.submit()

    time.sleep(3)

    # Grab results
    results = driver.find_elements(By.CSS_SELECTOR, "h3")
    for i, r in enumerate(results[:10], 1):
        print(f"{i}. {r.text}")

    # Keep browser open so you can see in noVNC
    input("Press ENTER to quit...")
    driver.quit()

if __name__ == "__main__":
    search_google("python selenium tutorial")
