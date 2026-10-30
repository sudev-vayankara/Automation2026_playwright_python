import pytest
#from _testcapi import awaitType
from playwright.async_api import async_playwright

# Abort specific network calls
# Objective: Block images, fonts, or identified analytics requests while allowing other requests to continue.

@pytest.mark.asyncio
async def test_req_res_logs():
    async with async_playwright() as p:
       browser = await p.chromium.launch(headless=False)
       page = await browser.new_page()

       async def log_request(request):
           #if "/api/" in request.url:
               print("\n--- API REQUEST ---")
               print("URL:", request.url)
               print("Method:", request.method)
               print("Headers:", await request.all_headers())
               print("Payload:", request.post_data)

       async def log_response(response):
           if "/api/" in response.url:
               print("\n--- API RESPONSE ---")
               print("URL:", response.url)
               print("Status:", response.status)

               content_type = response.headers.get(
                   "content-type", ""
               )

               if "application/json" in content_type:
                   try:
                       print("JSON:", await response.json())
                   except Exception as error:
                       print("Could not read JSON:", error)

       page.on("request",log_request)
       page.on("response",log_response)

       await page.goto("https://parabank.parasoft.com/parabank/index.htm")
       await page.wait_for_timeout(5000)
       print(await page.title())