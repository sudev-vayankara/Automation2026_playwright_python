import re
from playwright.sync_api import Playwright, sync_playwright, expect

#RUNNING CODE - python -m playwright codegen https://demowebshop.tricentis.com/
# Automatic create py file python -m playwright codegen -o tests/demo_code_.spec.ts  https://demowebshop.tricentis.com/
#or
#python -m playwright codegen --target python-pytest -o test_generated.py https://demowebshop.tricentis.com/


#playwright codegen --viewport-size="800,600" playwright.dev

#https://playwright.dev/python/docs/codegen

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Register").click()
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("textbox", name="Email:").click()
    page.get_by_role("textbox", name="Email:").fill("sudev.v")
    page.get_by_role("textbox", name="Email:").press("Shift+CapsLock")
    page.get_by_role("textbox", name="Email:").fill("sudev.v@BENSYINFOTECH.COM")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("TEST1234*-")
    page.get_by_role("button", name="Log in").click()
    expect(page.locator("body")).to_contain_text("Login was unsuccessful. Please correct the errors and try again. No customer account found")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


