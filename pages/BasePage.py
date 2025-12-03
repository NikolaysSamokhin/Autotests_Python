from __future__ import annotations

import allure
from playwright.sync_api import Response


class BasePage:
    def __init__(self, page) -> None:
        self.page = page

    def goto(self, url: str) -> Response | None:
        with allure.step(f'Opening the url "{url}"'):
            return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')
