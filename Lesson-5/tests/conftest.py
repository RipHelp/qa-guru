import pytest
from selene import browser


@pytest.fixture(scope="module")
def browser_management():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.type_by_js = True
    browser.config.timeout = 2.0

    yield

    browser.quit()