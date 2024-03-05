import pytest
from selene import browser, be, command

# Определение значений ширины и высоты для различных устройств
window_sizes = [
    (1920, 1080),  # Десктоп
    (375, 812),     # Мобильный
]


@pytest.fixture(params=window_sizes)
def adjust_size(request):
    width, height = request.param
    browser.config.base_url = 'https://github.com/'
    browser.driver.set_window_size(width, height)

    yield

    browser.quit()


def test_github_desktop(adjust_size):
    width, height = browser.driver.get_window_size()['width'], browser.driver.get_window_size()['height']

    # Проверка на соотношение сторон
    if height > width:
        pytest.skip("Мобильное соотношение сторон")

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)


def test_github_mobile(adjust_size):
    width, height = browser.driver.get_window_size()['width'], browser.driver.get_window_size()['height']

    # Проверка на соотношение сторон
    if width > height:
        pytest.skip("Десктопное соотношение сторон")

    browser.open('/')
    browser.element('[aria-label="Toggle navigation"][type="button"').perform(command.js.click)
    browser.element('.header-menu-wrapper').should(be.visible)
