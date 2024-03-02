import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '100.0',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f'https://user1:1234@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    browser.config.driver = driver

    yield

    html = browser.driver.page_source
    allure.attach(body=html, name='page_source', attachment_type=allure.attachment_type.HTML, extension='.html')

    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=allure.attachment_type.PNG, extension='.png')

    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', allure.attachment_type.TEXT, '.log')

    browser.quit()