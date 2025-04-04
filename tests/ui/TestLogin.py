from constants.MainPageTextConstants import MainPageTextConstants
from pages.LoginPage import LoginPage


class TestExample:

    def test_example(self, login_page: LoginPage):
        login_page.goto("https://www.saucedemo.com/")
        login_page.title_present()
        login_page.verify_usernames(6)
        login_page.write_down_credentials("standard_user", "secret_sauce")
        login_page.click_on_login_button()
