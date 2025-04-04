import allure
from playwright.async_api import expect

from components.Component import Component


class Input(Component):

    @property
    def type_of(self):
        return "input"

    def fill(self, value: str, isValidate: bool, **kwrgs):
        with allure.step(f'Fill {self.type_of} {self.name}'):
            locator = self.get_locator(**kwrgs)
            locator.fill(value)
            if isValidate:
                self.should_have_value()

    def should_have_value(self, value: str, timeout, **kwargs):
        with allure.step(f'Text shoud equal to {value}'):
            locator = self.get_locator(**kwargs)
            expect(locator).to_have_value()
