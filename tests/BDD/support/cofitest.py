import pytest

from playwright.async_api import async_playwright
from applications.pages.login_pages import LoginPage

@pytest.fixture(scope="session")
async def playwright_instance():
    """Starts the Playwright instance for the test session."""
    async with async_playwright() as p:
        yield p

@pytest.fixture(scope="function")
async def browser(playwright_instance):
    """Launches the browser instance for each test."""
    browser = await playwright_instance.chromium.launch(headless=False)
    yield browser
    await browser.close()

@pytest.fixture(scope="function")
async def page(browser):
    """Creates a fresh browser page for each test."""
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()

@pytest.fixture(scope="function")
async def login_page(page):
    """Returns an instance of the LoginPage."""
    return LoginPage(page)