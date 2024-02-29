import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser, Config
import os


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    browser.config.driver_options = options
    browser.config.driver_remote_url = (
        f'https://user1:1234@selenoid.autotests.cloud/wd/hub'
    )

    yield browser

    browser.quit()
