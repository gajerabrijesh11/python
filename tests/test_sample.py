from playwright.sync_api import sync_playwright

def test_example1():
   with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        print("page title:", page.title())

        browser.close()

        
def test_example2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://ciceroni.in/") 
        print("page tile", page.title() )

        browser.close()
