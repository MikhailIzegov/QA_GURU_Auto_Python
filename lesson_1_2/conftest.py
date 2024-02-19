from selene import browser
import pytest


@pytest.fixture(scope="session", autouse=False)
def config_browser():
    browser.config.window_width = 0
    browser.config.window_height = 0
    print("!!! Hello")


@pytest.fixture(scope="function", autouse=True)
def open_browser(config_browser):
    browser.open('https://www.google.com/')
    yield browser

    browser.quit()