import pytest
from _testcapi import awaitType
from playwright.async_api import async_playwright

# Abort specific network calls
# Objective: Block images, fonts, or identified analytics requests while allowing other requests to continue.

@pytest.mark.asyncio
async def test_block_img():
    async with async_playwright() as p:
       browser = await p.chromium.launch(headless=False)
       page = await browser.new_page()
       async def hand_function(route):
            req = route.requset
            url = req.url.lower() # resources :--> type
            res_type = req.resource_type
            if res_type in ["image","font"]:
                print("blocked resources :" , url)
                await route.abort()
            elif "analytics" in url:
               print("blocked analystics :" , url)
               await route.abort()
            else:
                await route.continue_()

       await page.route("**/*",hand_function)
       
       await page.goto("https://demowebshop.tricentis.com/")
       await page.wait_for_timeout(5000)
       print(await page.title())