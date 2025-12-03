from playwright.sync_api import Page

from components.Title import Title
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title = Title(page, name="Title", locator=".login_logo")

    def title_present(self):
        print(self.title.type_of)
        print(self.title.get_text())
