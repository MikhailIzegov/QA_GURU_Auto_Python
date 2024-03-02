import allure

from tests.pages.application import app
from tests.users_for_tests import users


def test_fill_in_form():
    with allure.step('Open registration page'):
        app.registration_page.open_page()

    with allure.step('Register user'):
        app.registration_page.register(users.test_user)

    with allure.step('Check user data'):
        app.registration_page.should_have_user(users.test_user)

