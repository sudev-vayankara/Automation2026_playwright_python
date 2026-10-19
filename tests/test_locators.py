
import pytest
from utils.config import BASE_URL, USERNAME, PASSWORD

import playwright.async_api as playwright


@pytest.mark.asyncio
async def test_evn_(async_page):
    await async_page.goto(BASE_URL)
    print(await async_page.title())


    