from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_url(self, url: str, timeout: int | None = None):
        self.page.goto(url, timeout=timeout)
