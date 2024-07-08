from typing import Type

from playwright.sync_api import Playwright,sync_playwright

from infra.page_base import PageBase


class Browser:
    browser = None
    context = None
    page = None

    def __init__(self):
        with sync_playwright() as playwright:
            playwright = sync_playwright().start()
            self.browser = playwright.chromium.launch(headless=False)
            self.context = self.browser.new_context()
            self.context.tracing.start(screenshots=True, snapshots=True)
            self.page = self.context.new_page()
            yield
            # Close the context when the tests are done
            self.context.close()
            self.browser.close()

    def navigate(self, address, page_type: Type[PageBase]):
        self.page.goto(address, wait_until="load")
        return self.create_page(page_type)

    def create_page(self, page_type):
        return page_type(self.page)
