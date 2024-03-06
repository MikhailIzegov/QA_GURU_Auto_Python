import pytest
from selene import browser, be, command


@pytest.fixture(params=[[1920, 1080], [390, 844], [380, 850]])
def adjust_size(request):
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

    yield

    browser.quit()


def test_github_desktop(adjust_size):
    if browser.config.window_width < 1012:
        pytest.skip(reason='Not desktop resolution')

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)


def test_github_mobile(adjust_size):
    if browser.config.window_width > 1011:
        pytest.skip(reason='Not mobile resolution')

    browser.open('/')
    browser.element('[aria-label="Toggle navigation"][type="button"').perform(command.js.click)
    browser.element('.header-menu-wrapper').should(be.visible)
