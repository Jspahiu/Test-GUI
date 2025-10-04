from playwright.sync_api import sync_playwright

def search_google(query):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,              # show window in noVNC
            args=[
                "--no-sandbox",          # important in Codespaces
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--start-maximized"
            ]
        )
        page = browser.new_page()
        page.goto("https://www.google.com")

        # Accept cookies if prompt appears
        try:
            page.click("text=Accept", timeout=2000)
        except:
            pass

        # Search
        page.fill("textarea[name=q]", query)
        page.press("textarea[name=q]", "Enter")

        # Wait a few seconds so you can see results
        page.wait_for_timeout(5000)
        print("✅ Search done. Check noVNC window!")

        # Keep browser open until you press ENTER
        input("Press ENTER to quit...")
        browser.close()

if __name__ == "__main__":
    search_google("python playwright tutorial")
