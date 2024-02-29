from selene.support.shared import browser

from tests.pages.application import app
from tests.users_for_tests import users


def test_fill_in_form():
    app.registration_page.open_page()

    app.registration_page.register(users.test_user)
    app.registration_page.should_have_user(users.test_user)

    app.registration_page.add_html(browser)
