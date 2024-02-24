import allure
from selene import browser, by, be


def test_selene_with_allure_decorator_steps():
    open_main_page()
    find_repo()
    go_to_repo()
    is_issue_tab_present()


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')
    browser.driver.maximize_window()


@allure.step('Ищем репозиторий')
def find_repo():
    browser.element('[data-target*=inputButtonText]').click()
    browser.element('#query-builder-test').send_keys('QA_GURU_Auto_Python').press_enter()


@allure.step('Переходим по ссылке репозитория')
def go_to_repo():
    browser.element(by.link_text('MikhailIzegov/QA_GURU_Auto_Python')).click()


@allure.step('Проверяем наличие секции "Issue"')
def is_issue_tab_present():
    browser.element('#issues-tab').should(be.visible)
