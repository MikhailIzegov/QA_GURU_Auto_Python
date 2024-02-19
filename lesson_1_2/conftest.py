from selene import browser
import pytest


@pytest.fixture(scope="session", autouse=False)
def config_browser():
    browser.config.window_width = 1024
    browser.config.window_height = 600


@pytest.fixture(scope="function", autouse=True)
def open_browser(config_browser):
    browser.open('https://www.google.com/')
    yield browser

    browser.quit()