import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser, Config
import os


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    options = webdriver.ChromeOptions()
    options.browser_version = '122.0'
    options.set_capability(
        'selenoid:options', {
            'enableVNC': True,
            'enableVideo': True,
            'enableLog': True
        }
    )

    browser.config.driver_options = options
    browser.config.driver_remote_url = (
        f'https://user1:1234@selenoid.autotests.cloud/wd/hub'
    )

    yield browser

    browser.quit()
