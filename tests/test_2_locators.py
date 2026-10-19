import pytest
from playwright.async_api import expect




@pytest.mark.asyncio
async def test_getBytitle(async_page):
   await async_page.goto("https://demowebshop.tricentis.com/")
   ele = async_page.locator("h2[class='topic-html-content-header']") # locator :notfinding
   await expect(ele).to_be_visible()
   print(ele.inner_html())




@pytest.mark.asyncio
async def test_getBytitle(async_page):
   await async_page.goto("https://demowebshop.tricentis.com/books")
   ele = async_page.locator(".product-title") # locator :notfinding
   # ele :-- all products
   all_product = await ele.all()
   for i in all_product:
       print(await i.inner_text())



@pytest.mark.asyncio
async def test_getBytitle(async_page):
   await async_page.goto("https://demowebshop.tricentis.com/")
   ele = async_page.locator("input[class='button-2 product-box-add-to-cart-button']") # locator :notfinding
   all_product = await ele.all()
   for i in all_product:
       await i.click()
       break
   await async_page.wait_for_timeout(5000)


   