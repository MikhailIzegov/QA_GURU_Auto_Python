"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, be, command


@pytest.fixture
def config_desktop():
    browser.config.base_url = 'https://github.com/'
    browser.driver.maximize_window()
    yield
    browser.quit()


@pytest.fixture
def config_mob():
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = 800
    browser.config.window_height = 600
    yield
    browser.quit()


def test_github_desktop(config_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)


def test_github_mobile(config_mob):
    browser.open('/')
    browser.element('[aria-label="Toggle navigation"][type="button"').perform(command.js.click)
    browser.element('.header-menu-wrapper').should(be.visible)
