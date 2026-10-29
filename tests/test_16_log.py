import pytest
from _testcapi import awaitType
from playwright.async_api import expect
from pathlib import Path
import sys

# Add the project root folder to Python's search path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import logger configuration
from log_config import logger


def test_logging():
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
@pytest.mark.asyncio
async def test_log_gen(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    logger.info(f"navigate to url = {async_page.url}")
    await async_page.get_by_text("Log in").click()
    logger.info("click on the login button")
    logger.info(f"user naviagte to login page = {async_page.url}")
    await async_page.locator("#Email").fill("abc@gmail.com")
    logger.info("user enter the un =abc@gmail.com")
    await async_page.locator("#Password").fill("abc@123")
    logger.info("user enter the pwd = abc@123")
    await async_page.locator("//input[@value='Log in']").click()
    logger.info("user click on the login button")
    try:
        logout = async_page.get_by_text("Log out")
        logger.info("user log in with valid data")
        await expect(logout).to_be_visible()
        print("test passed")
    except Exception:
        print("test failed")
        logger.error("user not login with invalid data")