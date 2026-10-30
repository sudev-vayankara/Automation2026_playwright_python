import pytest
from _testcapi import awaitType
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_slow_request():
    async with async_playwright() as p:
       browser = await p.chromium.launch(headless=False)
       page = await browser.new_page()

       async def slow_api(route):
            print("Delaying :" , route.request.url)
            await asyncio.sleep(3)
            await route.continue_()

       await page.route("**/api/*",slow_api)

       await page.goto("https://www.amazon.in/")
       await page.wait_for_timeout(5000)
       print(await page.title())