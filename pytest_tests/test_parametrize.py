"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be, command


@pytest.fixture(params=['desktop', 'mobile'])
def adjust_size(request):
    browser.config.base_url = 'https://github.com/'
    if request.param == 'desktop':
        browser.driver.maximize_window()
    elif request.param == 'mobile':
        browser.config.window_width = 800
        browser.config.window_height = 600

    yield
    browser.quit()


@pytest.mark.parametrize('adjust_size', ['desktop'], indirect=True)
def test_github_desktop(adjust_size):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)


@pytest.mark.parametrize('adjust_size', ['mobile'], indirect=True)
def test_github_mobile(adjust_size):
    browser.open('/')
    browser.element('[aria-label="Toggle navigation"][type="button"').perform(command.js.click)
    browser.element('.header-menu-wrapper').should(be.visible)