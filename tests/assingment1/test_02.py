#Browser, Context and Page Fixtures

from playwright.sync_api import expect

def test_home_page(page):
    page.goto("https://www.saucedemo.com/")
    expect(page.get_by_text("Swag Labs")).to_be_visible()


def test_save_data(cus_page):
    cus_page.goto("https://www.saucedemo.com/")
    cus_page.evaluate("localStorage.setItem('data', 'sudev')")
    assert cus_page.evaluate("localStorage.getItem('data')") == "sudev"


def test_check_data(cus_page):
    cus_page.goto("https://www.saucedemo.com/")
    assert cus_page.evaluate("localStorage.getItem('data')") is None