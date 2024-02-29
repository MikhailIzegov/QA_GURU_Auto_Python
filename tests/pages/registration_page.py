import allure
from selene import browser
from selene.support.shared import browser
from selene import have, be
from selene import command
import os
import tests
from tests.users_for_tests.users import test_user


class RegistrationPage:

    def open_page(self):
        browser.open('/automation-practice-form')
        browser.driver.maximize_window()

    def register(self, user):
        self.fill_first_name(test_user.first_name)
        self.fill_last_name(test_user.last_name)
        self.fill_gender(test_user.gender)
        self.fill_phone_number(test_user.phone_number)
        self.fill_email(test_user.email)
        self.fill_hobby()
        self.fill_current_address(test_user.current_address)
        self.select_state(test_user.state)
        self.select_city(test_user.city)
        self.select_date_of_birth()
        self.fill_subject(test_user.subject)
        self.upload_picture(test_user.photo)
        self.submit_data()

    def should_have_user(self, user):
        full_name = test_user.first_name + ' ' + test_user.last_name
        state_and_city = test_user.state + ' ' + test_user.city
        self.registered_user_data.should(have.exact_texts(
            full_name,
            test_user.email,
            test_user.gender,
            test_user.phone_number,
            test_user.date_of_birth.strftime('%d %B,%Y'),
            test_user.subject,
            test_user.hobbies_str,
            self.filename_picture(),
            test_user.current_address,
            state_and_city,
        )
        )

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

    def fill_hobby(self):
        browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view)
        hobby_values = [hobby.value for hobby in test_user.hobbies]  # Создаем список строк из объектов Hobby
        if 'Sports' in hobby_values:
            browser.element('[for="hobbies-checkbox-1"]').click()
        if 'Reading' in hobby_values:
            browser.element('[for="hobbies-checkbox-2"]').click()
        if 'Music' in hobby_values:
            browser.element('[for="hobbies-checkbox-3"]').click()

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

    def select_date_of_birth(self):
        day, month, year = test_user.date_of_birth.day, test_user.date_of_birth.strftime('%B'), test_user.date_of_birth.year
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
    def filename_picture(self):
        filename = os.path.basename(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'resources', 'foto.png'))
        return filename

    def submit_data(self):
        browser.element('#submit').press_enter()

    @property
    def registered_user_data(self):
        return browser.element('.table').all('td').with_(timeout=10).even

    def add_html(self):
        html = browser.driver.page_source
        allure.attach(body=html, name='page_source', attachment_type=allure.attachment_type.HTML, extension='.html')
