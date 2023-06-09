import allure
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import pytest

@allure.epic("Registration cases")
class TestUserRegister(BaseCase):
    @allure.title("Successful user creation")
    @allure.description("This test creates user and checks id in response")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_register.py",
                 name="<--Click to view code on GitHub")

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.title("Creating user with existing email")
    @allure.description("This test tries to create user using existing email and checks response message")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_register.py",
                 name="<--Click to view code on GitHub")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data = data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"

        #   --- Ex15: Тесты на метод user ---
        #       Создание пользователя с некорректным email - без символа @

    @allure.title("Creating user with incorrect email")
    @allure.description("This test tries to create user using wrong email format and checks response message")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_register.py",
                 name="<--Click to view code on GitHub")
    def test_create_user_with_incorrect_email(self):
        data = self.prepare_incorrect_email()           # метод добавлен в base_case.py

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response content {response.content}"

    exclude_params = ['password', 'username', 'firstName', 'lastName', 'email']

        #       Создание пользователя без указания одного из полей
    @allure.title("Creating user missing params")
    @allure.description("This test tries to create user missing required parameters and checks response message")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_register.py",
                 name="<--Click to view code on GitHub")
    @pytest.mark.parametrize('exclude_param', exclude_params)
    def test_create_user_missing_params(self, exclude_param):         # метод prepare_registration_data_missing_params добавлен в base_case.py
        data = self.prepare_registration_data_missing_params(exclude_param)

        response = MyRequests.post("/user/", data=data)
        '''print(data)
        print(response.status_code)
        print(response.content)'''
        Assertions.assert_code_status(response, 400)
        # <-- assert_response_match_content добавлен в assertions.py
        if exclude_param == 'password':
            Assertions.assert_response_match_content(response,f'The following required params are missed: password')
        elif exclude_param == 'username':
            Assertions.assert_response_match_content(response,f'The following required params are missed: username')
        elif exclude_param == 'firstName':
            Assertions.assert_response_match_content(response,f'The following required params are missed: firstName')
        elif exclude_param == 'lastName':
            Assertions.assert_response_match_content(response,f'The following required params are missed: lastName')
        elif exclude_param == 'email':
            Assertions.assert_response_match_content(response,f'The following required params are missed: email')

        #       Создание пользователя с очень коротким именем в один символ

    @allure.title("Creating user with too short name")
    @allure.description("This test tries to create user with 1-letter name and checks response message")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_register.py",
                 name="<--Click to view code on GitHub")
    def test_create_user_with_short_name(self):
        data = self.create_shortname_user()     # <-- метод create_shortname_user добавлен в base_case.py

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)                         # <-- assert_response_match_content добавлен в assertions.py
        Assertions.assert_response_match_content(response, f"The value of 'username' field is too short")

        #       Создание пользователя с очень длинным именем более 250 символов

    @allure.title("Creating user with extra long name")
    @allure.description("This test tries to create user with 251-letter name and checks response message")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_register.py",
                 name="<--Click to view code on GitHub")
    def test_create_user_with_extra_long_name(self):
        data = self.create_longname_user()     # <-- метод create_longname_user добавлен в base_case.py

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)                            # <-- assert_response_match_content добавлен в assertions.py
        Assertions.assert_response_match_content(response, f"The value of 'username' field is too long")

        #       Проверяем граничное значение длины имени

    @allure.title("Creating user with limited length name")
    @allure.description("This test boundary condition of user name length")
    @allure.link("https://github.com/andreyR-QA/Learn_Python_API/blob/main/tests/test_user_register.py",
                 name="<--Click to view code on GitHub")
    def test_create_user_with_limited_length_name(self):
        data = self.create_limited_length_name_user()     # <-- метод create_limited_length_name_user добавлен в base_case.py

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)                            # <-- assert_response_match_content добавлен в assertions.py
        Assertions.assert_json_has_key(response, "id")