from playwright.async_api import Page

from components.Button import Button
from components.Input import Input
from components.ItemList import ItemList
from components.Title import Title
from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title = Title(page, name="Title", locator=".login_logo")
        self.input_username = Input(page, locator="//*[@id='user-name']", name="User name input")
        self.input_password = Input(page, locator="//*[@id='password']", name="Password input")
        self.login_button = Button(page, "Login button", "//*[@id='login-button']")
        self.usernames = ItemList(page, "User names values", "//div[@data-test='login-credentials']//br")

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


    def verify_usernames(self, usernamesExpected):
        actualUsernames = self.usernames.get_text_from_elements()
        actualUsernames = self.usernames.get_text_from_elements()


        # assert actualUsernames == usernamesExpected, (f"Lists wer not equals: Actual result: {actualUsernames}\n "
        #                                               f"Expected result: {usernamesExpected} ")


