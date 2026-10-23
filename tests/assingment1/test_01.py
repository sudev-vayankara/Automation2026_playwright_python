#Playwright Installation & Project Setup

from playwright.sync_api import sync_playwright, expect

def test_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)           # Launch browser
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        print(page.title())
        expect(page).to_have_title("Swag Labs")
        browser.close()
