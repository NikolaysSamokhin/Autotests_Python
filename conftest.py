import pytest
from playwright.sync_api import sync_playwright
from pages.HomePage import HomePage

@pytest.fixture(scope='function')
def chromium_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def home_page(chromium_page):
    return HomePage(chromium_page)