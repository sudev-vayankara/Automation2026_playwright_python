import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Register").click()
    page.get_by_role("link", name="Jewelry").nth(1).click()
    page.get_by_role("link", name="Books").nth(1).click()
    page.get_by_role("button", name="Add to cart").first.click()
    page.get_by_role("button", name="Add to cart").nth(1).click()
    page.get_by_role("button", name="Add to cart").first.click()
    page.get_by_role("heading", name="My account").click()
    page.get_by_role("heading", name="My account").click()
