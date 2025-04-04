from constants.MainPageTextConstants import MainPageTextConstants
from pages.HomePage import HomePage


class TestExample:

    def test_example(self, home_page: HomePage):
        home_page.goto("https://www.saucedemo.com/")
        home_page.title_present()
        localized_usernames = MainPageTextConstants.ACCEPTED_USERNAMES_VALUES
        print(localized_usernames)
        home_page.verify_usernames( MainPageTextConstants.ACCEPTED_USERNAMES_VALUES)
        home_page.write_down_credentials("standard_user", "secret_sauce")
        home_page.click_on_login_button()
