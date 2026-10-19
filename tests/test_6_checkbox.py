import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_check_box(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    check_locator = async_page.locator("//div[@class='form-check form-check-inline']//input[@type='checkbox']/following-sibling::label")
    await expect(check_locator.first).not_to_be_checked()
    await check_locator.first.check()
    await expect(check_locator.first).to_be_checked()
    all_check_boxes = await check_locator.all_inner_texts()
    print(all_check_boxes)



@pytest.mark.asyncio
async def test_check_box_input_list(async_page):
    text_check_box = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    for i in text_check_box:
        check_locator = async_page.locator(f"//input[@id='{i.lower()}']")
        await expect(check_locator).not_to_be_checked()
        await check_locator.check()
        await expect(check_locator).to_be_checked()