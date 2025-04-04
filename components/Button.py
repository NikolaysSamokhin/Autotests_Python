import allure

from components.Component import Component


class Button(Component):
    @property
    def type_of(self):
        return 'button'

    def hover(self, **kwargs):
        with allure.step(f'Hover on {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(kwargs)
            locator.hover()

    def double_click(self, timeout=15, **kwargs):
        with allure.step(f'Double click on {self.type_of} with name "{self.name}"'):
            locator = self.get_locator(kwargs)
            locator.dblclick(timeout=timeout)
