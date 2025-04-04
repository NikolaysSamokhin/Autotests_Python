import pytest
from playwright.sync_api import sync_playwright
from pages.LoginPage import LoginPage

@pytest.fixture(scope='function')
def chromium_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def login_page(chromium_page):
    return LoginPage(chromium_page)