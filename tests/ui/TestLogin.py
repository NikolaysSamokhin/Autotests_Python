from pages.LoginPage import LoginPage


class TestExample:

    def test_example(self, login_page: LoginPage):
        login_page.goto("https://www.saucedemo.com/")
        login_page.title_present()

