import pytest
from log_config import logger
@pytest.mark.asyncio
async def test_main():
    logger.info("========== TEST EXECUTION STARTED ==========")

    try:
        async with async_playwright() as p:

            browser = await p.chromium.launch(headless=False)

            page = await browser.new_page()

            # 1. Capture browser console messages
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
                lambda error: logger.error(
                    "JAVASCRIPT ERROR: %s", error
                )
            )

            # 3. Capture failed network requests
            page.on(
                "requestfailed",
                lambda request: logger.error(
                    "REQUEST FAILED: %s | Error: %s",
                    request.url,
                    request.failure
                )
            )

            # 4. Capture HTTP error responses
            page.on(
                "response",
                lambda response: logger.warning(
                    "HTTP ERROR: %s | Status: %s",
                    response.url,
                    response.status
                ) if response.status >= 400 else None
            )

            logger.info("Launching browser: Chromium")

            # Navigate to application
            logger.info("Opening Demo Web Shop")
            await page.goto(
                "https://demowebshop.tricentis.com/",
                wait_until="domcontentloaded"
            )

            logger.info("Page title: %s", await page.title())

            # Search for a book
            search_box = page.get_by_role(
                "textbox", name="Search store"
            )

            await search_box.fill("book")
            await page.get_by_role(
                "button", name="Search"
            ).click()

            logger.info("Search executed successfully")

            # Wait for search results to appear
            await page.locator(
                ".product-item"
            ).first.wait_for(state="visible")

            logger.info("Search results are visible")

            logger.info("TEST RESULT: PASSED")

            await browser.close()
            logger.info("Browser closed successfully")

    except Exception:
        logger.exception("TEST RESULT: FAILED")

    finally:
        logger.info("========== TEST EXECUTION FINISHED ==========")