
from playwright.sync_api import sync_playwright, expect



def test_async_exp1():
 with sync_playwright() as p: 
    browser = p.chromium.launch(headless=False)
    user_context = browser.new_context()
    page = user_context.new_page()
    page.goto("https://www.google.com/")
    print(page.title()) # give me title of the page
    expect(page).to_have_title("Google")

    page.go_back()
    page.go_forward()
    page.reload()


