from tests.pages.registration_page import RegistrationPage
from tests.users_for_tests import users


def test_fill_in_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.register(users.test_user)
    registration_page.should_have_user(users.test_user)
