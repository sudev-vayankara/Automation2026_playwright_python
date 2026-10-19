import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_drag_and_drop(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    s = async_page.locator("//div[@id = 'draggable']")
    d = async_page.locator("//div[@id = 'droppable']")
    await s.drag_to(d)


@pytest.mark.asyncio
async def test_scroll(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    s = async_page.locator("//div[@id = 'draggable']")
    await s.scroll_into_view_if_needed()
    d = async_page.locator("//div[@id = 'droppable']")
    await s.drag_to(d)
    await async_page.mouse.wheel(0,1000)
    await async_page.wait_for_timeout(500)
    await async_page.mouse.wheel(0,-1000)
    await async_page.wait_for_timeout(500)



@pytest.mark.asyncio
async def test_scroll_end(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    await async_page.evaluate("window.scrollTo(0,document.body.scrollHeight);")
    await async_page.wait_for_timeout(500)



    
@pytest.mark.asyncio
async def test_scroll_end(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    await async_page.evaluate("window.scrollTo(0,document.body.scrollHeight);")
    await async_page.wait_for_timeout(500)
    # setTimeout(() => { debugger; }, 5000);


@pytest.mark.asyncio
async def test_scroll_infinite(async_page):
    await async_page.goto("https://www.playwrightautomation.com/infinite-scroll.html")
    loading = async_page.locator("//div[@id='loading-indicator']")
    end_of_catalog = async_page.locator("//P[text()='End of Catalog']")
    scroll = async_page.locator("#scroll-sentinel")
    print(await end_of_catalog.inner_text())
    while True:
        await scroll.scroll_into_view_if_needed()
        print("one more scroll needed")
        await async_page.wait_for_timeout(500)
        if await end_of_catalog.is_visible():
                print("scroll till end")
                break