import allure
from selene import browser, by, be


def test_is_issue_in_repo_with_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')
        browser.driver.maximize_window()
    with allure.step('Ищем репозиторий'):
        browser.element('[data-target*=inputButtonText]').click()
        browser.element('#query-builder-test').send_keys('QA_GURU_Auto_Python').press_enter()
    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('MikhailIzegov/QA_GURU_Auto_Python')).click()

    with allure.step('Проверяем наличие секции "Issue"'):
        browser.element('#issues-tab').should(be.visible)
