import pytest
from playwright.async_api import async_playwright
@pytest.mark.asyncio
async def test_use_session():
    async  with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(storage_state=".auth/loginsession.json")
        page = await context.new_page()
        await page.goto("https://demowebshop.tricentis.com/")
        await page.wait_for_timeout(5000)


        