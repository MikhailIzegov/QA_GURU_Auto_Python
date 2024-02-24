from selene import browser, by, be


def test_is_issue_in_repo():
    browser.open('https://github.com')
    browser.driver.maximize_window()
    browser.element('[data-target*=inputButtonText]').click()
    browser.element('#query-builder-test').send_keys('QA_GURU_Auto_Python').press_enter()
    browser.element(by.link_text('MikhailIzegov/QA_GURU_Auto_Python')).click()
    browser.element('#issues-tab').should(be.visible)
