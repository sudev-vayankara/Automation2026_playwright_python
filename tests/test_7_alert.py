import pytest
from playwright.async_api import expect


#simple alret

async def handle_aletrs(dialog):
    print("alert type = " , dialog.type)
    print("alter msg" , dialog.message)
    await dialog.accept()


@pytest.mark.asyncio
async def test_check_box_input_list(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    async_page.on("dialog", handle_aletrs)
    await async_page.get_by_text("Simple Alert").click()

    ele = async_page.locator("#sunday")
    await  expect(ele).not_to_be_checked()
    await ele.click()
    await  expect(ele).to_be_checked()



#confirmation alert






#prompt alert



