from selene import browser, by
from pathlib import Path
from selene.support.shared import browser
from selene import have
from selene import command
import os
import tests
from tests.users_for_tests import users


class RegistrationPage:

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)

    def fill_last_name(self, value):
        browser.element("#lastName").type(value)

    def fill_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value(gender)).element('..').click()

    def fill_phone_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_hobby(self, hobby):
        browser.all('[for^=hobbies').element_by(have.exact_text(hobby)).perform(command.js.scroll_into_view)
        browser.all('[for^=hobbies').element_by(have.exact_text(hobby)).click()

    def fill_current_address(self, address):
        browser.element('#currentAddress').type(address)

    def select_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def select_city(self, city):
        browser.element('#city').click()
        browser.all('[id^=react-select]').element_by(
            have.exact_text(city)
        ).click()

    def select_date_of_birth(self, month, year, day: int):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def upload_picture(self, path_to_picture):
        browser.element('#uploadPicture').set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), path_to_picture)
            )
        )

    def submit_data(self):
        browser.element('#submit').press_enter()

    @property
    def registered_user_data(self):
        return browser.element('.table').all('td').with_(timeout=10).even


def test_fill_in_form():
    registration_page = RegistrationPage()
    user = users.test_user
    browser.open('/automation-practice-form')

    registration_page.fill_first_name(user.first_name)
    registration_page.fill_last_name(user.last_name)
    registration_page.fill_gender(user.gender)

    registration_page.fill_phone_number(user.phone_number)
    registration_page.fill_email(user.email)

    registration_page.fill_hobby(user.hobby)

    registration_page.fill_current_address(user.current_address)
    registration_page.select_state(user.state)
    registration_page.select_city(user.city)

    registration_page.select_date_of_birth('May', '1999', 11)

    registration_page.fill_subject(user.subject)

    registration_page.upload_picture('resources/foto.png')

    registration_page.submit_data()

    registration_page.registered_user_data.should(
        have.exact_texts(
            'Olga YA',
            'name@example.com',
            'Female',
            '1234567891',
            '11 May,1999',
            'Computer Science',
            'Reading',
            'foto.png',
            'Moscowskaya Street 18',
            'NCR Delhi',
        )
    )
