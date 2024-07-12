import allure

from modules.registration_from import RegistrationForm
from modules.users import User

@allure.story("Пользователь регистриуется на DEMOQA")
@allure.feature('Регистрация')
@allure.link('http://demoqa.com/automation-practice-form')
@allure.description('Проверка регистрации на DEMOQA')
@allure.label('test_label')
@allure.tag('DEMOQA')
@allure.severity(allure.severity_level.CRITICAL)
def test_student_registration_form():
    form_action = RegistrationForm()
    human_being = User(first_name='Ivan',
                       last_name='Ivanov',
                       email='Vasya_the_terrible_2005@mail.ru',
                       gender='Other',
                       phone='1987198719',
                       birthday='16 June,2007',
                       subject='Computer Science',
                       photo='pic.jpg',
                       hobbies='Sports, Music',
                       address='Kyoto, Pushkin Street, 16',
                       state='Haryana',
                       city='Karnal')
    with allure.step('Открываем браузер'):
        form_action.open()

    with allure.step('Регистрация пользователя'):
        form_action.register(human_being)

    with allure.step('Проверяем данные пользователя'):
        form_action.table_check(human_being)
