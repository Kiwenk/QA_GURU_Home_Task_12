from selene import browser, have
from modules.users import User
from pathlib import Path


class RegistrationForm:
    def open(self):
        browser.open('automation-practice-form')  # исправил. С rc7 selene не работало почему то. Сейчас норм (rc2)

    def first_name(self, name):
        browser.element('#firstName').type(name)

    def last_name(self, second_name):
        browser.element('#lastName').type(second_name)

    def user_email(self, email):
        browser.element('#userEmail').type(email)

    def gender_radio(self):
        browser.element('[for="gender-radio-3"]').click()

    def user_number(self, number):
        browser.element('#userNumber').type(number)

    def date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('June')
        browser.element('.react-datepicker__year-select').type('2007')
        browser.element(
            f'.react-datepicker__day--0{16}:not(.react-datepicker__day--outside-month)'
        ).click()  # одолжил у коллег. Так работает)
        # browser.element('.react-datepicker__month').element('[aria-label="Choose Saturday, June 16th, 2007"]').click() у меня валится на таймауте, потому что не может найти элемент.

    def subjects(self, sub):
        browser.element('#subjectsInput').type(sub).press_enter()

    def hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_picture(self, photo):
        browser.element('#uploadPicture').send_keys(
            str(Path(__file__).parent.parent.joinpath(f'resources/{photo}')))  # исправил

    def current_address(self, address):
        browser.element("#currentAddress").type(address)

    def state(self, state):
        browser.element("#react-select-3-input").type(state).press_enter()

    def city(self, city):
        browser.element("#react-select-4-input").type(city).press_enter()

    def sumbit_button(self):
        browser.element("#submit").click()

    def check_text_after_submit_button(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def table_check(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.phone}',
            f'{user.birthday}',
            f'{user.subject}',
            f'{user.hobbies}',
            f'{user.photo}',
            f'{user.address}',
            f'{user.state} {user.city}'))

    def register(self, user: User):
        self.first_name(user.first_name)
        self.last_name(user.last_name)
        self.user_email(user.email)
        self.gender_radio()
        self.user_number(user.phone)
        self.date_of_birth()
        self.subjects(user.subject)
        self.hobbies()
        self.upload_picture(user.photo)
        self.current_address(user.address)
        self.state(user.state)
        self.city(user.city)
        self.sumbit_button()
