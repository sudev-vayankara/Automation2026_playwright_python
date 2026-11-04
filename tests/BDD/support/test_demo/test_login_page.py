import pytest


@pytest.mark.asyncio
async def test_login(login_page):

    # Navigate to application
    await login_page.navigate_to_login_page()

    # Enter username
    await login_page.enter_username("abc@gmail.com")

    # Enter password
    await login_page.enter_password("abc@123")

    # Click login
    await login_page.click_login()

    # Validate error message
    assert await login_page.error_msg.is_visible()