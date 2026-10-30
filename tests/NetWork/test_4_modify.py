import pytest
from _testcapi import awaitType
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_modify_req():
    async with async_playwright() as p:
       browser = await p.chromium.launch(headless=False)
       page = await browser.new_page()

       async def modify_request(route):
           req = route.request
           header = await req.all_headers()
           header["x-test-client"] = "Playwright-Async"

           if req.method == "POST" and req.post_data:
               try:
                   payload = json.loads(req.post_data)
                   if isinstance(payload,dict) :
                       print("original data :" , payload)

                       if "quantity" in payload:
                           payload["quantity"] = 5

                           updated_pl = json.dumps(payload)
                           await route.continue_(
                               headers=header,
                               post_data = updated_pl
                           )
                           return
               except json.JSONDecodeError:
                   print("req body not json")
           await route.continue_(headers=header)


       await page.route("**/*",modify_request)

       await page.goto("https://parabank.parasoft.com/parabank/index.htm")
       await page.wait_for_timeout(5000)
       print(await page.title())