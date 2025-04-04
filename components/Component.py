from abc import abstractmethod

import allure
from playwright.async_api import Locator, expect


class Component:
    def __init__(self, page, name, locator) -> None:
        self.page = page
        self.name = name
        self.locator = locator

    @property
    @abstractmethod
    def type_of(self):
        return "component"

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.locator(locator)

    def get_all_locator(self, **kwargs) -> Locator:
        elements = self.get_locator(**kwargs)
        return elements.all()

    def click(self, **kwargs) -> None:
        with allure.step(f'Click on {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.click()

    def should_be_visible(self, timeout=15, **kwargs):
        with allure.step(f'{self.name}  {self.type_of} should be visible'):
            locator = self.get_locator(self, **kwargs)
            expect(locator).to_be_visible(timeout=timeout)

    def should_be_invisible(self, timeout, **kwargs):
        with allure.step(f'{self.name}  {self.type_of} should be invisible'):
            locator = self.get_locator(kwargs)
            expect(locator).not_to_be_visible()

    def should_be_clickable(self, timeout=15, **kwargs):
        with allure.step(f'{self.name}  {self.type_of} should be clickable'):
            locator = self.get_locator(self, kwargs)
            expect(locator).to_be_enabled()

    def get_text(self, timeout = 35, **kwargs) -> str:
        locator = self.get_locator(**kwargs)
        return locator.text_content(timeout=timeout)
