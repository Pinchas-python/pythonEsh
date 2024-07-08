import pytest

from infra.browser import Browser
from logic.pages.youtube_page import YTPage
from infra.config.config_provider import configuration
from tests.test_base import TestBase

class TestClass(TestBase):

    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_open_youtube(self):
        browser = Browser()
        page: YTPage = browser.navigate(configuration['url'], YTPage)
        page.click_side_menu()
        print('past playwright')
        assert True is True


    @pytest.mark.smoke
    @pytest.mark.usefixtures("before_after_test")
    def test_10008_(self):
        browser = Browser()
        page: YTPage = browser.navigate(configuration['url'], YTPage)
        page.click_side_menu()
        print('past playwright')
        assert True is True

