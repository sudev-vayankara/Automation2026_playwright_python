# import os
# import pytest_asyncio
# from playwright.async_api import async_playwright
# import config
# from dotenv import load_dotenv


import os
import asyncio
import pytest
import pytest_asyncio

from playwright.async_api import async_playwright
from dotenv import load_dotenv
from log_config import logger
from applications.pages.loginpage import LoginPage

import config

@pytest_asyncio.fixture
async def async_page(request):
    async with async_playwright() as p:

        # Get browser names supplied through --browser
        browser_names = request.config.getoption("--browser")

        # Use Chromium if no browser is supplied
        browser_name = browser_names[0] if browser_names else "chromium"

        # Select Chromium, Firefox, or WebKit
        browser_type = getattr(p, browser_name)

        # Launch the selected browser
        browser = await browser_type.launch(
            headless=config.HEADLESS
        )

        # Create a new context and page
        context = await browser.new_context()
        page = await context.new_page()

        # Apply configured timeouts
        page.set_default_timeout(config.DEFAULT_TIMEOUT)
        page.set_default_navigation_timeout(
            config.NAVIGATION_TIMEOUT
        )

        yield page

        # Clean up
        await context.close()
        await browser.close()

from log_config import logger

@pytest_asyncio.fixture
async def async_page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False) # chromebrowser
        context = await browser.new_context()#storage_state=".auth/loginsession.json")
        await context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )
        page = await context.new_page() # page
        page.on(
            "console",
            lambda msg: logger.error(
                "BROWSER CONSOLE [%s]: %s",
                msg.type.upper(),
                msg.text
            )
        )
        # 2. Capture JavaScript errors
        page.on(
            "pageerror",
            lambda error: logger.error("JAVASCRIPT ERROR: %s", error)
        )
        # 3. Capture failed network requests
        page.on(
            "requestfailed",
            lambda req: logger.error("REQUEST FAILED [%s]: %s", req.url, req.failure)
        )
        #
        # 4. Capture HTTP error responses (status >= 400)
        page.on(
            "response",
            lambda response: logger.warning(
                "HTTP ERROR: %s | Status: %s",
                response.url,
                response.status
            ) if response.status >= 400 else None
        )



        yield  page
        await context.tracing.stop(path="trace.zip")
        await browser.close()


load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

@pytest_asyncio.fixture
async def api_():
    assert TOKEN,"GITHUB_TOKEN not present in the environment variables"
    async with async_playwright() as p:
        api = await p.request.new_context(
            extra_http_headers= {
                "Authorization": f"Bearer {TOKEN}",
                "Accept": "application/vnd.github.v3+json"
            }
        )
        yield api

        await api.dispose()

@pytest.fixture(scope="function")
async def browser():
    " ""Launches the browser instance for each test."" "
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
        await browser.close()

@pytest.fixture(scope="function")
async def page(browser):
    " ""Creates a fresh browser page for each test."" "
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()


@pytest.fixture(scope="function")
async def page(browser):
    " ""Creates a fresh browser page for each test."" "
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()

@pytest.fixture(scope="function")
async def login_page(page):
    " ""Returns an instance of the LoginPage."" "
    return LoginPage(page)