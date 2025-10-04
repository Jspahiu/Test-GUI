from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False to see window in noVNC
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("textarea[name=q]", "python playwright tutorial")
    page.press("textarea[name=q]", "Enter")
    page.wait_for_timeout(5000)  # 5 sec so you can see results
    browser.close()
