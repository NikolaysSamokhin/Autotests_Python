from playwright.sync_api import Page

from components.Title import Title
from pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title = Title(page, name="Title", locator=".app_logo")

    def title_present(self):
        print(self.title.type_of)
        print(self.title.get_text())

    def click_on_login_button(self):
        self.login_button.click()

    def write_down_credentials(self, username, password):
        self.write_username(username)
        self.write_password(password)

    def write_username(self, username):
        self.input_username.fill(value=username, isValidate=False)

    def write_password(self, password):
        self.input_password.fill(value=password, isValidate=False)

    def verify_usernames(self, amountExpected):
        actualCount = self.usernames.get_count()
        assert actualCount == amountExpected, f"Actual result:{actualCount}\n Expected result:{amountExpected}"
