from playwright.async_api import async_playwright
import pytest


async def test_diff_browser():

    #chrome
    async with async_playwright as p:
      chrome_browser =await  p.chromium.launch(headless=True)

      user_context = await chrome_browser.new_context()

      page = chrome_browser.new_page()
      await page.goto("https://www.google.com/")

      admin_context = await chrome_browser.new_context()

      page = chrome_browser.new_page()
      await page.goto("https://www.amazon.in/")




    