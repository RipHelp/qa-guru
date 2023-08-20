import time

import pytest
from selenium import webdriver
from selene import browser
from conftest import TMP_DIR
from os import path
import glob
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

@pytest.fixture()
def prepare(test_prepare):
    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options


def test_download_file_with_browser(prepare):
    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)
    assert path.exists(path.join(TMP_DIR, 'pytest-main.zip'))
