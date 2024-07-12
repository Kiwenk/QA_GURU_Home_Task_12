from modules.registration_from import RegistrationForm
from modules.users import User


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
    form_action.open()
    form_action.register(human_being)
    form_action.table_check(human_being)
